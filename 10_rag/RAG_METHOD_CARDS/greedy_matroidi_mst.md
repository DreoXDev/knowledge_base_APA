# Method Card — Greedy, Matroidi e MST (Kruskal/Prim)

## Triggers (Parole Chiave)

* `greedy`, `ingordo`, `scelta locale`, `greedy choice`
* `matroide`, `sistema di indipendenza`, `proprietà ereditaria`, `proprietà di scambio`, `scambio`
* `Kruskal`, `Prim`, `MST`, `albero ricoprente minimo`, `foresta`, `arco sicuro`, `Union-Find`, `Make-Set`, `Find-Set`, `Union`

---

## Decisione Rapida e Concetti Chiave

1. **Quando applicare Greedy**:
   - Solo se dimostrato corretto tramite **scambio** o mostrando che il problema costituisce un **matroide**.
   - Se il problema è modellabile come matroide pesato, l'algoritmo **GREEDY-MAX** (o GREEDY-MIN) trova l'ottimo globale (Teorema di Rado-Edmonds).

2. **Verificare se è un Matroide**:
   - Definire la coppia ordinata $M = (E, \mathcal{F})$ con $E$ insieme finito e $\mathcal{F}$ famiglia di sottoinsiemi indipendenti.
   - Mostrare **Proprietà Ereditaria**: se $A \in \mathcal{F}$ e $B \subseteq A \implies B \in \mathcal{F}$.
   - Mostrare **Proprietà di Scambio**: se $A, B \in \mathcal{F}$ e $|B| > |A|$, esiste $b \in B \setminus A$ tale che $A \cup \{b\} \in \mathcal{F}$.

3. **MST e Kruskal**:
   - Kruskal applica greedy sul **matroide grafico** (dove gli indipendenti sono foreste e le basi sono alberi di copertura).
   - Ordina gli archi in ordine **crescente** di peso.
   - Aggiunge un arco se e solo se collega due componenti disgiunte (controllato con `Find-Set` in Union-Find), altrimenti lo scarta (creerebbe un ciclo).

4. **Prim vs Kruskal**:
   - **Kruskal**: Greedy basato sugli archi globali. Mantiene una foresta disgiunta.
   - **Prim**: Greedy basato sulla crescita di una singola componente a partire da un vertice sorgente. Adatto quando il grafo è denso.

---

## Regole e Warning d'Esame

> [!WARNING]
> * **Giustificazione d'obbligo**: Nelle risposte d'esame non basta scrivere la scelta locale. Bisogna esplicitare il criterio greedy (es. ordinamento crescente degli archi) e fare riferimento al teorema dell'arco sicuro (Prim/Kruskal) o alla teoria dei matroidi.
> * **Insieme massimale vs massimo**: In un matroide, tutti gli insiemi indipendenti massimali hanno la stessa cardinalità (e sono basi).

---

## Riferimenti nella KB

* Teoria base greedy: [[greedy_teoria_base]]
* Teoria matroidi: [[matroidi_e_greedy]]
* Teoria Kruskal/Matroide grafico: [[kruskal_matroide_grafico]]
* Metodo Kruskal: [[metodo_kruskal_mst]]
* Metodo Prim: [[mst_prim]]
* Esempio svolto Kruskal: [[kruskal_schema_esecuzione]]
* Esempio svolto Prim: [[prim_schema_esecuzione]]
