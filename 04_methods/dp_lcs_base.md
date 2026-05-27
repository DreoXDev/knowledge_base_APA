---
type: method
status: complete
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, lcs]
---

# DP - LCS base

Fonte: [[source_inventory]] / SRC-NOTE-001 / `Analisi E Progettazione Di Algoritmi.pdf`, pagine 1-3.

## Metodo d'esame dagli appunti SRC-NOTE-001

## Istanza

Due sequenze $X=\langle x_1,\dots,x_m\rangle$ e $Y=\langle y_1,\dots,y_n\rangle$.

## Soluzione

Una sottosequenza comune $Z$ di lunghezza massima. La sequenza ottima puo non essere unica, ma la lunghezza ottima e unica.

## Sottoproblema

Considero i prefissi $X_i$ e $Y_j$.

## Coefficienti

$$
C[i,j]=\text{lunghezza di una LCS tra }X_i\text{ e }Y_j.
$$

## Caso base

$$
C[i,0]=C[0,j]=0.
$$

## Passo ricorsivo

$$
C[i,j]=
\begin{cases}
C[i-1,j-1]+1 & \text{se }x_i=y_j,\\
\max(C[i-1,j],C[i,j-1]) & \text{se }x_i\ne y_j.
\end{cases}
$$

## Valore della soluzione

$$
C[m,n].
$$

## Algoritmo bottom-up

```text
inizializza riga 0 e colonna 0 a 0
per i = 1..m:
  per j = 1..n:
    se x_i = y_j:
      C[i,j] = C[i-1,j-1] + 1
    altrimenti:
      C[i,j] = max(C[i-1,j], C[i,j-1])
ritorna C[m,n]
```

## Complessita

Tempo $O(mn)$, spazio $O(mn)$, riducibile a $O(\min(m,n))$ se serve solo la lunghezza.

## Collegamenti

- [[metodo_lcs_base]]
- [[lcs_base_SRC_NOTE_001]]
- [[dp_lcs_vincoli_colore]]
- [[dp_lcs_vincolo_somma_ingombro]]
- [[dp_lcs_crescente_lics]]

