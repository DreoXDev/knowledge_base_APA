---
type: solved_example
source_id: SRC-EXTRA-001
status: complete_with_warnings
tags: [apa, esempio-svolto, lcs, colori, booleana]
---

# Tutte le LCS hanno almeno 3 rossi - SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 07.

## Punto chiave

Non si chiede se esiste una LCS con almeno 3 rossi: si chiede se tutte le LCS ottime hanno almeno 3 rossi.

## Sottoproblema

$$
B_{i,j,r}=true
$$

se tutte le LCS di $X_i,Y_j$ contengono almeno $r$ rossi.

## Regola sui rami ottimi

Calcolare prima $L_{i,j}$, lunghezza LCS standard. In caso di mismatch:

- se solo $L_{i-1,j}$ e ottimo, eredito da sopra;
- se solo $L_{i,j-1}$ e ottimo, eredito da sinistra;
- se entrambi sono ottimi, uso AND.

Metodo: [[metodo_programmazione_dinamica_lcs_vincoli_colori]].

> [!Warning]
> La fonte evidenzia l'AND, ma il filtro sui rami ottimi va reso esplicito.

