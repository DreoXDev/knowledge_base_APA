---
type: method
status: complete_with_warnings
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, lcs, lics]
---

# DP - LCS crescente / LICS

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 8, 13-16.

## Trucco metodologico

Il sottoproblema non e la LCS classica su prefissi. Si usa un problema ausiliario in cui la soluzione termina con il match $x_i=y_j$.

> [!Important]
> Per LICS la soluzione del problema principale non e necessariamente $C[m,n]$, ma spesso $\max C[i,j]$.

## Coefficiente

$$
C[i,j]=\text{lunghezza di una LICS tra }X_i,Y_j\text{ che termina in }x_i=y_j.
$$

## Caso base

$$
C[i,j]=0 \quad \text{se }x_i\ne y_j.
$$

## Passo ricorsivo

Se $x_i=y_j$:

$$
C[i,j]=1+\max\{C[h,k]\mid h<i,\ k<j,\ x_h<x_i\}.
$$

## Soluzione

$$
\max_{1\le i\le m,\ 1\le j\le n}C[i,j].
$$

## Varianti

- Decrescente: sostituire $x_h<x_i$ con $x_h>x_i$.
- Con vincoli colore/parita: aggiungere il controllo sul predecessore.

> [!Warning]
> Le varianti con valori, colori o alternanze nelle pagine 13-16 sono parzialmente leggibili: usare il pattern, verificare le condizioni puntuali.

