# ELIS — skill único para a interface de chat (claude.ai)

Este diretório empacota o ELIS como **um único skill** (`elis`) para a **interface de chat do claude.ai** (web, desktop e mobile) — um só arquivo `.zip`, um só upload.

> Por que um único skill? O claude.ai aceita **um skill por zip** (o zip contém a pasta do skill com `SKILL.md`); não é possível empacotar vários skills num zip só. Para entregar **um único pacote**, consolidamos todo o ELIS em um skill, no qual cada etapa vira um arquivo interno carregado sob demanda (mesmo padrão da skill de PDF da Anthropic: um `SKILL.md` + arquivos de referência).

O plugin do Claude Code / Cowork continua em `../elis-plugin/` (lá, sim, cada etapa é uma skill separada dentro de um único plugin).

O skill é **gerado automaticamente** a partir do plugin (`../elis-plugin/skills/`) pelo `build.py`. **Não edite `skill/` ou `dist/` à mão** — altere a fonte no plugin e rode o build.

## O pacote

`dist/elis.zip` contém:

```
elis/
├── SKILL.md                 # orquestrador (regras, glossário, mapa das etapas)
├── etapas/
│   ├── 1-analise-firac.md   # Etapa 1 — Análise FIRAC+
│   ├── 1.5-liminar-rp.md    # Etapa 1.5 — Tutela de urgência (RP)
│   ├── 2-deliberacao.md     # Etapa 2 — Deliberação
│   ├── 3-arquitetura.md     # Etapa 3 — Arquitetura da sentença
│   ├── 4-sentenca.md        # Etapa 4 — Sentença final
│   └── templates-sentenca.md
├── reference/liminar-rp.md  # blocos invariáveis da tutela de urgência
├── INDICE-TEMPLATES.md      # índice dos 15 templates
└── templates/               # 15 templates de sentenças e decisões
```

Como é um único skill, o Claude carrega só o `SKILL.md` de início (leve) e lê o arquivo da etapa correspondente **apenas quando ela é acionada** (progressive disclosure).

### Simplificações em relação ao plugin do Claude Code

A versão de chat é enxuta de propósito — o claude.ai já cobre nativamente o que o plugin fazia via filesystem:

- **Sem camada de conversão**: o Claude lê PDF/DOCX de anexos nativamente (sem `scripts/` nem `etapas/conversao-arquivos.md`).
- **Sem pastas** `CONTEXTO/`, `PROCESSOS CONCLUIDOS/` ou `TEMPLATES/` local, e **sem etapa de finalização**.
- **Entradas = anexos** da conversa. **Saídas = Artefatos** (documentos na lateral do chat).
- Os 15 templates continuam embarcados como biblioteca de leitura; criar um novo template gera um **Artefato**.

## Pré-requisitos no claude.ai

- Plano **Pro, Max, Team ou Enterprise**.
- **Execução de código / criação de arquivos** habilitada nas configurações.
- Skills são **individuais por usuário** e **não sincronizam** com Claude Code nem com a API (cada superfície é separada).

## Como instalar

1. No claude.ai, abra **Configurações → Recursos (Features)** → seção **Skills**.
2. Clique em **fazer upload de skill** e selecione **`dist/elis.zip`**.
3. Habilite o skill. Pronto — disponível em qualquer chat novo.

## Como usar

Não há comandos slash na interface de chat — o acionamento é por **linguagem natural**:

- *"Faça a engenharia de contexto do processo 0001234-56.2024.6.15.0056"*
- *"Analise o pedido liminar"* (tutela de urgência)
- *"Prossiga para a Etapa 2 pela improcedência"*
- *"Finalize o processo"*

Anexe os documentos do processo diretamente na conversa. Ao concluir cada etapa, o ELIS pergunta sobre ajustes e sugere a próxima fase.

## Regenerar o pacote

Após qualquer alteração nas skills do plugin (`../elis-plugin/skills/`):

```bash
cd elis-chat-skills
python3 build.py
```

O script recria `skill/elis/` (versão adaptada, para revisão) e `dist/elis.zip`.

## Observações

- Anexe os documentos do processo diretamente na conversa — não é preciso converter nada.
- Use apenas skills de fontes confiáveis; audite o conteúdo antes de subir (este foi gerado do seu próprio projeto).
