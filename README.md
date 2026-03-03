# ⚖️ ELIS — Engenharia Legal e Inteligente de Sentenças

## 📋 Descrição

**ELIS** é um assistente de Inteligência Artificial Generativa especializado em processos judiciais eleitorais. Por meio de um fluxo estruturado de análise em 4 etapas (FIRAC+, Deliberação, Arquitetura e Sentença), o ELIS transforma documentos processuais em artefatos de contexto e **gera sentenças completas prontas para uso**.

## 🎯 Objetivo

Transformar documentos processuais em análises estruturadas que apoiam a tomada de decisão judicial, gerando artefatos de contexto através de:

1. **Análise FIRAC+** - Visão panorâmica completa do processo
2. **Tutela de Urgência** - Análise específica de liminares em propaganda eleitoral (condicional)
3. **Deliberação** - Análise do conjunto probatório e argumentação
4. **Arquitetura** - Estruturação da sentença
5. **Sentença** - Geração do documento judicial final

## 📁 Estrutura do Projeto

```
📦 ENGENHARIA DE CONTEXTO PARA SENTENCAS/
├── 📄 README.md                            # Este arquivo
├── 📄 CLAUDE.md                            # Gerenciador de contexto para Claude/Claude Code
├── 📄 .gitignore                           # Proteção de dados processuais e locais
├── 📂 .agents/skills/                      # Skills disponíveis
│   ├── INSTRUCOES-SKILLS.md             # Guia de criação e padronização de skills
│   ├── 📂 pdf/                             # Skill de manipulação de PDF
│   └── 📂 propaganda-eleitoral/            # Skill de tutela de urgência
├── 📂 PROMPTS/                             # Prompts das etapas
│   ├── ETAPA 1- ANALISE FIRAC.md        # Análise FIRAC+
│   ├── ETAPA 2 - DELIBERAÇÃO.md         # Conjunto probtório
│   ├── ETAPA 3 - ARQUITETURA E ESTILO.md # Arquitetura e estilo da sentença
│   └── ETAPA 4 - SENTENÇA.md            # Geração da sentença final
├── 📂 CONTEXTO/                            # Resultados temporários (limpa após finalização)
├── 📂 PROCESSOS CONCLUIDOS/               # Processos finalizados ⚠️ LEITURA RESTRITA
│   └── 📂 [NÚMERO DO PROCESSO]/            # Ex: 0600443-62.2024.6.15.0056
├── 📂 TEMPLATES/                           # Sistema de Templates
│   ├── INSTRUCOES-TEMPLATES.md          # Instruções de geração e uso
│   └── INDICE-TEMPLATES.md              # Índice de templates disponíveis
├── 📂 Modelos_e_Doutrina/                  # Modelos e doutrina jurídica ⚠️ LEITURA SOB DEMANDA
├── 📂 scripts/                             # Scripts de preparação e conversão
│   ├── prepare-input.ps1                # Script principal de conversão (PowerShell)
│   └── extract_docx_to_md.py            # Extrator de DOCX para Markdown (Python)
└── 📂 Documentations/                      # Documentação do projeto
    ├── Agents.md                        # Referência completa (fluxo de trabalho)
    ├── CONVERSAO-ARQUIVOS.md            # Guia técnico de conversão de arquivos
    ├── CHANGELOG.template.md            # Template zerado do changelog (rastreado pelo Git)
    └── CHANGELOG.md                     # Histórico local de alterações (gerado no 1° uso)
```

## 🚀 Como Usar

### 0. Primeiro Uso (ambiente recém-clonado)

Se for a primeira vez que você usa o ELIS neste ambiente, o assistente irá **automaticamente**:
1. Copiar `CHANGELOG.template.md` → `CHANGELOG.md` (seu histórico local zerado)
2. Instalar as dependências de conversão: `pip install pypdf python-docx`
3. Confirmar que o ambiente está pronto

> O gatilho é simples: se `CHANGELOG.template.md` existir e `CHANGELOG.md` não existir, é primeiro uso.

---

### 1. Preparar os Arquivos

Coloque na pasta raiz do projeto:
- Arquivo do processo completo (`.md`, `.docx`, `.txt` ou `.pdf`)
- Arquivos de audiência (resumo/transcrição; `.md`, `.txt`, `.docx` ou `.pdf`)
- Outros arquivos que achar necessários (exemplo: jurisprudências, trechos de artigos ou doutrina e etc)

