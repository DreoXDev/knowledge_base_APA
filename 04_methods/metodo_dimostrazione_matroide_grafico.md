---
type: method
topic: Graphical Matroid proof
status: draft
tags:
  - apa
  - metodo
  - topic/grafi
  - topic/matroidi
  - topic/teoria
---

# Metodo - Definizione e Dimostrazione del Matroide Grafico

## Quando si usa

Questo metodo si applica quando viene chiesto di definire formalmente il **matroide grafico** associato a un grafo non orientato $G=(V,E)$ e dimostrare che la coppia $(E,F)$ soddisfa gli assiomi di matroide (ereditarietà e scambio).

---

## 1. Definizione Formale del Matroide Grafico

Sia $G = (V,E)$ un grafo non orientato e connesso. Il **matroide grafico** associato a $G$ è la coppia $M(G) = (E, F)$ definita come segue:
- L'insieme di base $E$ è l'insieme degli archi del grafo $G$.
- La famiglia $F$ contiene tutti i sottoinsiemi di archi $I \subseteq E$ tali che il sottografo parziale $G' = (V,I)$ è una **foresta** (ovvero non contiene cicli semplici).

---

## 2. Dimostrazione degli Assiomi di Matroide

Per dimostrare che $M(G) = (E,F)$ è un matroide, occorre verificare i due assiomi fondamentali:

### I. Assioma del Sottoinsieme (Ereditarietà)
- **Richiesta**: Se $A \in F$ e $B \subseteq A$, allora $B \in F$.
- **Dimostrazione**:
  Se $A \in F$, allora il sottografo $(V,A)$ è privo di cicli per definizione. Poiché $B$ è un sottoinsieme di archi di $A$, ovvero $B \subseteq A$, il sottografo $(V,B)$ è un sottografo parziale di $(V,A)$. Eliminare archi da un grafo privo di cicli non può introdurre nuovi cicli. Di conseguenza, anche $(V,B)$ non contiene cicli ed è quindi una foresta, il che implica che $B \in F$. $\blacksquare$

### II. Assioma di Scambio (Exchange Property)
- **Richiesta**: Siano $A, B \in F$ due foreste tali che $|A| < |B|$. Allora esiste un arco $e \in B \setminus A$ tale che $A \cup \{e\} \in F$.
- **Dimostrazione**:
  1. Ricordiamo che in un qualsiasi grafo non orientato con vertici $V$ e archi $I$, se il grafo non contiene cicli (cioè è una foresta), il numero di componenti connesse è pari a:
     $$c(I) = |V| - |I|$$
  2. Consideriamo le due foreste $G_A = (V,A)$ e $G_B = (V,B)$:
     - Il numero di componenti connesse di $G_A$ è $c(A) = |V| - |A|$.
     - Il numero di componenti connesse di $G_B$ è $c(B) = |V| - |B|$.
  3. Poiché per ipotesi $|A| < |B|$, ricaviamo immediatamente che:
     $$c(A) > c(B)$$
     Ciò significa che la foresta $G_A$ è divisa in un numero strettamente maggiore di componenti connesse (alberi isolati) rispetto a $G_B$.
  4. Per il principio dei cassetti, poiché $G_B$ ha meno componenti connesse di $G_A$, deve esistere almeno una componente connessa (albero) in $G_B$ i cui vertici sono distribuiti su due o più componenti connesse distinte di $G_A$.
  5. Di conseguenza, in questa componente di $G_B$ deve esistere almeno un arco $e = (u,v) \in B$ tale che i suoi estremi $u$ e $v$ appartengono a due componenti connesse distinte di $G_A$.
  6. Chiaramente, l'arco $e$ non può appartenere ad $A$ (poiché in $G_A$ i nodi $u$ e $v$ sono in componenti disgiunte, mentre la presenza di $e$ in $A$ li renderebbe direttamente connessi). Quindi, $e \in B \setminus A$.
  7. Se aggiungiamo l'arco $e$ ad $A$, esso connette due componenti connesse precedentemente separate di $G_A$, senza creare alcun ciclo (perché non esisteva alcun cammino tra $u$ e $v$ in $G_A$).
  8. Il sottografo $(V, A \cup \{e\})$ è quindi ancora privo di cicli, il che dimostra che:
     $$A \cup \{e\} \in F$$
  La proprietà di scambio è verificata. $\blacksquare$

---

## Esercizi collegati

- [[exam_2025_06_09_p2_e05]]
- [[exam_2025_11_10_p2_e05]]

## Errori comuni

> [!Warning]
> Confondere l'insieme di base: nei matroidi grafici, l'insieme di base $E$ è formato dagli **archi** del grafo, non dai vertici $V$.
> Non citare la relazione fondamentale tra vertici, archi e componenti connesse nelle foreste ($c = |V| - |I|$), che costituisce il cardine quantitativo della dimostrazione dell'assioma di scambio.
