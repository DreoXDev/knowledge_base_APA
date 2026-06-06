---
type: solved_example
source_id: SRC-OFFICIAL-EX-013
status: official_confirmed
tags: [apa, esempio-svolto, lcs, fonte-ufficiale]
---

# Esempio svolto - LCS base da PDF ufficiale 6 ottobre 2025

## Fonte

- `01_sources/extra_materials/lcs-6ott25.pdf`

## Input

`X = <2, 10, 5, 3, 1, 12>`

`Y = <2, 5, 12, 2, 3, 12, 1, 30>`

## Metodo

Usare DP LCS base.

## Matrice C

Righe: `i=0..6`.

Colonne: `j=0..8`.

| i\j | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 0 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 4 | 0 | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 3 |
| 5 | 0 | 1 | 2 | 2 | 2 | 3 | 3 | 4 | 4 |
| 6 | 0 | 1 | 2 | 3 | 3 | 3 | 4 | 4 | 4 |

## Valore ottimo

`c_{6,8} = 4`.

## Una LCS ricostruita

`<2, 5, 3, 12>`.

## Nota sui pareggi

Il PDF mostra che esiste un percorso alternativo che porta a una diversa soluzione. Quindi non vincolare la KB a una singola LCS quando la matrice presenta pareggi.

## Errori da evitare

- Non confondere sottosequenza con sottostringa.
- Non cambiare ordine degli elementi.
- Non assumere unicita della soluzione.

## Collegamenti

- [[dp_lcs_base]]
- [[metodo_lcs_base]]
- [[metodo_ricostruzione_soluzione_dp]]
