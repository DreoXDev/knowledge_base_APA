# TODO RAG

## Bloccanti per uso da esame

- [ ] Eseguire un test reale da telefono copiando `RAG Interface/Prompt Chat Esame.md` in una chat nuova.
- [ ] Se la chat fallisce sul recupero, accorciare ulteriormente il prompt unico e tenere solo le sezioni Parte I 03 luglio 2025.

## Non bloccanti ma utili

- [ ] Aggiungere smoke test per Kruskal, NP-completezza, matroidi e Dijkstra.
- [ ] Integrare nel prompt unico solo i moduli specifici gia testati.
- [ ] Verificare manualmente warning manoscritti quando riguardano esercizi probabili.
- [ ] Completare esempi by-exam Parte I piu ricorrenti, senza bloccare l'uso RAG.
- [ ] Ridurre i doppioni tra metodi `dp_*` e `metodo_*` dopo un ciclo di uso reale della RAG.

## Materiale da non usare come fonte primaria durante l'esame

- `04_methods/dynamic_programming.md`: file generale `draft`; usare prima le card DP in `10_rag/RAG_METHOD_CARDS/`.
- `04_methods/graph_algorithms.md`: file generale `draft`; usare prima le card grafi in `10_rag/RAG_METHOD_CARDS/`.
- `04_methods/recurrence_relations.md`: `draft`; usare `10_rag/RAG_METHOD_CARDS/ricorrenze.md` e verificare se serve.
- `04_methods/complexity_analysis.md`, `04_methods/correctness_proofs.md`, `04_methods/divide_et_impera.md`: scaffold generali, non sorgenti primarie RAG.
- `07_solved_examples/by_topic/hateville_senza_due_rossi_consecutivi_SRC_EXTRA_001.md`: contiene warning, usare solo con prudenza.
- `07_solved_examples/by_topic/lcs_alternanza_pari_dispari_SRC_EXTRA_001.md`: `draft` con warning, non usare come esempio verificato.
