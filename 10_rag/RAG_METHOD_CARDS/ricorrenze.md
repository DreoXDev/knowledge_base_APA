---
type: rag-method-card
topic: ricorrenze
status: warning
source_methods:
  - 04_methods/recurrence_relations.md
  - 04_methods/metodo_equazioni_ricorrenza_chiusura_transitiva.md
source_examples:
  - 03_exercise_catalog/exercises/exam_2025_11_10_p2_e03.md
source_patterns:
  - 06_exam_patterns/recurring_theory_questions.md
exam_use: true
---

# Ricorrenze

## Quando riconoscerlo

Frasi tipiche:

- "risolvere la ricorrenza"
- "applicare il Master theorem"
- "equazioni di ricorrenza"
- "chiusura transitiva di Warshall"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Per ricorrenze divide-et-impera nella forma:

`T(n) = a T(n/b) + f(n)`.

Confrontare `f(n)` con `n^{log_b a}`.

Per chiusura transitiva:

`R_k[i][j] = true` se esiste un cammino da `i` a `j` che usa solo vertici intermedi in `{1,...,k}`.

### 2. Casi base

Master: `T(1)=Theta(1)`.

Warshall: `R_0[i][j] = true` se `i=j` oppure esiste arco `(i,j)`.

### 3. Ricorrenza / transizione

Master:

- se `f(n) = O(n^{log_b a - epsilon})`, allora `T(n)=Theta(n^{log_b a})`;
- se `f(n) = Theta(n^{log_b a} log^k n)`, allora `T(n)=Theta(n^{log_b a} log^{k+1} n)`;
- se `f(n) = Omega(n^{log_b a + epsilon})` e vale regolarita, allora `T(n)=Theta(f(n))`.

Warshall:

`R_k[i][j] = R_{k-1}[i][j] OR (R_{k-1}[i][k] AND R_{k-1}[k][j])`.

### 4. Ordine di calcolo

Master: calcolare `n^{log_b a}` e confrontare.

Warshall: calcolare `k = 1..n`, poi tutte le coppie `(i,j)`.

### 5. Soluzione finale

Master: indicare il caso applicato e la classe `Theta`.

Warshall: `R_n[i][j]` indica se `j` e raggiungibile da `i`.

### 6. Ricostruzione, se richiesta

Per Warshall, memorizzare il vertice `k` che rende vera la seconda parte e ricostruire i due sottocammini.

### 7. Complessita

Warshall: tempo `O(n^3)`, spazio `O(n^2)` o `O(n^3)` se si conservano tutti i livelli.

### 8. Correttezza breve

Per Warshall, un cammino con intermedi in `{1,...,k}` o non usa `k`, oppure usa `k` e si decompone in un cammino da `i` a `k` e uno da `k` a `j` con intermedi in `{1,...,k-1}`. Per induzione su `k`, la ricorrenza calcola esattamente la raggiungibilita.

## Errori da evitare

- `04_methods/recurrence_relations.md` e draft: usare questa card con prudenza.
- Nel Master theorem, non saltare il confronto con `n^{log_b a}`.
- Per Warshall, non usare `R_k` a destra della ricorrenza: servono valori di `R_{k-1}`.
