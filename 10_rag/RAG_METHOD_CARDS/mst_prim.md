---
type: rag-method-card
topic: mst-prim
status: official_confirmed
source_methods:
  - 04_methods/mst_greedy_base.md
  - 04_methods/mst_prim.md
  - 05_theory/teorema_arco_sicuro_mst.md
  - 04_methods/metodo_kruskal_mst.md
source_examples:
  - 07_solved_examples/prim_schema_esecuzione.md
  - 03_exercise_catalog/exercises/exam_2025_11_10_p2_e01.md
source_patterns:
  - 06_exam_patterns/simulazione_kruskal.md
exam_use: true
---

# MST e Prim

## Trigger

- "Minimum Spanning Tree"
- "MST"
- "albero ricoprente minimo"
- "arco sicuro"
- "taglio che rispetta A"
- "arco leggero"
- "Prim"
- "key", "predecessore", "Q"

## Decisione rapida

Se la traccia chiede teoria MST, recuperare [[mst_greedy_base]] e [[teorema_arco_sicuro_mst]].

Se la traccia chiede Prim, recuperare [[mst_prim]] e [[prim_schema_esecuzione]].

Se la traccia chiede Kruskal, recuperare anche [[kruskal_step_by_step]] e [[metodo_kruskal_mst]].

## MST base

Un MST e un albero ricoprente di peso minimo in un grafo non orientato, connesso e pesato.

Un albero ricoprente ha `|V|-1` archi.

La correttezza di Prim e Kruskal usa il teorema dell'arco sicuro: un arco leggero che attraversa un taglio che rispetta `A` puo essere aggiunto senza perdere la possibilita di completare un MST.

## Prim

Prim cresce una singola componente.

Ogni vertice `v` mantiene:

- `key[v]`: peso minimo dell'arco che collega `v` all'albero corrente;
- `pi[v]`: predecessore di `v` nell'MST;
- `Q`: vertici non ancora estratti.

Schema:

```text
PRIM(G,W,r)
    for each u in V do
        key[u] <- +infinito
        pi[u] <- NIL
    key[r] <- 0
    Q <- V

    while Q != insieme vuoto do
        u <- Extract-Min(Q)
        for each v in Adj[u] do
            if v in Q and W(u,v) < key[v] then
                pi[v] <- u
                key[v] <- W(u,v)

    return pi
```

Output:

```text
{ (pi[v], v) | v in V, pi[v] != NIL }
```

## Errori da evitare

- Non confondere MST con cammini minimi.
- Non confondere Prim con Dijkstra: `key[v]` non e distanza dalla sorgente.
- Non aggiornare vertici gia estratti da `Q`.
- Non dimenticare che MST richiede grafo non orientato e connesso.
