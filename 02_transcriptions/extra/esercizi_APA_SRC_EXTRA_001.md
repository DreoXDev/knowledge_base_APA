---
source_id: SRC-EXTRA-001
source_file: esercizi APA.pdf
source_type: handwritten_exercises
status: transcribed_with_warnings
priority: high
tags:
  - apa
  - trascrizione
  - source/SRC-EXTRA-001
  - topic/programmazione-dinamica
---

# Trascrizione - esercizi APA

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf

> [!Warning]
> La fonte e manoscritta. La trascrizione sotto combina lettura diretta/OCR e normalizzazione controllata. Le parti non pienamente leggibili sono marcate come warning o todo e non vanno considerate formule ufficiali senza verifica manuale.

## Pagina 01 - LCS crescente e LDS

> [!Info] Fonte
> SRC-EXTRA-001, pagina 01.

### Trascrizione fedele

- Considero due sequenze $X$ e $Y$.
- $C_{i,j}$: lunghezza di una tra le piu lunghe sottosequenze crescenti comuni tra $X_i$ e $Y_j$.
- Equazioni di ricorrenza.
- Caso base indicato per indici iniziali.
- Passo ricorsivo con vincolo $x_i = y_j$ e massimo sui predecessori.
- LDS: longest decreasing subsequence tra $X$ e $Y$.
- Siano $X$ e $Y$ sequenze di lunghezza $m$ e $n$: trovare la sottosequenza comune piu lunga e decrescente.

### Interpretazione normalizzata

La pagina introduce la variante LICS/LCS crescente:

$$
C_{i,j} = \text{lunghezza di una LICS tra } X_i \text{ e } Y_j \text{ che termina nel match } x_i=y_j.
$$

Una forma sicura, coerente con la pagina 15, e:

$$
C_{i,j} =
\begin{cases}
0 & \text{se } x_i \ne y_j,\\
1 + \max\{C_{h,k} \mid h<i,\ k<j,\ x_h<x_i\} & \text{se } x_i=y_j.
\end{cases}
$$

Per LDS il vincolo di crescita si inverte:

$$
x_h > x_i
$$

nel passaggio verso una sottosequenza decrescente.

### Punti dubbi

> [!Warning]
> La ricorrenza manoscritta della prima pagina e poco leggibile; la forma sopra e normalizzata usando la pagina 15 e il pattern LIS/LICS.

## Pagina 02 - LIS

> [!Info] Fonte
> SRC-EXTRA-001, pagina 02.

### Trascrizione fedele

- Istanza: $X_m=\langle x_1,\dots,x_m\rangle$.
- Soluzione: una tra le sottosequenze piu lunghe crescenti di $X_m$.
- Sottoproblema $i$: considero $C_i$, la lunghezza di una LIS che termina in $x_i$.
- Caso base: $C_1=1$.
- Passo ricorsivo: massimo sui predecessori $h<i$ con $x_h<x_i$.
- Algoritmo bottom-up con vettore $C$ e vettore predecessori $b$.

### Interpretazione normalizzata

$$
C_i = 1 + \max\{C_h \mid 1 \le h < i,\ x_h < x_i\}
$$

con massimo vuoto uguale a $0$. La soluzione e:

$$
\max_{1\le i\le m} C_i.
$$

Il vettore $b$ memorizza l'indice $h$ che realizza il massimo, cosi da ricostruire la LIS risalendo dai predecessori.

### Punti dubbi

> [!Warning]
> L'OCR non legge tutti i dettagli dello pseudocodice, ma sono riconoscibili ciclo esterno su $i$, ciclo interno su $h<i$, confronto $x_h<x_i$, aggiornamento di `tmp`, `ind`, `C[i]` e `b[i]`.

## Pagina 03 - LCS base

> [!Info] Fonte
> SRC-EXTRA-001, pagina 03.

### Trascrizione fedele

- Caso base: se $i=0$ oppure $j=0$, $C_{i,j}=0$.
- Passo ricorsivo:
  - se $x_i \ne y_j$, $C_{i,j}=\max(C_{i-1,j}, C_{i,j-1})$;
  - se $x_i=y_j$, $C_{i,j}=C_{i-1,j-1}+1$.
- Algoritmo bottom-up.
- Soluzione: $C_{m,n}$.

### Interpretazione normalizzata

