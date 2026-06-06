# Ingestion report - Floyd-Warshall unificato

## Fonti

| Source ID | PDF | Tema | Stato |
|---|---|---|---|
| SRC-OFFICIAL-EX-003 | `01_sources/extra_materials/floyd-warshall-esempio-bottomup-27ott25.pdf` | Floyd-Warshall base | applicato |
| SRC-OFFICIAL-EX-004 | `01_sources/extra_materials/fw-alt-arc-color-27ott25.pdf` | archi alternati, cammino minimo | applicato |
| SRC-OFFICIAL-EX-005 | `01_sources/extra_materials/fw-alt-arc-color-existence.pdf` | archi alternati, esistenza | applicato |
| SRC-OFFICIAL-EX-006 | `01_sources/extra_materials/fw-alt-vertex-color-27ott25.pdf` | vertici alternati, cammino minimo | applicato |
| SRC-OFFICIAL-EX-007 | `01_sources/extra_materials/fw-alt-vertex-color.-existence.pdf` | vertici alternati, esistenza | applicato |
| SRC-OFFICIAL-EX-008 | `01_sources/extra_materials/fw-even-red-arcs-alt-vertex-color.pdf` | pari archi rossi + vertici alternati | applicato |
| SRC-OFFICIAL-EX-009 | `01_sources/extra_materials/fw-exact three-red-consecutive-couples-vertexes.pdf` | 3 coppie vertici rossi consecutivi | applicato |
| SRC-OFFICIAL-EX-010 | `01_sources/extra_materials/fw-exact-3-red-arcs-27ott25.pdf` | esattamente 3 archi rossi | applicato |
| SRC-OFFICIAL-EX-011 | `01_sources/extra_materials/fw-red-blue-arcs-existence.pdf` | presenza archi rossi e blu | applicato |

## Decisione

I piani separati su alternanza e conteggi sono stati consolidati in una sola famiglia RAG:

- `04_methods/fw_base_bottom_up.md`
- `04_methods/fw_varianti_vincoli_colori.md`
- `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`
- `07_solved_examples/fw_varianti_vincoli_colori_schema.md`

## Principio unificante

Ogni variante mantiene lo schema Floyd-Warshall:

- `k` = massimo vertice intermedio ammesso;
- `E1` = non uso `k`;
- `E2` = uso `k` e concateno `i -> k` con `k -> j`;
- `min/+` per cammini minimi;
- `OR/AND` per esistenza.

Gli stati extra dipendono dal vincolo: `f,l`, `p`, `r` o flag booleani.
