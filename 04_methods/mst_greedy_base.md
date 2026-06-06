---
type: method
topic: mst-greedy-base
status: official_confirmed
source_id: SRC-OFFICIAL-EX-018
source_file: 01_sources/extra_materials/mst.pdf
tags:
  - apa
  - metodo
  - topic/grafi
  - topic/greedy
  - topic/mst
---

# MST - Minimum Spanning Tree

## Problema

Input:

- grafo `G = (V,E)` non orientato e connesso;
- funzione peso `W : E -> R+`.

Output: un sottoinsieme `T subseteq E` tale che:

- `(V,T)` e connesso;
- `(V,T)` e aciclico;
- il peso `W(T) = sum_{(u,v) in T} W(u,v)` e minimo.

`(V,T)` e un Minimum Spanning Tree.

## Proprieta operative

Per un grafo con `|V|` vertici, un albero ricoprente contiene:

```text
|V| - 1
```

archi.

## Algoritmo generico MST

```text
GENERIC-MST(G,W)
    A <- insieme vuoto
    while |V| - |A| > 1 do
        trova un taglio (V', V - V') che rispetti A
        (u,v) <- arco leggero per (V', V - V')
        A <- A unione {(u,v)}
    return (V,A)
```

## Taglio che rispetta `A`

Un taglio `(V', V - V')` rispetta `A` se nessun arco di `A` attraversa il taglio.

## Arco leggero

Un arco e leggero per un taglio se attraversa il taglio e ha peso minimo tra gli archi che lo attraversano.

## Arco sicuro

Un arco `(u,v) in E - A` e sicuro per `A` se:

```text
A unione {(u,v)}
```

e ancora sottoinsieme degli archi di qualche MST.

## Teorema dell'arco sicuro

Sia:

- `G = (V,E)` un grafo non orientato, connesso e pesato;
- `A` un sottoinsieme degli archi di qualche MST;
- `(V', V - V')` un taglio che rispetta `A`.

Allora un arco leggero `(u,v)` che attraversa il taglio e sicuro per `A`.

## Idea della dimostrazione

Se l'arco leggero `(u,v)` non appartiene a un MST `T`, allora nel cammino di `T` che collega `u` e `v` esiste un arco `(x,y)` che attraversa lo stesso taglio.

Poiche `(u,v)` e leggero:

```text
W(u,v) <= W(x,y)
```

Sostituendo `(x,y)` con `(u,v)` si ottiene un nuovo albero ricoprente di peso non maggiore:

```text
T' = T - {(x,y)} unione {(u,v)}
```

Quindi `(u,v)` puo appartenere a un MST ed e sicuro per `A`.

## Errori da evitare

- Un MST non e un cammino minimo: minimizza la somma degli archi scelti per connettere tutti i vertici, non le distanze tra coppie di vertici.
- Il grafo MST e non orientato e connesso.
- Non applicare Prim o Kruskal a grafi orientati come se fossero cammini minimi.

Collegamenti: [[teorema_arco_sicuro_mst]], [[mst_prim]], [[metodo_kruskal_mst]].
