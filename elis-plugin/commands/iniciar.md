---
description: Inicia a engenharia de contexto de um processo eleitoral (fluxo ELIS)
argument-hint: [referência ou número do processo]
---

Inicie a engenharia de contexto do processo: $ARGUMENTS

Invoque a skill `elis:fluxo-elis` e siga rigorosamente o fluxo ELIS:

1. Verificar os arquivos do processo na pasta de trabalho atual. Se o usuário não indicou os documentos e nenhum arquivo de processo for encontrado, **solicitar os documentos antes de prosseguir**.
2. Se houver arquivos `.pdf` ou `.docx`, converter para `.md` usando a skill `elis:conversao-arquivos` (Fase 0).
3. Verificar se já existe processo em andamento em `CONTEXTO/` — se houver, informar qual etapa foi concluída e perguntar como prosseguir.
4. Caso contrário, iniciar a **Etapa 1 (Análise FIRAC+)** com a skill `elis:etapa1-analise-firac`.
