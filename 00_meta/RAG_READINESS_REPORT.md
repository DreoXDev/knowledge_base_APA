# RAG Readiness Report

## Stato sintetico

La repository e pronta per un uso RAG controllato tramite `10_rag/`.

Il punto di ingresso primario e `10_rag/RAG_ENTRYPOINT.md`; il recupero deve passare da `10_rag/RAG_RETRIEVAL_INDEX.md` e poi dalle card in `10_rag/RAG_METHOD_CARDS/`.

## Pronto per l'esame

- LCS con vincoli di colore/conteggio: card completa, metodi sorgente e esempi collegati.
- LCS con ingombro/somma/budget: card completa, metodi sorgente e esempi collegati.
- Zaino 0/1 con varianti colore: card completa, metodi ed esempi collegati.
- Kruskal/MST: card step-by-step collegata a metodo e appello catalogato.
- NP-completezza e riduzioni: card completa con schema e riduzioni classiche.
- Matroidi: card completa con ereditarieta, scambio e collegamento greedy.

## Utilizzabile con prudenza

- DP su grafi con stato esteso: card presente, ma alcune fonti derivano da appunti manoscritti con warning.
- Dijkstra step-by-step: metodo presente; esempi numerici specifici sono meno strutturati rispetto a Kruskal.
- Ricorrenze: card presente, ma `04_methods/recurrence_relations.md` resta `draft`; per Warshall usare `04_methods/metodo_equazioni_ricorrenza_chiusura_transitiva.md`.

## Non usare come fonte primaria RAG

- `04_methods/dynamic_programming.md`
- `04_methods/graph_algorithms.md`
- `04_methods/recurrence_relations.md`
- `04_methods/complexity_analysis.md`
- `04_methods/correctness_proofs.md`
- `07_solved_examples/by_topic/hateville_senza_due_rossi_consecutivi_SRC_EXTRA_001.md`
- `07_solved_examples/by_topic/lcs_alternanza_pari_dispari_SRC_EXTRA_001.md`

Questi file sono draft, scaffold o contengono warning. Vanno usati solo dopo le card RAG e solo se servono dettagli secondari.

## Pattern piu affidabili

| Pattern | Affidabilita | Uso consigliato |
|---|---|---|
| LCS colori/conteggi | A | Usare direttamente card e esempi collegati |
| LCS ingombro/budget | A | Usare direttamente card e esempi collegati |
| Zaino 0/1 colori | A | Usare direttamente card e esempi collegati |
| Kruskal/MST | A | Usare card step-by-step |
| NP-completezza | A | Usare card e template NP |
| Matroidi | A | Usare card e template matroide |
| DP grafi stato esteso | B/C | Usare card, controllare warning |
| Dijkstra | B | Usare card, adattare alla traccia numerica |
| Ricorrenze | C | Usare con prudenza |

## Scansioni finali

- `final_todo_scan.txt`: rigenerato con occorrenze di TODO, draft, scaffold, placeholder, warning e completamenti.
- `final_warning_scan.txt`: rigenerato con warning e punti ambigui.

## Fix finali applicati

- Markdown RAG controllato e mantenuto in formato leggibile per Obsidian.
- Card `dp_lcs_ingombro.md` allineata alla formulazione primaria `<= k`.
- Prompt unico migrato in `AI Chat during Exam/Final Prompt.md`.
- Modulo `AI Chat during Exam/prompt_rag_apa_parteI_esercizio1_lcs_ingombro.md` normalizzato.
- Smoke test Parte I 03 luglio 2025 eseguito e salvato in `00_meta/RAG_SMOKE_TEST_2025_07_03_PARTE_I.md`.
- Cartella finale `AI Chat during Exam/` creata con `Final Prompt.md`, README e sezioni modulari.
- Smoke test del prompt finale salvato in `AI Chat during Exam/SMOKE_TEST_FINAL_PROMPT.md`.

## Validazione

Comando eseguito:

`python scripts/check_wikilinks.py`

Risultato:

- Markdown controllati: 270.
- Wikilink rotti: 0.
- Note importanti orfane: 0.
- Duplicati nome nota: 2.

Duplicati rilevati:

- `README`: `README.md`, `AI Chat during Exam/README.md`.
- `matroidi`: `05_theory/matroidi.md`, `10_rag/RAG_METHOD_CARDS/matroidi.md`.

Il duplicato `matroidi` e accettato perche il piano RAG richiede esplicitamente la card `10_rag/RAG_METHOD_CARDS/matroidi.md`. In caso di uso Obsidian con wikilink non qualificati, preferire link espliciti con path.

## Prossime azioni

1. Usare `AI Chat during Exam/Final Prompt.md` come prompt unico iniziale da telefono.
2. Estendere il prompt unico solo con moduli gia verificati.
3. Verificare manualmente i warning manoscritti quando emergono in esercizi probabili.
4. Aggiungere smoke test futuri per Kruskal, NP-completezza e matroidi.
