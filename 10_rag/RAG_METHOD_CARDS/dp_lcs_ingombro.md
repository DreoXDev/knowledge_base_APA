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

Siano `X_i = <x_1,...,x_i>` e `Y_j = <y_1,...,y_j>`.

`C[i,j,k]` = lunghezza di una LCS di `X_i` e `Y_j` con ingombro complessivo `<= k`.

Indici: `0 <= i <= m`, `0 <= j <= n`, `0 <= k <= W`.

> [!Info]
> Esiste anche una formulazione alternativa con ingombro esattamente `b` e valore `-infinito` per stati impossibili.
> Per risposte d'esame compatte usare come default la formulazione `<= k`.

### 2. Casi base

`C[0,j,k] = 0` per ogni `j,k`.

`C[i,0,k] = 0` per ogni `i,k`.

### 3. Ricorrenza / transizione

Se `x_i != y_j`:

`C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])`.

Se `x_i = y_j` e `w(x_i) <= k`:

```text
C[i,j,k] =
max(
  C[i-1,j,k],
  C[i,j-1,k],
  1 + C[i-1,j-1,k-w(x_i)]
)
```

Se `x_i = y_j` e `w(x_i) > k`:

`C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])`.

### 4. Ordine di calcolo

Calcolare `i = 0..m`, `j = 0..n`, `k = 0..W`.

### 5. Soluzione finale

`C[m,n,W]`.

### 6. Ricostruzione, se richiesta

Risalire da `C[m,n,W]`. Quando viene scelta la diagonale, chiamare prima la ricorsione su `(i-1,j-1,k-w(x_i))` e poi stampare `x_i`.

### 7. Complessita

Tempo: `O(m n W)`.

Spazio: `O(m n W)`, ottimizzabile se non serve ricostruzione.

### 8. Correttezza breve

Ogni LCS vincolata o ignora uno degli ultimi due simboli, oppure li usa entrambi quando coincidono e il budget residuo lo consente. La ricorrenza enumera esattamente questi casi. Per induzione sui prefissi e sul budget, ogni cella e ottima; `C[m,n,W]` risolve il vincolo "al massimo W".

## Errori da evitare

- Non usare la variante "esattamente b" come default quando la traccia dice "al massimo W".
- Non sottrarre il peso quando i due simboli non vengono presi.
- Non scrivere `-infinito` nei casi base della formulazione `<= k`.
