---
type: ingestion_report
source_id: SRC-EXAM-013
file_name: parteII-10nov25.pdf
exam_date: 2025-11-10
exam_part: II
status: applied
created_at: 2026-05-17T23:08:30Z
---

# Ingestion Report — Appello APA 2025-11-10 Parte II

## 1. Metadata della fonte

* **ID Fonte**: SRC-EXAM-013
* **Nome File**: `01_sources/exams_raw/parteII-10nov25.pdf`
* **Corso**: Analisi e Progetto di Algoritmi (APA)
* **Data Appello**: 10 novembre 2025
* **Parte**: Parte II
* **Punteggio Totale**: 33 punti (5 esercizi)
* **Lingua**: Italiano
* **Stato**: Ingestito e catalogato con successo

---

## 2. Sintesi del contenuto dell'appello

Questo appello di Parte II contiene 5 esercizi focalizzati su simulazione di algoritmi su grafi (MST/Kruskal), riduzioni polinomiali (3-SAT to CLIQUE), equazioni di ricorrenza (chiusura transitiva), requisiti formali per dimostrazione di NP-completezza e dimostrazione teorica su matroidi.

### Esercizio 1: Kruskal / Minimum Spanning Tree (valore: 6 punti)
* **Tipo**: Operativo (Simulazione manuale)
* **Argomento**: Minimum Spanning Tree (MST) con l'algoritmo di Kruskal.
* **Grafo**: Undirected, connesso, pesato con 5 vertici $\{a, b, c, d, e\}$ e 7 archi.
* **Richiesta**: Mostrare passo-passo la foresta progressiva (in quadrati `Q1` a `Q7`) che rappresenta gli archi aggiunti al MST dopo ciascun passo.

### Esercizio 2: Riduzione polinomiale 3-CNF-SAT → CLIQUE (valore: 6 punti)
* **Tipo**: Operativo (Costruzione del grafo di riduzione)
* **Argomento**: Riduzione polinomiale da 3-SAT a CLIQUE.
* **Formula**: $f = (\neg x_1 \lor x_2 \lor x_3) \land (x_1 \lor \neg x_2 \lor x_3) \land (x_1 \lor x_2 \lor \neg x_3)$.
* **Richiesta**: Disegnare il grafo ottenuto dalla riduzione polinomiale disponendo i vertici della prima clausola a sinistra, della seconda in alto, e della terza a destra.

### Esercizio 3: Equazioni di ricorrenza per la chiusura transitiva (valore: 7 punti)
* **Tipo**: Teorico/Pratico (Formulazione di ricorrenze)
* **Argomento**: Algoritmo di Warshall per la chiusura transitiva o riflessiva-transitiva.
* **Richiesta**: Scrivere le equazioni di ricorrenza (caso base e passo ricorsivo) per calcolare la raggiungibilità $e^k_{ij}$.

### Esercizio 4: Criterio per dimostrare la NP-completezza di un problema (valore: 7 punti)
* **Tipo**: Teorico (Descrizione di protocollo)
* **Argomento**: Classi P, NP, NP-completezza.
* **Richiesta**: Descrivere cosa sia sufficiente mostrare relativamente a un problema incognito $A$ per stabilire che esso è NP-completo.

### Esercizio 5: Definizione e dimostrazione del matroide grafico (valore: 7 punti)
* **Tipo**: Teorico (Dimostrazione matematica)
* **Argomento**: Teoria dei Matroidi e sistemi di indipendenza.
* **Richiesta**: Definire formalmente il matroide grafico associato a un grafo non orientato $G = (V,E)$ e dimostrare che soddisfa gli assiomi di matroide (ereditarietà e scambio).

---

## 3. Mappatura dei file creati e aggiornati

### File Creati
* Trascrizione: [exam_2025_11_10_part2.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/02_transcriptions/exams/exam_2025_11_10_part2.md)
* Esercizi catalogati in `03_exercise_catalog/exercises/`:
  - Esercizio 1: [exam_2025_11_10_p2_e01.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_11_10_p2_e01.md)
  - Esercizio 2: [exam_2025_11_10_p2_e02.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_11_10_p2_e02.md)
  - Esercizio 3: [exam_2025_11_10_p2_e03.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_11_10_p2_e03.md)
  - Esercizio 4: [exam_2025_11_10_p2_e04.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_11_10_p2_e04.md)
  - Esercizio 5: [exam_2025_11_10_p2_e05.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/03_exercise_catalog/exercises/exam_2025_11_10_p2_e05.md)
* Nuovo metodo didattico: [metodo_riduzione_3sat_clique.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods/metodo_riduzione_3sat_clique.md)

### File Aggiornati
* Metodo Kruskal: [metodo_kruskal_mst.md](file:///C:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods/metodo_kruskal_mst.md)
* Indici: `index_by_exam.md`, `index_by_topic.md`, `index_by_difficulty.md`
* Pattern: `recurring_exercise_types.md`, `variations_by_appeal.md`, `high_yield_topics.md`
* Status & Avanzamento: `source_inventory.md`, `PROJECT_STATUS.md`, `TODO.md`
