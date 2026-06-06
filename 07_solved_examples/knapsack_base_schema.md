# Schema — Zaino 0/1 base (Knapsack 0/1)

Questo schema mostra come impostare e risolvere in modo ordinato un esercizio di tipo **Zaino 0/1 base** in sede d'esame.

---

## Esempio di Istanza d'Esame

Consideriamo un'istanza tipica:
- **Oggetti**: $X = \{1, 2, 3, 4\}$ (quindi $n = 4$)
- **Pesi (ingombri)**: $w_1 = 2, w_2 = 1, w_3 = 3, w_4 = 2$
- **Valori (profitti)**: $v_1 = 12, v_2 = 10, v_3 = 20, v_4 = 15$
- **Capacità dello zaino**: $W = 5$

---

## 1. Definizione dei Sottoproblemi (Pilastro 1)

Definiamo il coefficiente:
* $V[i, p]$: massimo valore totale ottenibile scegliendo un sottoinsieme dei primi $i$ oggetti (tra $1$ e $i$) che non superi la capacità residua $p$.
* Indici: $i \in \{0, 1, \dots, 4\}$, $p \in \{0, 1, \dots, 5\}$.

---

## 2. Casi Base (Pilastro 2)

* $V[0, p] = 0 \quad \forall p \in \{0, \dots, 5\}$
* $V[i, 0] = 0 \quad \forall i \in \{0, \dots, 4\}$

---

## 3. Passo Ricorsivo (Pilastro 3)

Per $i \ge 1, p \ge 1$:
$$
V[i, p] =
\begin{cases}
V[i-1, p] & \text{se } w_i > p \\
\max\{V[i-1, p], \ V[i-1, p-w_i] + v_i\} & \text{se } w_i \le p
\end{cases}
$$

---

## 4. Matrice DP Costruita (Bottom-Up)

Risolvendo i sottoproblemi riga per riga (da $i=1$ a $n$ e per $p=1$ a $W$):

| $i$ \ $p$ | 0 | 1 | 2 | 3 | 4 | 5 (Capacità $W$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** (nessuno) | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** ($w_1=2, v_1=12$) | 0 | 0 | 12 | 12 | 12 | 12 |
| **2** ($w_2=1, v_2=10$) | 0 | 10 | 12 | 22 | 22 | 22 |
| **3** ($w_3=3, v_3=20$) | 0 | 10 | 12 | 22 | 30 | **32** |
| **4** ($w_4=2, v_4=15$) | 0 | 10 | 15 | 25 | 30 | **37** |

*Nota*: Il valore ottimo finale si trova in $V[4, 5] = 37$.

---

## 5. Algoritmo di Ricostruzione (Backtracking)

Ricostruiamo la soluzione a partire da $i = 4, p = 5$:

1. **Passo $i=4, p=5$**: 
   - $V[4,5] = 37$. Il ramo "non prendo" sarebbe $V[3,5] = 32$.
   - Poiché $V[4,5] \ne V[3,5]$, **l'oggetto 4 viene preso**.
   - Aggiorniamo la capacità: $p \leftarrow 5 - w_4 = 5 - 2 = 3$.
   - Passiamo a $i = 3$.

2. **Passo $i=3, p=3$**:
   - $V[3,3] = 22$. Il ramo "non prendo" sarebbe $V[2,3] = 22$.
   - Poiché $V[3,3] = V[2,3]$, **l'oggetto 3 non viene preso**.
   - La capacità resta $p = 3$.
   - Passiamo a $i = 2$.

3. **Passo $i=2, p=3$**:
   - $V[2,3] = 22$. Il ramo "non prendo" sarebbe $V[1,3] = 12$.
   - Poiché $V[2,3] \ne V[1,3]$, **l'oggetto 2 viene preso**.
   - Aggiorniamo la capacità: $p \leftarrow 3 - w_2 = 3 - 1 = 2$.
   - Passiamo a $i = 1$.

4. **Passo $i=1, p=2$**:
   - $V[1,2] = 12$. Il ramo "non prendo" sarebbe $V[0,2] = 0$.
   - Poiché $V[1,2] \ne V[0,2]$, **l'oggetto 1 viene preso**.
   - Aggiorniamo la capacità: $p \leftarrow 2 - w_1 = 2 - 2 = 0$.
   - Arresto (capacità nulla).

### Soluzione Ottima:
* **Oggetti scelti**: $S = \{1, 2, 4\}$
* **Valore totale**: $v_1 + v_2 + v_4 = 12 + 10 + 15 = 37$
* **Peso totale**: $w_1 + w_2 + w_4 = 2 + 1 + 2 = 5 \le 5$

---

## Collegamenti

- Teoria: [[zaino_01]]
- Metodo: [[metodo_programmazione_dinamica_zaino_01]]
- Esempio variante con colori: [[knapsack_al_massimo_3_rossi_schema]]
