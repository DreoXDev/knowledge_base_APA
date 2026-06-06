---
type: rag-method-card
topic: riduzioni-np-completezza
status: complete
source_methods:
  - 04_methods/np_completezza_schema_dimostrazione.md
  - 04_methods/metodo_dimostrare_np_completezza.md
  - 04_methods/metodo_riduzione_3sat_clique.md
  - 04_methods/metodo_riduzione_3sat_independent_set.md
  - 04_methods/metodo_riduzione_clique_vertex_cover.md
source_examples:
  - 07_solved_examples/theory/np_completezza_schema_SRC_NOTE_001.md
  - 03_exercise_catalog/exercises/exam_2025_11_10_p2_e02.md
  - 03_exercise_catalog/exercises/exam_2025_09_17_p2_e04.md
source_patterns:
  - 06_exam_patterns/dimostrazione_np_completezza.md
  - 06_exam_patterns/riduzione_clique_vertex_cover.md
exam_use: true
---

# Riduzioni e NP-completezza

## Quando riconoscerlo

Frasi tipiche:

- "dimostrare che A e NP-completo"
- "costruire una riduzione polinomiale"
- "3-SAT <=p CLIQUE/Independent Set"
- "CLIQUE e Vertex Cover"

## Risposta da scrivere all'esame

### 1. Definizione sottoproblema

Per dimostrare che `A` e NP-completo:

1. mostrare `A in NP`;
2. scegliere un problema noto `B` NP-completo;
3. costruire una riduzione polinomiale `B <=p A`.

### 2. Casi base

Non applicabile. Se la richiesta e una riduzione specifica, fissare chiaramente istanza di partenza e istanza costruita.

### 3. Ricorrenza / transizione

Schema di riduzione:

- Input: istanza `x` di `B`.
- Costruzione: istanza `f(x)` di `A` in tempo polinomiale.
- Correttezza:
  - se `x` e istanza SI di `B`, allora `f(x)` e istanza SI di `A`;
  - se `f(x)` e istanza SI di `A`, allora `x` e istanza SI di `B`.

### 4. Ordine di calcolo

Scrivere sempre nell'ordine: NP, problema noto, costruzione, doppia implicazione, polinomialita, conclusione.

### 5. Soluzione finale

Poiche `B` e NP-completo, `B <=p A` e `A in NP`, allora `A` e NP-completo.

### 6. Ricostruzione, se richiesta

Per `3-SAT <=p CLIQUE`: creare un vertice per ogni letterale in ogni clausola; collegare vertici di clausole diverse se non sono complementari; chiedere clique di dimensione numero clausole.

Per `3-SAT <=p Independent Set`: costruzione analoga, ma collegamenti interni alla clausola e tra letterali incompatibili; chiedere independent set di dimensione numero clausole.

Per `CLIQUE <=p Vertex Cover`: usare lo stesso grafo e parametro `|V|-k`.

### 7. Complessita

La costruzione deve avere dimensione polinomiale nell'input e richiedere tempo polinomiale.

### 8. Correttezza breve

La doppia implicazione dimostra che l'istanza di partenza e positiva se e solo se l'istanza trasformata e positiva. Quindi un algoritmo polinomiale per `A` risolverebbe anche `B`. Poiche `B` e NP-completo, `A` e NP-hard; insieme a `A in NP`, segue che `A` e NP-completo.

## Errori da evitare

- Non ridurre nel verso sbagliato: serve `B noto NP-completo <=p A da dimostrare`.
- Non basta dire che la costruzione e intuitiva: serve doppia implicazione.
- Non dimenticare l'appartenenza a NP.
