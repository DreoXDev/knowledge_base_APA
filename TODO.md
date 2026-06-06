# TODO RAG

## Problemi bloccanti per RAG

- [ ] Verificare manualmente i warning delle fonti manoscritte `SRC-NOTE-001` e `SRC-EXTRA-001` prima di usarli come fonte primaria.
- [ ] Completare o confermare gli esempi by-exam Parte I ancora catalogati ma non trasformati in soluzione completa.
- [ ] Rieseguire `python scripts/check_wikilinks.py` dopo ogni modifica strutturale del layer `10_rag/`.

## Miglioramenti utili ma non essenziali

- [ ] Convertire gradualmente gli esempi Parte I piu ricorrenti in soluzioni complete in `07_solved_examples/by_exam/`.
- [ ] Ridurre i doppioni tra metodi `dp_*` e `metodo_*` solo dopo un ciclo di uso reale della RAG.
- [ ] Aggiungere esempi numerici solo quando derivano chiaramente da appelli, note o materiali gia ingestiti.
- [ ] Integrare le card RAG con ulteriori query probabili osservate durante simulazioni d'esame.

## Materiale da non usare come fonte primaria durante l'esame

- `04_methods/dynamic_programming.md`: file generale `draft`; usare prima le card DP in `10_rag/RAG_METHOD_CARDS/`.
- `04_methods/graph_algorithms.md`: file generale `draft`; usare prima le card grafi in `10_rag/RAG_METHOD_CARDS/`.
- `04_methods/recurrence_relations.md`: `draft`; usare `10_rag/RAG_METHOD_CARDS/ricorrenze.md` e verificare se serve.
- `04_methods/complexity_analysis.md`, `04_methods/correctness_proofs.md`, `04_methods/divide_et_impera.md`: scaffold generali, non sorgenti primarie RAG.
- `07_solved_examples/by_topic/hateville_senza_due_rossi_consecutivi_SRC_EXTRA_001.md`: contiene warning, usare solo con prudenza.
- `07_solved_examples/by_topic/lcs_alternanza_pari_dispari_SRC_EXTRA_001.md`: `draft` con warning, non usare come esempio verificato.
