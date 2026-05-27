---
type: solved_example
source_id: SRC-EXTRA-001
status: complete_with_warnings
tags: [apa, esempio-svolto, lcs, lics]
---

# LCS crescente - esempio da SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 01.

## Istanza

Due sequenze $X$ e $Y$.

## Soluzione

Una sottosequenza comune di lunghezza massima che sia anche crescente.

## Metodo

Usare [[metodo_lics]]:

$$
C_{i,j}=0 \text{ se } x_i\ne y_j
$$

e, se $x_i=y_j$:

$$
C_{i,j}=1+\max\{C_{h,k}\mid h<i,\ k<j,\ x_h<x_i\}.
$$

## Soluzione del problema

$$
\max_{i,j} C_{i,j}.
$$

> [!Warning]
> La pagina 01 e poco leggibile; la formula e normalizzata anche con pagina 15.

