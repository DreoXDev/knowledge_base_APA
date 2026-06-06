# Project Status

## Current Phase

All known sources ingested. RAG exam layer created in `10_rag/`; final validation and manual warning checks remain.

## Completed

- [x] Folder structure, templates and initial indexes created.
- [x] All known exam PDFs cataloged through ingestion reports.
- [x] `SRC-EXTRA-001` integrated with transcription, methods, examples and warnings.
- [x] `SRC-NOTE-001` integrated with interpretive transcription, methods, examples and warnings.
- [x] Parte I and Parte II pattern notes created.
- [x] Final consolidation dashboard, AI guide, coverage matrix and validation workflow in progress.
- [x] `10_rag/` created with entrypoint, retrieval index, trust policy, prompts, exam style, method cards and templates.

## In Progress

- [ ] Manual verification of handwritten-source warnings.
- [ ] Completion of full solved examples for remaining Parte I appelli.
- [ ] Final wikilink cleanup and readiness validation.
- [ ] RAG smoke test on representative exam prompts.

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

1. Usare `10_rag/RAG_ENTRYPOINT.md` come punto di ingresso per RAG da esame.
2. Verificare manualmente i warning delle fonti manoscritte.
3. Completare esempi svolti Parte I ancora parziali.
4. Eseguire `python scripts/check_wikilinks.py` dopo modifiche strutturali.
