# Prompt RAG APA - Parte I, Esercizio 1: LCS con ingombro

Modulo specifico per l'esercizio:

> Date due sequenze `X = <x_1,...,x_m>` e `Y = <y_1,...,y_n>`, una funzione di ingombro `w:S -> N` e un budget `W`, determinare una piu lunga sottosequenza comune di `X` e `Y` con ingombro complessivo minore o uguale a `W`.

Questo modulo e gia integrato in `Final Prompt.md`.

## Riconoscimento

Usare quando la traccia contiene:

- piu lunga sottosequenza comune;
- ingombro complessivo minore o uguale a `W`;
- funzione `w:S -> N`;
- richieste su coefficienti, caso base, ricorrenza, bottom-up e ricostruzione.

Card RAG: `10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md`.

## Risposta da copiare

```text
1)
- X_i = <x_1,...,x_i>, con 0 <= i <= m.
- Y_j = <y_1,...,y_j>, con 0 <= j <= n.
- C[i,j,k] = lunghezza di una LCS di X_i e Y_j con ingombro <= k, con 0 <= k <= W.

2)
- C[0,j,k] = 0 per ogni j,k.
- C[i,0,k] = 0 per ogni i,k.

3)
Per i>0, j>0, 0 <= k <= W:

- Se x_i != y_j:
  C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])

- Se x_i = y_j e w(x_i) <= k:
  C[i,j,k] = max(
    C[i-1,j,k],
    C[i,j-1,k],
    1 + C[i-1,j-1,k-w(x_i)]
  )

- Se x_i = y_j e w(x_i) > k:
  C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])

4)
C[m,n,W]

5)
LCS-INGOMBRO(X, Y, W)
    m = length(X)
    n = length(Y)

    for k = 0 to W
        for j = 0 to n
            C[0,j,k] = 0
        for i = 0 to m
            C[i,0,k] = 0

    for i = 1 to m
        for j = 1 to n
            for k = 0 to W
                if x_i != y_j then
                    C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])
                else
                    if w(x_i) <= k then
                        C[i,j,k] = max(C[i-1,j,k],
                                        C[i,j-1,k],
                                        1 + C[i-1,j-1,k-w(x_i)])
                    else
                        C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])

    return C

6)
STAMPA-LCS-INGOMBRO(C, X, Y, i, j, k)
    if i = 0 then
        return
    if j = 0 then
        return

    if x_i != y_j then
        if C[i,j,k] = C[i-1,j,k] then
            STAMPA-LCS-INGOMBRO(C, X, Y, i-1, j, k)
        else
            STAMPA-LCS-INGOMBRO(C, X, Y, i, j-1, k)
    else
        if w(x_i) <= k and C[i,j,k] = 1 + C[i-1,j-1,k-w(x_i)] then
            STAMPA-LCS-INGOMBRO(C, X, Y, i-1, j-1, k-w(x_i))
            print x_i
        else
            if C[i,j,k] = C[i-1,j,k] then
                STAMPA-LCS-INGOMBRO(C, X, Y, i-1, j, k)
            else
                STAMPA-LCS-INGOMBRO(C, X, Y, i, j-1, k)
```

## Accortezze

- Non usare la variante "ingombro esattamente b" come default.
- Non usare `-infinito` nei casi base.
- La cella finale e `C[m,n,W]`.
- Se viene chiesta la complessita: tempo `O(mnW)`, spazio `O(mnW)`.
