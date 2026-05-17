# Ingestion Report — Exam 2025-07-03 Part II

## Metadata della fonte

- **Source ID**: `SRC-EXAM-009`
- **File**: `01_sources/exams_raw/parteII-03lug25.pdf`
- **Tipo**: appello esame scritto (Parte II)
- **Data appello**: 3 luglio 2025
- **Parte**: II
- **Stato**: applicato
- **Data ingestion**: 17 maggio 2026

---

## Analisi del contenuto

L'appello della Parte II del 3 luglio 2025 contiene 5 esercizi/domande a risposta aperta, ciascuno con un proprio valore in punti:

### Esercizio 1 (valore 6): Dijkstra step-by-step
- **Tipologia**: Cammini minimi da sorgente singola su grafo orientato/pesato.
- **Dettagli**: Richiede di eseguire manualmente l'algoritmo di Dijkstra con sorgente $A$. Si deve indicare, per ogni nodo, il valore della stima di cammino minimo $d$ dopo ogni estrazione, specificare l'ordine di estrazione ed evidenziare gli archi che subiscono rilassamenti ad ogni passo.
- **Valutazione metodologica**: Fa riferimento al metodo generale di tracciamento dell'esecuzione manuale di Dijkstra, che sarà documentato in `metodo_dijkstra`.

### Esercizio 2 (valore 6): Riduzione da CLIQUE a VERTEX-COVER
- **Tipologia**: NP-completezza e riduzioni polinomiali.
- **Dettagli**: Dato un grafo specifico $G$, si chiede di disegnare il grafo $G'$ ottenuto tramite la riduzione polinomiale classica da CLIQUE a VERTEX-COVER, specificando il numero e i vertici esatti della copertura di $G'$.
- **Valutazione metodologica**: Utilizza la riduzione tramite il grafo complementare ($G' = G^c$) e la proprietà per cui una clique di dimensione $k$ in $G$ corrisponde a una copertura di vertici di dimensione $|V| - k$ in $G^c$.

### Esercizio 3 (valore 7): Ricorrenza per la Chiusura Transitiva (Warshall)
- **Tipologia**: Programmazione dinamica su grafi.
- **Dettagli**: Scrivere le equazioni di ricorrenza (caso base e passo ricorsivo) per calcolare la chiusura transitiva o riflessiva-transitiva di un grafo $G=(V,E)$ usando il coefficiente $e_{i,j}^{(k)}$. Viene richiesto in via preliminare di specificare chiaramente il significato matematico del parametro $k$.
- **Valutazione metodologica**: Fa riferimento all'algoritmo di Floyd-Warshall/Warshall con coefficienti booleani, dove $k$ indica che i nodi intermedi appartengono all'insieme $\{1, \dots, k\}$.

### Esercizio 4 (valore 7): Teoria sulle Classi di Complessità
- **Tipologia**: Teoria della complessità computazionale.
- **Dettagli**: Definire formalmente le classi di problemi decisioni $P$, $NP$ e $NP$-completi ($NPC$).
- **Valutazione metodologica**: Risponde a requisiti puramente teorici e formali sulle riduzioni polinomiali e la non-determinazione.

### Esercizio 5 (valore 7): Teoria sul Minimum Spanning Tree
- **Tipologia**: Teoria degli algoritmi greedy su grafi.
- **Dettagli**: Enunciare e dimostrare formalmente il teorema dell'arco sicuro (Safe Edge Theorem) per i Minimum Spanning Tree.
- **Valutazione metodologica**: Richiede la dimostrazione formale sul taglio e sulla stabilità del MST, cruciale per la correttezza degli algoritmi greedy di Kruskal e Prim.

---

## Mappatura dei file della Knowledge Base

- **Trascrizione**: [[exam_2025_07_03_part2]] in `02_transcriptions/exams/`
- **Esercizi catalogati**:
  - Esercizio 1: [[exam_2025_07_03_p2_e01]] in `03_exercise_catalog/exercises/`
  - Esercizio 2: [[exam_2025_07_03_p2_e02]] in `03_exercise_catalog/exercises/`
  - Esercizio 3: [[exam_2025_07_03_p2_e03]] in `03_exercise_catalog/exercises/`
  - Esercizio 4: [[exam_2025_07_03_p2_e04]] in `03_exercise_catalog/exercises/`
  - Esercizio 5: [[exam_2025_07_03_p2_e05]] in `03_exercise_catalog/exercises/`
- **Metodi associati**:
  - Esercizio 1: [[metodo_dijkstra]] (nuovo)
  - Esercizio 2: [[metodo_riduzione_clique_vertex_cover]] (esistente)
  - Esercizio 3: [[metodo_equazioni_ricorrenza_chiusura_transitiva]] (nuovo)
  - Esercizio 5: [[metodo_teorema_arco_sicuro]] (nuovo)