---

## 🔧 Preparação de Arquivos PDF e DOCX

O sistema converte automaticamente arquivos `.pdf` e `.docx` para Markdown usando o script `scripts/prepare-input.ps1`.

**Comando básico:**
```powershell
powershell -ExecutionPolicy Bypass -File scripts/prepare-input.ps1 -InputFile "<arquivo>"
```

> 📚 **Para instruções técnicas completas** sobre instalação de dependências, comandos detalhados, tratamento de erros e skill de PDF, consulte: **[CONVERSAO-ARQUIVOS.md](Documentations/CONVERSAO-ARQUIVOS.md)**

---

### 2. Iniciar o Processamento

Execute o comando:
```
Faça a engenharia de contexto do processo [REFERÊNCIA AOS ARQUIVOS]
```

> ⚠️ **Nota:** Caso você esqueça de mencionar os documentos de referência, o agente solicitará automaticamente que você indique os arquivos antes de prosseguir.

### 3. Seguir o Fluxo

O agente executará as etapas conforme o cronograma do projeto, consultando você em cada transição.

**Etapa 1.5 - Tutela de Urgência (Fluxo Independente):**
Esta etapa pode ser acionada **a qualquer momento**, independentemente do fluxo principal. Se o processo for uma **Representação (Classe RP)** com **pedido liminar**, o agente informará que você pode acionar a análise liminar imediatamente.

**Comandos:** `"Execute a tutela de urgência"` ou `"Analise o pedido liminar"`.

Após a conclusão da Etapa 1.5, você poderá escolher:
- Prosseguir para **Etapa 2** (Deliberação) - análise completa do mérito
- Ir direto para **Etapa 3** (Arquitetura) - se a liminar já resolveu a questão principal ou se deseja pular a análise detalhada de mérito da Etapa 2.

**Na Etapa 4**, o agente solicitará:
- Jurisprudência que deseja citar
- Doutrina que deseja incluir
- Modelo de sentença (template do sistema ou externo)
- Após geração, opção de salvar como template

### 4. Revisar e Ajustar

Após cada etapa, você pode solicitar ajustes antes de prosseguir.

### 5. Finalização

Ao concluir, os arquivos serão movidos para `PROCESSOS CONCLUIDOS/[NÚMERO]/`

## 📄 Sistema de Templates

O projeto inclui um **Sistema de Templates** para reutilização de modelos de sentenças:

- **Usar templates**: Na Etapa 4, escolha templates compatíveis com o caso
- **Salvar templates**: Após gerar sentença, salve como template para uso futuro
- **Gerar templates**: Crie templates a partir de sentenças modelo fornecidas

Consulte `TEMPLATES/INSTRUCOES-TEMPLATES.md` para instruções completas.

## 📜 Instruções Completas

Consulte o arquivo `Documentations/Agents.md` para instruções detalhadas do projeto.

## ⚠️ Aviso Importante

> As análises geradas são ferramentas de apoio técnico. A decisão final é **prerrogativa exclusiva do julgador**, que deve revisar e adaptar todo o conteúdo antes da utilização.

## 📝 Licença

Uso interno para apoio à atividade jurisdicional.

## 🧹 Limpeza de Pastas Legadas

No fluxo atual, as pastas abaixo nao sao necessarias:
- `.agent/`
- `.venv/`
- `.tmp/` (cache temporario)

Comando de limpeza:

```powershell
Remove-Item -LiteralPath ".agent",".venv",".tmp" -Recurse -Force
```

Se a pasta `.tmp` estiver bloqueada por permissao, ela pode ser removida depois manualmente.

---

### Novidades da Versão 6.9 (atual)
- **Nome oficial**: ELIS — Engenharia Legal Inteligente de Sentenças
- **Preparação para GitHub**: `.gitignore` com proteção de dados processuais e doutrinárias
- **Fluxo de primeiro uso**: detecção automática de ambiente recém-clonado e configuração guiada
- **CHANGELOG protegido**: cada usuário tem seu próprio histórico local a partir do `CHANGELOG.template.md`

*Versão 6.9 - Março/2026*
