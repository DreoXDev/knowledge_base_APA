# Parte I - Esercizio 1

Questo esercizio e quasi sempre un esercizio di programmazione dinamica su sequenze.

Quando riconosci una traccia LCS, usa prima lo schema ufficiale base: sottoproblema sui prefissi `X_i,Y_j`, coefficiente `c_{i,j}`, casi base con prefisso vuoto, ricorrenza match/non-match, bottom-up e ricostruzione da `C`. Per varianti con vincoli aggiungi dimensioni di stato solo dopo aver fissato lo schema base.

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
- `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`
- `10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md`
- `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`
- `10_rag/RAG_METHOD_CARDS/dp_lics_varianti.md`
- `10_rag/RAG_METHOD_CARDS/dp_knapsack_vincoli_colore.md`
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

Nelle DP con conteggi, chiarisci sempre se il contatore rappresenta numero esatto usato, massimo ammesso/residuo, minimo richiesto oppure parita/stato booleano.

Per LCS con al massimo `k` rossi, la formulazione ufficiale del professore usa `r` come massimo ammesso e restituisce `C[m][n][k]`.

Per esercizi DP, rispondi sempre in ordine: sottoproblema, coefficiente, casi base, ricorrenza, bottom-up, ricostruzione, complessita.

Per LCS e varianti: non saltare mai definizione del coefficiente e casi base. Per ricostruzione, specificare che in caso di pareggio sono accettabili piu soluzioni.

Regole ufficiali per varianti LCS:

- LCS di tre sequenze: usare DP tridimensionale `c_{i,j,h}`, non due LCS successive; valore `c_{m,n,l}`.
- Due rossi consecutivi: usare stati vincolati a terminare nel match corrente (`c_ij1`, `c_ij0`) e valore ottimo come massimo globale.
- Dispari in posizioni dispari e pari in posizioni pari: usare la lunghezza precedente per determinare la posizione; non confondere parita del valore con parita dell'indice.
- LICS: usare stato vincolato a terminare con `x_i = y_j`, max sui predecessori compatibili e valore finale come massimo globale.
- Knapsack colori: per "al massimo 3 rossi" usare `r` come budget massimo e risposta `d_{n,C,3}`.
