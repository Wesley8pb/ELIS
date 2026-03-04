# 🛠️ CONVERSÃO DE ARQUIVOS - Guia Técnico

Este documento contém todas as instruções técnicas para conversão de arquivos no sistema de Engenharia de Contexto para Sentenças Eleitorais.

---

## 📋 **VISÃO GERAL**

O sistema aceita documentos processuais em diversos formatos e os converte para Markdown, permitindo processamento eficiente pelo agente.

### **Tipos de Arquivos Suportados**

| Formato | Tratamento |
|---------|------------|
| `.md` (Markdown) | Processamento direto, sem conversão |
| `.txt` (Texto) | Processamento direto, sem conversão |
| `.docx` (Word) | Extração de conteúdo + conversão para `.md` com nome `[NOME ORIGINAL - PROCESSADO].md` |
| `.pdf` (PDF) | Extração via biblioteca Python `pypdf` + conversão para `.md` com nome `[NOME ORIGINAL - PROCESSADO].md` |

### **Arquivos Esperados na Raiz do Projeto:**

1. **Processo Completo**: Arquivo com o número do processo (ex: `0600443-62.2024.6.15.0056.md`, `.docx` ou `.pdf`) ou simplesmente `Processo.md ou Processo.docx` ou `Processo.pdf`
2. **Arquivos de Audiência** (opcionais):
   - Resumo da Audiência (`.md`, `.txt`, `.docx` ou `.pdf`)
   - Transcrição da Audiência (`.md`, `.txt`, `.docx` ou `.pdf`)
   - Ou ambos

---

## ⚙️ **INSTALAÇÃO DE DEPENDÊNCIAS**

Se você está usando o projeto pela primeira vez, siga estas etapas para configurar o ambiente:

### **1. Verificar Python**

O projeto requer Python 3.x instalado. Verifique se está disponível:

```powershell
py --version
```

> ⚠️ **Atenção — Python pode não estar no PATH:** Em alguns casos, o Python está instalado mas o executável **não está visível** para o PowerShell (a opção "Add Python to PATH" não foi marcada durante a instalação). Nesse caso, o comando `py` e `python` retornam:
> `"The term 'py' is not recognized as a name of a cmdlet..."`

**Caminho típico do Python instalado (substitua `<SEU_USUARIO>` e `Python3XX` pela sua versão):**
```
C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe
```

> 💡 Para descobrir seu usuário, abra o PowerShell e execute: `$env:USERNAME`
> Para descobrir a versão instalada, procure a pasta em `C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\`

Para verificar se esse caminho existe e qual versão está instalada:

```powershell
& "C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe" --version
# Esperado: Python 3.x.x
```

Se não estiver instalado, baixe em: [python.org](https://www.python.org/downloads/)  
_(Durante a instalação, marque obrigatoriamente a opção **"Add Python to PATH"**)_

### **2. Instalar Biblioteca pypdf**

A biblioteca `pypdf` é necessária para processar arquivos PDF.

**Se `py` estiver disponível no PATH:**
```powershell
py -m pip install pypdf
```

**Se precisar usar o caminho completo:**
```powershell
& "C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe" -m pip install pypdf
```

### **3. (Opcional) Instalar Bibliotecas Avançadas**

Para funcionalidades avançadas da skill de PDF (extração de tabelas, OCR):

```powershell
# Se py estiver no PATH
py -m pip install pdfplumber reportlab

