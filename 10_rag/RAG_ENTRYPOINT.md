# RAG Entrypoint

Questo e il punto di ingresso primario per usare la knowledge base come contesto AI durante l'esame.

## Ordine di apertura

1. `10_rag/RAG_SYSTEM_RULES.md`
2. `10_rag/RAG_TRUST_POLICY.md`
3. `10_rag/RAG_RETRIEVAL_INDEX.md`
4. La method card piu vicina in `10_rag/RAG_METHOD_CARDS/`
5. Eventuali esempi svolti collegati in `07_solved_examples/`
6. Il formato risposta in `10_rag/RAG_EXAM_ANSWER_STYLE.md`

## Uso rapido

- Se la traccia contiene LCS, colori, ingombro o somma, cerca prima le card DP su sequenze.
- Se la traccia contiene cammini, colori degli archi o vincoli di stato, cerca prima le card DP su grafi.
- Se chiede una simulazione, usa le card step-by-step.
- Se chiede teoria, NP-completezza, matroidi o ricorrenze, usa la card specifica.

## Regola d'esame

La risposta deve essere breve, copiabile e basata sui file recuperati. Se manca un metodo specifico, usare il template piu vicino e trattare la risposta come ricostruzione prudente da pattern.
