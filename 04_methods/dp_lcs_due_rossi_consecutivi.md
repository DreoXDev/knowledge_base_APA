---
type: method
topic: dp-lcs-due-rossi-consecutivi
status: official_confirmed
source_id: SRC-OFFICIAL-EX-014
source_file: 01_sources/extra_materials/lcs-atleast-2-consecutive-red.pdf
tags:
  - apa
  - metodo
  - topic/lcs
  - topic/programmazione-dinamica
  - topic/colori
---

# DP - LCS con due elementi rossi consecutivi

## Problema

Input:

- `X = <x_1, ..., x_m>`
- `Y = <y_1, ..., y_n>`
- `col: Sigma -> {red, green, blue}`

Output: una LCS in cui sono presenti almeno due elementi rossi consecutivi.

Note:

- la sequenza vuota non e soluzione;
- "consecutivi" significa consecutivi nella sottosequenza costruita, non nelle sequenze originali.

## Idea

Usare due stati ausiliari vincolati a terminare nel match corrente. Questo permette di controllare se la coppia di rossi consecutivi e gia presente oppure puo nascere apponendo l'ultimo elemento.

## Sottoproblemi

### Stato 1: coppia gia presente

`LCS2red_v(X_i,Y_j)` = migliore sottosequenza comune dei prefissi `X_i,Y_j`, vincolata a terminare con `x_i`, in cui sono presenti due elementi rossi consecutivi.

Coefficiente:

```text
c_ij1 = |LCS2red_v(X_i,Y_j)|
```

### Stato 0: coppia non ancora presente

`LCS0red_v(X_i,Y_j)` = migliore sottosequenza comune dei prefissi `X_i,Y_j`, vincolata a terminare con `x_i`, in cui non sono presenti due elementi rossi consecutivi.

Coefficiente:

```text
c_ij0 = |LCS0red_v(X_i,Y_j)|
```

## Stati impossibili

Se `x_i != y_j`:

```text
c_ij1 = -infinito
c_ij0 = -infinito
```

Motivo: gli stati sono vincolati a terminare con `x_i`; se `x_i` non coincide con `y_j`, non possono terminare nello stesso elemento comune.

## Ricorrenza per `c_ij1`

Per `x_i = y_j`.

### `col(x_i) != red`

```text
c_ij1 = max{ c_hk1 != -infinito | 1 <= h < i, 1 <= k < j } + 1
```

Se il massimo e vuoto:

```text
c_ij1 = -infinito
```

### `col(x_i) = red`

```text
c_ij1 = max(
  max{ c_hk0 != -infinito | 1 <= h < i, 1 <= k < j, col(x_h) = red } + 1,
  max{ c_hk1 != -infinito | 1 <= h < i, 1 <= k < j } + 1
)
```

Se entrambi i massimi sono vuoti:

```text
c_ij1 = -infinito
```

Interpretazione:

- primo massimo: la coppia di rossi consecutivi nasce aggiungendo `x_i` dopo un precedente elemento rosso;
- secondo massimo: la coppia era gia presente.

## Ricorrenza per `c_ij0`

Per `x_i = y_j`.

### `col(x_i) = red`

```text
c_ij0 = max{ c_hk0 != -infinito | 1 <= h < i, 1 <= k < j, col(x_h) != red } + 1
```

Se il massimo e vuoto:

```text
c_ij0 = 1
```

Motivo: se `x_i` e rosso e vogliamo restare senza due rossi consecutivi, il predecessore non deve essere rosso.

### `col(x_i) != red`

```text
c_ij0 = max{ c_hk0 != -infinito | 1 <= h < i, 1 <= k < j } + 1
```

Se il massimo e vuoto:

```text
c_ij0 = 1
```

## Valore ottimo

```text
OPT = max{ c_ij1 | 1 <= i <= m, 1 <= j <= n }
```

Se `OPT = -infinito`, non esiste una sottosequenza comune con due rossi consecutivi.

## Complessita

Versione diretta dalle ricorrenze:

- per ogni coppia `(i,j)` si cercano predecessori `(h,k)`;
- tempo `O(m^2 n^2)`;
- spazio `O(mn)` per ogni stato, quindi `O(mn)` totale a fattori costanti.

Ottimizzazione possibile:

- mantenere massimi prefissi per `c_ij1`;
- mantenere massimi prefissi per `c_ij0` distinguendo ultimo elemento rosso/non rosso;
- tempo riducibile a `O(mn)` se i massimi prefissi sono aggiornati correttamente.

## Errori da evitare

- Non usare `c_{m,n}` come risposta.
- Non confondere "due rossi consecutivi" con "almeno due rossi totali".
- Non richiedere che i due rossi siano consecutivi in `X` o in `Y`.
- Non usare `0` per `c_ij1` e `c_ij0` quando `x_i != y_j`: qui lo stato e inesistente e va rappresentato con `-infinito`.
