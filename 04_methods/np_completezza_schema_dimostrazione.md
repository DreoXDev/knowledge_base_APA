---
type: method
status: complete
source_id: SRC-NOTE-001
tags: [apa, metodo, np-completezza, riduzioni]
---

# Schema per dimostrare NP-completezza

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 40-50.

## 1. Mostrare che il problema e in NP

Descrivere un certificato di dimensione polinomiale e un algoritmo verificatore polinomiale.

## 2. Scegliere un problema NP-completo noto

Esempi ricorrenti: SAT, 3-SAT, CLIQUE, VERTEX-COVER.

## 3. Definire la trasformazione polinomiale

Costruire, da un'istanza di $B$, un'istanza di $A$ in tempo polinomiale.

## 4. Dimostrare se e solo se

Dimostrare:

$$
x\in B \iff f(x)\in A.
$$

## 5. Concludere la NP-completezza

Poiche $A\in NP$ e $B\le_p A$ con $B$ NP-completo, allora $A$ e NP-completo.

## Errori comuni

- Dimostrare solo un verso.
- Non mostrare appartenenza a NP.
- Ridurre nel verso sbagliato.
- Dire "e difficile" senza una riduzione.
