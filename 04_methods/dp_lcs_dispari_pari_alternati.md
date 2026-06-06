---
type: method
topic: dp-lcs-dispari-pari-alternati
status: official_confirmed
source_id: SRC-OFFICIAL-EX-015
source_file: 01_sources/extra_materials/lcs-even-odd.pdf
tags:
  - apa
  - metodo
  - topic/lcs
  - topic/programmazione-dinamica
  - topic/parita
---

# DP - LCS con dispari in posizioni dispari e pari in posizioni pari

## Problema

Input:

- `X = <x_1, ..., x_m>`
- `Y = <y_1, ..., y_n>`

Output:

- una LCS in cui gli elementi in posizione dispari della sottosequenza sono dispari;
- gli elementi in posizione pari della sottosequenza sono pari.

Note:

- la sequenza vuota e una soluzione;
- il vincolo riguarda le posizioni nella sottosequenza, non gli indici in `X` o `Y`.

## Esempio ufficiale

```text
X = <1, 2, 5, 3, 5, 9, 9, 11, 18, 10, 19>
Y = <14, 2, 5, 5, 9, 9, 11, 18, 20, 19, 10>

LCSdp(X,Y) = <5, 18, 19>
<2, 5, 18, 19> non e una LCSdp(X,Y)
```

Motivo:

- `<5,18,19>` rispetta lo schema dispari-pari-dispari;
- `<2,5,18,19>` inizia con un pari in posizione 1, quindi viola il vincolo.

## Idea

Si usa un sottoproblema ausiliario vincolato a terminare nel match corrente. La lunghezza precedente decide la posizione del nuovo elemento.

## Sottoproblema

`LCSdp_v(X_i,Y_j)` = migliore sottosequenza comune valida dei prefissi `X_i,Y_j`, vincolata a terminare con `x_i` se `x_i = y_j`.

Se `x_i != y_j`, il sottoproblema vincolato non esiste.

Coefficiente:

```text
c_ij = |LCSdp_v(X_i,Y_j)|
```

Numero di sottoproblemi:

```text
mn
```

## Valore ottimo

```text
OPT = max { c_ij | 1 <= i <= m, 1 <= j <= n }
```

Non usare `c_{m,n}`.

## Casi base / stati non esistenti

Se:

```text
x_i != y_j
```

allora:

```text
c_ij = 0
```

Il valore `0` indica che il sottoproblema vincolato a terminare in `x_i` non esiste. In questa variante la sequenza vuota e ammessa, quindi non si usa `-infinito`.

## Ricorrenza

### `x_i = y_j` e `x_i` e pari

Un elemento pari puo stare solo in posizione pari della sottosequenza. Quindi la lunghezza precedente deve essere dispari.

```text
c_ij = max{ c_hk > 0 | 1 <= h < i, 1 <= k < j, c_hk mod 2 = 1 } + 1
```

Se il massimo e vuoto:

```text
c_ij = 0
```

Motivo: un pari non puo iniziare una sottosequenza valida, perche la prima posizione richiede un elemento dispari.

### `x_i = y_j` e `x_i` e dispari

Un elemento dispari puo stare solo in posizione dispari della sottosequenza. Quindi la lunghezza precedente deve essere pari.

```text
c_ij = max{ c_hk > 0 | 1 <= h < i, 1 <= k < j, c_hk mod 2 = 0 } + 1
```

Se il massimo e vuoto:

```text
c_ij = 1
```

Motivo: un dispari puo iniziare una sottosequenza valida di lunghezza `1`.

## Complessita

Versione diretta dalle ricorrenze:

- per ogni coppia `(i,j)` si cercano predecessori `(h,k)`;
- tempo `O(m^2 n^2)`;
- spazio `O(mn)`.

Ottimizzazione possibile:

- mantenere massimi prefissi separati per lunghezza precedente pari e dispari;
- tempo riducibile a `O(mn)`;
- spazio `O(mn)` o ottimizzabile se non serve ricostruzione.

## Ricostruzione

Se richiesta:

- salvare un predecessore `(h,k)` per ogni `c_ij`;
- partire dalla cella `(i,j)` che realizza `OPT`;
- risalire tramite predecessori;
- stampare gli elementi in ordine inverso.

## Errori da evitare

- Non confondere la parita del valore `x_i` con la parita dell'indice `i`.
- Non trattare il vincolo come alternanza tra indici delle sequenze originali.
- Non usare `c_{m,n}`.
- Non iniziare una soluzione valida con un elemento pari.
