---
type: method
status: complete
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, sequenze]
---

# DP - Interleaving di sequenze

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 4-5.

## Quando riconoscerla

La consegna chiede se una sequenza $W$ puo essere ottenuta intrecciando due sequenze $X$ e $Y$ mantenendo l'ordine interno di entrambe.

## Schema risolutivo

1. Definire $S[i,j]$.
2. Usare $W[i+j]$ come ultimo simbolo del prefisso considerato.
3. Distinguere se l'ultimo simbolo arriva da $X_i$, da $Y_j$, da entrambi o da nessuno.
4. Usare OR logico tra i casi possibili.

## Coefficiente

$$
S[i,j]=true
$$

sse $W_{i+j}$ e interleaving di $X_i$ e $Y_j$.

## Caso base

$$
S[0,0]=true.
$$

Per $i>0$:

$$
S[i,0]=S[i-1,0]\land x_i=w_i.
$$

Per $j>0$:

$$
S[0,j]=S[0,j-1]\land y_j=w_j.
$$

## Passo ricorsivo

$$
S[i,j]=(x_i=w_{i+j}\land S[i-1,j])\lor(y_j=w_{i+j}\land S[i,j-1]).
$$

## Soluzione

$$
S[m,n].
$$

## Errori comuni

- Usare $W[k]$ senza fissare $k=i+j$.
- Dimenticare i casi base sui prefissi vuoti.
- Usare AND invece di OR quando il carattere puo arrivare sia da $X$ sia da $Y$.

