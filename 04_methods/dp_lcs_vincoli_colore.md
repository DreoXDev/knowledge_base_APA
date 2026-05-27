---
type: method
status: complete_with_warnings
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, lcs, colori]
---

# DP - LCS con vincoli di colore

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 11-22. Collegato a SRC-EXTRA-001.

## Variante: al massimo K rossi

$$
C[i,j,k]=\text{lunghezza di una LCS tra }X_i,Y_j\text{ con al massimo }k\text{ rossi}.
$$

Caso base: $C[0,j,k]=C[i,0,k]=0$.

Se $x_i=y_j$ e $col(x_i)=rosso$:

$$
C[i,j,k]=
\begin{cases}
\max(C[i-1,j,k],C[i,j-1,k],C[i-1,j-1,k-1]+1) & k>0,\\
\max(C[i-1,j,k],C[i,j-1,k]) & k=0.
\end{cases}
$$

Se $x_i=y_j$ non rosso:

$$
C[i,j,k]=\max(C[i-1,j,k],C[i,j-1,k],C[i-1,j-1,k]+1).
$$

Se $x_i\ne y_j$:

$$
C[i,j,k]=\max(C[i-1,j,k],C[i,j-1,k]).
$$

## Variante: esattamente K rossi

Stesso stato, ma il caso base cambia:

$$
C[0,j,0]=C[i,0,0]=0,\qquad C[0,j,k]=C[i,0,k]=-\infty\text{ per }k>0.
$$

## Variante: tutte le LCS hanno numero pari di rossi

Calcolare prima la lunghezza ottima $L[i,j]$. Poi usare uno stato booleano:

$$
B[i,j,p]=true
$$

sse tutte le LCS ottime di $X_i,Y_j$ hanno parita $p$ di rossi, con $p=0$ pari e $p=1$ dispari.

> [!Warning]
> Le convenzioni di parita negli appunti e in SRC-EXTRA-001 vanno verificate manualmente prima di fissare una soluzione ufficiale.

## Variante: costruire/stampare una soluzione

Memorizzare un predecessore per ogni cella che realizza il massimo. Durante la stampa:

- se il predecessore e diagonale e il simbolo e stato preso, stampare/appendere $x_i$;
- scalare il contatore colore se il simbolo preso ha quel colore;
- altrimenti seguire il ramo sopra/sinistra.

## Caso base: quando usare 0, false, -infinito

| Variante | Stato aggiuntivo | Tipo coefficiente | Caso base | Soluzione |
|---|---|---|---|---|
| al massimo K rossi | $k$ residuo | lunghezza | $0$ | $C[m,n,K]$ |
| esattamente K rossi | $k$ residuo | lunghezza | $0$ se $k=0$, $-\infty$ se $k>0$ | $C[m,n,K]$ |
| parita rossi | $p\in\{0,1\}$ | booleano/lunghezza | dipende dalla consegna | $B[m,n,p]$ |

## Collegamenti

- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[lcs_al_massimo_k_rossi_SRC_NOTE_001]]
- [[lcs_esattamente_k_rossi_SRC_NOTE_001]]

