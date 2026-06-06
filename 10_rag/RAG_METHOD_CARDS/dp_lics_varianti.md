---
type: rag-method-card
topic: dp-lics-varianti
status: official_confirmed
source_methods:
  - 04_methods/dp_lics_e_varianti.md
  - 04_methods/dp_lcs_crescente_lics.md
  - 04_methods/metodo_lics.md
source_examples:
  - 07_solved_examples/lics_schema.md
  - 07_solved_examples/by_topic/lics_SRC_EXTRA_001.md
source_patterns:
  - 08_review/varianti_lcs_con_vincoli.md
exam_use: true
---

# LICS e varianti

## Trigger

- "LICS"
- "Longest Common Increasing Subsequence"
- "sottosequenza comune crescente"
- "problema simile a LICS"
- "sottoproblema vincolato a terminare"
- "alternanza di parita in sottosequenza comune"

## Decisione rapida

Se la traccia chiede una sottosequenza comune con una proprieta tra elementi consecutivi:

- usare stati `c_ij` vincolati a terminare con `x_i = y_j`;
- cercare predecessori `(h,k)` precedenti;
- filtrare i predecessori in base alla proprieta;
- valore finale come massimo globale.

## LICS base

Stato:

```text
c_ij = |LICS_v(X_i,Y_j)|
```

dove `LICS_v(X_i,Y_j)` e vincolata a terminare con `x_i`, se `x_i = y_j`.

Ricorrenza:

```text
Se x_i != y_j:
  c_ij = 0

Se x_i = y_j:
  c_ij = max { c_hk > 0 | h < i, k < j, x_h < x_i } + 1
```

Se il massimo e vuoto, `c_ij = 1`.

Valore finale:

```text
max { c_ij }
```

## Varianti

Per una variante, cambiare solo il filtro sui predecessori.

Esempio alternanza di parita:

```text
x_h mod 2 != x_i mod 2
```

## Warning

- Non usare la LCS standard.
- LICS non ha ricorrenza `max(c[i-1][j], c[i][j-1])`.
- Il valore finale e `max c_ij`, non `c_{m,n}`.
- La parita riguarda i valori, non gli indici.
