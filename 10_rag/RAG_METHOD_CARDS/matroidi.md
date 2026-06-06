---
type: rag-method-card
topic: matroidi
status: complete
source_methods:
  - 04_methods/metodo_dimostrazione_matroide_grafico.md
  - 04_methods/metodo_dimostrare_matroide_foreste.md
  - 04_methods/metodo_dimostrazione_greedy_matroidi.md
  - 04_methods/metodo_greedy_matroidi_rado.md
source_examples:
  - 03_exercise_catalog/exercises/exam_2025_09_17_p2_e05.md
  - 03_exercise_catalog/exercises/exam_2025_11_10_p2_e05.md
  - 03_exercise_catalog/exercises/exam_2026_01_12_bonus_matroidi.md
source_patterns:
  - 06_exam_patterns/domanda_teorica_matroidi.md
exam_use: true
---

# Matroidi

## Quando riconoscerlo

Frasi tipiche:

- "dimostrare che e un matroide"
- "sistema di indipendenza"
- "proprieta ereditaria e proprieta di scambio"
- "matroide grafico", "foreste"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Un matroide e una coppia `M=(E,I)` dove `E` e l'insieme finito degli elementi e `I` e una famiglia di sottoinsiemi indipendenti.

Per il matroide grafico: `E` sono gli archi del grafo e `I` e la famiglia dei sottoinsiemi di archi che non contengono cicli, cioe foreste.

### 2. Casi base

Mostrare che `vuoto in I`. Nel matroide grafico, il grafo senza archi non contiene cicli.

### 3. Ricorrenza / transizione

Proprieta ereditaria:

Se `A in I` e `B subseteq A`, allora `B in I`. Infatti togliere archi da una foresta non puo creare cicli.

Proprieta di scambio:

Se `A,B in I` e `|A| < |B|`, allora esiste `e in B \ A` tale che `A union {e} in I`. Per foreste, `B` ha piu archi e quindi collega piu componenti; esiste un arco di `B` che collega due componenti distinte di `A`, quindi aggiungerlo non crea ciclo.

### 4. Ordine di calcolo

Scrivere: definizione di `E` e `I`, vuoto, ereditarieta, scambio, conclusione.

### 5. Soluzione finale

Poiche `I` soddisfa vuoto, ereditarieta e scambio, `(E,I)` e un matroide.

### 6. Ricostruzione, se richiesta

Se la domanda collega greedy/matroidi: su un matroide pesato, il greedy che considera gli elementi per peso e aggiunge quelli che mantengono l'indipendenza produce una base ottima.

### 7. Complessita

Per una dimostrazione teorica non serve una complessita. Per greedy su archi: ordinamento `O(|E| log |E|)` piu test di indipendenza.

### 8. Correttezza breve

La correttezza deriva dagli assiomi: ereditarieta garantisce che ogni sottoinsieme di una soluzione ammissibile resta ammissibile; scambio garantisce che una soluzione indipendente piu piccola puo essere estesa verso una piu grande. Queste proprieta sono esattamente quelle richieste dalla definizione di matroide.

## Errori da evitare

- Non confondere il grafo `G` con l'insieme base `E` del matroide.
- Nella proprieta di scambio serve trovare un elemento di `B \ A`.
- Non limitarsi a dire "e ovvio": va mostrato per ereditarieta e scambio.
