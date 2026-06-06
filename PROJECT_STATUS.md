# Project Status

## Current Phase

All known exam sources ingested. Validation with official professor PDFs is in progress; the primary LCS family, Floyd-Warshall family, MST/Prim, LICS and knapsack-color variants now have official-confirmed RAG coverage.

## Completed

- [x] Folder structure, templates and initial indexes created.
- [x] All known exam PDFs cataloged through ingestion reports.
- [x] `SRC-EXTRA-001` integrated with transcription, methods, examples and warnings.
- [x] `SRC-NOTE-001` integrated with interpretive transcription, methods, examples and warnings.
- [x] Parte I and Parte II pattern notes created.
- [x] Final consolidation dashboard, AI guide, coverage matrix and validation workflow in progress.
- [x] `10_rag/` created with entrypoint, retrieval index, trust policy, prompts, exam style, method cards and templates.
- [x] `01_sources/source_inventory.md` updated with all local PDFs, SHA256 hashes and page counts.
- [x] `SRC-LECTURE-001` applied: official PDF `lcs_atmost_red-13ott25.pdf`.
- [x] `SRC-OFFICIAL-EX-013` applied: official PDF `lcs-6ott25.pdf` for LCS base.
- [x] `SRC-OFFICIAL-EX-014`, `SRC-OFFICIAL-EX-015`, `SRC-OFFICIAL-EX-016` applied: official LCS variants cumulative plan.
- [x] `SRC-OFFICIAL-EX-012`, `SRC-OFFICIAL-EX-017`, `SRC-OFFICIAL-EX-018`, `SRC-OFFICIAL-EX-019` applied: final exercises block MST/Prim, LICS, knapsack.
- [x] `SRC-OFFICIAL-EX-003` ... `SRC-OFFICIAL-EX-011` applied: unified Floyd-Warshall official block.
- [x] `09_ingestion_reports/official_lectures_workplan.md` created for the remaining official PDFs.

## In Progress

- [ ] Manual verification of handwritten-source warnings.
- [ ] Completion of full solved examples for remaining Parte I appelli.
- [ ] Final wikilink cleanup and readiness validation.
- [ ] RAG smoke test on representative exam prompts.
- [ ] Plan and apply remaining official PDFs by priority queue.

## PDF Processing Status

