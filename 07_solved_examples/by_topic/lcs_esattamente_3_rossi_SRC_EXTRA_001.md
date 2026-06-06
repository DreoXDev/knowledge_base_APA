---
type: solved_example
source_id: SRC-EXTRA-001
status: complete
tags: [apa, esempio-svolto, lcs, colori]
---

# LCS con esattamente 3 rossi - SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagine 04-06.

> [!Info]
> Questo esempio e per "esattamente 3 rossi". Non va citato come esempio di "al massimo 3 rossi". Per la variante ufficiale "al massimo" usare [[lcs_al_massimo_3_rossi_SRC_LECTURE_001]].

## Istanza

Due sequenze $X,Y$ e una funzione colore $col$.

## Soluzione

Lunghezza di una LCS con esattamente $3$ simboli rossi.

## Sottoproblema

$$
C_{i,j,r} = \text{lunghezza di una LCS tra } X_i,Y_j \text{ con esattamente } r \text{ rossi}.
$$

## Caso base

$$
C_{0,j,0}=C_{i,0,0}=0,\qquad C_{0,j,r}=C_{i,0,r}=-\infty \text{ per } r>0.
$$

## Soluzione

$$
C_{m,n,3}.
$$

Metodo: [[metodo_programmazione_dinamica_lcs_vincoli_colori]].
