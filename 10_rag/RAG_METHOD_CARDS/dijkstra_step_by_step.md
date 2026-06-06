---
type: rag-method-card
topic: dijkstra-step-by-step
status: complete
source_methods:
  - 04_methods/metodo_dijkstra.md
  - 04_methods/metodo_dimostrazione_correttezza_dijkstra.md
source_examples:
  - 07_solved_examples/priority_examples_index.md
source_patterns:
  - 06_exam_patterns/parte_ii_grafi_np_patterns.md
exam_use: true
---

# Dijkstra step-by-step

## Quando riconoscerlo

Frasi tipiche:

- "eseguire Dijkstra a partire dal nodo s"
- "mostrare le distanze a ogni iterazione"
- "cammini minimi con pesi non negativi"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Mantenere per ogni vertice `v`:

- `d[v]`: migliore distanza provvisoria da `s`;
- `pred[v]`: predecessore nel cammino;
- `S`: insieme dei vertici definitivi.

### 2. Casi base

`d[s]=0`; `d[v]=+infty` per `v != s`; `pred[v]=NIL`; `S=vuoto`.

### 3. Ricorrenza / transizione

Finche esistono vertici non definitivi:

1. scegli `u` non in `S` con `d[u]` minima;
2. aggiungi `u` a `S`;
3. per ogni arco `(u,v)`, se `d[v] > d[u] + w(u,v)`, aggiorna:
   `d[v] = d[u] + w(u,v)`, `pred[v]=u`.

### 4. Ordine di calcolo

Una iterazione per vertice, sempre scegliendo la distanza provvisoria minima.

### 5. Soluzione finale

La tabella finale `d[v]` contiene le distanze minime da `s`; i predecessori ricostruiscono i cammini.

### 6. Ricostruzione, se richiesta

Per il cammino da `s` a `t`, risalire da `t` tramite `pred[t]` fino a `s`, poi invertire.

### 7. Complessita

Con heap: `O((|V|+|E|) log |V|)`.

Con matrice/lista semplice: `O(|V|^2)`.

### 8. Correttezza breve

Quando un vertice `u` viene estratto con distanza minima provvisoria, nessun cammino futuro puo migliorarlo perche tutti i pesi sono non negativi. Quindi `d[u]` diventa definitivo. I rilassamenti mantengono le migliori distanze note verso i vertici non definitivi. Per induzione sul numero di estrazioni, tutte le distanze finali sono minime.

## Errori da evitare

- Non usare Dijkstra con pesi negativi.
- Non rendere definitivo un vertice due volte.
- Non dimenticare di aggiornare anche il predecessore.
