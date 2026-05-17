---
type: exercise
exam: 2025-02-11 Parte II completo/recupero
exercise_number: bonus
topic:
  - domande_bonus
  - matroidi
  - clique_vertex_cover
  - dijkstra
difficulty: alta
status: cataloged
method:
  - [[metodo_greedy_matroidi_rado]]
  - [[metodo_riduzione_clique_vertex_cover]]
  - [[metodo_dimostrazione_correttezza_dijkstra]]
---

# Domande Facoltative Premiali (11 Febbraio 2025)

## Testo

Il testo d'esame offre una domanda facoltativa premiale da 3 punti, a scelta dello studente tra le tre opzioni di seguito riportate.

---

## Opzione 1: Dimostrazione di correttezza dell'algoritmo Greedy su Matroidi

### Testo
> Dimostrare che se un sistema di indipendenza $(E,\mathcal{F})$ è un matroide allora per ogni funzione peso $w: E \to \mathbb{R}^+ \cup \{0\}$ (oppure $w: E \to \mathbb{R}$), l’algoritmo **Greedy-max** restituisce una soluzione ottima.

### Risoluzione Formale
Vedi il metodo dettagliato e la dimostrazione passo-passo in:
* **[[metodo_greedy_matroidi_rado]]** (Teorema di correttezza dell'algoritmo Greedy per i matroidi / Teorema di Rado-Edmonds).

---

## Opzione 2: Dimostrazione formale che CLIQUE si riduce a VERTEX-COVER

### Testo
> Dimostrare che **CLIQUE** si riduce a **VERTEX-COVER** ($CLIQUE \le_p VERTEX-COVER$).

### Risoluzione Formale
La dimostrazione formale si basa sul dimostrare la seguente equivalenza per ogni sottoinsieme di vertici $V'$ in un grafo $G = (V,E)$ rispetto al suo complementare $G' = \bar{G}$:

$$V' \text{ è una Clique in } G \iff V \setminus V' \text{ è un Vertex Cover in } G'$$

#### Dimostrazione $\implies$ (Se $V'$ è una Clique in $G$, allora $V \setminus V'$ è un Vertex Cover in $G'$)
1. Sia $V'$ una clique in $G$. Per definizione, per ogni coppia di vertici distinti $u, v \in V'$, l'arco $(u,v)$ appartiene a $E$.
2. Di conseguenza, nel grafo complementare $G' = \bar{G}$, per definizione di complementare, non può esistere alcun arco tra nodi di $V'$. Cioè, per ogni $u, v \in V'$, $(u,v) \notin E'$.
3. Sia ora un generico arco $(x,y) \in E'$ nel complementare. Poiché non esistono archi in $E'$ con entrambi gli estremi in $V'$, è impossibile che sia $x \in V'$ e contemporaneamente $y \in V'$.
4. Di conseguenza, almeno uno tra $x$ e $y$ deve appartenere al complementare $V \setminus V'$.
5. Poiché ogni arco $(x,y) \in E'$ tocca almeno un nodo in $V \setminus V'$, l'insieme $V \setminus V'$ è per definizione una copertura di vertici (Vertex Cover) per $G'$.

#### Dimostrazione $\impliedby$ (Se $V \setminus V'$ è un Vertex Cover in $G'$, allora $V'$ è una Clique in $G$)
1. Sia $V \setminus V'$ un Vertex Cover in $G'$.
2. Supponiamo per assurdo che $V'$ **non** sia una clique in $G$.
3. Allora devono esistere due vertici distinti $u, v \in V'$ tali che l'arco $(u,v) \notin E$.
4. Per definizione di grafo complementare, l'assenza dell'arco in $G$ implica la sua presenza in $G'$, ovvero $(u,v) \in E'$.
5. Poiché $V \setminus V'$ è un Vertex Cover per $G'$, l'arco $(u,v) \in E'$ deve toccare almeno un vertice in $V \setminus V'$.
6. Ma per costruzione abbiamo scelto sia $u \in V'$ che $v \in V'$, il che implica che nessuno dei due estremi appartiene a $V \setminus V'$. Questo contraddice il fatto che $V \setminus V'$ sia un Vertex Cover.
7. L'ipotesi assurda è quindi falsa: $V'$ deve essere una clique in $G$. ($\text{Q.E.D.}$)

---

## Opzione 3: Dimostrazione di correttezza dell'algoritmo di Dijkstra

### Testo
> Dimostrare la correttezza dell'algoritmo di **Dijkstra** (non occorre dimostrare le proprietà del limite superiore, della convergenza, e la disuguaglianza triangolare).

### Risoluzione Formale
Vedi la dimostrazione dettagliata basata sull'invariante di ciclo in:
* **[[metodo_dimostrazione_correttezza_dijkstra]]**
