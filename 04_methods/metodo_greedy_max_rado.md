---
type: method
topic: Greedy-Max and Rado Theorem
status: draft
tags:
  - apa
  - metodo
  - topic/greedy
  - topic/matroidi
  - topic/sistemi_indipendenza
---

# Metodo - Algoritmo GREEDY-MAX e Teorema di Rado

## Quando si usa

Questo metodo si applica quando viene richiesto di scrivere formalmente l'algoritmo **GREEDY-MAX** associato a un sistema di indipendenza $(E,F)$ ed enunciare il **Teorema di Rado** (caratterizzazione della correttezza del greedy).

## Riconoscimento rapido

> [!Info]
> Segnali che indicano che questo esercizio usa questo metodo:
> - Richiesta di definire l'algoritmo greedy su sistemi di indipendenza.
> - Richiesta di enunciare il Teorema di Rado (caratterizzazione per cui il greedy fornisce soluzioni ottime).

---

## 1. Algoritmo GREEDY-MAX

Dato un sistema di indipendenza $(E,F)$ (dove $E$ è l'insieme finito degli elementi e $F \subseteq 2^E$ è la famiglia dei sottoinsiemi indipendenti, ereditari per inclusione) e una funzione peso non negativa sugli elementi $w: E \to \mathbb{R}^+$:

### Pseudocodice Formale

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

## 2. Enunciato del Teorema di Rado

Sia $(E,F)$ un **sistema di indipendenza** (ovvero un sistema di insiemi non vuoto ed ereditario: se $A \in F$ e $B \subseteq A \implies B \in F$).

L'algoritmo **GREEDY-MAX** restituisce un sottoinsieme indipendente $I \in F$ di peso massimo per **qualsiasi** funzione peso non negativa $w: E \to \mathbb{R}^+$ se e solo se la coppia $(E,F)$ è un **matroide** (ovvero soddisfa l'Assioma di Scambio).

> [!Important]
> Il Teorema di Rado stabilisce un'equivalenza logica bilaterale (*se e solo se*): 
> 1. Se $(E,F)$ è un matroide, allora GREEDY-MAX trova sempre l'ottimo.
> 2. Se GREEDY-MAX trova sempre l'ottimo per qualsiasi peso $w$, allora $(E,F)$ è necessariamente un matroide.

---

## Esercizi collegati

- [[exam_2025_06_09_p2_e03]]
- [[exam_2026_01_12_bonus_matroidi]] (collegato per dimostrazione correttezza greedy)

## Errori comuni

> [!Warning]
> Dimenticare di specificare che gli elementi di $E$ devono essere ordinati in ordine *non crescente* ($w(e_1) \ge w(e_2) \ge \dots$).
> Formulare il Teorema di Rado in modo unilaterale, dimenticando il "se e solo se". La forza del teorema risiede proprio nella caratterizzazione esatta dei matroidi.
