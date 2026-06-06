# RAG Readiness Report

## Stato sintetico

La repository e pronta per un uso RAG controllato tramite `10_rag/`.

Il punto di ingresso primario e `10_rag/RAG_ENTRYPOINT.md`; il recupero deve passare da `10_rag/RAG_RETRIEVAL_INDEX.md` e poi dalle card in `10_rag/RAG_METHOD_CARDS/`.

## Pronto per l'esame

- LCS base: card completa, confermata da `SRC-OFFICIAL-EX-013`, con ricostruzione `Print_LCS` e nota sui pareggi.
- LCS con vincoli di colore/conteggio: card completa, confermata da `SRC-LECTURE-001` per "al massimo 3 rossi".
- LCS varianti ufficiali: card completa `dp_lcs_varianti.md`, confermata da `SRC-OFFICIAL-EX-014`, `SRC-OFFICIAL-EX-015`, `SRC-OFFICIAL-EX-016`.
- LICS e varianti: card completa `dp_lics_varianti.md`, confermata da `SRC-OFFICIAL-EX-019`.
- LCS con ingombro/somma/budget: card completa, metodi sorgente e esempi collegati.
- Floyd-Warshall base e varianti: card completa `fw_varianti_vincoli_colori.md`, confermata da `SRC-OFFICIAL-EX-003` ... `SRC-OFFICIAL-EX-011`.
- Zaino 0/1 con varianti colore: card ufficiale `dp_knapsack_vincoli_colore.md`, confermata da `SRC-OFFICIAL-EX-012`.
- MST/Prim/Kruskal: card ufficiale `mst_prim.md` collegata a MST base, Prim, arco sicuro e Kruskal.
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
| LCS base | A+ | Usare card `dp_lcs_base.md`; fonte ufficiale `SRC-OFFICIAL-EX-013` |
| LCS colori/conteggi | A+ | Usare direttamente card; variante "al massimo 3 rossi" confermata da PDF ufficiale |
| LCS varianti ufficiali | A+ | Usare `dp_lcs_varianti.md` per tre sequenze, due rossi consecutivi e dispari/pari per posizione |
| LICS e varianti | A+ | Usare `dp_lics_varianti.md`; stato vincolato a terminare e valore `max c_ij` |
| LCS ingombro/budget | A | Usare direttamente card e esempi collegati |
| Zaino 0/1 colori | A+ | Usare `dp_knapsack_vincoli_colore.md`; per al massimo 3 rossi risposta `d_{n,C,3}` |
| MST/Prim/Kruskal | A+ | Usare `mst_prim.md`; per Kruskal anche `kruskal_step_by_step.md` |
| NP-completezza | A | Usare card e template NP |
| Matroidi | A | Usare card e template matroide |
| Floyd-Warshall ufficiale | A+ | Usare `fw_varianti_vincoli_colori.md` per base, alternanza, conteggi, parita e presenza |
| DP grafi stato esteso | B/C | Usare card storica solo se la variante non e coperta dalla card ufficiale |
| Dijkstra | B | Usare card, adattare alla traccia numerica |
| Ricorrenze | C | Usare con prudenza |

## Scansioni finali

- `final_todo_scan.txt`: rigenerato con occorrenze di TODO, draft, scaffold, placeholder, warning e completamenti.
- `final_warning_scan.txt`: rigenerato con warning e punti ambigui.

## Fix finali applicati

- PDF ufficiale `SRC-OFFICIAL-EX-013` indicizzato e applicato alla LCS base.
- Card `10_rag/RAG_METHOD_CARDS/dp_lcs_base.md` creata.
- PDF ufficiali `SRC-OFFICIAL-EX-014`, `SRC-OFFICIAL-EX-015`, `SRC-OFFICIAL-EX-016` applicati in piano cumulativo LCS varianti.
- Card `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md` creata con metodi ufficiali per tre sequenze, due rossi consecutivi e dispari/pari.
- PDF ufficiali `SRC-OFFICIAL-EX-012`, `SRC-OFFICIAL-EX-017`, `SRC-OFFICIAL-EX-018`, `SRC-OFFICIAL-EX-019` applicati per ultimo blocco esercizi.
- Card `mst_prim.md`, `dp_lics_varianti.md`, `dp_knapsack_vincoli_colore.md` create.
- PDF ufficiali `SRC-OFFICIAL-EX-003` ... `SRC-OFFICIAL-EX-011` applicati con card unica Floyd-Warshall.
- Card `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md` creata.
- PDF ufficiale `SRC-LECTURE-001` indicizzato e applicato alla variante LCS con al massimo 3 rossi.
- RAG aggiornata per distinguere formulazione "al massimo r" da formulazione "esattamente r".
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

- Markdown controllati: 296.
- Wikilink rotti: 0.
- Note importanti orfane: 0.
- Duplicati nome nota: 6.

Duplicati rilevati:

- `README`: `README.md`, `AI Chat during Exam/README.md`.
- `dp_knapsack_vincoli_colore`: `04_methods/dp_knapsack_vincoli_colore.md`, `10_rag/RAG_METHOD_CARDS/dp_knapsack_vincoli_colore.md`.
- `dp_lcs_base`: `04_methods/dp_lcs_base.md`, `10_rag/RAG_METHOD_CARDS/dp_lcs_base.md`.
- `fw_varianti_vincoli_colori`: `04_methods/fw_varianti_vincoli_colori.md`, `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`.
- `matroidi`: `05_theory/matroidi.md`, `10_rag/RAG_METHOD_CARDS/matroidi.md`.
- `mst_prim`: `04_methods/mst_prim.md`, `10_rag/RAG_METHOD_CARDS/mst_prim.md`.

I duplicati `dp_lcs_base`, `dp_knapsack_vincoli_colore`, `fw_varianti_vincoli_colori`, `mst_prim` e `matroidi` sono accettati perche il layer RAG usa alcune card omonime ai metodi/teorie sorgente. In caso di uso Obsidian con wikilink non qualificati, preferire link espliciti con path.

## Prossime azioni

1. Usare `AI Chat during Exam/Final Prompt.md` come prompt unico iniziale da telefono.
2. Per LCS con "al massimo k rossi", usare `SRC-LECTURE-001` e la card `dp_lcs_colori.md`.
3. Per LCS base usare `SRC-OFFICIAL-EX-013` e la card `dp_lcs_base.md`.
4. Per LCS a tre sequenze, due rossi consecutivi e dispari/pari usare `dp_lcs_varianti.md`.
5. Per MST/Prim usare `mst_prim.md`; per LICS usare `dp_lics_varianti.md`; per zaino colori usare `dp_knapsack_vincoli_colore.md`.
6. Per Floyd-Warshall usare `fw_varianti_vincoli_colori.md`.
7. Proseguire la queue in `09_ingestion_reports/official_lectures_workplan.md`.
8. Aggiungere smoke test futuri per NP-completezza e matroidi.
