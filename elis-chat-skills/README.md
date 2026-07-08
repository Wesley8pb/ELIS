# ELIS — Agent Skills para a interface de chat (claude.ai)

Este diretório empacota o ELIS como **Agent Skills** para uso na **interface de chat do claude.ai** (web, desktop e mobile) — não confundir com o plugin do Claude Code / Cowork, que fica em `../elis-plugin/`.

As skills aqui são **geradas automaticamente** a partir do plugin (`../elis-plugin/skills/`) pelo script `build.py`, com as adaptações necessárias para o chat. **Não edite os arquivos em `skills/` ou `dist/` à mão** — altere a fonte no plugin e rode o build.

## Pré-requisitos no claude.ai

- Plano **Pro, Max, Team ou Enterprise**.
- **Execução de código / criação de arquivos** habilitada nas configurações.
- As Skills são **individuais por usuário** (não sincronizam com Claude Code nem com a API — cada superfície é separada).

## Como instalar

Para cada arquivo `.zip` em `dist/`:

1. No claude.ai, abra **Configurações → Recursos (Features)** → seção **Skills**.
2. Clique em **fazer upload de skill** e selecione o `.zip`.
3. Repita para as 8 skills. Depois de habilitadas, elas ficam disponíveis em novos chats.

> **Recomendação de ordem**: comece por `elis-fluxo.zip` (o orquestrador). As demais são acionadas por ele conforme a etapa.

As 8 skills:

| Zip | Papel |
|-----|-------|
| `elis-fluxo.zip` | Orquestrador — regras, glossário, mapa das etapas, finalização |
| `elis-etapa1-analise-firac.zip` | Etapa 1 — Análise FIRAC+ |
| `elis-etapa1-5-liminar-rp.zip` | Etapa 1.5 — Tutela de urgência em RP |
| `elis-etapa2-deliberacao.zip` | Etapa 2 — Deliberação |
| `elis-etapa3-arquitetura.zip` | Etapa 3 — Arquitetura da sentença |
| `elis-etapa4-sentenca.zip` | Etapa 4 — Sentença final |
| `elis-conversao-arquivos.zip` | Conversão de PDF/DOCX |
| `elis-templates-sentenca.zip` | 15 templates + índice |

## Como usar no chat

Não há comandos slash na interface de chat — as skills são acionadas por **linguagem natural**. Exemplos:

- *"Faça a engenharia de contexto do processo 0001234-56.2024.6.15.0056"* → dispara `elis-fluxo`
- *"Analise o pedido liminar"* → `elis-etapa1-5-liminar-rp`
- *"Prossiga para a Etapa 2 pela improcedência"* → `elis-etapa2-deliberacao`
- *"Finalize o processo"* → arquivamento

Anexe os documentos do processo diretamente na conversa. Ao concluir cada etapa, o ELIS pergunta sobre ajustes e sugere a próxima fase.

## Diferenças em relação ao plugin do Claude Code

| Aspecto | Plugin (Code/Cowork) | Agent Skills (chat) |
|---------|----------------------|---------------------|
| Instalação | `/plugin marketplace add` + `/plugin install` | Upload de `.zip` em Configurações |
| Acionamento | Comandos slash (`/elis:etapa1`) **e** linguagem natural | Só linguagem natural |
| Caminhos de arquivo | `${CLAUDE_PLUGIN_ROOT}` | Relativos à skill |
| Conversão de arquivos | Scripts Python/PowerShell | Anexar o documento ao chat costuma bastar (Claude lê PDF/DOCX nativamente) |
| Distribuição | Um plugin com todas as skills | Uma skill (zip) por vez, por usuário |

## Regenerar os zips

Após qualquer alteração nas skills do plugin (`../elis-plugin/skills/`):

```bash
cd elis-chat-skills
python3 build.py
```

O script recria `skills/` (versões adaptadas, para revisão) e `dist/` (os zips prontos para upload).

## Observações

- **Nomes prefixados com `elis-`** para agruparem na sua lista de Skills e evitarem colisão com outras skills.
- **PDF**: a skill de conversão usa `pypdf`, que pode não estar disponível no ambiente do chat. Nesse caso, anexe o PDF diretamente — o Claude o lê nativamente.
- Use apenas skills de fontes confiáveis; audite o conteúdo antes de subir (estas foram geradas a partir do seu próprio projeto).
