---
type: method
topic: dp-lics-e-varianti
status: official_confirmed
source_id: SRC-OFFICIAL-EX-019
source_file: 01_sources/extra_materials/varianti-lics-20ott25.pdf
tags:
  - apa
  - metodo
  - topic/lics
  - topic/programmazione-dinamica
---

# DP - LICS e varianti

## Problema LICS

Input:

- `X = <x_1, x_2, ..., x_m>`;
- `Y = <y_1, y_2, ..., y_n>`.

Output: `LICS(X,Y)`, Longest Common Increasing Subsequence, cioe una sottosequenza comune `Z = <z_1, ..., z_k>` tale che:

```text
z_i < z_{i+1}, per 1 <= i < k
```

## Sottoproblema ausiliario

`LICS_v(X_i,Y_j)` e la piu lunga sottosequenza comune crescente dei prefissi `X_i` e `Y_j`, vincolata a terminare con `x_i`, se `x_i = y_j`.

Se:

```text
x_i != y_j
```

allora `LICS_v(X_i,Y_j)` non esiste.

Coefficiente:

```text
c_ij = |LICS_v(X_i,Y_j)|
```

Numero totale di sottoproblemi:

```text
mn
```

Valore ottimo:

```text
LICS(X,Y) = max { c_ij | 1 <= i <= m, 1 <= j <= n }
```

## Casi base

```text
x_i != y_j:
  c_ij = 0
```

## Passo ricorsivo

Se:

```text
x_i = y_j
```

allora:

```text
c_ij = max { c_hk > 0 | 1 <= h < i, 1 <= k < j, x_h < x_i } + 1
```

con `max(insieme vuoto) = 0`. Quindi, se non esiste predecessore valido:

```text
c_ij = 1
```

## Bottom-up

Calcolare la matrice `C` per `i = 1..m`, `j = 1..n`.

Per ogni cella `(i,j)`:

- se `x_i != y_j`, porre `C[i,j]=0`;
- se `x_i = y_j`, cercare tra tutte le celle precedenti `(h,k)` con `h<i`, `k<j`, `x_h < x_i`.

## Complessita

Versione diretta:

```text
Tempo: O(m^2 n^2)
Spazio: O(mn)
```

## Pattern generale - problemi simili a LICS

Molte varianti su due sequenze usano lo stesso schema:

1. Definire un sottoproblema `P_v(X_i,Y_j)` vincolato a terminare con `x_i`, se `x_i = y_j`.
2. Se `x_i != y_j`, lo stato non esiste e il coefficiente vale `0`.
3. Se `x_i = y_j`, cercare predecessori `(h,k)` con `h < i`, `k < j` e proprieta richiesta dalla traccia.
4. Il valore ottimo e `max { c_ij }`, non `c_{m,n}`.

## Variante - alternanza di parita

Se la traccia richiede alternanza di parita tra elementi consecutivi della sottosequenza:

```text
c_ij = max { c_hk > 0 | 1 <= h < i, 1 <= k < j, x_h mod 2 != x_i mod 2 } + 1
```

con `max(insieme vuoto) = 0`.

Warning:

- `x_h mod 2` e `x_i mod 2` sono parita dei valori, non degli indici;
- la condizione riguarda elementi consecutivi nella sottosequenza.

## Errori da evitare

- Non usare la ricorrenza LCS standard `max(c[i-1][j], c[i][j-1])`.
- Non usare `c_{m,n}` come valore finale.
- Non dimenticare che lo stato e vincolato a terminare nel match corrente.

Collegamenti: [[dp_lcs_varianti]], [[lics_schema]], [[dp_lcs_crescente_lics]], [[metodo_lics]].
