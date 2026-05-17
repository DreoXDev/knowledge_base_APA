---
type: method
topic: Greedy su Matroidi e Teorema di Rado-Edmonds
status: complete
tags:
  - apa
  - metodo
  - topic/greedy
  - topic/matroidi
  - topic/sistemi_indipendenza
---

# Metodo — Algoritmo Greedy su Matroidi e Dimostrazione (Rado-Edmonds)

## Quando si usa

Questo metodo si applica quando l'esercizio richiede di:
1. Definire l'algoritmo **GREEDY-MAX** per un sistema di indipendenza.
2. Enunciare il **Teorema di Rado-Edmonds** (caratterizzazione della correttezza del greedy).
3. Dimostrare formalmente che se un sistema di indipendenza $(E, \mathcal{F})$ è un matroide, l'algoritmo Greedy-max restituisce sempre una soluzione ottima.

---

## 1. Algoritmo GREEDY-MAX

Sia $(E,\mathcal{F})$ un sistema di indipendenza (dove $E$ è l'insieme finito degli elementi e $\mathcal{F} \subseteq 2^E$ è la famiglia dei sottoinsiemi indipendenti, ereditari per inclusione) e una funzione peso non negativa $w: E \to \mathbb{R}^+ \cup \{0\}$.

```txt
Algoritmo GREEDY-MAX(E, F, w)
Input: 
  - Un sistema di indipendenza (E, F)
  - Una funzione peso w: E -> R+
Output:
  - Un sottoinsieme indipendente I in F che tenta di massimizzare w(I) = sum_{e in I} w(e)

Passaggi:
1. Ordinare gli elementi di E = {e_1, e_2, ..., e_n} in ordine di peso non crescente, ovvero:
   w(e_1) >= w(e_2) >= ... >= w(e_n)
2. Inizializzare la soluzione parziale I:
   I = vuoto
3. Per i = 1 fino a n fare:
     Se (I unione {e_i}) appartiene a F allora:
       I = I unione {e_i}
4. Ritornare I
```

---

## 2. Enunciato del Teorema di Rado-Edmonds

> **Teorema**:
> Sia $(E,\mathcal{F})$ un sistema di indipendenza.
> L'algoritmo **GREEDY-MAX** restituisce un sottoinsieme indipendente $I \in \mathcal{F}$ di peso massimo per **qualsiasi** funzione peso non negativa $w: E \to \mathbb{R}^+$ se e solo se la coppia $(E,\mathcal{F})$ è un **matroide**.

---

## 3. Dimostrazione (Se $(E, \mathcal{F})$ è un matroide $\implies$ Greedy-max è Ottimo)

Sia $(E,\mathcal{F})$ un matroide. Siano gli elementi di $E$ ordinati in ordine non crescente di peso:
$$w(e_1) \ge w(e_2) \ge \dots \ge w(e_n)$$

Sia $G = \{g_1, g_2, \dots, g_k\}$ la soluzione restituita dall'algoritmo Greedy-max, dove gli elementi sono ordinati secondo l'ordine di inserimento (che rispetta l'ordinamento decrescente dei pesi).

Sia $O = \{o_1, o_2, \dots, o_m\}$ una qualunque soluzione ottima (un sottoinsieme indipendente in $\mathcal{F}$ di peso massimo). Poiché in un matroide tutti i sottoinsiemi indipendenti massimali (basi) hanno la stessa cardinalità, si ha necessariamente:
$$k = m$$

Ordiniamo gli elementi di $O = \{o_1, \dots, o_k\}$ in modo tale che i loro pesi siano non crescenti:
$$w(o_1) \ge w(o_2) \dots \ge w(o_k)$$

### Tesi
Vogliamo dimostrare che:
$$w(g_i) \ge w(o_i) \quad \forall i \in \{1, 2, \dots, k\}$$
Se questo è vero, allora sommando su tutti gli elementi si ha:
$$\sum_{i=1}^k w(g_i) \ge \sum_{i=1}^k w(o_i) \implies w(G) \ge w(O)$$
Essendo $O$ ottima, ne consegue che $w(G) = w(O)$, cioè la soluzione greedy è ottima.

---

### Dimostrazione per Assurdo (della Tesi)

Supponiamo per assurdo che la tesi non sia vera. Sia $p \in \{1, \dots, k\}$ il **primo** indice per cui si ha:
$$w(g_p) < w(o_p)$$

Definiamo due sottoinsiemi di elementi:
* $G_{p-1} = \{g_1, g_2, \dots, g_{p-1}\}$ (i primi $p-1$ elementi scelti da Greedy, con $G_0 = \emptyset$).
* $O_p = \{o_1, o_2, \dots, o_p\}$ (i primi $p$ elementi della soluzione ottima).

Valutiamo le cardinalità dei due insiemi:
* $|G_{p-1}| = p-1$
* $|O_p| = p$

Essendo $(E,\mathcal{F})$ un matroide, e poiché sia $G_{p-1}$ che $O_p$ sono insiemi indipendenti in $\mathcal{F}$ (essendo sottoinsiemi di insiemi indipendenti), possiamo applicare l'**Assioma di Scambio (Proprietà di Estensione)**:

> Poiché $|O_p| > |G_{p-1}|$, esiste un elemento $o^* \in O_p \setminus G_{p-1}$ tale che:
> $$G_{p-1} \cup \{o^*\} \in \mathcal{F}$$

Sia $o^* = o_j$ per qualche indice $j \le p$. 
Poiché gli elementi in $O$ sono ordinati per peso non crescente, si ha:
$$w(o^*) \ge w(o_p)$$

Unendo questa relazione alla nostra ipotesi di assurdo ($w(o_p) > w(g_p)$), ricaviamo:
$$w(o^*) > w(g_p)$$

### Contradizione logica dell'algoritmo Greedy

Valutiamo il comportamento dell'algoritmo Greedy al momento in cui ha preso in considerazione l'elemento $o^*$:
1. Poiché $w(o^*) > w(g_p)$, l'elemento $o^*$ ha un peso strettamente maggiore di $g_p$.
2. Di conseguenza, l'algoritmo Greedy deve aver esaminato l'elemento $o^*$ in un'iterazione precedente a quella in cui ha inserito $g_p$ (o al più nella stessa iterazione, se avessero lo stesso peso, ma qui il peso è strettamente maggiore).
3. Sia $G'$ la soluzione parziale accumulata da Greedy subito prima di esaminare $o^*$. Poiché $o^*$ è stato esaminato prima di inserire $g_p$, si ha:
   $$G' \subseteq G_{p-1}$$
4. Per la proprietà di ereditarietà dei matroidi, poiché $G_{p-1} \cup \{o^*\} \in \mathcal{F}$, allora anche:
   $$G' \cup \{o^*\} \in \mathcal{F}$$
5. Questo implica che quando Greedy ha esaminato $o^*$, il test di indipendenza ha avuto esito positivo. L'algoritmo avrebbe **dovuto** inserire $o^*$ nella sua soluzione parziale.
6. Tuttavia, per costruzione $o^* \in O_p \setminus G_{p-1}$, il che significa che $o^*$ **non** fa parte della soluzione greedy final (e in particolare non è in $G_{p-1}$).

Questa è una contraddizione insostenibile. Di conseguenza, l'ipotesi di assurdo è falsa, il che dimostra la tesi:
$$w(g_i) \ge w(o_i) \quad \forall i \implies w(G) = w(O)$$

L'algoritmo Greedy-max restituisce una soluzione ottima. ($\text{Q.E.D.}$)

---

## Esercizi collegati

- [[exam_2025_02_11_p2_completo_recupero_bonus]] (Richiesta esplicita come domanda bonus 1)
- [[exam_2026_01_12_bonus_matroidi]] (Richiesta analoga)
- [[exam_2025_06_09_p2_e03]] (Definizione di GREEDY-MAX e Rado)
