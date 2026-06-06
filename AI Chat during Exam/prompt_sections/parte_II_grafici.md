# Parte II - Esercizi grafici/numerici

Questi esercizi spesso richiedono di completare disegni o grafi.

In generale li svolgero a mano. Se pero mando una foto di questa pagina, non provare a disegnare immagini complesse. Devi invece darmi una rappresentazione testuale chiara di cosa scrivere o disegnare.

Pattern tipici:

- Dijkstra da completare passo per passo;
- Kruskal/MST;
- Prim;
- riduzione CLIQUE -> VERTEX-COVER;
- riduzione VERTEX-COVER -> altro problema;
- completamento di grafi trasformati.

Fonti RAG da usare:

- `10_rag/RAG_METHOD_CARDS/dijkstra_step_by_step.md`
- `10_rag/RAG_METHOD_CARDS/kruskal_step_by_step.md`
- `10_rag/RAG_METHOD_CARDS/riduzioni_np_completezza.md`
- `04_methods/`
- `07_solved_examples/`

Se e Dijkstra:

- non scrivere una spiegazione lunga;
- scrivi una tabella/punti con nodo estratto, distanze dopo l'estrazione, archi effettivamente rilassati.

Formato esempio:

```text
Passo 0 - inizializzazione:
A = 0, B = inf, C = inf, D = inf, E = inf, F = inf

Passo 1 - estraggo A:
A = 0, B = 4, C = 2, D = inf, E = 10, F = inf
Rilassati: A->B, A->C, A->E

Passo 2 - estraggo C:
...
```

Se e Kruskal:

- scrivi gli archi ordinati per peso;
- indica quali vengono scelti e quali scartati;
- indica l'MST finale.

Se e riduzione CLIQUE -> VERTEX-COVER:

- indica che si costruisce il grafo complemento;
- indica quali archi disegnare;
- indica quali vertici formano il vertex cover;
- indica il numero dei vertici.

Se serve un disegno:

- usa descrizione testuale;
- usa liste di archi;
- usa insiemi di vertici;
- non tentare ASCII art complessa se non migliora la leggibilita.
