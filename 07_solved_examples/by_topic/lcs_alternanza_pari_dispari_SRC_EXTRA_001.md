---
type: solved_example
source_id: SRC-EXTRA-001
status: draft
tags: [apa, esempio-svolto, lcs, parita]
---

# LCS con alternanza pari/dispari - SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 17-18.

> [!Warning]
> Esempio draft da fonte manoscritta. Per la variante ufficiale "dispari in posizioni dispari e pari in posizioni pari" usare [[lcs_dispari_pari_alternati_schema]] e [[dp_lcs_dispari_pari_alternati]].

## Problema

Trovare una LCS in cui i valori scelti alternano parita pari e dispari.

## Stato da verificare

$$
C_{i,j,p}
$$

dove $p$ rappresenta la parita dell'ultimo elemento scelto.

> [!Warning]
> La fonte non basta per completare la ricorrenza. Non usare questa nota come soluzione definitiva.

> [!Todo]
> Mantenere come confronto storico; non usare come fonte primaria RAG.

Metodo: [[metodo_lcs_alternanza_pari_dispari]].
