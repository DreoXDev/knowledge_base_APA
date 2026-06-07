---
type: method
status: complete
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, lcs, ingombro]
---

# DP - LCS con vincolo di somma o ingombro

Fonte: [[source_inventory]] / SRC-NOTE-001, pagina 7.

## Regola anti-confusione

La frase "ingombro complessivo <= W" indica una somma totale dei pesi dei simboli scelti. Non indica che i pesi debbano essere crescenti o non decrescenti.

Quindi il metodo corretto usa un indice di budget:

```text
C[i,j,k]
```

Non usare una ricorrenza tipo LICS con condizione locale:

```text
w(prev) <= w(curr)
```

a meno che la traccia chieda esplicitamente una sottosequenza crescente/non decrescente rispetto al peso.

## Coefficiente

$$
C[i,j,k]=\text{lunghezza di una LCS di }X_i,Y_j\text{ con somma complessiva }\le k.
$$

## Caso base

$$
C[0,j,k]=C[i,0,k]=0.
$$

## Passo ricorsivo

Se $x_i\ne y_j$:

$$
C[i,j,k]=\max(C[i-1,j,k],C[i,j-1,k]).
$$

Se $x_i=y_j$ e $x_i\le k$:

$$
C[i,j,k]=\max(C[i-1,j,k],C[i,j-1,k],C[i-1,j-1,k-x_i]+1).
$$

Se $x_i=y_j$ e $x_i>k$:

$$
C[i,j,k]=\max(C[i-1,j,k],C[i,j-1,k]).
$$

## Soluzione

$$
C[m,n,K].
$$

## Collegamenti

- [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]
- [[dp_lcs_base]]
- [[dp_knapsack_colori]]
