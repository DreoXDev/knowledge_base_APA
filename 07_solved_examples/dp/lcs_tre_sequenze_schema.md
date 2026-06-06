---
type: solved-example
topic: lcs-tre-sequenze
status: official_confirmed
source_id: SRC-OFFICIAL-EX-016
source_file: 01_sources/extra_materials/lcs-three-sequences-20ott25.pdf
tags:
  - apa
  - esempio-svolto
  - topic/lcs
---

# Schema soluzione - LCS di 3 sequenze

## Riconoscimento

Traccia tipica: "Date tre sequenze `X`, `Y`, `W`, trovare una LCS comune a tutte e tre."

## Schema da esame

1. Definire il sottoproblema `LCS(X_i,Y_j,W_h)`.
2. Definire il coefficiente `c_{i,j,h}`.
3. Scrivere il valore ottimo: `c_{m,n,l}`.
4. Scrivere i casi base: `c_{i,j,h}=0` se `i=0` oppure `j=0` oppure `h=0`.
5. Scrivere il caso di match: se `x_i=y_j=w_h`, allora `c_{i,j,h}=c_{i-1,j-1,h-1}+1`.
6. Scrivere il caso di mismatch: `c_{i,j,h}=max(c_{i-1,j,h}, c_{i,j-1,h}, c_{i,j,h-1})`.
7. Calcolare bottom-up in ordine crescente di `i`, `j`, `h`.
8. Per ricostruire, seguire a ritroso la scelta che ha determinato il massimo.

## Warning

Non risolvere con due LCS successive: una LCS scelta tra `X` e `Y` puo eliminare una sottosequenza che sarebbe ottima considerando anche `W`.

Metodo: [[dp_lcs_tre_sequenze]].
