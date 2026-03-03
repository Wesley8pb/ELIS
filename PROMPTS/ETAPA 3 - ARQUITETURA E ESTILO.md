# 🏗️ ARQUITETURA DA SENTENÇA (Plano de Decisão Judicial) - V3.0

## 🎯 **OBJETIVO**
Elaborar um **plano estruturado e completo da sentença judicial**, organizando automaticamente todos os elementos decisórios em ordem lógica e sequencial, com base nas análises das etapas anteriores (FIRAC+ e Conjunto Probatório).

**⚠️ PREMISSA FUNDAMENTAL:**
Este plano utiliza automaticamente todos os argumentos e elementos probatórios já identificados na Etapa 2 (Conjunto Probatório), organizando-os em arquitetura decisória coerente conforme o julgamento definido pelo magistrado.

---

## 📋 **INÍCIO AUTOMÁTICO**

**Qual será o julgamento da ação?**

- [ ] **PROCEDÊNCIA** (total ou parcial)
- [ ] **IMPROCEDÊNCIA**

---

## 🏗️ **ESTRUTURA OBRIGATÓRIA DO PLANO**

### **TÍTULO**
```markdown
# 🏛️ PLANO DE SENTENÇA - [TIPO_DE_AÇÃO] - JULGAMENTO: [PROCEDÊNCIA/IMPROCEDÊNCIA]
```

---

### **📋 1. DADOS ESTRUTURAIS DA DECISÃO**

**Apresentar em formato de tabela:**

| Campo | Informação |
|-------|------------|
| **PROCESSO:** | [Número do processo] |
| **TIPO DE AÇÃO:** | [Extrair da análise FIRAC+] |
| **CRIME IMPUTADO/PEDIDO:** | [Conforme FIRAC+] |
| **AUTOR/REQUERENTE:** | [Extrair da análise FIRAC+] |
| **RÉU/REQUERIDO:** | [Extrair da análise FIRAC+] |
| **POSICIONAMENTO ADOTADO:** | [Conforme julgamento definido pelo magistrado] |
| **DATA DE ELABORAÇÃO:** | [Data atual] |

---

### **📝 2. ROTEIRO DO RELATÓRIO**

#### **2.1 Abertura**

**Estrutura Sugerida (em formato de texto corrido para redação):**

> Trata-se de **[TIPO DE AÇÃO]** proposta por **[AUTOR/POLO ATIVO]** em face de **[RÉU/POLO PASSIVO]**, já qualificado(s), [resumo da imputação/pedido].

> Narra a [denúncia/petição inicial] que [síntese dos fatos principais com datas e circunstâncias].

#### **2.2 Narrativa Fática**

**Ordem sugerida para apresentação dos fatos (EM ORDEM CRONOLÓGICA):**

| Ordem | Fato | Referência Probatória |
|-------|------|----------------------|
| 1º | [Fato cronológico inicial] | [Documento (ID XXXXXX, págs. XX-XX)] |
| 2º | [Fato subsequente] | [Documento (ID XXXXXX)] |
| ... | ... | ... |

**Observação:** Esta tabela serve como roteiro. Na redação final, os fatos devem ser narrados em **texto corrido e coeso**, com parágrafos bem detalhados, sem subdivisões visíveis.

#### **2.3 Pedidos Formulados**

**Pedido do [Autor/MPE] (Alegações Finais):**
- [Pedido principal]
- [Pedidos subsidiários, se houver]
- [Sanções requeridas, se aplicável]

#### **2.4 Síntese da Defesa**

**Principais argumentos da defesa (em tabela para organização):**

| Argumento | Síntese |
|-----------|---------|
| [Argumento 1] | [Resumo] |
| [Argumento 2] | [Resumo] |
| [Pedido] | [Síntese do pedido defensivo] |

#### **2.5 Instrução Processual**

**Provas Produzidas (em tabela):**

| Tipo | Descrição | Relevância |
|------|-----------|------------|
| **Documental** | [Listar documentos principais] | [Finalidade probatória] |
| **Testemunhal (Acusação/Autor)** | [Nomes das testemunhas] | [Síntese dos depoimentos] |
| **Testemunhal (Defesa)** | [Nomes das testemunhas] | [Síntese dos depoimentos] |
| **Interrogatório/Depoimento Pessoal** | [Depoimento da parte] | [Pontos relevantes] |

