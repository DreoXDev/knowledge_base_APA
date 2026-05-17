---
type: exam_pattern
topic: Parte II Theory and Graph Patterns
status: complete
tags:
  - apa
  - pattern
  - topic/parte_ii
  - topic/teoria
  - topic/grafi
---

# Pattern d'Esame — Parte II: Grafi, Riduzioni e Teoria

L'analisi degli appelli della **Parte II** ha rivelato una struttura ciclica e altamente prevedibile dei quesiti proposti. Questa guida raccoglie i pattern ricorrenti per la parte grafica-operativa e per la parte teorica-dimostrativa.

---

## 1. Algoritmi su Grafi (Operativo)

Ogni appello contiene almeno un esercizio operativo su grafi concreti (solitamente 5 o 6 nodi), valutato **6 punti**.

### Pattern A: Simulazione manuale di Kruskal (MST)
* **Punteggio**: 6 punti.
* **Formato di risposta obbligatorio**: Viene fornita una griglia progressiva di "quadrati" ($Q_1, Q_2, \dots, Q_{|E|}$). Ciascun quadrato $Q_i$ deve contenere l'insieme degli archi aggiunti al MST dopo l'esame del $i$-esimo arco.
* **Regola aurea**: Mostrare la foresta accumulata includendo *solo* gli archi inseriti definitivamente (quelli che non creano cicli). Se un arco viene esaminato e scartato, il quadrato corrispondente deve rimanere identico al precedente.
* **Esercizi correlati**: [[exam_2025_02_11_p2_completo_recupero_e01]], [[exam_2025_11_10_p2_e01]], [[exam_2026_01_12_e03]], [[exam_2025_09_17_p2_e01]].

### Pattern B: Simulazione step-by-step di Dijkstra
* **Punteggio**: 6 punti.
* **Formato di risposta**: Tabella che traccia per ciascuna iterazione:
  - Il nodo estratto dalla coda con priorità.
  - Il valore corrente della stima $d[v]$ per ciascun nodo $v$.
  - Il predecessore $\pi[v]$ aggiornato dopo i rilassamenti.
* **Esercizi correlati**: [[exam_2025_06_09_p2_e01]], [[exam_2025_07_03_p2_e01]], [[exam_2025_01_13_p2_e01]].

---

## 2. Riduzioni Polinomiali (Operativo)

Un esercizio da **6 punti** richiede l'applicazione di una riduzione polinomiale di Karp su grafi o formule concrete.

### Pattern A: Riduzione da CLIQUE a VERTEX-COVER
* **Costruzione**: Il grafo di destinazione $G'$ è il **complementare** del grafo originale $G$ ($G' = \bar{G}$).
* **Relazione**: Una clique di dimensione $k$ in $G$ corrisponde biunivocamente a un vertex cover di dimensione $|V| - k$ in $G'$.
* **Esercizi correlati**: [[exam_2025_02_11_p2_completo_recupero_e02]], [[exam_2025_06_09_p2_e02]], [[exam_2025_07_03_p2_e02]], [[exam_2026_01_12_e04]].

### Pattern B: Riduzione da 3-SAT a CLIQUE
* **Costruzione**: Grafo a gadget in cui ogni clausola è un insieme di 3 nodi indipendenti. Gli archi collegano letterali di clausole diverse che non sono complementari.
* **Esercizi correlati**: [[exam_2025_11_10_p2_e02]], [[exam_2025_01_13_p2_e02]], [[exam_2025_09_17_p2_e02]].

---

## 3. Formazione di Equazioni di Ricorrenza

Un esercizio da **7 punti** richiede di formulare le ricorrenze per un problema classico di ottimizzazione.

* **Zaino 0/1 (Knapsack 0/1)**: Richiede la definizione di $OPT(i,c)$, i casi base ($OPT(0,c)=0$ e $OPT(i,0)=0$) e il passo ricorsivo con la scelta binaria $\max$ di inclusione/esclusione.
  - *Esercizio correlato*: [[exam_2025_02_11_p2_completo_recupero_e03]].
* **Chiusura Transitiva (Warshall)**: Richiede la ricorrenza booleana $e_{i,j}^{(k)} = e_{i,j}^{(k-1)} \lor (e_{i,k}^{(k-1)} \land e_{k,j}^{(k-1)})$ spiegando accuratamente il significato dell'indice intermedio $k$.
  - *Esercizi correlati*: [[exam_2025_11_10_p2_e03]], [[exam_2025_07_03_p2_e03]], [[exam_2025_01_13_p2_e03]].

---

## 4. Dimostrazioni Teoriche e Domande Premiali

Ciascun appello contiene domande teoriche principali (**7 punti**) e domande bonus premiali (**3 punti bonus**, una a scelta dello studente).

### Le Cinque Grandi Dimostrazioni della Parte II:
1. **Teorema dell'arco sicuro (Safe Edge Theorem)**:
   - *Frequenza*: Altissima.
   - *Dimostrazione*: Tramite lo scambio di un arco del ciclo indotto dall'arco leggero con quest'ultimo, provando che il peso dell'albero non aumenta.
   - *Metodo*: [[metodo_teorema_arco_sicuro]].
   - *Esercizi*: [[exam_2025_02_11_p2_completo_recupero_e05]], [[exam_2025_07_03_p2_e05]].
2. **Dimostrazione del Matroide Grafico**:
   - *Frequenza*: Altissima.
   - *Dimostrazione*: Prova che il sistema $(E,\mathcal{F})$ delle foreste di un grafo è un matroide, con verifica accurata dell'Assioma di Scambio tramite componenti connesse disgiunte.
   - *Metodo*: [[metodo_dimostrazione_matroide_grafico]].
   - *Esercizi*: [[exam_2025_11_10_p2_e05]], [[exam_2025_06_09_p2_e05]], [[exam_2025_01_13_p2_e05]], [[exam_2025_09_17_p2_e05]].
3. **Correttezza di Greedy-max su Matroidi (Rado-Edmonds)**:
   - *Frequenza*: Alta (spesso come bonus).
   - *Dimostrazione*: Per assurdo, ordinando gli elementi e supponendo che esista un prima elemento in cui la scelta greedy ha peso minore della scelta ottima, applicando poi la proprietà di scambio.
   - *Metodo*: [[metodo_greedy_matroidi_rado]].
   - *Esercizi*: [[exam_2025_02_11_p2_completo_recupero_bonus]] (Opzione 1), [[exam_2026_01_12_bonus_matroidi]], [[exam_2025_01_13_p2_bonus]] (Opzione 2), [[exam_2025_09_17_p2_e03]].
4. **Correttezza di Dijkstra**:
   - *Frequenza*: Media (spesso come bonus).
   - *Dimostrazione*: Per assurdo tramite invariante di ciclo, considerando il primo nodo estratto fuori da $S$ per cui la stima non coincide con la distanza minima reale.
   - *Metodo*: [[metodo_dimostrazione_correttezza_dijkstra]].
   - *Esercizi*: [[exam_2025_02_11_p2_completo_recupero_bonus]] (Opzione 3).
5. **Riducibilità CLIQUE $\le_p$ VERTEX-COVER**:
   - *Frequenza*: Alta (spesso come bonus).
   - *Dimostrazione*: Prova formale bilaterale che $V'$ è una clique in $G$ se e solo se $V \setminus V'$ è una copertura di vertici nel complementare $\bar{G}$.
   - *Esercizi*: [[exam_2025_02_11_p2_completo_recupero_bonus]] (Opzione 2), [[exam_2025_01_13_p2_bonus]] (Opzione 4).
