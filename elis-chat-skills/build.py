#!/usr/bin/env python3
"""
build.py — Gera as Agent Skills do ELIS para a interface de chat do claude.ai.

Fonte única: ../elis-plugin/skills (o plugin do Claude Code / Cowork).
Este script adapta cada skill para o formato aceito no claude.ai:

  - Renomeia as skills com o prefixo `elis-` (agrupa na lista de Skills do usuário).
  - Remove `${CLAUDE_PLUGIN_ROOT}` (variável exclusiva do Claude Code):
      * referências à própria skill viram caminhos relativos;
      * referências a outra skill viram menção pelo nome da skill.
  - Converte os comandos slash (`/elis:...`, exclusivos do Claude Code) em
    gatilhos de linguagem natural.
  - Remove o namespace `elis:` das invocações de skill.
  - Acrescenta uma nota sobre o ambiente do claude.ai.

Saídas:
  - skills/<nome>/...   (skills adaptadas, versionadas para revisão)
  - dist/<nome>.zip     (um zip por skill, pronto para upload em
                         Configurações → Recursos no claude.ai)

Uso:  python3 build.py
"""

import os
import re
import shutil
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "elis-plugin", "skills"))
OUT_SKILLS = os.path.join(HERE, "skills")
OUT_DIST = os.path.join(HERE, "dist")

# Mapa de renomeação: nome no plugin -> nome da Agent Skill (prefixo elis-)
RENAME = {
    "fluxo-elis": "elis-fluxo",
    "etapa1-analise-firac": "elis-etapa1-analise-firac",
    "etapa1-5-liminar-rp": "elis-etapa1-5-liminar-rp",
    "etapa2-deliberacao": "elis-etapa2-deliberacao",
    "etapa3-arquitetura": "elis-etapa3-arquitetura",
    "etapa4-sentenca": "elis-etapa4-sentenca",
    "conversao-arquivos": "elis-conversao-arquivos",
    "templates-sentenca": "elis-templates-sentenca",
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

CHAT_NOTE = (
    "\n\n---\n\n"
    "> **Ambiente claude.ai:** os arquivos e scripts citados estão empacotados "
    "nesta skill; ao executar um script, rode-o a partir do diretório desta skill. "
    "Para converter PDF/DOCX, anexar o documento diretamente à conversa costuma "
    "bastar — o Claude lê esses formatos nativamente — sem precisar dos scripts.\n"
)


def transform_text(text: str, self_new: str) -> str:
    # 1) Comandos slash -> linguagem natural (antes de mexer no namespace)
    text = re.sub(
        r"/elis:(" + "|".join(map(re.escape, SLASH)) + r")",
        lambda m: SLASH[m.group(1)],
        text,
    )
    # 2) Remover namespace `elis:` das invocações de skill
    text = text.replace("elis:", "")
    # 3) Renomear tokens de skill (nome de pasta/skill) para o prefixo elis-
    for old, new in RENAME.items():
        text = text.replace(old, new)
    # 4) ${CLAUDE_PLUGIN_ROOT}: caminho da própria skill -> relativo
    text = text.replace("${CLAUDE_PLUGIN_ROOT}/skills/%s/" % self_new, "")
    # 5) ${CLAUDE_PLUGIN_ROOT}: caminho de outra skill -> menção pelo nome
    text = re.sub(
        r"\$\{CLAUDE_PLUGIN_ROOT\}/skills/([a-z0-9-]+)/[^\s`\"'\)]+",
        lambda m: "(arquivo empacotado na skill `%s`)" % m.group(1),
        text,
    )
    # 6) ${CLAUDE_PLUGIN_ROOT} remanescente
    text = text.replace("${CLAUDE_PLUGIN_ROOT}", "o diretório desta skill")
    return text


def process_skill(old_name: str, new_name: str) -> None:
    src_dir = os.path.join(SRC, old_name)
    dst_dir = os.path.join(OUT_SKILLS, new_name)
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)

    for root, _dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        target_root = os.path.join(dst_dir, rel) if rel != "." else dst_dir
        os.makedirs(target_root, exist_ok=True)
        # Não transformar o conteúdo dos templates jurídicos (só copiar)
        in_templates = rel == "templates" or rel.startswith("templates" + os.sep)
        for fn in files:
            src_f = os.path.join(root, fn)
            dst_f = os.path.join(target_root, fn)
            if fn.endswith(".md") and not in_templates:
                with open(src_f, encoding="utf-8") as fh:
                    text = fh.read()
                text = transform_text(text, new_name)
                if fn == "SKILL.md":
                    text = text.rstrip() + CHAT_NOTE
                with open(dst_f, "w", encoding="utf-8") as fh:
                    fh.write(text)
            else:
                shutil.copy2(src_f, dst_f)


def zip_skill(new_name: str) -> str:
    os.makedirs(OUT_DIST, exist_ok=True)
    zip_path = os.path.join(OUT_DIST, new_name + ".zip")
    skill_dir = os.path.join(OUT_SKILLS, new_name)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, files in os.walk(skill_dir):
            for fn in sorted(files):
                abs_f = os.path.join(root, fn)
                # Arquivo dentro do zip: <new_name>/<caminho relativo>
                arc = os.path.join(new_name, os.path.relpath(abs_f, skill_dir))
                zf.write(abs_f, arc)
    return zip_path


def main() -> None:
    if os.path.exists(OUT_SKILLS):
        shutil.rmtree(OUT_SKILLS)
    if os.path.exists(OUT_DIST):
        shutil.rmtree(OUT_DIST)
    for old_name, new_name in RENAME.items():
        process_skill(old_name, new_name)
        z = zip_skill(new_name)
        print("OK  %-28s -> %s" % (new_name, os.path.relpath(z, HERE)))
    print("\n%d skills geradas em skills/ e empacotadas em dist/." % len(RENAME))


if __name__ == "__main__":
    main()
