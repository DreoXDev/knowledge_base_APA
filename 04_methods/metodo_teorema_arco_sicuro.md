---
type: method
topic: Safe Edge Theorem proof
status: draft
tags:
  - apa
  - metodo
  - topic/grafi
  - topic/mst
  - topic/teoria
  - topic/kruskal
---

# Metodo - Dimostrazione del Teorema dell'Arco Sicuro

## Quando si usa

Questo metodo si applica quando viene richiesto di enunciare e dimostrare formalmente il **Teorema dell'arco sicuro (Safe Edge Theorem)**, che costituisce la base teorica per la correttezza degli algoritmi greedy per la costruzione del Minimum Spanning Tree (MST), come Kruskal e Prim.

## Enunciato del Teorema

Sia $G=(V,E)$ un grafo non orientato, connesso e pesato con una funzione peso $w: E \to \mathbb{R}$. Sia $A \subseteq E$ un sottoinsieme di archi incluso in un qualche Minimum Spanning Tree (MST) di $G$. 

Sia $(S, V \setminus S)$ un **taglio** di $G$ che **rispetta** $A$ (ovvero nessun arco in $A$ attraversa il taglio, cioè non ha un estremo in $S$ e l'altro in $V \setminus S$). 

Sia $(u,v) \in E$ un **arco leggero** che attraversa il taglio $(S, V \setminus S)$ (ovvero ha il peso minimo tra tutti gli archi che attraversano il taglio).

Allora, l'arco $(u,v)$ è **sicuro** per $A$, ossia anche l'insieme $A \cup \{(u,v)\}$ è incluso in un qualche MST di $G$.

---

## Dimostrazione Formale

Sia $T$ un MST di $G$ tale che $A \subseteq T$. Dobbiamo mostrare che esiste un MST $T'$ che contiene $A \cup \{(u,v)\}$.

1. **Caso 1: $(u,v) \in T$**
   Se l'arco leggero $(u,v)$ fa già parte di $T$, allora $A \cup \{(u,v)\} \subseteq T$. In questo caso, poniamo semplicemente $T' = T$, ed il teorema è dimostrato poiché $T$ è un MST per ipotesi.

2. **Caso 2: $(u,v) \notin T$**
   Se $(u,v)$ non appartiene a $T$, la sua aggiunta a $T$ crea esattamente un **ciclo semplice** $C$ (poiché un albero con l'aggiunta di un arco non appartenente ad esso genera un ciclo).
   
   Poiché $u \in S$ e $v \in V \setminus S$, i due vertici si trovano su lati opposti del taglio. Pertanto, il cammino in $T$ che collega $u$ a $v$ deve necessariamente attraversare il taglio $(S, V \setminus S)$ almeno una volta. Sia $(x,y) \in T$ un arco del cammino (diverso da $(u,v)$) che attraversa il taglio.
   
   L'arco $(x,y)$ ha le seguenti proprietà:
   - Appartiene a $T$, ma **non appartiene ad $A$**, poiché il taglio $(S, V \setminus S)$ rispetta $A$ per ipotesi (nessun arco di $A$ può attraversare il taglio).
   - Poiché $(u,v)$ è un arco leggero per il taglio $(S, V \setminus S)$, si ha:
     $$
     w(u,v) \le w(x,y)
     $$

3. **Costruzione di $T'$**:
   Rimuoviamo l'arco $(x,y)$ e aggiungiamo l'arco $(u,v)$ per spezzare il ciclo e ripristinare la struttura ad albero:
   $$
   T' = T \setminus \{(x,y)\} \cup \{(u,v)\}
   $$
   Poiché abbiamo rimosso un arco da un ciclo e aggiunto un altro arco che collega le due componenti connesse risultanti, $T'$ è ancora un albero ricoprente (spanning tree) di $G$.

4. **Verifica della Minimalità di $T'$**:
   Calcoliamo il peso complessivo di $T'$:
   $$
   w(T') = w(T) - w(x,y) + w(u,v)
   $$
   Poiché $w(u,v) \le w(x,y)$, si ha:
   $$
   w(T') \le w(T)
   $$
   Tuttavia, $T$ è un Minimum Spanning Tree per ipotesi, quindi il suo peso è il minimo possibile. Di conseguenza, deve valere l'uguaglianza:
   $$
   w(T') = w(T)
   $$
   Questo dimostra che anche $T'$ è un Minimum Spanning Tree.

5. **Conclusione**:
   Poiché $A \subseteq T$ e l'arco rimosso $(x,y) \notin A$, si ha $A \subseteq T'$. Dato che $(u,v) \in T'$, concludiamo che:
   $$
   A \cup \{(u,v)\} \subseteq T'
   $$
   Essendo $T'$ un MST di $G$, l'arco $(u,v)$ è sicuro per $A$. $\blacksquare$

---

## Esercizi collegati

- [[exam_2025_02_11_p2_completo_recupero_e05]]
- [[exam_2025_07_03_p2_e05]]
- [[exam_2026_01_12_e03]] (collegato per Kruskal MST)

## Errori comuni

> [!Warning]
> Dimenticare di specificare che il taglio deve *rispettare* l'insieme $A$. Senza questa condizione, l'arco $(x,y)$ rimosso potrebbe appartenere ad $A$, invalidando la prova.
> Definire genericamente $(u,v)$ come arco leggero del grafo anziché *arco leggero che attraversa il taglio*.