**Manifestações Finais:**
- [Parte A]: Requereu [pedido] (ID XXXXXX)
- [Parte B]: Requereu [pedido] (ID XXXXXX)

---

### **⚖️ 3. ROTEIRO DA FUNDAMENTAÇÃO**

#### **3.1 🔍 QUESTÕES PRELIMINARES**

**Apresentar em tabela:**

| Questão | Posicionamento | Fundamento-Chave |
|---------|---------------|------------------|
| Tempestividade | ✅/❌ | [Fundamento] |
| Legitimidade ativa | ✅/❌ | [Fundamento] |
| Pressupostos processuais | ✅/❌ | [Fundamento] |
| [Outras questões identificadas no FIRAC+] | ✅/❌ | [Fundamento] |

**Se não houver preliminares:** 📌 Não há preliminares pendentes de análise.

---

#### **3.2 ⚖️ ORDEM DOS ARGUMENTOS DE MÉRITO**

**Estratégia Argumentativa:**

[Descrever em parágrafo a estratégia geral: se a fundamentação será construída em ordem decrescente de força, se privilegiará demonstração de cumprimento/não cumprimento do ônus da prova, etc.]

**Hierarquização dos Argumentos (em tabela com sistema de estrelas):**

| Ordem | Argumento | Força | Justificativa da Posição |
|-------|-----------|-------|-------------------------|
| **1º** | [Argumento mais forte] | ⭐⭐⭐⭐⭐ | [Por que este argumento é o mais robusto] |
| **2º** | [Segundo argumento] | ⭐⭐⭐⭐⭐ / ⭐⭐⭐⭐ | [Justificativa] |
| **3º** | [Terceiro argumento] | ⭐⭐⭐⭐ | [Justificativa] |
| ... | ... | ... | ... |

**Sistema de Classificação de Força:**
- ⭐⭐⭐⭐⭐ = Argumento decisivo, prova robusta, fundamento irrefutável
- ⭐⭐⭐⭐ = Argumento forte, prova consistente
- ⭐⭐⭐ = Argumento relevante, prova razoável
- ⭐⭐ = Argumento de reforço, prova complementar
- ⭐ = Argumento fraco ou meramente ilustrativo

---

#### **3.3 DESENVOLVIMENTO DE CADA ARGUMENTO**

**Para cada argumento principal, estruturar conforme o modelo abaixo:**

---

##### **ARGUMENTO [N]: [TÍTULO DO ARGUMENTO]**

**Premissa:**
[Enunciar a premissa jurídica ou fática que fundamenta o argumento]

**Desenvolvimento:**
[Desenvolver o argumento em texto corrido, com parágrafos médios (3-5 linhas), altamente coesos. Utilizar contextualização gradual. Mesclar paráfrases com trechos literais entre aspas nos pontos-chave. Citar sempre os IDs dos documentos entre parênteses, exemplo: (ID 123138800). Quando necessário, especificar páginas do documento.]

**Exemplo de desenvolvimento:**
- [Ponto 1 do argumento com fundamentação]
- [Ponto 2 do argumento com prova documental ou testemunhal]
- [Ponto 3 com citação literal, se aplicável]: "[Trecho literal entre aspas]" (ID XXXXXX, pág. XX)

**Conclusão:**
[Síntese conclusiva do argumento, demonstrando como ele sustenta a tese adotada]

**Provas que sustentam:**
- [Documento/Depoimento 1] (ID XXXXXX)
- [Documento/Depoimento 2] (ID XXXXXX, págs. XX-XX)

**Cadeia Argumentativa Visual:**

```
PREMISSA 1: [Fato incontroverso ou prova robusta]
    ↓
PREMISSA 2: [Norma jurídica aplicável - transcrever literalmente o dispositivo]
    ↓
INFERÊNCIA: [Subsunção fato-norma]
    ↓
CONCLUSÃO: [Tese jurídica]
```

