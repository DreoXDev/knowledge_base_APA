# Varianti DP su grafi con stato

Fonti: [[dp_grafi_floyd_warshall_stato_esteso]], [[floyd_warshall]], [[mapping_appelli_to_SRC_NOTE_001]].

| Variante | Stato | Caso base | Passo | Operatore | Esempi |
|---|---|---|---|---|---|
| Chiusura transitiva | $D^k[i,j]$ | arco diretto / identita | passa da $k$ | OR/AND | [[metodo_equazioni_ricorrenza_chiusura_transitiva]] |
| Cammini con colori | $D^k[i,j,r,b]$ | arco diretto con colore | passa da $k$ e somma conteggi | OR | [[metodo_dp_cammini_colori_conteggi]] |
| Cammini con parita | $D^k[i,j,p]$ | arco diretto | flip/somma parita | OR/min | [[metodo_dp_cammini_colori_parita]] |
| Cammini minimi con vincoli | $D^k[i,j,\dots]$ | peso arco | min tra non passa/passa | min-plus | [[metodo_cammini_minimi_vincoli_colori_parita]] |
| No due colori consecutivi | $D^k[i,j,a,b]$ | primo/ultimo colore | compatibilita colori al merge | OR/AND | [[metodo_dp_cammini_colori_precedenze]] |
| Precedenze di sequenza | stato su posizione pattern | base su archi | avanza automa | OR | [[metodo_dp_cammini_colori_precedenze]] |

## Template universale Floyd-Warshall esteso

$$
D^k[i,j,s]=D^{k-1}[i,j,s]\ \oplus\ 
\bigoplus_{s_1\otimes s_2=s}
D^{k-1}[i,k,s_1]\otimes D^{k-1}[k,j,s_2].
$$

Per problemi booleani, $\oplus$ e OR e $\otimes$ e AND. Per problemi di minimo, $\oplus$ e min e $\otimes$ combina costi e stati.

## Errori comuni

- $k$ indica i vertici intermedi ammessi, non la lunghezza del cammino.
- Nel merge bisogna aggiornare anche lo stato extra.
- Con vincoli su colori consecutivi servono colore iniziale e finale del cammino parziale.

