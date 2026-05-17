---
type: method
topic: Programmazione dinamica zaino 0/1
status: complete
tags:
  - apa
  - metodo
  - topic/programmazione_dinamica
  - topic/zaino-01
---

# Metodo — Programmazione Dinamica Zaino 0/1

## Quando si usa

Questo metodo si applica quando l'esercizio richiede di:
1. Massimizzare il profitto o valore totale di una selezione di oggetti.
2. Rispettare un vincolo di capacità complessiva (peso, ingombro, tempo o costo).
3. Scegliere ciascun oggetto al massimo una volta (scelta binaria 0/1: prendo o non prendo).

---

## Schema Formale di Risoluzione (I 5 Pilastri)

Quando viene richiesto di impostare o scrivere le equazioni per lo Zaino 0/1 in sede d'esame, seguire scrupolosamente questa struttura formale:

### 1. Definizione Formale dei Sottoproblemi (Coefficienti)
Definire chiaramente cosa rappresenta la variabile di stato $OPT(i, c)$:
* $OPT(i, c)$ = valore massimo ottenibile selezionando un sottoinsieme di oggetti tra i primi $i$ oggetti (da $1$ a $i$) con capacità residua/totale dello zaino pari a $c$, per $i \in \{0, 1, \dots, n\}$ e $c \in \{0, 1, \dots, C\}$.

### 2. Casi Base
Impostare i casi banali che arrestano la ricorsione:
* **Nessun oggetto disponibile ($i = 0$)**:
  $$OPT(0, c) = 0 \quad \forall c \in \{0, 1, \dots, C\}$$
* **Capacità dello zaino nulla ($c = 0$)**:
  $$OPT(i, 0) = 0 \quad \forall i \in \{0, 1, \dots, n\}$$

### 3. Passo Ricorsivo
Esprimere il valore ottimo $OPT(i,c)$ per $i \ge 1$ e $c \ge 1$ mediante le decisioni ottime locali:

$$
OPT(i, c) =
\begin{cases}
OPT(i-1, c) & \text{se } w_i > c \\
\max\{OPT(i-1, c), \ OPT(i-1, c-w_i) + v_i\} & \text{se } w_i \le c
\end{cases}
$$

*Giustificazione*:
* Se il peso dell'oggetto $i$ ($w_i$) supera la capacità corrente $c$, non possiamo includerlo. Dunque la soluzione ottima coincide con quella senza l'oggetto $i$.
* Se l'oggetto $i$ può essere inserito ($w_i \le c$), confrontiamo l'esclusione (valore $OPT(i-1, c)$) con l'inclusione (valore $v_i$ più la soluzione ottima sul resto dello zaino $OPT(i-1, c-w_i)$), prendendo la scelta migliore.

### 4. Soluzione Finale
Indicare quale cella della matrice contiene la risposta al problema originale:
$$\text{Soluzione Ottima} = OPT(n, C)$$

### 5. Algoritmo di Ricostruzione (Backtracking)
Se richiesto, descrivere come recuperare l'insieme ottimo di oggetti $S$:
1. Inizializzare $i = n$, $c = C$ e $S = \emptyset$.
2. Finché $i > 0$ e $c > 0$:
   - Se $OPT(i, c) \neq OPT(i-1, c)$, significa che l'oggetto $i$ è stato incluso.
     - Aggiungere l'oggetto $i$ a $S$: $S = S \cup \{i\}$.
     - Sottrarre l'ingombro dell'oggetto $i$ dalla capacità: $c = c - w_i$.
   - Decrementare l'indice dell'oggetto: $i = i - 1$.

---

## Esercizi collegati

- [[exam_2026_01_12_e05]] (Risoluzione di Zaino 0/1 classico con ricostruzione)
- [[exam_2026_01_12_e01]] (Variante: Zaino 0/1 con vincolo di presenza obbligatoria di almeno un elemento rosso)
- [[exam_2025_02_11_p2_completo_recupero_e03]] (Scrittura formale delle equazioni di ricorrenza standard per Zaino 0/1)

---

## Errori comuni da evitare

> [!Warning]
> * **Dimensione indici**: Dimenticare di dichiarare gli intervalli di definizione per gli indici (es. $i \in \{0,\dots,n\}$ e $c \in \{0,\dots,C\}$).
> * **Caso base incompleto**: Scrivere solo $OPT(0,c) = 0$ tralasciando $OPT(i,0) = 0$ (o viceversa) può costare punti preziosi.
> * **Mancanza di spiegazione**: Non limitarsi a scrivere le formule matematiche; specificare sempre a parole il significato matematico del parametro $OPT(i,c)$.
