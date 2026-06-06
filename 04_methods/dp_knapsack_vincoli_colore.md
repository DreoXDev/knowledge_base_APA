---
type: method
topic: dp-knapsack-vincoli-colore
status: official_confirmed
source_id: SRC-OFFICIAL-EX-012
source_file: 01_sources/extra_materials/knapsack-atmost-3-red.pdf
tags:
  - apa
  - metodo
  - topic/zaino-01
  - topic/programmazione-dinamica
  - topic/colori
---

# DP - Zaino con al massimo 3 oggetti rossi

## Problema

Input:

- `X = {1,2,...,n}`, insieme di oggetti;
- `W : X -> N+`, con `W(i)=w_i`, ingombro dell'oggetto `i`;
- `V : X -> N+`, con `V(i)=v_i`, valore dell'oggetto `i`;
- `Col : X -> {red, blue}`;
- `C in N+`, capacita dello zaino;
- vincolo: al massimo 3 oggetti rossi.

Output: un sottoinsieme `S subseteq X` di valore totale massimo, con ingombro totale `<= C` e al massimo 3 oggetti rossi.

## Sottoproblema

Questa variante estende lo stato base $OPT(i,p)$ (si veda [[metodo_programmazione_dinamica_zaino_01]]) aggiungendo una dimensione $r$, che rappresenta il budget massimo di oggetti rossi ancora utilizzabile o ammesso.

`S_{i,c,r}` e il sottoinsieme di massimo valore tra gli oggetti:

```text
X_i = {1,2,...,i}
```

con:

- ingombro totale `<= c`;
- al massimo `r` oggetti rossi.

Dominio:

```text
0 <= i <= n
0 <= c <= C
0 <= r <= 3
```

Numero di sottoproblemi:

```text
4(n+1)(C+1)
```

## Coefficiente

```text
d_{i,c,r} = valore di S_{i,c,r}
```

Valore ottimo:

```text
d_{n,C,3}
```

## Casi base

```text
i = 0:
  d_{0,c,r} = 0
```

per ogni `c,r`.

```text
c = 0:
  d_{i,0,r} = 0
```

per ogni `i,r`, se tutti gli ingombri sono positivi.

## Passo ricorsivo

Per `i > 0`, `c > 0`.

### Oggetto troppo grande

Se `w_i > c`:

```text
d_{i,c,r} = d_{i-1,c,r}
```

### Oggetto non rosso

Se `w_i <= c` e `Col(i) != red`:

```text
d_{i,c,r} = max(
  d_{i-1,c-w_i,r} + v_i,
  d_{i-1,c,r}
)
```

### Oggetto rosso

Se `w_i <= c`, `Col(i) = red`, `r > 0`:

```text
d_{i,c,r} = max(
  d_{i-1,c-w_i,r-1} + v_i,
  d_{i-1,c,r}
)
```

Se `Col(i) = red` e `r = 0`:

```text
d_{i,c,0} = d_{i-1,c,0}
```

## Complessita

```text
Tempo: O(n C 4) = O(nC)
Spazio: O(n C 4) = O(nC)
```

Il fattore `4` deriva da `r in {0,1,2,3}`.

## Ricostruzione

Partire da `(n,C,3)`.

- Se `d_{i,c,r} = d_{i-1,c,r}`, l'oggetto `i` non e stato scelto.
- Altrimenti l'oggetto `i` e stato scelto:
  - se non rosso, passare a `(i-1, c-w_i, r)`;
  - se rosso, passare a `(i-1, c-w_i, r-1)`.

## Errori da evitare

- "Al massimo 3 rossi" non significa "esattamente 3 rossi".
- Il valore ottimo e `d_{n,C,3}`, perche lo stato consente fino a `r` rossi.
- Se una traccia chiede "esattamente 3 rossi", semantica dello stato e casi base cambiano.

Collegamenti: [[zaino_01_varianti]], [[knapsack_al_massimo_3_rossi_schema]], [[dp_knapsack_colori]].
