# RAG Exam Answer Style

Durante l'esame, la risposta deve essere pronta da copiare a mano.

## Regole generali

- Non iniziare con spiegazioni lunghe.
- Non scrivere alternative se non sono richieste.
- Non scrivere codice eseguibile se basta pseudocodice.
- Non usare markdown pesante nella risposta finale.
- Usare sezioni brevi e fisse.

## Formato standard per DP

1. Sottoproblema
2. Casi base
3. Ricorrenza
4. Ordine di calcolo
5. Risposta finale
6. Ricostruzione, se richiesta
7. Complessita
8. Correttezza breve

## Formato DP su sequenze secondo PDF ufficiali

1. Definire sottoproblema
2. Definire coefficiente
3. Casi base
4. Passo ricorsivo separato per casi
5. Bottom-up
6. Ricostruzione
7. Complessita

Per esercizi LCS, rispondere sempre nell'ordine: sottoproblema, coefficiente, valore ottimo, casi base, ricorrenza, bottom-up, ricostruzione, complessita. Non partire direttamente dal codice.

Per generalizzazioni della LCS a piu sequenze:

1. Definire una dimensione della DP per ogni sequenza.
2. Indicare chiaramente il sottoproblema sui prefissi.
3. Indicare il coefficiente.
4. Scrivere casi base per ogni prefisso vuoto.
5. Nel match richiedere uguaglianza di tutti gli ultimi elementi.
6. Nel mismatch prendere il massimo scartando un elemento da una sequenza alla volta.
7. Dare complessita come prodotto delle lunghezze.

Per varianti LCS in cui la soluzione puo terminare in qualunque posizione:

1. Definire sottoproblema e coefficiente vincolati a terminare nel match corrente.
2. Specificare stati esistenti e inesistenti (`-infinito` oppure `0`, secondo la variante ufficiale).
3. Scrivere le ricorrenze.
4. Indicare il valore ottimo come massimo globale sui coefficienti validi.
5. Aggiungere ricostruzione solo se richiesta.

Per varianti LCS con vincoli sulla posizione nella sottosequenza:

1. Specificare cosa rappresenta la posizione nella sottosequenza.
2. Non confonderla con l'indice in `X` o `Y`.
3. Usare la lunghezza precedente per capire la posizione del nuovo elemento.
4. Indicare se la sequenza vuota e ammessa.

## Formato standard per grafi

1. Modellazione dello stato
2. Inizializzazione
3. Transizione/rilassamento
4. Algoritmo
5. Complessita
6. Correttezza breve

## Formato standard per greedy

1. Algoritmo
2. Criterio greedy
3. Correttezza
4. Complessita

## Risposte su MST / Prim

Quando la traccia chiede MST:

1. Specificare che il grafo e non orientato, connesso e pesato.
2. Distinguere spanning tree da minimum spanning tree.
3. Se si usa Prim o Kruskal, richiamare l'arco sicuro.
4. Per Prim, indicare `key`, `pi`, `Q`.
5. Per esercizi numerici, mostrare ordine di estrazione e aggiornamenti.

## Risposte su LICS

Quando la traccia chiede LICS o varianti:

1. Definire il sottoproblema vincolato a terminare.
2. Definire `c_ij`.
3. Chiarire che il valore finale e `max c_ij`.
4. Scrivere il filtro sui predecessori.
5. Non usare la ricorrenza LCS standard.

## Risposte su Knapsack (Zaino)

Quando la traccia chiede lo zaino:
1. **Distinguere la tipologia**: Zaino 0/1 (DP) vs Zaino Frazionario (Greedy).
2. **Per lo Zaino 0/1**: Definire formalmente sottoproblema, casi base, equazione di ricorrenza con rami "non prendo" ed "eventualmente prendo", valore ottimo finale e algoritmo di ricostruzione.
3. **Per vincoli aggiuntivi** (es. colori o quantità): Aggiungere una dimensione allo stato per il budget residuo (es. $r \in \{0, \dots, K\}$). Aggiornare lo stato speciale solo quando si sceglie un oggetto che consuma tale budget.

## Risposte su Floyd-Warshall e varianti

Per varianti di Floyd-Warshall:

1. Riconoscere che `k` indica i vertici intermedi ammessi `{1,...,k}`.
2. Definire il sottoproblema.
3. Definire il coefficiente.
4. Specificare eventuali stati extra.
5. Scrivere i casi base `k=0`.
6. Nel passo ricorsivo separare `E1`: il cammino non usa `k`, ed `E2`: il cammino usa `k`.
7. Spiegare come si combinano gli stati extra.
8. Indicare il valore finale.

Usare `min/+` per cammini minimi e `OR/AND` per esistenza. Non saltare i casi base: nelle varianti con vincoli, la maggior parte degli errori nasce da li.

## Risposte su Greedy e Matroidi

Quando la traccia chiede greedy o matroidi:
1. **Non limitarsi a intuizioni**: Evitare spiegazioni verbali generiche come "scelgo localmente il migliore".
2. **Specificare il criterio**: Definire l'ordinamento (crescente/decrescente) degli elementi e la regola locale di scelta.
3. **Giustificare la correttezza**: 
   - Richiamare il teorema dell'arco sicuro per problemi di MST.
   - Per i matroidi, definire formalmente il sistema di indipendenza $\langle E, \mathcal{F} \rangle$, dimostrare la **proprietà ereditaria** e la **proprietà di scambio**, e concludere tramite il teorema di Rado-Edmonds.

## Formato standard per NP-completezza

Quando la traccia chiede la NP-completezza:
1. **Separare sempre $\Pi \in NP$ da $NP$-hard**: Dimenticare l'appartenenza a NP costa punti.
2. **Appartenenza a NP**: Definire esplicitamente certificato polinomiale e verificatore deterministico di tempo polinomiale.
3. **NP-hard**:
   - Indicare il problema noto NP-completo di partenza (es. 3SAT, Clique, Vertex Cover).
   - Scrivere esplicitamente la **direzione della riduzione** (Noto $\le_p$ Nuovo).
   - Costruire la trasformazione polinomiale.
   - Dimostrare la correttezza in **entrambi i versi** ($\implies$ e $\impliedby$).
4. **Concludere**: Usare la formulazione standard di chiusura.
