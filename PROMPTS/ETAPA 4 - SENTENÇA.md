# ⚖️ SENTENÇA JUDICIAL (Documento Final) - V1.0

## 🎯 **OBJETIVO**
Gerar a **sentença judicial de EXCELÊNCIA completa e fundamentada**, pronta para uso, com base no contexto construído nas etapas anteriores (FIRAC+, Deliberação e Arquitetura).

**⚠️ PREMISSAS FUNDAMENTAIS:**
1. Esta sentença utiliza automaticamente todos os elementos das Etapas 1, 2 e 3
2. O estilo de escrita do magistrado deve ser aplicado rigorosamente
3. Jurisprudência e doutrina são APENAS as fornecidas pelo usuário
4. NUNCA CRIAR jurisprudência ou doutrina inexistentes
5. Transcrever os dispositivos legais literalmente, sem omissões, alterações ou parafrases

---

## 📚 **COLETA DE MATERIAIS COMPLEMENTARES**

Antes de gerar a sentença, solicitar ao usuário:

### **1. JURISPRUDÊNCIA**

```
📚 JURISPRUDÊNCIA PARA CITAÇÃO:

Por favor, forneça as jurisprudências que deseja citar na sentença.

Opções:
- Cole as ementas ou trechos relevantes dos julgados
- Forneça a referência completa (Tribunal, número, relator, data)
- Digite "Nenhuma" para prosseguir sem jurisprudência

⚠️ REGRA ABSOLUTA: O agente NÃO irá criar jurisprudência. 
Apenas utilizará as fornecidas pelo usuário.

Jurisprudência fornecida:
```

### **2. DOUTRINA**

```
📖 DOUTRINA PARA CITAÇÃO:

Por favor, forneça as citações doutrinárias que deseja incluir.

Formato esperado:
- Nome do autor
- Título da obra
- Edição, editora, ano
- Página(s)
- Trecho a ser citado (opcional)

Digite "Nenhuma" para prosseguir sem doutrina.

⚠️ REGRA ABSOLUTA: O agente NÃO irá criar doutrina. 
Apenas utilizará as fornecidas pelo usuário.

Doutrina fornecida:
```

### **3. MODELO DE SENTENÇA (TEMPLATE)**

```
📄 MODELO DE SENTENÇA:

Deseja usar um modelo de sentença para servir de template?

Opções:
- [ ] Usar template do SISTEMA (templates salvos no projeto)
- [ ] Fornecer um modelo EXTERNO (cole o texto ou forneça o arquivo)
- [ ] Não usar template (gerar com estrutura padrão do Framework)

Se escolher "SISTEMA", farei uma varredura nos templates disponíveis 
e sugerirei os mais compatíveis com o caso atual.

Se escolher "EXTERNO", o agente adaptará a estrutura do modelo ao caso concreto,
mantendo o estilo e formatação do template fornecido.
```

### **3.1 USO DE TEMPLATE DO SISTEMA**

Se o usuário escolher usar template do sistema:

1. **VARRER** o índice (`TEMPLATES/INDICE-TEMPLATES.md`)
2. **IDENTIFICAR** templates compatíveis com:
   - Tipo de ação do caso atual
   - Julgamento escolhido (procedência/improcedência)
   - Tema principal

3. **SUGERIR** templates compatíveis:
```
📚 TEMPLATES COMPATÍVEIS:

Com base no caso atual ([Tipo de Ação], [Julgamento], [Tema]):

1. [NOME_TEMPLATE_1].md ⭐ (100% compatível)
2. [NOME_TEMPLATE_2].md (80% compatível)

Qual deseja usar? (digite o número ou "nenhum")
```

4. **CARREGAR** o template escolhido
5. **ADAPTAR** ao caso concreto (substituir placeholders pelos dados reais)

**Critérios de Compatibilidade:**
| Critério | Peso |
|----------|------|
| Tipo de Ação idêntico | 50% |
| Julgamento idêntico | 30% |
| Tema principal igual/similar | 20% |

**Instruções completas**: Consulte `TEMPLATES/INSTRUCOES-TEMPLATES.md`

---

## 🏛️ **ESTRUTURA OBRIGATÓRIA DA SENTENÇA**

### **CABEÇALHO**

```
PODER JUDICIÁRIO
TRIBUNAL REGIONAL ELEITORAL DA PARAÍBA
[ZONA ELEITORAL]

SENTENÇA

PROCESSO: [Número completo]
CLASSE: [Tipo de Ação]
AUTOR/REQUERENTE: [Nome completo]
RÉU/REQUERIDO: [Nome completo]
```

### **RELATÓRIO**