# Se precisar do caminho completo
& "C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe" -m pip install pdfplumber reportlab
```

### **4. Verificar Instalação**

Execute um teste rápido:

```powershell
powershell -ExecutionPolicy Bypass -File .agents/scripts/prepare-input.ps1 -InputFile "arquivo_teste.pdf"
```

Se houver erro sobre `pypdf não encontrado`, repita o passo 2.  
Se houver erro sobre `py não reconhecido`, veja a seção **Tratamento de Erros** abaixo.

---

## 🔧 **SKILL DE PDF (ANTIGRAVITY)**

O projeto possui uma **skill de PDF** instalada via Antigravity que expande significativamente as capacidades de manipulação de documentos PDF.

### **📂 Localização**

`.agents/skills/pdf/`

### **📚 Documentação Disponível**

| Arquivo | Descrição |
|---------|-----------|
| `SKILL.md` | Guia principal com operações essenciais |
| `reference.md` | Referência completa com exemplos avançados |
| `forms.md` | Instruções para preenchimento de formulários PDF |
| `.agents/scripts/` | Scripts auxiliares prontos para uso |

### **🎯 Capacidades da Skill**

A skill oferece ferramentas e instruções para:

1. **Extração de Texto e Tabelas**:
   - Extração básica via `pypdf`
   - Extração avançada de tabelas via `pdfplumber`
   - Preservação de layout e estrutura

2. **Manipulação de PDFs**:
   - Mesclar múltiplos PDFs
   - Dividir PDFs em páginas individuais
   - Rotacionar páginas
   - Adicionar marcas d'água

3. **OCR em Documentos Escaneados**:
   - Conversão de PDFs escaneados em texto pesquisável
   - Usa `pytesseract` + `pdf2image`

4. **Criação de PDFs**:
   - Geração de PDFs do zero via `reportlab`
   - Criação de documentos com múltiplas páginas
   - Suporte a tabelas e formatação

5. **Preenchimento de Formulários**:
   - Identificação de campos preenchíveis
   - Preenchimento automático via scripts

6. **Proteção e Segurança**:
   - Criptografia de PDFs
   - Remoção de senhas

### **💡 Como Usar a Skill**

Para consultar a documentação completa da skill:

```markdown
@[.agents/skills/pdf/SKILL.md]
```

Para operações específicas, consulte os arquivos de referência dentro da pasta da skill.

### **🔗 Integração com o Projeto**

A skill está integrada ao fluxo de preparação de arquivos através do script `extract_pdf_to_md.py`, que utiliza a biblioteca `pypdf` recomendada pela skill.

---

## 📂 **ESTRUTURA DA PASTA `.agents/scripts/`**

```
.agents/scripts/
├── prepare-input.ps1         # Script principal de conversão (PowerShell)
├── extract_docx_to_md.py     # Extrator de DOCX para Markdown (Python stdlib)
└── extract_pdf_to_md.py      # Extrator de PDF para Markdown (Python + pypdf)
```

---

## 🔧 **SCRIPT PRINCIPAL: `prepare-input.ps1`**

**Localização:** `.agents/scripts/prepare-input.ps1`

**Função:** Converte arquivos `.pdf`, `.docx`, `.txt` ou `.md` para um formato Markdown padronizado.

### **Sintaxe**

```powershell
powershell -ExecutionPolicy Bypass -File .agents/scripts/prepare-input.ps1 -InputFile "<arquivo>"
```

### **Parâmetros**

| Parâmetro | Obrigatório | Descrição |
|-----------|-------------|------------|
| `-InputFile` | ✅ Sim | Caminho do arquivo a ser convertido |
| `-OutputFile` | ❌ Não | Caminho de saída (padrão: `[NOME ORIGINAL - PROCESSADO].md`) |

### **Exemplos de Uso**

```powershell
# Converter PDF para Markdown
powershell -ExecutionPolicy Bypass -File .agents/scripts/prepare-input.ps1 -InputFile "0600443-62.2024.6.15.0056.pdf"
# Saída: 0600443-62.2024.6.15.0056 - PROCESSADO.md

# Converter DOCX para Markdown
powershell -ExecutionPolicy Bypass -File .agents/scripts/prepare-input.ps1 -InputFile "Resumo_Audiencia.docx"
# Saída: Resumo_Audiencia - PROCESSADO.md

