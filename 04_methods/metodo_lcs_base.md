---
type: method
status: official_confirmed
source_id: SRC-OFFICIAL-EX-013
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
---

# Metodo - LCS base

Fonte ufficiale: `SRC-OFFICIAL-EX-013`, `01_sources/extra_materials/lcs-6ott25.pdf`.

Fonte precedente: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 03.

## Quando si usa

Quando bisogna trovare la lunghezza di una piu lunga sottosequenza comune tra due sequenze $X=\langle x_1,\dots,x_m\rangle$ e $Y=\langle y_1,\dots,y_n\rangle$.

## Sottoproblema e coefficienti

$$
c_{i,j} = |LCS(X_i,Y_j)|
$$

dove `X_i=<x_1,...,x_i>` e `Y_j=<y_1,...,y_j>`.

## Caso base

$$
C_{i,0}=C_{0,j}=0.
$$

Equivalente: se `i=0` oppure `j=0`, allora `c_{i,j}=0`.

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

## Schema risposta da esame

1. Definire `LCS(X_i,Y_j)`.
2. Definire `c_{i,j}=|LCS(X_i,Y_j)|`.
3. Scrivere `c_{m,n}` come valore ottimo.
4. Scrivere casi base con prefisso vuoto.
5. Scrivere ricorrenza match/non-match.
6. Scrivere bottom-up se richiesto.
7. Scrivere `Print_LCS` se richiesta ricostruzione.

Per la ricostruzione usare [[metodo_ricostruzione_soluzione_dp]].

## Algoritmo bottom-up

Riempire la tabella per righe o colonne crescenti: prima riga e prima colonna a $0$, poi $i=1,\dots,m$ e $j=1,\dots,n$.

## Ricostruzione

Se `x_i=y_j`, chiamare ricorsivamente su `(i-1,j-1)` e poi stampare `x_i`.

Se `x_i!=y_j`, seguire una cella precedente con lo stesso valore ottimo. In caso di pareggio sono possibili piu LCS corrette.

## Varianti collegate

- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]
- [[metodo_lics]]
- [[metodo_lcs_alternanza_pari_dispari]]
