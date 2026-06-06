---
type: theory
topic: kruskal_matroide_grafico
status: complete
tags:
  - apa
  - teoria
  - topic/greedy
  - topic/matroidi
  - topic/mst
---

# Teoria — Kruskal e il Matroide Grafico

L'algoritmo di **Kruskal** per la ricerca del *Minimum Spanning Tree* (MST) di un grafo può essere formalizzato e dimostrato corretto tramite il framework dei **matroidi**, in particolare ricorrendo al concetto di **Matroide Grafico**.

---

## Definizione di Matroide Grafico

Sia $G = (V, E)$ un grafo non orientato, connesso e pesato. Si definisce la coppia $M = (E, \mathcal{F})$ dove:
- L'insieme di base $E$ è l'insieme degli **archi** del grafo.
- La famiglia $\mathcal{F} \subseteq 2^E$ contiene tutti i sottoinsiemi di archi che non contengono cicli semplici (ovvero, le **foreste** generabili sui vertici $V$):
  $$\mathcal{F} = \{ A \subseteq E \mid (V, A) \text{ è una foresta} \}$$

Per mostrare che $M = (E, \mathcal{F})$ è un matroide, verifichiamo i due assiomi:

### 1. Proprietà Ereditaria
Se un insieme di archi $A$ non contiene cicli (è una foresta) e prendiamo un sottoinsieme $B \subseteq A$, anche $B$ non può contenere cicli. Di conseguenza:
$$A \in \mathcal{F} \land B \subseteq A \implies B \in \mathcal{F}$$

### 2. Proprietà di Scambio
Siano $A, B \in \mathcal{F}$ due foreste tali che $|B| > |A|$.
- La foresta $(V, A)$ ha esattamente $|V| - |A|$ componenti connesse (alberi).
- La foresta $(V, B)$ ha esattamente $|V| - |B|$ componenti connesse.
- Poiché $|B| > |A|$, la foresta $(V, B)$ ha meno componenti connesse di $(V, A)$. Di conseguenza, deve esistere almeno un albero nella foresta $B$ i cui vertici sono distribuiti su più alberi distinti nella foresta $A$.
- Esiste quindi un arco $b = (u,v) \in B \setminus A$ i cui estremi $u$ e $v$ si trovano in componenti connesse diverse nella foresta $(V, A)$.
- Aggiungendo l'arco $b$ ad $A$, non si crea alcun ciclo. Pertanto:
  $$A \cup \{b\} \in \mathcal{F}$$

---

## Collegamento con il Minimum Spanning Tree (MST)

Tutti gli insiemi indipendenti massimali di un matroide (le sue **basi**) hanno la stessa cardinalità.
Nel matroide grafico, le basi sono gli **spanning trees** (alberi di copertura) di $G$, e la loro cardinalità è esattamente pari a:
$$|V| - 1 \text{ archi}$$

L'algoritmo di **Kruskal** è l'applicazione diretta dell'algoritmo greedy su questo matroide:
1. Ordina gli elementi (archi) in ordine crescente di peso (poiché vogliamo minimizzare il peso, contrariamente alla massimizzazione del teorema di Rado-Edmonds standard, ma il principio di correttezza è identico).
2. Esamina ciascun arco ed effettua una scelta greedy: lo aggiunge all'insieme corrente se e solo se mantiene l'indipendenza (ovvero, non crea cicli, mantenendo la struttura di foresta).

La correttezza di Kruskal segue direttamente dal teorema di Rado-Edmonds applicato al matroide grafico.

---

## Struttura Union-Find per il Controllo dei Cicli

Operativamente, la verifica dell'indipendenza (assenza di cicli) viene implementata in modo efficiente tramite una struttura dati per insiemi disgiunti (**Union-Find**):
- **Make-Set($v$)**: Inizializza ciascun vertice come componente isolata.
- **Find-Set($u$)**: Restituisce il rappresentante della componente a cui appartiene il vertice. Se `Find-Set(u) != Find-Set(v)`, l'aggiunta dell'arco non crea cicli.
- **Union($u,v$)**: Fonde le due componenti connesse.

---

## Warning d'Esame

> [!WARNING]
> **Kruskal (Greedy su Archi) vs Prim (Greedy su Vertici)**
> Non confondere i due approcci:
> - **Kruskal** lavora su archi ordinati globalmente, gestendo una foresta di alberi che si fondono progressivamente.
> - **Prim** fa crescere un unico albero a partire da una sorgente fissa, aggiungendo a ogni passo il vertice non ancora coperto più vicino alla componente già costruita.
> Entrambi calcolano un MST corretto, ma la dimostrazione di Prim si basa sul teorema dell'arco sicuro sui tagli, non direttamente sul matroide grafico.

---

## Collegamenti

- Teoria matroidi: [[matroidi_e_greedy]]
- Metodo Kruskal: [[metodo_kruskal_mst]]
- Teorema dell'arco sicuro: [[teorema_arco_sicuro_mst]]
- Metodo dimostrazione matroide grafico: [[metodo_dimostrazione_matroide_grafico]]
