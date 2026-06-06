# Schema — Simulazione di Kruskal (MST)

Questo schema descrive come tracciare l'esecuzione dell'algoritmo di **Kruskal** per la ricerca del *Minimum Spanning Tree* (MST) di un grafo non orientato in modo corretto per l'esame.

---

## Esempio di Grafo d'Esame

Sia $G = (V, E)$ un grafo con:
- **Vertici**: $V = \{A, B, C, D, E, F\}$ (quindi $|V| = 6$)
- **Archi e pesi**:
  - $(A, B): 4$
  - $(A, C): 2$
  - $(B, C): 1$
  - $(B, D): 5$
  - $(C, D): 8$
  - $(C, E): 10$
  - $(D, E): 2$
  - $(D, F): 6$
  - $(E, F): 3$

---

## 1. Ordinamento degli Archi per Peso Crescente

Elenchiamo gli archi del grafo in ordine crescente di peso:

1. $e_1 = (B, C)$ con peso $1$
2. $e_2 = (A, C)$ con peso $2$
3. $e_3 = (D, E)$ con peso $2$
4. $e_4 = (E, F)$ con peso $3$
5. $e_5 = (A, B)$ con peso $4$
6. $e_6 = (B, D)$ con peso $5$
7. $e_7 = (D, F)$ con peso $6$
8. $e_8 = (C, D)$ con peso $8$
9. $e_9 = (C, E)$ con peso $10$

---

## 2. Inizializzazione Union-Find

All'inizio ciascun vertice forma una componente connessa autonoma:
$$\{\{A\}, \{B\}, \{C\}, \{D\}, \{E\}, \{F\}\}$$
Insieme degli archi scelti: $T = \emptyset$. Criterio di arresto: $|T| = |V| - 1 = 5$ archi.

---

## 3. Simulazione Passo-Passo

| Passo | Arco $e = (u,v)$ | Peso | Componenti Disgiunte (Union-Find) | Scelta | Giustificazione |
|:---:|:---:|:---:|---|:---:|---|
| **0** | — | — | $\{\{A\}, \{B\}, \{C\}, \{D\}, \{E\}, \{F\}\}$ | — | Inizializzazione |
| **1** | $(B, C)$ | $1$ | $Find(B) \ne Find(C) \implies$ **Unione** | **PRENDO** | Componenti separate. Nuove comp: $\{\{A\}, \{B, C\}, \{D\}, \{E\}, \{F\}\}$ |
| **2** | $(A, C)$ | $2$ | $Find(A) \ne Find(C) \implies$ **Unione** | **PRENDO** | Componenti separate. Nuove comp: $\{\{A, B, C\}, \{D\}, \{E\}, \{F\}\}$ |
| **3** | $(D, E)$ | $2$ | $Find(D) \ne Find(E) \implies$ **Unione** | **PRENDO** | Componenti separate. Nuove comp: $\{\{A, B, C\}, \{D, E\}, \{F\}\}$ |
| **4** | $(E, F)$ | $3$ | $Find(E) \ne Find(F) \implies$ **Unione** | **PRENDO** | Componenti separate. Nuove comp: $\{\{A, B, C\}, \{D, E, F\}\}$ |
| **5** | $(A, B)$ | $4$ | $Find(A) = Find(B) \implies$ **Stessa comp** | **SCARTO** | Entrambi i vertici sono già in $\{A, B, C\}$ (creerebbe ciclo $A-B-C-A$). |
| **6** | $(B, D)$ | $5$ | $Find(B) \ne Find(D) \implies$ **Unione** | **PRENDO** | Componenti separate. Nuove comp: $\{\{A, B, C, D, E, F\}\}$ |

### Criterio di Arresto Raggiunto
L'insieme degli archi scelti è:
$$T = \{(B, C), (A, C), (D, E), (E, F), (B, D)\}$$
La dimensione di $T$ è $5$ (pari a $|V|-1$). L'algoritmo termina. Gli archi rimanenti non vengono esaminati (o verrebbero scartati).

---

## 4. Soluzione Finale

* **Archi dell'MST**: $T = \{(B, C), (A, C), (D, E), (E, F), (B, D)\}$
* **Peso dell'MST**: $1 + 2 + 2 + 3 + 5 = 13$

---

## Collegamenti

- Teoria: [[kruskal_matroide_grafico]]
- Metodo: [[metodo_kruskal_mst]]
- Esercizio correlato: [[exam_2025_11_10_p2_e01]]