**Exemplo prático aplicado ao caso concreto:**
```
PREMISSA 1: [Descrever o fato específico do caso com referência probatória]
    ↓
PREMISSA 2: [Transcrever literalmente o dispositivo legal aplicável]
    ↓
INFERÊNCIA: [Explicar como o fato se enquadra na norma]
    ↓
CONCLUSÃO: [Tese jurídica específica para este caso]
```

---

**Repetir esta estrutura para cada argumento hierarquizado (do 1º ao último).**

---

#### **3.4 VALORAÇÃO DO CONJUNTO PROBATÓRIO**

**Síntese da Valoração (em tabela):**

| Elemento | Valoração |
|----------|-----------|
| **Prova Documental** | [Análise da força probatória] |
| **Prova Testemunhal (Acusação/Autor)** | [Análise da credibilidade e conteúdo] |
| **Prova Testemunhal (Defesa)** | [Análise da credibilidade e conteúdo] |
| **Interrogatório/Depoimento Pessoal** | [Análise de contradições, confissões, etc.] |
| **Ônus da Prova** | [Quem tinha o ônus e se foi cumprido] |

**Fundamento Jurídico:**
- [Dispositivo legal sobre ônus da prova]
- [Dispositivo legal sobre livre convencimento motivado]
- [Dispositivo legal sobre absolvição/procedência, conforme o caso]

---

#### **3.5 ENFRENTAMENTO DOS ARGUMENTOS CONTRÁRIOS**

**Refutação dos Argumentos da Parte Contrária (em tabela):**

| Argumento da Parte Contrária | Refutação | Fundamento |
|------------------------------|-----------|------------|
| "[Argumento 1]" | [Contra-argumentação] | [Prova/norma que refuta] |
| "[Argumento 2]" | [Contra-argumentação] | [Prova/norma que refuta] |
| ... | ... | ... |

**Observação:** Na redação final, esta refutação deve ser integrada ao texto corrido da fundamentação, sem subdivisões visíveis.

---

#### **3.6 APLICAÇÃO DE DOUTRINA E JURISPRUDÊNCIA (SE FORNECIDAS PELO USUÁRIO)**

**⚠️ REGRA ABSOLUTA: NUNCA CRIAR DOUTRINA OU JURISPRUDÊNCIA. UTILIZAR APENAS AS FORNECIDAS PELO USUÁRIO.**

**Se o usuário forneceu doutrina:**
- Citar moderadamente, apenas quando fortalecer argumento central
- Formato: [Nome do autor], [Obra], [edição], [editora], [ano], [página]

**Se o usuário forneceu jurisprudência:**
- Transcrever trechos relevantes com aspas
- Formato: [Tribunal], [Tipo de Recurso] nº [Número], rel. [Nome do Relator], julg. [Data]
- Exemplo de transcrição: "O Tribunal Superior Eleitoral consolidou o entendimento de que '[trecho literal da ementa ou voto]' (TSE, AR-REsp nº xxx/xx, rel. Min. Fulano de tal, julg. dd/mm/aaaa)."

**Se o usuário NÃO forneceu doutrina ou jurisprudência:**
- NÃO mencionar doutrina ou jurisprudência
- Fundamentar exclusivamente na lei, nas provas e na lógica jurídica

---

### **📌 4. DISPOSITIVO PLANEJADO**

#### **4.1 Resultado do Julgamento**

- [ ] PROCEDÊNCIA total
- [ ] PROCEDÊNCIA PARCIAL
- [x] **[MARCAR A OPÇÃO CONFORME JULGAMENTO DEFINIDO]**

**Fundamentação Legal:**
- [Dispositivo legal que embasa a decisão - transcrever literalmente]

#### **4.2 Consequências da Decisão**

**Apresentar em tabela:**

| Consequência | Observação |
|--------------|------------|
| [Absolvição/Condenação/Procedência/Improcedência/outros julgamentos] | [Fundamento legal] |
| [Sanções aplicadas, se houver] | [Dosimetria, se aplicável] |
| [Restituição de bens, se aplicável] | [Determinação específica] |
| [Outras consequências] | [Detalhamento] |

#### **4.3 Custas e Honorários**

- Sem custas e honorários, sempre

#### **4.4 Providências Finais**

