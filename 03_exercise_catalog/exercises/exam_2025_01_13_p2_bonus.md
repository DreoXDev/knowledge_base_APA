---
type: exercise
topic: Domande bonus di teoria
difficulty: alta
points: 3
exam: 2025-01-13 Parte II
status: solved
tags:
  - apa
  - esercizio
  - topic/matroidi
  - topic/greedy
  - topic/lcs
  - topic/np_completezza
  - topic/riduzioni_polinomiali
---

# Esercizi Facoltativi Premiali (Appello 13 Gennaio 2025)

## Descrizione Generale

Questa sezione raccoglie le 4 domande facoltative teoriche (da sceglierne una sola in sede d'esame, valore **3 punti**). Ciascuna opzione rappresenta un pilastro teorico fondamentale del corso di APA.

---

## Opzione 1: Sottostruttura Ottima della LCS

### Richiesta:
Siano $X = \langle x_1, \dots, x_m \rangle$ e $Y = \langle y_1, \dots, y_n \rangle$ due sequenze e sia $Z = \langle z_1, \dots, z_k \rangle$ una LCS (Longest Common Subsequence) di $X$ e $Y$. Enunciare e dimostrare la proprietà della sottostruttura ottima di $Z$.

### Risoluzione & Teoria:
La dimostrazione procede per casi confrontando gli elementi finali delle sequenze ($x_m$ e $y_n$):
- **Caso 1 ($x_m = y_n$)**: Allora $z_k = x_m = y_n$, e $Z_{k-1}$ è una LCS di $X_{m-1}$ e $Y_{n-1}$.
- **Caso 2 ($x_m \neq y_n$ e $z_k \neq x_m$)**: Allora $Z$ è una LCS di $X_{m-1}$ e $Y$.
- **Caso 3 ($x_m \neq y_n$ e $z_k \neq y_n$)**: Then $Z$ è una LCS di $X$ e $Y_{n-1}$.

Vedere la guida metodologica e la dimostrazione dettagliata:
👉 [[metodo_programmazione_dinamica_lcs_vincoli_colori]] (Principi LCS)

---

## Opzione 2: Ottimalità di Greedy-max sui Matroidi

### Richiesta:
Dimostrare che se un sistema di indipendenza $(E,\mathcal{F})$ è un matroide allora per ogni funzione peso $w: E \to \mathbb{R}^+ \cup \{0\}$, l’algoritmo `Greedy-max` restituisce una soluzione ottima.

### Risoluzione & Teoria:
Questo enunciato costituisce la prima direzione del celebre **Teorema di Rado-Edmonds**. La dimostrazione formale si effettua mostrando che la soluzione ordinata prodotta dal greedy non può essere superata in peso da nessun'altra soluzione indipendente del matroide, utilizzando una prova per induzione accoppiata a un argomento di scambio degli elementi.

Vedere la dimostrazione formale passo-passo:
👉 [[metodo_greedy_matroidi_rado]]

---

## Opzione 3: Riduzione 3-SAT $\le_p$ Independent Set

### Richiesta:
Dimostrare che 3-SAT si riduce polinomialmente a Independent Set.

### Risoluzione & Teoria:
Data una formula 3-CNF $\varphi$ con $k$ clausole, costruiamo un grafo $G = (V,E)$ in cui:
- Ogni letterale di ciascuna clausola corrisponde a un vertice.
- Aggiungiamo archi che collegano nodi all'interno della stessa clausola (formando $k$ triangoli).
- Aggiungiamo archi tra nodi di clausole diverse se i loro letterali sono complementari ($x_i$ e $\neg x_i$).
Si dimostra che la formula $\varphi$ è soddisfacibile se e solo se il grafo $G$ ha un **Independent Set** (insieme indipendente) di dimensione $k$.

Vedere la riduzione formale e la prova di correttezza:
👉 [[metodo_riduzione_3sat_independent_set]]

---

## Opzione 4: Riduzione CLIQUE $\le_p$ Vertex Cover

### Richiesta:
Dimostrare che CLIQUE si riduce polinomialmente a Vertex Cover.

### Risoluzione & Teoria:
La riduzione si basa sul **Teorema di Dualità Complementare** tra Clique e Vertex Cover. 
Data un'istanza $(G, k)$ per il problema CLIQUE, costruiamo l'istanza $(G', |V| - k)$ per il problema Vertex Cover, dove $G' = (V, E')$ è il **grafo complementare** di $G$.
La dimostrazione prova che $G$ contiene una clique di dimensione $k$ se e solo se il grafo complementare $G'$ contiene una copertura dei vertici (vertex cover) di dimensione $|V| - k$.

Vedere la riduzione formale e la prova di correttezza:
👉 [[metodo_riduzione_clique_vertex_cover]]
