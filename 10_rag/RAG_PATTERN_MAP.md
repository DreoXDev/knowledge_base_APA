# RAG Pattern Map - APA

## Uso

Questo file serve a riconoscere rapidamente il tipo di esercizio e scegliere la method card corretta. Ogni path nella sezione `File` e stato verificato rispetto ai file presenti nella repo.

## Answer template

Per la forma della risposta da scrivere sul foglio, usare sempre `10_rag/RAG_ANSWER_WRITING_TEMPLATES.md` insieme alla method card del pattern. Il template di scrittura decide ordine, intestazioni e livello di dettaglio; la method card decide formule e correttezza.

Mappa rapida:

| Macro-pattern | Template di scrittura |
| --- | --- |
| LCS standard | `RAG_ANSWER_WRITING_TEMPLATES.md#template-esercizio-1---dp-su-sequenze` |
| LCS variante con stato extra | `RAG_ANSWER_WRITING_TEMPLATES.md#template-esercizio-1---dp-su-sequenze` |
| LICS | `RAG_ANSWER_WRITING_TEMPLATES.md#template-esercizio-1---dp-su-sequenze` |
| Knapsack | `RAG_ANSWER_WRITING_TEMPLATES.md#template-esercizio-1---dp-su-sequenze` |
| Floyd-Warshall con stato extra | `RAG_ANSWER_WRITING_TEMPLATES.md#template-esercizio-2---dp-su-grafi` |
| DP su grafi con vincoli | `RAG_ANSWER_WRITING_TEMPLATES.md#template-esercizio-2---dp-su-grafi` |
| Greedy / Matroidi | `RAG_ANSWER_WRITING_TEMPLATES.md#template-teoria` |
| MST / Prim / Kruskal numerici | `RAG_ANSWER_WRITING_TEMPLATES.md#disegni-e-parti-grafiche` e method card step-by-step |
| Dijkstra numerico | `RAG_ANSWER_WRITING_TEMPLATES.md#disegni-e-parti-grafiche` e method card step-by-step |
| NP-completezza | `RAG_ANSWER_WRITING_TEMPLATES.md#template-teoria` |
| Riduzioni classiche | `RAG_ANSWER_WRITING_TEMPLATES.md#template-teoria` |
| Completamenti testuali | `RAG_ANSWER_WRITING_TEMPLATES.md#template-completamento-testuale` |

## Pattern: LCS standard

Trigger:

- due sequenze `X` e `Y`;
- sottosequenza comune piu lunga;
- prefissi `X_i`, `Y_j`;
- matrice `C` o ricostruzione Print-LCS.

Metodo:

- usare DP sui prefissi;
- stato `c_{i,j}`;
- casi base su prefisso vuoto;
- match/non-match;
- valore finale `c_{m,n}`.

File:

- `10_rag/RAG_METHOD_CARDS/dp_lcs_base.md`
- `04_methods/dp_lcs_base.md`
- `07_solved_examples/dp/lcs_base_6ott25.md`

Errori da evitare:

- non dimenticare i casi base;
- non confondere sottosequenza con sottostringa;
- non saltare la ricostruzione se richiesta.

## Pattern: LCS variante con stato extra

Trigger:

- LCS con colori, conteggi, parita, posizioni o vincoli interni;
- "al massimo", "esattamente", "almeno";
- "colore in {R,B,N}" + "presenza del rosso";
- "due rossi consecutivi";
- "dispari in posizioni dispari e pari in posizioni pari";
- tre sequenze.

Metodo:

- partire dallo schema LCS base;
- aggiungere solo lo stato necessario al vincolo;
- chiarire se il contatore e esatto, massimo, residuo, minimo o booleano;
- scegliere se il valore finale e una cella finale o un massimo globale.
- per `col:S->{R,B,N}` e presenza del rosso, usare stato `C[i,j,r]`, `r in {0,1}`, e indicatore `rho(a)=1 se rosso, 0 altrimenti`.