- [ ] Publicação no DJe
- [ ] Intimação pessoal de [parte]
- [ ] Intimação via publicação de [parte]
- [ ] Após trânsito em julgado: [providência]
- [ ] [Outras providências específicas]

---

### **🛡️ 5. BLINDAGEM RECURSAL**

#### **5.1 CHECKLIST DE BLINDAGEM RECURSAL**

**Verifique se o plano de sentença aborda adequadamente:**

- [ ] **Todos os pedidos foram apreciados:** Nenhum pedido principal ou subsidiário foi ignorado
- [ ] **Argumentos centrais da parte perdedora foram refutados:** Cada tese importante da parte contrária foi analisada e desconstruída (verificar seção 3.5)
- [ ] **Precedentes contrários foram distinguidos (se aplicável):** Jurisprudências que poderiam favorecer a parte perdedora foram diferenciadas do caso concreto
- [ ] **Interpretação normativa foi fundamentada:** Escolha interpretativa das normas aplicáveis está justificada
- [ ] **Provas foram valoradas adequadamente:** Análise crítica do conjunto probatório está presente e fundamentada (seção 3.4)
- [ ] **Questões preliminares foram enfrentadas:** Tempestividade, legitimidade, interesse processual foram analisados (seção 3.1)
- [ ] **Proporcionalidade foi observada (se aplicável):** Sanções aplicadas estão adequadamente dosadas e justificadas
- [ ] **Dispositivos legais foram transcritos literalmente:** Sem omissões, alterações ou paráfrases

#### **5.2 Pontos Vulneráveis Identificados**

**Identificar pontos sensíveis para recurso (em tabela):**

| Ponto | Risco | Mitigação Proposta |
|-------|-------|-------------------|
| [Ponto vulnerável 1] | Alto/Médio/Baixo | [Estratégia de reforço argumentativo] |
| [Ponto vulnerável 2] | Alto/Médio/Baixo | [Estratégia de reforço argumentativo] |

#### **5.3 Fundamentação Preventiva**

**Para cada ponto vulnerável de risco médio ou alto, desenvolver:**

**Ponto [N]: [Título do Ponto Vulnerável]**

**Argumento de blindagem:**
[Desenvolver em texto corrido, com parágrafos médios, a fundamentação adicional que blindará este ponto contra questionamento recursal. Utilizar contextualização gradual e coesão textual.]

---

### **✍️ 6. TRECHOS SUGERIDOS PARA A SENTENÇA**

**⚠️ IMPORTANTE: Os trechos abaixo devem seguir rigorosamente o estilo de escrita do magistrado.**

#### **6.1 Trecho de Abertura (Relatório)**

```
Vistos etc.

[Desenvolver parágrafo de abertura em texto corrido, com linguagem equilibrada (técnica quando necessário, mas compreensível), parágrafos médios (3-5 linhas), contextualização gradual, citando IDs dos documentos entre parênteses.]

[Exemplo:]
Trata-se de [TIPO DE AÇÃO] proposta pelo [AUTOR] em face de [RÉU, nome e qualificação], imputando-lhe [síntese da imputação/pedido].

Narra a [denúncia/petição inicial] que [desenvolvimento dos fatos principais, com datas, circunstâncias e referências probatórias com IDs].

[Continuar narrando o trâmite processual: recebimento da denúncia/petição, defesa, audiências, alegações finais, sempre citando IDs dos documentos.]

É o relatório. DECIDO.
```

---

#### **6.2 Trechos de Fundamentação-Chave**

**Trecho 1 - [Título do Argumento Principal]:**

```
[Desenvolver em texto corrido, com parágrafos médios (3-5 linhas), altamente coesos, sem subdivisões visíveis. Utilizar contextualização gradual. Evitar termos extremamente rebuscados. Usar latinismos moderadamente. Mesclar paráfrases com trechos literais entre aspas nos pontos-chave. Citar IDs dos documentos entre parênteses. Transcrever dispositivos legais literalmente, sem omissões ou alterações. Usar ênfases (negrito, itálico) com moderação.]

[Exemplo de estrutura:]
[Parágrafo introdutório contextualizando o argumento]

[Parágrafo desenvolvendo a premissa jurídica, com transcrição literal do dispositivo legal aplicável]

[Parágrafo aplicando a norma ao caso concreto, citando provas com IDs]

[Parágrafo com eventual citação literal de depoimento ou documento]: "Trecho literal entre aspas" (ID XXXXXX, pág. XX).

[Parágrafo conclusivo do argumento]
```

