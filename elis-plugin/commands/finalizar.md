---
description: Finaliza o processo do fluxo ELIS — arquiva os artefatos em PROCESSOS CONCLUIDOS/ e limpa a área de trabalho
argument-hint: [número do processo, opcional]
---

Finalize o processo do fluxo ELIS. $ARGUMENTS

Siga o procedimento de finalização da skill `elis:fluxo-elis`:

1. Criar a pasta `PROCESSOS CONCLUIDOS/[NÚMERO_DO_PROCESSO]/` na pasta de trabalho atual (formato do número: `NNNNNNN-DD.AAAA.J.TT.OOOO`).
2. COPIAR os arquivos do processo (raiz da pasta de trabalho) para a nova pasta.
3. COPIAR os arquivos de `CONTEXTO/` para a nova pasta.
4. DELETAR os originais da raiz e de `CONTEXTO/`.
5. VERIFICAR que a raiz e `CONTEXTO/` estão limpos.
6. Confirmar a conclusão ao usuário, listando os arquivos arquivados.
