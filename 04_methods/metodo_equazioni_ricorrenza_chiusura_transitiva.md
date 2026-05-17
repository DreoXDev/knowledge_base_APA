---
type: method
topic: Chiusura transitiva recurrence
status: draft
tags:
  - apa
  - metodo
  - topic/programmazione_dinamica
  - topic/grafi
  - topic/chiusura_transitiva
  - topic/floyd_warshall
---

# Metodo - Equazioni di Ricorrenza per la Chiusura Transitiva

## Quando si usa

Questo metodo si applica quando viene richiesto di scrivere le equazioni di ricorrenza (caso base e passo ricorsivo) per la chiusura transitiva o riflessiva-transitiva di un grafo $G=(V,E)$ usando la programmazione dinamica (algoritmo di Warshall, derivazione di Floyd-Warshall).

## Riconoscimento rapido

> [!Info]
> Segnali che indicano che questo esercizio usa questo metodo:
> - Richiesta di scrivere le equazioni usando il coefficiente $e_{i,j}^{(k)}$ (o simile).
> - Richiesta esplicita di spiegare il significato matematico del parametro $k$ che appare all'esponente o come pedice.

## Definizione del Significato di $k$

Il parametro $k \in \{0, 1, \dots, n\}$ rappresenta il **limite superiore sull'indice dei vertici intermedi** ammissibili nel cammino. 
Più precisamente, $e_{i,j}^{(k)} = 1$ (o *vero*) se e solo se esiste un cammino dal vertice $i$ al vertice $j$ tale che tutti i vertici intermedi appartengono all'insieme $\{1, 2, \dots, k\}$.
- Per $k=0$, non sono ammessi vertici intermedi (sono consentiti solo archi diretti o il cammino vuoto).
- Per $k=n$, i vertici intermedi possono essere qualsiasi nodo del grafo (chiusura transitiva completa).

## Equazioni di Ricorrenza

### Chiusura Transitiva (Riflessiva-Transitiva)

#### Caso Base: $k = 0$
Per ogni coppia $i, j \in V$:
$$
e_{i,j}^{(0)} = 
\begin{cases}
1 & \text{se } i = j \text{ oppure } (i,j) \in E \\
0 & \text{altrimenti}
\end{cases}
$$
*(Nota: se si richiede la chiusura transitiva non riflessiva, per $i=j$ il valore è $1$ solo se è presente un self-loop $(i,i) \in E$, ma negli esercizi d'esame si assume quasi sempre la versione riflessiva-transitiva).*

#### Passo Ricorsivo: $k \ge 1$
Per ogni $i, j \in V$:
$$
e_{i,j}^{(k)} = e_{i,j}^{(k-1)} \lor \left( e_{i,k}^{(k-1)} \land e_{k,j}^{(k-1)} \right)
$$

## Esercizi collegati

- [[exam_2025_07_03_p2_e03]]
- [[exam_2025_11_10_p2_e03]]
- [[exam_2025_01_13_p1_e02]] (collegato per stato esteso su grafi)
- [[exam_2025_09_17_p1_e02]] (parità blu su grafi)

## Errori comuni

> [!Warning]
> Dimenticare di definire il caso base riflessivo ($i = j$) se richiesto.
> Spiegare in modo errato il parametro $k$, per esempio dicendo che indica la "lunghezza massima" del cammino o "il numero di archi". $k$ rappresenta l'indice del massimo vertice intermedio consentito, NON la lunghezza del cammino.
