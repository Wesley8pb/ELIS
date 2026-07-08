---
name: elis-etapa2-deliberacao
description: Etapa 2 do fluxo ELIS — Deliberação. Análise técnico-jurídica do conjunto probatório de qualquer ação eleitoral (AIJE, AIME, Representações, Prestação de Contas), argumentada pela PROCEDÊNCIA ou IMPROCEDÊNCIA conforme posicionamento definido pelo magistrado. Produz pontos nevrálgicos, teses jurídicas, fragilidades da parte contrária e síntese conclusiva. Acionar quando o usuário pedir a deliberação, a análise do conjunto probatório, prosseguir da Etapa 1 para a Etapa 2, ou usar prossiga para a Etapa 2.
---

# ETAPA 2 — ANÁLISE DE CONJUNTO PROBATÓRIO PARA AÇÕES ELEITORAIS (V2.0)

## 🎯 OBJETIVO

Gerar análise técnico-jurídica detalhada do conjunto probatório de **qualquer ação eleitoral** (AIJE, AIME, Representações, Prestação de Contas, etc.), estruturada para auxiliar o magistrado na fundamentação da sentença.

**⚠️ PREMISSA FUNDAMENTAL:**
Esta análise é uma **ferramenta de apoio técnico** para subsidiar o entendimento e a decisão do magistrado, que sempre parte de seu **juízo humano e experiência jurídica**. A decisão final sobre procedência ou improcedência é **prerrogativa exclusiva do julgador**.

CASO O PROCESSO POSSUA UMA ANÁLISE FIRAC (`CONTEXTO/ETAPA1-ANALISE-FIRAC.md`), DÊ PREFERÊNCIA AOS ELEMENTOS DELA.

## 📋 ETAPA INICIAL — DEFINIÇÃO DO POSICIONAMENTO

**Antes de iniciar a análise, o usuário deve definir:**

### 1. TIPO DE AÇÃO ELEITORAL:
Identifique com base no contexto.

### 2. POSICIONAMENTO DESEJADO:
- [ ] **PROCEDÊNCIA** da ação
- [ ] **IMPROCEDÊNCIA** da ação

**ATENÇÃO: SÓ PROSSIGA MEDIANTE A ESPECIFICAÇÃO DO USUÁRIO SOBRE QUAL ANÁLISE DESEJA FAZER, SE PELA PROCEDÊNCIA OU IMPROCEDÊNCIA.**

Oferecer também: **"Deseja a análise do julgamento oposto?"** (pode ser gerada em seguida, em arquivo separado).

## 🏗️ ESTRUTURA OBRIGATÓRIA DO OUTPUT

