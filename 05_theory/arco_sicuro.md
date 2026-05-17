---
type: theory
topic: Safe Edge Theorem
status: complete
tags:
  - apa
  - teoria
  - topic/MST
  - topic/arco_sicuro
---

# Teoria — Il Teorema dell'Arco Sicuro

Il **Teorema dell'Arco Sicuro** (Safe Edge Theorem) costituisce la base matematica su cui si poggia la correttezza di tutti gli algoritmi greedy per la costruzione del **Minimum Spanning Tree** (come l'algoritmo di Kruskal e l'algoritmo di Prim).

---

## Definizioni Chiave

### 1. Taglio e Attraversamento
Un **taglio** $(S, V \setminus S)$ di un grafo non orientato $G = (V,E)$ rappresenta una partizione dell'insieme dei nodi $V$ in due sottoinsiemi disgiunti.
Un arco $(u,v) \in E$ **attraversa il taglio** se uno dei suoi estremi appartiene a $S$ e l'altro appartiene a $V \setminus S$.

### 2. Rispetto di un sottoinsieme di archi
Un taglio $(S, V \setminus S)$ **rispetta** un insieme di archi $A \subseteq E$ se nessun arco in $A$ attraversa il taglio. In altre parole, tutti gli archi di $A$ hanno entrambi gli estremi interamente dentro $S$ o interamente dentro $V \setminus S$.

### 3. Arco Leggero
Un arco $(u,v)$ è un **arco leggero** che attraversa un taglio se attraversa il taglio e possiede il peso minimo assoluto tra tutti gli archi che attraversano lo stesso taglio. 

*Nota: Se ci sono più archi con lo stesso peso minimo che attraversano il taglio, ciascuno di essi è considerato un arco leggero.*

### 4. Arco Sicuro
Dato un sottoinsieme di archi $A \subseteq E$ che è parte di qualche albero di copertura minimo (MST) di $G$, un arco $e \notin A$ si dice **sicuro** per $A$ se anche $A \cup \{e\}$ è sottoinsieme di qualche albero di copertura minimo di $G$.

---

## Enunciato del Teorema dell'Arco Sicuro

> **Teorema dell'Arco Sicuro**:
> Sia $G = (V,E)$ un grafo non orientato, connesso e pesato con funzione peso $w: E \to \mathbb{R}$.
> Sia $A$ un sottoinsieme di $E$ contenuto in qualche albero di copertura minimo (MST) di $G$.
> Sia $(S, V \setminus S)$ un taglio di $G$ che rispetta $A$.
> Sia $(u,v)$ un arco leggero che attraversa il taglio $(S, V \setminus S)$.
> 
> Allora, l'arco $(u,v)$ è **sicuro** per $A$.

---

## Ruolo negli Algoritmi per MST

Il teorema dell'arco sicuro garantisce che possiamo costruire l'MST in modo incrementale (greedy) partendo da un insieme vuoto di archi $A = \emptyset$:
- Ad ogni passo, individuiamo un taglio opportuno che rispetta l'insieme corrente $A$.
- Troviamo l'arco leggero che attraversa tale taglio.
- Il teorema ci assicura che possiamo aggiungere in sicurezza tale arco ad $A$ senza precluderci la possibilità di ottenere un MST finale.

### Differenza di tagli tra Kruskal e Prim:
* **Algoritmo di Prim**: Mantiene un singolo albero $A$. Ad ogni passo, il taglio è definito da $(S, V \setminus S)$ dove $S$ è l'insieme di nodi dell'albero corrente. L'arco leggero che attraversa il taglio collega l'albero corrente a un nuovo nodo esterno.
* **Algoritmo di Kruskal**: Mantiene una foresta $A$ di alberi. Quando considera l'arco di peso minimo $(u,v)$ che collega due alberi diversi, il taglio che rispetta $A$ è $(S, V \setminus S)$ dove $S$ è l'insieme di nodi dell'albero che contiene $u$. L'arco $(u,v)$ è l'arco leggero che attraversa il taglio, ed è dunque sicuro.

---

## Collegamenti ad Esercizi e Metodi

* **Guida alla Dimostrazione**: [[metodo_teorema_arco_sicuro]]
* **Esercizi correlati**: [[exam_2025_02_11_p2_completo_recupero_e05]], [[exam_2025_07_03_p2_e05]]
