# LCS con presenza di almeno un simbolo rosso

## Pattern

Colori possibili: `{R,B,N}`.

Vincolo: almeno un simbolo rosso nella sottosequenza comune.

## Definizione corretta dell'indicatore

```text
rho(a)=1 se a e rosso
rho(a)=0 altrimenti
```

Equivalente:

```text
rho(a)=1 se a e rosso
rho(a)=0 se a e blu o nero
```

Nota da esame: non serve distinguere blu e nero nello stato, perche il vincolo riguarda solo il rosso.

## Stato minimo

```text
C[i,j,r] = lunghezza massima di una sottosequenza comune tra X[1..i] e Y[1..j]
con requisito residuo r sulla presenza del rosso, r in {0,1}.
```

## Casi base

```text
C[0,j,0]=C[i,0,0]=0
C[0,j,1]=C[i,0,1]=-infinito
```

## Ricorrenza

```text
Se x_i != y_j:
  C[i,j,r] = max{C[i-1,j,r], C[i,j-1,r]}

Se x_i = y_j = a:
  C[i,j,r] = max{
    C[i-1,j,r],
    C[i,j-1,r],
    1 + C[i-1,j-1,max(0,r-rho(a))]
  }
```

## Soluzione

```text
C[m,n,1]
```

## Errore da evitare

Non scrivere:

```text
rho(a)=0 se a e blu
```

se la traccia ammette anche il colore nero.
