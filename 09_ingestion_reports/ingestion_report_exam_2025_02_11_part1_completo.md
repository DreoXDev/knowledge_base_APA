---
type: ingestion_report
source_ids:
  - SRC-EXAM-003
status: ready_for_codex
created: 2026-05-17
tags:
  - apa
  - ingestion-report
---

# Ingestion Report - Appello APA 2025-02-11 Parte I scritto completo

> [!Info]
> Source ID: `SRC-EXAM-003`
>
> File sorgente: `01_sources/exams_raw/parteI-11feb25-completo.pdf`
>
> Tipo fonte: appello
>
> Stato: pronto per Codex

## 1. Sintesi del contenuto

Questo appello scritto completo di Parte I del corso "Analisi e Progettazione di Algoritmi" del 11 febbraio 2025 contiene due importanti esercizi di programmazione dinamica che esplorano estensioni avanzate dello stato ed eliminazione di vincoli locali.

*   **Esercizio 1**: LCS comune a tre sequenze con vincolo di al massimo due simboli rossi.
*   **Esercizio 2**: DP su grafo colorato per verificare l'esistenza di un cammino senza due archi consecutivi neri ($NN$) e senza due archi consecutivi blu ($BB$).

## 2. Pagine / sezioni analizzate

| Pagina / sezione | Contenuto | Affidabilita interpretazione |
|---|---|---|
| Esercizio 1 | LCS a tre sequenze con colore e budget | alta |
| Esercizio 2 | DP booleana su grafi con transizioni locali | alta |

## 3. Argomenti individuati

- LCS tridimensionale
- Vincoli di colore e budget massimo
- Programmazione dinamica su grafi colorati
- Floyd-Warshall esteso con consecutività
- Ricostruzione di soluzioni ottime

## 4. Esercizi da creare

| File da creare | Argomento | Fonte | Stato iniziale | Note |
|---|---|---|---|---|
| `03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e01.md` | LCS a tre sequenze con budget rossi | `SRC-EXAM-003` | cataloged | Richiede stato 4D (3 prefissi sequenze + budget rossi) |
| `03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e02.md` | DP su grafi con consecutività vietata | `SRC-EXAM-003` | cataloged | Richiede salvataggio colore iniziale e finale |

## 5. Esercizi da aggiornare

Nessuno (gli indici generali verranno aggiornati separatamente).

## 6. Metodi da creare o aggiornare

| File | Azione | Motivo | Collegamenti |
|---|---|---|---|
| `04_methods/metodo_lcs_tre_sequenze_vincolo_colori.md` | creare | Nuovo pattern per LCS su 3 sequenze con budget | `[[exam_2025_02_11_p1_completo_e01]]` |
| `04_methods/metodo_dp_cammini_colori_precedenze.md` | aggiornare | Integrare la variante sui divieti consecutivi | `[[exam_2025_02_11_p1_completo_e02]]` |

## 7. Teoria da creare o aggiornare

| File | Azione | Motivo | Collegamenti |
|---|---|---|---|
| `05_theory/lcs.md` | aggiornare | Riferire la variante a 3 sequenze | `[[exam_2025_02_11_p1_completo_e01]]` |
| `05_theory/sottosequenze_comuni.md` | aggiornare | Inserire LCS a 3 sequenze | `[[exam_2025_02_11_p1_completo_e01]]` |
| `05_theory/vincoli_su_colori.md` | aggiornare | Inserire i nuovi vincoli combinati | `[[exam_2025_02_11_p1_completo_e01]]`, `[[exam_2025_02_11_p1_completo_e02]]` |
| `05_theory/grafi_colorati.md` | aggiornare | Collegare la variante di consecutività | `[[exam_2025_02_11_p1_completo_e02]]` |

## 8. Pattern d'esame individuati

| Pattern | Azione | File suggerito | Fonte |
|---|---|---|---|
| LCS tridimensionale con vincoli | creare | `04_methods/metodo_lcs_tre_sequenze_vincolo_colori.md` | `SRC-EXAM-003` |
| Floyd-Warshall con colore estremi | aggiornare | `06_exam_patterns/parte_i_dynamic_programming_patterns.md` | `SRC-EXAM-003` |

## 9. Esempi svolti da creare

Nessuno in questa fase di catalogazione iniziale.

## 10. Indici da aggiornare

Aggiornare:
- `03_exercise_catalog/index_by_exam.md`
- `03_exercise_catalog/index_by_topic.md`
- `03_exercise_catalog/index_by_difficulty.md`
- `06_exam_patterns/recurring_exercise_types.md`
- `06_exam_patterns/variations_by_appeal.md`
- `06_exam_patterns/high_yield_topics.md`

## 11. Dubbi / parti da verificare

> [!Warning]
> Nessun dubbio bloccante. Entrambe le soluzioni raccomandate sono stabili e matematicamente rigorose.

## 12. Istruzioni operative per Codex

1. Creare la trascrizione pulita LaTeX in `02_transcriptions/exams/exam_2025_02_11_part1_completo.md`.
2. Catalogare l'Esercizio 1 in `03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e01.md`.
3. Catalogare l'Esercizio 2 in `03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e02.md`.
4. Creare la nota metodologica `04_methods/metodo_lcs_tre_sequenze_vincolo_colori.md`.
5. Aggiornare tutti gli indici e i pattern per incorporare l'appello.

## 13. Definition of Done

- [x] Tutti i file richiesti sono stati creati o aggiornati.
- [x] Gli indici sono stati aggiornati.
- [x] I collegamenti Obsidian sono coerenti.
- [x] Le parti incerte sono marcate con `[!Warning]`.
- [x] `PROJECT_STATUS.md` e stato aggiornato.
- [x] `01_sources/source_inventory.md` e stato aggiornato con il link al report.
