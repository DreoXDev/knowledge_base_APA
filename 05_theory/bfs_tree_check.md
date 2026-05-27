---
type: theory
status: complete
source_id: SRC-NOTE-001
tags: [apa, teoria, grafi, bfs, alberi]
---

# BFS per verificare se un grafo e un albero

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 36-37.

## Domanda tipica

Modificare BFS per verificare se un grafo non orientato e un albero.

## Risposta d'esame

Un grafo non orientato e un albero se e connesso e aciclico. Operativamente:

1. Eseguire BFS da un vertice qualunque.
2. Verificare che tutti i vertici siano stati visitati.
3. Durante la visita, se incontro un arco verso un vertice gia visitato che non e il padre, ho trovato un ciclo.

Alternativa equivalente: verificare connettivita e $|E|=|V|-1$.

## Complessita

$O(|V|+|E|)$.

## Errori comuni

- In un grafo non orientato, l'arco verso il padre non e un ciclo.
- Verificare solo $|E|=|V|-1$ senza connettivita non basta.