$$
C_{i,j} =
\begin{cases}
0 & \text{se } i=0 \text{ oppure } j=0,\\
\max(C_{i-1,j}, C_{i,j-1}) & \text{se } x_i \ne y_j,\\
C_{i-1,j-1}+1 & \text{se } x_i=y_j.
\end{cases}
$$

### Punti dubbi

Nessun dubbio sostanziale: e la ricorrenza LCS standard.

## Pagine 04-06 - LCS con esattamente 3 rossi

> [!Info] Fonte
> SRC-EXTRA-001, pagine 04-06.

### Trascrizione fedele

- Calcolare la lunghezza di una piu lunga sottosequenza comune di $X$ e $Y$ con esattamente 3 rossi.
- Sottoproblema $(i,j,r)$.
- $C_{i,j,r}$: lunghezza di una LCS tra $X_i$ e $Y_j$ con esattamente $r$ rossi.
- $r \in \{0,\dots,R\}$, nel caso $R=3$.
- Caso base: per sequenze vuote si ha valore $0$ se $r=0$, valore impossibile se $r>0$.
- Passo ricorsivo:
  - se $x_i \ne y_j$, massimo tra rami senza prendere il match;
  - se $x_i=y_j$ e il simbolo e rosso, decremento del contatore dei rossi;
  - se $x_i=y_j$ e il simbolo non e rosso, non decremento $r$.
- Algoritmo bottom-up con cicli su $i,j,r$.
- Soluzione: $C_{m,n,3}$.

### Interpretazione normalizzata

Caso base:

$$
C_{0,j,0}=C_{i,0,0}=0,\qquad
C_{0,j,r}=C_{i,0,r}=-\infty \text{ per } r>0.
$$

Passo:

$$
C_{i,j,r} =
\begin{cases}
\max(C_{i-1,j,r}, C_{i,j-1,r}) & \text{se } x_i \ne y_j,\\
\max(C_{i-1,j,r}, C_{i,j-1,r}, C_{i-1,j-1,r-1}+1) & \text{se } x_i=y_j,\ col(x_i)=rosso,\ r>0,\\
\max(C_{i-1,j,r}, C_{i,j-1,r}) & \text{se } x_i=y_j,\ col(x_i)=rosso,\ r=0,\\
\max(C_{i-1,j,r}, C_{i,j-1,r}, C_{i-1,j-1,r}+1) & \text{se } x_i=y_j,\ col(x_i)\ne rosso.
\end{cases}
$$

### Punti dubbi

> [!Warning]
> Le pagine 04 e 06 sembrano due stesure dello stesso esercizio. La nota lavorata deduplica lo schema, ma la trascrizione conserva il riferimento a entrambe.

## Pagina 07 - Tutte le LCS hanno almeno 3 rossi

> [!Info] Fonte
> SRC-EXTRA-001, pagina 07.

### Trascrizione fedele

- Date due sequenze $X$ e $Y$ con colore associato a ogni simbolo, stabilire se tutte le LCS di $X$ e $Y$ hanno almeno 3 simboli rossi.
- Attenzione evidenziata: tutte le LCS, non esiste una LCS.
- Coefficienti booleani $C_{i,j,r}$.
- Caso base: $r=0$ true; $r>0$ false.
- In caso di mismatch, la fonte annota AND perche si chiedono tutte le LCS.

### Interpretazione normalizzata

Serve prima la tabella delle lunghezze LCS standard $L_{i,j}$. Poi:

$$
B_{i,j,r} = true
$$

se tutte le LCS ottime di $X_i$ e $Y_j$ contengono almeno $r$ rossi.

Base:

$$
B_{i,j,0}=true,\qquad B_{0,j,r}=B_{i,0,r}=false \text{ per } r>0.
$$

Nel mismatch si considerano solo i rami che mantengono la lunghezza ottima:

- se $L_{i-1,j}>L_{i,j-1}$, eredito $B_{i-1,j,r}$;
- se $L_{i-1,j}<L_{i,j-1}$, eredito $B_{i,j-1,r}$;
- se sono uguali, uso AND tra i due rami.

### Punti dubbi

> [!Warning]
> La fonte mostra l'idea dell'AND, ma non esplicita sempre il filtro sui soli rami ottimi. Senza quel filtro si rischia di ragionare su sottosequenze non LCS.

## Pagine 08-10 - Tutte le LCS hanno numero pari di rossi

> [!Info] Fonte
> SRC-EXTRA-001, pagine 08-10.

