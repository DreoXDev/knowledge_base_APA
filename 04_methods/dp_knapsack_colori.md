---
type: method
status: complete
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, zaino-01, colori]
---

# DP - Knapsack con vincolo sui colori

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 9-10.

## Istanza

Oggetti $1,\dots,n$, valori $v_i$, pesi $w_i$, colori $col(i)$, capacita $C$, massimo numero di oggetti rossi $R$.

## Soluzione

Sottoinsieme $S$ di valore massimo con peso totale $\le C$ e al massimo $R$ oggetti rossi.

## Sottoproblema

$$
OPT[i,c,r]=\text{valore massimo usando i primi }i\text{ oggetti, capacita }c\text{ e al massimo }r\text{ rossi}.
$$

## Caso base

$$
OPT[0,c,r]=0,\qquad OPT[i,0,r]=0.
$$

## Passo ricorsivo

$$
OPT[i,c,r]=
\begin{cases}
OPT[i-1,c,r] & w_i>c,\\
\max(OPT[i-1,c,r],OPT[i-1,c-w_i,r-1]+v_i) & w_i\le c,\ col(i)=rosso,\ r>0,\\
OPT[i-1,c,r] & w_i\le c,\ col(i)=rosso,\ r=0,\\
\max(OPT[i-1,c,r],OPT[i-1,c-w_i,r]+v_i) & w_i\le c,\ col(i)\ne rosso.
\end{cases}
$$

## Soluzione

$$
OPT[n,C,R].
$$

## Ricostruzione

Confrontare $OPT[i,c,r]$ con $OPT[i-1,c,r]$. Se la cella deriva dalla presa, aggiungere $i$, ridurre $c$ di $w_i$ e ridurre $r$ solo se $i$ e rosso.

