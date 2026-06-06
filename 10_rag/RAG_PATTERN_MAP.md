# RAG Pattern Map

| Famiglia | Pattern osservato | Card primaria | Affidabilita |
|---|---|---|---|
| DP sequenze | LCS base su due sequenze; matrice C; ricostruzione Print_LCS | `RAG_METHOD_CARDS/dp_lcs_base.md` | A+ |
| DP sequenze | LCS con vincoli di colore o conteggio; A+ per al massimo 3 rossi da PDF ufficiale | `RAG_METHOD_CARDS/dp_lcs_colori.md` | A+ |
| DP sequenze | LCS varianti ufficiali: tre sequenze, due rossi consecutivi, dispari/pari per posizione | `RAG_METHOD_CARDS/dp_lcs_varianti.md` | A+ |
| DP sequenze | LICS e varianti con stato vincolato a terminare | `RAG_METHOD_CARDS/dp_lics_varianti.md` | A+ |
| DP sequenze | LCS con ingombro/somma/budget | `RAG_METHOD_CARDS/dp_lcs_ingombro.md` | A |
| DP grafi | Floyd-Warshall o cammini con stato esteso | `RAG_METHOD_CARDS/dp_grafi_stato_esteso.md` | B |
| DP grafi | Floyd-Warshall base e varianti ufficiali con colori/conteggi/esistenza | `RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md` | A+ |
| DP zaino | Zaino 0/1 base e varianti (colori/vincoli) | `RAG_METHOD_CARDS/dp_knapsack.md` | A+ |
| Grafi | Simulazione Dijkstra | `RAG_METHOD_CARDS/dijkstra_step_by_step.md` | B |
| Grafi greedy | MST, Prim, Kruskal, Matroide Grafico | `RAG_METHOD_CARDS/greedy_matroidi_mst.md` | A+ |
| NP-completezza | Schema generale e riduzioni classiche | `RAG_METHOD_CARDS/np_completezza_riduzioni.md` | A |
| Matroidi | Matroidi, ereditarietà, scambio, Rado | `RAG_METHOD_CARDS/greedy_matroidi_mst.md` | A |
| Ricorrenze | Master, iterazione, chiusura transitiva | `RAG_METHOD_CARDS/ricorrenze.md` | C |

## Note RAG

- I pattern `A` sono recuperabili direttamente durante l'esame.
- I pattern `B` sono utilizzabili, ma vanno adattati alla traccia.
- I pattern `C` richiedono prudenza o verifica, soprattutto se la fonte primaria e `draft`.

## Pattern: LCS base su due sequenze

Segnali nella traccia:

- due sequenze `X` e `Y`;
- richiesta di sottosequenza comune piu lunga;
- richiesta di calcolare valore ottimo o ricostruire una soluzione;
- matrice `C` da riempire o usare per backtracking.

Metodo da recuperare:

- `RAG_METHOD_CARDS/dp_lcs_base.md`

Varianti vicine:

- LCS con vincoli colore;
- LCS con tre sequenze;
- LCS crescente / LICS;
- LCS con lunghezza esatta o vincoli booleani.

## Pattern: LCS di 3 sequenze

Segnali nella traccia:

- "LCS di 3 sequenze";
- "tre sequenze";
- `LCS(X,Y,W)`;
- "sottosequenza comune di `X`, `Y` e `W`".

Metodo da recuperare:

- `RAG_METHOD_CARDS/dp_lcs_varianti.md`
- `04_methods/dp_lcs_tre_sequenze.md`

Schema:

- usare DP tridimensionale;
- sottoproblema `LCS(X_i,Y_j,W_h)`;
- coefficiente `c_{i,j,h}`;
- casi base quando almeno un indice e zero;
- match solo se `x_i = y_j = w_h`;
- mismatch con massimo tra le tre possibilita di scartare un ultimo elemento.

Errori da evitare:

- non usare una tabella bidimensionale;
- non fare prima `LCS(X,Y)` e poi `LCS(risultato,W)`;
- non usare massimo globale: il valore ottimo e `c_{m,n,l}`;
- non confondere `h` con un parametro di vincolo.

