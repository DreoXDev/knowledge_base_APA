---
type: theory
topic: Clique Vertex-Cover Independent Set
status: complete
tags:
  - apa
  - teoria
  - topic/NP-completezza
  - topic/clique
  - topic/vertex_cover
  - topic/independent_set
---

# Teoria — La Triade: CLIQUE, VERTEX-COVER e INDEPENDENT SET

I problemi **CLIQUE**, **VERTEX-COVER** e **INDEPENDENT SET** sono tre dei più importanti problemi decisionali sui grafi nell'ambito dello studio della **NP-completezza**. Essi formano una "triade" strettamente correlata tramite riduzioni polinomiali immediate e dualità insiemistiche.

---

## Definizioni dei Problemi

Sia $G = (V,E)$ un grafo non orientato.

### 1. CLIQUE
* **Definizione**: Una *clique* in $G$ è un sottoinsieme di vertici $K \subseteq V$ tale che ogni coppia di nodi distinti in $K$ è collegata da un arco. In altre parole, il sottografo indotto da $K$ è un grafo completo.
* **Problema di Decisione**: "Dato un grafo $G = (V,E)$ e un intero $k \ge 1$, esiste una clique di dimensione almeno $k$?"

### 2. VERTEX-COVER (Copertura dei Vertici)
* **Definizione**: Un *vertex cover* in $G$ è un sottoinsieme di vertici $V' \subseteq V$ tale che per ogni arco $(u,v) \in E$, almeno uno dei suoi estremi appartiene a $V'$ ($u \in V'$ oppure $v \in V'$).
* **Problema di Decisione**: "Dato un grafo $G = (V,E)$ e un intero $k' \ge 1$, esiste una copertura di vertici di dimensione al più $k'$?"

### 3. INDEPENDENT SET (Insieme Indipendente)
* **Definizione**: Un *independent set* in $G$ è un sottoinsieme di vertici $I \subseteq V$ tale che nessuna coppia di nodi distinti in $I$ è collegata da un arco in $E$.
* **Problema di Decisione**: "Dato un grafo $G = (V,E)$ e un intero $k'' \ge 1$, esiste un insieme indipendente di dimensione almeno $k''$?"

---

## Dualità e Teoremi di Equivalenza

Questi tre problemi sono strettamente legati dalla seguente equivalenza fondamentale per qualsiasi sottoinsieme di vertici $S \subseteq V$:

> **Teorema della Triade**:
> Sia $G = (V,E)$ un grafo non orientato e $\bar{G} = (V, \bar{E})$ il suo grafo complementare.
> Per ogni sottoinsieme di vertici $S \subseteq V$, le seguenti tre affermazioni sono logicamente equivalenti:
> 1. $S$ è una **Clique** in $G$.
> 2. $S$ è un **Independent Set** in $\bar{G}$.
> 3. $V \setminus S$ è un **Vertex Cover** in $\bar{G}$.

### Conseguenza per le Riduzioni Polinomiali:
Questo teorema fornisce riduzioni polinomiali dirette e istantanee:
* **CLIQUE $\le_p$ INDEPENDENT SET**: Data un'istanza $(G, k)$ di CLIQUE, costruiamo l'istanza $(\bar{G}, k)$ di INDEPENDENT SET.
* **INDEPENDENT SET $\le_p$ VERTEX-COVER**: Data un'istanza $(G, k)$ di INDEPENDENT SET, costruiamo l'istanza $(G, |V|-k)$ di VERTEX-COVER.
* **CLIQUE $\le_p$ VERTEX-COVER**: Data un'istanza $(G, k)$ di CLIQUE, costruiamo l'istanza $(\bar{G}, |V|-k)$ di VERTEX-COVER.

---

## Collegamenti ad Esercizi e Metodi

* **Metodo di riduzione CLIQUE-VC**: [[metodo_riduzione_clique_vertex_cover]]
* **Dimostrazione Formale CLIQUE $\le_p$ VC**: [[exam_2025_02_11_p2_completo_recupero_bonus]] (Opzione 2)
* **Esercizi operativi su grafi concreti**:
  - [[exam_2025_02_11_p2_completo_recupero_e02]] (Zaino/Complementare con Vertex Cover)
  - [[exam_2025_06_09_p2_e02]], [[exam_2025_07_03_p2_e02]]
