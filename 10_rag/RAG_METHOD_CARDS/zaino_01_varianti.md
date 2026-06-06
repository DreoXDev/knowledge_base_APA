---
type: rag-method-card
topic: zaino-01-varianti
status: complete
source_methods:
  - 04_methods/metodo_programmazione_dinamica_zaino_01.md
  - 04_methods/dp_knapsack_colori.md
source_examples:
  - 07_solved_examples/dp/knapsack_colori_SRC_NOTE_001.md
  - 07_solved_examples/by_topic/knapsack_max_R_rossi_SRC_EXTRA_001.md
source_patterns:
  - 06_exam_patterns/ricorrenza_zaino_01.md
exam_use: true
---

# Zaino 0/1 con varianti di colore

## Quando riconoscerlo

Frasi tipiche:

- "zaino 0/1 con capacita W"
- "al massimo R oggetti rossi"
- "oggetti colorati con vincoli sul numero scelto"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

`DP[i][w][r]` = valore massimo ottenibile usando solo i primi `i` oggetti, capacita residua/usata `w`, e scegliendo esattamente `r` oggetti rossi.

Per piu colori aggiungere dimensioni analoghe.

### 2. Casi base

`DP[0][w][0] = 0` per ogni `w`.

`DP[0][w][r] = -infty` per `r > 0`.

### 3. Ricorrenza / transizione

Oggetto `i` con peso `p_i`, valore `v_i`, indicatore rosso `c_i`.

Non prendo `i`:

`DP[i][w][r] = DP[i-1][w][r]`.

Prendo `i`, se `w >= p_i` e `r >= c_i`:

`DP[i][w][r] = max(DP[i][w][r], v_i + DP[i-1][w-p_i][r-c_i])`.

### 4. Ordine di calcolo

Calcolare per `i = 0..n`, `w = 0..W`, `r = 0..R`.

### 5. Soluzione finale

- Esattamente `R` rossi: `DP[n][W][R]`.
- Al massimo `R` rossi: `max_{0 <= r <= R} DP[n][W][r]`.

### 6. Ricostruzione, se richiesta

Se `DP[i][w][r] = DP[i-1][w][r]`, non prendo `i`; altrimenti prendo `i` e passo a `(i-1, w-p_i, r-c_i)`.

### 7. Complessita

Tempo: `O(n W R)`.

Spazio: `O(n W R)`, ottimizzabile a `O(W R)` senza ricostruzione.

### 8. Correttezza breve

Ogni soluzione ottima sui primi `i` oggetti o non contiene l'oggetto `i`, oppure lo contiene e allora il resto e una soluzione ottima sui primi `i-1` oggetti con capacita e conteggio aggiornati. La ricorrenza prende il migliore tra questi due casi. Per induzione su `i`, la cella finale e ottima.

## Errori da evitare

- Non riutilizzare un oggetto: la transizione deve partire da `i-1`.
- Non confondere peso con valore.
- Per "al massimo R", prendere il massimo su tutti i conteggi ammessi.
