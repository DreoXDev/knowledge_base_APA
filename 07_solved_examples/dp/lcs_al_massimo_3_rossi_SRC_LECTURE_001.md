---
type: solved_example
source_id: SRC-LECTURE-001
status: official_confirmed
tags: [apa, esempio-svolto, lcs, colori, fonte-ufficiale]
---

# LCS con al massimo 3 rossi - SRC-LECTURE-001

Fonte: `01_sources/extra_materials/lcs_atmost_red-13ott25.pdf`.

## Istanza ufficiale

`X = <3,5,9,6,4,8,12,10,5,30,7>`

`Y = <3,2,4,9,6,10,2,8,30,13,30,7>`

## LCS senza vincolo

Esempi di LCS massime:

- `<3,9,6,8,30,7>`
- `<3,9,6,10,30,7>`

## LCS con al massimo 3 rossi

Una soluzione ufficiale con al massimo 3 elementi rossi e:

`<3,6,8,30,7>`

## Metodo

Usare:

`C[i][j][r]` = lunghezza di una LCS tra `X_i` e `Y_j` con al massimo `r` rossi.

Valore finale per il caso del PDF:

`C[m][n][3]`.

## Collegamenti

- [[dp_lcs_vincoli_colore]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- `10_rag/RAG_METHOD_CARDS/dp_lcs_colori.md`