## Pattern: LCS con almeno due elementi rossi consecutivi

Segnali nella traccia:

- "due rossi consecutivi";
- "almeno due elementi rossi consecutivi";
- `LCS2red`;
- presenza di `c_ij1`, `c_ij0` o stati vincolati a terminare.

Metodo da recuperare:

- `RAG_METHOD_CARDS/dp_lcs_varianti.md`
- `04_methods/dp_lcs_due_rossi_consecutivi.md`

Schema:

- usare stati ausiliari vincolati a terminare nel match corrente;
- `c_ij1`: coppia di rossi consecutivi gia presente;
- `c_ij0`: coppia non ancora presente;
- se `x_i != y_j`, stato inesistente con `-infinito`;
- valore ottimo come massimo globale dei `c_ij1`.

Errori da evitare:

- non usare direttamente `c_{m,n}`;
- non confondere il vincolo con "almeno due rossi totali";
- non richiedere che i due rossi siano consecutivi nelle sequenze originali.

## Pattern: LCS con dispari in posizioni dispari e pari in posizioni pari

Segnali nella traccia:

- `LCSdp`;
- "dispari in posizioni dispari";
- "pari in posizioni pari";
- "odd/even";
- vincolo sulla posizione nella sottosequenza.

Metodo da recuperare:

- `RAG_METHOD_CARDS/dp_lcs_varianti.md`
- `04_methods/dp_lcs_dispari_pari_alternati.md`

Schema:

- usare sottoproblema vincolato a terminare nel match corrente;
- controllare la parita del valore `x_i`;
- controllare la parita della lunghezza precedente `c_hk`;
- valore finale come massimo globale dei `c_ij`.

Errori da evitare:

- non confondere parita del valore con parita dell'indice;
- non usare `c_{m,n}`;
- non trattare il vincolo come alternanza tra indici delle sequenze originali;
- non iniziare la sottosequenza con un elemento pari.

## Pattern: LICS / sottosequenze comuni vincolate

Segnali nella traccia:

- "LICS";
- "Longest Common Increasing Subsequence";
- "sottosequenza comune crescente";
- "simile a LICS";
- "vincolata a terminare con `x_i`".

Metodo da recuperare:

- `RAG_METHOD_CARDS/dp_lics_varianti.md`
- `04_methods/dp_lics_e_varianti.md`

Schema:

- stato `c_ij` vincolato a terminare con `x_i = y_j`;
- se `x_i != y_j`, `c_ij = 0`;
- se `x_i = y_j`, massimo sui predecessori validi;
- per LICS il predecessore deve avere valore minore;
- valore finale come massimo globale.

Errori da evitare:

- non usare la ricorrenza LCS standard;
- non usare `c_{m,n}`;
- non confondere parita dei valori con parita degli indici nelle varianti.

## Pattern: MST / Prim

Segnali nella traccia:

- "Minimum Spanning Tree";
- "MST";
- "arco sicuro";
- "taglio";
- "Prim";
- "arco leggero";
- `key`, `pi`, `Q`.

Metodo da recuperare:

- `RAG_METHOD_CARDS/mst_prim.md`
- `04_methods/mst_greedy_base.md`
- `04_methods/mst_prim.md`
- `05_theory/teorema_arco_sicuro_mst.md`

Schema:

- usare proprieta del taglio e arco sicuro;
- per Prim mantenere componente, chiavi e predecessori;
- output come insieme di archi `(pi[v],v)`.

Errori da evitare:

- non confondere Prim con Dijkstra;
- `key[v]` non e distanza da sorgente;
- MST richiede grafo non orientato e connesso.

## Pattern: Knapsack e varianti (Zaino 0/1)

Segnali nella traccia:
- "zaino", "knapsack", "capacità", "peso", "valore", "oggetti";
- "al massimo 3 oggetti rossi", "vincolo colore oggetti";
- `V[i,p]`, `d_{i,c,r}`, `S_{i,c,r}`.

