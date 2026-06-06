---
type: method
status: scaffold
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/vincoli-di-conteggio
  - topic/colori
---

# Metodo - LCS con vincoli sui colori

## Quando si usa

Quando si cerca una sottosequenza comune massima tra due sequenze, ma la soluzione deve rispettare vincoli sul numero di simboli di certi colori.

## Stato tipico

Un possibile stato per due sequenze è:

$$
c_{i,j,r,b}
$$

dove:

- $i$ e $j$ indicano i prefissi delle due sequenze;
- $r$ e il numero massimo di simboli rossi utilizzabili;
- $b$ e il numero massimo di simboli blu utilizzabili.

Nel caso di tre sequenze (vedi [[exam_2025_02_11_p1_completo_e01]]), lo stato si estende aggiungendo un terzo indice di prefisso $k$:

$$
c_{i,j,k,r}
$$

## Caso ufficiale: LCS(X,Y,3) con al massimo 3 rossi

Fonte ufficiale: `SRC-LECTURE-001`, PDF `lcs_atmost_red-13ott25.pdf`.

Da usare quando la traccia chiede esplicitamente `LCS(X,Y,3)` o "al massimo 3 elementi rossi".

Siano:

$$
X=\langle x_1,\ldots,x_m\rangle,\qquad Y=\langle y_1,\ldots,y_n\rangle.
$$

Sia:

$$
col:\Sigma\to\{red, black\}.
$$

Sottoproblema:

$$
LCS(X_i,Y_j,r)
$$

dove `r` e il numero massimo di elementi rossi ammessi.

Coefficiente:

$$
c_{i,j,r}=\text{lunghezza di una LCS tra }X_i,Y_j\text{ con al massimo }r\text{ rossi}.
$$

Valore ottimo:

$$
c_{m,n,3}.
$$

Pseudocodice bottom-up essenziale:

```text
LCS-MAX-3-ROSSI(X,Y,col)
    for i = 0 to m
        for r = 0 to 3
            c[i,0,r] = 0
    for j = 0 to n
        for r = 0 to 3
            c[0,j,r] = 0

    for i = 1 to m
        for j = 1 to n
            for r = 0 to 3
                if x_i != y_j then
                    c[i,j,r] = max(c[i-1,j,r], c[i,j-1,r])
                else
                    if col(x_i) != red then
                        c[i,j,r] = c[i-1,j-1,r] + 1
                    else
                        if r = 0 then
                            c[i,j,r] = c[i-1,j-1,r]
                        else
                            c[i,j,r] = c[i-1,j-1,r-1] + 1

    return c[m,n,3]
```

## Soluzione finale tipica

Per il caso dell'appello 2025-06-09:

$$
c_{m,n,2,3}
$$

Per il caso dell'appello 2025-11-10 (presenza obbligatoria, stato booleano):

$$
c_{m,n,1}
$$

Per il caso dell'appello 2025-01-13 (al massimo 3 rossi e al massimo 2 blu):

$$
c_{m,n,3,2}
$$

## Esercizi collegati

- [[exam_2025_06_09_p1_e01]]
- [[exam_2025_07_03_p1_e01]]
- [[exam_2025_11_10_p1_tema_a_e01]]
- [[exam_2025_02_11_p1_completo_e01]]
- [[exam_2025_02_11_p1_recupero_e01]]
- [[exam_2025_01_13_p1_e01]]
- [[exam_2025_09_17_p1_e01]]

## Teoria necessaria

- [[programmazione_dinamica]]
- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]

## Errori comuni

- Dimenticare di diminuire il contatore corretto quando si sceglie un simbolo rosso o blu.
- Diminuire un contatore quando il simbolo e nero.
- Trattare come scegliibile un simbolo se $x_i \ne y_j$.
- Ricostruire la soluzione senza verificare quale caso della ricorrenza ha prodotto il massimo.

> [!Warning]
> Metodo da completare durante la fase di soluzione.

## Integrazione da SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 04-10.

### Esattamente $R$ rossi

Per imporre esattamente $R$ simboli rossi nella LCS:

$$
C_{i,j,r} = \text{lunghezza di una LCS tra } X_i,Y_j \text{ con esattamente } r \text{ rossi}.
$$

Caso base:

$$
C_{0,j,0}=C_{i,0,0}=0,\qquad C_{0,j,r}=C_{i,0,r}=-\infty \text{ per } r>0.
$$

Passo chiave:

$$
C_{i,j,r} =
\begin{cases}
\max(C_{i-1,j,r}, C_{i,j-1,r}) & \text{se } x_i \ne y_j,\\
\max(C_{i-1,j,r}, C_{i,j-1,r}, C_{i-1,j-1,r-1}+1) & \text{se } x_i=y_j,\ col(x_i)=rosso,\ r>0,\\
\max(C_{i-1,j,r}, C_{i,j-1,r}) & \text{se } x_i=y_j,\ col(x_i)=rosso,\ r=0,\\
\max(C_{i-1,j,r}, C_{i,j-1,r}, C_{i-1,j-1,r}+1) & \text{se } x_i=y_j,\ col(x_i)\ne rosso.
\end{cases}
$$

### Quantificatore: tutte le LCS

> [!Warning]
> Non confondere "esiste una LCS con proprieta $P$" con "tutte le LCS hanno proprieta $P$".

Per proprieta su tutte le LCS ottime conviene calcolare prima la tabella delle lunghezze standard $L_{i,j}$. Nel mismatch si ereditano solo i rami che producono la lunghezza ottima:

- se un solo ramo e ottimo, si eredita quel ramo;
- se entrambi i rami sono ottimi, si usa AND.

Per "tutte le LCS hanno almeno $R$ rossi":

$$
B_{i,j,r}=true
$$

se tutte le LCS di $X_i,Y_j$ contengono almeno $r$ rossi.

Per "tutte le LCS hanno parita $p$ di rossi", uso convenzione:

$$
p=0 \text{ pari},\qquad p=1 \text{ dispari}.
$$

> [!Todo]
> Verificare manualmente la convenzione di parita nelle pagine 08-10 della fonte.

### Esempi collegati

- [[lcs_esattamente_3_rossi_SRC_EXTRA_001]]
- [[lcs_tutte_almeno_3_rossi_SRC_EXTRA_001]]
- [[lcs_tutte_parita_rossi_SRC_EXTRA_001]]
