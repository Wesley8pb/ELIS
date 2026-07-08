#!/usr/bin/env python3
"""
build.py — Gera o ELIS como UM ÚNICO skill para a interface de chat do claude.ai.

O claude.ai aceita um skill por zip (o zip contém a pasta do skill com SKILL.md).
Não é possível empacotar vários skills num único zip. Portanto, para entregar um
ÚNICO pacote, consolidamos todo o ELIS em um só skill `elis`, no qual cada etapa
vira um arquivo interno carregado sob demanda (padrão de "progressive disclosure",
igual à skill de PDF da Anthropic: SKILL.md + arquivos de referência).

Fonte única: ../elis-plugin/skills (o plugin do Claude Code / Cowork).

Estrutura gerada:

  skill/elis/
  ├── SKILL.md                 (orquestrador; frontmatter name: elis)
  ├── etapas/
  │   ├── 1-analise-firac.md
  │   ├── 1.5-liminar-rp.md
  │   ├── 2-deliberacao.md
  │   ├── 3-arquitetura.md
  │   ├── 4-sentenca.md
  │   ├── conversao-arquivos.md
  │   └── templates-sentenca.md
  ├── reference/liminar-rp.md  (referência da tutela de urgência)
  ├── INDICE-TEMPLATES.md      (índice dos 15 templates)
  ├── templates/               (15 templates)
  └── scripts/                 (conversores PDF/DOCX)

Saída: dist/elis.zip  (um único arquivo para upload em Configurações → Recursos)

Uso:  python3 build.py
"""

import os
import re
import shutil
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "elis-plugin", "skills"))
OUT = os.path.join(HERE, "skill", "elis")
DIST = os.path.join(HERE, "dist")

# Skill do plugin -> arquivo de etapa dentro do skill único
ETAPA_FILE = {
    "etapa1-analise-firac": "etapas/1-analise-firac.md",
    "etapa1-5-liminar-rp": "etapas/1.5-liminar-rp.md",
    "etapa2-deliberacao": "etapas/2-deliberacao.md",
    "etapa3-arquitetura": "etapas/3-arquitetura.md",
    "etapa4-sentenca": "etapas/4-sentenca.md",
    "conversao-arquivos": "etapas/conversao-arquivos.md",
    "templates-sentenca": "etapas/templates-sentenca.md",
}

# Referências a "skill X" (por nome de máquina) -> arquivo interno correspondente
NAME2PATH = {
    "etapa1-analise-firac": "etapas/1-analise-firac.md",
    "etapa1-5-liminar-rp": "etapas/1.5-liminar-rp.md",
    "etapa2-deliberacao": "etapas/2-deliberacao.md",
    "etapa3-arquitetura": "etapas/3-arquitetura.md",
    "etapa4-sentenca": "etapas/4-sentenca.md",
    "conversao-arquivos": "etapas/conversao-arquivos.md",
    "templates-sentenca": "etapas/templates-sentenca.md",
}

# Comandos slash (Claude Code) -> frases de linguagem natural (chat)
SLASH = {
    "iniciar": "faça a engenharia de contexto do processo",
    "etapa1": "iniciar a Etapa 1",
    "liminar": "analise o pedido liminar",
    "etapa2": "prossiga para a Etapa 2",
    "etapa3": "prossiga para a Etapa 3",
    "etapa4": "prossiga para a Etapa 4",
    "finalizar": "finalize o processo",
}

ORCHESTRATOR_FRONTMATTER = """---
name: elis
description: >-
  ELIS — assistente de direito eleitoral brasileiro. Fluxo completo de engenharia
  de contexto para sentenças eleitorais, em etapas: análise FIRAC+, tutela de
  urgência (liminar em RP), deliberação, arquitetura da sentença e sentença final,
  além de conversão de documentos e 15 templates. Acionar quando o usuário disser
  "faça a engenharia de contexto do processo", "analise o pedido liminar" ou
  "execute a tutela de urgência", pedir análise, deliberação, plano ou minuta de
  sentença eleitoral, ou mencionar processos das classes AIJE, AIME, AIRC, RP,
  RPEsp, PCE, RCED ou ação penal eleitoral. As instruções de cada etapa estão nos
  arquivos em etapas/; leia o arquivo da etapa correspondente quando ela for
  acionada.
---
"""

