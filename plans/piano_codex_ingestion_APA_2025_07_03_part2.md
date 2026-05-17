# Piano Codex — Ingestion appello APA 2025-07-03 Parte II

## Obiettivo

Integrare nella knowledge base APA la seconda parte dell'appello del 3 luglio 2025.

```txt
Analisi e Progetto di Algoritmi — Parte II
Data: 3 luglio 2025
File sorgente: parteII-03lug25.pdf
Source ID: SRC-EXAM-009
```

L'appello contiene 5 esercizi/domande della Parte II:

1. **Esercizio 1 (val 6)**: Esecuzione di Dijkstra con sorgente A.
2. **Esercizio 2 (val 6)**: Riduzione polinomiale da CLIQUE a VERTEX-COVER (disegno di G', numero e lista vertici della copertura).
3. **Esercizio 3 (val 7)**: Equazioni di ricorrenza per la chiusura transitiva/riflessiva-transitiva ($e_{i,j}^{(k)}$) e significato di $k$.
4. **Esercizio 4 (val 7)**: Definizione formale delle classi di problemi P, NP e NP-completi.
5. **Esercizio 5 (val 7)**: Enunciato e dimostrazione del teorema dell'arco sicuro (Safe Edge Theorem).

---

## 1. File da creare

Creare il report di ingestion:
- `09_ingestion_reports/ingestion_report_exam_2025_07_03_part2.md`

Creare la trascrizione dell'appello Parte II:
- `02_transcriptions/exams/exam_2025_07_03_part2.md`

Creare i cinque esercizi catalogati:
- `03_exercise_catalog/exercises/exam_2025_07_03_p2_e01.md`
- `03_exercise_catalog/exercises/exam_2025_07_03_p2_e02.md`
- `03_exercise_catalog/exercises/exam_2025_07_03_p2_e03.md`
- `03_exercise_catalog/exercises/exam_2025_07_03_p2_e04.md`
- `03_exercise_catalog/exercises/exam_2025_07_03_p2_e05.md`

---

## 2. File da aggiornare

Aggiornare gli indici:
- `03_exercise_catalog/index_by_exam.md`
- `03_exercise_catalog/index_by_topic.md`
- `03_exercise_catalog/index_by_difficulty.md`

Aggiornare i pattern e le variazioni:
- `06_exam_patterns/recurring_exercise_types.md`
- `06_exam_patterns/variations_by_appeal.md`
- `06_exam_patterns/high_yield_topics.md`

Aggiornare/creare i metodi correlati in `04_methods/`:
- `metodo_dijkstra.md` (nuovo)
- `metodo_riduzione_clique_vertex_cover.md` (aggiornare)
- `metodo_equazioni_ricorrenza_chiusura_transitiva.md` (nuovo)
- `metodo_teorema_arco_sicuro.md` (nuovo)

Aggiornare la teoria correlata in `05_theory/`:
- `cammini_minimi.md`
- `floyd_warshall.md`
- `clique.md`
- `vertex_cover.md`
- `np_completeness.md`
- `minimum_spanning_tree.md`

Aggiornare lo stato del progetto:
- `01_sources/source_inventory.md`
- `PROJECT_STATUS.md`
- `TODO.md`

---

## 3. Trascrizione essenziale dell'appello

Nel file `02_transcriptions/exams/exam_2025_07_03_part2.md`:

```md
---
type: exam_transcription
source: 01_sources/exams_raw/parteII-03lug25.pdf
source_id: SRC-EXAM-009
exam_date: 2025-07-03
status: transcribed
tags:
  - apa
  - appello
  - exam/raw
---

# Appello 2025-07-03 — Parte II

> [!Info]
> Fonte originale: `01_sources/exams_raw/parteII-03lug25.pdf`
>
> Source ID: `SRC-EXAM-009`
>
> Report: [[ingestion_report_exam_2025_07_03_part2]]

## Struttura dell'appello (Parte II)

| ID | Esercizio | Argomento | Punti | Stato |
|---|---|---|---:|---|
| [[exam_2025_07_03_p2_e01]] | Esercizio 1 | Dijkstra step-by-step | 6 | cataloged |
| [[exam_2025_07_03_p2_e02]] | Esercizio 2 | Riduzione CLIQUE to VERTEX-COVER | 6 | cataloged |
| [[exam_2025_07_03_p2_e03]] | Esercizio 3 | Chiusura transitiva (Floyd-Warshall) | 7 | cataloged |
| [[exam_2025_07_03_p2_e04]] | Esercizio 4 | Teoria: Classi P, NP, NP-completo | 7 | cataloged |
| [[exam_2025_07_03_p2_e05]] | Esercizio 5 | Teoria: Teorema dell'arco sicuro | 7 | cataloged |

## Trascrizione Testo

### Esercizio 1 (valore 6)
Mostrare, per ogni nodo del grafo sotto riportato e all’interno dei cerchi rappresentanti i nodi, il valore dell’attributo d dopo l’estrazione di un certo nodo durante l’esecuzione dell’algoritmo di Dijkstra, considerando il nodo A come sorgente. Specificare (in corrispondenza dei puntini) il nodo che viene ad ogni passo estratto ed evidenziare gli archi che vengono effettivamente rilassati ad ogni passo dalla procedura di rilassamento.
*Estrazioni:* A, ..., ..., ..., ..., ...

### Esercizio 2 (valore 6)
Dato il grafo G sotto riportato, disegnare il grafo G' che si ottiene nella riduzione da CLIQUE a VERTEX COVER, indicando quanti e quali sono i vertici della copertura di vertici di G'.
*Risposta:* La copertura di vertici di G' è composta dai seguenti vertici .................... in numero pari a ......

### Esercizio 3 (valore 7)
Sia G=(V,E) un grafo. Scrivere nello spazio sottostante le equazioni di ricorrenza (caso base e passo ricorsivo) per stabilire, per ogni coppia (i,j) di vertici, se esiste un cammino da i a j, ossia scrivere le equazioni di ricorrenza per il calcolo della chiusura transitiva/riflessiva-transitiva di G, nelle quali $e_{i,j}^{(k)}$ è il coefficiente. Prima di scrivere le equazioni di ricorrenza, si chiede di indicare chiaramente il significato di k che appare nel coefficiente.

### Esercizio 4 (valore 7)
Definire le classi di problemi P, NP e NP-completi.

### Esercizio 5 (valore 7)
Enunciare e dimostrare il teorema dell'arco sicuro (RISPONDERE SUL FOGLIO PROTOCOLLO).
```

---

## 4. Esercizio 1 — Catalogazione
File: `03_exercise_catalog/exercises/exam_2025_07_03_p2_e01.md`
- **Topic**: Algoritmi su grafi / Cammini minimi / Dijkstra
- **Difficulty**: Medium
- **Pattern**: Esecuzione manuale di Dijkstra con tracciamento di $d$ e rilassamenti.

---

## 5. Esercizio 2 — Catalogazione
File: `03_exercise_catalog/exercises/exam_2025_07_03_p2_e02.md`
- **Topic**: NP-completezza / Riduzioni polinomiali / CLIQUE / Vertex Cover
- **Difficulty**: Medium
- **Pattern**: Riduzione da CLIQUE a VERTEX-COVER tramite grafo complementare $G^c$. Copertura in $G^c$ avente dimensione $|V| - k$.

---

## 6. Esercizio 3 — Catalogazione
File: `03_exercise_catalog/exercises/exam_2025_07_03_p2_e03.md`
- **Topic**: Programmazione dinamica / Chiusura transitiva / Floyd-Warshall
- **Difficulty**: Easy-Medium
- **Pattern**: Formulazione formale della chiusura transitiva (algoritmo di Warshall). Coefficiente $e_{i,j}^{(k)}$ indicante l'esistenza di un cammino da $i$ a $j$ con nodi intermedi in $\{1,\dots,k\}$.

---

## 7. Esercizio 4 — Catalogazione
File: `03_exercise_catalog/exercises/exam_2025_07_03_p2_e04.md`
- **Topic**: Teoria / Complessità computazionale / P, NP, NP-completo
- **Difficulty**: Easy
- **Pattern**: Definizioni formali di complessità.

---

## 8. Esercizio 5 — Catalogazione
File: `03_exercise_catalog/exercises/exam_2025_07_03_p2_e05.md`
- **Topic**: Teoria / Minimum Spanning Tree / Teorema dell'arco sicuro
- **Difficulty**: Hard
- **Pattern**: Dimostrazione formale del Teorema dell'arco sicuro (Safe Edge Theorem) per il calcolo del MST.

---

## 9. Stato atteso e aggiornamenti indici

Gli indici e i pattern verranno aggiornati puntualmente per includere la seconda parte di questo appello. In `PROJECT_STATUS.md` l'appello `SRC-EXAM-009` passerà allo stato `applicato`.
