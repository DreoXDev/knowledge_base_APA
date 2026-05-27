---
type: method
status: complete
source_id: SRC-EXTRA-001
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
---

# Metodo - LCS base

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 03.

## Quando si usa

Quando bisogna trovare la lunghezza di una piu lunga sottosequenza comune tra due sequenze $X=\langle x_1,\dots,x_m\rangle$ e $Y=\langle y_1,\dots,y_n\rangle$.

## Sottoproblema e coefficienti

$$
C_{i,j} = \text{lunghezza di una LCS tra } X_i \text{ e } Y_j.
$$

## Caso base

$$
C_{i,0}=C_{0,j}=0.
$$

## Passo ricorsivo

$$
C_{i,j} =
\begin{cases}
\max(C_{i-1,j}, C_{i,j-1}) & \text{se } x_i \ne y_j,\\
C_{i-1,j-1}+1 & \text{se } x_i=y_j.
\end{cases}
$$

## Soluzione

$$
C_{m,n}.
$$

## Algoritmo bottom-up

Riempire la tabella per righe o colonne crescenti: prima riga e prima colonna a $0$, poi $i=1,\dots,m$ e $j=1,\dots,n$.

## Varianti collegate

- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]
- [[metodo_lics]]
- [[metodo_lcs_alternanza_pari_dispari]]