**Diretrizes:**
- Texto corrido, parágrafos médios (3-5 linhas), altamente coeso
- Contextualização gradual dos fatos
- Citar IDs dos documentos entre parênteses
- Seguir o roteiro da seção 2 da Arquitetura (Etapa 3)
- Reaproveitar o trecho sugerido 6.1 da Etapa 3

**Estrutura:**
```
Vistos etc.

[Parágrafo de abertura: tipo de ação, partes, síntese da imputação/pedido]

[Parágrafos de desenvolvimento: narração cronológica dos fatos principais]

[Parágrafos processuais: recebimento, citação, defesa, audiência, alegações]

É o relatório. DECIDO.
```

---

### **FUNDAMENTAÇÃO**

**Diretrizes Gerais:**
- Texto corrido, SEM subdivisões visíveis (sem subtítulos na versão final)
- Parágrafos médios (3-5 linhas), altamente coesos
- Contextualização gradual dos argumentos
- Transcrição literal dos dispositivos legais
- Citar IDs dos documentos entre parênteses
- Mesclar paráfrases com trechos literais entre aspas nos trechos de audiências (se houver)
- Integrar jurisprudência e doutrina fornecidas

**Sequência Recomendada:**

#### A) Questões Preliminares (se houver)
- Analisar em texto corrido, integrado ao corpo da fundamentação
- Resolver cada questão antes de avançar ao mérito

#### B) Tipificação / Enquadramento Jurídico
- Apresentar o tipo legal aplicável
- Transcrever literalmente o dispositivo legal
- Explicar os elementos configuradores

#### C) Argumentação Hierarquizada
- Iniciar pelo argumento mais forte (conforme hierarquização da Etapa 3)
- Desenvolver cada argumento com: premissa → análise probatória → conclusão
- Citar provas com IDs e páginas
- Transcrever trechos de depoimentos entre aspas nos pontos-chave
- Integrar jurisprudência fornecida (se aplicável)

#### D) Valoração do Conjunto Probatório
- Síntese da análise probatória
- Conclusão sobre cumprimento do ônus da prova
- Aplicação de princípios (in dubio pro reo, livre convencimento, in dubio pro suffragio e etc.)

#### E) Refutação de Argumentos Contrários
- Integrar ao texto corrido (sem seção separada)
- Demonstrar por que os argumentos da parte contrária não prosperam

#### F) Integração de Jurisprudência (SE FORNECIDA)
```
Nesse sentido, o [Tribunal Superior Eleitoral/Supremo Tribunal Federal] consolidou o entendimento de que "[trecho literal da ementa ou voto fornecido]" ([Referência completa fornecida pelo usuário]).
```

#### G) Integração de Doutrina (SE FORNECIDA)
```
Na lição de [Nome do autor], "[trecho literal fornecido]" ([Referência bibliográfica completa]).
```

#### H) Conclusão da Fundamentação
- Parágrafo de síntese antes do dispositivo
- Preparar transição para a decisão

---

### **DISPOSITIVO**

**Diretrizes:**
- Iniciar com frase de transição formal ("Ante o exposto...", "Pelo exposto...")
- Detalhado, repetindo fundamentos principais
- Transcrever literalmente o dispositivo legal que embasa a decisão
- Incluir todas as consequências da decisão
- Determinar formas de publicação e intimações

**Estrutura:**

```
DISPOSITIVO

[Frase de transição formal]

JULGO [PROCEDENTE/IMPROCEDENTE/PARCIALMENTE PROCEDENTE] a presente [tipo de ação], [especificar objeto], para [descrever a decisão específica: absolver/condenar/declarar/desconstituir], com fundamento no [transcrever literalmente o dispositivo legal].

[Se condenação/procedência:]
[Descrever sanções aplicadas com dosimetria fundamentada]
[Especificar penas, multas, cassações, inelegibilidades]

[Se absolvição/improcedência:]
[Declarar a absolvição/improcedência com fundamento específico]

[Custas e honorários:]
[Definir responsabilidade ou isenção]

[Providências finais:]
Publique-se via DJE. Registre-se. Intimem-se.

Vistas ao MPE via sistema com as prerrogativas legais

Após o trânsito em julgado, [providências específicas: arquivamento, comunicações, etc.].

[Cidade], [data por extenso].

[NOME DO JUIZ ELEITORAL]
Juiz(a) Eleitoral da [Zona] Zona Eleitoral
```

---

> **Estilo de escrita:** aplicar as diretrizes da seção `ESTILO DE ESCRITA DO MAGISTRADO` definidas na Etapa 3 — texto corrido, parágrafos médios (3–5 linhas), sem subdivisões visíveis na fundamentação, nunca criar jurisprudência ou doutrina.

---

## ✅ **CHECKLIST DE QUALIDADE DA SENTENÇA**

Antes de apresentar a sentença final, verificar:

