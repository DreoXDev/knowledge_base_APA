# Piano Codex — Ingestion appello APA 2025-06-09 Parte II

## Obiettivo

Integrare nella knowledge base APA la seconda parte dell'appello del 9 giugno 2025.

```txt
Analisi e Progetto di Algoritmi — Parte II
Data: 9 giugno 2025
File sorgente: parteII-09giu25.pdf
Source ID: SRC-EXAM-007
```

L'appello contiene 5 esercizi/domande della Parte II:

1. **Esercizio 1 (val 6)**: Esecuzione di Dijkstra con sorgente s.
2. **Esercizio 2 (val 6)**: Riduzione polinomiale da CLIQUE a VERTEX-COVER.
3. **Esercizio 3 (val 7)**: Algoritmo GREEDY-MAX su Sistemi di Indipendenza ed enunciazione del Teorema di Rado.
4. **Esercizio 4 (val 7)**: Requisiti formali per dimostrare la NP-completezza di un problema generico A.
5. **Esercizio 5 (val 7)**: Definizione di matroide grafico e dimostrazione che soddisfa gli assiomi di matroide.

---

## 1. File da creare

Creare il report di ingestion:
- `09_ingestion_reports/ingestion_report_exam_2025_06_09_part2.md`

Creare la trascrizione dell'appello Parte II:
- `02_transcriptions/exams/exam_2025_06_09_part2.md`

Creare i cinque esercizi catalogati:
- `03_exercise_catalog/exercises/exam_2025_06_09_p2_e01.md`
- `03_exercise_catalog/exercises/exam_2025_06_09_p2_e02.md`
- `03_exercise_catalog/exercises/exam_2025_06_09_p2_e03.md`
- `03_exercise_catalog/exercises/exam_2025_06_09_p2_e04.md`
- `03_exercise_catalog/exercises/exam_2025_06_09_p2_e05.md`

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
- `metodo_dijkstra.md` (aggiungere collegamento)
- `metodo_riduzione_clique_vertex_cover.md` (aggiungere collegamento)
- `metodo_greedy_max_rado.md` (nuovo)
- `metodo_dimostrazione_matroide_grafico.md` (nuovo)
- `metodo_dimostrare_np_completezza.md` (nuovo)

Aggiornare la teoria correlata in `05_theory/`:
- `cammini_minimi.md`
- `clique.md`
- `vertex_cover.md`
- `np_completeness.md`
- `matroidi.md` (nuovo)

Aggiornare lo stato del progetto:
- `01_sources/source_inventory.md`
- `PROJECT_STATUS.md`
- `TODO.md`

---

## 3. Trascrizione essenziale dell'appello

Nel file `02_transcriptions/exams/exam_2025_06_09_part2.md`:

```md
---
type: exam_transcription
source: 01_sources/exams_raw/parteII-09giu25.pdf
source_id: SRC-EXAM-007
exam_date: 2025-06-09
status: transcribed
tags:
  - apa
  - appello
  - exam/raw
---

# Appello 2025-06-09 — Parte II

> [!Info]
> Fonte originale: `01_sources/exams_raw/parteII-09giu25.pdf`
>
> Source ID: `SRC-EXAM-007`
>
> Report: [[ingestion_report_exam_2025_06_09_part2]]

## Struttura dell'appello (Parte II)

| ID | Esercizio | Argomento | Punti | Stato |
|---|---|---|---:|---|
| [[exam_2025_06_09_p2_e01]] | Esercizio 1 | Dijkstra step-by-step | 6 | cataloged |
| [[exam_2025_06_09_p2_e02]] | Esercizio 2 | Riduzione CLIQUE to VERTEX-COVER | 6 | cataloged |
| [[exam_2025_06_09_p2_e03]] | Esercizio 3 | GREEDY-MAX e Teorema di Rado | 7 | cataloged |
| [[exam_2025_06_09_p2_e04]] | Esercizio 4 | Teoria: Requisiti per NP-completezza di A | 7 | cataloged |
| [[exam_2025_06_09_p2_e05]] | Esercizio 5 | Teoria: Dimostrazione matroide grafico | 7 | cataloged |

## Trascrizione Testo

### Esercizio 1 (valore 6)
Mostrare, per ogni nodo del grafo sotto riportato e all’interno dei cerchi rappresentanti i nodi, il valore dell’attributo d dopo l’estrazione di un certo nodo durante l’esecuzione dell’algoritmo di Dijkstra, considerando il nodo s come sorgente. Specificare (in corrispondenza dei puntini) il nodo che viene ad ogni passo estratto ed evidenziare gli archi che vengono effettivamente rilassati ad ogni passo dalla procedura di rilassamento.

*Estrazioni:* s, ..., ..., ..., ..., ...

### Esercizio 2 (valore 6)
Dato il grafo G sotto riportato, disegnare il grafo G' che si ottiene nella riduzione da CLIQUE a VERTEX COVER, indicando quanti e quali sono i vertici della copertura di vertici di G'.

*La copertura di vertici di G' è composta dai seguenti vertici ..................................................... in numero pari a ......*

### Esercizio 3 (valore 7)
Scrivere l’algoritmo (GREEDY-MAX) associato a un Sistema di Indipendenza (E,F) e a una funzione peso w : E -> R+. Enunciare inoltre il teorema di Rado (non è richiesta la dimostrazione).

### Esercizio 4 (valore 7)
Considerando un problema specifico A, tra quelli visti a lezione, cosa è sufficiente mostrare relativamente ad A per stabilire che A è NP-completo? Rispondere nello spazio sottostante. Nota Bene: non è richiesta alcuna dimostrazione.

### Esercizio 5 (valore 7)
Sia G = (V,E) un grafo non orientato. Definire il matroide grafico e dimostrare che è a tutti gli effetti un matroide. Nota Bene: non occorre dimostrare che il numero di alberi in una foresta è pari alla differenza tra il numero di vertici e il numero di archi (RISPONDERE SUL FOGLIO PROTOCOLLO).
```
