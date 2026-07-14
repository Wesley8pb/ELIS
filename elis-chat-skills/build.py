#!/usr/bin/env python3
"""
build.py — Gera o ELIS como UM ÚNICO skill, SIMPLIFICADO para o chat do claude.ai.

Diferente do plugin do Claude Code (../elis-plugin/), a versão de chat NÃO tem
camada de sistema de arquivos:

  - Sem conversão de arquivos (o claude.ai lê PDF/DOCX de anexos nativamente).
  - Sem pastas CONTEXTO/, PROCESSOS CONCLUIDOS/ nem TEMPLATES/ local.
  - Sem etapa de finalização/arquivamento.
  - Entradas = anexos da conversa. Saídas = Artefatos.

Todo o ELIS fica em um só skill `elis`; cada etapa é um arquivo interno em
etapas/, carregado sob demanda. Fonte única: ../elis-plugin/skills.

Saída: dist/elis.zip

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

# Skill do plugin -> arquivo de etapa (conversao-arquivos é omitido de propósito)
ETAPA_FILE = {
    "etapa1-analise-firac": "etapas/1-analise-firac.md",
    "etapa1-5-liminar-rp": "etapas/1.5-liminar-rp.md",
    "etapa2-deliberacao": "etapas/2-deliberacao.md",
    "etapa3-arquitetura": "etapas/3-arquitetura.md",
    "etapa4-sentenca": "etapas/4-sentenca.md",
    "templates-sentenca": "etapas/templates-sentenca.md",
}

NAME2PATH = {
    "etapa1-analise-firac": "etapas/1-analise-firac.md",
    "etapa1-5-liminar-rp": "etapas/1.5-liminar-rp.md",
    "etapa2-deliberacao": "etapas/2-deliberacao.md",
    "etapa3-arquitetura": "etapas/3-arquitetura.md",
    "etapa4-sentenca": "etapas/4-sentenca.md",
    "conversao-arquivos": "etapas/conversao-arquivos.md",  # só para limpar refs
    "templates-sentenca": "etapas/templates-sentenca.md",
}

SLASH = {
    "iniciar": "faça a engenharia de contexto do processo",
    "etapa1": "iniciar a Etapa 1",
    "liminar": "analise o pedido liminar",
    "etapa2": "prossiga para a Etapa 2",
    "etapa3": "prossiga para a Etapa 3",
    "etapa4": "prossiga para a Etapa 4",
    "finalizar": "finalize o processo",
}

# Título do Artefato + sugestão de próxima etapa, por arquivo
TRAILER = {
    "etapas/1-analise-firac.md": (
        "ELIS — Análise FIRAC+",
        "Se a classe for **RP** com pedido de tutela de urgência, ofereça a "
        "Etapa 1.5 (leia `etapas/1.5-liminar-rp.md`). Caso contrário, sugira a "
        "**Etapa 2 (Deliberação)** — o usuário pode dizer *\"prossiga para a Etapa 2\"*.",
    ),
    "etapas/1.5-liminar-rp.md": (
        "ELIS — Decisão Liminar (RP)",
        "Pergunte se o usuário deseja seguir para a **Etapa 2 (Deliberação)** ou "
        "diretamente para a **Etapa 3 (Arquitetura)**.",
    ),
    "etapas/2-deliberacao.md": (
        "ELIS — Deliberação",
        "Ofereça a análise pelo **julgamento oposto**, se desejar, e sugira a "
        "**Etapa 3 (Arquitetura da Sentença)** — *\"prossiga para a Etapa 3\"*.",
    ),
    "etapas/3-arquitetura.md": (
        "ELIS — Arquitetura da Sentença",
        "Sugira a **Etapa 4 (Sentença Final)** — *\"prossiga para a Etapa 4\"*.",
    ),
    "etapas/4-sentenca.md": (
        "ELIS — Sentença Final",
        "Para reaproveitar a sentença como modelo, veja `etapas/templates-sentenca.md` "
        "— o template é entregue como um **novo Artefato**.",
    ),
}

ORCHESTRATOR_FRONTMATTER = """---
name: elis
description: >-
  ELIS — assistente de direito eleitoral brasileiro. Fluxo completo de engenharia
  de contexto para sentenças eleitorais, em etapas: análise FIRAC+, tutela de
  urgência (liminar em RP), deliberação, arquitetura da sentença e sentença final,
  com 15 templates de apoio. Acionar quando o usuário disser "faça a engenharia de
  contexto do processo", "analise o pedido liminar" ou "execute a tutela de
  urgência", pedir análise, deliberação, plano ou minuta de sentença eleitoral, ou
  mencionar processos das classes AIJE, AIME, AIRC, RP, RPEsp, PCE, RCED ou ação
  penal eleitoral. Os documentos do processo chegam como anexos; cada etapa é
  entregue como um Artefato. As instruções de cada etapa estão nos arquivos em
  etapas/; leia o arquivo da etapa correspondente quando ela for acionada.
