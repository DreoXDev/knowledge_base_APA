---
type: method
topic: dp-lcs-tre-sequenze
status: official_confirmed
source_id: SRC-OFFICIAL-EX-016
source_file: 01_sources/extra_materials/lcs-three-sequences-20ott25.pdf
tags:
  - apa
  - metodo
  - topic/lcs
  - topic/programmazione-dinamica
---

# DP - LCS di 3 sequenze

## Problema

Input:

- `X = <x_1, ..., x_m>`
- `Y = <y_1, ..., y_n>`
- `W = <w_1, ..., w_l>`

Output: una piu lunga sottosequenza comune di `X`, `Y` e `W`.

## Idea

Generalizzare la LCS standard usando una tabella tridimensionale. A differenza delle varianti con vincoli di terminazione, qui il valore ottimo e direttamente il coefficiente finale.

## Sottoproblema

Per:

```text
i in {0, ..., m}
j in {0, ..., n}
h in {0, ..., l}
```

definiamo `LCS(X_i,Y_j,W_h)` come la LCS dei prefissi `X_i`, `Y_j`, `W_h`.

Coefficiente:

```text
c_{i,j,h} = |LCS(X_i,Y_j,W_h)|
```

Numero di sottoproblemi:

```text
(m+1)(n+1)(l+1)
```

Problema principale:

```text
LCS(X,Y,W) = LCS(X_m,Y_n,W_l)
```

Valore ottimo:

```text
c_{m,n,l}
```

## Casi base

Se almeno un prefisso e vuoto:

```text
i = 0 oppure j = 0 oppure h = 0
```

allora:

```text
LCS(X_i,Y_j,W_h) = <>
c_{i,j,h} = 0
```

## Passo ricorsivo

Per `i > 0`, `j > 0`, `h > 0`.

### Ultimi elementi uguali

Se:

```text
x_i = y_j = w_h
```

allora:

```text
c_{i,j,h} = c_{i-1,j-1,h-1} + 1
```

### Ultimi elementi non tutti uguali

Se gli ultimi elementi non coincidono tutti:

```text
c_{i,j,h} = max {
  c_{i-1,j,h},
  c_{i,j-1,h},
  c_{i,j,h-1}
}
```

Interpretazione: si prova a scartare l'ultimo elemento da una delle tre sequenze.

## Algoritmo bottom-up

```text
calcola_ottimo_LCS_3_sequenze(X,Y,W)
    C <- matrice di dimensione (m+1)(n+1)(l+1)

    for i = 0 to m do
        for j = 0 to n do
            C[i,j,0] <- 0

    for i = 0 to m do
        for h = 0 to l do
            C[i,0,h] <- 0

    for j = 0 to n do
        for h = 0 to l do
            C[0,j,h] <- 0

    for i = 1 to m do
        for j = 1 to n do
            for h = 1 to l do
                if x_i = y_j and y_j = w_h then
                    C[i,j,h] <- C[i-1,j-1,h-1] + 1
                else
                    C[i,j,h] <- max(C[i-1,j,h], C[i,j-1,h], C[i,j,h-1])

    return C[m,n,l]
```

## Ricostruzione

```text
Print_LCS_3_sequenze(C, X, Y, W, i, j, h)
    if i > 0 and j > 0 and h > 0 then
        if x_i = y_j and y_j = w_h then
            Print_LCS_3_sequenze(C, X, Y, W, i-1, j-1, h-1)
            print x_i
        else
            if C[i,j,h] = C[i-1,j,h] then
                Print_LCS_3_sequenze(C, X, Y, W, i-1, j, h)
            else if C[i,j,h] = C[i,j-1,h] then
                Print_LCS_3_sequenze(C, X, Y, W, i, j-1, h)
            else
                Print_LCS_3_sequenze(C, X, Y, W, i, j, h-1)
```

In caso di pareggio tra piu massimi, una qualunque scelta valida produce una LCS ottima.

## Complessita

- Tempo: `Theta(mnl)`.
- Spazio: `Theta(mnl)`.

## Errori da evitare

- Non calcolare prima una LCS tra `X` e `Y` e poi una LCS con `W`.
- Non usare una tabella 2D.
- Non usare un massimo globale: il valore ottimo e `c_{m,n,l}`.
- Non confondere `h` con un parametro di vincolo: qui e l'indice del prefisso di `W`.
