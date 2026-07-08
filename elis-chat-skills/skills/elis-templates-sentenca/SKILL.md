---
name: elis-templates-sentenca
description: Sistema de templates de sentenças e decisões eleitorais do ELIS. Contém 15 templates embarcados (sentenças de AIJE, AIME, Ação Penal Eleitoral e decisões liminares em RP/RPEsp) com índice para busca por tipo de ação, julgamento e tema. Cobre três fluxos - gerar template a partir de documento, salvar sentença como template e usar template na Etapa 4. Acionar quando o usuário pedir para usar, listar, gerar ou salvar templates de sentença, ou quando a Etapa 4 oferecer template do sistema.
---

# Sistema de Templates de Sentenças (ELIS)

Permite **gerar, salvar, indexar e utilizar templates** de sentenças eleitorais, reutilizando modelos já validados para acelerar a produção de novas sentenças.

## Onde os templates vivem

| Local | Conteúdo | Escrita |
|-------|----------|---------|
| `templates/` | **15 templates embarcados** no plugin | ❌ Somente leitura (o diretório do plugin instalado é somente leitura) |
| `TEMPLATES/` na pasta de trabalho do usuário | Templates criados pelo usuário | ✅ Novos templates são salvos aqui |

**Ao buscar templates, SEMPRE consultar os dois locais**: o índice embarcado (`INDICE.md` nesta skill) e a pasta `TEMPLATES/` local (com seu `INDICE-TEMPLATES.md`, se existir).

## Nomenclatura de Templates

### Formato obrigatório:
```
[TIPO-ACAO]_[JULGAMENTO]_[TEMA-PRINCIPAL].md
```

### Tipos de Ação

#### Sentenças (julgamento de mérito):
| Sigla | Descrição |
|-------|-----------|
| `ACAO-PENAL` | Ação Penal Eleitoral |
| `AIJE` | Ação de Investigação Judicial Eleitoral |
| `AIME` | Ação de Impugnação de Mandato Eletivo |
| `AIRC` | Ação de Impugnação de Registro de Candidatura |
| `RCED` | Recurso Contra Expedição de Diploma |
| `RPEsp` | Representação Especial (Conduta Vedada) |
| `RP` | Representação por Propaganda Irregular |
| `PCE` | Prestação de Contas de Campanha Eleitoral |
| `RO` | Recurso Ordinário |
| `AC` | Apelação Criminal |

#### Decisões interlocutórias (tutela de urgência / liminar):
| Sigla | Descrição |
|-------|-----------|
| `RP-LIMINAR` | Decisão sobre tutela de urgência em RP (Propaganda Irregular) |
| `RPEsp-LIMINAR` | Decisão sobre tutela de urgência em RPEsp (Conduta Vedada) |
| `RP_CITACAO` | Decisão de recebimento da inicial e citação em RP (sem liminar) |

### Julgamentos

Para sentenças: `PROCEDENCIA`, `IMPROCEDENCIA`, `PARCIAL`, `EXTINCAO`, `DESAPROVACAO`, `APROVACAO`, `APROVACAO-RESSALVAS`.
Para liminares: `CONCESSAO`, `DENEGACAO`, `PARCIAL`, `CITACAO`.

### Exemplos:
- `ACAO-PENAL_IMPROCEDENCIA_CORRUPCAO-ELEITORAL.md`
- `AIJE_PROCEDENCIA_ABUSO-PODER-ECONOMICO.md`
- `RP-LIMINAR_CONCESSAO_FAKE-NEWS-REDES-SOCIAIS.md`
- `RP-LIMINAR_DENEGACAO_LIBERDADE-EXPRESSAO.md`

## FLUXO 1: Geração de template a partir de documento

**Quando usar**: o usuário fornece uma sentença modelo para criar um template reutilizável.
**Comando do usuário**: `"Gere um template a partir desta sentença: [documento]"`

1. **ANALISAR** o documento: tipo de ação, julgamento, tema principal e secundários, estrutura e padrões de redação.
2. **GENERALIZAR**: substituir dados específicos por placeholders; manter estrutura, estilo e fundamentação jurídica genérica.
3. **GERAR** o template conforme a Estrutura Obrigatória abaixo.
4. **SALVAR** em `TEMPLATES/` (pasta de trabalho) com a nomenclatura padrão.
5. **ATUALIZAR** o índice local `TEMPLATES/INDICE-TEMPLATES.md` (criar se não existir).

## FLUXO 2: Salvar template após a Etapa 4

**Quando usar**: após gerar uma sentença na Etapa 4, o sistema oferece salvar como template.

1. **GENERALIZAR** a sentença gerada:
   - Nome das partes → `[NOME_AUTOR]`, `[NOME_REU]`
   - Número do processo → `[NUMERO_PROCESSO]`
   - Datas → `[DATA_FATO]`, `[DATA_SENTENCA]`
   - IDs de documentos → `[ID_DOCUMENTO_X]`
   - Manter estrutura, estilo e fundamentação
2. **IDENTIFICAR** metadados: tipo de ação, julgamento, tema principal (do contexto da Etapa 1).
3. **SALVAR** e **INDEXAR** conforme Fluxo 1.

## FLUXO 3: Uso de template na Etapa 4