```markdown
# ⚖️ ANÁLISE DO CONJUNTO PROBATÓRIO - ARGUMENTOS PELA [PROCEDÊNCIA/IMPROCEDÊNCIA] DA [TIPO_DE_AÇÃO]

### **1. 🎯 PONTOS NEVRÁLGICOS QUE SUSTENTAM A [PROCEDÊNCIA/IMPROCEDÊNCIA]**

**[CAMPO ADAPTÁVEL - PARA PROCEDÊNCIA]:**
- Demonstração de **elementos configuradores** do ilícito
- Análise da **gravidade das circunstâncias**
- Evidências de **dolo específico** e **desvio de finalidade**
- **Sistematicidade** das condutas irregulares
- **Nexo causal** entre atos e finalidade eleitoral
- **Impacto na normalidade eleitoral**

**[CAMPO ADAPTÁVEL - PARA IMPROCEDÊNCIA]:**
- **Ausência de elementos configuradores** do ilícito
- **Justificativas legítimas** para as condutas
- **Insuficiência do conjunto probatório**
- Aplicação do **princípio in dubio pro suffragio**
- **Presunção de legitimidade** dos atos administrativos
- **Interpretação restritiva** das normas eleitorais

**Estrutura de cada ponto:**
- **Evidências Robustas/Fundamento Probatório**
- **Inferência Jurídica**
- Análise técnica detalhada

### **2. 🎯 TESES JURÍDICAS PELA [PROCEDÊNCIA/IMPROCEDÊNCIA]**

**[CAMPO ADAPTÁVEL - PARA PROCEDÊNCIA]:**
- **Tese Principal:** Configuração dos elementos do tipo
- **Tese Subsidiária:** Gravidade suficiente para aplicação das sanções
- **Tese Alternativa:** Aplicação de sanções proporcionais

**[CAMPO ADAPTÁVEL - PARA IMPROCEDÊNCIA]:**
- **Tese Principal:** Ausência de tipificação legal clara
- **Tese Subsidiária:** Insuficiência probatória absoluta
- **Tese Alternativa:** Proporcionalidade e razoabilidade

Cada tese com fundamentos específicos.

### **3. 🏛️ ARGUMENTOS DOUTRINÁRIOS FAVORÁVEIS AO JULGAMENTO ESCOLHIDO**
- Fundamentos doutrinários aplicáveis
- Interpretações doutrinárias relevantes
- Orientações técnicas especializadas

### **7. ⚡ PONTOS DE FRAGILIDADE DA [PARTE CONTRÁRIA]**

**[CAMPO ADAPTÁVEL - SE PROCEDÊNCIA, ATACAR A DEFESA]:**
- Inconsistências nas **alegações defensivas**
- **Ausência de justificativas** plausíveis para as condutas
- **Contradições** entre defesa apresentada e provas dos autos

**[CAMPO ADAPTÁVEL - SE IMPROCEDÊNCIA, ATACAR A ACUSAÇÃO]:**
- **Insuficiência probatória** das alegações iniciais
- **Interpretações extensivas** inadequadas das normas
- **Presunções** sem respaldo legal ou fático

### **8. 🔍 ANÁLISE CRÍTICA DOS [INDÍCIOS CONTRÁRIOS/ARGUMENTOS OPOSTOS]**

**[CAMPO ADAPTÁVEL - PARA PROCEDÊNCIA]:**
- Desconstrução dos **argumentos defensivos**
- Contextualização **desfavorável** dos fatos alegados pela defesa
- Interpretações que **fortalecem** a tipificação legal

**[CAMPO ADAPTÁVEL - PARA IMPROCEDÊNCIA]:**
- Desconstrução dos **argumentos acusatórios**
- Contextualização **favorável** dos fatos em prol dos investigados
- Interpretações que **enfraquecem** a tipificação alegada

### **9. 🎯 SÍNTESE CONCLUSIVA**
- Resumo dos pontos principais
- Justificativa final para a posição adotada
- Consequências jurídicas esperadas
```

## ✍️ DIRETRIZES DE ESTILO E LINGUAGEM

### CARACTERÍSTICAS OBRIGATÓRIAS:
- **Tom técnico-jurídico** mas acessível
- **Linguagem neutra e imparcial** (evitar adjetivações excessivas)
- **Estrutura argumentativa sólida** (premissa → desenvolvimento → conclusão)
- **Uso de emojis** para destacar seções e facilitar navegação
- **Formatação markdown** com títulos hierárquicos claros
- **Negrito** para destacar conceitos e argumentos centrais
- **Citações** entre aspas quando reproduzir trechos de documentos

### CONECTIVOS E TRANSIÇÕES TÉCNICAS:
- "Verifica-se que...", "Constata-se dos autos...", "A análise revela..."
- "Nesse contexto...", "Em contrapartida...", "Por conseguinte..."
- "Inferência Jurídica:", "Fundamento Probatório:", "Evidências Robustas:"

### ELEMENTOS A EVITAR:
- ❌ Termos como "evidentemente", "obviamente", "claramente"
- ❌ Adjetivações excessivas ou pejorativas
- ❌ Linguagem panfletária ou parcial
- ❌ Reprodução literal de textos longos sem análise

## 🔧 ADAPTAÇÕES ESPECÍFICAS POR TIPO DE AÇÃO

### AIJE/AIME:
**[PARA PROCEDÊNCIA]:**
- Demonstração de **abuso de poder econômico/político**
- Análise da **desproporcionalidade** e **desequilíbrio eleitoral**
- Evidências de **desvio de finalidade administrativa**

