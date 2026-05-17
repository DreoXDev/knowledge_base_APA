---
type: theory
topic: np-completezza
status: draft
tags:
  - apa
  - teoria
  - topic/np-completezza
---

# Teoria — NP-completezza e complessità computazionale

## Classi di complessità principali

### 1. La classe P
La classe **P** contiene tutti i problemi decisionali che possono essere risolti da un algoritmo deterministico in tempo polinomiale, ovvero in tempo $O(n^k)$ per qualche costante intera $k$, dove $n$ è la dimensione dell'input.
- Rappresenta i problemi considerati computazionalmente "trattabili".

### 2. La classe NP
La classe **NP** (Non-deterministic Polynomial-time) contiene tutti i problemi decisionali per cui una risposta "sì" può essere **verificata** in tempo polinomiale da un algoritmo deterministico, dato un opportuno "certificato" (o testimone) di lunghezza polinomiale.
- Equivalentemente, è la classe dei problemi decisionali risolvibili da una macchina di Turing non deterministica in tempo polinomiale.
- Vale banalmente che $P \subseteq NP$.

### 3. NP-durezza (NP-hard)
Un problema $A$ (non necessariamente in NP o decisionale) è **NP-difficile** (NP-hard) se ogni problema in NP è riducibile polinomiale ad esso. Ovvero:
$$\forall B \in NP, \quad B \le_p A$$
Questo significa che il problema è "almeno altrettanto difficile" di qualsiasi problema in NP.

### 4. NP-completezza (NP-complete)
Un problema decisionale $A$ è **NP-completo** se soddisfa contemporaneamente due condizioni:
1. Appartiene ad NP: $A \in NP$.
2. È NP-difficile: $A \text{ è NP-hard}$ (ovvero, $\forall B \in NP$, $B \le_p A$).

---

## Riduzione polinomiale di Karp ($B \le_p A$)

La riduzione polinomiale (o riduzione di Karp) da un problema decisionale $B$ a un problema decisionale $A$ è una funzione $f: \Sigma^* \to \dots$ computabile in tempo polinomiale tale che, per ogni istanza $x$:
$$x \in B \iff f(x) \in A$$

> [!Important]
> Per dimostrare che un nuovo problema $A$ è NP-completo:
> 1. Dimostrare che $A \in NP$ (fornendo un certificato polinomiale e un algoritmo di verifica polinomiale).
> 2. Scegliere un problema $B$ **già noto** per essere NP-completo e mostrare una riduzione polinomiale da $B$ ad $A$ ($B \le_p A$).

---

## Collegamenti agli esercizi

- [[exam_2026_01_12_e04]] (Riduzione CLIQUE to VC)
- [[exam_2026_01_12_e06]] (Dimostrazione CLIQUE NPC)
- [[exam_2025_07_03_p2_e02]] (Riduzione CLIQUE to VC)
- [[exam_2025_07_03_p2_e04]] (Definizioni P, NP, NPC)
- [[exam_2025_06_09_p2_e02]] (Riduzione CLIQUE to VC)
- [[exam_2025_06_09_p2_e04]] (Teoria: Requisiti per NP-completezza)

---

## Collegamenti ai metodi

- [[metodo_riduzione_clique_vertex_cover]]
- [[metodo_dimostrare_np_completezza]]
