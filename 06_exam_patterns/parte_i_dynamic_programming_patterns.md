---
type: pattern
status: scaffold
tags:
  - apa
  - pattern
  - topic/programmazione-dinamica
---

# Pattern - Programmazione Dinamica in Parte I

> [!Info]
> Guida ai pattern e alle strutture standard per gli esercizi di Programmazione Dinamica (DP) nella Parte I degli appelli di APA.

---

## 1. Struttura Generale Richiesta

Tutti gli esercizi di DP in Parte I richiedono un'impostazione formale rigorosa divisa in:

1. **Definizione dei coefficienti**: Spiegare chiaramente cosa rappresenta ogni cella della tabella DP (es. $c_{i,j}$ è la lunghezza del sottoproblema prefisso).
2. **Caso base**: Definire le condizioni iniziali della tabella (es. quando una delle sequenze è vuota, o per $k=0$ intermedi nei grafi).
3. **Passo ricorsivo**: Esprimere i coefficienti del problema corrente in funzione di quelli dei sottoproblemi più piccoli, coprendo tutti i casi.
4. **Soluzione finale**: Indicare l'esatta coordinata o formula che restituisce il valore cercato.
5. **Algoritmo bottom-up**: Scrivere l'algoritmo iterativo per riempire la tabella.
6. **Algoritmo di ricostruzione**: Scrivere la procedura ricorsiva o iterativa all'indietro per stampare la soluzione ottima.

---

## 2. Pattern su Sequenze (LCS con Vincoli)

### Stato esteso
Quando oltre alla sequenza si hanno vincoli di budget o presenza (es. rossi, blu, ingombro), lo stato si estende aggiungendo dimensioni:

$$
C[i,j,v]
$$

dove:
- $i,j$ indicano i prefissi delle sequenze $X_i$ e $Y_j$.
- $v$ è la variabile del vincolo (contatore di rosso/blu, budget residuo, o stato booleano).

### Esempi e Variazioni:
*   **Vincolo di ingombro massimo (Budget)**: $C[i,j,w]$ = lunghezza LCS con ingombro $\le w$. 
    *   *Appello*: [[exam_2025_07_03_p1_e01]]
*   **Vincoli di conteggio massimo**: $C[i,j,r,b]$ = lunghezza LCS con al più $r$ rossi e $b$ blu.
    *   *Appelli*: [[exam_2025_06_09_p1_e01]], [[exam_2025_01_13_p1_e01]]
*   **Vincolo di presenza obbligatoria**: $C[i,j,r]$ con $r \in \{0,1\}$ dove $r=1$ indica presenza obbligatoria di almeno un rosso.
    *   *Appello*: [[exam_2025_11_10_p1_tema_a_e01]]
*   **LCS a tre sequenze con budget massimo**: $C[i,j,k,r]$ = lunghezza LCS a tre sequenze con al più $r$ rossi.
    *   *Appelli*: [[exam_2025_02_11_p1_completo_e01]], [[exam_2025_02_11_p1_recupero_e01]], [[exam_2025_09_17_p1_e01]]

---

## 3. Pattern su Grafi (DP Booleana / Stato Esteso)

### Chiusura transitiva modificata (Floyd-Warshall esteso)
Per stabilire l'esistenza di cammini con proprietà specifiche, si estende l'algoritmo di Floyd-Warshall definendo:

$$
D[k,i,j,h]
$$

dove:
- $k$ indica che i vertici intermedi utilizzabili sono solo nell'insieme $\{1,\dots,k\}$.
- $i,j$ sono i vertici sorgente e destinazione.
- $h$ è lo stato esteso (es. parità della lunghezza, conteggio archi colorati).

### Esempi e Variazioni:
*   **Vincolo di parità**: $D[k,i,j,p]$ con $p \in \{0,1\}$ indicante se il cammino ha numero pari ($0$) o dispari ($1$) di archi target.
    *   *Appelli*: [[exam_2026_01_12_e02]] (numero pari di archi totali), [[exam_2025_09_17_p1_e02]] (numero dispari di archi blu)
*   **Conteggio esatto di archi colorati**: $D[k,i,j,r,b]$ = esistenza cammino con esattamente $r$ rossi e $b$ blu.
    *   *Appello*: [[exam_2025_07_03_p1_e02]]
*   **Regole locali tra archi consecutivi**: Esistenza cammino senza transizioni vietate (es. $(R,N)$ o $(B,R)$, divieto di consecutivi identici $NN$ e $BB$, o divieto di $(N,R)$ e $(R,B)$). Richiede di salvare il colore del primo e dell'ultimo arco dello stato.
    *   *Appelli*: [[exam_2025_06_09_p1_e02]], [[exam_2025_02_11_p1_completo_e02]], [[exam_2025_01_13_p1_e02]]
*   **Somma aggregata di archi specifici**: $D[k,i,j,h]$ con $h \in \{0,1,2,3\}$ indicante che la somma degli archi A e B è esattamente $h$.
    *   *Appello*: [[exam_2025_11_10_p1_tema_a_e02]]
*   **Cammini minimi pesati con vincolo di parità ed esclusione locale**: $D[k,i,j,p]$ = peso minimo di un cammino con parità $p$ modulo 2 di archi blu, senza due vertici rossi consecutivi.
    *   *Appello*: [[exam_2025_02_11_p1_recupero_e02]]
