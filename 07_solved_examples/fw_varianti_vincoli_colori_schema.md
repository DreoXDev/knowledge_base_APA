---
type: solved-example
topic: floyd-warshall-varianti-vincoli-colori
status: official_confirmed
source_id:
  - SRC-OFFICIAL-EX-003
  - SRC-OFFICIAL-EX-004
  - SRC-OFFICIAL-EX-005
  - SRC-OFFICIAL-EX-006
  - SRC-OFFICIAL-EX-007
  - SRC-OFFICIAL-EX-008
  - SRC-OFFICIAL-EX-009
  - SRC-OFFICIAL-EX-010
  - SRC-OFFICIAL-EX-011
tags:
  - apa
  - esempio-svolto
  - topic/floyd-warshall
---

# Schema soluzione - Floyd-Warshall con vincoli

## Riconoscimento

Traccia tipica: "per ogni coppia di vertici" + cammini minimi o esistenza di cammini con vincoli.

## Schema da esame

1. Dire che si usa Floyd-Warshall con `k` = massimo vertice intermedio ammesso.
2. Definire `P_ij^k` o lo stato esteso.
3. Definire il coefficiente:
   - `d` per cammino minimo;
   - `e` per esistenza.
4. Scrivere i casi base `k=0`.
5. Scrivere:
   - `E1`: non uso `k`;
   - `E2`: uso `k`, concateno `i -> k` e `k -> j`.
6. Combinare lo stato extra.
7. Indicare il valore finale.

## Scelta dello stato extra

| Vincolo | Stato extra |
|---|---|
| archi alternati | `f,l` |
| vertici alternati | nessuno |
| numero pari | `p` |
| esattamente `t` | `r=0..t` |
| presenza colori | flag booleani |

## Errori comuni

- Non usare `f,l` per vertici alternati.
- Non dimenticare `a != b` per archi alternati.
- Non usare pesi nelle varianti di esistenza.
- Non confondere conteggio esatto con presenza.

Metodo: [[fw_varianti_vincoli_colori]].