1. **VARRER** os índices (embarcado `INDICE.md` + `TEMPLATES/INDICE-TEMPLATES.md` local, se existir): identificar tipo de ação, julgamento e tema do caso atual.
2. **SUGERIR** templates compatíveis:

```
📚 TEMPLATES COMPATÍVEIS:

Com base no caso ([Tipo de Ação], [Julgamento], [Tema]):

1. [NOME_TEMPLATE_1].md ⭐ (100% compatível)
2. [NOME_TEMPLATE_2].md (80% compatível)

Qual deseja usar? (digite o número ou "nenhum")
```

3. **CARREGAR** o template escolhido (embarcado: `templates/<nome>.md`; local: `TEMPLATES/<nome>.md`).
4. **ADAPTAR** ao caso concreto: substituir placeholders pelos dados reais, ajustar fundamentação aos fatos, integrar provas/argumentos das etapas anteriores e jurisprudência/doutrina fornecidas.
5. **GERAR** a sentença final.

## Compatibilidade de Templates

| Critério | Peso |
|----------|------|
| Tipo de Ação idêntico | 40% |
| Julgamento idêntico | 30% |
| Tema principal igual ou similar | 30% |

- **100%**: todos os critérios iguais | **80%**: tipo e julgamento iguais, tema similar | **60%**: apenas tipo igual | **Abaixo de 60%**: não sugerir.

## Estrutura Obrigatória do Template

### Para Sentenças (julgamento de mérito):

```markdown
# TEMPLATE DE SENTENÇA

## METADADOS
- **Tipo de Ação**: [TIPO]
- **Julgamento**: [PROCEDÊNCIA/IMPROCEDÊNCIA/PARCIAL/EXTINÇÃO]
- **Tema Principal**: [TEMA]
- **Temas Secundários**: [TEMA1], [TEMA2]
- **Data de Criação**: [DATA]
- **Baseado em**: [PROCESSO ORIGEM ou "Modelo genérico"]

## SENTENÇA
[Conteúdo generalizado com placeholders]

## INSTRUÇÕES DE USO
[Como adaptar ao caso concreto]

## TABELA DE PLACEHOLDERS
[Tabela de placeholders e descrições]

## CASOS DE USO IDEAL
[Quando usar este template]
```

### Para Decisões Interlocutórias (tutela de urgência / liminar):

```markdown
# TEMPLATE DE DECISÃO

## METADADOS
- **Tipo de Ação**: [RP/RPEsp]
- **Tipo de Decisão**: [Tutela de Urgência / Recebimento e Citação]
- **Resultado**: [Concessão/Denegação/Concessão Parcial/Simples Citação]
- **Tema Principal**: [TEMA]
- **Temas Secundários**: [TEMA1], [TEMA2]
- **Data de Criação**: [DATA]
- **Baseado em**: [PROCESSOS-MODELO]

## DECISÃO
### CABEÇALHO
[Cabeçalho institucional com placeholders]

### DECISÃO
[Corpo: Relatório → Fundamentação → Dispositivo → Publicação/Citação/MP → Fecho]

> **SUGESTÃO DE MULTA** (obrigatório nos templates de CONCESSÃO e PARCIAL):
> Valor sugerido, faixa observada nos modelos, critérios de calibragem e processos de referência.

## INSTRUÇÕES DE USO
[Como adaptar ao caso concreto]

## TABELA DE PLACEHOLDERS
[Tabela de placeholders e descrições, incluindo condicionais]

## CASOS DE USO IDEAL
[Quando usar este template]
```

### Placeholders Comuns:

| Placeholder | Descrição | Exemplo |
|-------------|-----------|---------|
| `[NUMERO_PROCESSO]` | Número completo do processo | 0600443-62.2024.6.15.0056 |
| `[NOME_REPRESENTANTE]` | Representante / Autor | Coligação ALIANÇA PELO TRABALHO |
| `[NOME_REPRESENTADO]` | Representado / Réu | [NOME COMPLETO] |
| `[ZONA_ELEITORAL]` | Zona eleitoral | 56ª ZONA ELEITORAL - [MUNICÍPIO]/[UF] |
| `[CIDADE]` | Cidade | [CIDADE] |
| `[ID_DOCUMENTO_X]` | ID do documento no PJe | ID 123138800 |
| `[NOME_JUIZ]` | Nome do juiz eleitoral | [NOME DO JUIZ] |

## ⚠️ Regras Absolutas

1. **NUNCA** incluir dados específicos de processo no template
2. **SEMPRE** usar placeholders para dados variáveis
3. **MANTER** a estrutura e estilo de redação do modelo original
4. **PRESERVAR** a qualidade técnica da fundamentação
5. **ATUALIZAR** o índice local sempre que criar novo template
6. **VERIFICAR** nomenclatura antes de salvar
7. **NUNCA** tentar gravar dentro do diretório do plugin — novos templates vão para `TEMPLATES/` da pasta de trabalho

## Índice dos Templates Embarcados

Consultar o arquivo `INDICE.md` desta skill.

---

> **Ambiente claude.ai:** os arquivos e scripts citados estão empacotados nesta skill; ao executar um script, rode-o a partir do diretório desta skill. Para converter PDF/DOCX, anexar o documento diretamente à conversa costuma bastar — o Claude lê esses formatos nativamente — sem precisar dos scripts.
