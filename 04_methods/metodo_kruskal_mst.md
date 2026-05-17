---
type: method
topic: Kruskal MST simulation
status: draft
tags:
  - apa
  - metodo
  - topic/grafi
  - topic/greedy
  - topic/kruskal
  - topic/mst
---

# Metodo — Simulazione progressiva di Kruskal per MST

## Quando si usa

Questo metodo si applica a problemi d'esame in cui viene richiesto di calcolare o simulare passo-passo l'esecuzione dell'algoritmo di **Kruskal** per trovare il *Minimum Spanning Tree* (MST) di un grafo non orientato, connesso e pesato $G = (V,E)$, tracciando l'aggiunta o lo scarto sequenziale degli archi ordinati per peso.

---

## Procedura operativa passo-passo

1. **Elencare e ordinare gli archi**:
   Raccogliere tutti gli archi del grafo con i rispettivi pesi e ordinarli in una lista in ordine **crescente** di peso.
   - *Nota in caso di parità*: Se due o più archi hanno lo stesso identico peso, l'algoritmo può esaminarli in qualsiasi ordine arbitrario (a meno che il testo dell'esame non indichi esplicitamente un criterio di priorità, come l'ordine alfabetico dei nodi).

2. **Inizializzazione**:
   Creare una foresta $T = \emptyset$ in cui ciascun nodo $v \in V$ appartiene a un insieme disgiunto separato (una componente connessa autonoma). Il numero iniziale di componenti connesse è $|V|$.

3. **Ciclo principale di esame**:
   Scorrere la lista ordinata degli archi dall'inizio alla fine. Per ogni arco $e = (u,v)$ esaminato:
   - Controllare se gli estremi $u$ e $v$ appartengono alla **stessa componente connessa** (ad esempio tramite l'operazione `Find-Set` in una struttura Union-Find).
   - **Caso A (Componenti disgiunte)**: Se $u$ e $v$ appartengono a componenti diverse, l'arco $e$ viene **aggiunto** a $T$. Le due componenti connesse vengono fuse in una sola (operazione `Union`).
   - **Caso B (Stessa componente)**: Se $u$ e $v$ sono già nella stessa componente, l'arco $e$ viene **scartato** (in quanto la sua aggiunta creerebbe un ciclo semplice).
   - Registrare rigorosamente lo stato progressivo degli archi inclusi e scartati.

4. **Criterio di arresto**:
   L'algoritmo termina non appena la foresta $T$ contiene esattamente:
   $$|V| - 1 \text{ archi}$$
   A questo punto il grafo è completamente coperto ed è connesso in un unico albero Spanning Tree. Tutti gli archi rimanenti non ancora esaminati verrebbero comunque scartati.

---

## Gestione del formato d'esame "Progressivo"

In alcuni appelli (es. *10 novembre 2025*), il testo richiede di mostrare lo stato degli archi aggiunti all'interno di quadrati sequenziali $Q_1, Q_2, \dots, Q_m$ (uno per ogni arco del grafo):
- In $Q_1$ si disegna lo stato dopo aver esaminato il primo arco (incluso).
- In $Q_i$ si disegna lo stato dopo il passo $i$. Se l'arco esaminato al passo $i$ viene scartato, lo stato in $Q_i$ rimarrà identico a quello del passo precedente $Q_{i-1}$.
- Non interrompere la sequenza dei quadrati anche se l'MST è stato completato prima di aver esaurito gli archi: i quadrati successivi conterranno lo stesso MST finale completo, evidenziando che gli ultimi archi esaminati sono stati scartati.

---

## Esercizi collegati

- [[exam_2026_01_12_e03]]
- [[exam_2025_11_10_p2_e01]]

---

## Errori comuni da evitare

> [!Warning]
> **Creare cicli**: Dimenticare di tracciare le componenti connesse e inserire un arco che collega due nodi già connessi indirettamente, introducendo un ciclo.
> **Ordinamento errato**: Sbagliare l'ordinamento iniziale degli archi o tralasciarne qualcuno.
> **Confondere Kruskal con Prim**: Prim cresce un unico albero a partire da un nodo sorgente fisso, mentre Kruskal lavora su una foresta che unisce alberi sparsi basandosi esclusivamente sui pesi globali degli archi.
