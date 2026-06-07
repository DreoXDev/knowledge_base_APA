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
- "ingombro complessivo <= W"
- "peso totale <= W"
- "costo complessivo <= W"
- "somma dei pesi al piu W"
- "LCS con budget"
- "ogni simbolo ha peso/costo"

## Regola critica

Quando la traccia usa parole come "complessivo", "totale", "somma", "budget" oppure "`<= W`", il vincolo riguarda l'intera soluzione. In DP questo richiede un indice di budget che viene consumato quando si sceglie un elemento.

Non sostituire mai un vincolo totale con una condizione locale tra elementi consecutivi, a meno che la traccia dica esplicitamente "crescente", "non decrescente" o simile.

Errore da evitare:

```text
w(prev) <= w(curr)
```

Questa condizione serve solo per sottosequenze crescenti/non decrescenti rispetto al peso, non per budget totale.

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Siano `X_i = <x_1,...,x_i>` e `Y_j = <y_1,...,y_j>`.

`C[i,j,p]` = lunghezza di una LCS di `X_i` e `Y_j` con ingombro complessivo `<= p`.

Indici: `0 <= i <= m`, `0 <= j <= n`, `0 <= p <= W`.

> [!Info]
> Esiste anche una formulazione alternativa con ingombro esattamente `b` e valore `-infinito` per stati impossibili.
> Per risposte d'esame compatte usare come default la formulazione `<= k`.

### 2. Casi base

`C[0,j,p] = 0` per ogni `j,p`.

`C[i,0,p] = 0` per ogni `i,p`.

### 3. Ricorrenza / transizione

Per `i>=1`, `j>=1`, `p=0..W`.

Se `x_i != y_j`:

`C[i,j,p] = max(C[i-1,j,p], C[i,j-1,p])`.

Se `x_i = y_j = a`:

```text
C[i,j,p] = max(C[i-1,j,p], C[i,j-1,p])
if p >= w(a):
    C[i,j,p] = max(C[i,j,p], 1 + C[i-1,j-1,p-w(a)])
```

Se `p < w(a)`, il ramo diagonale non e ammesso.

### 4. Ordine di calcolo

Calcolare `i = 0..m`, `j = 0..n`, `p = 0..W`.

### 5. Soluzione finale

`C[m,n,W]`.

### 6. Ricostruzione, se richiesta

Risalire da `C[m,n,W]`. Quando viene scelta la diagonale, chiamare prima la ricorsione su `(i-1,j-1,k-w(x_i))` e poi stampare `x_i`.

Schema compatto:

```text
STAMPA(i,j,p):
  if i==0 or j==0: return
  if C[i,j,p] == C[i-1,j,p]:
      STAMPA(i-1,j,p)
  else if C[i,j,p] == C[i,j-1,p]:
      STAMPA(i,j-1,p)
  else:
      STAMPA(i-1,j-1,p-w(x_i))
      stampa x_i
```

Chiamata: `STAMPA(m,n,W)`.

### 7. Complessita

Tempo: `O(m n W)`.

Spazio: `O(m n W)`, ottimizzabile se non serve ricostruzione.

### 8. Correttezza breve

Ogni LCS vincolata o ignora uno degli ultimi due simboli, oppure li usa entrambi quando coincidono e il budget residuo lo consente. La ricorrenza enumera esattamente questi casi. Per induzione sui prefissi e sul budget, ogni cella e ottima; `C[m,n,W]` risolve il vincolo "al massimo W".

## Errori da evitare

- Non usare la variante "esattamente b" come default quando la traccia dice "al massimo W".
- Non sottrarre il peso quando i due simboli non vengono presi.
- Non scrivere `-infinito` nei casi base della formulazione `<= k`.
- Non usare `C[i,j]` con condizione `w(prev)<=w(curr)` se la traccia parla solo di ingombro complessivo.
