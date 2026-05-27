---
type: method
status: complete_with_warnings
source_id: SRC-EXTRA-001
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/lics
---

# Metodo - LICS

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 01 e 15.

## Quando si usa

Quando bisogna trovare una Longest Increasing Common Subsequence: una sottosequenza comune a $X$ e $Y$ che sia anche crescente.

## Sottoproblema

$$
C_{i,j} = \text{lunghezza di una LICS che termina nel match } x_i=y_j.
$$

## Caso base

$$
C_{i,j}=0 \quad \text{se } x_i\ne y_j.
$$

## Passo ricorsivo

Se $x_i=y_j$:

$$
C_{i,j}=1+\max\{C_{h,k}\mid h<i,\ k<j,\ x_h<x_i\}.
$$

Con massimo vuoto uguale a $0$.

## Soluzione

$$
\max_{i,j} C_{i,j}.
$$

## Collegamenti

- [[metodo_lcs_base]]
- [[metodo_lis_lds]]
- [[lics_SRC_EXTRA_001]]

> [!Warning]
> Lo pseudocodice manoscritto e parzialmente rumoroso; la ricorrenza e comunque leggibile come massimo sui predecessori precedenti e minori.

