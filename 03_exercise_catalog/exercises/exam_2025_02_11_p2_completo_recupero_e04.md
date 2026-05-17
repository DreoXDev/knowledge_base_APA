---
type: exercise
exam: 2025-02-11 Parte II completo/recupero
exercise_number: 4
topic:
  - NP-completezza
  - riduzioni_polinomiali
  - 3-sat
  - clique
  - independent_set
difficulty: media
status: cataloged
method:
  - [[metodo_riduzione_3sat_clique]]
  - [[metodo_riduzione_3sat_independent_set]]
---

# Esercizio 4 — Definizione di grafo nella riduzione da 3-SAT a CLIQUE o INDEPENDENT SET

## Testo

Data una generica formula 3-SAT (o 3-CNF-SAT) $f = C_1 \land \dots \land C_k$ dove per ogni $r \in \{1,\dots,k\}$, la $r$-esima clausola è $C_r = l^r_1 \lor l^r_2 \lor l^r_3$, definire il grafo $G$ utilizzato nella riduzione da **3-SAT** a **CLIQUE** oppure da **3-SAT** a **INDEPENDENT SET** (a scelta dello studente).

---

## Risoluzione

Di seguito vengono fornite entrambe le costruzioni formali consentite dall'esercizio (in sede d'esame è sufficiente presentarne una sola).

---

### Opzione A: Riduzione da 3-SAT a CLIQUE ($3\text{-SAT} \le_p \text{CLIQUE}$)

Data la formula $\varphi = C_1 \land C_2 \land \dots \land C_k$ con $k$ clausole, costruiamo un grafo non orientato $G = (V,E)$ e una dimensione target $K = k$.

#### 1. Definizione dei Vertici ($V$)
Per ciascun letterale $l^r_i$ presente nella clausola $C_r$, creiamo un vertice contrassegnato con la coppia $(r, i)$. Essendoci $k$ clausole, ognuna con 3 letterali, il numero di vertici in $G$ sarà esattamente:
$$|V| = 3k$$

#### 2. Definizione degli Archi ($E$)
Colleghiamo due vertici $v_i^r = (r, i)$ e $v_j^s = (s, j)$ con un arco non orientato se e solo se soddisfano due condizioni:
1. **Clausole diverse**: I due vertici appartengono a clausole distinte, ovvero $r \neq s$. *(Nessun arco tra vertici della stessa clausola).*
2. **Letterali compatibili**: I letterali corrispondenti non sono complementari, ovvero $l^r_i \neq \neg l^s_j$. *(Non colleghiamo mai un letterale alla sua negazione, ad esempio $x_1$ e $\neg x_1$).*

#### 3. Corrispondenza e Correttezza
* **Tesi**: La formula $f$ è soddisfacibile $\iff G$ contiene una clique di dimensione $k$.
* **Dimostrazione $\implies$**: Se $f$ è soddisfacibile, esiste un assegnamento di verità consistente che rende vera $f$. Questo significa che in ciascuna delle $k$ clausole $C_r$ esiste almeno un letterale vero. Scegliamo un letterale vero per ciascuna clausola, individuando $k$ vertici nel grafo. Poiché provengono tutti da clausole distinte e sono compatibili sotto lo stesso assegnamento (non possono essere complementari), esiste un arco tra ogni coppia di questi $k$ vertici. Questi formano quindi una clique di dimensione $k$.
* **Dimostrazione $\impliedby$**: Se $G$ contiene una clique di dimensione $k$, tale clique deve contenere esattamente un vertice per ciascuna delle $k$ clausole (poiché non ci sono archi intra-clausola). Inoltre, i letterali di questi $k$ vertici sono mutuamente compatibili (non complementari). Assegnando il valore di verità `true` a ciascuno di questi letterali (e valori coerenti a tutte le altre variabili), rendiamo vera la formula $f$, che risulta quindi soddisfacibile.

---

### Opzione B: Riduzione da 3-SAT a INDEPENDENT SET ($3\text{-SAT} \le_p \text{INDEPENDENT SET}$)

Data la formula $\varphi = C_1 \land C_2 \land \dots \land C_k$ con $k$ clausole, costruiamo un grafo non orientato $G = (V,E)$ e una dimensione target $K = k$.

#### 1. Definizione dei Vertici ($V$)
Esattamente come per CLIQUE, creiamo un vertice per ciascuno dei 3 letterali di ciascuna delle $k$ clausole:
$$|V| = 3k$$

#### 2. Definizione degli Archi ($E$)
Colleghiamo due vertici $v_i^r = (r, i)$ e $v_j^s = (s, j)$ con un arco non orientato se e solo se soddisfano **almeno una** delle seguenti condizioni (è la costruzione duale rispetto a CLIQUE):
1. **Clausola identica (Intra-clausola)**: I due vertici appartengono alla stessa clausola, ovvero $r = s$. *(Formiamo un triangolo completo di archi tra i 3 letterali di ciascuna clausola).*
2. **Letterali incompatibili**: I due vertici appartengono a clausole diverse ($r \neq s$) ma rappresentano letterali complementari, ovvero $l^r_i = \neg l^s_j$.

#### 3. Corrispondenza e Correttezza
* **Tesi**: La formula $f$ è soddisfacibile $\iff G$ contiene un insieme indipendente (Independent Set) di dimensione $k$.
* **Dimostrazione $\implies$**: Se $f$ è soddisfacibile, scegliamo un letterale vero per ciascuna delle $k$ clausole. Questo ci fornisce $k$ vertici. Poiché provengono da clausole diverse, non ci sono archi intra-clausola tra di essi. Poiché appartengono ad un assegnamento consistente, non contengono letterali complementari, quindi non ci sono archi di incompatibilità tra di essi. Questi $k$ vertici sono mutuamente non adiacenti, formando un Independent Set di dimensione $k$.
* **Dimostrazione $\impliedby$**: Se $G$ contiene un Independent Set di dimensione $k$, esso deve contenere esattamente un vertice per ciascuna clausola (poiché i 3 nodi intra-clausola sono connessi da archi, rendendo impossibile sceglierne più di uno). Inoltre, non essendoci archi tra i $k$ nodi scelti, nessun paio di essi può essere complementare. Questo garantisce che possiamo assegnare il valore `true` a tutti i letterali corrispondenti in modo consistente, soddisfacendo la formula $f$.
