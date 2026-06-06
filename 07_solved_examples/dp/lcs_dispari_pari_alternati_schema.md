---
type: solved-example
topic: lcs-dispari-pari-alternati
status: official_confirmed
source_id: SRC-OFFICIAL-EX-015
source_file: 01_sources/extra_materials/lcs-even-odd.pdf
tags:
  - apa
  - esempio-svolto
  - topic/lcs
  - topic/parita
---

# Schema soluzione - LCS con dispari in posizioni dispari e pari in posizioni pari

## Riconoscimento

Traccia tipica: "Date due sequenze `X,Y`, trovare una LCS in cui gli elementi dispari stanno nelle posizioni dispari e gli elementi pari nelle posizioni pari."

## Esempio ufficiale

```text
X = <1, 2, 5, 3, 5, 9, 9, 11, 18, 10, 19>
Y = <14, 2, 5, 5, 9, 9, 11, 18, 20, 19, 10>

Soluzione valida:
<5, 18, 19>

Soluzione non valida:
<2, 5, 18, 19>
```

Motivo:

- `<5,18,19>`: posizione 1 dispari, posizione 2 pari, posizione 3 dispari;
- `<2,5,18,19>` non e valida perche la posizione 1 contiene `2`, che e pari.

## Schema da esame

1. Definire `LCSdp_v(X_i,Y_j)` vincolata a terminare con `x_i`.
2. Definire `c_ij`.
3. Se `x_i != y_j`, porre `c_ij = 0`.
4. Se `x_i` e pari, cercare predecessori con lunghezza dispari.
5. Se `x_i` e dispari, cercare predecessori con lunghezza pari.
6. Valore ottimo come massimo globale dei `c_ij`.

Metodo: [[dp_lcs_dispari_pari_alternati]].
