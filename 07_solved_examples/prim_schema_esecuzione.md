---
type: solved-example
topic: prim-schema-esecuzione
status: official_confirmed
source_id: SRC-OFFICIAL-EX-017
source_file: 01_sources/extra_materials/mst-prim.pdf
tags:
  - apa
  - esempio-svolto
  - topic/mst
  - topic/prim
---

# Schema esecuzione Prim

## Checklist

1. Scegliere il vertice sorgente `r`.
2. Inizializzare:
   - `key[r] = 0`;
   - `pi[r] = NIL`;
   - tutti gli altri `key = +infinito`, `pi = NIL`.
3. Inserire tutti i vertici in `Q`.
4. Finche `Q` non e vuota:
   - estrarre il vertice con chiave minima;
   - rilassare solo archi verso vertici ancora in `Q`;
   - aggiornare `key` e `pi`.
5. Alla fine, l'MST e dato dagli archi `(pi[v],v)` con `pi[v] != NIL`.

## Tabella consigliata

```text
Passo | Estratto u | Q dopo estrazione | Aggiornamenti key/pi | Arco MST aggiunto
```

L'arco MST aggiunto al passo di estrazione di `u` e `(pi[u],u)`, se `pi[u] != NIL`.

## Errori comuni

- Non aggiornare un vertice gia estratto da `Q`.
- Confondere `key[v]` con distanza minima da `r`.
- Confondere Prim con Dijkstra: Prim sceglie il miglior arco verso l'albero corrente, non un cammino minimo dalla sorgente.

Metodo: [[mst_prim]].