### Trascrizione fedele

- Date due sequenze $X$ e $Y$, stabilire se tutte le LCS hanno un numero pari di simboli rossi.
- Stato booleano con parametro di parita.
- La pagina distingue i casi $x_i \ne y_j$, $x_i=y_j$ rosso, $x_i=y_j$ non rosso.
- Quando i due rami di mismatch sono entrambi ottimi, serve combinare con AND.

### Interpretazione normalizzata

Uso convenzione:

$$
p=0 \text{ pari},\qquad p=1 \text{ dispari}.
$$

$$
B_{i,j,p}=true
$$

se tutte le LCS ottime di $X_i,Y_j$ hanno parita $p$ del numero di rossi.

Se $x_i=y_j$ e il simbolo e rosso, la parita si inverte:

$$
B_{i,j,p}=B_{i-1,j-1,1-p}.
$$

Se il simbolo non e rosso:

$$
B_{i,j,p}=B_{i-1,j-1,p}.
$$

Nei mismatch si ereditano solo i rami ottimi e si usa AND quando entrambi hanno lunghezza ottima.

### Punti dubbi

> [!Warning]
> Le pagine 08-10 sembrano usare convenzioni non sempre uniformi per la parita. Questa trascrizione normalizza a $p=0$ pari e $p=1$ dispari.

> [!Todo]
> Verificare manualmente se la fonte intende $p$ come parita richiesta oppure come parita residua.

## Pagina 11 - LCS con ingombro complessivo al massimo C

> [!Info] Fonte
> SRC-EXTRA-001, pagina 11.

### Trascrizione fedele

- Date due sequenze $X$ e $Y$, stabilire una piu lunga sottosequenza comune di ingombro complessivo $\le C$.
- Sottoproblema $(i,j,c)$.
- $L_{i,j,c}$: lunghezza di una piu lunga sottosequenza comune di $X_i$ e $Y_j$ con ingombro complessivo al massimo $c$.
- Caso base: indice zero.
- Se $x_i \ne y_j$, massimo tra $L_{i-1,j,c}$ e $L_{i,j-1,c}$.
- Se $x_i=y_j$ e $w(x_i)\le c$, confronto con presa del simbolo.

### Interpretazione normalizzata

$$
L_{i,j,c} =
\begin{cases}
0 & \text{se } i=0 \text{ oppure } j=0,\\
\max(L_{i-1,j,c},L_{i,j-1,c}) & \text{se } x_i \ne y_j,\\
\max(L_{i-1,j,c},L_{i,j-1,c},L_{i-1,j-1,c-w(x_i)}+1) & \text{se } x_i=y_j,\ w(x_i)\le c,\\
\max(L_{i-1,j,c},L_{i,j-1,c}) & \text{se } x_i=y_j,\ w(x_i)>c.
\end{cases}
$$

### Punti dubbi

> [!Warning]
> La fonte sembra anche usare una forma piu compatta nel caso di match; la forma sopra conserva in modo sicuro anche la possibilita di non prendere il match.

## Pagina 12 - Hateville senza due rossi consecutivi

> [!Info] Fonte
> SRC-EXTRA-001, pagina 12.

### Trascrizione fedele

- Hateville senza due rossi consecutivi.
- Istanza: abitanti/case $1,\dots,n$; donazione $d_i$; colore della casa $col(i)$.
- Soluzione: sottoinsieme ammissibile di case con massima donazione.
- Vincolo: non scegliere due case rosse consecutive.
- Sottoproblema sui primi $i$ elementi.
- $OPT_i$ e indicato come valore massimo.
- Casi base per $i=0,1,2$.

### Interpretazione normalizzata

Il metodo certo e:

$$
OPT_i = \max\{D(A)\mid A\subseteq \{1,\dots,i\},\ A \text{ ammissibile}\}.
$$

Per una ricorrenza completa bisogna conoscere con precisione se "consecutivi" significa case adiacenti scelte entrambe rosse oppure due case rosse scelte consecutivamente nella soluzione. La pagina indica il primo significato, ma il passo ricorsivo non e pienamente leggibile.

### Punti dubbi

> [!Warning]
> Il passo ricorsivo di pagina 12 non e abbastanza leggibile per fissare una formula unica.

> [!Todo]
> Verificare la ricorrenza confrontando con SRC-NOTE-001 o con una derivazione separata.

