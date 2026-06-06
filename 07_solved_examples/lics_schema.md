---
type: solved-example
topic: lics-schema
status: official_confirmed
source_id: SRC-OFFICIAL-EX-019
source_file: 01_sources/extra_materials/varianti-lics-20ott25.pdf
tags:
  - apa
  - esempio-svolto
  - topic/lics
---

# Schema soluzione - LICS

## Riconoscimento

Traccia tipica: "Date due sequenze `X,Y`, trovare una Longest Common Increasing Subsequence."

## Schema da esame

1. Definire `LICS_v(X_i,Y_j)` vincolata a terminare con `x_i = y_j`.
2. Definire `c_ij = |LICS_v(X_i,Y_j)|`.
3. Se `x_i != y_j`, porre `c_ij = 0`.
4. Se `x_i = y_j`, cercare predecessori `(h,k)` con `h<i`, `k<j`, `x_h < x_i`.
5. Se non esiste predecessore valido, `c_ij = 1`.
6. Valore ottimo: `max { c_ij }`.

## Warning

LICS non usa la ricorrenza LCS standard sui prefissi. Lo stato e vincolato a terminare nel match corrente.

Metodo: [[dp_lics_e_varianti]].