---
"""

STRUCTURE_NOTE = """
> **Como este pacote funciona (claude.ai):** este é um único skill que contém todo
> o ELIS. As instruções de cada etapa ficam em arquivos separados, carregados sob
> demanda. Ao acionar uma etapa, **leia o arquivo correspondente**:
>
> | Etapa | Arquivo a ler |
> |-------|---------------|
> | 1 — Análise FIRAC+ | `etapas/1-analise-firac.md` |
> | 1.5 — Tutela de urgência (RP) | `etapas/1.5-liminar-rp.md` (+ `reference/liminar-rp.md`) |
> | 2 — Deliberação | `etapas/2-deliberacao.md` |
> | 3 — Arquitetura da sentença | `etapas/3-arquitetura.md` |
> | 4 — Sentença final | `etapas/4-sentenca.md` |
> | Templates | `etapas/templates-sentenca.md` (índice em `INDICE-TEMPLATES.md`, modelos em `templates/`) |
>
> **Entradas** = anexos da conversa. **Saídas** = **Artefatos** (documentos na
> lateral do chat). Não há pastas, conversão de arquivos nem finalização: o
> histórico da própria conversa é o registro do processo.
"""

NEW_INICIALIZACAO = """## Inicialização

Ao ser acionado, **antes de qualquer ação**:

1. Verificar os **anexos** da conversa (peças do processo).
2. Verificar se já há etapas concluídas antes nesta conversa (mensagens e artefatos anteriores).
3. Se houver processo em andamento → informar a última etapa concluída e perguntar como prosseguir.
4. Se não houver anexos e o usuário não os mencionou → **solicitar os documentos antes de prosseguir**.

**Comando de ativação**: `"Faça a engenharia de contexto do processo [REFERÊNCIA]"`
"""

NEW_ENTRADAS = """## Entradas e saídas

- **Entradas**: os documentos do processo chegam como **anexos** na conversa. Leia-os integralmente (o Claude lê PDF e DOCX nativamente — não é preciso converter).
- **Saídas**: cada etapa é entregue como um **Artefato** (documento na lateral do chat).
- Não há sistema de arquivos, pastas de contexto, arquivamento ou finalização: o histórico da conversa (mensagens e artefatos anteriores) é o contexto do processo.
"""

NEW_TITULOS = """## Títulos dos Artefatos

Use títulos claros e estáveis para o artefato de cada etapa:

| Etapa | Título do Artefato |
|-------|--------------------|
| 1 | ELIS — Análise FIRAC+ |
| 1.5 | ELIS — Decisão Liminar (RP) |
| 2 | ELIS — Deliberação |
| 3 | ELIS — Arquitetura da Sentença |
| 4 | ELIS — Sentença Final |
"""

TEMPLATES_ONDE = """## Biblioteca de templates

Os **15 templates** ficam em `templates/`, com índice em `INDICE-TEMPLATES.md` (ambos empacotados neste skill, somente leitura).

