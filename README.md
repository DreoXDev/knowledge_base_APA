# Knowledge Base APA

## Scopo

Questa repository contiene una Knowledge Base per preparare l'esame di Analisi e Progettazione di Algoritmi (APA) e usarla come base RAG durante studio, simulazioni ed esercizi.

## Stato attuale

La repo contiene:

- appelli/esami passati;
- appunti e trascrizioni;
- PDF ufficiali di esercizi;
- teoria prioritaria;
- metodi operativi per esercizi;
- solved examples e schemi d'esame;
- method card RAG;
- prompt finale per AI.

## Struttura

| Cartella | Contenuto |
|---|---|
| `01_sources/` | PDF originali, appelli, appunti raw e inventario fonti |
| `02_transcriptions/` | Trascrizioni lavorate di esami, appunti e materiali extra |
| `03_exercise_catalog/` | Catalogo esercizi per appello, topic e difficolta |
| `04_methods/` | Metodi operativi per risolvere esercizi |
| `05_theory/` | Teoria compatta per domande d'esame |
| `06_exam_patterns/` | Pattern ricorrenti e varianti osservate negli appelli |
| `07_solved_examples/` | Esempi svolti e schemi copiabili |
| `09_ingestion_reports/` | Report di ingestion e audit |
| `10_rag/` | Entrypoint RAG, retrieval index, pattern map, method card e policy |
| `AI Chat during Exam/` | Prompt finale e sezioni operative per assistente AI |

## Come usare la repo

1. Per esercizi: partire da `04_methods/` o `10_rag/RAG_RETRIEVAL_INDEX.md`.
2. Per teoria: partire da `05_theory/`.
3. Per pattern d'esame: usare `06_exam_patterns/`.
4. Per esempi/schemi: usare `07_solved_examples/`.
5. Per AI/RAG: usare `10_rag/` e `AI Chat during Exam/Final Prompt.md`.

## Entrypoint consigliati

- `10_rag/RAG_RETRIEVAL_INDEX.md`: associa query d'esame ai file piu utili.
- `10_rag/RAG_PATTERN_MAP.md`: riconosce il pattern e sceglie il metodo.
- `10_rag/RAG_ENTRYPOINT.md`: ordine di consultazione per un modello AI.
- `AI Chat during Exam/Final Prompt.md`: prompt generale per risposte da esame.
- `09_ingestion_reports/final_repo_audit.md`: stato finale della pulizia.

## Fonti e affidabilita

In caso di incongruenze, usare questo ordine:

1. PDF ufficiali del professore;
2. appelli ufficiali;
3. appunti della compagna se coerenti;
4. KB/RAG consolidata;
5. inferenze del modello.

## Warning residui

- OCR e appunti manoscritti non sono sempre perfetti.
- Alcuni file raw non sono stati analizzati in profondita.
- Il RAG punta ai file consolidati, non necessariamente a ogni PDF sorgente.
- I file generali o draft vanno usati come supporto, non come fonte primaria se esiste una method card specifica.

## Regola guida

Traccia d'esame -> `RAG_RETRIEVAL_INDEX.md` -> method card -> metodo/esempio collegato -> risposta compatta da esame.