**Repetir para cada argumento principal (Trecho 2, Trecho 3, etc.).**

---

**Trecho [N] - Valoração do Conjunto Probatório:**

```
[Desenvolver síntese da valoração probatória em texto corrido, demonstrando como as provas foram analisadas e qual conclusão se extrai do conjunto. Mencionar se o ônus da prova foi cumprido e por quem.]
```

---

**Trecho [N+1] - Presunção de Inocência / In Dubio Pro Reo / Princípio Aplicável:**

```
[Se aplicável ao caso, desenvolver parágrafo sobre aplicação de princípios constitucionais ou processuais relevantes, com transcrição literal dos dispositivos constitucionais/legais.]
```

---

#### **6.3 Trecho de Dispositivo**

```
DISPOSITIVO

[Frase de transição formal: "Ante o exposto..." ou "Pelo exposto..."]

[Desenvolver dispositivo detalhado, repetindo fundamentos principais da decisão, em texto corrido.]

JULGO [PROCEDENTE/IMPROCEDENTE/PARCIALMENTE PROCEDENTE] [especificar o objeto da ação] para [descrever a decisão específica], com fundamento no [transcrever literalmente o dispositivo legal que embasa a decisão].

[Se houver condenação/sanções, detalhar:]
[Descrever sanções, dosimetria, fundamentação da proporcionalidade]

[Se houver custas e honorários:]
[Detalhar responsabilidade e valores/percentuais]

Publique-se. Registre-se. Intimem-se.

Após o trânsito em julgado, [providências finais].

[Local], [data].

[NOME DO JUIZ/DESEMBARGADOR]
[Cargo]
```

---

### **📎 7. ANEXOS E REFERÊNCIAS**

#### **7.1 Mapa de Referências Probatórias**

**Organizar em tabela todos os documentos citados:**

| ID | Documento | Páginas | Relevância | Uso na Sentença |
|----|-----------|---------|------------|-----------------|
| [ID] | [Nome do documento] | [págs. XX-XX] | [Finalidade probatória] | [Seção/Argumento onde será usado] |
| ... | ... | ... | ... | ... |

#### **7.2 Referências Jurisprudenciais (SE FORNECIDAS PELO USUÁRIO)**

**⚠️ INCLUIR APENAS SE O USUÁRIO FORNECEU JURISPRUDÊNCIA.**

| Tribunal | Processo | Ementa/Trecho Relevante | Aplicação |
|----------|----------|------------------------|-----------|
| [Tribunal] | [Tipo e número] | "[Trecho literal]" | [Argumento onde será citada] |

#### **7.3 Referências Doutrinárias (SE FORNECIDAS PELO USUÁRIO)**

**⚠️ INCLUIR APENAS SE O USUÁRIO FORNECEU DOUTRINA.**

| Autor | Obra | Edição/Ano | Página | Aplicação |
|-------|------|-----------|--------|-----------|
| [Nome] | [Título] | [Dados] | [pág. XX] | [Argumento onde será citada] |

#### **7.4 Referências Legais**

**Listar todos os dispositivos legais aplicados:**

| Dispositivo | Conteúdo (transcrição literal) | Aplicação |
|-------------|-------------------------------|-----------|
| [Art. XX, Lei/Código] | "[Transcrição literal completa]" | [Finalidade na sentença] |

---

### **🎯 8. SÍNTESE EXECUTIVA DO PLANO**

**Resumo automático baseado na deliberação da Etapa 2 e julgamento definido:**

**Linha decisória em síntese:**
- **Julgamento:** [Procedência/Improcedência/Procedência Parcial]
- **Fundamento principal:** [Tese central em uma frase]
- **Argumentos-chave:** 
  1. [Argumento mais forte]
  2. [Segundo argumento mais forte]
  3. [Terceiro argumento mais forte]
- **Diferencial da decisão:** [O que torna esta fundamentação sólida e blindada]

---

## 📐 **ESTILO DE ESCRITA DO MAGISTRADO**

