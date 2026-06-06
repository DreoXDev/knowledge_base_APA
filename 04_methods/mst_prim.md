---
type: method
topic: mst-prim
status: official_confirmed
source_id: SRC-OFFICIAL-EX-017
source_file: 01_sources/extra_materials/mst-prim.pdf
tags:
  - apa
  - metodo
  - topic/grafi
  - topic/greedy
  - topic/mst
  - topic/prim
---

# MST - Algoritmo di Prim

## Idea

Prim costruisce un MST facendo crescere una singola componente.

A ogni passo:

1. considera la componente gia costruita;
2. sceglie l'arco di peso minimo che collega un vertice nella componente con un vertice esterno;
3. aggiunge quell'arco.

La correttezza deriva dal teorema dell'arco sicuro.

## Versione concettuale dal GENERIC-MST

```text
A <- insieme vuoto
while |V| - |A| > 1 do
    scegli una componente connessa C = (V_C, E_C)
    (u,v) <- arco di peso minimo che collega un vertice in C con un vertice esterno a C
    A <- A unione {(u,v)}
return (V,A)
```

## Versione con coda di priorita

Ogni vertice `v` mantiene:

- `key[v]`: peso minimo dell'arco che collega `v` alla componente gia scelta;
- `pi[v]`: predecessore di `v` nell'MST;
- `Q`: vertici non ancora estratti.

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

## Output

L'MST e dato dagli archi:

```text
{ (pi[v], v) | v in V, pi[v] != NIL }
```

## Complessita

- Implementazione semplice o matrice di adiacenza: `O(n^2)`.
- Lista di adiacenza e heap binario: `O((n + m) log n)`.

## Errori da evitare

- Non confondere Prim con Dijkstra: la struttura e simile, ma `key[v]` non e una distanza dalla sorgente.
- Non aggiornare un vertice gia estratto da `Q`.
- Non dimenticare `pi[v]`: serve per ricostruire gli archi dell'MST.
- Prim richiede grafo non orientato, connesso e pesato.

Collegamenti: [[mst_greedy_base]], [[teorema_arco_sicuro_mst]], [[prim_schema_esecuzione]].