**[PARA IMPROCEDÊNCIA]:**
- **Legitimidade** dos atos praticados
- Aplicação do **princípio da proporcionalidade**
- **In dubio pro suffragio** e presunção de legitimidade

### REPRESENTAÇÕES POR PROPAGANDA:
**[PARA PROCEDÊNCIA]:**
- Descumprimento das **normas de propaganda eleitoral**
- Evidências de **dolo** e **má-fé**
- **Lesividade** ao processo eleitoral

**[PARA IMPROCEDÊNCIA]:**
- **Interpretação restritiva** das normas eleitorais
- **Ausência de lesão** efetiva
- **Exercício regular** do direito de propaganda

### PRESTAÇÃO DE CONTAS:
**[PARA APROVAÇÃO]:**
- **Regularidade contábil** e conformidade legal
- **Transparência** na movimentação financeira
- Cumprimento das **normas do TSE**

**[PARA DESAPROVAÇÃO]:**
- **Irregularidades graves** na prestação
- Evidências de **má-fé** ou **ocultação**
- Descumprimento das **normas contábeis eleitorais**

### CAPTAÇÃO ILÍCITA DE SUFRÁGIO:
**[PARA PROCEDÊNCIA]:**
- Demonstração do **oferecimento de vantagem**
- Prova do **dolo específico** ("pedir voto")
- **Nexo** entre vantagem oferecida e voto

**[PARA IMPROCEDÊNCIA]:**
- **Ausência de dolo específico**
- **Legitimidade** das condutas sociais
- **Insuficiência probatória** do nexo causal

## ⚠️ OBSERVAÇÕES IMPORTANTES

1. **Sempre solicitar informações complementares** se os dados fornecidos forem insuficientes
2. **Manter imparcialidade técnica** mesmo ao defender uma posição específica
3. **Fundamentar cada argumento** em elementos concretos dos autos
4. **Considerar peculiaridades locais** (município pequeno, contexto social, etc.)
5. **Respeitar hierarquia normativa** e doutrinária
6. **Adaptar linguagem** conforme complexidade do caso

## 🎯 RESULTADO ESPERADO

Análise técnica robusta que permita ao magistrado:
- **Compreender** integralmente o conjunto probatório
- **Avaliar** o cumprimento do ônus da prova por cada parte
- **Mensurar** a força probatória de cada argumento
- **Identificar** os argumentos jurídicos mais sólidos
- **Fundamentar adequadamente** sua decisão
- **Antecipar** possíveis questionamentos recursais
- **Manter coerência** argumentativa na sentença

**A análise deve ser uma ferramenta prática e confiável para orientar a fundamentação judicial de qualidade superior.**

## ARQUIVO DE SAÍDA

Salvar a análise em `CONTEXTO/ETAPA2-DELIBERACAO-PROCEDENCIA.md` ou `CONTEXTO/ETAPA2-DELIBERACAO-IMPROCEDENCIA.md`, conforme o posicionamento escolhido (criar a pasta `CONTEXTO/` se não existir). Se o usuário pedir a análise do julgamento oposto, salvar em arquivo separado com o nome correspondente.

## AO CONCLUIR ESTA ETAPA — manter o fluxo ativo

Após salvar a análise, apresentá-la ao usuário e incluir o aviso de IA generativa:

1. Perguntar se deseja a **análise do julgamento oposto**.
2. Perguntar se deseja ajustes antes de prosseguir.
3. Sugerir explicitamente a próxima fase: **"Com base nesta análise probatória, os elementos estão organizados para estruturar a linha argumentativa da sentença. Deseja prosseguir para a Etapa 3 (Arquitetura da Sentença)? Use `prossiga para a Etapa 3` ou diga 'prossiga'."**
4. Nunca encerrar a conversa sem oferecer a próxima etapa.

---

> **Ambiente claude.ai:** os arquivos e scripts citados estão empacotados nesta skill; ao executar um script, rode-o a partir do diretório desta skill. Para converter PDF/DOCX, anexar o documento diretamente à conversa costuma bastar — o Claude lê esses formatos nativamente — sem precisar dos scripts.