**⚠️ TODOS OS TRECHOS SUGERIDOS DEVEM SEGUIR RIGOROSAMENTE ESTAS DIRETRIZES:**

### **1. TOM E LINGUAGEM**
- **Formalidade:** Equilibrado (técnico quando necessário, mas compreensível)
- **Latinismos:** Usar moderadamente (apenas os mais consagrados: in dubio pro reo, ratio decidendi, etc.)
- **Referência às partes:** Nome + qualificação (ex: "o réu Thiago de Oliveira", "o denunciado")

### **2. ESTRUTURA TEXTUAL**
- **Parágrafos:** Médios (3-5 linhas)
- **Coesão:** Parágrafos altamente coesos, com transições claras entre ideias
- **Subdivisões:** NÃO usar subtítulos ou marcadores visíveis na fundamentação. Preferir texto corrido sem subdivisões aparentes
- **Listas e enumerações:** Evitar. Preferir texto dissertativo

### **3. ARGUMENTAÇÃO**
- **Início da fundamentação:** Contextualização gradual (preparar terreno antes da tese principal)
- **Doutrina:** Citar moderadamente, APENAS quando fornecida pelo usuário. **NUNCA CRIAR DOUTRINA.**
- **Jurisprudência:** Transcrever trechos relevantes com aspas, APENAS quando fornecida pelo usuário. **NUNCA CRIAR JURISPRUDÊNCIA.**

### **4. ELEMENTOS ESTILÍSTICOS**
- **Perguntas retóricas:** NÃO usar. Preferir afirmações diretas
- **Analogias/metáforas:** Usar moderadamente, apenas quando necessário para esclarecer conceitos complexos
- **Ênfases (negrito, itálico, MAIÚSCULAS):** Usar com moderação

### **5. CITAÇÕES E REFERÊNCIAS**
- **Dispositivos legais:** Formato médio: "art. 299 do Código Eleitoral"
- **Transcrição de dispositivos:** SEMPRE literal, sem omissões, alterações ou paráfrases
- **Depoimentos:** Mesclar paráfrase + trechos literais entre aspas nos pontos-chave
- **IDs de documentos:** SEMPRE citar entre parênteses, exemplo: (ID 123138800)
- **Páginas:** Quando necessário, especificar: (ID 123138800, págs. 10-16)

### **6. TRANSIÇÃO E DISPOSITIVO**
- **Transição para dispositivo:** Frase formal ("Ante o exposto...", "Pelo exposto...")
- **Estilo do dispositivo:** Detalhado (repetir fundamentos principais)

### **7. EVITAR**
- ❌ Termos extremamente rebuscados
- ❌ Uso de hífens em substituição a vírgulas
- ❌ Bullet points desnecessários
- ❌ Gerundismo excessivo
- ❌ Voz passiva excessiva
- ❌ Criação de doutrina ou jurisprudência não fornecida pelo usuário

### **8. PRIORIZAR**
- ✅ Clareza e objetividade
- ✅ Coesão textual entre parágrafos
- ✅ Contextualização gradual dos argumentos
- ✅ Transcrição literal de dispositivos legais
- ✅ Citação precisa de IDs e páginas de documentos
- ✅ Texto corrido sem subdivisões visíveis na fundamentação

---

## ✅ **CRITÉRIOS PARA AVANÇAR PARA ETAPA 4 (MINUTA DA SENTENÇA)**

Antes de prosseguir, verifique se você possui:

- [ ] **Julgamento** claramente definido pelo magistrado
- [ ] **Roteiro da fundamentação** estruturado em sequência lógica
- [ ] **Linha argumentativa** hierarquizada e coerente (com sistema de estrelas)
- [ ] **Cadeia argumentativa visual** estruturada para argumentos principais
- [ ] **Trechos sugeridos** redigidos conforme estilo do magistrado
- [ ] **Dispositivo** completamente planejado
- [ ] **Antecipação recursal** realizada
- [ ] **Checklist de blindagem recursal** verificado (todos os itens ✅)
- [ ] **Mapa de referências probatórias** completo (com IDs e páginas)
- [ ] **Plano aprovado** pelo magistrado (com ou sem adaptações)

