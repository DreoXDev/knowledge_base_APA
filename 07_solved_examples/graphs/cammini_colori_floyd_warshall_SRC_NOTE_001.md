# Cammini colorati con Floyd-Warshall esteso - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagine 23-32.

## Istanza

Grafo orientato o non orientato con colori su archi/vertici e vincolo richiesto.

## Sottoproblema

$$
D^k[i,j,\sigma]
$$

descrive cammini da $i$ a $j$ con intermedi in $\{1,\dots,k\}$ e stato extra $\sigma$.

## Caso base

Archi diretti per $k=0$.

## Passo ricorsivo

OR tra non passare da $k$ e concatenare un cammino $i\to k$ con uno $k\to j$.

## Collegamenti

- [[dp_grafi_floyd_warshall_stato_esteso]]

