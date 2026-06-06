# Template DP

1. Sottoproblema: `DP[...] = ...` sul prefisso/stato indicato dalla traccia.
2. Base: inizializzare istanze vuote; stati impossibili a `-infty`, `+infty` o `false`.
3. Ricorrenza: separare sempre caso "non prendo/non uso" e caso "prendo/uso".
4. Ordine: indicare l'ordine che rispetta le dipendenze.
5. Risposta: cella finale o massimo/minimo su stati accettanti.
6. Ricostruzione: seguire a ritroso le scelte.
7. Complessita: prodotto delle dimensioni della tabella per costo transizione.
8. Correttezza: induzione sull'ordine di calcolo.
