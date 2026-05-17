---
type: method
topic: Dijkstra step-by-step
status: draft
tags:
  - apa
  - metodo
  - topic/grafi
  - topic/cammini_minimi
  - topic/dijkstra
---

# Metodo - Esecuzione manuale di Dijkstra

## Quando si usa

Questo metodo si applica ad esercizi in cui viene chiesto di simulare passo-passo l'esecuzione dell'algoritmo di Dijkstra su un grafo orientato o non orientato con pesi non negativi sugli archi, tracciando l'evoluzione dei valori dell'attributo $d$ (stima del cammino minimo), l'ordine dei nodi estratti e gli archi rilassati ad ogni iterazione.

## Riconoscimento rapido

> [!Info]
> Segnali che indicano che questo esercizio usa questo metodo:
> - Richiesta esplicita di mostrare il valore dell'attributo $d$ all'interno dei cerchi rappresentanti i nodi.
> - Presenza di puntini per specificare l'ordine dei nodi estratti (es. *Estrazioni:* A, ...).
> - Richiesta di evidenziare o elencare gli archi che vengono rilassati ad ogni passo.

## Procedura operativa

1. **Inizializzazione**:
   - Impostare $d[s] = 0$ per la sorgente $s$.
   - Impostare $d[u] = \infty$ per tutti gli altri nodi $u \in V \setminus \{s\}$.
   - Inserire tutti i vertici in una coda di priorità $Q$ (tutti i nodi sono inizialmente non estratti).
2. **Ciclo principale**: Finché $Q$ non è vuota:
   - Estrarre da $Q$ il nodo $u$ avente il valore di $d[u]$ minimo (ad ogni passo, registrare questo nodo nella lista delle estrazioni).
   - Per ciascun arco uscente da $u$, $(u,v) \in E$, eseguire il rilassamento:
     - Se $d[u] + w(u,v) < d[v]$:
       - Impostare $d[v] = d[u] + w(u,v)$.
       - Registrare l'arco $(u,v)$ come "effettivamente rilassato" in questo passo.
3. **Tracciamento dei valori**:
   - In molti testi, viene richiesto di scrivere il valore finale di $d$ dentro ciascun nodo, oppure mostrare il valore dopo ogni singola estrazione. Seguire rigorosamente le istruzioni grafiche.

## Formule utili

Rilassamento di un arco $(u,v)$:
$$
\text{Relax}(u, v, w):
\quad \text{if } d[v] > d[u] + w(u,v) \text{ then } d[v] = d[u] + w(u,v)
$$

## Esercizi collegati

- [[exam_2025_07_03_p2_e01]]
- [[exam_2025_06_09_p2_e01]]
- [[exam_2025_06_09_p1_e02]] (collegato indirettamente per cammini)

## Errori comuni

> [!Warning]
> Estrarre un nodo non raggiungibile (con $d[u] = \infty$) se non ci sono più nodi raggiungibili in $Q$.
> Non aggiornare correttamente le priorità degli altri nodi rimasti in $Q$ quando si effettua un rilassamento.
> Confondere Dijkstra con Kruskal o Prim: Dijkstra trova cammini minimi da sorgente singola, non il Minimum Spanning Tree.
