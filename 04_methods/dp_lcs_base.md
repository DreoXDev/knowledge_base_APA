---
type: method
status: official_confirmed
source_id: SRC-OFFICIAL-EX-013
tags: [apa, metodo, programmazione-dinamica, lcs]
---

# DP - Longest Common Subsequence base

## Fonte ufficiale

- `SRC-OFFICIAL-EX-013`: `01_sources/extra_materials/lcs-6ott25.pdf`.
- Fonti precedenti: `SRC-NOTE-001`, `SRC-EXTRA-001`.

## Problema

Date due sequenze:

`X = <x_1,...,x_m>`

`Y = <y_1,...,y_n>`

trovare una sottosequenza comune di lunghezza massima.

## Definizioni essenziali

- Sequenza: lista ordinata di elementi.
- Prefisso `X_i`: sequenza `<x_1,...,x_i>`.
- Sottosequenza: sequenza ottenuta cancellando zero o piu elementi senza cambiare l'ordine relativo.
- Sottosequenza comune: sottosequenza di entrambe le sequenze.
- LCS: sottosequenza comune di lunghezza massima.

## Formulazione DP

### Sottoproblema

`LCS(X_i,Y_j)`.

### Coefficiente

`c_{i,j}=|LCS(X_i,Y_j)|`.

Il coefficiente contiene la lunghezza ottima, non la sequenza stessa.

### Valore ottimo

`c_{m,n}`.

### Casi base

Se `i=0` oppure `j=0`, allora:

`LCS(X_i,Y_j)=<>` e `c_{i,j}=0`.

### Passo ricorsivo

Per `i>0`, `j>0`:

```text
se x_i = y_j:
    c[i,j] = c[i-1,j-1] + 1
altrimenti:
    c[i,j] = max(c[i-1,j], c[i,j-1])
```

## Algoritmo bottom-up

```text
LCS-LENGTH(X,Y)
    m = length(X)
    n = length(Y)

    for i = 0 to m
        C[i,0] = 0
    for j = 0 to n
        C[0,j] = 0

    for i = 1 to m
        for j = 1 to n
            if x_i = y_j then
                C[i,j] = C[i-1,j-1] + 1
            else
                C[i,j] = max(C[i-1,j], C[i,j-1])

    return C
```

## Ricostruzione

```text
Print_LCS(C,X,Y,i,j)
    if i = 0 then
        return
    if j = 0 then
        return

    if x_i = y_j then
        Print_LCS(C,X,Y,i-1,j-1)
        print x_i
    else
        if C[i,j] = C[i-1,j] then
            Print_LCS(C,X,Y,i-1,j)
        else
            Print_LCS(C,X,Y,i,j-1)
```

Il `print x_i` va dopo la chiamata ricorsiva, cosi la sottosequenza viene stampata nell'ordine corretto.

In caso di pareggio tra `C[i-1,j]` e `C[i,j-1]`, possono esistere piu LCS corrette.

## Complessita

- Calcolo valore ottimo: `O(mn)` tempo.
- Spazio con ricostruzione: `O(mn)`.
- Ricostruzione: `O(m+n)` visite nel cammino, stampa al piu `min(m,n)` elementi.

## Errori comuni

- Dimenticare la prima riga/colonna a zero.
- Usare `i,j` invece di `i-1,j-1` quando `x_i=y_j`.
- Stampare il carattere prima della chiamata ricorsiva.
- Pensare che la LCS sia unica: in caso di pareggi possono esistere piu soluzioni.

## Collegamenti

- [[metodo_lcs_base]]
- [[metodo_ricostruzione_soluzione_dp]]
- [[lcs_base_6ott25]]
- [[lcs_base_SRC_NOTE_001]]
- [[dp_lcs_vincoli_colore]]
- [[dp_lcs_vincolo_somma_ingombro]]
- [[dp_lcs_crescente_lics]]
