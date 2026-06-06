---
type: rag-method-card
topic: dp-grafi-stato-esteso
status: warning
source_methods:
  - 04_methods/dp_grafi_floyd_warshall_stato_esteso.md
  - 04_methods/metodo_cammini_minimi_vincoli_colori_parita.md
  - 04_methods/metodo_dp_cammini_colori_conteggi.md
  - 04_methods/metodo_dp_cammini_colori_precedenze.md
source_examples:
  - 07_solved_examples/graphs/cammini_colori_floyd_warshall_SRC_NOTE_001.md
  - 07_solved_examples/graphs/floyd_warshall_colori_archi_SRC_NOTE_001.md
  - 07_solved_examples/graphs/floyd_warshall_coppie_colori_SRC_NOTE_001.md
source_patterns:
  - 06_exam_patterns/dp_con_stato_esteso.md
exam_use: true
---

# DP su grafi con stato esteso

## Quando riconoscerlo

Frasi tipiche:

- "cammino con vincoli sui colori degli archi"
- "numero pari/dispari di archi rossi"
- "prima un arco A poi un arco B"
- "cammino minimo con esattamente/al massimo k archi colorati"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Per variante Floyd-Warshall:

`DP[k][u][v][s]` = valore ottimo di un cammino da `u` a `v` che usa solo vertici intermedi in `{1,...,k}` e termina nello stato `s`.

Lo stato `s` rappresenta il vincolo: parita, conteggio colori, ultimo colore, fase della precedenza.

### 2. Casi base

Per `k = 0`, inizializzare:

- cammino vuoto: `DP[0][u][u][s0] = 0`;
- arco diretto `(u,v)`: aggiornare lo stato `s' = update(s0, colore(u,v))` e porre `DP[0][u][v][s'] = w(u,v)`;
- stati impossibili: `+infty` per minimizzazione o `false` per variante booleana.

### 3. Ricorrenza / transizione

Caso "non passo da k":

`DP[k][u][v][s] = DP[k-1][u][v][s]`.

Caso "passo da k":

`DP[k][u][v][s] = min(DP[k][u][v][s], DP[k-1][u][k][s1] + DP[k-1][k][v][s2])`

dove `combine(s1,s2)=s`.

Per DP booleana sostituire `min/+` con `or/and`.

### 4. Ordine di calcolo

Calcolare `k = 0..n`, poi tutte le coppie `(u,v)` e gli stati `s`.

### 5. Soluzione finale

Prendere `DP[n][sorgente][destinazione][s_accettante]`, oppure il minimo su tutti gli stati accettanti.

### 6. Ricostruzione, se richiesta

Memorizzare se la cella deriva dal caso "non passo da k" o dalla decomposizione tramite `k`. Ricostruire ricorsivamente i due sottocammini.

### 7. Complessita

Tempo: `O(n^3 |S|^2)` se si provano tutte le coppie di stati da combinare; `O(n^3 |S|)` se la transizione di stato e diretta.

Spazio: `O(n^3 |S|)` oppure `O(n^2 |S|)` senza ricostruzione completa.

### 8. Correttezza breve

Ogni cammino con intermedi in `{1,...,k}` o non usa il vertice `k`, oppure lo usa e si decompone in un cammino da `u` a `k` e uno da `k` a `v`, entrambi con intermedi in `{1,...,k-1}`. Lo stato esteso registra esattamente le informazioni necessarie sul vincolo. Per induzione su `k`, la cella finale contiene il cammino ottimo vincolato.

## Errori da evitare

- Non usare come fonte primaria formule marcate con warning senza verificare il vincolo.
- Non dimenticare lo stato iniziale `s0`.
- Non confondere cammino minimo con esistenza booleana.