| Source ID | File | Tipo | Stato RAG | Ultima azione | Prossimo step |
|---|---|---|---|---|---|
| SRC-EXAM-001 | `parteI-13gen25.pdf` | appello | transcribed, cataloged, method-linked, warning | Parte I catalogata; pattern LCS colori coperto da card | Completare esempio by-exam solo se serve |
| SRC-EXAM-002 | `parteII-13gen25.pdf` | appello | transcribed, cataloged, method-linked, solved | Parte II catalogata | Nessuna azione bloccante |
| SRC-EXAM-003 | `parteI-11feb25-completo.pdf` | appello | transcribed, cataloged, method-linked | Parte I catalogata | Completare esempi prioritari |
| SRC-EXAM-004 | `parteI-11feb25-recupero.pdf` | appello | transcribed, cataloged, method-linked | Parte I catalogata | Verificare deduplicazione se riusata |
| SRC-EXAM-005 | `parteII-11feb25-completo-recupero.pdf` | appello | transcribed, cataloged, method-linked, solved | Parte II catalogata | Nessuna azione bloccante |
| SRC-EXAM-006 | `parteI-09giu25.pdf` | appello | transcribed, cataloged, method-linked | Parte I catalogata | Completare esempi by-exam |
| SRC-EXAM-007 | `parteII-09giu25.pdf` | appello | transcribed, cataloged, method-linked, solved | Parte II catalogata | Nessuna azione bloccante |
| SRC-EXAM-008 | `parteI-03lug25.pdf` | appello | transcribed, cataloged, method-linked | Parte I catalogata | Completare esempi by-exam |
| SRC-EXAM-009 | `parteII-03lug25.pdf` | appello | transcribed, cataloged, method-linked, solved | Parte II catalogata | Nessuna azione bloccante |
| SRC-EXAM-010 | `parteI-17set25.pdf` | appello | transcribed, cataloged, method-linked, warning | Varianti LCS catalogate | Verificare varianti LCS ambigue |
| SRC-EXAM-011 | `parteII-17set25.pdf` | appello | transcribed, cataloged, method-linked, solved | Greedy/matroidi coperti | Nessuna azione bloccante |
| SRC-EXAM-012 | `parte-I-10nov25-A.pdf` | appello | transcribed, cataloged, method-linked | Parte I catalogata | Completare esempi by-exam |
| SRC-EXAM-013 | `parteII-10nov25.pdf` | appello | transcribed, cataloged, method-linked, solved | Kruskal, riduzioni, Warshall, matroidi catalogati | Nessuna azione bloccante |
| SRC-EXAM-014 | `esame_apa_12_01_2026.pdf` | appello | transcribed, cataloged, method-linked, warning | Appello catalogato; zaino e matroidi collegati | Verificare warning degli esercizi catalogati |
| SRC-NOTE-001 | `Analisi E Progettazione Di Algoritmi.pdf` | appunti | transcribed, method-linked, solved, warning | Trascrizione e metodi integrati | Verifica manuale formule ambigue |
| SRC-EXTRA-001 | `esercizi APA.pdf` | extra | transcribed, method-linked, solved, warning | Trascrizione e integrazione Parte I | Verifica manuale punti ambigui |
| SRC-LECTURE-001 | `lcs_atmost_red-13ott25.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | Formulazione ufficiale LCS con al massimo 3 rossi applicata a RAG/metodi/esempio | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-013 | `lcs-6ott25.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | Formulazione ufficiale LCS base applicata a RAG/metodi/esempio | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-014 | `lcs-atleast-2-consecutive-red.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | Variante LCS con due rossi consecutivi applicata a RAG/metodi/schema | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-015 | `lcs-even-odd.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | Variante LCS dispari/pari per posizione applicata a RAG/metodi/schema | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-016 | `lcs-three-sequences-20ott25.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | Variante LCS a tre sequenze applicata a RAG/metodi/schema | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-012 | `knapsack-atmost-3-red.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | Zaino con al massimo 3 rossi applicato a RAG/metodi/schema | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-017 | `mst-prim.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | Prim applicato a RAG/metodi/schema | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-018 | `mst.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | MST base e arco sicuro applicati a RAG/metodi/teoria | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-019 | `varianti-lics-20ott25.pdf` | PDF ufficiale | raw, cataloged, method-linked, solved, verified | LICS e varianti applicate a RAG/metodi/schema | Nessuna azione bloccante |
| SRC-OFFICIAL-EX-003..011 | `floyd-warshall-*`, `fw-*` | PDF ufficiali | raw, cataloged, method-linked, solved, verified | Floyd-Warshall base e varianti colori/conteggi/esistenza applicate a RAG/metodi/schema | Nessuna azione bloccante |

## Stato Fonti Manoscritte

### SRC-EXTRA-001

- Report: `09_ingestion_reports/ingestion_report_extra_esercizi_APA_SRC_EXTRA_001.md`
- Trascrizione: `02_transcriptions/extra/esercizi_APA_SRC_EXTRA_001.md`
- Stato: applicato con warning.

### SRC-NOTE-001

- Report: `09_ingestion_reports/ingestion_report_note_analisi_e_progettazione_algoritmi.md`
- Trascrizione: `02_transcriptions/notes/note_analisi_e_progettazione_algoritmi.md`
- Stato: applicato con warning.

## Next Actions

1. Usare `AI Chat during Exam/Final Prompt.md` come prompt da telefono.
2. Per LCS base usare `SRC-OFFICIAL-EX-013`; per LCS con "al massimo k rossi", usare `SRC-LECTURE-001`; per LCS a tre sequenze, due rossi consecutivi e dispari/pari usare `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`.
3. Per MST/Prim usare `10_rag/RAG_METHOD_CARDS/mst_prim.md`; per LICS usare `dp_lics_varianti.md`; per zaino con colori usare `dp_knapsack_vincoli_colore.md`.
4. Per Floyd-Warshall base e varianti usare `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`.
5. Proseguire con `09_ingestion_reports/official_lectures_workplan.md`.
6. Eseguire `python scripts/check_wikilinks.py` dopo modifiche strutturali.
