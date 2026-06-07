---
type: method
status: official_confirmed_with_notes
source_id: SRC-NOTE-001
official_confirmation: SRC-LECTURE-001
tags: [apa, metodo, programmazione-dinamica, lcs, colori]
---

# DP - LCS con vincoli di colore

## Fonti

- `SRC-NOTE-001`: appunti compagna, fonte precedente.
- `SRC-EXTRA-001`: esercizi/appunti extra, fonte precedente.
- `SRC-LECTURE-001`: PDF ufficiale `lcs_atmost_red-13ott25.pdf`, conferma/corregge la variante "al massimo k rossi".

## Regola: colore richiesto vs colori presenti

Se la traccia definisce `col:S->{R,B,N}` ma il vincolo riguarda solo il rosso, lo stato deve ricordare solo il requisito sul rosso.

Indicatore corretto:

```text
rho(a)=1 se a e rosso
rho(a)=0 altrimenti
```

oppure, esplicitando il codominio:

```text
rho(a)=1 se a e rosso
rho(a)=0 se a e blu o nero
```

Non scrivere solo `rho(a)=0 se a e blu` quando il nero e ammesso. Blu e nero sono entrambi non-rossi per questo vincolo. Non aggiungere contatori/flag separati per blu o nero salvo richiesta esplicita.

## Variante ufficiale del professore: al massimo K rossi

Fonte primaria per tracce del tipo `LCS(X,Y,3)` o "al massimo 3 elementi rossi".

$$
C[i,j,r]=\text{lunghezza di una LCS tra }X_i,Y_j\text{ con al massimo }r\text{ rossi}.
$$

Il valore ottimo e:

$$
C[m,n,K].
$$

Nel PDF ufficiale `K=3`, quindi il valore ottimo e `C[m,n,3]`.

Casi base:

$$
C[0,j,r]=C[i,0,r]=0 \qquad \forall r\ge 0.
$$

Passo ricorsivo:

$$
C[i,j,r]=
\begin{cases}
\max(C[i-1,j,r],C[i,j-1,r]) & \text{se } x_i\ne y_j,\\
C[i-1,j-1,r]+1 & \text{se } x_i=y_j,\ col(x_i)\ne rosso,\\
C[i-1,j-1,r] & \text{se } x_i=y_j,\ col(x_i)=rosso,\ r=0,\\
C[i-1,j-1,r-1]+1 & \text{se } x_i=y_j,\ col(x_i)=rosso,\ r>0.
\end{cases}
$$

Per `K=3`, il numero totale di stati e `(m+1)(n+1)(3+1)`.

Complessita:

- tempo `O(mnK)`, quindi `O(mn)` per `K=3` fissato;
- spazio `O(mnK)` se serve ricostruire.

Ricostruzione: seguire i predecessori o confrontare le celle. Decrementare `r` solo quando si stampa/prende un simbolo rosso.

> [!Info]
> La formulazione robusta con `max` anche nei casi di match resta utile per appelli generici. Quando la traccia segue la notazione ufficiale del professore, usare pero questa sezione come fonte primaria.

## Variante: al massimo K rossi

$$
C[i,j,k]=\text{lunghezza di una LCS tra }X_i,Y_j\text{ con al massimo }k\text{ rossi}.
$$

Caso base: $C[0,j,k]=C[i,0,k]=0$.

Se $x_i=y_j$ e $col(x_i)=rosso$:

$$
C[i,j,k]=
\begin{cases}
\max(C[i-1,j,k],C[i,j-1,k],C[i-1,j-1,k-1]+1) & k>0,\\
\max(C[i-1,j,k],C[i,j-1,k]) & k=0.
\end{cases}
$$

Se $x_i=y_j$ non rosso:

$$
C[i,j,k]=\max(C[i-1,j,k],C[i,j-1,k],C[i-1,j-1,k]+1).
$$

Se $x_i\ne y_j$:

$$
C[i,j,k]=\max(C[i-1,j,k],C[i,j-1,k]).
$$

## Variante: esattamente K rossi

Stesso stato, ma il caso base cambia:

$$
C[0,j,0]=C[i,0,0]=0,\qquad C[0,j,k]=C[i,0,k]=-\infty\text{ per }k>0.
$$

## Variante: tutte le LCS hanno numero pari di rossi

Calcolare prima la lunghezza ottima $L[i,j]$. Poi usare uno stato booleano:

$$
B[i,j,p]=true
$$

sse tutte le LCS ottime di $X_i,Y_j$ hanno parita $p$ di rossi, con $p=0$ pari e $p=1$ dispari.

> [!Warning]
> Le convenzioni di parita negli appunti e in SRC-EXTRA-001 vanno verificate manualmente prima di fissare una soluzione ufficiale.

## Variante: costruire/stampare una soluzione

Memorizzare un predecessore per ogni cella che realizza il massimo. Durante la stampa:

- se il predecessore e diagonale e il simbolo e stato preso, stampare/appendere $x_i$;
- scalare il contatore colore se il simbolo preso ha quel colore;
- altrimenti seguire il ramo sopra/sinistra.

## Caso base: quando usare 0, false, -infinito

| Variante | Stato aggiuntivo | Tipo coefficiente | Caso base | Soluzione |
|---|---|---|---|---|
| al massimo K rossi | $k$ residuo | lunghezza | $0$ | $C[m,n,K]$ |
| esattamente K rossi | $k$ residuo | lunghezza | $0$ se $k=0$, $-\infty$ se $k>0$ | $C[m,n,K]$ |
| parita rossi | $p\in\{0,1\}$ | booleano/lunghezza | dipende dalla consegna | $B[m,n,p]$ |

## Collegamenti

- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[lcs_al_massimo_k_rossi_SRC_NOTE_001]]
- [[lcs_esattamente_k_rossi_SRC_NOTE_001]]