- **Usar um template**: consulte `INDICE-TEMPLATES.md` e leia `templates/<nome>.md`.
- **Criar um novo template**: gere-o como um **Artefato** (não há pasta local para gravar).
"""


def strip_frontmatter(text):
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    return text[m.end():] if m else text


def rewrite(text):
    """Transformações de caminho/comando/namespace (comuns a todos os arquivos)."""
    text = re.sub(
        r"/elis:(" + "|".join(map(re.escape, SLASH)) + r")",
        lambda m: SLASH[m.group(1)],
        text,
    )
    text = text.replace(
        "${CLAUDE_PLUGIN_ROOT}/skills/etapa1-5-liminar-rp/reference.md",
        "reference/liminar-rp.md",
    )
    text = text.replace(
        "${CLAUDE_PLUGIN_ROOT}/skills/templates-sentenca/templates/", "templates/"
    )
    text = text.replace(
        "${CLAUDE_PLUGIN_ROOT}/skills/templates-sentenca/INDICE.md",
        "INDICE-TEMPLATES.md",
    )
    text = re.sub(r"\$\{CLAUDE_PLUGIN_ROOT\}/skills/[a-z0-9.-]+/", "", text)
    text = text.replace("${CLAUDE_PLUGIN_ROOT}", ".")
    text = text.replace("elis:", "")
    for name, path in NAME2PATH.items():
        text = text.replace(name, path)
    text = text.replace("a skill `etapas/", "as instruções em `etapas/")
    text = text.replace("à skill `etapas/", "às instruções em `etapas/")
    text = text.replace("skill `etapas/", "instruções em `etapas/")
    text = text.replace("invocar as instruções", "consultar as instruções")
    text = text.replace("invoque as instruções", "consulte as instruções")
    return text


def chat_simplify(text):
    """Remove a camada de filesystem/conversão do texto (específico do chat)."""
    text = text.replace("INDICE.md", "INDICE-TEMPLATES.md")
    # Referências a materiais das etapas anteriores
    text = text.replace("disponíveis em `CONTEXTO/`", "produzidas anteriormente nesta conversa")
    text = re.sub(r"\(`CONTEXTO/[^`]+`\)", "(das etapas anteriores desta conversa)", text)
    text = text.replace("em `CONTEXTO/`", "nesta conversa")
    text = text.replace("(templates embarcados no plugin + TEMPLATES/ local)", "(os 15 templates deste skill)")
    text = text.replace(" + TEMPLATES/ local", "")
    # Saídas em pastas -> Artefato
    text = re.sub(r"\*\*Saída\*\*: `CONTEXTO/[^`]+`", "**Saída**: um **Artefato**", text)
    # Menções à pasta TEMPLATES/ local
    text = text.replace(" e a pasta `TEMPLATES/` local da área de trabalho (se existir)", "")
    text = text.replace(
        "os dois locais**: o índice embarcado (`INDICE-TEMPLATES.md` nesta skill) "
        "e a pasta `TEMPLATES/` local (com seu `INDICE-TEMPLATES.md`, se existir).",
        "o índice `INDICE-TEMPLATES.md` deste skill.",
    )
    text = text.replace(
        " + `TEMPLATES/INDICE-TEMPLATES.md` local, se existir): identificar",
        "): identificar",
    )
    text = text.replace("; local: `TEMPLATES/<nome>.md`", "")
    text = text.replace(
        "**SALVAR** em `TEMPLATES/` (pasta de trabalho) com a nomenclatura padrão.",
        "**GERAR** o template como um **Artefato**, com a nomenclatura padrão no título.",
    )
    text = text.replace(
        "**SALVAR** em `TEMPLATES/` (pasta de trabalho) com a nomenclatura padrão",
        "**GERAR** o template como um **Artefato**",
    )
    text = text.replace("**SALVAR** e **INDEXAR** conforme Fluxo 1.", "**GERAR** o template como um **Artefato** (ver Fluxo 1).")
    text = re.sub(r"\n\d+\.\s+\*\*ATUALIZAR\*\* o índice local `TEMPLATES/INDICE-TEMPLATES.md`[^\n]*", "", text)
    text = text.replace("gravar em `TEMPLATES/` do workspace do usuário", "gerar como um novo Artefato")
    text = text.replace("**SALVAR** em `TEMPLATES/` da pasta de trabalho (o diretório do plugin instalado é somente leitura)", "**GERAR** como um novo Artefato")
    text = text.replace("**ATUALIZAR** o índice local `TEMPLATES/INDICE-TEMPLATES.md` (criar se não existir)", "Manter a nomenclatura padrão no título do Artefato")
    text = text.replace("gravar em `TEMPLATES/`", "gerar como Artefato")
    text = text.replace("`TEMPLATES/INDICE-TEMPLATES.md`", "o índice deste skill")
    text = text.replace("`TEMPLATES/<nome>.md`", "os modelos deste skill")
    text = text.replace("`TEMPLATES/`", "a biblioteca deste skill")
    return text


def cut_from(text, *headers):
    idxs = [text.find(h) for h in headers if text.find(h) != -1]
    return (text[: min(idxs)].rstrip() + "\n") if idxs else text


def remove_section(text, header, level):
    out, skipping = [], False
    for ln in text.split("\n"):
        if not skipping and ln.rstrip() == header:
            skipping = True
            continue
        if skipping:
            if ln.startswith("#") and (len(ln) - len(ln.lstrip("#"))) <= level:
                skipping = False
                out.append(ln)
            continue
        out.append(ln)
    return "\n".join(out)


def replace_section(text, header, level, new_block):
    out, skipping, done = [], False, False
    for ln in text.split("\n"):
        if not skipping and not done and ln.rstrip() == header:
            skipping = True
            out.append(new_block.rstrip() + "\n")  # linha em branco antes do próximo cabeçalho
            done = True
            continue
        if skipping:
            if ln.startswith("#") and (len(ln) - len(ln.lstrip("#"))) <= level:
                skipping = False
                out.append(ln)
            continue
        out.append(ln)
    return "\n".join(out)


def build_orchestrator():
    body = strip_frontmatter(open(os.path.join(SRC, "fluxo-elis", "SKILL.md"), encoding="utf-8").read())
    body = rewrite(body)
    body = chat_simplify(body)
    # Cirurgia de seções para o chat
    body = replace_section(body, "## Área de trabalho", 2, NEW_ENTRADAS)
    body = replace_section(body, "## Inicialização", 2, NEW_INICIALIZACAO)
    body = replace_section(body, "## Nomenclatura dos Arquivos", 2, NEW_TITULOS)
    body = remove_section(body, "### Fase 0: Preparação", 3)
    body = remove_section(body, "## Finalização", 2)
    # Regra fundamental 9 (limpeza/arquivamento) -> Artefatos
    body = body.replace(
        "9. **Limpar a área de trabalho** após finalizar e mover para `PROCESSOS CONCLUIDOS/`.",
        "9. **Entregar cada etapa como um Artefato**; o histórico da conversa é o registro do processo.",
    )
    # Ajustes de linguagem (skill único, sem finalização)
    body = body.replace("saber qual skill acionar em cada momento", "saber qual etapa acionar em cada momento")
    body = body.replace(
        "- Ao concluir: oferecer `finalize o processo`.",
        "- Ao concluir: oferecer ajustes e, opcionalmente, gerar um template a partir da sentença.",
    )
    # Rótulos da tabela de etapas
    body = body.replace("- **Skill**:", "- **Instruções**:").replace("| **Comando**:", "| **Como pedir**:")
    # Remover a linha "Finalizar" dos Comandos Rápidos
    body = re.sub(r"\n\| Finalizar \|[^\n]*", "", body)
    # Inserir a nota de estrutura após o primeiro título nível 1
    out, inserted = [], False
    for ln in body.splitlines():
        out.append(ln)
        if not inserted and ln.startswith("# "):
            out.append(STRUCTURE_NOTE)
            inserted = True
    content = ORCHESTRATOR_FRONTMATTER + "\n" + "\n".join(out).rstrip() + "\n"
    open(os.path.join(OUT, "SKILL.md"), "w", encoding="utf-8").write(content)


def build_etapas():
    os.makedirs(os.path.join(OUT, "etapas"), exist_ok=True)
    for skill, dest in ETAPA_FILE.items():
        text = strip_frontmatter(open(os.path.join(SRC, skill, "SKILL.md"), encoding="utf-8").read())
        text = rewrite(text)
        text = chat_simplify(text)
        if skill == "templates-sentenca":
            text = replace_section(text, "## Onde os templates vivem", 2, TEMPLATES_ONDE)
            text = text.replace("reference.md", "reference/liminar-rp.md") if False else text
        else:
            # Remover trailer de filesystem e anexar trailer de chat (Artefato)
            text = cut_from(
                text,
                "## ARQUIVO DE SAÍDA",
                "## Arquivo de Saída",
                "## AO CONCLUIR ESTA ETAPA",
                "## 📄 SALVAR COMO TEMPLATE",
            )
            title, nxt = TRAILER[dest]
            text += (
                "\n\n## Entrega desta etapa (Artefato)\n\n"
                "Apresente o resultado como um **Artefato** intitulado **\"%s\"**. "
                "Ao final, inclua o aviso obrigatório de IA generativa.\n\n"
                "Em seguida:\n"
                "1. Pergunte ao usuário se deseja **ajustes**.\n"
                "2. %s\n" % (title, nxt)
            )
        if skill == "etapa1-5-liminar-rp":
            text = text.replace("reference.md", "reference/liminar-rp.md")
        open(os.path.join(OUT, dest), "w", encoding="utf-8").write(text.lstrip())


def build_resources():
    os.makedirs(os.path.join(OUT, "reference"), exist_ok=True)
    ref = open(os.path.join(SRC, "etapa1-5-liminar-rp", "reference.md"), encoding="utf-8").read()
    open(os.path.join(OUT, "reference", "liminar-rp.md"), "w", encoding="utf-8").write(ref)
    idx = chat_simplify(rewrite(open(os.path.join(SRC, "templates-sentenca", "INDICE.md"), encoding="utf-8").read()))
    open(os.path.join(OUT, "INDICE-TEMPLATES.md"), "w", encoding="utf-8").write(idx)
    shutil.copytree(os.path.join(SRC, "templates-sentenca", "templates"), os.path.join(OUT, "templates"))


def zip_skill():
    os.makedirs(DIST, exist_ok=True)
    zip_path = os.path.join(DIST, "elis.zip")
    root = os.path.dirname(OUT)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for base, _d, files in os.walk(OUT):
            for fn in sorted(files):
                abs_f = os.path.join(base, fn)
                zf.write(abs_f, os.path.relpath(abs_f, root))
    return zip_path


def main():
    for p in (os.path.join(HERE, "skill"), DIST):
        if os.path.exists(p):
            shutil.rmtree(p)
    os.makedirs(OUT)
    build_orchestrator()
    build_etapas()
    build_resources()
    z = zip_skill()
    nfiles = sum(len(f) for _r, _d, f in os.walk(OUT))
    print("Skill único 'elis' (simplificado p/ chat) — %d arquivos." % nfiles)
    print("Pacote:", os.path.relpath(z, HERE))


if __name__ == "__main__":
    main()
