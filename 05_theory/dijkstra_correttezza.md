---
type: theory
topic: Dijkstra Correctness
status: complete
tags:
  - apa
  - teoria
  - topic/grafi
  - topic/cammini_minimi
  - topic/dijkstra
---

# Teoria — Algoritmo di Dijkstra e Correttezza

## Definizione dell'Algoritmo

L'algoritmo di **Dijkstra** risolve il problema dei **cammini minimi a sorgente singola** (*Single-Source Shortest Paths - SSSP*) su un grafo orientato o non orientato $G = (V,E)$ con pesi degli archi non negativi ($w(u,v) \ge 0$ per ogni $(u,v) \in E$).

L'algoritmo mantiene un insieme $S$ di vertici per cui le distanze definitive dalla sorgente $s$ sono state già determinate. Ad ogni passo, Dijkstra estrae un nodo $u \in V \setminus S$ con la stima del cammino minimo $d[u]$ minore, lo aggiunge a $S$ e rilassa tutti gli archi uscenti da $u$.

---

## Importanza dei Pesi Non Negativi

La correttezza dell'algoritmo di Dijkstra si basa fortemente sull'assunzione che **tutti i pesi degli archi siano non negativi**.

Se il grafo contiene archi con peso negativo, Dijkstra può fallire nel calcolare le distanze corrette. 

### Perché fallisce con pesi negativi?
Una volta che un nodo $u$ viene aggiunto all'insieme $S$, la sua stima $d[u]$ viene considerata definitiva e non verrà più rielaborata o aggiornata. Se nel grafo esistono archi negativi, potrebbe esistere un cammino che passa attraverso nodi non ancora esplorati e riduce ulteriormente la distanza di un nodo già inserito in $S$. Poiché Dijkstra non riconsidera i nodi in $S$, non troverà mai tale cammino.

*Per grafi con archi di peso generico (anche negativi), si deve utilizzare l'algoritmo di **Bellman-Ford** (tempo $O(VE)$).*

---

## Proprietà Fondamentali dei Cammini Minimi usate nella Dimostrazione

La dimostrazione di correttezza fa uso di alcune proprietà teoriche dei cammini minimi:

1. **Disuguaglianza Triangolare**:
   Per ogni coppia di archi $(u,v) \in E$:
   $$\delta(s, v) \le \delta(s, u) + w(u,v)$$
2. **Proprietà del Limite Superiore**:
   Per ogni nodo $v \in V$, si ha sempre $d[v] \ge \delta(s, v)$. Inoltre, una volta che $d[v]$ raggiunge il valore $\delta(s,v)$, esso non cambia più.
3. **Proprietà di Convergenza**:
   Se $s \to \dots \to u \to v$ è un cammino minimo in $G$, e si ha $d[u] = \delta(s,u)$, il rilassamento dell'arco $(u,v)$ garantisce che $d[v] = \delta(s,v)$.

---

## Collegamenti agli Esercizi e Metodi

* **Guida alla Dimostrazione**: [[metodo_dimostrazione_correttezza_dijkstra]]
* **Simulazioni pratiche**: [[exam_2025_06_09_p2_e01]], [[exam_2025_07_03_p2_e01]]
* **Esercizio d'Esame collegato**: [[exam_2025_02_11_p2_completo_recupero_bonus]]

## Integrazione SRC-NOTE-001

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 33-35.

## Domanda tipica

Spiegare quando usare Dijkstra e perche la scelta greedy e corretta.

## Risposta d'esame breve

Dijkstra risolve cammini minimi da una sorgente in grafi con pesi non negativi. A ogni passo estrae il vertice non definitivo con distanza temporanea minima; grazie alla non negativita dei pesi, nessun cammino scoperto in seguito puo migliorare quella distanza.

## Errore comune

Applicare Dijkstra con archi di peso negativo.
