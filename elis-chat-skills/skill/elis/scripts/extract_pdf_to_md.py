#!/usr/bin/env python3
"""
Extrai texto de PDF para Markdown usando pypdf.
"""
import argparse
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("Erro: Biblioteca 'pypdf' nao encontrada. Instale com: pip install pypdf")
    sys.exit(1)

def extract_pdf_to_markdown(input_path: Path) -> str:
    try:
        reader = PdfReader(input_path)
    except Exception as e:
        raise RuntimeError(f"Falha ao abrir PDF com pypdf: {e}")

    meta = reader.metadata
    
    lines = [
        "> [EXTRACTION] backend=pypdf",
        f"> [SOURCE] {input_path.name}",
    ]
    
    if meta:
        try:
            if meta.title:
                lines.append(f"> [TITLE] {meta.title}")
            if meta.author:
                lines.append(f"> [AUTHOR] {meta.author}")
        except:
            pass # Ignora erros de codificacao em metadados
    
    lines.append("") # Linha em branco apos cabecalho

    total_pages = len(reader.pages)
    print(f"Processando {total_pages} paginas...")

    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text()
            if text:
                lines.append(text)
                lines.append("") # Linha vazia entre paginas
        except Exception as e:
            print(f"Aviso: Erro ao extrair texto da pagina {i+1}: {e}")
            continue

    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Extrai texto de PDF para Markdown usando pypdf.")
    parser.add_argument("--input", required=True, help="Arquivo PDF de entrada")
    parser.add_argument("--output", required=True, help="Arquivo Markdown de saida")
    
    args = parser.parse_args()
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()

    if not input_path.exists():
        print(f"Erro: arquivo nao encontrado: {input_path}")
        sys.exit(1)
        
    try:
        content = extract_pdf_to_markdown(input_path)
        if not content.strip():
             print("Aviso: Nenhum texto foi extraido do PDF. O arquivo pode ser uma imagem (escaneado).")
             
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        print(f"Sucesso: {output_path}")
    except Exception as e:
        print(f"Erro fatal ao processar PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
