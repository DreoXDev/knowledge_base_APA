---
type: method
status: scaffold
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/ricostruzione-soluzione
---

# Metodo - Ricostruzione soluzione DP

## Quando si usa

Quando l'esercizio non chiede solo il valore ottimo, ma anche di stampare o ricostruire una soluzione ottima.

## Schema ricorrente

- partire dal coefficiente soluzione;
- confrontare i casi che hanno generato il valore;
- registrare le scelte;
- ricorrere sul sottoproblema precedente.

## Ricostruzione LCS da matrice C

Per LCS non serve necessariamente una matrice dei predecessori: si puo ricostruire leggendo i valori di `C`.

- Se `x_i = y_j`, la soluzione passa per la diagonale `(i-1,j-1)` e poi include `x_i`.
- Se `x_i != y_j`, si segue una cella precedente con lo stesso valore ottimo: `(i-1,j)` oppure `(i,j-1)`.
- In caso di pareggio, entrambe le scelte possono portare a LCS corrette diverse.

Il carattere va stampato dopo la chiamata ricorsiva diagonale, altrimenti l'ordine della sottosequenza viene invertito.

### Ricostruzione LCS con al massimo k rossi

Usare per la variante ufficiale `SRC-LECTURE-001`.

- se `x_i != y_j`, seguire il ramo sopra/sinistra che realizza `C[i][j][r]`;
- se `x_i = y_j` e non e rosso, chiamare `(i-1,j-1,r)` e stampare `x_i`;
- se `x_i = y_j`, e rosso e `r = 0`, chiamare `(i-1,j-1,r)` senza stampare;
- se `x_i = y_j`, e rosso e `r > 0`, chiamare `(i-1,j-1,r-1)` e stampare `x_i`.

Nella stampa ricorsiva, il `print x_i` va dopo la chiamata ricorsiva per mantenere l'ordine sinistra-destra della sottosequenza.

Nome standard da usare nella KB: `Print_LCS_max_3`.

## Esercizi collegati

- [[exam_2026_01_12_e01]]
- [[exam_2025_07_03_p1_e01]]
- [[exam_2025_06_09_p1_e01]]

## Teoria necessaria

- [[programmazione_dinamica]]

## Errori comuni

> [!Warning]
> Metodo da completare dopo analisi di altri appelli o degli appunti.
