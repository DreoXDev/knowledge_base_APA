---
type: exercise
source: 01_sources/exams_raw/parteI-11feb25-completo.pdf
source_id: SRC-EXAM-003
exam_date: 2025-02-11
part: Parte I
exercise_number: 2
points: 31
status: cataloged
difficulty: alta
tags:
  - apa
  - esercizio
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/grafi-colorati
  - topic/cammini
  - topic/dp-booleana
  - topic/problema-ausiliario
  - status/cataloged
---

# exam_2025_02_11_p1_completo_e02 — Cammini senza due neri o due blu consecutivi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_completo]]
> Stato: cataloged
> Tipologia: programmazione dinamica su grafi
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_dp_cammini_colori_precedenze]]

## Problema

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha colore rosso ($R$), nero ($N$) o blu ($B$) tramite una funzione:

$$
col:E \to \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ nel quale:

- non compaiono due archi consecutivi neri ($NN$);
- non compaiono due archi consecutivi blu ($BB$).

Gli archi rossi non presentano restrizioni di consecutività.

## Pattern riconosciuto

È una DP booleana su grafi colorati con vincolo locale di consecutività.

Il vincolo non dipende solo dalla coppia di vertici, ma anche dal colore dell'ultimo arco usato. Serve quindi uno stato esteso (problema ausiliario) che memorizzi le estremità del cammino.

## Variante consigliata robusta (Floyd-Warshall Esteso)

Per poter comporre due cammini controllando solo la compatibilità locale all'intersezione (dove si uniscono), lo stato della DP deve tenere traccia sia del colore del **primo arco** che del colore dell'**ultimo arco** del cammino.

Numerare i vertici come $V = \{1,\dots,n\}$ e definire:

$$
D[k,i,j,a,b]
$$

dove:

- $0 \le k \le n$;
- $i,j \in V$;
- $a,b \in \{R,N,B,\bot\}$ indicano rispettivamente il colore del primo e dell'ultimo arco del cammino (dove $\bot$ rappresenta il cammino vuoto privo di archi).

$D[k,i,j,a,b]$ è vero se e solo se esiste un cammino valido da $i$ a $j$, che usa come vertici intermedi solo vertici in $\{1,\dots,k\}$, il cui primo arco ha colore $a$ e l'ultimo ha colore $b$.

## Predicato di compatibilità

Definire il predicato $compatibile(c_1,c_2)$ che è vero se la giunzione di due archi di colore $c_1$ e $c_2$ è consentita.

Le coppie vietate sono $(N,N)$ e $(B,B)$. Se uno dei due colori è $\bot$, la compatibilità è sempre vera poiché non rappresenta un vero arco.

$$
compatibile(c_1,c_2) =
\begin{cases}
falso & \text{se } c_1=N \land c_2=N \\
falso & \text{se } c_1=B \land c_2=B \\
vero & \text{altrimenti}
\end{cases}
$$

## Caso base ($k=0$)

Cammino vuoto da un nodo a se stesso (lunghezza 0, nessun arco):

$$
D[0,i,i,\bot,\bot] = vero \quad \forall i \in V
$$

Arco diretto da $i$ a $j$ (se $(i,j) \in E$), con colore $c = col(i,j)$:

$$
D[0,i,j,c,c] = vero
$$

Tutti gli altri coefficienti sono inizializzati a $falso$.

## Passo ricorsivo ($k \ge 1$)

Per ricavare $D[k,i,j,a,b]$ consideriamo se il vertice $k$ viene usato o meno come nodo intermedio.

Se non viene usato, manteniamo il valore precedente. Se viene usato, combiniamo un cammino da $i$ a $k$ e un cammino da $k$ a $j$ controllando la compatibilità all'intersezione tra l'ultimo arco della prima parte ($\beta$) e il primo arco della seconda parte ($\gamma$):

$$
D[k,i,j,a,b] =
D[k-1,i,j,a,b]
\lor
\bigvee_{\alpha,\beta,\gamma,\delta}
\left(
D[k-1,i,k,\alpha,\beta]
\land
D[k-1,k,j,\gamma,\delta]
\land
compatibile(\beta,\gamma)
\land
a = \alpha'
\land
b = \delta'
\right)
$$

dove $\alpha'$ e $\delta'$ gestiscono correttamente i cammini vuoti ($\bot$):
- se il primo cammino è vuoto ($\alpha=\beta=\bot$), allora il colore iniziale del cammino composto diventa quello del secondo cammino ($\gamma$);
- analogo discorso speculare se il secondo cammino è vuoto ($\gamma=\delta=\bot$).

## Soluzione

Per ogni coppia di vertici $(i,j)$, esiste un cammino valido se e solo se esiste almeno una combinazione di colori estremi $a,b$ per cui il coefficiente finale è vero:

$$
\bigvee_{a,b \in \{R,N,B,\bot\}} D[n,i,j,a,b]
$$

## Collegamenti

- [[grafi_colorati]]
- [[metodo_dp_cammini_colori_precedenze]]
- [[parte_i_dynamic_programming_patterns]]
