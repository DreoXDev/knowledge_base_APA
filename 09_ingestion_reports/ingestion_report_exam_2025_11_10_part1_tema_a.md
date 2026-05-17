# Ingestion Report — exam_2025_11_10_part1_tema_a

> [!Info]
> Report finale per l'ingestione dell'appello `parte-I-10nov25-A.pdf` nella knowledge base Obsidian `knowledge_base_APA`.
>
> Stato report: `ready_for_codex`
>
> Obiettivo: catalogare la Parte I dell'appello del 10 novembre 2025, variante Tema A, aggiornando trascrizioni, catalogo esercizi, pattern ricorrenti, metodi e teoria minima.

---

## 1. Metadata

- Source ID: `exam_2025_11_10_part1_tema_a`
- File sorgente consigliato nella repo: `01_sources/exams_raw/parte-I-10nov25-A.pdf`
- File PDF analizzato: `parte-I-10nov25-A.pdf`
- Tipo fonte: `appello_raw`
- Corso: `Analisi e Progetto di Algoritmi`
- Data appello: `2025-11-10`
- Parte: `Parte I`
- Variante: `Tema A`
- Numero pagine: `2`
- Stato fonte: `report_creato`
- Stato report: `ready_for_codex`
- Priorità: `alta`
- Nome report consigliato: `09_ingestion_reports/ingestion_report_exam_2025_11_10_part1_tema_a.md`

---

## 2. Sintesi contenuto

L'appello contiene solo la Parte I e presenta due esercizi, entrambi di programmazione dinamica:

```txt
Parte I — 10 novembre 2025 (Tema A)

Esercizio 1:
- LCS tra due sequenze X e Y.
- Ogni simbolo ha colore rosso, blu o nero.
- Si vuole una più lunga sottosequenza comune di X e Y nella quale sia presente almeno un simbolo rosso.
- Richiede coefficienti, caso base, passo ricorsivo, coefficiente ottimo, algoritmo bottom-up e ricostruzione.

Esercizio 2:
- Grafo con archi etichettati A/B/C.
- Stabilire per ogni coppia di vertici se esiste un cammino in cui la somma tra il numero di archi con lettera A e il numero di archi con lettera B sia uguale a 3.
- Richiede coefficienti, caso base, passo ricorsivo e soluzione finale.
```

Pattern forti:
- programmazione dinamica tabellare;
- LCS con stato esteso da vincolo booleano di presenza del rosso;
- ricostruzione della soluzione in DP;
- DP booleana su grafi etichettati;
- Floyd-Warshall modificato con stato esteso per conteggio di archi di un certo tipo;
- budget aggregato nello stato esteso.

---

## 3. Pagine / sezioni analizzate

| Pagina PDF | Contenuto |
|---|---|
| 1 | Parte I, Esercizio 1: LCS con presenza obbligatoria di almeno un simbolo rosso |
| 2 | Parte I, Esercizio 2: cammini in grafo etichettato con somma di archi A/B uguale a 3 |

---

## 4. Argomenti individuati

```md
- #topic/programmazione-dinamica
- #topic/lcs
- #topic/sottosequenze
- #topic/vincoli-di-presenza
- #topic/colori
- #topic/ricorrenze-dp
- #topic/ricostruzione-soluzione
- #topic/grafi
- #topic/grafi-colorati
- #topic/cammini
- #topic/dp-booleana
- #topic/stato-esteso
- #topic/problema-ausiliario
```

---

## 5. Stato di Ingestione

Tutti i file descritti nel piano sono stati creati e collegati correttamente.
Le modifiche apportate normalizzano la presenza di accenti nei file esistenti e inseriscono i dettagli della variante d'esame.
