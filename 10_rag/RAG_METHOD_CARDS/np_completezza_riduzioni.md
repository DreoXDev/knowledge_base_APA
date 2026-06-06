---
type: rag-method-card
topic: np-completezza-riduzioni
status: complete
source_methods:
  - 04_methods/np_completezza_schema_dimostrazione.md
  - 04_methods/metodo_dimostrare_np_completezza.md
  - 04_methods/metodo_riduzione_3sat_clique.md
  - 04_methods/metodo_riduzione_3sat_independent_set.md
  - 04_methods/metodo_riduzione_clique_vertex_cover.md
source_examples:
  - 07_solved_examples/np_completezza_schema.md
  - 07_solved_examples/riduzione_3sat_clique_schema.md
  - 07_solved_examples/riduzioni_vertex_cover_clique_independent_set.md
source_patterns:
  - 06_exam_patterns/dimostrazione_np_completezza.md
exam_use: true
---

# Method Card — P, NP, NP-completezza e Riduzioni

## Triggers (Parole Chiave)

* `P`, `NP`, `NP-completo`, `NP-hard`, `verificatore`, `certificato`
* `riduzione polinomiale`, `<=p`
* `SAT`, `3SAT`, `CLIQUE`, `Vertex Cover`, `Independent Set`, `Hamiltoniano`

---

## Decisione Rapida e Schema Risolutivo

Per dimostrare che un problema $\Pi$ è NP-completo, seguire rigorosamente questi 5 passaggi:

1. **Mostrare $\Pi \in NP$**:
   - Definire un certificato $y$ di dimensione polinomiale.
   - Fornire un verificatore deterministico $V(x,y)$ che lavori in tempo polinomiale rispetto a $|x|$.
2. **Scegliere un problema noto $\Pi'$**:
   - Scegliere un problema già dimostrato NP-completo (es. 3SAT, Clique, Vertex Cover).
3. **Costruire la riduzione polinomiale ($\Pi' \le_p \Pi$)**:
   - Definire la funzione $f$ per mappare le istanze di $\Pi'$ in istanze di $\Pi$ in tempo polinomiale.
4. **Dimostrare la doppia implicazione**:
   - $\implies$: Se l'istanza di $\Pi'$ ha risposta YES, allora l'istanza di $\Pi$ ha risposta YES.
   - $\impliedby$: Se l'istanza di $\Pi$ ha risposta YES, allora l'istanza di $\Pi'$ ha risposta YES.
5. **Concludere**:
   - Poiché $\Pi \in NP$ e $\Pi' \le_p \Pi$ con $\Pi' \in NPC$, allora $\Pi \in NPC$.

---

## Riduzioni Classiche e Schemi Notevoli

* **$3SAT \le_p CLIQUE$**:
   - Vertici: uno per ogni letterale di ogni clausola.
   - Archi: collega letterali appartenenti a clausole diverse se non sono contraddittori (es. non collegare $x$ con $\neg x$).
   - Parametro clique: $k = \text{numero di clausole}$.
* **$Independent Set \le_p Clique$**:
   - Grafo complemento $\overline{G}$ (preserva i vertici, inverte la presenza degli archi).
   - Parametro: lo stesso $k$.
* **$Vertex Cover \le_p Clique$**:
   - Grafo complemento $\overline{G}$.
   - Parametro: $k_{clique} = |V| - k_{vc}$.

---

## Warning d'Esame Critici

> [!CAUTION]
> * **Direzione corretta**: Per dimostrare che $\Pi$ è NP-completo, serve ridurre da un problema noto $\Pi' \le_p \Pi$. Ridurre al contrario non dimostra nulla.
> * **Certificato polinomiale**: Il verificatore deve prendere in input l'istanza originale e il certificato, lavorando in tempo polinomiale rispetto alla sola istanza.

---

## Riferimenti nella KB

* Teoria base: [[p_np_np_completezza]]
* Teoria riduzioni: [[riduzioni_np_completezza]]
* Metodo d'esame: [[np_completezza_schema_dimostrazione]]
* Esempio svolto base: [[np_completezza_schema]]
* Esempio svolto 3SAT -> Clique: [[riduzione_3sat_clique_schema]]
* Relazioni VC/Clique/IS: [[riduzioni_vertex_cover_clique_independent_set]]