STRUCTURE_NOTE = """
> **Estrutura deste pacote (claude.ai):** este é um único skill que contém todo o
> ELIS. As instruções detalhadas de cada etapa ficam em arquivos separados,
> carregados sob demanda. Ao acionar uma etapa, **leia o arquivo correspondente**:
>
> | Etapa | Arquivo a ler |
> |-------|---------------|
> | 1 — Análise FIRAC+ | `etapas/1-analise-firac.md` |
> | 1.5 — Tutela de urgência (RP) | `etapas/1.5-liminar-rp.md` (+ `reference/liminar-rp.md`) |
> | 2 — Deliberação | `etapas/2-deliberacao.md` |
> | 3 — Arquitetura da sentença | `etapas/3-arquitetura.md` |
> | 4 — Sentença final | `etapas/4-sentenca.md` |
> | Conversão de arquivos | `etapas/conversao-arquivos.md` (scripts em `scripts/`) |
> | Templates | `etapas/templates-sentenca.md` (índice em `INDICE-TEMPLATES.md`, modelos em `templates/`) |
>
> Os documentos do processo e os artefatos (`CONTEXTO/`, `PROCESSOS CONCLUIDOS/`,
> `TEMPLATES/`) ficam na área de trabalho da conversa. Para converter PDF/DOCX,
> anexar o documento diretamente à conversa costuma bastar — o Claude lê esses
> formatos nativamente.
"""


