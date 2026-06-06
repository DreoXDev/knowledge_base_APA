# AI Chat during Exam

Questa cartella contiene il prompt finale da copiare in una nuova chat ChatGPT dall'app prima dell'esame.

## File principale

- `Final Prompt.md`: prompt unico finale da incollare nella chat.

## Scopo

La chat deve:

- ricevere fotografie degli esercizi;
- riconoscere il numero/posizione dell'esercizio;
- recuperare il metodo corretto dalla RAG;
- rispondere con testo copiabile sul foglio;
- evitare spiegazioni inutili;
- rispettare lo spazio disponibile nella prova.

## Uso

1. Aprire `Final Prompt.md`.
2. Copiare tutto il contenuto.
3. Incollarlo in una nuova chat ChatGPT.
4. Durante l'esame inviare una foto alla volta.
5. Copiare sul foglio solo la risposta generata.

## Sezioni modulari

Le sezioni in `prompt_sections/` servono per aggiornare singole parti del prompt senza riscrivere tutto il file finale.
