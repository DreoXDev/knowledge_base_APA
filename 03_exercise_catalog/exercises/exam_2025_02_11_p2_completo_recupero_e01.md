---
type: exercise
exam: 2025-02-11 Parte II completo/recupero
exercise_number: 1
topic:
  - MST
  - Kruskal
  - grafi_pesati
  - algoritmi_greedy
difficulty: media
status: cataloged
method:
  - [[metodo_kruskal_mst]]
---

# Esercizio 1 — Simulazione manuale di Kruskal per MST (11 Febbraio 2025)

## Testo

Si consideri un grafo non orientato, connesso e pesato $G = (V,E)$ con archi:
* $(b,c)$ di peso 4,
* $(b,d)$ di peso 1,
* $(a,c)$ di peso 6,
* $(a,b)$ di peso 7,
* $(c,d)$ di peso 2,
* $(d,e)$ di peso 5,
* $(c,e)$ di peso 3.

Mostrare nello schema sotto riportato l’ordine con cui l’algoritmo di **Kruskal** aggiunge (uno dopo l’altro) gli archi del *Minimum Spanning Tree*.

Avete a disposizione un numero di quadrati pari al numero di archi di $G$ (cioè 7 quadrati: Q1, Q2, Q3, Q4, Q5, Q6, Q7), contenente ciascuno i vertici di $G$. 

**DOVETE** riportare:
* nel quadrato **Q1** il primo arco aggiunto,
* nel quadrato **Q2** i primi due archi aggiunti,
* nel quadrato **Q3** i primi tre archi aggiunti,
* ...
* nel quadrato **Qi** i primi $i$ archi aggiunti,
* ...
* fino a mostrare l’intero MST costruito.

*Nota Bene: Non verranno considerate risposte che non seguono questo schema.*

---

## Risoluzione Guida Passo-Passo

### 1. Ordinamento degli archi per peso crescente
Elenchiamo e ordiniamo tutti i 7 archi del grafo in ordine non decrescente di peso:
1. $(b,d)$ — peso 1
2. $(c,d)$ — peso 2
3. $(c,e)$ — peso 3
4. $(b,c)$ — peso 4
5. $(d,e)$ — peso 5
6. $(a,c)$ — peso 6
7. $(a,b)$ — peso 7

### 2. Simulazione dell'algoritmo di Kruskal
Inizializziamo una foresta $T = \emptyset$ in cui ciascun vertice $\{a,b,c,d,e\}$ forma una componente connessa a sé stante.

* **Passo 1**: Esaminiamo l'arco di peso minimo $(b,d)$ (peso 1). 
  - I nodi $b$ e $d$ appartengono a componenti connesse disgiunte.
  - Aggiungiamo $(b,d)$ a $T$. 
  - *Stato foresta*: $T = \{(b,d)\}$. Componenti: $\{a\}$, $\{b,d\}$, $\{c\}$, $\{e\}$.
  - **Q1 contiene**: $\{(b,d)\}$.

* **Passo 2**: Esaminiamo l'arco $(c,d)$ (peso 2).
  - I nodi $c$ (componente $\{c\}$) e $d$ (componente $\{b,d\}$) sono in componenti disgiunte.
  - Aggiungiamo $(c,d)$ a $T$.
  - *Stato foresta*: $T = \{(b,d), (c,d)\}$. Componenti: $\{a\}$, $\{b,c,d\}$, $\{e\}$.
  - **Q2 contiene**: $\{(b,d), (c,d)\}$.

* **Passo 3**: Esaminiamo l'arco $(c,e)$ (peso 3).
  - I nodi $c$ (componente $\{b,c,d\}$) e $e$ (componente $\{e\}$) sono in componenti disgiunte.
  - Aggiungiamo $(c,e)$ a $T$.
  - *Stato foresta*: $T = \{(b,d), (c,d), (c,e)\}$. Componenti: $\{a\}$, $\{b,c,d,e\}$.
  - **Q3 contiene**: $\{(b,d), (c,d), (c,e)\}$.

* **Passo 4**: Esaminiamo l'arco $(b,c)$ (peso 4).
  - I nodi $b$ e $c$ appartengono alla **stessa** componente connessa ($\{b,c,d,e\}$).
  - L'inserimento dell'arco $(b,c)$ formerebbe un ciclo semplice $(b,d,c,b)$.
  - **Scartiamo** $(b,c)$.
  - *Stato foresta*: Invariato.
  - **Q4 contiene**: $\{(b,d), (c,d), (c,e)\}$.

* **Passo 5**: Esaminiamo l'arco $(d,e)$ (peso 5).
  - I nodi $d$ e $e$ appartengono alla **stessa** componente connessa ($\{b,c,d,e\}$).
  - L'inserimento dell'arco $(d,e)$ formerebbe un ciclo $(d,c,e,d)$.
  - **Scartiamo** $(d,e)$.
  - *Stato foresta*: Invariato.
  - **Q5 contiene**: $\{(b,d), (c,d), (c,e)\}$.

* **Passo 6**: Esaminiamo l'arco $(a,c)$ (peso 6).
  - Il nodo $a$ (componente $\{a\}$) e il nodo $c$ (componente $\{b,c,d,e\}$) sono in componenti disgiunte.
  - Aggiungiamo $(a,c)$ a $T$.
  - *Stato foresta*: $T = \{(b,d), (c,d), (c,e), (a,c)\}$.
  - Il numero di archi inseriti è $4 = |V|-1$. Tutte le componenti sono ora unite in un unico Spanning Tree di peso totale:
    $$W(T) = 1 + 2 + 3 + 6 = 12$$
  - **Q6 contiene**: $\{(b,d), (c,d), (c,e), (a,c)\}$.

* **Passo 7**: Esaminiamo l'arco $(a,b)$ (peso 7).
  - I nodi $a$ e $b$ appartengono alla stessa componente connessa.
  - **Scartiamo** $(a,b)$.
  - **Q7 contiene**: $\{(b,d), (c,d), (c,e), (a,c)\}$.

---

## Rappresentazione degli output (Q1 - Q7)

Per soddisfare rigorosamente lo schema grafico del foglio d'esame:

* **Q1**:
  $$\text{Archi aggiunti: } \{(b,d)\}$$
* **Q2**:
  $$\text{Archi aggiunti: } \{(b,d), (c,d)\}$$
* **Q3**:
  $$\text{Archi aggiunti: } \{(b,d), (c,d), (c,e)\}$$
* **Q4**:
  $$\text{Archi aggiunti: } \{(b,d), (c,d), (c,e)\}$$
* **Q5**:
  $$\text{Archi aggiunti: } \{(b,d), (c,d), (c,e)\}$$
* **Q6**:
  $$\text{Archi aggiunti: } \{(b,d), (c,d), (c,e), (a,c)\}$$
* **Q7**:
  $$\text{Archi aggiunti: } \{(b,d), (c,d), (c,e), (a,c)\}$$
