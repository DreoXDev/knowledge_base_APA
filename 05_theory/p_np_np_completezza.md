---
type: theory
topic: p_np_np_completezza
status: complete
tags:
  - apa
  - teoria
  - topic/np-completezza
---

# Teoria — P, NP e NP-completezza

Nello studio della complessità computazionale, ci si concentra sulla classificazione dei problemi in base alle risorse di tempo necessarie per risolverli.

---

## Problemi di Decisione

Un **problema di decisione** è un problema computazionale la cui risposta per ogni istanza di input è binaria:
$$\text{YES / NO} \quad (\text{oppure } 1 / 0)$$
Le classi di complessità come **P** e **NP** sono definite formalmente solo per problemi di decisione. I problemi di ottimizzazione possono essere ricondotti a problemi di decisione imponendo una soglia (es. "esiste una clique di dimensione $\ge k$?").

---

## Classe P

La classe **P** (Polynomial-time) è l'insieme dei problemi di decisione che possono essere risolti da un algoritmo deterministico in tempo polinomiale, ossia in tempo $O(|x|^c)$ per una qualche costante $c \ge 1$, dove $|x|$ è la dimensione dell'input.
- Esempi in P: cammini minimi, connessione nei grafi, ordinamento, programmazione lineare.

---

## Classe NP

La classe **NP** (Non-deterministic Polynomial-time) è l'insieme dei problemi di decisione per cui una risposta `YES` può essere **verificata** in tempo polinomiale da un algoritmo deterministico, a patto che venga fornito un opportuno **certificato** (o testimone).
- Formalmente: $P \subseteq NP$. Non è noto se $P = NP$, ma la congettura prevalente è che $P \ne NP$.

### Certificato e Verificatore Polinomiale
* **Certificato ($y$)**: Un'informazione aggiuntiva di dimensione polinomiale rispetto all'input ($|y| \le |x|^d$) che dimostra che l'istanza $x$ è positiva.
* **Verificatore ($A$)**: Un algoritmo deterministico che prende in input l'istanza $x$ e il certificato $y$ e restituisce $1$ se il certificato è valido, $0$ altrimenti.
* **Verificatore Polinomiale**: Il verificatore lavora in tempo polinomiale rispetto alla sola dimensione dell'input $|x|$.

---

## Esempi di problemi in NP

### 1. Ciclo Hamiltoniano in NP
Un ciclo Hamiltoniano è un ciclo che visita ogni vertice del grafo $G = (V,E)$ esattamente una volta.
- **Certificato**: La sequenza ordinata di vertici $v_1, v_2, \dots, v_n$ che costituisce il ciclo.
- **Verificatore polinomiale**:
  1. Controlla che la sequenza contenga esattamente $n$ vertici distinti di $V$.
  2. Verifica che per ogni coppia consecutiva $(v_i, v_{i+1})$ e per la coppia finale $(v_n, v_1)$ esista un arco in $E$.
  3. Il tempo richiesto è $O(n)$, ovvero lineare, quindi polinomiale.

### 2. Clique in NP
Una clique è un sottoinsieme di vertici $C \subseteq V$ del grafo $G = (V,E)$ tale che ogni coppia di vertici in $C$ sia adiacente.
- **Certificato**: Un sottoinsieme di vertici $C$.
- **Verificatore polinomiale**:
  1. Verifica che $|C| = k$.
  2. Per ogni coppia $u, v \in C$ con $u \ne v$, controlla se l'arco $(u,v) \in E$.
  3. Richiede $O(k^2)$ controlli sulla struttura del grafo, ed essendo $k \le |V|$ il tempo è polinomiale.

---

## Il Problema SAT e il Teorema di Cook

* **SAT (Satisfiability)**: Data una formula booleana, stabilire se esiste un'assegnazione di valori di verità alle variabili che renda la formula vera.
* **SAT in NP**: Data un'assegnazione booleana come certificato, possiamo valutare la formula e verificare in tempo polinomiale se il risultato è vero.

### Teorema di Cook (1971)
> **Teorema**: SAT è NP-completo.
> *Significato*: Ogni altro problema $B \in NP$ può essere ridotto in tempo polinomiale a SAT ($B \le_p SAT$). SAT è quindi il primo problema formalmente dimostrato essere tra i "più difficili" in NP.

---

## Warning d'Esame

> [!WARNING]
> **NP non significa "Non Polinomiale"!**
> "NP" sta per *Non-deterministic Polynomial-time*. I problemi in NP potrebbero essere risolvibili in tempo polinomiale (se $P = NP$), ma attualmente sappiamo solo che sono *verificabili* in tempo polinomiale. Dire che un problema in NP non è polinomiale è un grave errore concettuale.

---

## Collegamenti

- Teoria riduzioni: [[riduzioni_np_completezza]]
- Metodo dimostrazione: [[np_completezza_schema_dimostrazione]]
- Esempio di riduzione 3SAT -> Clique: [[riduzione_3sat_clique_schema]]
- Esempio Clique to VC: [[metodo_riduzione_clique_vertex_cover]]
