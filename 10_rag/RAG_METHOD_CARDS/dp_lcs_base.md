---
type: rag-method-card
topic: dp-lcs-base
status: official_confirmed
source_methods:
  - 04_methods/dp_lcs_base.md
  - 04_methods/metodo_lcs_base.md
source_examples:
  - 07_solved_examples/dp/lcs_base_6ott25.md
  - 07_solved_examples/dp/lcs_base_SRC_NOTE_001.md
source_patterns:
  - 06_exam_patterns/parte_i_dynamic_programming_patterns.md
exam_use: true
---

# Method Card - DP LCS base

## Quando usarla

Usa questa card quando la traccia chiede la Longest Common Subsequence tra due sequenze `X` e `Y`, oppure una variante LCS che parte dal caso base.

Parole chiave: LCS, Longest Common Subsequence, sottosequenza comune piu lunga, prefissi, ricostruzione LCS, matrice C.

## Sottoproblema

`LCS(X_i, Y_j)`: LCS tra i prefissi `X_i = <x_1,...,x_i>` e `Y_j = <y_1,...,y_j>`.

Indici:

- `i in {0,...,m}`
- `j in {0,...,n}`

Numero di sottoproblemi: `(m+1)(n+1)`.

## Coefficiente

`c_{i,j} = |LCS(X_i, Y_j)|`.

Valore ottimo: `c_{m,n}`.

## Casi base

Se `i = 0` oppure `j = 0`:

`LCS(X_i,Y_j)=<>` e `c_{i,j}=0`.

## Ricorrenza

Se `i>0` e `j>0`:

- se `x_i = y_j`, allora `c_{i,j}=c_{i-1,j-1}+1`;
- se `x_i != y_j`, allora `c_{i,j}=max(c_{i-1,j}, c_{i,j-1})`.

## Bottom-up

Inizializza prima riga e prima colonna a `0`.

Poi calcola `C[i,j]` per `i=1..m`, `j=1..n` usando la ricorrenza.

Complessita: `O(mn)` tempo, `O(mn)` spazio se si conserva tutta la matrice per la ricostruzione.

## Ricostruzione

`Print_LCS(C,X,Y,i,j)`:

- se `i=0` oppure `j=0`, termina;
- se `x_i = y_j`, chiama `Print_LCS(C,X,Y,i-1,j-1)` e poi stampa `x_i`;
- se `x_i != y_j` e `C[i,j]=C[i-1,j]`, ricostruisci da `(i-1,j)`;
- altrimenti ricostruisci da `(i,j-1)`.

In caso di pareggio sono possibili piu LCS corrette.

## Errori da evitare

- Non confondere sottosequenza con sottostringa.
- Non definire `c_{i,j}` come la sequenza: e la lunghezza.
- Non stampare `x_i` prima della chiamata ricorsiva.
- Non assumere che la LCS sia unica.
