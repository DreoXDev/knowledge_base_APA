---
type: method
topic: Riduzione 3-SAT to Independent Set
status: complete
tags:
  - apa
  - metodo
  - topic/np-completezza
  - topic/riduzioni_polinomiali
  - topic/3-sat
  - topic/independent_set
---

# Metodo — Riduzione Polinomiale da 3-SAT a INDEPENDENT SET

## Quando si usa

Questo metodo si applica quando l'esercizio richiede di definire formalmente la riduzione polinomiale (tipo Karp) a partire da una generica formula in forma normale congiuntiva con 3 letterali per clausola (3-SAT) ad un'istanza del problema dell'insieme indipendente (INDEPENDENT SET).

---

## Schema Formale di Riduzione ($3\text{-SAT} \le_p \text{INDEPENDENT SET}$)

Data una generica formula booleana $\varphi = C_1 \land C_2 \land \dots \land C_k$ in formato 3-CNF operante su $n$ variabili, dove ciascuna clausola $C_r$ (per $r \in \{1,\dots,k\}$) ha la forma:
$$C_r = l^r_1 \lor l^r_2 \lor l^r_3$$

Costruiamo un grafo non orientato $G = (V,E)$ e una dimensione target $K \in \mathbb{N}$ nel modo seguente:

### 1. Costruzione dei Vertici ($V$)
Per ciascun letterale $l^r_i$ presente nella clausola $C_r$, creiamo un vertice contrassegnato con la coppia $(r, i)$.
Il numero complessivo di vertici è:
$$|V| = 3k$$

### 2. Costruzione degli Archi ($E$)
Colleghiamo due vertici distinti $v_i^r = (r, i)$ e $v_j^s = (s, j)$ con un arco non orientato se e solo se soddisfano **almeno una** delle seguenti condizioni:
1. **Archi Intra-clausola**: I due vertici appartengono alla stessa clausola, ovvero $r = s$. *(Questo crea un sottografo completo di 3 nodi, cioè un triangolo $K_3$, per ciascuna clausola).*
2. **Archi di Incompatibilità**: I due vertici appartengono a clausole diverse ($r \neq s$) ma rappresentano letterali complementari, ovvero $l^r_i = \neg l^s_j$ (ad esempio $x_1$ e $\neg x_1$).

### 3. Parametro Target $K$
La dimensione dell'Independent Set cercata è impostata a:
$$K = k \quad (\text{numero di clausole della formula original})$$

---

## Dimostrazione di Correttezza

Dobbiamo dimostrare che:
$$\varphi \text{ è soddisfacibile} \iff G \text{ ha un Independent Set di dimensione al più/almeno } k$$

### Dimostrazione $\implies$
1. Sia $\varphi$ soddisfacibile. Allora esiste un assegnamento di verità consistente delle variabili che rende vera $\varphi$.
2. Di conseguenza, in ogni clausola $C_r$ (per $r \in \{1,\dots,k\}$) deve esistere almeno un letterale vero. Scegliamo esattamente un letterale vero per ciascuna clausola.
3. Questo definisce un insieme $S \subseteq V$ di esattamente $k$ vertici nel grafo.
4. Verifichiamo che non vi siano archi tra i nodi scelti in $S$:
   - Poiché abbiamo scelto esattamente un nodo per ciascuna clausola, non esistono archi intra-clausola tra i vertici in $S$.
   - Poiché i letterali selezionati provengono da un assegnamento di verità consistente e reale, non è possibile che contengano letterali complementari (non possiamo avere contemporaneamente $x \in S$ e $\neg x \in S$). Dunque non vi sono archi di incompatibilità tra i vertici in $S$.
5. Di conseguenza, $S$ è un Independent Set di dimensione $k$.

### Dimostrazione $\impliedby$
1. Sia $S \subseteq V$ un Independent Set di dimensione $k$ in $G$.
2. Poiché per ciascuna clausola $C_r$ i tre vertici sono tra loro tutti collegati (formano un triangolo $K_3$), un insieme indipendente non può contenere più di un vertice da ciascuna clausola.
3. Avendo $|S| = k$ e essendoci $k$ clausole, l'Independent Set deve contenere **esattamente** un vertice per ciascuna clausola.
4. Poiché non ci sono archi tra i vertici in $S$:
   - Nessun paio di vertici scelti può rappresentare letterali complementari (altrimenti ci sarebbe un arco di incompatibilità tra di essi).
5. Possiamo quindi assegnare il valore di verità `true` a tutti i letterali corrispondenti ai nodi in $S$ in modo consistente. Se una variabile non è coperta da $S$, le assegniamo un valore arbitrario.
6. Avendo un letterale vero per ciascuna clausola, la formula $\varphi$ è soddisfatta, risultando soddisfacibile. ($\text{Q.E.D.}$)

---

## Esercizi collegati

- [[exam_2025_02_11_p2_completo_recupero_e04]] (Richiesta esplicita della riduzione generale a scelta dello studente)
