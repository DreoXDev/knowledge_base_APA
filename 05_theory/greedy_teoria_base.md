---
type: theory
topic: greedy
status: complete
tags:
  - apa
  - teoria
  - topic/greedy
---

# Teoria — Algoritmi Greedy (Teoria Base)

## Idea Intuitiva

Un algoritmo **greedy** (o ingordo) costruisce una soluzione per passi successivi attraverso un processo incrementale ("per aggiunta"). A ogni passo compie una scelta che appare come **localmente ottima** in quel momento (ottimo locale), senza mai tornare indietro (no backtracking) e sperando che tale scelta conduca a una soluzione **globalmente ottima** (ottimo globale).

---

## Quando si applica

Gli algoritmi greedy si applicano tipicamente a **problemi di ottimizzazione**. Tuttavia, a differenza della programmazione dinamica, non è sufficiente che il problema presenti una sottostruttura ottima: serve dimostrare formalmente che la scelta locale non preclude la possibilità di raggiungere l'ottimo globale.

Le proprietà fondamentali per la correttezza sono:
1. **Greedy Choice Property** (Proprietà della scelta greedy): Una soluzione ottima globale può essere ottenuta compiendo una scelta greedy locale.
2. **Optimal Substructure** (Sottostruttura ottima): Una soluzione ottima al problema contiene al suo interno le soluzioni ottime ai sottoproblemi.

---

## Differenza tra Programmazione Dinamica e Greedy

| Aspetto | Programmazione Dinamica | Greedy |
|---|---|---|
| **Costruzione** | Risolve i sottoproblemi in modo bottom-up/top-down e ne combina i risultati. | Costruisce la soluzione passo-passo per aggiunta incrementale. |
| **Scelte** | Valuta e confronta molteplici alternative (es. prendere o non prendere un oggetto). | Effettua una singola scelta locale determinata da un criterio fisso. |
| **Correttezza** | Garantita dalla correttezza della ricorrenza e dall'assenza di scelte premature. | Richiede una dimostrazione matematica ad-hoc della scelta locale. |
| **Efficienza** | Evita i ricalcoli (memoria), ma può avere elevata complessità tempo/spazio. | Spesso riduce drasticamente il tempo di esecuzione e lo spazio rispetto alla DP. |

---

## Esempi Classici di Applicazione

* **Minimum Spanning Tree (MST)**: Algoritmi di Prim e Kruskal (scelta dell'arco più leggero).
* **Cammini Minimi**: Algoritmo di Dijkstra (scelta del vertice più vicino non ancora visitato).
* **Zaino Frazionario** (Fractional Knapsack): Si seleziona l'oggetto con massima densità di valore $v_i/w_i$ (anche frazionandolo).
* **Scheduling**: Selezione degli intervalli (scelta dell'attività che termina prima).
* **Resto di Monete** (Change-Making): Funziona solo per determinati sistemi monetari (es. Euro, Dollaro).

---

## Warning Importanti

> [!WARNING]
> **Il greedy non funziona in generale!**
> Moltissimi problemi di ottimizzazione non possono essere risolti esattamente tramite greedy.
> * **Zaino 0/1**: Richiede la programmazione dinamica. Un approccio greedy produce soluzioni sub-ottimali.
> * **Change-Making generico**: Con un set di monete arbitrario (es. $\{1, 3, 4\}$ per dare resto $6$), il greedy sceglie $\{4, 1, 1\}$ (3 monete) invece dell'ottimo $\{3, 3\}$ (2 monete).
> * **Necessità di dimostrazione**: All'esame non basta dichiarare una strategia intuitiva; occorre dimostrarne la correttezza formale (es. tramite scambio o tramite teoria dei matroidi).

---

## Collegamenti

- Teoria matroidi: [[matroidi_e_greedy]]
- Kruskal e matroide grafico: [[kruskal_matroide_grafico]]
- Floyd-Warshall e DP su grafi: [[floyd_warshall]]
- Metodi greedy: [[mst_greedy_base]], [[metodo_kruskal_mst]], [[mst_prim]]
