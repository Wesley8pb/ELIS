# 📚 INSTRUÇÕES PARA GERAÇÃO E USO DE TEMPLATES DE SENTENÇAS

## 🎯 **OBJETIVO**

Este documento contém as instruções completas para **gerar, salvar, indexar e utilizar templates** de sentenças eleitorais, permitindo a reutilização de modelos já validados para acelerar a produção de novas sentenças.

---

## 📋 **VISÃO GERAL DO SISTEMA**

O Sistema de Templates permite:
1. **Gerar templates** a partir de documentos de sentença fornecidos
2. **Salvar templates** após a geração de uma sentença na Etapa 4
3. **Utilizar templates** salvos para gerar novas sentenças
4. **Indexar templates** para facilitar busca e seleção

---

## 📝 **NOMENCLATURA DE TEMPLATES**

### **Formato Obrigatório**:
```
[TIPO-ACAO]_[JULGAMENTO]_[TEMA-PRINCIPAL].md
```

### **Tipos de Ação**:

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

### **Julgamentos**:

#### Para sentenças:
| Sigla | Descrição |
|-------|-----------|
| `PROCEDENCIA` | Sentença de procedência/condenação |
| `IMPROCEDENCIA` | Sentença de improcedência/absolvição |
| `PARCIAL` | Procedência parcial |
| `EXTINCAO` | Extinção sem resolução de mérito |
| `DESAPROVACAO` | Desaprovação de contas (PCE) |
| `APROVACAO` | Aprovação de contas (PCE) |
| `APROVACAO-RESSALVAS` | Aprovação com ressalvas (PCE) |

#### Para decisões interlocutórias (liminar):
| Sigla | Descrição |
|-------|-----------|
| `CONCESSAO` | Tutela de urgência concedida |
| `DENEGACAO` | Tutela de urgência denegada |
| `PARCIAL` | Tutela de urgência concedida parcialmente |
| `CITACAO` | Recebimento da inicial e citação (sem análise de liminar) |

### **Exemplos de Nomenclatura**:

#### Sentenças:
- `ACAO-PENAL_IMPROCEDENCIA_CORRUPCAO-ELEITORAL.md`
- `AIJE_PROCEDENCIA_ABUSO-PODER-ECONOMICO.md`
- `AIME_PROCEDENCIA_FRAUDE-ELEITORAL.md`
- `AIRC_PROCEDENCIA_INELEGIBILIDADE-FICHA-LIMPA.md`
- `RPEsp_PROCEDENCIA_CONDUTA-VEDADA-PUBLICIDADE.md`
- `PCE_DESAPROVACAO_IRREGULARIDADE-FINANCEIRA.md`

#### Decisões interlocutórias (liminar):
- `RP-LIMINAR_CONCESSAO_FAKE-NEWS-REDES-SOCIAIS.md`
- `RP-LIMINAR_DENEGACAO_LIBERDADE-EXPRESSAO.md`
- `RP-LIMINAR_PARCIAL_FAKE-NEWS-MULTIPLAS.md`
- `RPEsp-LIMINAR_CONCESSAO_PROPAGANDA-INSTITUCIONAL.md`
- `RP_CITACAO_PROPAGANDA-NEGATIVA-WHATSAPP.md`

---

## 🔄 **FLUXO 1: GERAÇÃO DE TEMPLATE A PARTIR DE DOCUMENTO**

### **Quando usar**: 
Quando o usuário fornece uma sentença modelo para criar um template reutilizável.

### **Comando do Usuário**:
```
Gere um template a partir desta sentença: [documento]
```

### **Processo de Geração**:

1. **ANALISAR** o documento fornecido:
   - Identificar tipo de ação
   - Identificar julgamento (procedência/improcedência)
   - Identificar tema principal e temas secundários
   - Identificar estrutura e padrões de redação

2. **GENERALIZAR** a sentença:
   - Substituir dados específicos por placeholders
   - Manter estrutura e estilo de redação
   - Preservar fundamentação jurídica genérica
   - Manter transições e frases de efeito

3. **GERAR** o template com estrutura:
   ```markdown
   # 🏛️ TEMPLATE DE SENTENÇA

   ## 📋 METADADOS
   - **Tipo de Ação**: [identificado]
   - **Julgamento**: [identificado]
   - **Tema Principal**: [identificado]
   - **Temas Secundários**: [lista]
   - **Data de Criação**: [data atual]
   - **Baseado em**: [processo origem, se informado]

   ## 🏛️ SENTENÇA
   [Conteúdo generalizado com placeholders]

   ## 📝 INSTRUÇÕES DE USO
   [Como adaptar ao caso concreto]

   ## 🔄 PLACEHOLDERS
   [Tabela de placeholders e descrições]
   ```

4. **SALVAR** o template:
   - Nome: `[TIPO]_[JULGAMENTO]_[TEMA].md`
   - Local: `TEMPLATES/`

