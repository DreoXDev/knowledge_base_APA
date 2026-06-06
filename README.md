# APA Knowledge Base

Knowledge base Obsidian per preparare l'esame di Analisi e Progettazione di Algoritmi.

## Punto di ingresso

La KB e pronta per due usi distinti:

- `10_rag/RAG_ENTRYPOINT.md` per uso RAG durante l'esame.
- [[STUDY_DASHBOARD]] per il percorso di ripasso.
- [[AI_USAGE_GUIDE]] per usare la repo come contesto AI senza inventare formule o soluzioni.

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
- `10_rag/`: layer compatto per retrieval, prompt, policy e method card da esame.
- `templates/`: template Markdown.

## Uso RAG da esame

Per usare la repo come contesto AI durante l'esame, partire da:

- `10_rag/RAG_ENTRYPOINT.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_SYSTEM_PROMPT.md`
- `10_rag/RAG_MOBILE_PROMPT.md`

La cartella `10_rag/` contiene materiale compatto e controllato per retrieval. Le cartelle precedenti restano la base estesa, ma non sono il punto di ingresso primario per risposte da copiare in esame.

## Workflow PDF

1. I PDF originali vengono salvati in `01_sources/`.
2. Ogni PDF riceve un Source ID in `01_sources/source_inventory.md`.
3. Un'AI analizza il PDF e produce un ingestion report.
4. Codex applica il report alla knowledge base.
5. Gli indici e lo stato progetto vengono aggiornati.

## Stato attuale

Tutte le fonti note sono state ingestite o applicate. Le fonti manoscritte `SRC-NOTE-001` e `SRC-EXTRA-001` contengono warning espliciti dove la lettura e ambigua. La repo non contiene soluzioni ufficiali: contiene metodi, esempi e interpretazioni derivate da appelli e appunti.

## Regola guida

> [!Summary]
> RAG: Traccia -> Retrieval index -> Method card -> Esempio svolto -> Risposta breve.
> Studio: Appello -> Esercizio -> Pattern -> Metodo -> Teoria -> Esempio svolto -> Errori comuni.
