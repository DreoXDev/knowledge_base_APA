---
type: solved_example
source_id: SRC-EXTRA-001
status: complete_with_warnings
tags: [apa, esempio-svolto, lics]
---

# LICS - SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 15.

## Coefficiente

$$
C_{i,j} = \text{lunghezza di una LICS che termina in } x_i=y_j.
$$

## Ricorrenza

$$
C_{i,j} =
\begin{cases}
0 & \text{se } x_i \ne y_j,\\
1+\max\{C_{h,k}\mid h<i,\ k<j,\ x_h<x_i\} & \text{se } x_i=y_j.
\end{cases}
$$

## Soluzione

$$
\max_{i,j} C_{i,j}.
$$

Metodo: [[metodo_lics]].

