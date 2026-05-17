---
type: ingestion_report
source_id: SRC-EXAM-011
source_file: parteII-17set25.pdf
exam_date: 2025-09-17
exam_part: Parte II
status: applicato
tags:
  - apa
  - ingestion
  - exam/2025-09-17
  - part/II
---

# Ingestion Report — Appello APA 2025-09-17 Parte II

## Informazioni Fonte

| Campo | Valore |
|---|---|
| **Source ID** | SRC-EXAM-011 |
| **File** | `01_sources/exams_raw/parteII-17set25.pdf` |
| **Tipo** | Appello d'esame |
| **Data** | 17 settembre 2025 |
| **Parte** | Parte II |
| **Pagine** | 2 |
| **Immagini** | 2 (grafo Kruskal, griglia Q1–Q8) |

## Contenuto dell'Appello

L'appello contiene **5 esercizi** (nessuna domanda bonus esplicita):

| # | Argomento | Punti | Tipo |
|---|---|---:|---|
| 1 | Kruskal / Minimum Spanning Tree | 6 | Operativo (tracciamento progressivo) |
| 2 | Riduzione 3-SAT → CLIQUE | 6 | Operativo (costruzione grafo) |
| 3 | GREEDY-MAX e Teorema di Rado | 7 | Teorico (algoritmo + enunciato) |
| 4 | Criterio per NP-completezza | 7 | Teorico (risposta discorsiva) |
| 5 | Matroide grafico | 7 | Teorico (definizione + dimostrazione) |

## Analisi di Difficoltà

- **Esercizio 1**: Difficoltà *media*. Kruskal standard con 8 archi e tie-break da gestire (due archi di peso 1, due archi di peso 6).
- **Esercizio 2**: Difficoltà *media*. Riduzione 3-SAT → CLIQUE con 3 clausole (la prima e la terza sono identiche, ma generano vertici distinti nella riduzione).
- **Esercizio 3**: Difficoltà *media*. Scrittura dell'algoritmo GREEDY-MAX e enunciato del Teorema di Rado. Nessuna dimostrazione richiesta.
- **Esercizio 4**: Difficoltà *bassa-media*. Schema standard per dimostrare che un problema A è NP-completo.
- **Esercizio 5**: Difficoltà *alta*. Definizione del matroide grafico e dimostrazione completa dei 3 assiomi (non vuoto, ereditarietà, scambio).

## Note Specifiche

- **Clausole ripetute (E02)**: La formula $\varphi$ contiene $C_1 = C_3 = (x_1 \vee \neg x_2 \vee x_3)$. Nella riduzione, ciascuna occorrenza di clausola genera un gruppo distinto di 3 vertici. Il grafo ha quindi 9 vertici totali.
- **Nessuna domanda bonus**: A differenza degli appelli del 13 Gennaio e dell'11 Febbraio 2025, questo appello non include domande facoltative premiali.
- **Pattern confermato**: L'appello conferma lo schema ricorrente della Parte II: MST/Kruskal + riduzione NP + teoria Greedy/Matroidi + schema NPC + matroide grafico.

## Trascrizione

→ [[exam_2025_09_17_part2]]

## Esercizi Catalogati

→ [[exam_2025_09_17_p2_e01]] — Kruskal MST
→ [[exam_2025_09_17_p2_e02]] — Riduzione 3-SAT to CLIQUE
→ [[exam_2025_09_17_p2_e03]] — GREEDY-MAX e Teorema di Rado
→ [[exam_2025_09_17_p2_e04]] — Criterio NP-completezza
→ [[exam_2025_09_17_p2_e05]] — Matroide grafico
