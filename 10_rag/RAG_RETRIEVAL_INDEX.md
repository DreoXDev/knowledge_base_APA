# RAG Retrieval Index - APA

## Come usare questo file

Usa questa tabella per associare una query o un pattern d'esame ai file piu rilevanti. Ogni entry punta a pochi file principali per ridurre rumore nel retrieval.

## Entrypoint stile risposta

- `10_rag/RAG_ANSWER_WRITING_TEMPLATES.md`: usare quando serve sapere come formattare la risposta da esame.
- Il file dei template di scrittura e una fonte di stile, non di ground truth matematica.

## Index

| Query / Pattern | Keyword utili | File principali |
| --- | --- | --- |
| Stile risposta da esame | istanza, soluzione, sottoproblema, caso base, passo ricorsivo, completamento testuale | `10_rag/RAG_ANSWER_WRITING_TEMPLATES.md`, `10_rag/RAG_EXAM_ANSWER_STYLE.md`, `09_ingestion_reports/compagna_answer_writing_style_ingestion.md` |
| LCS standard | LCS, sottosequenza comune, prefissi, `c_{i,j}`, Print-LCS | `10_rag/RAG_METHOD_CARDS/dp_lcs_base.md`, `04_methods/dp_lcs_base.md`, `07_solved_examples/dp/lcs_base_6ott25.md` |
| LCS con vincoli colore | al massimo k rossi, esattamente k rossi, colori, `c_{i,j,r}` | `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`, `04_methods/dp_lcs_vincoli_colore.md`, `07_solved_examples/dp/lcs_al_massimo_3_rossi_SRC_LECTURE_001.md` |
| LCS con presenza del rosso e colori R/B/N | presenza del rosso, almeno un rosso, `{R,B,N}`, rosso blu nero, indicatore | `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`, `04_methods/dp_lcs_vincoli_colore.md`, `07_solved_examples/dp/lcs_presenza_rosso_RBN.md` |
| LCS con due rossi consecutivi | due rossi consecutivi, almeno due rossi, stato booleano, massimo globale | `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`, `04_methods/dp_lcs_due_rossi_consecutivi.md`, `07_solved_examples/dp/lcs_due_rossi_consecutivi_schema.md` |
| LCS dispari/pari | LCSdp, posizioni dispari, posizioni pari, parita valore, parita lunghezza | `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`, `04_methods/dp_lcs_dispari_pari_alternati.md`, `07_solved_examples/dp/lcs_dispari_pari_alternati_schema.md` |
| LCS tre sequenze | tre sequenze, LCS(X,Y,W), DP tridimensionale, `c_{i,j,h}` | `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`, `04_methods/dp_lcs_tre_sequenze.md`, `07_solved_examples/dp/lcs_tre_sequenze_schema.md` |
| LICS e varianti | Longest Common Increasing Subsequence, crescente, stato vincolato a terminare | `10_rag/RAG_METHOD_CARDS/dp_lics_varianti.md`, `04_methods/dp_lics_e_varianti.md`, `07_solved_examples/lics_schema.md` |
| LCS con somma/ingombro | budget, peso, somma, ingombro, capacita residua | `10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md`, `04_methods/dp_lcs_vincolo_somma_ingombro.md`, `07_solved_examples/dp/lcs_somma_leq_k_SRC_NOTE_001.md` |
| LCS con ingombro complessivo <= W / peso totale | ingombro complessivo, peso totale, costo totale, somma dei pesi, budget W, `<= W` | `10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md`, `04_methods/dp_lcs_vincolo_somma_ingombro.md`, `07_solved_examples/DP_LCS_ingombro_complessivo_W.md` |
| Floyd-Warshall base | FW base, cammini minimi ogni coppia, matrice D, bottom-up | `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`, `04_methods/fw_base_bottom_up.md`, `05_theory/floyd_warshall.md` |
| Floyd-Warshall con alternanza archi | archi alternati, primo colore, ultimo colore, esistenza archi alternati | `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`, `04_methods/fw_varianti_vincoli_colori.md`, `07_solved_examples/fw_varianti_vincoli_colori_schema.md` |
| Floyd-Warshall con alternanza vertici | vertici alternati, colori dei vertici, cammini minimi o esistenza | `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`, `04_methods/fw_varianti_vincoli_colori.md`, `05_theory/programmazione_dinamica_floyd_warshall_varianti.md` |
| Floyd-Warshall con conteggi/parita/presenza | esattamente 3 archi rossi, pari archi rossi, flag presenza, conteggi colori | `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`, `04_methods/fw_varianti_vincoli_colori.md`, `07_solved_examples/fw_varianti_vincoli_colori_schema.md` |
| Floyd-Warshall esistenza | esiste cammino, booleano, OR/AND, archi rossi e blu presenti | `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`, `04_methods/fw_varianti_vincoli_colori.md`, `10_rag/RAG_METHOD_CARDS/dp_grafi_stato_esteso.md` |
| Knapsack 0/1 base | zaino, knapsack, peso, valore, capacita, `V[i,p]` | `10_rag/RAG_METHOD_CARDS/dp_knapsack.md`, `04_methods/dp_knapsack_base.md`, `07_solved_examples/knapsack_base_schema.md` |
| Knapsack con al massimo 3 rossi | oggetti rossi, al massimo 3, budget colore, `V[i,c,r]` | `10_rag/RAG_METHOD_CARDS/dp_knapsack.md`, `04_methods/dp_knapsack_vincoli_colore.md`, `07_solved_examples/knapsack_al_massimo_3_rossi_schema.md` |
| Greedy teoria | greedy, scelta locale, correttezza, scambio | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`, `05_theory/greedy_teoria_base.md`, `04_methods/greedy_algorithms.md` |
| Matroidi | matroide, ereditarieta, scambio, Rado-Edmonds, indipendenza | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`, `05_theory/matroidi_e_greedy.md`, `04_methods/metodo_greedy_matroidi_rado.md` |
| MST e arco sicuro | MST, taglio, arco leggero, arco sicuro, albero ricoprente minimo | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`, `04_methods/mst_greedy_base.md`, `05_theory/teorema_arco_sicuro_mst.md` |
| Prim | Prim, key, predecessore, coda di priorita, componente corrente | `10_rag/RAG_METHOD_CARDS/mst_prim.md`, `04_methods/mst_prim.md`, `07_solved_examples/prim_schema_esecuzione.md` |
| Kruskal | Kruskal, archi ordinati, union-find, componenti, ciclo | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`, `04_methods/metodo_kruskal_mst.md`, `07_solved_examples/kruskal_schema_esecuzione.md` |
| Matroide grafico | foreste, indipendenza grafica, Kruskal come greedy su matroide | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`, `05_theory/kruskal_matroide_grafico.md`, `04_methods/metodo_dimostrazione_matroide_grafico.md` |
| P e NP | classe P, classe NP, certificato, verificatore polinomiale | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`, `05_theory/p_np_np_completezza.md`, `04_methods/np_completezza_schema_dimostrazione.md` |
| NP-completezza | NP-hard, NP-completo, appartenenza a NP, riduzione polinomiale | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`, `04_methods/np_completezza_schema_dimostrazione.md`, `07_solved_examples/np_completezza_schema.md` |
| Riduzioni polinomiali | `A <=p B`, direzione riduzione, problema noto verso target | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`, `05_theory/riduzioni_np_completezza.md`, `04_methods/metodo_dimostrare_np_completezza.md` |
| SAT / 3SAT | SAT, 3SAT, clausole, letterali, riduzione da 3SAT | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`, `04_methods/metodo_riduzione_3sat_clique.md`, `07_solved_examples/riduzione_3sat_clique_schema.md` |
| Clique | clique, cricca, grafo complemento, riduzione | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`, `05_theory/clique_vertex_cover_independent_set.md`, `04_methods/metodo_riduzione_3sat_clique.md` |
| Vertex Cover | copertura di vertici, complemento, Clique <=p Vertex Cover | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`, `05_theory/vertex_cover.md`, `04_methods/metodo_riduzione_clique_vertex_cover.md` |
| Independent Set | insieme indipendente, complemento, relazione con Clique e Vertex Cover | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`, `05_theory/clique_vertex_cover_independent_set.md`, `04_methods/metodo_riduzione_3sat_independent_set.md` |

## Warning

- Le entry sono entrypoint, non sostituiscono method card e metodi completi.
- I file generali `04_methods/dynamic_programming.md`, `04_methods/graph_algorithms.md` e `04_methods/recurrence_relations.md` sono utili come supporto, ma non sono fonti primarie RAG quando esiste una card specifica.
