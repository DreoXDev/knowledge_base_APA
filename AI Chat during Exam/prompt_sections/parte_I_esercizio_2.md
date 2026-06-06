# Parte I - Esercizio 2

Questo esercizio e quasi sempre programmazione dinamica su grafi.

Pattern tipici:

- chiusura transitiva;
- chiusura riflessiva-transitiva;
- Floyd-Warshall booleano;
- cammini con vincoli su colori;
- cammini con esattamente/al massimo un certo numero di archi di un tipo;
- cammini con stato esteso.

Fonti RAG da usare:

- `10_rag/RAG_METHOD_CARDS/dp_grafi_stato_esteso.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `04_methods/`
- `07_solved_examples/`

La risposta deve seguire i punti della traccia.

Formato standard:

1. Coefficienti: definire il coefficiente booleano o numerico. Specificare chiaramente vertici di partenza/arrivo, eventuale indice `k` di Floyd-Warshall, eventuali contatori di archi/colori, eventuale insieme di vertici intermedi ammessi.
2. Caso base: scrivere solo le condizioni iniziali. Se e chiusura transitiva/riflessiva-transitiva, distinguere arco diretto, cammino vuoto se riflessiva, assenza di arco.
3. Passo ricorsivo: scrivere la ricorrenza in forma compatta. Per Floyd-Warshall usare `coefficiente senza usare k` OR `passaggio tramite k`. Per stati con colori/contatori, scrivere i casi in bullet list.
4. Soluzione del problema: una o poche righe. Indicare il coefficiente finale per ogni coppia o per la coppia richiesta.

Non aggiungere algoritmi se la traccia chiede solo coefficienti e ricorrenze.
