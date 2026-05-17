---
type: exercise
exam: 2025-02-11 Parte II completo/recupero
exercise_number: 5
topic:
  - MST
  - arco_sicuro
  - dimostrazioni_teoriche
difficulty: medio-alta
status: cataloged
method:
  - [[metodo_teorema_arco_sicuro]]
---

# Esercizio 5 — Enunciato e Dimostrazione del Teorema dell'Arco Sicuro

## Testo

Enunciare e dimostrare il **teorema dell'arco sicuro** (Safe Edge Theorem).

---

## Risoluzione Formale

### 1. Definizioni Preliminari

* **Taglio**: Un taglio $(S, V \setminus S)$ di un grafo non orientato $G = (V,E)$ è una partizione dell'insieme dei vertici $V$.
* **Attraversamento**: Un arco $(u,v) \in E$ *attraversa* il taglio $(S, V \setminus S)$ se uno dei suoi estremi appartiene a $S$ e l'altro appartiene a $V \setminus S$.
* **Rispetto**: Un taglio $(S, V \setminus S)$ *rispetta* un insieme di archi $A \subseteq E$ se nessun arco in $A$ attraversa il taglio.
* **Arco Leggero**: Un arco $(u,v) \in E$ è un *arco leggero* per un taglio $(S, V \setminus S)$ se il suo peso è il minimo tra tutti gli archi che attraversano il taglio.
* **Arco Sicuro**: Un arco $e \notin A$ è *sicuro* per un sottoinsieme di archi $A$ (già contenuto in qualche albero di copertura minimo) se $A \cup \{e\}$ è anch'esso sottoinsieme di qualche albero di copertura minimo.

---

### 2. Enunciato del Teorema dell'Arco Sicuro

> **Teorema**:
> Sia $G = (V,E)$ un grafo non orientato, connesso e pesato con funzione peso $w: E \to \mathbb{R}$.
> Sia $A$ un sottoinsieme di $E$ contenuto in qualche albero di copertura minimo (MST) di $G$.
> Sia $(S, V \setminus S)$ un taglio di $G$ che rispetta $A$.
> Sia $(u,v)$ un arco leggero che attraversa il taglio $(S, V \setminus S)$.
> 
> Allora, l'arco $(u,v)$ è **sicuro** per $A$.

---

### 3. Dimostrazione

Sia $T$ un albero di copertura minimo (MST) di $G$ che contiene il sottoinsieme di archi $A$ ($A \subseteq T$). 

Dobbiamo dimostrare che esiste un albero di copertura minimo $T'$ che contiene $A \cup \{(u,v)\}$.

#### Caso 1: L'arco $(u,v)$ fa già parte di $T$ ($(u,v) \in T$)
In questo scenario, poniamo $T' = T$. Poiché $T$ è per ipotesi un MST contenente $A$, allora $T'$ è un MST che contiene banalmente $A \cup \{(u,v)\}$. La tesi è dimostrata.

#### Caso 2: L'arco $(u,v)$ non appartiene a $T$ ($(u,v) \notin T$)
Poiché $T$ è un albero di copertura, deve contenere un cammino semplice unico $P$ tra i vertici $u$ e $v$.

1. **Creazione del ciclo**:
   Se aggiungiamo l'arco $(u,v)$ a $T$, formiamo un unico ciclo semplice $C = P \cup \{(u,v)\}$.

2. **Esistenza di un secondo arco che attraversa il taglio**:
   Poiché il nodo $u$ appartiene a $S$ e il nodo $v$ appartiene a $V \setminus S$ (l'arco $(u,v)$ attraversa il taglio), il cammino semplice $P$ in $T$ che collega $u$ e $v$ deve necessariamente attraversare il taglio almeno una volta.
   Esiste quindi almeno un arco $(x,y) \in T$ nel cammino $P$ che attraversa il taglio $(S, V \setminus S)$.

3. **Proprietà del taglio e degli archi**:
   - L'arco $(x,y)$ non può appartenere ad $A$ ($(x,y) \notin A$), perché per ipotesi il taglio $(S, V \setminus S)$ rispetta $A$ (nessun arco in $A$ può attraversare il taglio).
   - Poiché $(u,v)$ è per ipotesi un *arco leggero* per il taglio, il suo peso soddisfa:
     $$w(u,v) \le w(x,y)$$

4. **Costruzione del nuovo albero $T'$**:
   Definiamo un nuovo insieme di archi $T'$ rimuovendo $(x,y)$ e aggiungendo $(u,v)$:
   $$T' = T \setminus \{(x,y)\} \cup \{(u,v)\}$$
   
   - *Connettività e assenza di cicli*: Rimuovendo un arco da un ciclo semplice $C$ manteniamo il grafo connesso senza cicli. Avendo $|V|-1$ archi, $T'$ è a tutti gli effetti un albero di copertura per $G$.
   - *Inclusione di A*: Poiché $(x,y) \notin A$, la rimozione di $(x,y)$ mantiene integro il sottoinsieme $A$ in $T'$. Quindi $A \cup \{(u,v)\} \subseteq T'$.

5. **Confronto del peso totale**:
   Calcoliamo il peso totale di $T'$:
   $$w(T') = w(T) - w(x,y) + w(u,v)$$
   
   Poiché $w(u,v) \le w(x,y)$, si ha:
   $$w(T') \le w(T)$$
   
   Ma per ipotesi $T$ è un albero di copertura minimo (MST), il che implica che il suo peso deve essere il minimo possibile:
   $$w(T) \le w(T') \implies w(T') = w(T)$$

Di conseguenza, anche $T'$ è un albero di copertura minimo (MST) di $G$. Poiché $A \cup \{(u,v)\} \subseteq T'$, l'arco $(u,v)$ è **sicuro** per $A$. 
La tesi è dimostrata ($\text{Q.E.D.}$).
