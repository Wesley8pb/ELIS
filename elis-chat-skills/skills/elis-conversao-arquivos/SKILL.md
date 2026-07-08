---
name: elis-conversao-arquivos
description: Fase 0 do fluxo ELIS — conversão de documentos processuais .pdf e .docx para Markdown antes das etapas de análise. Usa scripts Python embarcados (pypdf para PDF, stdlib para DOCX) ou o script PowerShell prepare-input.ps1 no Windows. Acionar sempre que houver arquivos .pdf ou .docx de processo a converter na pasta de trabalho, ou quando o usuário pedir para converter/extrair documentos do processo.
---

# Conversão de Arquivos (Fase 0 do fluxo ELIS)

Converte documentos processuais para Markdown, permitindo processamento eficiente pelas etapas do ELIS.

## Tipos de Arquivos Suportados

| Formato | Tratamento |
|---------|------------|
| `.md` / `.txt` | Processamento direto, sem conversão |
| `.docx` | Extração de conteúdo → `[NOME ORIGINAL - PROCESSADO].md` |
| `.pdf` | Extração via biblioteca Python `pypdf` → `[NOME ORIGINAL - PROCESSADO].md` |

## Scripts Embarcados

Os scripts ficam em `scripts/`:

| Script | Função |
|--------|--------|
| `extract_pdf_to_md.py` | Extrai texto de `.pdf` (requer `pypdf`); extrai metadados (Autor, Título) automaticamente |
| `extract_docx_to_md.py` | Extrai texto, tabelas e notas de `.docx` (apenas bibliotecas padrão do Python) |
| `prepare-input.ps1` | Wrapper PowerShell (Windows) que roteia para o extrator correto conforme a extensão |

## Como Converter

### Linux / macOS / qualquer ambiente com Python

```bash
# PDF (requer pypdf)
python3 "scripts/extract_pdf_to_md.py" "processo.pdf" "processo - PROCESSADO.md"

# DOCX (sem dependências externas)
python3 "scripts/extract_docx_to_md.py" "documento.docx" "documento - PROCESSADO.md"
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -File "scripts/prepare-input.ps1" -InputFile "processo.pdf"
# Saída: processo - PROCESSADO.md
```

Parâmetros do `prepare-input.ps1`:

| Parâmetro | Obrigatório | Descrição |
|-----------|-------------|-----------|
| `-InputFile` | ✅ | Caminho do arquivo a converter |
| `-OutputFile` | ❌ | Caminho de saída (padrão: `[NOME ORIGINAL - PROCESSADO].md`) |

## Pré-requisitos

- **Python 3.x** instalado
- Biblioteca `pypdf` (apenas para PDFs): `pip install pypdf` (ou `py -m pip install pypdf` no Windows)
- Opcional para funcionalidades avançadas: `pip install pdfplumber reportlab python-docx`

> **Windows — Python fora do PATH:** se `py`/`python` não for reconhecido, usar o caminho absoluto típico `C:\Users\<USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe`.

## Formato de Saída

Todos os arquivos convertidos possuem um **cabeçalho de metadados** no início:

```markdown
> [EXTRACTION] backend=pypdf
> [SOURCE] nome_do_arquivo_original.pdf
> [TITLE] Título nos Metadados (se houver)

[Conteúdo extraído do documento...]
```

## Fluxo de Conversão Automática

Quando encontrar arquivos `.docx` ou `.pdf` de processo na pasta de trabalho:

1. ✅ Executar o extrator adequado com o arquivo de entrada
2. ✅ Aguardar geração do arquivo `[NOME - PROCESSADO].md`
3. ✅ Usar o arquivo convertido em todas as etapas subsequentes
4. ✅ Manter o arquivo original para arquivamento final

**Se a conversão falhar**: informar o erro ao usuário e aguardar instrução — **não tentar alternativas sem aprovação**.

## Tratamento de Erros

| Erro | Causa | Solução |
|------|-------|---------|
| `Arquivo de entrada não encontrado` | Caminho incorreto ou arquivo inexistente | Verificar o caminho do arquivo |
| `Extensão não suportada` | Formato não reconhecido | Usar `.md`, `.txt`, `.docx` ou `.pdf` |
| `Biblioteca 'pypdf' não encontrada` | Dependência Python ausente | Executar `pip install pypdf` |
| `Falha ao extrair PDF` | PDF corrompido ou protegido | Verificar integridade do PDF |
| `Aviso: Nenhum texto foi extraído` | PDF escaneado (imagem) sem OCR | O PDF precisa ter texto selecionável (OCR) |
| `Arquivo DOCX inválido` | DOCX corrompido | Verificar integridade do arquivo |
| `'py' is not recognized...` | Python fora do PATH (Windows) | Usar o caminho absoluto do Python ou reinstalar marcando "Add to PATH" |

---

> **Ambiente claude.ai:** os arquivos e scripts citados estão empacotados nesta skill; ao executar um script, rode-o a partir do diretório desta skill. Para converter PDF/DOCX, anexar o documento diretamente à conversa costuma bastar — o Claude lê esses formatos nativamente — sem precisar dos scripts.