Metodo da recuperare:
- `RAG_METHOD_CARDS/dp_knapsack.md`
- `04_methods/metodo_programmazione_dinamica_zaino_01.md`
- `04_methods/dp_knapsack_vincoli_colore.md`

Schema:
- per lo zaino base usare lo stato $V[i,p]$ (include/esclude oggetto $i$);
- per varianti con colore (es. al massimo 3 rossi) aggiungere la dimensione $r$ come budget di oggetti speciali: $V[i,c,r]$;
- se si sceglie un oggetto speciale, decrementare $r$.

Errori da evitare:
- non usare greedy per lo zaino 0/1 (usare sempre DP);
- non trattare "al massimo" come "esattamente" (il primo non richiede inizializzazione con $-\infty$ per celle non utilizzate).

## Pattern: Floyd-Warshall con stato extra

Segnali nella traccia:

- "per ogni coppia di vertici";
- "Floyd-Warshall";
- "cammino minimo" oppure "verificare se esiste";
- "si alternano";
- "esattamente";
- "numero pari";
- "sono presenti".

Metodo da recuperare:

- `RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`
- `04_methods/fw_varianti_vincoli_colori.md`

Schema:

- partire da `P_ij^k`;
- `k` indica i vertici intermedi ammessi;
- aggiungere dimensioni allo stato solo per cio che serve ricordare;
- usare `E1` per non usare `k`;
- usare `E2` per passare da `k`;
- combinare gli stati extra dei sottocammini;
- scegliere `min/+` oppure `OR/AND` in base al tipo di problema.

Decisioni:

- alternanza archi: servono `f,l`;
- alternanza vertici: non servono `f,l`;
- conteggio esatto: stato `r`;
- parita: stato `p`;
- presenza: flag booleani.

## Pattern: Greedy e Matroidi

Segnali nella traccia:
- "greedy", "matroide", "sistema di indipendenza", "proprietà di scambio", "ereditaria", "Rado-Edmonds".

Metodo da recuperare:
- `RAG_METHOD_CARDS/greedy_matroidi_mst.md`
- `05_theory/matroidi_e_greedy.md`
- `04_methods/metodo_greedy_matroidi_rado.md`

Schema:
- definire la coppia $\langle E, \mathcal{F} \rangle$;
- mostrare la proprietà ereditaria (sottoinsiemi di indipendenti sono indipendenti);
- mostrare la proprietà di scambio (se $|B| > |A|$, esiste $b \in B \setminus A$ tale che $A \cup \{b\} \in \mathcal{F}$);
- se entrambi valgono, è un matroide e l'approccio greedy è corretto (Teorema di Rado-Edmonds).

## Pattern: Kruskal (MST)

Segnali nella traccia:
- "Kruskal", "MST", "albero ricoprente minimo", "foresta", "archi ordinati", "union-find".

Metodo da recuperare:
- `RAG_METHOD_CARDS/greedy_matroidi_mst.md`
- `04_methods/metodo_kruskal_mst.md`
- `07_solved_examples/kruskal_schema_esecuzione.md`

Schema:
- ordinare gli archi in ordine crescente di peso;
- per ciascun arco, se gli estremi appartengono a componenti connesse diverse (Find-Set), aggiungere l'arco all'MST e fondere le componenti (Union);
- fermarsi quando si hanno $|V|-1$ archi.

## Pattern: Dimostrazione NP-completezza

Segnali nella traccia:
- "dimostrare che è NP-completo", "NP-hard", "riduzione polinomiale", "SAT/3SAT", "Clique", "Vertex Cover", "Independent Set".

Metodo da recuperare:
- `RAG_METHOD_CARDS/np_completezza_riduzioni.md`
- `04_methods/np_completezza_schema_dimostrazione.md`
- `07_solved_examples/np_completezza_schema.md`

Schema:
1. Dimostrare l'appartenenza a NP (definire certificato e verificatore polinomiale).
2. Scegliere un problema noto NP-completo (es. 3SAT, Clique, Vertex Cover).
3. Definire una riduzione polinomiale dal noto al target.
4. Dimostrare la correttezza in entrambi i versi ($\implies$ e $\impliedby$).
5. Concludere l'NP-completezza.
