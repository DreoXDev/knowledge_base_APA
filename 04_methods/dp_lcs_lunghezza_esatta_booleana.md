---
type: method
status: complete_with_warning
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, lcs, booleana]
---

# DP - LCS con lunghezza esatta booleana

Fonte: [[source_inventory]] / SRC-NOTE-001, pagina 6.

## Quando riconoscerla

La consegna chiede se esiste una sottosequenza comune di lunghezza $L$, oppure se la LCS ha una lunghezza richiesta.

> [!Warning]
> Gli appunti usano "LCS di lunghezza $L$". Se la domanda intende proprio una LCS ottima, bisogna anche verificare che $L$ sia la lunghezza ottima calcolata da [[dp_lcs_base]].

## Coefficiente booleano

$$
B[i,j,\ell]=true
$$

sse esiste una sottosequenza comune tra $X_i$ e $Y_j$ di lunghezza $\ell$.

## Caso base

$$
B[i,j,0]=true.
$$

$$
B[0,j,\ell]=B[i,0,\ell]=false \quad \text{per }\ell>0.
$$

## Passo ricorsivo

Se $x_i=y_j$:

$$
B[i,j,\ell]=B[i-1,j,\ell]\lor B[i,j-1,\ell]\lor B[i-1,j-1,\ell-1].
$$

Se $x_i\ne y_j$:

$$
B[i,j,\ell]=B[i-1,j,\ell]\lor B[i,j-1,\ell].
$$

## Soluzione

$$
B[m,n,L].
$$

## Complessita

Tempo $O(mnL)$, spazio $O(mnL)$.

