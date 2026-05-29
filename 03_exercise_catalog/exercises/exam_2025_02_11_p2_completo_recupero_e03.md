---
type: exercise
exam: 2025-02-11 Parte II completo/recupero
exercise_number: 3
topic:
  - programmazione_dinamica
  - zaino
  - equazioni_ricorrenza
difficulty: easy-medium
status: cataloged
method:
  - [[metodo_programmazione_dinamica_zaino_01]]
---

# Esercizio 3 — Equazioni di ricorrenza per Knapsack 0/1

## Testo

Siano dati $C \in \mathbb{N}$ ($C > 0$) e un insieme $X = \{1, \dots, n\}$ di oggetti tali che ad ogni oggetto $i$ è associato un valore $v_i \in \mathbb{N}$ ed un ingombro $w_i \in \mathbb{N}$, $v_i > 0$ e $w_i > 0$.

Mediante programmazione dinamica, si vuole determinare il valore complessivo di un sottoinsieme $S$ di $X$ di valore complessivo massimo e di ingombro complessivo al più $C$ (**Knapsack 0/1**).

Scrivere le equazioni di ricorrenza per trovare tale valore ottimo, indicando in esse con $OPT(i,c)$ il coefficiente relativo al generico sottoproblema $(i,c)$.

---

## Risoluzione

### 1. Definizione Formale del Coefficiente
Definiamo il coefficiente $OPT(i,c)$ della matrice di programmazione dinamica come:
$$OPT(i,c) = \text{valore massimo ottenibile selezionando un sottoinsieme di oggetti tra i primi } i \text{ oggetti (1, ..., } i\text{) con capacità massima residua } c$$
Per ogni $i \in \{0, 1, \dots, n\}$ e per ogni $c \in \{0, 1, \dots, C\}$.

---

### 2. Equazioni di Ricorrenza

#### Casi Base
* **Capacità nulla ($c = 0$)**: Se la capacità residua dello zaino è 0, non è possibile inserire alcun oggetto (essendo tutti gli ingombri $w_i > 0$). Il valore ottimo è nullo:
  $$OPT(i, 0) = 0 \quad \forall i \in \{0, 1, \dots, n\}$$
* **Zero oggetti ($i = 0$)**: Se non abbiamo oggetti a disposizione tra cui scegliere, il valore ottimo è nullo indipendente dalla capacità dello zaino:
  $$OPT(0, c) = 0 \quad \forall c \in \{0, 1, \dots, C\}$$

#### Passo Ricorsivo ($i \ge 1$, $c \ge 1$)
Per calcolare il valore ottimo $OPT(i,c)$ esaminando l'oggetto $i$-esimo (con peso $w_i$ e valore $v_i$), abbiamo due scenari:

1. **L'oggetto $i$ supera la capacità residua ($w_i > c$)**:
   In questo caso, l'oggetto $i$ non può essere fisicamente inserito nello zaino. Il valore massimo si riduce al valore ottimo calcolato considerando solo i primi $i-1$ oggetti:
   $$OPT(i,c) = OPT(i-1, c)$$

2. **L'oggetto $i$ è compatibile con la capacità residua ($w_i \le c$)**:
   Abbiamo la scelta se includere o escludere l'oggetto $i$:
   - *Se escludiamo l'oggetto $i$*: il valore massimo rimane $OPT(i-1, c)$.
   - *Se includiamo l'oggetto $i$*: otteniamo il valore dell'oggetto $v_i$ più il valore massimo ricavato inserendo i primi $i-1$ oggetti nella capacità rimanente $c - w_i$, ossia $OPT(i-1, c-w_i) + v_i$.
   
   Scegliamo l'opzione che massimizza il profitto:
   $$OPT(i,c) = \max\{OPT(i-1, c), \ OPT(i-1, c-w_i) + v_i\}$$

#### Formulazione Unificata del Passo Ricorsivo
$$
OPT(i,c) =
\begin{cases}
OPT(i-1, c) & \text{se } w_i > c \\
\max\{OPT(i-1, c), \ OPT(i-1, c-w_i) + v_i\} & \text{se } w_i \le c
\end{cases}
$$

---

### 3. Soluzione Ottima Finale
La soluzione ottima finale che rappresenta il massimo valore ottenibile considerando tutti gli $n$ oggetti con la capacità massima totale $C$ è memorizzata nella cella:
$$\text{Soluzione Finale} = OPT(n, C)$$
