---
type: method
topic: 3-SAT to CLIQUE reduction
status: draft
tags:
  - apa
  - metodo
  - topic/np_completezza
  - topic/riduzioni_polinomiali
  - topic/3-sat
  - topic/clique
---

# Metodo — Riduzione Polinomiale da 3-CNF-SAT a CLIQUE

## Quando si usa

Questo metodo si applica ad esercizi di teoria o operativi in cui viene richiesta la costruzione del grafo risultante dalla riduzione polinomiale (riduzione di Karp) da una formula in forma normale congiuntiva con 3 letterali per clausola (3-CNF-SAT) ad un'istanza del problema CLIQUE.

---

## Procedura operativa di riduzione

Data una formula booleana $\varphi = C_1 \land C_2 \land \dots \land C_k$ formata da $k$ clausole, dove ogni clausola contiene esattamente 3 letterali $C_i = (l_{i,1} \lor l_{i,2} \lor l_{i,3})$:

### 1. Costruzione dei Vertici ($V$)
Per ciascun letterale $l_{i,j}$ presente nella clausola $C_i$, creiamo un vertice contrassegnato con la coppia $(i, j)$ e con il valore del letterale stesso.
- Il numero complessivo di vertici nel grafo $G = (V,E)$ sarà esattamente:
  $$|V| = 3k$$
  dove $k$ è il numero di clausole nella formula.

### 2. Costruzione degli Archi ($E$)
Colleghiamo due vertici $v_{i,a}$ (appartenente alla clausola $C_i$) e $v_{j,b}$ (appartenente alla clausola $C_j$) con un arco non orientato se e solo se soddisfano **entrambe** le seguenti condizioni:
1. **Clausole diverse**: I due vertici provengono da clausole distinte, ovvero:
   $$i \neq j$$
   *(Non aggiungiamo mai archi tra vertici appartenenti alla stessa clausola!)*
2. **Letterali compatibili**: I due letterali non sono l'uno la negazione dell'altro (cioè non sono complementari):
   $$l_{i,a} \neq \neg l_{j,b}$$
   *(Ad esempio, non colleghiamo mai un vertice contrassegnato con $x_1$ ad uno contrassegnato con $\neg x_1$.)*

### 3. Parametro Clique ($K$)
Il parametro target per il problema CLIQUE (dimensione della clique da ricercare nel grafo $G$) è impostato esattamente al numero di clausole della formula originale:
$$K = k$$

---

## Giustificazione teorica della riduzione

* **Direzione $\implies$ (Satisfiability $\implies$ Clique)**:
  Se la formula $\varphi$ è soddisfacibile, esiste un assegnamento di verità che rende vera $\varphi$. Per definizione, questo assegnamento deve rendere vero almeno un letterale in ciascuna delle $k$ clausole. Scegliamo un letterale vero per ciascuna clausola, individuando $k$ vertici corrispondenti nel grafo. Poiché provengono tutti da clausole distinte e sono tutti veri sotto lo stesso assegnamento (quindi non possono essere complementari), esiste un arco tra ogni coppia di questi $k$ vertici. Questi vertici formano pertanto una clique di dimensione $k$.

* **Direzione $\impliedby$ (Clique $\implies$ Satisfiability)**:
  Se il grafo $G$ possiede una clique di dimensione $k$, questa deve essere formata da esattamente $k$ vertici che sono tutti mutuamente connessi da archi. Poiché non esistono archi tra vertici appartenenti alla stessa clausola, la clique deve contenere esattamente un vertice per ciascuna delle $k$ clausole. Inoltre, poiché i vertici nella clique sono adiacenti, nessun paio di essi può corrispondere a letterali complementari. Possiamo quindi assegnare il valore di verità `true` a tutti i letterali corrispondenti ai vertici della clique. Questo assegnamento soddisfa contemporaneamente tutte le clausole, rendendo la formula $\varphi$ soddisfacibile.

---

## Esercizi collegati

- [[exam_2025_11_10_p2_e02]]

---

## Errori comuni da evitare

> [!Warning]
> **Collegare la stessa clausola**: Aggiungere archi tra nodi della stessa clausola. Ricorda che la regola vieta categoricamente archi intra-clausola.
> **Collegare letterali complementari**: Collegare un letterale al suo negato (es. $x$ e $\neg x$). Essi sono logicamente incompatibili, quindi non possono appartenere entrambi a una clique di assegnazione consistente.