### **Estrutura**
- [ ] Cabeçalho completo com dados do processo
- [ ] Ementa presente e adequada
- [ ] Relatório completo e coeso
- [ ] Fundamentação em texto corrido
- [ ] Dispositivo detalhado e fundamentado

### **Conteúdo**
- [ ] Todos os pedidos foram apreciados no dispositivo
- [ ] Argumentos da parte perdedora foram refutados
- [ ] Dispositivos legais transcritos literalmente
- [ ] IDs de documentos citados corretamente
- [ ] Provas valoradas adequadamente

### **Materiais Externos**
- [ ] Jurisprudência integrada conforme fornecido (se aplicável)
- [ ] Doutrina integrada conforme fornecido (se aplicável)
- [ ] NÃO foi criada jurisprudência ou doutrina inexistente

### **Estilo**
- [ ] Parágrafos médios (3-5 linhas)
- [ ] Texto corrido sem subdivisões visíveis na fundamentação
- [ ] Latinismos usados moderadamente
- [ ] Citações e referências no formato correto
- [ ] Transições claras entre argumentos

### **Blindagem Recursal**
- [ ] Fundamentação completa em todos os pontos sensíveis
- [ ] Precedentes distinguidos (se aplicável)
- [ ] Proporcionalidade observada (se sanções aplicadas)

---

## 🔧 **REVISÃO E AJUSTES FINAIS**

**Após apresentar a sentença completa, questionar:**

```
📝 REVISÃO DA SENTENÇA:

A sentença foi gerada com base no contexto das etapas anteriores, 
aplicando o estilo de escrita definido e integrando os materiais fornecidos.

Deseja fazer ajustes?

- [ ] Manter a sentença como está
- [ ] Ajustar trechos específicos (indicar quais)
- [ ] Reforçar fundamentação em pontos específicos
- [ ] Adicionar jurisprudência/doutrina adicional
- [ ] Modificar linguagem ou tom
- [ ] Ajustar ementa
- [ ] Revisar dispositivo

Por favor, indique suas preferências para ajuste final.
```

---
## 🏁 **FINALIZAÇÃO DO PROCESSO**

**Após aprovação da sentença:**

1. **Salvar** a sentença em `CONTEXTO/ETAPA4-SENTENCA-FINAL.md`
2. **Consultar** se o usuário deseja ajustes finais
3. **Confirmar** conclusão do processamento
4. **Mover** todos os arquivos para `PROCESSOS CONCLUIDOS/[NÚMERO]/`

**Mensagem de Conclusão:**
```
✅ Engenharia de contexto do processo [NÚMERO] concluída com sucesso!

📁 Arquivos gerados:
- ETAPA1-ANALISE-FIRAC.md
- ETAPA2-DELIBERACAO-[TIPO].md
- ETAPA3-ARQUITETURA-SENTENCA.md
- ETAPA4-SENTENCA-FINAL.md

Os arquivos foram movidos para PROCESSOS CONCLUIDOS/[NÚMERO]/

🎯 A sentença está pronta para revisão final e utilização.
```

---

## 📄 **SALVAR COMO TEMPLATE**

**Após geração da sentença, SEMPRE questionar:**

```
📄 SALVAR COMO TEMPLATE?

A sentença foi gerada com sucesso. Deseja salvá-la como template para uso futuro?

- [ ] Sim, salvar como template
- [ ] Não, apenas finalizar

Se SIM:
- O template será generalizado (dados específicos substituídos por placeholders)
- Será salvo em TEMPLATES/ com nomenclatura padrão
- O índice INDICE-TEMPLATES.md será atualizado automaticamente
```

**Processo de Salvamento como Template:**

1. **GENERALIZAR** a sentença:
   - Substituir nome das partes por `[NOME_AUTOR]`, `[NOME_REU]`
   - Substituir número do processo por `[NUMERO_PROCESSO]`
   - Substituir datas por `[DATA_FATO]`, `[DATA_SENTENCA]`
   - Substituir IDs de documentos por `[ID_DOCUMENTO_X]`
   - Manter estrutura, estilo e fundamentação

2. **IDENTIFICAR** metadados:
   - Tipo de ação (do contexto da Etapa 1)
   - Julgamento (procedência/improcedência)
   - Tema principal (do contexto da Etapa 1)

3. **NOMEAR** o template:
   - Formato: `[TIPO-ACAO]_[JULGAMENTO]_[TEMA-PRINCIPAL].md`
   - Ex: `ACAO-PENAL_IMPROCEDENCIA_CORRUPCAO-ELEITORAL.md`

4. **SALVAR** em `TEMPLATES/`

5. **ATUALIZAR** `TEMPLATES/INDICE-TEMPLATES.md`

**Instruções completas**: Consulte `TEMPLATES/INSTRUCOES-TEMPLATES.md`
