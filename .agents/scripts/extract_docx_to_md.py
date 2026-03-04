#!/usr/bin/env python3
"""
Extract text from DOCX into Markdown without external dependencies.
"""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path
from typing import Iterable, List
from xml.etree import ElementTree as ET

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def qn(tag: str) -> str:
    prefix, local = tag.split(":")
    return f"{{{NS[prefix]}}}{local}"


def normalize_spaces(value: str) -> str:
    value = value.replace("\r", "\n")
    value = re.sub(r"[ \t]+\n", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    value = re.sub(r"[ \t]{2,}", " ", value)
    return value.strip()


def text_from_run_container(node: ET.Element) -> str:
    parts: List[str] = []
    for child in node.iter():
        if child.tag == qn("w:t"):
            parts.append(child.text or "")
        elif child.tag == qn("w:tab"):
            parts.append("\t")
        elif child.tag in {qn("w:br"), qn("w:cr")}:
            parts.append("\n")
    return "".join(parts)


def paragraph_to_md(paragraph: ET.Element) -> str:
    raw = text_from_run_container(paragraph)
    text = normalize_spaces(raw)
    if not text:
        return ""

    ppr = paragraph.find("w:pPr", NS)
    is_list = ppr is not None and ppr.find("w:numPr", NS) is not None
    if is_list:
        return f"- {text}"
    return text


def table_to_md(table: ET.Element) -> List[str]:
    rows: List[List[str]] = []
    for row in table.findall("w:tr", NS):
        cells: List[str] = []
        for cell in row.findall("w:tc", NS):
            cell_text_parts = []
            for p in cell.findall("w:p", NS):
                item = paragraph_to_md(p)
                if item:
                    if item.startswith("- "):
                        item = item[2:]
                    cell_text_parts.append(item)
            cells.append(" ".join(cell_text_parts).strip())
        if any(cells):
            rows.append(cells)

    if not rows:
        return []

    col_count = max(len(r) for r in rows)
    normalized = [r + [""] * (col_count - len(r)) for r in rows]

    header = normalized[0]
    body = normalized[1:] if len(normalized) > 1 else []

    lines = []
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * col_count) + " |")
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def extract_main_part(root: ET.Element) -> List[str]:
    lines: List[str] = []

    body = root.find("w:body", NS)
    if body is None:
        return lines

    for child in list(body):
        if child.tag == qn("w:p"):
            text = paragraph_to_md(child)
            if text:
                lines.append(text)
                lines.append("")
        elif child.tag == qn("w:tbl"):
            table_lines = table_to_md(child)
            if table_lines:
                lines.extend(table_lines)
                lines.append("")

    return lines


def extract_simple_part(root: ET.Element, title: str) -> List[str]:
    lines: List[str] = []
    content: List[str] = []
    for child in list(root):
        if child.tag == qn("w:p"):
            text = paragraph_to_md(child)
            if text:
                content.append(text)
        elif child.tag == qn("w:tbl"):
            content.extend(table_to_md(child))

    if content:
        lines.append(f"## {title}")
        lines.append("")
        lines.extend(content)
        lines.append("")
    return lines


def extract_notes(root: ET.Element, note_tag: str, title: str) -> List[str]:
    lines: List[str] = []
    entries: List[str] = []

    for note in root.findall(f"w:{note_tag}", NS):
        note_id = note.get(qn("w:id"))
        if note_id in {"-1", "0"}:
            continue
        text_parts: List[str] = []
        for paragraph in note.findall("w:p", NS):
            text = paragraph_to_md(paragraph)
            if text:
                text_parts.append(text)
        joined = " ".join(text_parts).strip()
        if joined:
            if note_id is None:
                entries.append(f"- {joined}")
            else:
                entries.append(f"- [{note_id}] {joined}")

    if entries:
        lines.append(f"## {title}")
        lines.append("")
        lines.extend(entries)
        lines.append("")
    return lines


def read_xml_from_zip(docx_path: Path, member: str) -> ET.Element | None:
    try:
        with zipfile.ZipFile(docx_path, "r") as zf:
            data = zf.read(member)
    except KeyError:
        return None
    return ET.fromstring(data)


def list_members(docx_path: Path) -> Iterable[str]:
    with zipfile.ZipFile(docx_path, "r") as zf:
        return list(zf.namelist())


def extract_docx_to_markdown(input_path: Path) -> str:
    members = list_members(input_path)

    lines: List[str] = [
        "> [EXTRACTION] backend=docx-stdlib",
        f"> [SOURCE] {input_path.name}",
        "",
    ]

    main_root = read_xml_from_zip(input_path, "word/document.xml")
    if main_root is None:
        raise RuntimeError("Arquivo DOCX invalido: word/document.xml ausente.")
    lines.extend(extract_main_part(main_root))

    header_members = sorted(m for m in members if m.startswith("word/header") and m.endswith(".xml"))
    for i, member in enumerate(header_members, start=1):
        root = read_xml_from_zip(input_path, member)
        if root is not None:
            lines.extend(extract_simple_part(root, f"Cabecalho {i}"))

    footer_members = sorted(m for m in members if m.startswith("word/footer") and m.endswith(".xml"))
    for i, member in enumerate(footer_members, start=1):
        root = read_xml_from_zip(input_path, member)
        if root is not None:
            lines.extend(extract_simple_part(root, f"Rodape {i}"))

    footnotes_root = read_xml_from_zip(input_path, "word/footnotes.xml")
    if footnotes_root is not None:
        lines.extend(extract_notes(footnotes_root, "footnote", "Notas de rodape"))

    endnotes_root = read_xml_from_zip(input_path, "word/endnotes.xml")
    if endnotes_root is not None:
        lines.extend(extract_notes(endnotes_root, "endnote", "Notas finais"))

    body = "\n".join(lines).strip() + "\n"
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extrai texto de DOCX para Markdown.")
    parser.add_argument("--input", required=True, help="Arquivo .docx de entrada")
    parser.add_argument("--output", required=True, help="Arquivo .md de saida")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()

    if not input_path.exists():
        print(f"Erro: arquivo nao encontrado: {input_path}")
        return 1
    if input_path.suffix.lower() != ".docx":
        print("Erro: arquivo de entrada precisa ser .docx")
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    markdown = extract_docx_to_markdown(input_path)
    output_path.write_text(markdown, encoding="utf-8")
    print(str(output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
