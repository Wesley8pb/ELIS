# ELIS — Engenharia Legal e Inteligente de Sentenças

> Plugin Claude Code especializado em **direito eleitoral brasileiro**. Processa documentos de processos judiciais eleitorais por meio de um fluxo estruturado de 4 etapas (análise, deliberação, arquitetura, sentença), gerando artefatos de contexto e sentenças completas prontas para revisão.

## Instalação

```
/plugin marketplace add wesley8pb/elis
/plugin install elis@elis
```

> Quando o plugin ganhar repositório dedicado, basta trocar `wesley8pb/elis` pelo novo `owner/repo` — este diretório é autocontido.

**Pré-requisitos** (apenas para conversão de PDFs/DOCX): Python 3.x e `pip install pypdf`.

## O fluxo ELIS

| Etapa | O que faz | Comando | Saída |
|-------|-----------|---------|-------|
| **0. Preparação** | Converte `.pdf`/`.docx` do processo para Markdown | automático | `[NOME - PROCESSADO].md` |
| **1. Análise FIRAC+** | Análise completa do caso (fatos, provas, problema jurídico, argumentos, crítica) | `/elis:etapa1` | `CONTEXTO/ETAPA1-ANALISE-FIRAC.md` |
| **1.5. Tutela de Urgência** | Decisão liminar em representação por propaganda irregular (RP) — fluxo independente | `/elis:liminar` | `CONTEXTO/ETAPA1.5-LIMINAR-RP.md` |
| **2. Deliberação** | Análise do conjunto probatório pela procedência ou improcedência | `/elis:etapa2` | `CONTEXTO/ETAPA2-DELIBERACAO-[...].md` |
| **3. Arquitetura** | Plano completo da sentença com blindagem recursal e trechos sugeridos | `/elis:etapa3` | `CONTEXTO/ETAPA3-ARQUITETURA-SENTENCA.md` |
| **4. Sentença Final** | Sentença completa e fundamentada, com jurisprudência/doutrina fornecidas | `/elis:etapa4` | `CONTEXTO/ETAPA4-SENTENCA-FINAL.md` |
| **Finalização** | Arquiva tudo em `PROCESSOS CONCLUIDOS/[Nº]/` e limpa a área de trabalho | `/elis:finalizar` | — |

**Início rápido**: abra o Claude Code na pasta que contém os documentos do processo e use:

```
/elis:iniciar 0001234-56.2024.6.15.0056
```

ou simplesmente diga: *"Faça a engenharia de contexto do processo 0001234-56.2024.6.15.0056"*.

Ao concluir cada etapa, o ELIS pergunta sobre ajustes e **sugere a próxima fase** — o fluxo segue contínuo até a finalização, sempre sob confirmação do usuário.

## Skills incluídas

| Skill | Papel |
|-------|-------|
| `fluxo-elis` | Orquestrador: regras fundamentais, glossário de classes processuais, mapa das etapas, estilo, finalização |
| `etapa1-analise-firac` | Etapa 1 — Análise FIRAC+ |
| `etapa1-5-liminar-rp` | Etapa 1.5 — Tutela de urgência em RP (com `reference.md` de blocos invariáveis) |
| `etapa2-deliberacao` | Etapa 2 — Deliberação sobre o conjunto probatório |
| `etapa3-arquitetura` | Etapa 3 — Arquitetura da sentença + estilo de escrita do magistrado |
| `etapa4-sentenca` | Etapa 4 — Sentença final |
| `conversao-arquivos` | Fase 0 — Conversão de `.pdf`/`.docx` (scripts Python/PowerShell embarcados) |
| `templates-sentenca` | 15 templates embarcados de sentenças e decisões liminares, com índice e fluxos de uso/criação |

As skills também são ativadas por **linguagem natural** (ex.: "analise o pedido liminar", "prossiga para a próxima etapa") — os comandos slash são atalhos explícitos.

## Área de trabalho

O plugin opera na pasta de trabalho atual do usuário:

- **Documentos do processo**: raiz da pasta de trabalho
- **Artefatos das etapas**: `CONTEXTO/` (criada automaticamente)
- **Processos finalizados**: `PROCESSOS CONCLUIDOS/[NÚMERO]/`
- **Templates do usuário**: `TEMPLATES/` (os 15 templates embarcados no plugin são somente leitura; novos templates são salvos localmente)

## Regras fundamentais

1. Cada conversa = 1 processo
2. Nunca prosseguir sem confirmar com o usuário ao final de cada etapa
3. **Nunca criar jurisprudência ou doutrina** — usar exclusivamente as fornecidas pelo usuário
4. Transcrever literalmente dispositivos legais, sem omissões
5. Citar IDs de documentos entre parênteses
6. Texto corrido na fundamentação, sem subdivisões visíveis
7. Aviso de IA generativa ao final de cada etapa

## Aviso

> **ATENÇÃO**: As análises e minutas são geradas por Inteligência Artificial Generativa. Embora elaboradas com rigor técnico, é fundamental que sejam revisadas e adaptadas por profissional do Direito antes de sua utilização.

---

*ELIS — plugin v1.0.0*
