---
type: rag-method-card
topic: dp-lcs-varianti
status: official_confirmed
source_methods:
  - 04_methods/dp_lcs_tre_sequenze.md
  - 04_methods/dp_lcs_due_rossi_consecutivi.md
  - 04_methods/dp_lcs_dispari_pari_alternati.md
source_examples:
  - 07_solved_examples/dp/lcs_tre_sequenze_schema.md
  - 07_solved_examples/dp/lcs_due_rossi_consecutivi_schema.md
  - 07_solved_examples/dp/lcs_dispari_pari_alternati_schema.md
source_patterns:
  - 06_exam_patterns/parte_i_dynamic_programming_patterns.md
exam_use: true
---

# DP LCS - varianti ufficiali

Questa card raccoglie varianti LCS ufficiali che non sono solo "LCS base" e non sono solo "conteggio di colori". Usarla quando la traccia aggiunge sequenze, vincoli interni alla sottosequenza o vincoli sulle posizioni della sottosequenza.

## Scelta rapida del pattern

| Traccia | Stato principale | Valore ottimo | Metodo |
|---|---|---|---|
| LCS di tre sequenze `X,Y,W` | `c_{i,j,h}` sui tre prefissi | `c_{m,n,l}` | [[dp_lcs_tre_sequenze]] |
| LCS con due rossi consecutivi | `c_ij1`, `c_ij0`, vincolati a terminare nel match | `max c_ij1` | [[dp_lcs_due_rossi_consecutivi]] |
| LCS con dispari in posizioni dispari e pari in posizioni pari | `c_ij`, vincolato a terminare nel match | `max c_ij` | [[dp_lcs_dispari_pari_alternati]] |

## Variante ufficiale - LCS di 3 sequenze

Fonte ufficiale: `SRC-OFFICIAL-EX-016`, PDF `01_sources/extra_materials/lcs-three-sequences-20ott25.pdf`.

Pattern traccia:

- "LCS di 3 sequenze"
- "Longest Common Subsequence di tre sequenze"
- `LCS(X,Y,W)`
- "sottosequenza comune di `X`, `Y` e `W`"

Idea: generalizzare la LCS standard aggiungendo una dimensione alla tabella DP.

Sottoproblema:

`LCS(X_i,Y_j,W_h)` = LCS dei prefissi `X_i`, `Y_j`, `W_h`.

Coefficiente:

`c_{i,j,h} = |LCS(X_i,Y_j,W_h)|`.

Valore ottimo:

`c_{m,n,l}`.

Ricorrenza:

```text
Se i = 0 oppure j = 0 oppure h = 0:
  c_{i,j,h} = 0

Se i,j,h > 0 e x_i = y_j = w_h:
  c_{i,j,h} = c_{i-1,j-1,h-1} + 1

Altrimenti:
  c_{i,j,h} = max(c_{i-1,j,h}, c_{i,j-1,h}, c_{i,j,h-1})
```

Complessita:

- tempo `Theta(mnl)`;
- spazio `Theta(mnl)`.

Attenzione:

- non fare prima `LCS(X,Y)` e poi LCS con `W`;
- non usare tabella bidimensionale;
- non usare massimo globale: il valore e `c_{m,n,l}`;
- nel mismatch si scarta un ultimo elemento da una sola sequenza alla volta.

## Variante ufficiale - LCS con due rossi consecutivi

Fonte ufficiale: `SRC-OFFICIAL-EX-014`, PDF `01_sources/extra_materials/lcs-atleast-2-consecutive-red.pdf`.

Pattern traccia:

- `LCS2red(X,Y)`
- "due elementi rossi consecutivi"
- "almeno due rossi consecutivi nella sottosequenza"

Idea: non basta contare i rossi. Servono stati vincolati a terminare nel match corrente.

Stati:

- `c_ij1`: migliore sottosequenza comune dei prefissi `X_i,Y_j`, vincolata a terminare con `x_i`, in cui sono gia presenti due rossi consecutivi;
- `c_ij0`: migliore sottosequenza comune dei prefissi `X_i,Y_j`, vincolata a terminare con `x_i`, in cui non sono presenti due rossi consecutivi.

Stati impossibili:

```text
Se x_i != y_j:
  c_ij1 = c_ij0 = -infinito
```

Valore ottimo:

```text
OPT = max { c_ij1 | 1 <= i <= m, 1 <= j <= n }
```

Ricorrenze compatte, per `x_i = y_j`:

```text
Se col(x_i) != red:
  c_ij1 = max{ c_hk1 != -infinito | h < i, k < j } + 1
  c_ij0 = max{ c_hk0 != -infinito | h < i, k < j } + 1

Se col(x_i) = red:
  c_ij1 = max(
    max{ c_hk0 != -infinito | h < i, k < j, col(x_h) = red } + 1,
    max{ c_hk1 != -infinito | h < i, k < j } + 1
  )
  c_ij0 = max{ c_hk0 != -infinito | h < i, k < j, col(x_h) != red } + 1
```

Se un massimo per `c_ij1` e vuoto, il valore resta `-infinito`. Se un massimo per `c_ij0` e vuoto e `x_i = y_j`, si puo iniziare una sottosequenza di lunghezza `1`.

Attenzione:

- "consecutivi" significa consecutivi nella sottosequenza, non necessariamente in `X` o in `Y`;
- i predecessori sono tutti gli `h < i`, `k < j`, non solo `(i-1,j-1)`;
- non usare `c_{m,n}`.

## Variante ufficiale - LCS con dispari in posizioni dispari e pari in posizioni pari

Fonte ufficiale: `SRC-OFFICIAL-EX-015`, PDF `01_sources/extra_materials/lcs-even-odd.pdf`.

Pattern traccia:

- `LCSdp(X,Y)`
- "dispari in posizioni dispari e pari in posizioni pari"
- "odd/even alternating LCS"

Vincolo:

- posizione 1, 3, 5, ... della sottosequenza: elemento dispari;
- posizione 2, 4, 6, ... della sottosequenza: elemento pari.

Sottoproblema:

`LCSdp_v(X_i,Y_j)` = migliore sottosequenza comune valida dei prefissi `X_i,Y_j`, vincolata a terminare con `x_i` se `x_i = y_j`.

Coefficiente:

`c_ij = |LCSdp_v(X_i,Y_j)|`.

Ricorrenza:

```text
Se x_i != y_j:
  c_ij = 0

Se x_i = y_j e x_i e pari:
  c_ij = max{ c_hk > 0 | h < i, k < j, c_hk mod 2 = 1 } + 1
  se il massimo e vuoto: c_ij = 0

Se x_i = y_j e x_i e dispari:
  c_ij = max{ c_hk > 0 | h < i, k < j, c_hk mod 2 = 0 } + 1
  se il massimo e vuoto: c_ij = 1
```

Valore ottimo:

```text
OPT = max { c_ij | 1 <= i <= m, 1 <= j <= n }
```

Attenzione:

- la parita di `x_i` e la parita del valore, non dell'indice `i`;
- `c_hk mod 2` e la parita della lunghezza gia costruita;
- la posizione del nuovo elemento e `c_hk + 1`;
- la sequenza vuota e ammessa come soluzione, ma gli stati vincolati inesistenti valgono `0`;
- non usare direttamente la LCS standard.
