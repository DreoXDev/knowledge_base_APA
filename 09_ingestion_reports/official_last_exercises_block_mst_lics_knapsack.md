# Ingestion report - ultimo blocco esercizi ufficiali

## Fonti

| Source ID | PDF | Tema | Stato |
|---|---|---|---|
| SRC-OFFICIAL-EX-012 | `01_sources/extra_materials/knapsack-atmost-3-red.pdf` | Zaino con al massimo 3 oggetti rossi | applicato |
| SRC-OFFICIAL-EX-017 | `01_sources/extra_materials/mst-prim.pdf` | Prim per MST | applicato |
| SRC-OFFICIAL-EX-018 | `01_sources/extra_materials/mst.pdf` | Minimum Spanning Tree e arco sicuro | applicato |
| SRC-OFFICIAL-EX-019 | `01_sources/extra_materials/varianti-lics-20ott25.pdf` | LICS e varianti | applicato |

## Decisioni

- MST e Prim sono stati integrati come famiglia greedy unica, collegando anche Kruskal e il teorema dell'arco sicuro gia presenti.
- LICS e varianti sono state separate dalla LCS standard: lo stato ufficiale e vincolato a terminare nel match corrente e il valore finale e un massimo globale.
- Knapsack con al massimo 3 rossi e stato reso fonte primaria per la semantica "al massimo r", distinta da "esattamente r".

## File principali creati

- `04_methods/mst_greedy_base.md`
- `04_methods/mst_prim.md`
- `05_theory/teorema_arco_sicuro_mst.md`
- `07_solved_examples/prim_schema_esecuzione.md`
- `10_rag/RAG_METHOD_CARDS/mst_prim.md`
- `04_methods/dp_lics_e_varianti.md`
- `07_solved_examples/lics_schema.md`
- `10_rag/RAG_METHOD_CARDS/dp_lics_varianti.md`
- `04_methods/dp_knapsack_vincoli_colore.md`
- `07_solved_examples/knapsack_al_massimo_3_rossi_schema.md`
- `10_rag/RAG_METHOD_CARDS/dp_knapsack_vincoli_colore.md`

## Note

I vecchi file da `SRC-NOTE-001` e `SRC-EXTRA-001` restano collegati come supporto, ma per uso RAG durante l'esame le card ufficiali hanno precedenza.