File:

- `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`
- `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`
- `04_methods/dp_lcs_due_rossi_consecutivi.md`
- `04_methods/dp_lcs_tre_sequenze.md`

Errori da evitare:

- non usare `-infinito` per ogni problema "al massimo" se una formulazione `<= k` e sufficiente;
- non usare due LCS successive per tre sequenze;
- non confondere posizione nella sottosequenza con indice nella sequenza originale.
- non scrivere `rho(a)=0 se blu` se il codominio include anche nero: blu e nero sono entrambi non-rossi.
- non aggiungere stati separati per blu/nero salvo vincoli espliciti su blu/nero.

## Disambiguazione LCS con pesi: budget totale vs monotonia

Quando una traccia LCS assegna un peso/ingombro `w(a)` ai simboli, distinguere subito questi due casi.

### Caso A - Budget totale / ingombro complessivo

Parole chiave:

```text
ingombro complessivo <= W
peso totale <= W
costo complessivo <= W
somma dei pesi <= W
budget W
```

Metodo:

```text
DP con budget: C[i,j,p], p=0,...,W
```

Soluzione tipica:

```text
C[m,n,W]
```

File:

- `10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md`
- `04_methods/dp_lcs_vincolo_somma_ingombro.md`
- `07_solved_examples/DP_LCS_ingombro_complessivo_W.md`

### Caso B - Monotonia / crescente rispetto a w

Parole chiave:

```text
pesi non decrescenti
sottosequenza crescente
ordine crescente rispetto a w
w(a_1) <= w(a_2) <= ...
```

Metodo:

```text
DP tipo LICS / stato che termina in una coppia di posizioni o in un valore precedente
```

### Regola anti-errore

```text
Non usare condizioni come w(prev) <= w(curr) quando la traccia parla solo di
"ingombro complessivo <= W". In quel caso serve consumare budget p-w(a).
```

## Pattern: LICS

Trigger:

- LICS;
- Longest Common Increasing Subsequence;
- sottosequenza comune crescente;
- sottoproblemi vincolati a terminare in un match.

Metodo:

- usare stati vincolati a terminare con `x_i = y_j`;
- se `x_i != y_j`, lo stato non rappresenta una soluzione valida;
- cercare predecessori compatibili e minori;
- prendere massimo globale.

File:

- `10_rag/RAG_METHOD_CARDS/dp_lics_varianti.md`
- `04_methods/dp_lics_e_varianti.md`
- `07_solved_examples/lics_schema.md`

Errori da evitare:

- non usare la ricorrenza LCS standard;
- non restituire automaticamente `c_{m,n}`;
- non dimenticare il vincolo di crescita sui valori.

## Pattern: Floyd-Warshall con stato extra

Trigger:

- "per ogni coppia di vertici";
- Floyd-Warshall;
- cammini minimi o esistenza di cammini;
- archi/vertici colorati;
- alternanza, conteggi, parita, presenza di colori.

Metodo:

- usare `k` come insieme di vertici intermedi ammessi `{1,...,k}`;
- definire il coefficiente con eventuali stati extra;
- ricorrenza: non uso `k` oppure passo da `k`;
- per cammini minimi usare `min/+`;
- per esistenza usare `OR/AND`.

File:

- `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`
- `10_rag/RAG_METHOD_CARDS/dp_grafi_stato_esteso.md`
- `04_methods/fw_varianti_vincoli_colori.md`
- `07_solved_examples/fw_varianti_vincoli_colori_schema.md`

Errori da evitare:

- non confondere archi colorati e vertici colorati;
- non usare pesi se il problema chiede solo esistenza;
- non aggiungere stati non necessari.

## Pattern: Knapsack

Trigger:

- zaino o knapsack;
- oggetti, peso, valore, capacita;
- vincolo "al massimo 3 oggetti rossi" o simili.

Metodo:

