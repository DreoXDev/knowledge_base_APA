# Schema — Dimostrazione NP-completezza (Esempio Vertex Cover)

Questo schema applica il **Metodo dei 5 Pilastri** per dimostrare che un problema (in questo caso **Vertex Cover**) è NP-completo, riducendolo da **Clique**.

---

## 1. Definizione dei Problemi

* **Clique**: Dato un grafo $G = (V,E)$ e un intero $k$, esiste un sottoinsieme $C \subseteq V$ di dimensione $\ge k$ in cui ogni coppia di vertici è collegata da un arco? (Noto essere NP-completo).
* **Vertex Cover (VC)**: Dato un grafo $G' = (V',E')$ e un intero $k'$, esiste un sottoinsieme $S \subseteq V'$ di dimensione $\le k'$ tale che ogni arco in $E'$ ha almeno un estremo in $S$?

---

## Passo 1: Dimostrare l'appartenenza a NP ($VC \in NP$)

1. **Certificato ($S$)**: Un sottoinsieme di vertici $S \subseteq V'$. La dimensione di $S$ è polinomiale rispetto alla dimensione dell'input (in quanto $|S| \le |V'|$).
2. **Verificatore ($V$)**:
   - Controlla se la cardinalità $|S| \le k'$.
   - Per ciascun arco $e = (u,v) \in E'$, controlla se $u \in S$ oppure $v \in S$.
   - Se entrambi i controlli sono soddisfatti per ogni arco, restituisce YES, altrimenti NO.
3. **Analisi della Complessità**:
   - Il controllo della cardinalità richiede tempo $O(|V'|)$.
   - Per ciascuno degli $|E'|$ archi, l'appartenenza a $S$ si verifica in tempo costante $O(1)$ usando un array di booleani di dimensione $|V'|$. Il tempo totale è quindi $O(|V'| + |E'|)$, che è lineare rispetto alla dimensione del grafo, ovvero polinomiale. Pertanto, $VC \in NP$.

---

## Passo 2: Scegliere il Problema Noto ($CLIQUE \in NPC$)

Scegliamo il problema **Clique**, già noto per essere NP-completo dalla teoria.

---

## Passo 3: Costruire la Riduzione Polinomiale ($CLIQUE \le_p VC$)

Definiamo la trasformazione delle istanze:
* Sia $\langle G=(V,E), k \rangle$ un'istanza generica del problema **Clique**.
* Costruiamo un'istanza $\langle G'=(V',E'), k' \rangle$ del problema **Vertex Cover** nel seguente modo:
  1. Il set di vertici è lo stesso: $V' = V$.
  2. Il set di archi $E'$ è l'insieme complemento degli archi di $G$, ovvero:
     $$E' = \overline{E} = \{ (u,v) \mid u, v \in V, u \ne v, (u,v) \notin E \}$$
  3. Il parametro $k'$ viene impostato a:
     $$k' = |V| - k$$

### Complessità della Trasformazione
La costruzione del grafo complemento $G' = (V, \overline{E})$ richiede di esaminare tutte le coppie di vertici di $G$ e invertire la presenza degli archi. La complessità in tempo è $O(|V|^2)$, che è polinomiale rispetto alla dimensione dell'input originale.

---

## Passo 4: Dimostrare la Correttezza (Se e Solo Se)

Dobbiamo dimostrare che:
$$G \text{ ha una clique di dimensione } k \iff G' \text{ ha un vertex cover di dimensione } |V|-k$$

### Direzione Diretta ($\implies$)
1. Supponiamo che $G$ contenga una clique $C \subseteq V$ con $|C| = k$.
2. Per definizione di clique, per ogni coppia di vertici distinti $u, v \in C$, si ha che $(u,v) \in E$. Dunque, nessun arco in $\overline{E}$ può avere entrambi gli estremi in $C$.
3. Questo implica che per ogni arco $(u,v) \in \overline{E}$ (archi di $G'$), almeno uno dei due estremi $u$ o $v$ deve appartenere a $V \setminus C$.
4. Per definizione, allora, l'insieme $S = V \setminus C$ è un **vertex cover** per il grafo $G'$.
5. La dimensione di $S$ è $|S| = |V| - |C| = |V| - k = k'$.

### Direzione Inversa ($\impliedby$)
1. Supponiamo che $G'$ contenga un vertex cover $S \subseteq V$ di dimensione $|S| \le |V| - k$.
2. Per definizione di vertex cover, per ogni arco $(u,v) \in E'$ (archi di $G'$), almeno uno degli estremi $u$ o $v$ appartiene a $S$.
3. Di conseguenza, non esiste alcun arco in $E'$ che colleghi due vertici di $V \setminus S$.
4. Poiché $E'$ contiene tutti gli archi mancanti in $G$, questo significa che nel grafo originale $G$ tutti i vertici del sottoinsieme $C = V \setminus S$ sono mutuamente collegati da archi di $E$.
5. Pertanto, $C$ è una **clique** in $G$.
6. La dimensione della clique è $|C| = |V| - |S| \ge |V| - (|V| - k) = k$.

---

## Passo 5: Conclusione

Poiché abbiamo dimostrato che $VC \in NP$ e che il problema NP-completo $Clique$ si riduce polinomialmente a $VC$ ($Clique \le_p VC$), concludiamo che il problema **Vertex Cover** è NP-completo.

---

## Collegamenti

- Metodo: [[np_completezza_schema_dimostrazione]]
- Relazioni VC / Clique / IS: [[riduzioni_vertex_cover_clique_independent_set]]
- Riduzione 3SAT -> Clique: [[riduzione_3sat_clique_schema]]
