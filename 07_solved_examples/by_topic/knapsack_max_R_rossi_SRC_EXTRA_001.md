---
type: solved_example
source_id: SRC-EXTRA-001
status: complete
tags: [apa, esempio-svolto, zaino-01, colori]
---

# Knapsack con massimo R oggetti rossi - SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 13-14 e 16-17.

## Sottoproblema

$$
OPT_{i,c,r} = \text{valore massimo usando i primi } i \text{ oggetti, capacita } c \text{ e al massimo } r \text{ rossi}.
$$

## Passo chiave

Se l'oggetto $i$ e rosso e $r>0$:

$$
OPT_{i,c,r}=\max(OPT_{i-1,c,r},OPT_{i-1,c-w_i,r-1}+v_i).
$$

Se l'oggetto non e rosso:

$$
OPT_{i,c,r}=\max(OPT_{i-1,c,r},OPT_{i-1,c-w_i,r}+v_i).
$$

Metodo: [[metodo_programmazione_dinamica_zaino_01]].

