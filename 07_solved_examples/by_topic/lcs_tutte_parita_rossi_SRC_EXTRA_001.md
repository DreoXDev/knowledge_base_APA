---
type: solved_example
source_id: SRC-EXTRA-001
status: draft
tags: [apa, esempio-svolto, lcs, colori, parita]
---

# Tutte le LCS hanno numero pari di rossi - SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 08-10.

## Convenzione normalizzata

$$
p=0 \text{ pari},\qquad p=1 \text{ dispari}.
$$

## Sottoproblema

$$
B_{i,j,p}=true
$$

se tutte le LCS ottime di $X_i,Y_j$ hanno parita $p$ del numero di rossi.

## Passo chiave

- Match rosso: si inverte la parita.
- Match non rosso: si mantiene la parita.
- Mismatch: si combinano con AND solo i rami che restano ottimi.

> [!Warning]
> Le pagine 08-10 sembrano avere convenzioni di parita non uniformi. Verificare prima dell'uso in esame.

