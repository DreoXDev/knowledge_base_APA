---
type: method
topic: floyd-warshall-base
status: official_confirmed
source_id: SRC-OFFICIAL-EX-003
source_file: 01_sources/extra_materials/floyd-warshall-esempio-bottomup-27ott25.pdf
tags:
  - apa
  - metodo
  - topic/floyd-warshall
  - topic/cammini-minimi
---

# Floyd-Warshall - base bottom-up

## Problema

Input:

- grafo orientato senza cappi `G = (V,E,W)`;
- vertici `V = {1,2,...,n}`;
- matrice dei pesi `W = [w_ij]`.

Output: per ogni coppia di vertici `i,j`, trovare il cammino minimo da `i` a `j`.

## Matrice `W`

```text
i = j:
  w_ij = 0

i != j and (i,j) in E:
  w_ij = peso di (i,j)

i != j and (i,j) notin E:
  w_ij = +infinito
```

## Sottoproblema

`P_ij^k` = cammino minimo da `i` a `j` con eventuali vertici intermedi in `{1,...,k}`.

Coefficiente:

```text
d_ij^k = peso di P_ij^k
```

Predecessore:

```text
pi_ij^k = predecessore di j nel cammino P_ij^k
```

Valore ottimo:

```text
d_ij = d_ij^n
pi_ij = pi_ij^n
```

## Ricorrenza

Caso base:

```text
d_ij^0 = W[i,j]
```

Passo ricorsivo:

```text
d_ij^k = min(d_ij^{k-1}, d_ik^{k-1} + d_kj^{k-1})
```

Predecessori:

```text
se d_ij^{k-1} <= d_ik^{k-1} + d_kj^{k-1}:
  pi_ij^k = pi_ij^{k-1}
altrimenti:
  pi_ij^k = pi_kj^{k-1}
```

## Algoritmo bottom-up

```text
FLOYD_WARSHALL(W)
    D <- W
    inizializza Pi

    for k = 1 to n do
        for i = 1 to n do
            for j = 1 to n do
                if D[i,k] + D[k,j] < D[i,j] then
                    D[i,j] <- D[i,k] + D[k,j]
                    Pi[i,j] <- Pi[k,j]

    return D, Pi
```

## Ricostruzione

```text
PRINT_PATH(Pi, i, j)
    if i = j then
        print i
    else if Pi[i,j] = NIL then
        print "nessun cammino"
    else
        PRINT_PATH(Pi, i, Pi[i,j])
        print j
```

## Complessita

- Tempo: `Theta(n^3)`.
- Spazio: `Theta(n^2)` se si mantiene solo la matrice corrente; `Theta(n^3)` se si conservano tutti i livelli.

Collegamenti: [[fw_varianti_vincoli_colori]], [[fw_varianti_vincoli_colori_schema]].
