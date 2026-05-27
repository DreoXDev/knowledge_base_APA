# Interleaving - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagine 4-5.

## Istanza

Sequenze $X,Y,W$ con $|W|=|X|+|Y|$.

## Soluzione richiesta

Stabilire se $W$ e interleaving di $X$ e $Y$.

## Sottoproblema

Prefissi $X_i,Y_j,W_{i+j}$.

## Definizione coefficienti

$$
S[i,j]=true
$$

sse $W_{i+j}$ e interleaving di $X_i,Y_j$.

## Caso base

$S[0,0]=true$, poi inizializzazione della prima riga e colonna.

## Passo ricorsivo

$$
S[i,j]=(x_i=w_{i+j}\land S[i-1,j])\lor(y_j=w_{i+j}\land S[i,j-1]).
$$

## Valore della soluzione

$$
S[m,n].
$$

## Complessita

$O(mn)$.

## Collegamenti

- [[dp_interleaving_sequenze]]

