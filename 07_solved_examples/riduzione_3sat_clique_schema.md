# Schema — Riduzione $3SAT \le_p CLIQUE$

Questo schema descrive la riduzione polinomiale utilizzata per dimostrare che il problema **Clique** è NP-hard, partendo dal problema noto **3SAT**.

---

## 1. Definizioni del Problema

* **3SAT**: Data una formula booleana in Forma Normale Congiuntiva (CNF) in cui ogni clausola contiene esattamente 3 letterali (es. $C_1 \land C_2 \land \dots \land C_k$), esiste un'assegnazione di verità per le variabili tale da soddisfare la formula?
* **Clique**: Dato un grafo $G=(V,E)$ e un intero $k$, esiste un insieme di vertici $C \subseteq V$ di dimensione $\ge k$ mutuamente adiacenti?

---

## 2. Costruzione del Grafo $G = (V,E)$

Data una formula 3SAT $\Phi$ con $k$ clausole, costruiamo un grafo $G = (V,E)$ e impostiamo la dimensione richiesta per la clique a $k$.

1. **Vertici ($V$)**: Per ogni clausola $C_i$ e per ogni letterale in essa contenuto, creiamo un vertice nel grafo. Se la formula ha $k$ clausole, il grafo avrà esattamente:
   $$|V| = 3k \text{ vertici}$$
   Ogni vertice è etichettato con la coppia $\langle \text{letterale}, \text{indice clausola} \rangle$.

2. **Archi ($E$)**: Colleghiamo due vertici $u$ e $v$ con un arco se e solo se soddisfano **entrambe** le seguenti condizioni:
   - I due vertici appartengono a **clausole diverse** (nessun arco all'interno della stessa clausola).
   - I due letterali non sono **contraddittori** (ad esempio, non colleghiamo $x$ con $\neg x$).

---

## 3. Esempio Concreto

Consideriamo la formula $\Phi$ con $k = 3$ clausole:
$$\Phi = (x_1 \lor \neg x_2 \lor \neg x_3) \land (\neg x_1 \lor x_2 \lor x_3) \land (x_1 \lor x_2 \lor x_3)$$

### Vertici:
Il grafo ha $3 \times 3 = 9$ vertici organizzati in 3 "gruppi" (uno per clausola):
- **Clausola 1**: $v_{1,1} = x_1$, $v_{1,2} = \neg x_2$, $v_{1,3} = \neg x_3$
- **Clausola 2**: $v_{2,1} = \neg x_1$, $v_{2,2} = x_2$, $v_{2,3} = x_3$
- **Clausola 3**: $v_{3,1} = x_1$, $v_{3,2} = x_2$, $v_{3,3} = x_3$

### Archi (Esempio):
- Colleghiamo $v_{1,1} = x_1$ con $v_{2,2} = x_2$ (clausole diverse, non contraddittori).
- **NON** colleghiamo $v_{1,1} = x_1$ con $v_{1,2} = \neg x_2$ (stessa clausola).
- **NON** colleghiamo $v_{1,1} = x_1$ con $v_{2,1} = \neg x_1$ (contraddittori, poiché $x_1$ e $\neg x_1$ non possono essere contemporaneamente veri).

---

## 4. Dimostrazione di Correttezza (Se e Solo Se)

Vogliamo dimostrare che:
$$\Phi \text{ è soddisfacibile } \iff G \text{ contiene una clique di dimensione } k$$

### Direzione Diretta ($\implies$)
1. Se $\Phi$ è soddisfacibile, esiste un'assegnazione di verità che rende vera la formula.
2. In questa assegnazione, in ogni clausola $C_i$ vi è almeno un letterale vero. Scegliamo esattamente un letterale vero per ciascuna delle $k$ clausole.
3. Consideriamo l'insieme di vertici $C \subseteq V$ corrispondenti a questi letterali scelti. Chiaramente $|C| = k$.
4. Poiché abbiamo scelto un solo vertice per clausola, tutti i vertici in $C$ appartengono a clausole distinte.
5. Poiché i letterali selezionati sono tutti veri sotto la stessa assegnazione coerente, non vi può essere alcuna coppia di letterali contraddittori (es. non ci saranno sia $x_1$ che $\neg x_1$ in $C$).
6. Di conseguenza, tutti i vertici in $C$ sono mutuamente collegati da archi nel grafo $G$.
7. Pertanto, $C$ costituisce una clique di dimensione $k$.

### Direzione Inversa ($\impliedby$)
1. Supponiamo che il grafo $G$ contenga una clique $C$ di dimensione $k$.
2. Poiché non esistono archi tra vertici della stessa clausola, la clique deve contenere esattamente un vertice da ciascuna delle $k$ clausole.
3. Assegniamo il valore `TRUE` a tutte le variabili corrispondenti ai letterali contenuti in $C$.
4. Poiché non esistono archi tra letterali contraddittori, la clique non può contenere sia $x_i$ che $\neg x_i$. L'assegnazione di verità è quindi coerente.
5. Per le variabili non associate ad alcun vertice in $C$, assegniamo un valore di verità arbitrario.
6. Poiché la clique contiene esattamente un letterale da ciascuna clausola, e a tutti questi letterali è stato assegnato `TRUE`, ciascuna clausola della formula risulta soddisfatta.
7. Pertanto, la formula $\Phi$ è soddisfacibile.

---

## Collegamenti

- Teoria riduzioni: [[riduzioni_np_completezza]]
- Metodo d'esame: [[np_completezza_schema_dimostrazione]]
- Relazioni VC / Clique / IS: [[riduzioni_vertex_cover_clique_independent_set]]
