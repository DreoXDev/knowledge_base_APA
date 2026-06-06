---
type: rag-method-card
topic: kruskal-step-by-step
status: complete
source_methods:
  - 04_methods/metodo_kruskal_mst.md
source_examples:
  - 03_exercise_catalog/exercises/exam_2025_11_10_p2_e01.md
  - 07_solved_examples/priority_examples_index.md
source_patterns:
  - 06_exam_patterns/simulazione_kruskal.md
exam_use: true
---

# Kruskal step-by-step

## Quando riconoscerlo

Frasi tipiche:

- "eseguire Kruskal"
- "trovare un MST"
- "ordinare gli archi per peso crescente"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Costruire un insieme `T` di archi che resta sempre aciclico e collega progressivamente le componenti.

### 2. Casi base

`T = vuoto`. Ogni vertice e una componente separata.

### 3. Ricorrenza / transizione

Ordina gli archi per peso crescente. Per ogni arco `(u,v)` in ordine:

- se `u` e `v` sono in componenti diverse, aggiungi `(u,v)` a `T` e fondi le componenti;
- altrimenti scarta l'arco perche creerebbe un ciclo.

### 4. Ordine di calcolo

Unica scansione degli archi ordinati, fermandosi quando `|T| = |V|-1`.

### 5. Soluzione finale

`T` e un albero di copertura minimo. Il peso e `sum_{e in T} w(e)`.

### 6. Ricostruzione, se richiesta

Mostrare tabella con colonne: arco, peso, componenti prima, scelto/scartato, motivo.

### 7. Complessita

Tempo: `O(|E| log |E|)` per ordinamento; union-find quasi lineare per le unioni.

Spazio: `O(|V|)`.

### 8. Correttezza breve

Ogni arco scelto da Kruskal e il piu leggero che collega due componenti diverse, quindi e sicuro per la proprieta del taglio. Aggiungerlo non crea cicli e mantiene l'esistenza di un MST che contiene gli archi scelti. Dopo `|V|-1` scelte si ottiene un albero di copertura minimo.

## Errori da evitare

- Non aggiungere archi che chiudono un ciclo.
- Non fermarsi prima di avere `|V|-1` archi.
- In caso di pesi uguali, qualsiasi ordine compatibile puo dare un MST valido.
