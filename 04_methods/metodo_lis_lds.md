---
type: method
status: complete
source_id: SRC-EXTRA-001
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lis
  - topic/lds
---

# Metodo - LIS e LDS

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 01-02.

## LIS

Istanza:

$$
X_m=\langle x_1,\dots,x_m\rangle.
$$

Soluzione: una tra le sottosequenze crescenti piu lunghe di $X_m$.

## Sottoproblema

$$
C_i = \text{lunghezza di una LIS che termina in } x_i.
$$

## Caso base

$$
C_1=1.
$$

## Passo ricorsivo

$$
C_i = 1 + \max\{C_h \mid 1\le h<i,\ x_h<x_i\}.
$$

Se l'insieme e vuoto, il massimo vale $0$ e quindi $C_i=1$.

## Soluzione

$$
\max_{1\le i\le m} C_i.
$$

## Ricostruzione

Memorizzare in $b_i$ l'indice $h$ che realizza il massimo. Si parte dall'indice con valore $C_i$ massimo e si risale tramite $b$.

## LDS

Per la Longest Decreasing Subsequence si usa lo stesso schema, cambiando il vincolo:

$$
x_h > x_i.
$$

