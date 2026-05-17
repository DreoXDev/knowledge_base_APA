---
type: method
topic: Dimostrazione correttezza Dijkstra
status: complete
tags:
  - apa
  - metodo
  - topic/grafi
  - topic/cammini_minimi
  - topic/dijkstra
---

# Metodo — Dimostrazione di Correttezza dell'Algoritmo di Dijkstra

## Quando si usa

Questo metodo si applica quando viene richiesto di dimostrare formalmente la correttezza dell'algoritmo di Dijkstra per cammini minimi a sorgente singola su grafi orientati con pesi non negativi ($w(u,v) \ge 0$).

---

## Struttura della Dimostrazione Formale

La dimostrazione si basa sulla definizione di un **invariante di ciclo** basato sull'insieme $S$ di nodi di cui l'algoritmo ha già determinato definitivamente il cammino minimo dalla sorgente $s$.

---

### 1. Invariante di Ciclo

Sia $S$ l'insieme dei vertici il cui peso del cammino minimo definitivo è stato determinato dall'algoritmo.
L'invariante di ciclo dell'algoritmo di Dijkstra è:

> **Invariante**:
> All'inizio di ogni iterazione del ciclo `while` (prima di estrarre un nodo da $Q = V \setminus S$), per ogni vertice $u \in S$, la stima del cammino minimo $d[u]$ coincide con la reale distanza minima $\delta(s, u)$ da $s$ a $u$:
> $$d[u] = \delta(s, u) \quad \forall u \in S$$

---

### 2. Dimostrazione dell'Invariante

#### Inizializzazione (Caso Base)
* All'inizio, l'insieme $S$ è vuoto ($S = \emptyset$).
* L'invariante è vacuamente vero (poiché non ci sono nodi in $S$).
* Al primo passo viene inserito $s$ in $S$. Poiché $d[s] = 0 = \delta(s,s)$, l'invariante continua a valere.

#### Mantenimento (Passo Induttivo)
Supponiamo che l'invariante valga all'inizio di un'iterazione (quindi $d[y] = \delta(s,y)$ per tutti i nodi $y \in S$). 

Sia $u$ il primo nodo estratto da $Q = V \setminus S$ in questa iterazione. Dijkstra imposta formalmente $S = S \cup \{u\}$.
Dobbiamo dimostrare che:
$$d[u] = \delta(s, u)$$

##### Dimostrazione per Assurdo:
Supponiamo per assurdo che al momento dell'estrazione di $u$ si abbia:
$$d[u] \neq \delta(s, u)$$

Poiché per la proprietà del limite superiore vale sempre $d[u] \ge \delta(s,u)$, la nostra ipotesi per assurdo implica che:
$$d[u] > \delta(s, u)$$

1. **Esistenza di un cammino minimo reale**:
   Sia $P$ un cammino minimo reale da $s$ a $u$ nel grafo $G$. Il cammino $P$ parte da $s$ (che appartiene a $S$) e termina su $u$ (che non appartiene a $S$).

2. **Individuazione del primo nodo fuori da $S$**:
   Se percorriamo $P$ partendo da $s$, deve esistere un primo arco $(x, y)$ in $P$ che attraversa il taglio da $S$ a $V \setminus S$. Dunque $x \in S$ e $y \in V \setminus S$ (con la possibilità che $y = u$).

   Rappresentazione del cammino $P$:
   $$s \xrightarrow{P_1} x \to y \xrightarrow{P_2} u$$

3. **Valutazione della stima del cammino minimo su $y$**:
   - Poiché $x \in S$, per ipotesi induttiva la sua stima è corretta: $d[x] = \delta(s, x)$.
   - Quando $x$ è stato inserito in $S$, l'arco $(x,y)$ è stato rilassato dall'algoritmo.
   - Poiché il cammino da $s$ a $y$ che passa per $x$ è un sotto-cammino di un cammino minimo reale $P$, per la proprietà di convergenza e del rilassamento si ha:
     $$d[y] = \delta(s, y)$$

4. **Confronto tra le distanze**:
   Poiché tutti i pesi degli archi nel grafo sono non negativi ($w(a,b) \ge 0$), la distanza da $s$ a $y$ non può superare la distanza totale da $s$ a $u$ lungo il cammino minimo $P$:
   $$\delta(s, y) \le \delta(s, u)$$
   
   Unendo le relazioni, otteniamo:
   $$d[y] = \delta(s, y) \le \delta(s, u)$$

5. **Assurdità della scelta del minimo**:
   Dato che per ipotesi di assurdo $d[u] > \delta(s, u)$, unendo quest'ultima relazione con il punto precedente ricaviamo:
   $$d[y] < d[u]$$
   
   Tuttavia, all'inizio dell'iterazione corrente sia $y$ che $u$ appartenevano a $Q = V \setminus S$. Poiché l'algoritmo di Dijkstra estrae sempre il nodo in $Q$ con la stima $d$ **minima** e ha estratto $u$, deve valere:
   $$d[u] \le d[y]$$
   
   Questa relazione contraddice direttamente $d[y] < d[u]$.

L'ipotesi di assurdo $d[u] > \delta(s,u)$ è quindi insostenibile, il che dimostra che:
$$d[u] = \delta(s, u)$$

L'invariante è mantenuto.

#### Conclusione (Terminazione)
Alla fine del ciclo `while`, la coda con priorità $Q$ è vuota, il che implica che $S = V$.
Essendo l'invariante valido, per ogni nodo $v \in V$ si ha:
$$d[v] = \delta(s, v)$$

La correttezza di Dijkstra è dimostrata ($\text{Q.E.D.}$).

---

## Esercizi collegati

- [[exam_2025_02_11_p2_completo_recupero_bonus]] (Richiesta esplicita come domanda premiale bonus)
- [[exam_2025_06_09_p2_e01]] (Simulazione operativa di Dijkstra)
- [[exam_2025_07_03_p2_e01]] (Simulazione operativa di Dijkstra)
