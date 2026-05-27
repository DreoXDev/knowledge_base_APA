---
type: solved_example
source_id: SRC-EXTRA-001
status: complete_with_warnings
tags: [apa, esempio-svolto, lds]
---

# LDS - esempio da SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 01.

## Schema

Si usa lo stesso sottoproblema della LIS:

$$
C_i = \text{lunghezza di una LDS che termina in } x_i.
$$

ma il vincolo sui predecessori diventa:

$$
x_h>x_i.
$$

## Passo ricorsivo

$$
C_i=1+\max\{C_h\mid 1\le h<i,\ x_h>x_i\}.
$$

Metodo: [[metodo_lis_lds]].

> [!Warning]
> La pagina nomina esplicitamente LDS ma non fornisce uno pseudocodice completo.

