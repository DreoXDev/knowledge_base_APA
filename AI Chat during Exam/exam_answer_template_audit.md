# Audit template risposte d'esame APA

Questo file mappa i pattern minimi richiesti dal prompt finale. Serve come audit operativo, non come risposta da mostrare durante l'esame.

| Tipo esercizio | Trigger nella traccia | File RAG/metodo | Forma risposta richiesta | Errori comuni |
| --- | --- | --- | --- | --- |
| DP LCS base | LCS, sottosequenza comune piu lunga, prefissi | `10_rag/RAG_METHOD_CARDS/dp_lcs_base.md` | Stato `C[i,j]`, base, match/non-match, `C[m,n]` | Confondere sottosequenza e sottostringa; saltare base |
| DP LCS con colori/vincoli | colori, al massimo, esattamente, almeno, rossi/blu | `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md` | Stato con soli vincoli richiesti, base, update colore, finale coerente | Aggiungere colori non richiesti; confondere almeno/al massimo/esattamente |
| DP LCS tre sequenze | tre sequenze, `LCS(X,Y,Z)` | `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md` | Stato `C[i,j,k]`, base con prefisso vuoto, match triplo, max su tre scarti | Fare due LCS successive |
| DP LICS | LICS, sottosequenza comune crescente | `10_rag/RAG_METHOD_CARDS/dp_lics_varianti.md` | Stato vincolato a terminare nel match, predecessori minori, max globale | Usare ricorrenza LCS standard; finale `C[m,n]` |
| DP Knapsack | zaino, knapsack, peso, valore, capacita | `10_rag/RAG_METHOD_CARDS/dp_knapsack.md` | Stato `V[i,p]`, include/esclude, `V[n,P]` | Usare greedy sullo 0/1 |
| DP Knapsack con colore | al massimo k oggetti rossi, budget colore | `10_rag/RAG_METHOD_CARDS/dp_knapsack.md` | Stato `V[i,p,r]`, decremento budget solo se prendo oggetto vincolato | Confondere al massimo con esattamente |
| DP su grafi / Floyd-Warshall | per ogni coppia, FW, cammini minimi | `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md` | Stato `D_k[i,j,...]`, base `k=0`, non uso/uso k, finale `D_n` | Trattare `k` come lunghezza |
| Cammini con vincoli colori/parita/conteggi | archi/vertici colorati, pari, esattamente, presenza | `10_rag/RAG_METHOD_CARDS/dp_grafi_stato_esteso.md` | Stato extra minimo, combinazione stati, `min/+` o `OR/AND` | Confondere colori su archi e vertici |
| Greedy generico | greedy, scelta locale, correttezza | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md` | Algoritmo, criterio, scambio/scelta sicura, complessita | Dire solo "scelgo il migliore" |
| Matroidi / Rado-Edmonds | matroide, ereditaria, scambio, indipendenza | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md` | Definire `(E,F)`, ereditaria, scambio, Rado-Edmonds | Saltare proprieta di scambio |
| MST teorico | MST, arco sicuro, taglio, arco leggero | `10_rag/RAG_METHOD_CARDS/mst_prim.md` | Definizione MST, taglio/arco sicuro, conclusione | Confondere MST con shortest path |
| Kruskal numerico | Kruskal, archi ordinati, ciclo | `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md` | Ordine archi, scelto/scartato, MST, peso | Aggiungere archi che creano ciclo |
| Prim numerico | Prim, key, predecessore | `10_rag/RAG_METHOD_CARDS/mst_prim.md` | Inizializzazione key/pi, estrazioni, aggiornamenti, MST | Usare distanze da sorgente come Dijkstra |
| Dijkstra numerico | Dijkstra, sorgente, distanze, pesi non negativi | `10_rag/RAG_METHOD_CARDS/dijkstra_step_by_step.md` | Inizializzazione, estrazioni minime, rilassamenti, distanze/predecessori | Estrarre nodo non minimo globale |
| Riduzioni NP-complete | NP-completo, NP-hard, certificato, riduzione | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md` | NP, riduzione da noto, costruzione, doppia implicazione, conclusione | Invertire riduzione; saltare NP |
| 3SAT -> Clique | clausole, letterali, clique | `07_solved_examples/riduzione_3sat_clique_schema.md` | Vertici per letterali, archi tra clausole diverse non contraddittorie, `k=#clausole` | Collegare letterali della stessa clausola |
| Clique -> Vertex Cover | complemento, clique, vertex cover | `04_methods/metodo_riduzione_clique_vertex_cover.md` | Complemento, parametro `n-k`, doppia implicazione | Dimenticare complemento o parametro `n-k` |
| Independent Set / VC / Clique | insieme indipendente, copertura, cricca | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md` | Relazione via complemento/cardinalita, versi espliciti | Confondere clique con independent set |
| Domande P/NP/NP-hard/NP-completo | definire classi, certificato, verificatore | `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md` | Definizioni brevi, certificato se richiesto | Dire che NP significa non polinomiale |
| Completamento grafico | disegna, completa, indica insieme/archi | `06_exam_patterns/parte_ii_grafi_np_patterns.md` | Elenco vertici/archi da includere/escludere, cardinalita/finale | Scrivere spiegazione lunga invece del risultato |
| Domande teoriche brevi | definizione, teorema, proprieta | `10_rag/RAG_EXAM_ANSWER_STYLE.md` | Definizione, proprieta, idea breve, conclusione | Risposta troppo lunga o esempi non richiesti |

## Controllo specifico LCS con presenza del rosso

Se la traccia dice "nella quale tra i colori associati ai simboli vi e la presenza del rosso", il vincolo e:

```text
almeno un simbolo rosso
```

Lo stato corretto deve rappresentare solo quel requisito, ad esempio:

```text
C[i,j,r], r in {0,1}
```

Non usare:

```text
C[i,j,r,b]
```

a meno che la traccia chieda esplicitamente presenza sia del rosso sia del blu.
