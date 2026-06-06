# Coverage Matrix

Affidabilita:

- `A`: metodo completo + esempio svolto + piu appelli.
- `B`: metodo completo + almeno un appello.
- `C`: metodo parziale o warning.
- `D`: solo teoria/scaffold, non usare come fonte primaria.

| Pattern | Appelli osservati | Metodo completo | Esempio svolto | Card RAG | Affidabilita |
|---|---|---|---|---|---|
| LCS con vincoli di colore/conteggio | Parte I 2025-01-13, 2025-09-17, 2025-11-10, extra | `04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md` | `07_solved_examples/dp/lcs_esattamente_k_rossi_SRC_NOTE_001.md`, `07_solved_examples/dp/lcs_al_massimo_k_rossi_SRC_NOTE_001.md` | `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md` | A |
| LCS con ingombro/somma/budget | Parte I, SRC-NOTE-001, SRC-EXTRA-001 | `04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md` | `07_solved_examples/dp/lcs_somma_leq_k_SRC_NOTE_001.md`, `07_solved_examples/by_topic/lcs_ingombro_SRC_EXTRA_001.md` | `10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md` | A |
| DP su grafi con stato esteso/colori | Parte I 2025-01-13, 2025-11-10, SRC-NOTE-001 | `04_methods/dp_grafi_floyd_warshall_stato_esteso.md` | `07_solved_examples/graphs/cammini_colori_floyd_warshall_SRC_NOTE_001.md` | `10_rag/RAG_METHOD_CARDS/dp_grafi_stato_esteso.md` | B |
| Zaino 0/1 con varianti di colore | 2026-01-12, SRC-NOTE-001, SRC-EXTRA-001 | `04_methods/metodo_programmazione_dinamica_zaino_01.md` | `07_solved_examples/dp/knapsack_colori_SRC_NOTE_001.md`, `07_solved_examples/by_topic/knapsack_max_R_rossi_SRC_EXTRA_001.md` | `10_rag/RAG_METHOD_CARDS/zaino_01_varianti.md` | A |
| Dijkstra step-by-step | Parte II e indici di esempi prioritari | `04_methods/metodo_dijkstra.md` | `07_solved_examples/priority_examples_index.md` | `10_rag/RAG_METHOD_CARDS/dijkstra_step_by_step.md` | B |
| Kruskal/MST step-by-step | 2025-11-10 Parte II, pattern MST | `04_methods/metodo_kruskal_mst.md` | `03_exercise_catalog/exercises/exam_2025_11_10_p2_e01.md` | `10_rag/RAG_METHOD_CARDS/kruskal_step_by_step.md` | A |
| NP-completezza e riduzioni | 2025-09-17, 2025-11-10, Parte II ricorrente | `04_methods/np_completezza_schema_dimostrazione.md`, `04_methods/metodo_dimostrare_np_completezza.md` | `07_solved_examples/theory/np_completezza_schema_SRC_NOTE_001.md`, `03_exercise_catalog/exercises/exam_2025_11_10_p2_e02.md` | `10_rag/RAG_METHOD_CARDS/riduzioni_np_completezza.md` | A |
| Matroidi e greedy | 2025-09-17, 2025-11-10, 2026-01-12 bonus | `04_methods/metodo_dimostrazione_matroide_grafico.md`, `04_methods/metodo_dimostrare_matroide_foreste.md` | `03_exercise_catalog/exercises/exam_2025_09_17_p2_e05.md`, `03_exercise_catalog/exercises/exam_2025_11_10_p2_e05.md` | `10_rag/RAG_METHOD_CARDS/matroidi.md` | A |
| Ricorrenze / Warshall / Master | 2025-11-10 Parte II, teoria | `04_methods/metodo_equazioni_ricorrenza_chiusura_transitiva.md` | `03_exercise_catalog/exercises/exam_2025_11_10_p2_e03.md` | `10_rag/RAG_METHOD_CARDS/ricorrenze.md` | C |

## Lettura rapida

Durante l'esame usare prioritariamente pattern `A` e `B`. I pattern `C` sono utilizzabili solo con template prudente e controllo dei warning.
