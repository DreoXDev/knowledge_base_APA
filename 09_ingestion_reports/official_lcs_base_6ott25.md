---
type: ingestion_report
source_ids:
  - SRC-OFFICIAL-EX-013
status: applied
created: 2026-06-06
tags:
  - apa
  - ingestion-report
  - fonte-ufficiale
  - lcs
---

# Ingestion report - SRC-OFFICIAL-EX-013 - LCS base

## Fonte

- File: `01_sources/extra_materials/lcs-6ott25.pdf`
- Titolo: Longest Common Subsequence (LCS)
- Tipo: PDF ufficiale professore
- Pagine: 125
- Rilevanza: alta

## Concetti ufficiali estratti

- definizioni di sequenza, prefisso, sottosequenza e sottosequenza comune;
- sottoproblema `LCS(X_i,Y_j)`;
- coefficiente `c_{i,j}=|LCS(X_i,Y_j)|`;
- valore ottimo `c_{m,n}`;
- casi base con prefisso vuoto;
- ricorrenza match/non-match;
- algoritmo bottom-up;
- ricostruzione `Print_LCS` dalla matrice `C`;
- nota sui pareggi e sulle LCS alternative.

## File aggiornati

- `10_rag/RAG_METHOD_CARDS/dp_lcs_base.md`
- `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`
- `10_rag/RAG_EXAM_ANSWER_STYLE.md`
- `04_methods/dp_lcs_base.md`
- `04_methods/metodo_lcs_base.md`
- `04_methods/metodo_ricostruzione_soluzione_dp.md`
- `05_theory/lcs.md`
- `07_solved_examples/dp/lcs_base_6ott25.md`
- `AI Chat during Exam/Final Prompt.md`
- `AI Chat during Exam/prompt_sections/parte_I_esercizio_1.md`

## Decisioni prese

- `SRC-OFFICIAL-EX-013` diventa la fonte primaria per LCS base.
- La variante `SRC-LECTURE-001` su LCS con al massimo 3 rossi viene trattata come estensione dello schema LCS base.
- La ricostruzione ufficiale usa la matrice dei valori `C`; la matrice dei predecessori e opzionale.

## Definition of Done

- [x] Method card RAG LCS base creata.
- [x] Metodi LCS base aggiornati.
- [x] Esempio ufficiale creato.
- [x] Prompt da esame aggiornato.
