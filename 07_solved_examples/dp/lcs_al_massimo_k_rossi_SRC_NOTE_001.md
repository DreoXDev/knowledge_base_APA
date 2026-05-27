# LCS con al massimo K rossi - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagine 17-18.

## Istanza

Sequenze $X,Y$, funzione colore, budget $K$.

## Soluzione richiesta

Lunghezza massima di una LCS con al massimo $K$ rossi.

## Definizione coefficienti

$$
C[i,j,k]=\text{lunghezza di una LCS tra }X_i,Y_j\text{ con al massimo }k\text{ rossi}.
$$

## Caso base

Prefisso vuoto: $0$.

## Passo ricorsivo

Vedi [[dp_lcs_vincoli_colore]].

## Valore della soluzione

$$
C[m,n,K].
$$

## Errori comuni

Scalare $k$ anche quando il simbolo non e rosso.