5. **ATUALIZAR** o índice:
   - Adicionar entrada em `INDICE-TEMPLATES.md`

---

## 🔄 **FLUXO 2: SALVAR TEMPLATE APÓS ETAPA 4**

### **Quando usar**: 
Após gerar uma sentença na Etapa 4, o sistema oferece a opção de salvar como template.

### **Questionamento Obrigatório**:
```
📄 SALVAR COMO TEMPLATE?

A sentença foi gerada com sucesso. Deseja salvá-la como template para uso futuro?

- [ ] Sim, salvar como template
- [ ] Não, apenas finalizar

Se SIM, o template será generalizado e salvo em TEMPLATES/
```

### **Processo de Salvamento**:

1. **GENERALIZAR** a sentença gerada:
   - Substituir nome das partes por `[NOME_AUTOR]`, `[NOME_REU]`
   - Substituir número do processo por `[NUMERO_PROCESSO]`
   - Substituir datas por `[DATA_FATO]`, `[DATA_SENTENCA]`
   - Substituir IDs de documentos por `[ID_DOCUMENTO_X]`
   - Manter estrutura, estilo e fundamentação

2. **IDENTIFICAR** metadados:
   - Tipo de ação (do contexto da Etapa 1)
   - Julgamento (procedência/improcedência)
   - Tema principal (do contexto da Etapa 1)

3. **SALVAR** e **INDEXAR** conforme Fluxo 1

---

## 🔄 **FLUXO 3: USO DE TEMPLATE NA ETAPA 4**

### **Quando usar**: 
Na Etapa 4, quando o usuário opta por usar um template do sistema.

### **Questionamento na Etapa 4**:
```
📄 MODELO DE SENTENÇA:

Deseja usar um template modelo do sistema?

- [ ] Sim, mostrar templates disponíveis
- [ ] Não, gerar sem template

Se SIM, farei uma varredura nos templates e sugerirei os mais compatíveis.
```

### **Processo de Uso**:

1. **VARRER** o índice (`INDICE-TEMPLATES.md`):
   - Identificar tipo de ação do caso atual
   - Identificar julgamento escolhido
   - Identificar tema principal

2. **SUGERIR** templates compatíveis:
   ```
   📚 TEMPLATES COMPATÍVEIS:

   Com base no caso (Ação Penal Eleitoral, Improcedência, Corrupção Eleitoral):

   1. ACAO-PENAL_IMPROCEDENCIA_CORRUPCAO-ELEITORAL.md ⭐ (100% compatível)
   2. ACAO-PENAL_IMPROCEDENCIA_COMPRA-VOTOS.md (80% compatível)
   
   Qual deseja usar? (digite o número ou "nenhum")
   ```

3. **CARREGAR** o template escolhido

4. **ADAPTAR** ao caso concreto:
   - Substituir placeholders pelos dados reais
   - Ajustar fundamentação aos fatos específicos
   - Integrar provas e argumentos das etapas anteriores
   - Integrar jurisprudência/doutrina fornecidas

5. **GERAR** a sentença final

---

## 📐 **ESTRUTURA OBRIGATÓRIA DO TEMPLATE**

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
[Corpo da decisão: Relatório → Fundamentação → Dispositivo → Publicação/Citação/MP → Fecho]

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
| `[NOME_REPRESENTADO]` | Representado / Réu | EVILAZIO DE ARAUJO SOUTO |
| `[ZONA_ELEITORAL]` | Zona eleitoral | 56ª ZONA ELEITORAL - JUAZEIRINHO/PB |
| `[CIDADE]` | Cidade | Juazeirinho |
| `[ID_DOCUMENTO_X]` | ID do documento no PJe | ID 123138800 |
| `[NOME_JUIZ]` | Nome do juiz eleitoral | IVNA MOZART BEZERRA SOARES |

---

## ⚠️ **REGRAS ABSOLUTAS**

1. **NUNCA** incluir dados específicos de processo no template
2. **SEMPRE** usar placeholders para dados variáveis
3. **MANTER** a estrutura e estilo de redação do modelo original
4. **PRESERVAR** a qualidade técnica da fundamentação
5. **ATUALIZAR** o índice sempre que criar novo template
6. **VERIFICAR** nomenclatura antes de salvar

---

## 📊 **COMPATIBILIDADE DE TEMPLATES**

Ao sugerir templates, considerar:

| Critério | Peso |
|----------|------|
| Tipo de Ação idêntico | 40% |
| Julgamento idêntico | 30% |
| Tema principal igual ou similar | 30% |

- **100% compatível**: Todos os critérios iguais
- **80% compatível**: Tipo e julgamento iguais, tema similar
- **60% compatível**: Apenas tipo igual
- **Abaixo de 60%**: Não sugerir

---

🏁 **FIM DAS INSTRUÇÕES DE TEMPLATES V2.0**
