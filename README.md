# APA Knowledge Base

Knowledge base Obsidian per preparare l'esame di Analisi e Progettazione di Algoritmi.

## Obiettivo

Studiare l'esame tramite appelli passati, appunti manoscritti di una studentessa che ha gia passato l'esame e catalogazione dei pattern ricorrenti.

La base di conoscenza serve a riconoscere rapidamente:

- tipologie di esercizio;
- procedure risolutive;
- teoria collegata;
- variazioni tra appelli;
- errori comuni.

## Struttura

- `00_meta/`: convenzioni, workflow e strategia di studio.
- `01_sources/`: fonti originali, da non modificare.
- `02_transcriptions/`: trascrizioni e interpretazioni iniziali.
- `03_exercise_catalog/`: catalogo degli esercizi.
- `04_methods/`: metodi operativi.
- `05_theory/`: teoria richiesta.
- `06_exam_patterns/`: pattern ricorrenti negli appelli.
- `07_solved_examples/`: esempi svolti.
- `08_review/`: materiale di ripasso.
- `09_ingestion_reports/`: report intermedi generati dall'analisi dei PDF e usati da Codex per aggiornare la knowledge base.
- `templates/`: template Markdown.

## Workflow PDF

1. I PDF originali vengono salvati in `01_sources/`.
2. Ogni PDF riceve un Source ID in `01_sources/source_inventory.md`.
3. Un'AI analizza il PDF e produce un ingestion report.
4. Codex applica il report alla knowledge base.
5. Gli indici e lo stato progetto vengono aggiornati.

## Regola guida

> [!Summary]
> Appello -> Esercizio -> Pattern -> Metodo -> Teoria -> Esempio svolto -> Errori comuni.
