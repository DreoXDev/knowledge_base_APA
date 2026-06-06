---
type: theory
topic: teorema-arco-sicuro-mst
status: official_confirmed
source_id: SRC-OFFICIAL-EX-018
source_file: 01_sources/extra_materials/mst.pdf
tags:
  - apa
  - teoria
  - topic/mst
  - topic/greedy
---

# Teorema dell'arco sicuro per MST

## Definizioni

Un taglio `(S, V - S)` e una partizione dei vertici.

Un arco attraversa il taglio se ha un estremo in `S` e l'altro in `V - S`.

Un taglio rispetta `A` se nessun arco di `A` attraversa il taglio.

Un arco e leggero per un taglio se attraversa il taglio e ha peso minimo tra gli archi che attraversano quel taglio.

Un arco `e` e sicuro per `A` se `A unione {e}` e ancora contenuto in qualche MST.

## Enunciato

Sia `G = (V,E)` un grafo non orientato, connesso e pesato. Sia `A` un sottoinsieme degli archi di qualche MST. Sia `(S, V - S)` un taglio che rispetta `A`.

Se `(u,v)` e un arco leggero che attraversa il taglio, allora `(u,v)` e sicuro per `A`.

## Dimostrazione breve

Sia `T` un MST che contiene `A`.

Se `(u,v)` appartiene gia a `T`, la tesi e immediata.

Altrimenti, aggiungendo `(u,v)` a `T` si crea un ciclo. Nel cammino di `T` tra `u` e `v` esiste un arco `(x,y)` che attraversa lo stesso taglio. Poiche il taglio rispetta `A`, l'arco `(x,y)` non appartiene ad `A`.

Poiche `(u,v)` e leggero:

```text
W(u,v) <= W(x,y)
```

Costruiamo:

```text
T' = T - {(x,y)} unione {(u,v)}
```

`T'` e ancora un albero ricoprente e:

```text
W(T') = W(T) - W(x,y) + W(u,v) <= W(T)
```

Dato che `T` e minimo, anche `T'` e un MST. Inoltre contiene `A` e contiene `(u,v)`, quindi `A unione {(u,v)}` e contenuto in un MST. L'arco e sicuro.

## Uso negli algoritmi

- Prim: il taglio separa l'albero corrente dai vertici esterni.
- Kruskal: il taglio separa una componente della foresta corrente dal resto.

Collegamenti: [[mst_greedy_base]], [[mst_prim]], [[metodo_kruskal_mst]], [[metodo_teorema_arco_sicuro]].
