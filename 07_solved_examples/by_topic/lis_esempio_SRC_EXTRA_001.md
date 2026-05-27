---
type: solved_example
source_id: SRC-EXTRA-001
status: complete
tags: [apa, esempio-svolto, lis]
---

# LIS - esempio da SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 02.

## Istanza

$$
X_m=\langle x_1,\dots,x_m\rangle.
$$

## Soluzione

Una tra le sottosequenze crescenti piu lunghe di $X_m$.

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
C_i=1+\max\{C_h\mid 1\le h<i,\ x_h<x_i\}.
$$

## Ricostruzione

Memorizzare il predecessore $b_i$ che realizza il massimo e risalire dal massimo globale.

Metodo: [[metodo_lis_lds]].

