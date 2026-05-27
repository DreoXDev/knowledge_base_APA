# LCS base - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagine 1-3.

## Istanza

Due sequenze $X,Y$.

## Soluzione richiesta

Lunghezza di una LCS.

## Sottoproblema

Prefissi $X_i,Y_j$.

## Definizione coefficienti

$$
C[i,j]=\text{lunghezza di una LCS tra }X_i,Y_j.
$$

## Caso base

$$
C[i,0]=C[0,j]=0.
$$

## Passo ricorsivo

Vedi [[dp_lcs_base]].

## Valore della soluzione

$$
C[m,n].
$$

## Algoritmo / pseudocodice

Bottom-up con due cicli annidati su $i$ e $j$.

## Complessita

$O(mn)$ tempo e spazio.

## Collegamenti

- [[dp_lcs_base]]