- per zaino 0/1 base usare DP include/esclude con stato `V[i,p]`;
- per colori aggiungere una dimensione `r` come budget residuo/massimo ammesso;
- se si sceglie un oggetto rosso, decrementare `r`.

File:

- `10_rag/RAG_METHOD_CARDS/dp_knapsack.md`
- `04_methods/dp_knapsack_base.md`
- `04_methods/dp_knapsack_vincoli_colore.md`
- `07_solved_examples/knapsack_al_massimo_3_rossi_schema.md`

Errori da evitare:

- knapsack 0/1 non e greedy;
- non confondere "al massimo" con "esattamente";
- non dimenticare la capacita come dimensione dello stato.

## Pattern: Greedy / Matroide

Trigger:

- greedy;
- matroide;
- ereditarieta, scambio, indipendenza;
- Rado-Edmonds;
- dimostrare correttezza di un algoritmo greedy.

Metodo:

- definire il sistema di indipendenza;
- verificare ereditarieta;
- verificare proprieta di scambio;
- concludere con il teorema di Rado-Edmonds quando applicabile.

File:

- `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`
- `05_theory/matroidi_e_greedy.md`
- `04_methods/metodo_greedy_matroidi_rado.md`

Errori da evitare:

- greedy non funziona sempre;
- non basta dire "scelgo localmente il migliore";
- non saltare la prova di scambio.

## Pattern: MST / Prim / Kruskal

Trigger:

- MST, albero ricoprente minimo;
- Prim, Kruskal;
- arco sicuro, taglio, arco leggero;
- union-find, archi ordinati, `key[v]`.

Metodo:

- per MST usare proprieta del taglio e arco sicuro;
- per Prim mantenere `key`, predecessore e insieme dei vertici non estratti;
- per Kruskal ordinare gli archi e aggiungere solo quelli che non creano cicli.

File:

- `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`
- `10_rag/RAG_METHOD_CARDS/mst_prim.md`
- `04_methods/metodo_kruskal_mst.md`
- `07_solved_examples/kruskal_schema_esecuzione.md`

Errori da evitare:

- MST non e shortest path;
- Prim non e Dijkstra;
- in Kruskal non aggiungere archi che chiudono cicli.

## Pattern: NP-completezza

Trigger:

- dimostrare NP-completo;
- NP-hard;
- certificato e verificatore;
- riduzione polinomiale;
- SAT, 3SAT, Clique, Vertex Cover, Independent Set.

Metodo:

- mostrare appartenenza a NP;
- scegliere un problema noto NP-completo;
- ridurre dal noto al nuovo target;
- dimostrare la doppia implicazione;
- concludere NP-completezza.

File:

- `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`
- `04_methods/np_completezza_schema_dimostrazione.md`
- `05_theory/riduzioni_np_completezza.md`
- `07_solved_examples/np_completezza_schema.md`

Errori da evitare:

- NP non significa "non polinomiale";
- non invertire la direzione della riduzione;
- per dimostrare che `B` e NP-completo si riduce da un noto NP-completo `A` verso `B`.

## Pattern: Riduzioni classiche

Trigger:

- 3SAT -> Clique;
- Clique -> Vertex Cover;
- Clique, Vertex Cover, Independent Set;
- grafo complemento;
- parametro `k` trasformato.

Metodo:

- indicare costruzione polinomiale;
- dichiarare parametro finale;
- provare entrambi i versi;
- controllare complementi e cardinalita.

File:

- `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`
- `04_methods/metodo_riduzione_3sat_clique.md`
- `04_methods/metodo_riduzione_clique_vertex_cover.md`
- `07_solved_examples/riduzioni_vertex_cover_clique_independent_set.md`

Errori da evitare:

- non confondere clique e independent set;
- non dimenticare che Clique e Vertex Cover usano il complemento nella riduzione standard;
- non sbagliare il parametro, spesso `n-k`.
