# Esempio svolto - LCS con ingombro complessivo <= W

## Traccia tipo

Date due sequenze `X` e `Y` su un alfabeto `Sigma`. Ogni simbolo `a` ha ingombro `w(a)`.

Determinare una piu lunga sottosequenza comune tra `X` e `Y` con ingombro complessivo `<= W`.

## Parole chiave

```text
ingombro complessivo <= W
```

Significa somma dei pesi dei simboli scelti, non monotonia dei pesi.

## Errore frequente

Sbagliato:

```text
w(prev) <= w(curr)
```

Corretto:

```text
p -> p-w(a)
```

## Soluzione da esame

### Coefficienti

```text
C[i,j,p] = lunghezza massima di una sottosequenza comune tra X[1..i] e Y[1..j]
con ingombro complessivo al piu p.

i=0,...,m; j=0,...,n; p=0,...,W.
```

### Caso base

```text
C[0,j,p]=0 per ogni j,p
C[i,0,p]=0 per ogni i,p
```

Con una sequenza vuota non si puo prendere alcun simbolo.

### Passo ricorsivo

Per `i,j>0` e `p=0,...,W`.

```text
Se x_i != y_j:
  C[i,j,p] = max{C[i-1,j,p], C[i,j-1,p]}

Se x_i = y_j = a:
  C[i,j,p] = max{C[i-1,j,p], C[i,j-1,p]}
  se p >= w(a):
    C[i,j,p] = max{C[i,j,p], 1 + C[i-1,j-1,p-w(a)]}
```

### Soluzione

```text
C[m,n,W]
```

## Pseudocodice bottom-up

```text
LCS-BUDGET(X,Y,W):
  for j=0..n:
    for p=0..W:
      C[0,j,p]=0

  for i=0..m:
    for p=0..W:
      C[i,0,p]=0

  for i=1..m:
    for j=1..n:
      for p=0..W:
        if X[i] != Y[j]:
          C[i,j,p]=max(C[i-1,j,p], C[i,j-1,p])
        else:
          a=X[i]
          C[i,j,p]=max(C[i-1,j,p], C[i,j-1,p])
          if p >= w(a):
            C[i,j,p]=max(C[i,j,p], 1+C[i-1,j-1,p-w(a)])

  return C[m,n,W]
```

## Stampa ricorsiva

```text
STAMPA(i,j,p):
  if i==0 or j==0:
    return

  if C[i,j,p] == C[i-1,j,p]:
    STAMPA(i-1,j,p)

  else if C[i,j,p] == C[i,j-1,p]:
    STAMPA(i,j-1,p)

  else:
    STAMPA(i-1,j-1,p-w(X[i]))
    stampa X[i]
```

Chiamata:

```text
STAMPA(m,n,W)
```

## Complessita

```text
Tempo: O(m*n*W)
Spazio: O(m*n*W)
```

La stampa richiede `O(m+n)` se si segue la tabella.

## Checklist finale

- [ ] Lo stato contiene il budget `p=0,...,W`.
- [ ] Il ramo "prendo" consuma `w(a)`.
- [ ] La soluzione finale e `C[m,n,W]`.
- [ ] Non compare `w(prev)<=w(curr)` se la traccia non chiede monotonia.
