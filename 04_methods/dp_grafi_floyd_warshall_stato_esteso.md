---
type: method
status: complete_with_warnings
source_id: SRC-NOTE-001
tags: [apa, metodo, programmazione-dinamica, grafi, floyd-warshall]
---

# DP su grafi con vertici intermedi e stato esteso

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 23-32.

## Quando riconoscerla

L'esercizio chiede esistenza, conteggio, parita o costo di cammini in un grafo, con vincoli su colori di archi/vertici o su coppie consecutive.

## Schema del sottoproblema

$$
D^k[i,j,\sigma]=true
$$

sse esiste un cammino da $i$ a $j$ che usa solo vertici intermedi in $\{1,\dots,k\}$ e soddisfa lo stato aggiuntivo $\sigma$.

## Significato di k

$k$ non e la lunghezza del cammino: indica quali vertici intermedi sono autorizzati.

## Caso base k = 0

Si considerano solo archi diretti $(i,j)$, inizializzando lo stato aggiuntivo in base al colore/peso/proprieta dell'arco.

## Passo ricorsivo: il cammino passa o non passa da k

$$
D^k[i,j,\sigma]=
D^{k-1}[i,j,\sigma]\lor
\bigvee_{\sigma_1\oplus\sigma_2=\sigma}
\left(D^{k-1}[i,k,\sigma_1]\land D^{k-1}[k,j,\sigma_2]\right).
$$

## Come inserire vincoli sui colori

- Conteggio: aggiungere dimensioni $r,b,\dots$.
- Parita: aggiungere $p\in\{0,1\}$.
- Consecutivita vietate: salvare colore del primo e dell'ultimo arco del cammino.
- Coppie uguali: aggiungere un contatore e controllare il colore al punto di concatenazione.

## Come leggere la soluzione finale

Di solito si legge $D^n[s,t,\sigma]$ oppure un OR/minimo sui possibili stati finali ammessi.

## Errori comuni

- Confondere $k$ con il numero di archi.
- Dimenticare il caso "non passa da $k$".
- Concatenare due cammini senza aggiornare lo stato extra.
- Non controllare il vincolo al punto di giunzione.