## Pagine 13-14 e 16-17 - Knapsack con massimo numero di oggetti rossi

> [!Info] Fonte
> SRC-EXTRA-001, pagine 13-14 e 16-17.

### Trascrizione fedele

- Knapsack.
- Oggetti $1,\dots,n$.
- $v_i$: valore dell'oggetto $i$.
- $w_i$: ingombro dell'oggetto $i$.
- $col(i)\in\{rosso,blu\}$.
- $C$: capacita dello zaino.
- $R$: massimo numero di oggetti rossi.
- Sottoproblema $(i,c,r)$.
- $OPT_{i,c,r}$: valore massimo con primi $i$ oggetti, capacita $c$, al massimo $r$ oggetti rossi.
- Viene annotato anche l'insieme soluzione $S_{i,c,r}$ per la ricostruzione.

### Interpretazione normalizzata

Caso base:

$$
OPT_{0,c,r}=0,\qquad OPT_{i,0,r}=0.
$$

Passo:

$$
OPT_{i,c,r} =
\begin{cases}
OPT_{i-1,c,r} & \text{se } w_i>c,\\
\max(OPT_{i-1,c,r},OPT_{i-1,c-w_i,r-1}+v_i) & \text{se } w_i\le c,\ col(i)=rosso,\ r>0,\\
OPT_{i-1,c,r} & \text{se } w_i\le c,\ col(i)=rosso,\ r=0,\\
\max(OPT_{i-1,c,r},OPT_{i-1,c-w_i,r}+v_i) & \text{se } w_i\le c,\ col(i)\ne rosso.
\end{cases}
$$

### Punti dubbi

> [!Warning]
> Le pagine 13-14 e 16-17 sono due versioni dello stesso schema. La trascrizione le mantiene aggregate e la KB lavorata le deduplica.

## Pagina 15 - LICS

> [!Info] Fonte
> SRC-EXTRA-001, pagina 15.

### Trascrizione fedele

- LICS.
- Istanza: $X=\langle x_1,\dots,x_m\rangle$, $Y=\langle y_1,\dots,y_n\rangle$.
- Soluzione: trovare LICS tra $X_m$ e $Y_n$.
- Sottoproblema $(i,j)$.
- $C_{i,j}$: lunghezza di una LICS tra $X_i$ e $Y_j$.
- Caso base: se $x_i\ne y_j$, $C_{i,j}=0$.
- Se $x_i=y_j$, massimo sui predecessori con valore minore.
- Algoritmo bottom-up con massimo globale.

### Interpretazione normalizzata

$$
C_{i,j} =
\begin{cases}
0 & \text{se } x_i \ne y_j,\\
1+\max\{C_{h,k}\mid h<i,\ k<j,\ x_h<x_i\} & \text{se } x_i=y_j.
\end{cases}
$$

Soluzione:

$$
\max_{i,j} C_{i,j}.
$$

### Punti dubbi

> [!Warning]
> L'OCR confonde alcuni indici nello pseudocodice; la struttura dei due cicli esterni e dei due cicli sui predecessori e comunque riconoscibile.

## Pagine 17-18 - LCS con alternanza pari/dispari

> [!Info] Fonte
> SRC-EXTRA-001, pagine 17-18.

### Trascrizione fedele

- LCS in cui si alternano pari e dispari.
- Sottoproblema: stabilisco $C_{i,j}$, lunghezza di una LCS di $X_i$ e $Y_j$ in cui si alternano pari e dispari.
- Caso base: $i=0$ oppure $j=0$.
- Passo ricorsivo:
  - se $x_i\ne y_j$, massimo tra $C_{i-1,j}$ e $C_{i,j-1}$;
  - se $x_i=y_j$, compare un massimo sui predecessori con controllo di parita opposta.

### Interpretazione normalizzata

La ricorrenza richiede uno stato che ricordi la parita dell'ultimo elemento scelto oppure una definizione "termina in $x_i=y_j$":

$$
C_{i,j,p} = \text{lunghezza di una LCS alternante di } X_i,Y_j \text{ che termina con parita } p.
$$

### Punti dubbi

> [!Warning]
> La fonte non e completa/leggibile abbastanza per fissare il metodo. La nota collegata resta in stato draft.

> [!Todo]
> Verificare su SRC-NOTE-001 o completare con derivazione separata prima di usare questa ricorrenza in un esercizio.
