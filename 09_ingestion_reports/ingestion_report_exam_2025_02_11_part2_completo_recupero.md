---
type: ingestion_report
source_id: SRC-EXAM-005
file_name: parteII-11feb25-completo-recupero.pdf
exam_date: 2025-02-11
exam_part: II
status: applied
created_at: 2026-05-17T23:13:00Z
---

# Ingestion Report — Appello APA 2025-02-11 Parte II completo/recupero

## 1. Metadata della fonte

* **ID Fonte**: SRC-EXAM-005
* **Nome File**: `01_sources/exams_raw/parteII-11feb25-completo-recupero.pdf`
* **Corso**: Analisi e Progetto di Algoritmi (APA)
* **Data Appello**: 11 febbraio 2025
* **Parte**: Parte II completo / recupero
* **Punteggio Totale**: 33 punti principali + 3 punti bonus (5 esercizi principali + 1 domanda bonus a scelta)
* **Lingua**: Italiano
* **Stato**: Ingestito e catalogato con successo

---

## 2. Sintesi del contenuto dell'appello

Questo appello di Parte II completo/recupero contiene 5 esercizi principali focalizzati su simulazione di algoritmi su grafi (MST/Kruskal), riduzioni concrete (CLIQUE to VERTEX-COVER su un grafo a 6 nodi), formulazione di ricorrenze per problemi classici (Knapsack 0/1), descrizioni di riduzioni generali (3-SAT to CLIQUE/INDEPENDENT SET), e dimostrazione teorica del Teorema dell'arco sicuro, insieme a tre domande bonus a scelta da 3 punti (Greedy su matroidi, riduzione CLIQUE-VC, correttezza di Dijkstra).

### Esercizio 1: Kruskal / Minimum Spanning Tree (valore: 6 punti)
* **Tipo**: Operativo (Simulazione manuale)
* **Argomento**: Minimum Spanning Tree (MST) con l'algoritmo di Kruskal.
* **Grafo**: Undirected, connesso, pesato con 5 vertici $\{a, b, c, d, e\}$ e 7 archi.
* **Richiesta**: Mostrare passo-passo la foresta progressiva (in quadrati `Q1` a `Q7`) che rappresenta gli archi aggiunti al MST dopo ciascun passo.

### Esercizio 2: Riduzione da CLIQUE a VERTEX-COVER su grafo concreto (valore: 6 punti)
* **Tipo**: Operativo (Costruzione del grafo di riduzione e copertura)
* **Argomento**: Riduzione da CLIQUE a VERTEX-COVER tramite complementare.
* **Grafo**: $G$ con 6 nodi $\{a, b, c, d, e, f\}$ e 7 archi.
* **Richiesta**: Disegnare il grafo complementare $G'$ ottenuto nella riduzione ed indicare quali e quanti vertici compongono la vertex cover in $G'$ corrispondente a una clique in $G$.

### Esercizio 3: Knapsack 0/1 ricorrenza DP (valore: 7 punti)
* **Tipo**: Teorico/Pratico (Formulazione di ricorrenze)
* **Argomento**: Zaino 0/1 (Knapsack 0/1) con programmazione dinamica.
* **Richiesta**: Scrivere le equazioni di ricorrenza (casi base e passo ricorsivo) per determinare il valore ottimo usando $OPT(i,c)$.

### Esercizio 4: Riduzione polinomiale 3-SAT → CLIQUE / INDEPENDENT SET (valore: 7 punti)
* **Tipo**: Teorico (Descrizione di riduzione generale)
* **Argomento**: Riduzione da 3-SAT a CLIQUE o INDEPENDENT SET (a scelta dello studente).
* **Richiesta**: Definire formalmente la costruzione del grafo di riduzione a partire da una generica formula 3-SAT.

### Esercizio 5: Enunciato e dimostrazione del Teorema dell'arco sicuro (valore: 7 punti)
* **Tipo**: Teorico (Dimostrazione matematica)
* **Argomento**: Minimum Spanning Tree (MST) e Safe Edge Theorem.
* **Richiesta**: Enunciare e dimostrare formalmente il teorema dell'arco sicuro.

### Domande facoltative premiali (valore: 3 punti bonus, una a scelta)
* **Q1**: Dimostrare che se un sistema di indipendenza è un matroide, l'algoritmo Greedy-max restituisce una soluzione ottima.
* **Q2**: Dimostrare formalmente che CLIQUE si riduce a VERTEX-COVER ($CLIQUE \le_p VERTEX-COVER$).
* **Q3**: Dimostrare la correttezza dell'algoritmo di Dijkstra.

---

## 3. Mappatura dei file creati e aggiornati

### File Creati
* Trascrizione: [exam_2025_02_11_part2_completo_recupero.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/02_transcriptions/exams/exam_2025_02_11_part2_completo_recupero.md)
* Esercizi catalogati in `03_exercise_catalog/exercises/`:
  - Esercizio 1: [exam_2025_02_11_p2_completo_recupero_e01.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e01.md)
  - Esercizio 2: [exam_2025_02_11_p2_completo_recupero_e02.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e02.md)
  - Esercizio 3: [exam_2025_02_11_p2_completo_recupero_e03.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e03.md)
  - Esercizio 4: [exam_2025_02_11_p2_completo_recupero_e04.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e04.md)
  - Esercizio 5: [exam_2025_02_11_p2_completo_recupero_e05.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e05.md)
  - Domande Bonus: [exam_2025_02_11_p2_completo_recupero_bonus.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_bonus.md)
* Nuovi metodi didattici:
  - [metodo_knapsack_01_dp.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods/metodo_knapsack_01_dp.md)
  - [metodo_riduzione_3sat_independent_set.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods/metodo_riduzione_3sat_independent_set.md)
  - [metodo_dimostrazione_correttezza_dijkstra.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods/metodo_dimostrazione_correttezza_dijkstra.md)
  - [metodo_teorema_arco_sicuro.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods/metodo_teorema_arco_sicuro.md)
  - [metodo_greedy_matroidi_rado.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods/metodo_greedy_matroidi_rado.md)
* File di Teoria:
  - [knapsack_01.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/05_theory/knapsack_01.md)
  - [arco_sicuro.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/05_theory/arco_sicuro.md)
  - [clique_vertex_cover_independent_set.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/05_theory/clique_vertex_cover_independent_set.md)
  - [matroidi_e_greedy.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/05_theory/matroidi_e_greedy.md)
  - [dijkstra_correttezza.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/05_theory/dijkstra_correttezza.md)

### File Aggiornati
* Indici: `index_by_exam.md`, `index_by_topic.md`, `index_by_difficulty.md`
* Pattern: `recurring_exercise_types.md`, `variations_by_appeal.md`, `high_yield_topics.md`, `parte_ii_theory_and_graph_patterns.md`
* Status & Avanzamento: `source_inventory.md`, `PROJECT_STATUS.md`, `TODO.md`
