# Relazioni tra Vertex Cover, Clique e Independent Set

Questo documento illustra le relazioni matematiche e le riduzioni polinomiali che intercorrono tra tre problemi fondamentali su grafi: **Vertex Cover**, **Clique** e **Independent Set**.

---

## 1. Definizioni dei Problemi

Dato un grafo non orientato $G = (V, E)$:
* **Clique**: Sottoinsieme di vertici $C \subseteq V$ i cui elementi sono tutti mutuamente adiacenti in $G$.
* **Independent Set** (Insieme Indipendente): Sottoinsieme di vertici $I \subseteq V$ in cui nessuna coppia di vertici è collegata da un arco in $G$.
* **Vertex Cover** (Copertura dei Vertici): Sottoinsieme di vertici $S \subseteq V$ tale che ogni arco in $E$ ha almeno un estremo in $S$.

---

## 2. Il Grafo Complemento ($\overline{G}$)

Molte riduzioni utilizzano il concetto di **grafo complemento** (o grafo inverso).
Dato il grafo $G = (V,E)$, il suo complemento $\overline{G} = (V, \overline{E})$ ha lo stesso set di vertici $V$ e una lista di archi $\overline{E}$ definita come:
$$(u,v) \in \overline{E} \iff (u,v) \notin E \quad \text{per ogni } u \ne v$$
Ovvero, due vertici sono collegati in $\overline{G}$ se e solo se non sono collegati in $G$.

---

## 3. Relazione 1: Vertex Cover ed Independent Set

> **Teorema**:
> $S$ è un Vertex Cover di $G$ se e solo se il suo complemento $V \setminus S$ è un Independent Set di $G$.

### Proof (Dimostrazione)
* **Direzione ($\implies$)**: Sia $S$ un vertex cover di $G$. Supponiamo per assurdo che $V \setminus S$ non sia un independent set. Allora esistono due vertici $u, v \in V \setminus S$ collegati da un arco $(u,v) \in E$. Ma se l'arco $(u,v) \in E$, almeno uno dei suoi estremi deve trovarsi in $S$ (per definizione di vertex cover). Questo contraddice il fatto che sia $u$ che $v$ non appartengono a $S$. Dunque $V \setminus S$ è un independent set.
* **Direzione ($\impliedby$)**: Sia $I = V \setminus S$ un independent set. Vogliamo mostrare che $S$ è un vertex cover. Sia $(u,v) \in E$ un arco qualsiasi. Poiché $I$ è un independent set, non è possibile che entrambi gli estremi si trovino in $I$ (altrimenti l'arco non potrebbe esistere). Quindi, almeno uno dei due estremi deve trovarsi fuori da $I$, ovvero in $S$. Questo dimostra che $S$ copre l'arco $(u,v)$, quindi $S$ è un vertex cover.

### Riduzione Parametrica:
$$G \text{ ha un Vertex Cover di dimensione } k \iff G \text{ ha un Independent Set di dimensione } |V| - k$$

---

## 4. Relazione 2: Independent Set e Clique

> **Teorema**:
> $S$ è un Independent Set in $G$ se e solo se $S$ è una Clique nel grafo complemento $\overline{G}$.

### Proof (Dimostrazione)
* **Direzione ($\implies$)**: Sia $S$ un independent set in $G$. Per definizione, nessuna coppia di vertici $u,v \in S$ è collegata da un arco in $E$. Per definizione di grafo complemento, allora, tutte le coppie $u,v \in S$ devono essere collegate da un arco in $\overline{E}$. Dunque $S$ è una clique in $\overline{G}$.
* **Direzione ($\impliedby$)**: Sia $S$ una clique in $\overline{G}$. Per definizione, tutte le coppie $u,v \in S$ sono collegate da un arco in $\overline{E}$. Dunque nessuna coppia di vertici $u,v \in S$ può essere collegata da un arco in $E$. Pertanto $S$ è un independent set in $G$.

### Riduzione Parametrica:
$$G \text{ ha un Independent Set di dimensione } k \iff \overline{G} \text{ ha una Clique di dimensione } k$$

---

## 5. Relazione 3: Vertex Cover e Clique

Combinando le due relazioni precedenti otteniamo il legame diretto tra Vertex Cover e Clique.

> **Teorema**:
> $G$ ha un Vertex Cover di dimensione $k$ se e solo se il complemento $\overline{G}$ ha una Clique di dimensione $|V| - k$.

### Schema Riassuntivo delle Trasformazioni

| Problema di Partenza | Grafo | Parametro | Problema di Arrivo | Grafo | Parametro |
|---|---|---|---|---|---|
| **Vertex Cover** | $G$ | $k$ | **Independent Set** | $G$ | $|V|-k$ |
| **Independent Set** | $G$ | $k$ | **Clique** | $\overline{G}$ | $k$ |
| **Vertex Cover** | $G$ | $k$ | **Clique** | $\overline{G}$ | $|V|-k$ |

---

## Collegamenti

- Teoria riduzioni: [[riduzioni_np_completezza]]
- Metodo d'esame: [[np_completezza_schema_dimostrazione]]
- Schema Clique: [[np_completezza_schema]]
- Esempio riduzione 3SAT: [[riduzione_3sat_clique_schema]]
