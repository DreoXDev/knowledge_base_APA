# Flashcards SRC-NOTE-001

## Sottosequenza

> [!Question]
> Che cos'e una sottosequenza?

> [!Answer]
> Una sequenza ottenuta eliminando zero o piu simboli, senza cambiare l'ordine dei simboli rimasti.

## LCS

> [!Question]
> Qual e la sottostruttura ottima della LCS?

> [!Answer]
> Se $x_i=y_j$, prendo il match e guardo $C[i-1,j-1]$; se sono diversi, confronto $C[i-1,j]$ e $C[i,j-1]$.

## Meno infinito

> [!Question]
> Quando in una DP uso $-\infty$?

> [!Answer]
> Nei problemi di massimo con vincoli esatti, per marcare stati impossibili che non devono vincere un massimo.

## Rossi

> [!Question]
> Differenza tra LCS con al massimo $K$ rossi ed esattamente $K$ rossi?

> [!Answer]
> "Al massimo" usa base $0$ sui prefissi vuoti; "esattamente" usa $0$ solo per $K=0$ e $-\infty$ per $K>0$.

## Risorsa residua

> [!Question]
> Come riconoscere una DP su sequenze con risorsa residua?

> [!Answer]
> La consegna limita somma, peso, costo o budget: aggiungo una dimensione $k$ allo stato.

## LICS

> [!Question]
> Perche in LICS la risposta puo essere $\max C[i,j]$ e non $C[m,n]$?

> [!Answer]
> Perche $C[i,j]$ rappresenta soluzioni che terminano nel match $x_i=y_j$, e l'ultimo match ottimo puo trovarsi prima di $m,n$.

## Floyd-Warshall

> [!Question]
> Schema generale del Floyd-Warshall con vertici intermedi?

> [!Answer]
> $D^k[i,j]$ usa solo intermedi in $\{1,\dots,k\}$; il passo confronta non passare da $k$ con passare da $k$.

## Stato colore

> [!Question]
> Come si aggiunge uno stato colore in una DP su grafi?

> [!Answer]
> Si aggiunge una dimensione per conteggio/parita oppure si salva colore iniziale/finale se il vincolo riguarda archi consecutivi.

## NP-completezza

> [!Question]
> Cosa bisogna dimostrare per NP-completezza?

> [!Answer]
> Che il problema e in NP e che un problema NP-completo noto si riduce polinomialmente a esso.

## Dijkstra vs Floyd-Warshall

> [!Question]
> Differenza tra Dijkstra e Floyd-Warshall?

> [!Answer]
> Dijkstra calcola cammini minimi da una sorgente con pesi non negativi; Floyd-Warshall calcola cammini minimi tra tutte le coppie usando DP sui vertici intermedi.

