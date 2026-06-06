---
type: rag-method-card
topic: dp-lcs-colori
status: complete
source_methods:
  - 04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
  - 04_methods/dp_lcs_vincoli_colore.md
source_examples:
  - 07_solved_examples/dp/lcs_esattamente_k_rossi_SRC_NOTE_001.md
  - 07_solved_examples/dp/lcs_al_massimo_k_rossi_SRC_NOTE_001.md
  - 07_solved_examples/by_topic/lcs_esattamente_3_rossi_SRC_EXTRA_001.md
source_patterns:
  - 06_exam_patterns/dp_su_sequenze_con_vincoli_di_conteggio.md
exam_use: true
---

# DP LCS con vincoli sui colori

## Quando riconoscerlo

Frasi tipiche:

- "sottosequenza comune con esattamente/al massimo k rossi"
- "LCS con vincolo sul numero di simboli di un colore"
- "almeno un rosso", "al massimo 2 blu", "esattamente 3 rossi"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Siano `X[1..n]`, `Y[1..m]`. Per un solo colore rosso:

`DP[i][j][r]` = lunghezza massima di una sottosequenza comune tra `X[1..i]` e `Y[1..j]` che usa esattamente `r` elementi rossi.

Per piu colori, aggiungere una dimensione per ogni conteggio vincolato, es. `DP[i][j][r][b]`.

### 2. Casi base

`DP[0][j][0] = DP[i][0][0] = 0`.

`DP[0][j][r] = DP[i][0][r] = -infty` per `r > 0` se il vincolo e "esattamente".

Per "al massimo", si puo usare lo stesso DP a conteggio esatto e poi prendere il massimo su `r <= k`.

### 3. Ricorrenza / transizione

Se `X[i] != Y[j]`:

`DP[i][j][r] = max(DP[i-1][j][r], DP[i][j-1][r])`.

Se `X[i] = Y[j] = a`, sia `c(a)=1` se `a` e rosso, altrimenti `0`:

`DP[i][j][r] = max(DP[i-1][j][r], DP[i][j-1][r], 1 + DP[i-1][j-1][r-c(a)])`.

Il terzo termine e valido solo se `r-c(a) >= 0`.

### 4. Ordine di calcolo

Calcolare per `i = 0..n`, `j = 0..m`, `r = 0..k`, con dipendenze gia disponibili da righe/colonne precedenti.

### 5. Soluzione finale

- Esattamente `k` rossi: `DP[n][m][k]`.
- Al massimo `k` rossi: `max_{0 <= r <= k} DP[n][m][r]`.
- Almeno `k` rossi: `max_{k <= r <= Rmax} DP[n][m][r]`.

### 6. Ricostruzione, se richiesta

Partire dalla cella finale e risalire scegliendo una transizione che realizza il massimo. Se si prende `X[i]=Y[j]`, aggiungere il carattere e diminuire il conteggio del colore se necessario.

### 7. Complessita

Tempo: `O(n m k)` per un colore; `O(n m k1 k2 ...)` per piu colori.

Spazio: `O(n m k)` oppure ottimizzabile se non serve ricostruire.

### 8. Correttezza breve

La ricorrenza considera tutti e soli i casi possibili: l'ultimo simbolo di una soluzione ottima non usa `X[i]`, non usa `Y[j]`, oppure usa la coppia `X[i]=Y[j]` aggiornando il conteggio del colore. Per induzione su `i+j`, ogni cella contiene il valore ottimo per il prefisso e per il conteggio fissato. La cella finale quindi risolve il problema originale.

## Errori da evitare

- Non confondere "esattamente k" con "al massimo k".
- Non inizializzare a `0` stati impossibili quando serve "esattamente".
- Non dimenticare di scalare il conteggio solo quando il carattere scelto ha il colore vincolato.
