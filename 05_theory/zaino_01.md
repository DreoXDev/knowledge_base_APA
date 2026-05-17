---
type: theory
topic: Knapsack 0/1
status: complete
tags:
  - apa
  - teoria
  - topic/programmazione_dinamica
  - topic/zaino-01
---

# Teoria — Zaino 0/1 (Knapsack 0/1)

## Definizione del Problema

Il problema dello **Zaino 0/1** (Knapsack 0/1) è un classico problema di ottimizzazione combinatoria NP-hard.

Dato:
- Un budget o capacità dello zaino $C \in \mathbb{N}, C > 0$.
- Un insieme $X = \{1, 2, \dots, n\}$ di $n$ oggetti.
- Per ogni oggetto $i \in X$:
  - Un valore o profitto $v_i \in \mathbb{N}, v_i > 0$.
  - Un ingombro o peso $w_i \in \mathbb{N}, w_i > 0$.

L'obiettivo è selezionare un sottoinsieme di oggetti $S \subseteq X$ tale che la somma dei loro pesi non superi la capacità $C$ e la somma dei loro valori sia massimizzata:

$$\text{Massimizzare } \sum_{i \in S} v_i$$
$$\text{soggetto a } \sum_{i \in S} w_i \le C$$

Il vincolo "0/1" indica che ogni oggetto può essere selezionato al massimo una volta ($i \in S$ oppure $i \notin S$), a differenza del *Fractional Knapsack* (risolvibile in tempo greedy polinomiale) dove gli oggetti possono essere frazionati.

---

## Complessità Computazionale

* **NP-completezza**: La versione di decisione dello Zaino 0/1 ("Esiste un sottoinsieme di oggetti con peso $\le C$ e valore $\ge K$?") è uno dei 21 problemi NP-completi di Karp.
* **Pseudopolinomialità**: Sebbene sia NP-completo, il problema è risolvibile in tempo **pseudopolinomiale** $O(nC)$ tramite la programmazione dinamica. Se la capacità $C$ è rappresentata in notazione unaria (o se $C$ è polinomialmente limitato rispetto a $n$), il tempo di esecuzione è polinomiale.

---

## Formulazione con Programmazione Dinamica (Bottom-Up)

Definiamo $OPT(i, c)$ come il valore massimo che si può ottenere considerando solo gli oggetti $\{1, \dots, i\}$ con capacità dello zaino pari a $c$.

### 1. Casi Base
* Nessun oggetto a disposizione ($i = 0$): il valore ottimo è 0 per qualsiasi capacità.
  $$OPT(0, c) = 0 \quad \forall c \in \{0, \dots, C\}$$
* Capacità residua nulla ($c = 0$): non è possibile inserire alcun oggetto, quindi il valore ottimo è 0.
  $$OPT(i, 0) = 0 \quad \forall i \in \{0, \dots, n\}$$

### 2. Equazioni di Ricorrenza
Per ogni oggetto $i \ge 1$ e capacità $c \ge 1$:

$$
OPT(i, c) =
\begin{cases}
OPT(i-1, c) & \text{se } w_i > c \\
\max\{OPT(i-1, c), \ OPT(i-1, c-w_i) + v_i\} & \text{se } w_i \le c
\end{cases}
$$

### 3. Ricostruzione della Soluzione
Per determinare l'insieme ottimo $S$, possiamo eseguire un backtracking a partire dalla cella $(n, C)$:

```python
i = n
c = C
S = []
while i > 0 and c > 0:
    if OPT[i][c] != OPT[i-1][c]:
        S.append(i)
        c -= w[i]
    i -= 1
```

---

## Collegamenti agli esercizi catalogati

- [[exam_2026_01_12_e05]] (Zaino 0/1 classico in Parte II)
- [[exam_2026_01_12_e01]] (Zaino 0/1 con vincolo di presenza di almeno un elemento rosso in Parte I)
- [[exam_2025_02_11_p2_completo_recupero_e03]] (Equazioni di ricorrenza standard per Zaino 0/1 in Parte II)
