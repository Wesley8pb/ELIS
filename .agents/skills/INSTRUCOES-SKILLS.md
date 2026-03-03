# 🛠️ Instruções para Criação de Skills (Padrão skill_creator)

Este documento define o padrão obrigatório para a criação de novas *skills* no projeto, seguindo o modelo `skill_creator` da Anthropic/Antigravity.

## 📋 Padrão de Cabeçalho (YAML Frontmatter)

Toda nova skill deve começar obrigatoriamente com um bloco de metadados YAML no topo do arquivo `SKILL.md`. Este bloco é o que permite ao Antigravity identificar quando a skill deve ser carregada.

### Estrutura Obrigatória:
```yaml
---
name: nome-da-skill-em-kebab-case
description: Descrição detalhada da funcionalidade e critérios de ativação.
---
```

### Regras dos Campos:

1.  **`name`**:
    *   Deve estar em **kebab-case** (letras minúsculas e hifens).
    *   Deve ser único e, preferencialmente, igual ao nome da pasta da skill.
    *   Máximo de 64 caracteres.

2.  **`description`**:
    *   É o campo mais crítico, pois define o **gatilho de ativação**.
    *   Deve descrever claramente **o que a skill faz** e **quando deve ser usada**.
    *   Deve mencionar classes processuais, palavras-chave ou condições específicas (ex: "Ativada quando detectar classe RP e pedido de liminar").
    *   Máximo de 1024 caracteres.

## 🏗️ Estrutura de Pastas da Skill

Cada skill deve estar em sua própria subpasta dentro de `.agents/skills/`:

```
📂 .agents/skills/
└── 📂 nome-da-skill/
    ├── SKILL.md          # Arquivo principal com cabeçalho YAML e instruções
    ├── reference.md      # (Opcional) Referências técnicas ou legais
    └── scripts/          # (Opcional) Scripts específicos da skill
```

## 📝 Exemplo de `SKILL.md`

```markdown
---
name: minha-nova-skill
description: Skill ativada quando o processo trata de [TEMA ESPECÍFICO]. Serve para realizar [AÇÃO X] e [AÇÃO Y], garantindo a aplicação do [ARTIGO LEGAL].
---

# Título da Skill

## Regras Gerais
...

## Tarefas
...

## Exemplos
...
## Legislação [quando aplicável]
...     

## Checklist
...

## Outros campos necessários de acordo com o escopo da skill
...

```

---
*Documento criado em: 11/02/2026*
*Versão: 1.0*
