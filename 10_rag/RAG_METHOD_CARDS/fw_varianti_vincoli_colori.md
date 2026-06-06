---
type: rag-method-card
topic: floyd-warshall-varianti-vincoli-colori
status: official_confirmed
source_methods:
  - 04_methods/fw_base_bottom_up.md
  - 04_methods/fw_varianti_vincoli_colori.md
source_examples:
  - 07_solved_examples/fw_varianti_vincoli_colori_schema.md
source_patterns:
  - 06_exam_patterns/parte_i_dynamic_programming_patterns.md
exam_use: true
---

# Floyd-Warshall - base e varianti con vincoli

## Trigger

- "Floyd-Warshall"
- "cammini minimi per ogni coppia"
- "per ogni coppia di vertici"
- "variante di Floyd-Warshall"
- "archi alternati"
- "vertici alternati"
- "esattamente 3 archi rossi"
- "numero pari di archi rossi"
- "coppie di vertici rossi consecutivi"
- "archi rossi e archi blu presenti"
- "esistenza di cammini"

## Decisione rapida

1. Capire se la domanda e:
   - cammino minimo;
   - esistenza.
2. Capire cosa bisogna ricordare:
   - nulla: FW standard;
   - primo/ultimo colore: alternanza sugli archi;
   - parita: numero pari/dispari;
   - conteggio: esattamente `t`;
   - flag: presenza/assenza.
3. Usare:
   - `d`, `min`, `+`, `+infinito` per cammini minimi;
   - `e`, `OR`, `AND`, `TRUE/FALSE` per esistenza.
4. Scrivere sempre:
   - sottoproblema;
   - coefficiente;
   - casi base `k=0`;
   - `E1`: non uso `k`;
   - `E2`: uso `k`;
   - valore finale.

## Tabella compatta

| Variante | Tipo | Stato extra | Finale |
|---|---|---|---|
| FW standard | minimo | nessuno | `d_ij^n` |
| Archi alternati | minimo/esistenza | `f,l` primo e ultimo arco | `min/OR` su `f,l` |
| Vertici alternati | minimo/esistenza | nessuno | `d/e_ij^n` |
| Pari archi rossi + vertici alternati | minimo | `p in {0,1}` | `d_ij^{n,0}` |
| Esattamente 3 coppie vertici rossi consecutivi | minimo | `r=0..3` | `d_ij^{n,3}` |
| Esattamente 3 archi rossi | minimo | `r=0..3` | `d_ij^{n,3}` |
| Presenza archi rossi e blu | esistenza | `r,b in {0,1}` | `e_ij^{n,1,1}` |

## Ricorrenza scheletro

Cammino minimo:

```text
d_ij^k = min(E1,E2)
E1 = non uso k
E2 = uso k: costo(i,k) + costo(k,j), combinando lo stato extra
```

Esistenza:

```text
e_ij^k = E1 OR E2
E1 = non uso k
E2 = uso k: esiste(i,k) AND esiste(k,j), combinando lo stato extra
```

## Warning da esame

- `k` e il massimo vertice intermedio ammesso, non la lunghezza del cammino.
- Archi colorati alternati richiedono `f,l`; vertici colorati alternati no.
- Nelle varianti con primo/ultimo colore arco, il cammino banale non ha archi: nello stato la diagonale e impossibile, ma nel risultato finale `d_ii=0` ed `e_ii=TRUE`.
- "Esattamente 3 archi rossi" richiede un contatore; "sono presenti archi rossi e blu" richiede flag.
- Per esistenza non usare pesi.
