---
type: theory
topic: matroidi
status: draft
tags:
  - apa
  - teoria
  - topic/greedy
  - topic/matroidi
---

# Teoria — Matroidi e Algoritmi Greedy

## Definizione di Matroide

Un **matroide** è una coppia ordinata $M = (E, F)$ dove:
- $E$ è un insieme finito di elementi (detto insieme di base).
- $F$ è una famiglia non vuota di sottoinsiemi di $E$ (chiamati sottoinsiemi indipendenti) che soddisfa i seguenti due assiomi fondamentali:

### Assioma 1: Assioma del sottoinsieme (Ereditarietà)
Se $A \in F$ e $B \subseteq A$, allora anche $B \in F$.
- Questo significa che qualsiasi sottoinsieme di un insieme indipendente è a sua volta indipendente.
- Una coppia $(E,F)$ che soddisfa solo questo assioma è chiamata **sistema di indipendenza**.

### Assioma 2: Assioma di scambio (Exchange Property)
Se $A, B \in F$ e $|A| < |B|$, allora esiste almeno un elemento $x \in B \setminus A$ tale che:
$A \cup \{x\} \in F$
- Questo significa che se abbiamo due insiemi indipendenti di dimensioni diverse, possiamo sempre estendere quello più piccolo con un elemento di quello più grande mantenendo l'indipendenza.

---

## Esempi principali di Matroidi

### 1. Matroide Grafico
Dato un grafo non orientato $G = (V,E)$:
- $E$ sono gli archi del grafo.
- $F = \{ I \subseteq E \mid (V,I) \text{ è una foresta (priva di cicli)} \}$.
- Le basi (insiemi indipendenti massimali) sono gli alberi di copertura (Spanning Trees) del grafo (se $G$ è connesso).

### 2. Matroide Matriciale (o Lineare)
Data una matrice $A$ su un campo:
- $E$ sono le colonne della matrice.
- $F = \{ I \subseteq E \mid \text{le colonne in } I \text{ sono linearmente indipendenti} \}$.

---

## Proprietà e Teoremi Fondamentali

### Basi di un Matroide
Tutti gli insiemi indipendenti massimali (chiamati **basi** del matroide) hanno la stessa identica cardinalità.
- Nel caso del matroide grafico, tutte le basi (alberi di copertura) hanno esattamente $|V| - 1$ archi.

### Funzione Rango
La funzione rango $r: 2^E \to \mathbb{N}$ associa ad ogni sottoinsieme $X \subseteq E$ la dimensione massima di un sottoinsieme indipendente contenuto in $X$.

### Il Teorema di Rado
Sia $(E,F)$ un sistema di indipendenza. L'algoritmo **GREEDY-MAX** restituisce una soluzione ottimale per qualsiasi funzione peso non negativa $w: E \to \mathbb{R}^+$ se e solo se $(E,F)$ è un **matroide**.

---

## Collegamenti agli esercizi

- [[exam_2026_01_12_bonus_matroidi]] (Correttezza greedy su matroidi)
- [[exam_2025_07_03_p2_e05]] (Teorema dell'arco sicuro per MST)
- [[exam_2025_06_09_p2_e03]] (GREEDY-MAX e Rado)
- [[exam_2025_06_09_p2_e05]] (Dimostrazione matroide grafico)

---

## Collegamenti ai metodi

- [[metodo_greedy_max_rado]]
- [[metodo_dimostrazione_matroide_grafico]]
- [[metodo_teorema_arco_sicuro]]
