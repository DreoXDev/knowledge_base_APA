# LICS - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagina 8.

## Istanza

Due sequenze numeriche $X,Y$.

## Soluzione richiesta

Lunghezza di una LCS crescente.

## Definizione coefficienti

$$
C[i,j]=\text{lunghezza di una LICS che termina in }x_i=y_j.
$$

## Passo ricorsivo

$$
C[i,j]=1+\max\{C[h,k]\mid h<i,\ k<j,\ x_h<x_i\}
$$

se $x_i=y_j$, altrimenti $0$.

## Valore della soluzione

$$
\max_{i,j}C[i,j].
$$

## Collegamenti

- [[dp_lcs_crescente_lics]]
- [[lics_SRC_EXTRA_001]]

