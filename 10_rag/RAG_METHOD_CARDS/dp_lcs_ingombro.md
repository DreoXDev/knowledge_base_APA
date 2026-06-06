---
type: rag-method-card
topic: dp-lcs-ingombro
status: complete
source_methods:
  - 04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md
  - 04_methods/dp_lcs_vincolo_somma_ingombro.md
source_examples:
  - 07_solved_examples/dp/lcs_somma_leq_k_SRC_NOTE_001.md
  - 07_solved_examples/by_topic/lcs_ingombro_SRC_EXTRA_001.md
source_patterns:
  - 06_exam_patterns/dp_su_sequenze_con_budget.md
exam_use: true
---

# DP LCS con ingombro o somma

## Quando riconoscerlo

Frasi tipiche:

- "sottosequenza comune di somma/ingombro al massimo K"
- "LCS con budget"
- "ogni simbolo ha peso/costo"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

`DP[i][j][b]` = lunghezza massima di una sottosequenza comune tra `X[1..i]` e `Y[1..j]` con ingombro totale esattamente `b`.

Se serve "al massimo B", si prende il massimo finale su `b <= B`.

### 2. Casi base

`DP[0][j][0] = DP[i][0][0] = 0`.

`DP[0][j][b] = DP[i][0][b] = -infty` per `b > 0`.

### 3. Ricorrenza / transizione

Se `X[i] != Y[j]`:

`DP[i][j][b] = max(DP[i-1][j][b], DP[i][j-1][b])`.

Se `X[i] = Y[j] = a`, con peso `w(a)`:

`DP[i][j][b] = max(DP[i-1][j][b], DP[i][j-1][b], 1 + DP[i-1][j-1][b-w(a)])`.

Il terzo termine e valido solo se `b >= w(a)`.

### 4. Ordine di calcolo

Calcolare `i = 0..n`, `j = 0..m`, `b = 0..B`.

### 5. Soluzione finale

`max_{0 <= b <= B} DP[n][m][b]`.

Se la traccia chiede ingombro esattamente `B`, usare `DP[n][m][B]`.

### 6. Ricostruzione, se richiesta

Risalire dalla cella finale. Quando viene scelta la diagonale, inserire il simbolo e diminuire `b` di `w(a)`.

### 7. Complessita

Tempo: `O(n m B)`.

Spazio: `O(n m B)`, ottimizzabile se non serve ricostruzione.

### 8. Correttezza breve

Ogni LCS vincolata o ignora uno degli ultimi due simboli, oppure li usa entrambi quando coincidono e il budget residuo lo consente. La ricorrenza enumera esattamente questi casi. Per induzione sui prefissi e sul budget, ogni cella e ottima; il massimo finale sui budget ammessi risolve il vincolo "al massimo".

## Errori da evitare

- Non usare `DP[n][m][B]` se la traccia dice "al massimo B".
- Non sottrarre il peso quando i due simboli non vengono presi.
- Non trattare gli stati impossibili come soluzioni valide.
