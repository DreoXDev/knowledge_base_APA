---
type: method
status: draft
source_id: SRC-EXTRA-001
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/parita
---

# Metodo - LCS con alternanza pari/dispari

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 17-18.

> [!Warning]
> Nota draft da fonte manoscritta. Per la variante ufficiale "dispari in posizioni dispari e pari in posizioni pari" usare [[dp_lcs_dispari_pari_alternati]].

## Quando si usa

Quando si cerca una LCS in cui gli elementi scelti alternano parita pari e dispari.

## Stato minimo consigliato

La fonte parte da $C_{i,j}$, ma la ricorrenza manoscritta suggerisce che serva ricordare la parita dell'ultimo elemento scelto:

$$
C_{i,j,p} = \text{lunghezza di una LCS alternante di } X_i,Y_j \text{ che termina con parita } p.
$$

## Schema operativo sicuro

- Se $x_i\ne y_j$, si confrontano i rami $i-1,j$ e $i,j-1$.
- Se $x_i=y_j$, si puo prendere il match solo se la parita del predecessore e opposta.
- La soluzione finale e un massimo tra gli stati di parita finali.

> [!Warning]
> La ricorrenza del manoscritto e incompleta. Questa nota e volutamente draft e non va usata come formula definitiva.

> [!Todo]
> Mantenere questa nota solo come confronto storico con SRC-EXTRA-001; la fonte primaria RAG e [[dp_lcs_dispari_pari_alternati]].
