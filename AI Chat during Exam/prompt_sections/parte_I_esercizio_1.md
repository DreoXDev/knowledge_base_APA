# Parte I - Esercizio 1

Questo esercizio e quasi sempre un esercizio di programmazione dinamica su sequenze.

Pattern tipici:

- LCS classica;
- LCS con vincolo su colori;
- LCS con vincolo di ingombro/somma/peso;
- LCS con esattamente/al massimo K simboli di un certo tipo;
- interleaving;
- sottosequenze con proprieta aggiuntive;
- zaino o varianti se la traccia parla di oggetti, pesi, valori, budget.

Fonti RAG da usare:

- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md`
- `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`
- `10_rag/RAG_METHOD_CARDS/zaino_01_varianti.md`
- `04_methods/`
- `07_solved_examples/`

La risposta deve seguire i punti della traccia.

Formato standard:

1. Coefficienti: risposta molto breve. Solo definizione dei prefissi, indici e coefficiente. Usare bullet point. Non spiegare perche.
2. Caso base: solo formule. Nessuna frase lunga.
3. Passo ricorsivo: solo equazioni necessarie. Usare bullet list per i casi. Non aggiungere dimostrazione.
4. Coefficiente soluzione: una sola riga, per esempio `C[m,n,W]`, oppure il coefficiente richiesto dal problema.
5. Algoritmo bottom-up: scrivere pseudocodice compatto. Puo essere piu lungo perche di solito e richiesto "sul protocollo".
6. Algoritmo ricorsivo di ricostruzione/stampa: scrivere pseudocodice compatto ma completo. Deve stampare la soluzione nell'ordine corretto.

Regole di sintassi per pseudocodice:

- usare `for i = ... to ...`;
- usare `if ... then`;
- usare `else`;
- usare indentazione semplice;
- usare `return`;
- usare `print`;
- evitare codice Python/Java/C;
- evitare commenti lunghi.

Regola importante:

Se il vincolo e "al massimo" o "minore o uguale", NON usare stati impossibili con `-infinito` come default. Usare una formulazione con coefficiente che rappresenta direttamente il vincolo `<= k`.

Se invece il vincolo e "esattamente K", allora possono servire valori impossibili come `-infinito`.