# Especificar arquivo de saída personalizado
powershell -ExecutionPolicy Bypass -File .agents/scripts/prepare-input.ps1 -InputFile "documento.pdf" -OutputFile "saida_customizada.md"
```

### **Formatos Suportados**

| Extensão | Backend Utilizado | Descrição |
|----------|-------------------|------------|
| `.docx` | `extract_docx_to_md.py` | Parser Python sem dependências externas |
| `.pdf` | `extract_pdf_to_md.py` | Extração via biblioteca `pypdf` |
| `.txt` | passthrough | Cópia direta com cabeçalho de metadados |
| `.md` | passthrough | Cópia direta com cabeçalho de metadados |

> ⚠️ **Nota:** O antigo extrator baseado em `pdftotext` (poppler) foi substituído pela biblioteca Python nativa `pypdf`, eliminando a necessidade de instalar ferramentas externas via Scoop.

---

## 📄 **EXTRATORES PYTHON (`.agents/scripts/*.py`)**

### **1. `extract_docx_to_md.py`**
- Extrai texto, tabelas e notas de arquivos `.docx`
- Usa apenas bibliotecas padrão do Python

### **2. `extract_pdf_to_md.py`**
- Extrai texto de arquivos `.pdf`
- Requer biblioteca `pypdf` (`pip install pypdf`)
- Extrai metadados (Autor, Título) automaticamente

---

## 📝 **FORMATO DE SAÍDA**

Todos os arquivos convertidos possuem um **cabeçalho de metadados** no início:

```markdown
> [EXTRACTION] backend=pypdf
> [SOURCE] nome_do_arquivo_original.pdf
> [TITLE] Título nos Metadados (se houver)

[Conteúdo extraído do documento...]
```

---

## ⚠️ **TRATAMENTO DE ERROS**

| Erro | Causa | Solução |
|------|-------|--------|
| `Arquivo de entrada não encontrado` | Caminho incorreto ou arquivo inexistente | Verificar o caminho do arquivo |
| `Extensão não suportada` | Arquivo com formato não reconhecido | Usar `.md`, `.txt`, `.docx` ou `.pdf` |
| `Biblioteca 'pypdf' não encontrada` | Dependência Python ausente | Executar `pip install pypdf` ou usar o caminho completo |
| `Falha ao extrair PDF` | PDF corrompido ou protegido | Verificar integridade do PDF |
| `Aviso: Nenhum texto foi extraído` | PDF escaneado (imagem) sem OCR | O PDF precisa ter texto selecionável (OCR) |
| `Arquivo DOCX inválido` | DOCX corrompido ou inválido | Verificar integridade do arquivo |
| `'py' is not recognized...` | Python não está no PATH do sistema | Usar o caminho completo: `C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe` — ou reinstalar o Python marcando "Add to PATH" |

---

## 🔄 **FLUXO DE CONVERSÃO AUTOMÁTICA**

Quando o agente encontrar arquivos `.docx` ou `.pdf` na raiz do projeto:

1. ✅ Executar o script `prepare-input.ps1` com o arquivo de entrada
2. ✅ Aguardar geração do arquivo `[NOME - PROCESSADO].md`
3. ✅ Usar o arquivo convertido em todas as etapas subsequentes
4. ✅ Manter o arquivo original para arquivamento final

---

## 📋 **CHECKLIST RÁPIDO DE CONVERSÃO**

```
□ Verificar se Python 3.x está instalado
    → Caminho típico: C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe
    → Para descobrir seu usuário: execute $env:USERNAME no PowerShell
□ Verificar se 'py' está disponível no PATH (opcional, mas facilita o uso):
    → Se não estiver, usar sempre o caminho completo acima
□ Instalar pypdf:
    → Com py no PATH: py -m pip install pypdf
    → Com caminho completo: & "C:\Users\<SEU_USUARIO>\AppData\Local\Programs\Python\Python3XX\python.exe" -m pip install pypdf
□ (Opcional) Instalar pdfplumber, pdf2image, reportlab
□ Colocar arquivos na raiz do projeto
□ Executar: powershell -ExecutionPolicy Bypass -File .agents/scripts/prepare-input.ps1 -InputFile "arquivo.ext"
□ Se o script falhar com 'py not recognized', o script auto-detecta o Python via caminho absoluto
□ Verificar arquivo [NOME - PROCESSADO].md gerado
□ Proceder com a engenharia de contexto
```

---

## 🔗 **REFERÊNCIAS**

- Documentação principal: `Agents.md`
- Skill PDF Antigravity: `.agents/skills/pdf/SKILL.md`
- Prompts das etapas: `PROMPTS/`

---

*Documento criado em: 11/02/2026*  
*Última atualização: 02/03/2026*  
*Versão: 1.1*  
*Extraído de: Agents.md v2.0 | Atualizado com instruções genéricas de PATH do Python (AppData/Local/Programs/Python/Python3XX)*