def strip_frontmatter(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    return text[m.end():] if m else text


def rewrite(text: str, is_liminar: bool = False, is_templates: bool = False) -> str:
    # 1) Comandos slash -> linguagem natural
    text = re.sub(
        r"/elis:(" + "|".join(map(re.escape, SLASH)) + r")",
        lambda m: SLASH[m.group(1)],
        text,
    )
    # 2) Caminhos ${CLAUDE_PLUGIN_ROOT} específicos -> caminhos internos do skill
    text = text.replace(
        "${CLAUDE_PLUGIN_ROOT}/skills/etapa1-5-liminar-rp/reference.md",
        "reference/liminar-rp.md",
    )
    text = text.replace(
        "${CLAUDE_PLUGIN_ROOT}/skills/conversao-arquivos/scripts/", "scripts/"
    )
    text = text.replace(
        "${CLAUDE_PLUGIN_ROOT}/skills/templates-sentenca/templates/", "templates/"
    )
    text = text.replace(
        "${CLAUDE_PLUGIN_ROOT}/skills/templates-sentenca/INDICE.md",
        "INDICE-TEMPLATES.md",
    )
    # 3) Prefixo ${CLAUDE_PLUGIN_ROOT}/skills/<x>/ remanescente -> relativo
    text = re.sub(r"\$\{CLAUDE_PLUGIN_ROOT\}/skills/[a-z0-9.-]+/", "", text)
    text = text.replace("${CLAUDE_PLUGIN_ROOT}", ".")
    # 4) Remover namespace `elis:`
    text = text.replace("elis:", "")
    # 5) Referências a skill (por nome) -> arquivo interno da etapa
    for name, path in NAME2PATH.items():
        text = text.replace(name, path)
    # 6) Suavizar frases "skill `etapas/...`" -> "instruções em `etapas/...`"
    text = text.replace("a skill `etapas/", "as instruções em `etapas/")
    text = text.replace("à skill `etapas/", "às instruções em `etapas/")
    text = text.replace("skill `etapas/", "instruções em `etapas/")
    text = text.replace("invocar as instruções", "consultar as instruções")
    text = text.replace("invoque as instruções", "consulte as instruções")
    # 7) Ajustes específicos
    if is_liminar:
        text = text.replace("reference.md", "reference/liminar-rp.md")
    if is_templates:
        text = text.replace("INDICE.md", "INDICE-TEMPLATES.md")
    return text


def build_orchestrator() -> None:
    body = open(os.path.join(SRC, "fluxo-elis", "SKILL.md"), encoding="utf-8").read()
    body = strip_frontmatter(body)
    body = rewrite(body)
    # Relabels da tabela de etapas (agora apontam para arquivos, não skills)
    body = body.replace("- **Skill**:", "- **Instruções**:")
    body = body.replace("| **Comando**:", "| **Como pedir**:")
    # Monta SKILL.md: frontmatter curado + nota de estrutura + corpo do orquestrador
    lines = body.splitlines()
    # Insere a nota de estrutura logo após o primeiro título de nível 1
    out, inserted = [], False
    for ln in lines:
        out.append(ln)
        if not inserted and ln.startswith("# "):
            out.append(STRUCTURE_NOTE)
            inserted = True
    content = ORCHESTRATOR_FRONTMATTER + "\n" + "\n".join(out).rstrip() + "\n"
    with open(os.path.join(OUT, "SKILL.md"), "w", encoding="utf-8") as fh:
        fh.write(content)


def build_etapas() -> None:
    os.makedirs(os.path.join(OUT, "etapas"), exist_ok=True)
    for skill, dest in ETAPA_FILE.items():
        text = open(os.path.join(SRC, skill, "SKILL.md"), encoding="utf-8").read()
        text = strip_frontmatter(text)
        text = rewrite(
            text,
            is_liminar=(skill == "etapa1-5-liminar-rp"),
            is_templates=(skill == "templates-sentenca"),
        )
        title = "# ELIS — %s\n\n" % os.path.basename(dest)
        with open(os.path.join(OUT, dest), "w", encoding="utf-8") as fh:
            fh.write(text.lstrip())


def build_resources() -> None:
    # Referência da tutela de urgência
    os.makedirs(os.path.join(OUT, "reference"), exist_ok=True)
    ref = open(
        os.path.join(SRC, "etapa1-5-liminar-rp", "reference.md"), encoding="utf-8"
    ).read()
    with open(os.path.join(OUT, "reference", "liminar-rp.md"), "w", encoding="utf-8") as fh:
        fh.write(ref)  # referência jurídica: copiada como está
    # Índice de templates (na raiz do skill; links `templates/...` resolvem daqui)
    idx = open(
        os.path.join(SRC, "templates-sentenca", "INDICE.md"), encoding="utf-8"
    ).read()
    idx = rewrite(idx, is_templates=True)
    with open(os.path.join(OUT, "INDICE-TEMPLATES.md"), "w", encoding="utf-8") as fh:
        fh.write(idx)
    # Templates (copiados como estão)
    dst_t = os.path.join(OUT, "templates")
    shutil.copytree(os.path.join(SRC, "templates-sentenca", "templates"), dst_t)
    # Scripts de conversão (copiados como estão)
    dst_s = os.path.join(OUT, "scripts")
    shutil.copytree(os.path.join(SRC, "conversao-arquivos", "scripts"), dst_s)


def zip_skill() -> str:
    os.makedirs(DIST, exist_ok=True)
    zip_path = os.path.join(DIST, "elis.zip")
    root = os.path.dirname(OUT)  # .../skill  -> zip conterá "elis/..."
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for base, _dirs, files in os.walk(OUT):
            for fn in sorted(files):
                abs_f = os.path.join(base, fn)
                zf.write(abs_f, os.path.relpath(abs_f, root))
    return zip_path


def main() -> None:
    if os.path.exists(os.path.join(HERE, "skill")):
        shutil.rmtree(os.path.join(HERE, "skill"))
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(OUT)
    build_orchestrator()
    build_etapas()
    build_resources()
    z = zip_skill()
    nfiles = sum(len(f) for _r, _d, f in os.walk(OUT))
    print("Skill único 'elis' gerado com %d arquivos." % nfiles)
    print("Pacote: %s" % os.path.relpath(z, HERE))


if __name__ == "__main__":
    main()
