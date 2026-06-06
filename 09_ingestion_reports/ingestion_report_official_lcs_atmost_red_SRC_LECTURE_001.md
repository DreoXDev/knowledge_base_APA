---
type: ingestion_report
source_ids:
  - SRC-LECTURE-001
status: applied
created: 2026-06-06
tags:
  - apa
  - ingestion-report
  - fonte-ufficiale
  - lcs
---

# Ingestion report - SRC-LECTURE-001 - LCS con al massimo 3 rossi

## Fonte

- File: `01_sources/extra_materials/lcs_atmost_red-13ott25.pdf`
- Titolo: Longest Common Subsequence (LCS) con al massimo 3 elementi rossi
- Tipo: PDF ufficiale professore
- Corso: Analisi e Progetto di Algoritmi, Laurea Triennale in Informatica, AA 2025/2026
- Docente: Raffaella Rizzi
- Pagine: 42
- Rilevanza: alta

## Concetti ufficiali estratti

- sottoproblema `LCS(X_i,Y_j,r)`;
- coefficiente `c_{i,j,r}`;
- casi base con prefisso vuoto;
- ricorrenza per caratteri diversi;
- ricorrenza per carattere uguale non rosso;
- ricorrenza per carattere uguale rosso con `r=0`;
- ricorrenza per carattere uguale rosso con `r>0`;
- algoritmo bottom-up;
- ricostruzione/stampa della soluzione.

## Regola ufficiale principale

Per LCS con al massimo `k` rossi:

`C[i][j][r]` = lunghezza di una LCS tra `X_i` e `Y_j` con al massimo `r` elementi rossi.

Il valore finale e `C[m][n][k]`.

Nel PDF, `k=3`, quindi il valore finale e `C[m][n][3]`.

## File aggiornati

- `01_sources/source_inventory.md`
- `09_ingestion_reports/official_lectures_workplan.md`
- `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`
- `10_rag/RAG_TRUST_POLICY.md`
- `10_rag/RAG_EXAM_ANSWER_STYLE.md`
- `04_methods/dp_lcs_vincoli_colore.md`
- `04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md`
- `04_methods/metodo_ricostruzione_soluzione_dp.md`
- `05_theory/lcs.md`
- `06_exam_patterns/dp_su_sequenze_con_vincoli_di_conteggio.md`
- `07_solved_examples/dp/lcs_al_massimo_3_rossi_SRC_LECTURE_001.md`
- `AI Chat during Exam/Final Prompt.md`
- `AI Chat during Exam/prompt_sections/parte_I_esercizio_1.md`

## Discrepanze corrette

- La RAG distingueva la variante "esattamente r rossi" e derivava "al massimo k" con `max_{0 <= r <= k}`.
- La fonte ufficiale usa invece, come formulazione primaria, uno stato cumulativo "al massimo r rossi".
- La card RAG ora tiene entrambe le formulazioni, ma usa quella ufficiale quando la traccia dice "al massimo".
- Gli esempi "esattamente" sono stati marcati per non essere confusi con la variante "al massimo".

## Definition of Done

- [x] Fonte registrata in `source_inventory.md`.
- [x] Workplan ufficiale creata.
- [x] Method card RAG aggiornata.
- [x] Metodi sorgente aggiornati.
- [x] Esempio ufficiale minimo creato.
- [x] Prompt da esame aggiornato.
