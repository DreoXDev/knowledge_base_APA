---
type: solved_example
source_id: SRC-EXTRA-001
status: complete
tags: [apa, esempio-svolto, lcs, ingombro]
---

# LCS con ingombro - SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 11.

## Sottoproblema

$$
L_{i,j,c} = \text{lunghezza di una LCS tra } X_i,Y_j \text{ con ingombro al massimo } c.
$$

## Caso base

$$
L_{i,j,c}=0 \quad \text{se } i=0 \text{ oppure } j=0.
$$

## Passo chiave

Se $x_i=y_j$ e $w(x_i)\le c$:

$$
L_{i,j,c}=\max(L_{i-1,j,c},L_{i,j-1,c},L_{i-1,j-1,c-w(x_i)}+1).
$$

Metodo: [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]].

