# Ingestion Report — Exam 2025-06-09 Part II

## Metadata della fonte

- **Source ID**: `SRC-EXAM-007`
- **File**: `01_sources/exams_raw/parteII-09giu25.pdf`
- **Tipo**: appello esame scritto (Parte II)
- **Data appello**: 9 giugno 2025
- **Parte**: II
- **Stato**: applicato
- **Data ingestion**: 17 maggio 2026

---

## Analisi del contenuto

L'appello della Parte II del 9 giugno 2025 contiene 5 esercizi/domande a risposta aperta:

### Esercizio 1 (valore 6): Dijkstra step-by-step
- **Tipologia**: Cammini minimi da sorgente singola su grafo orientato/pesato.
- **Dettagli**: Richiede di simulare l'algoritmo di Dijkstra a partire dalla sorgente $s$, tracciando l'evoluzione dei valori $d$ nei nodi, l'ordine di estrazione e gli archi rilassati.
- **Valutazione metodologica**: Utilizza lo schema consolidato in `metodo_dijkstra`.

### Esercizio 2 (valore 6): Riduzione da CLIQUE a VERTEX-COVER
- **Tipologia**: NP-completezza e riduzioni polinomiali.
- **Dettagli**: Richiede di disegnare il grafo complementare $G'$ e indicare numero e vertici della copertura di $G'$ a partire da un grafo $G$ fornito.
- **Valutazione metodologica**: Utilizza lo schema consolidato in `metodo_riduzione_clique_vertex_cover`.

### Esercizio 3 (valore 7): Algoritmo GREEDY-MAX e Teorema di Rado
- **Tipologia**: Teoria degli algoritmi greedy e matroidi.
- **Dettagli**: Chiede di scrivere in pseudocodice l'algoritmo GREEDY-MAX per un sistema di indipendenza $(E,F)$ con funzione peso $w: E \to \mathbb{R}^+$, ed enunciare il celebre Teorema di Rado (caratterizzazione dei sistemi di indipendenza in cui il greedy restituisce sempre l'ottimo). La dimostrazione del teorema non è richiesta.
- **Valutazione metodologica**: Richiede la stesura del metodo `metodo_greedy_max_rado`.

### Esercizio 4 (valore 7): Requisiti per NP-completezza di un problema A
- **Tipologia**: Teoria della complessità computazionale.
- **Dettagli**: Chiede cosa sia necessario mostrare formalmente per stabilire che un problema specifico $A$ (scelto tra quelli del corso) è NP-completo, senza richiedere la dimostrazione effettiva.
- **Valutazione metodologica**: Coinvolge la definizione di NP-completezza, in particolare i due passaggi chiave ($A \in NP$ e riduzione polinomiale da un problema noto $B \le_p A$). Sarà documentato in `metodo_dimostrare_np_completezza`.

### Esercizio 5 (valore 7): Definizione e dimostrazione del Matroide Grafico
- **Tipologia**: Teoria dei matroidi su grafi.
- **Dettagli**: Definire formalmente la coppia $(E,F)$ di un matroide grafico per un grafo non orientato $G=(V,E)$ e dimostrare che soddisfa gli assiomi di matroide (ereditarietà e scambio). Viene esplicitato che non occorre dimostrare la proprietà sul numero di alberi di una foresta ($|I| = |V| - c(I)$).
- **Valutazione metodologica**: Richiede la stesura del metodo `metodo_dimostrazione_matroide_grafico` e della nota teorica `matroidi`.

---

## Mappatura dei file della Knowledge Base

- **Trascrizione**: [[exam_2025_06_09_part2]] in `02_transcriptions/exams/`
- **Esercizi catalogati**:
  - Esercizio 1: [[exam_2025_06_09_p2_e01]] in `03_exercise_catalog/exercises/`
  - Esercizio 2: [[exam_2025_06_09_p2_e02]] in `03_exercise_catalog/exercises/`
  - Esercizio 3: [[exam_2025_06_09_p2_e03]] in `03_exercise_catalog/exercises/`
  - Esercizio 4: [[exam_2025_06_09_p2_e04]] in `03_exercise_catalog/exercises/`
  - Esercizio 5: [[exam_2025_06_09_p2_e05]] in `03_exercise_catalog/exercises/`
- **Metodi associati**:
  - Esercizio 1: [[metodo_dijkstra]] (esistente, collegato)
  - Esercizio 2: [[metodo_riduzione_clique_vertex_cover]] (esistente, collegato)
  - Esercizio 3: [[metodo_greedy_max_rado]] (nuovo)
  - Esercizio 4: [[metodo_dimostrare_np_completezza]] (nuovo)
  - Esercizio 5: [[metodo_dimostrazione_matroide_grafico]] (nuovo)
