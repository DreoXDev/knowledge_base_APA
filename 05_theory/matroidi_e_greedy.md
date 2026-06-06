---
type: theory
topic: Matroidi e Greedy
status: complete
tags:
  - apa
  - teoria
  - topic/matroidi
  - topic/greedy
---

# Teoria — Matroidi e Algoritmi Greedy

Un **matroide** è una struttura matematica che generalizza la nozione di indipendenza lineare dagli spazi vettoriali a insiemi finiti generici. I matroidi forniscono il framework teorico fondamentale per caratterizzare i problemi di ottimizzazione combinatoria che possono essere risolti in modo esatto tramite **algoritmi greedy**.

---

## Strutture di Base

### 1. Sistema di Indipendenza
Un **sistema di indipendenza** è una coppia $(E, \mathcal{F})$ dove:
- $E$ è un insieme finito di elementi.
- $\mathcal{F} \subseteq 2^E$ è una famiglia non vuota di sottoinsiemi di $E$, detti **insiemi indipendenti**.
- La famiglia soddisfa la **Proprietà di Ereditarietà**:
  $$\text{Se } A \in \mathcal{F} \text{ e } B \subseteq A \implies B \in \mathcal{F}$$

*Nota: L'insieme vuoto appartiene sempre a $\mathcal{F}$ ($\emptyset \in \mathcal{F}$).*

### 2. Definizione di Matroide
Un **matroide** è un sistema di indipendenza $(E, \mathcal{F})$ che soddisfa un assioma aggiuntivo, detto **Assioma di Scambio (o Proprietà di Estensione)**:

> **Assioma di Scambio**:
> Se $A, B \in \mathcal{F}$ e $|A| > |B|$, allora esiste un elemento $x \in A \setminus B$ tale che:
> $$B \cup \{x\} \in \mathcal{F}$$

---

## Concetti e Proprietà Fondamentali

### 1. Basi e Cardinalità Costante
Un sottoinsieme indipendente $B \in \mathcal{F}$ si dice **base** del matroide se è massimale rispetto all'inclusione (ovvero non esiste alcun $x \notin B$ tale che $B \cup \{x\} \in \mathcal{F}$).

* **Teorema**: In un matroide, **tutte le basi hanno la stessa identica cardinalità**.
* Esempio: In un grafo non orientato connesso $G=(V,E)$, le basi del matroide grafico sono gli alberi ricoprenti (spanning trees), e hanno tutte cardinalità pari a $|V|-1$.

### 2. Rango
Dato un sottoinsieme $A \subseteq E$, il suo **rango** $r(A)$ è la cardinalità del più grande sottoinsieme indipendente contenuto in $A$:
$$r(A) = \max \{ |I| \mid I \subseteq A, I \in \mathcal{F} \}$$

---

## Algoritmo Greedy e il Teorema di Rado-Edmonds

La connessione tra matroidi e algoritmi greedy è formalizzata dal **Teorema di Rado-Edmonds** (spesso chiamato semplicemente Teorema di Rado):

> **Teorema**:
> Sia $(E, \mathcal{F})$ un sistema di indipendenza. 
> L'algoritmo **GREEDY-MAX** (che ordina gli elementi per peso decrescente e li aggiunge ricorsivamente se mantengono l'indipendenza) trova un sottoinsieme indipendente di peso massimo per **qualsiasi** funzione peso non negativa $w: E \to \mathbb{R}^+$ se e solo se $(E, \mathcal{F})$ è un **matroide**.

Questo teorema stabilisce una corrispondenza biunivoca perfetta: i matroidi sono *esattamente* le strutture per cui l'approccio greedy è garantito essere ottimo per qualsiasi peso.

### Proof Sketch (Schema di Dimostrazione)

La correttezza si dimostra per induzione o per contraddizione confrontando la soluzione greedy con una generica soluzione ottima.

1. Sia $G = \{g_1, g_2, \dots, g_k\}$ l'insieme indipendente ordinato per peso decrescente scelto dall'algoritmo greedy:
   $$w(g_1) \ge w(g_2) \ge \dots \ge w(g_k)$$
2. Sia $O = \{o_1, o_2, \dots, o_k\}$ una soluzione ottima (anch'essa ordinata per peso decrescente).
3. Se $G = O$, allora greedy è ottimo. Se $G \ne O$, consideriamo il primo elemento in cui differiscono, sia esso all'indice $j$ (ovvero $g_j \ne o_j$).
4. Definiamo gli insiemi $A = \{g_1, \dots, g_{j-1}\}$ e $B = \{o_1, \dots, o_j\}$. Poiché $|B| > |A|$, per la **Proprietà di Scambio** esiste un elemento $x \in B \setminus A$ tale che $A \cup \{x\} \in \mathcal{F}$.
5. Poiché greedy valuta gli elementi in ordine strettamente decrescente e non ha scelto $x$ al passo $j$ (ma ha scelto $g_j$), deve valere che $w(g_j) \ge w(x)$. Inoltre, poiché $x \in B$, $w(x)$ deve essere almeno pari al peso degli elementi successivi di $O$.
6. Sostituendo l'elemento divergente in $O$ con $g_j$, costruiamo un nuovo insieme indipendente $O'$ il cui peso $w(O')$ è maggiore o uguale a $w(O)$.
7. Ripetendo questo processo per ogni divergenza, trasformiamo $O$ in $G$ senza mai diminuire il peso totale. Di conseguenza, $w(G) \ge w(O)$, dimostrando che $G$ è una soluzione ottima.

---

## Collegamenti ad Esercizi e Metodi

* **Guida Operativa e Dimostrazione**: [[metodo_greedy_matroidi_rado]]
* **Dimostrazione del Matroide Grafico**: [[metodo_dimostrazione_matroide_grafico]]
* **Esercizi correlati**: [[exam_2025_02_11_p2_completo_recupero_bonus]], [[exam_2026_01_12_bonus_matroidi]], [[exam_2025_06_09_p2_e03]]
