# Piano Codex — Ingestion appello APA 2025-02-11 Parte II completo/recupero

> [!Info]
> Fonte analizzata: `parteII-11feb25-completo-recupero.pdf`.
>
> Appello: **Analisi e Progetto di Algoritmi — Parte II (scritto completo e recupero del II parziale) — 11 febbraio 2025**.
>
> Questo piano serve a far aggiornare la repository `knowledge_base_APA` senza usare Codex come lettore primario del PDF.

---

## Obiettivo

Integrare nella knowledge base l'appello Parte II dell'11 febbraio 2025, che contiene esercizi su:

```txt
1. Kruskal / Minimum Spanning Tree
2. Riduzione CLIQUE -> VERTEX-COVER su grafo concreto
3. Knapsack 0/1 tramite programmazione dinamica
4. Riduzione generale 3-SAT -> CLIQUE oppure 3-SAT -> INDEPENDENT SET
5. Teorema dell'arco sicuro
6. Domande facoltative premiali su matroidi/greedy, CLIQUE -> VERTEX-COVER, Dijkstra
```

Il file va trattato come **Parte II completo/recupero**, quindi usare naming esplicito per evitare collisioni con l'appello Parte I dell'11 febbraio 2025 già presente nella KB.

---

## 1. File da creare

Creare i seguenti file:

```txt
09_ingestion_reports/ingestion_report_exam_2025_02_11_part2_completo_recupero.md
02_transcriptions/exams/exam_2025_02_11_part2_completo_recupero.md
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e01.md
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e02.md
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e03.md
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e04.md
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e05.md
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_bonus.md
```

Se non esistono già, creare o consolidare anche questi metodi/teoria:

```txt
04_methods/metodo_kruskal_mst.md
04_methods/metodo_riduzione_clique_vertex_cover.md
04_methods/metodo_knapsack_01_dp.md
04_methods/metodo_riduzione_3sat_clique.md
04_methods/metodo_riduzione_3sat_independent_set.md
04_methods/metodo_teorema_arco_sicuro.md
04_methods/metodo_dimostrazione_correttezza_dijkstra.md
04_methods/metodo_greedy_matroidi_rado.md

05_theory/minimum_spanning_tree.md
05_theory/kruskal.md
05_theory/arco_sicuro.md
05_theory/riduzioni_np_completezza.md
05_theory/clique_vertex_cover_independent_set.md
05_theory/knapsack_01.md
05_theory/3sat_clique_independent_set.md
05_theory/matroidi_e_greedy.md
05_theory/dijkstra_correttezza.md
```

> [!Warning]
> Non duplicare file di metodo già creati dai precedenti appelli Parte II.
> Se un metodo esiste già, aggiornalo e collega questo appello come ulteriore occorrenza.

---

## 2. File da aggiornare

Aggiornare almeno:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
06_exam_patterns/parte_ii_theory_and_graph_patterns.md
PROJECT_STATUS.md
TODO.md
README.md
AI_CONTEXT.md
```

Se `06_exam_patterns/parte_ii_theory_and_graph_patterns.md` non esiste, crearlo.

---

## 3. Trascrizione essenziale dell'appello

Nel file:

```txt
02_transcriptions/exams/exam_2025_02_11_part2_completo_recupero.md
```

inserire una trascrizione sintetica con frontmatter simile:

```md
---
type: exam_transcription
exam: APA
part: II
date: 2025-02-11
variant: completo_recupero
status: transcribed
source: parteII-11feb25-completo-recupero.pdf
---
```

Contenuto consigliato:

```md
# Appello APA — Parte II — 2025-02-11 — completo/recupero

## Esercizi

1. Kruskal su grafo non orientato, connesso e pesato.
2. Riduzione da CLIQUE a VERTEX-COVER su grafo concreto.
3. Knapsack 0/1: ricorrenza per il valore ottimo `OPT(i,c)`.
4. Definizione del grafo nella riduzione da 3-SAT a CLIQUE oppure da 3-SAT a INDEPENDENT SET.
5. Enunciato e dimostrazione del teorema dell'arco sicuro.
6. Domanda facoltativa premiale, una a scelta:
   - dimostrare che se un sistema di indipendenza è un matroide allora Greedy-max restituisce una soluzione ottima;
   - dimostrare che CLIQUE si riduce a VERTEX-COVER;
   - dimostrare la correttezza dell'algoritmo di Dijkstra.
```

---

## 4. Esercizio 1 — Kruskal / MST

File:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e01.md
```

### Catalogazione

```yaml
topic:
  - grafi
  - minimum spanning tree
  - kruskal
  - greedy
difficulty: medium
exam_part: II
points: 6
status: cataloged
method: metodo_kruskal_mst
```

### Testo essenziale

Grafo non orientato, connesso e pesato con vertici:

```txt
{a,b,c,d,e}
```

Archi e pesi:

```txt
(b,c) peso 4
(b,d) peso 1
(a,c) peso 6
(a,b) peso 7
(c,d) peso 2
(d,e) peso 5
(c,e) peso 3
```

Richiesta:

```txt
Mostrare l'ordine con cui Kruskal aggiunge gli archi del Minimum Spanning Tree.
Usare lo schema Q1, Q2, ..., Q7, dove Qi contiene i primi i archi aggiunti fino alla costruzione dell'MST.
```

### Soluzione / note da includere

Ordinamento crescente degli archi:

```txt
1. (b,d), peso 1
2. (c,d), peso 2
3. (c,e), peso 3
4. (b,c), peso 4
5. (d,e), peso 5
6. (a,c), peso 6
7. (a,b), peso 7
```

Esecuzione Kruskal:

```txt
Q1: aggiunge (b,d)
Q2: aggiunge (b,d), (c,d)
Q3: aggiunge (b,d), (c,d), (c,e)
Q4: considera (b,c), ma NON lo aggiunge perché crea ciclo b-d-c-b
Q5: considera (d,e), ma NON lo aggiunge perché crea ciclo d-c-e-d
Q6: aggiunge (a,c)
Q7: considera (a,b), ma NON lo aggiunge perché crea ciclo
```

MST finale:

```txt
{(b,d), (c,d), (c,e), (a,c)}
```

Peso totale:

```txt
1 + 2 + 3 + 6 = 12
```

> [!Warning]
> Nel file esercizio distinguere chiaramente tra "arco considerato" e "arco aggiunto".
> Lo schema dell'esame richiede di mostrare progressivamente solo gli archi aggiunti all'MST, non tutti gli archi considerati.

### Collegamenti

Aggiungere link a:

```md
[[metodo_kruskal_mst]]
[[minimum_spanning_tree]]
[[arco_sicuro]]
```

---

## 5. Esercizio 2 — Riduzione CLIQUE -> VERTEX-COVER su grafo concreto

File:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e02.md
```

### Catalogazione

```yaml
topic:
  - np-completezza
  - riduzioni
  - clique
  - vertex cover
difficulty: medium
exam_part: II
points: 6
status: cataloged
method: metodo_riduzione_clique_vertex_cover
```

### Testo essenziale

Dato il grafo G mostrato nel PDF, disegnare il grafo G' ottenuto nella riduzione da CLIQUE a VERTEX-COVER e indicare quanti e quali sono i vertici della copertura di vertici di G'.

Dal diagramma del PDF, il grafo G ha vertici:

```txt
{a,b,c,d,e,f}
```

Archi visibili:

```txt
(a,b)
(a,f)
(f,e)
(b,e)
(b,c)
(c,e)
(e,d)
```

### Soluzione / note da includere

Nella riduzione standard:

```txt
(G, k) in CLIQUE
    ↓
(G', |V|-k) in VERTEX-COVER
```

Dove:

```txt
G' = complementare di G
```

Archi del complementare G', dato V = {a,b,c,d,e,f}, sono tutti gli archi non presenti in G:

```txt
(a,c)
(a,d)
(a,e)
(b,d)
(b,f)
(c,d)
(c,f)
(d,f)
```

Il PDF non specifica esplicitamente il valore di k nella trascrizione testuale, ma dal formato di questi appelli è probabile che si debba riconoscere una clique nel grafo G e indicare la corrispondente vertex cover nel complementare.

Clique evidente in G:

```txt
{b,c,e}
```

perché sono presenti:

```txt
(b,c), (b,e), (c,e)
```

Quindi per k = 3:

```txt
Vertex cover in G' = V \ {b,c,e} = {a,d,f}
```

Numero di vertici della copertura:

```txt
|V| - k = 6 - 3 = 3
```

> [!Warning]
> Segnare come assunzione che la clique scelta sia `{b,c,e}` e che quindi `k=3`.
> Se nella repo si preferisce non risolvere completamente gli esercizi grafici senza conferma visiva dettagliata, mantenere la soluzione come "soluzione probabile".

### Collegamenti

```md
[[metodo_riduzione_clique_vertex_cover]]
[[clique_vertex_cover_independent_set]]
[[riduzioni_np_completezza]]
```

---

## 6. Esercizio 3 — Knapsack 0/1 tramite programmazione dinamica

File:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e03.md
```

### Catalogazione

```yaml
topic:
  - programmazione dinamica
  - knapsack
  - ricorrenze
difficulty: easy-medium
exam_part: II
points: 7
status: cataloged
method: metodo_knapsack_01_dp
```

### Testo essenziale

Sono dati:

```txt
C ∈ N, C > 0
X = {1, ..., n}
```

Per ogni oggetto `i`:

```txt
v_i ∈ N, v_i > 0
w_i ∈ N, w_i > 0
```

Richiesta:

```txt
Scrivere le equazioni di ricorrenza per determinare il valore massimo di un sottoinsieme S di X con ingombro complessivo al più C.
Usare OPT(i,c) come coefficiente del sottoproblema generico (i,c).
```

### Ricorrenza da inserire

Significato:

```txt
OPT(i,c) = valore massimo ottenibile usando solo i primi i oggetti con capacità residua/totale c.
```

Caso base:

```md
$$
OPT(0,c) = 0 \quad \forall c \in \{0,\dots,C\}
$$

$$
OPT(i,0) = 0 \quad \forall i \in \{0,\dots,n\}
$$
```

Passo ricorsivo:

```md
$$
OPT(i,c) =
\begin{cases}
OPT(i-1,c) & \text{se } w_i > c \\
\max\{OPT(i-1,c),\ OPT(i-1,c-w_i)+v_i\} & \text{se } w_i \le c
\end{cases}
$$
```

Soluzione:

```md
$$
OPT(n,C)
$$
```

### Collegamenti

```md
[[metodo_knapsack_01_dp]]
[[knapsack_01]]
```

> [!Important]
> Questo esercizio è Parte II ma richiama la programmazione dinamica classica. Collegarlo anche ai pattern della Parte I, ma senza confonderlo con gli esercizi di DP con stato esteso su LCS/grafi.

---

## 7. Esercizio 4 — Riduzione 3-SAT -> CLIQUE oppure 3-SAT -> INDEPENDENT SET

File:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e04.md
```

### Catalogazione

```yaml
topic:
  - np-completezza
  - riduzioni
  - 3-sat
  - clique
  - independent set
difficulty: medium
exam_part: II
points: 7
status: cataloged
method:
  - metodo_riduzione_3sat_clique
  - metodo_riduzione_3sat_independent_set
```

### Testo essenziale

Data una formula 3-SAT:

```txt
f = C_1 ∧ ... ∧ C_k
```

con ogni clausola:

```txt
C_r = l_1^r ∨ l_2^r ∨ l_3^r
```

Richiesta:

```txt
Definire il grafo G utilizzato nella riduzione da 3-SAT a CLIQUE oppure da 3-SAT a INDEPENDENT SET, a scelta dello studente.
```

### Contenuto da inserire — versione 3-SAT -> CLIQUE

Costruzione:

```txt
- Per ogni clausola C_r e per ogni letterale l_i^r, creare un vertice v_i^r.
- Non collegare vertici della stessa clausola.
- Collegare due vertici v_i^r e v_j^s con r != s se i due letterali non sono complementari.
- Chiedere se esiste una clique di dimensione k.
```

Equivalenza:

```txt
La formula è soddisfacibile se e solo se il grafo costruito contiene una clique di dimensione k.
```

Idea:

```txt
Scegliere un vertice per ogni clausola equivale a scegliere un letterale vero per ogni clausola.
La condizione di clique impone che le scelte siano compatibili, cioè non contengano contemporaneamente una variabile e la sua negazione.
```

### Contenuto opzionale — versione 3-SAT -> INDEPENDENT SET

Costruzione alternativa:

```txt
- Per ogni clausola creare tre vertici, uno per ciascun letterale.
- Collegare i tre vertici della stessa clausola tra loro.
- Collegare vertici di clausole diverse se rappresentano letterali complementari.
- Chiedere se esiste un insieme indipendente di dimensione k.
```

Equivalenza:

```txt
La formula è soddisfacibile se e solo se il grafo contiene un independent set di dimensione k.
```

> [!Note]
> Siccome l'esercizio chiede una delle due riduzioni a scelta, nella KB conviene registrare entrambe, ma indicare chiaramente che in sede d'esame basta sceglierne una e scriverla bene.

### Collegamenti

```md
[[metodo_riduzione_3sat_clique]]
[[metodo_riduzione_3sat_independent_set]]
[[3sat_clique_independent_set]]
[[riduzioni_np_completezza]]
```

---

## 8. Esercizio 5 — Teorema dell'arco sicuro

File:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_e05.md
```

### Catalogazione

```yaml
topic:
  - minimum spanning tree
  - arco sicuro
  - dimostrazione
  - greedy
difficulty: medium-hard
exam_part: II
points: 7
status: cataloged
method: metodo_teorema_arco_sicuro
```

### Testo essenziale

Richiesta:

```txt
Enunciare e dimostrare il teorema dell'arco sicuro.
```

### Contenuto da collegare / consolidare

Il teorema deve comparire nella teoria MST:

```txt
Sia G=(V,E) un grafo non orientato, connesso e pesato.
Sia A un sottoinsieme di archi contenuto in qualche MST.
Sia (S, V-S) un taglio che rispetta A.
Se (u,v) è un arco leggero che attraversa il taglio, allora (u,v) è sicuro per A.
```

Idea della dimostrazione:

```txt
- Prendere un MST T che contiene A.
- Se T contiene già l'arco leggero, fatto.
- Altrimenti aggiungendo l'arco leggero a T si crea un ciclo.
- Nel ciclo esiste un altro arco che attraversa lo stesso taglio.
- Sostituire quell'arco con l'arco leggero non aumenta il peso totale.
- Si ottiene un MST che contiene A ∪ {(u,v)}.
- Quindi l'arco è sicuro.
```

### Collegamenti

```md
[[metodo_teorema_arco_sicuro]]
[[arco_sicuro]]
[[minimum_spanning_tree]]
[[metodo_kruskal_mst]]
```

---

## 9. Domanda facoltativa premiale

File:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p2_completo_recupero_bonus.md
```

### Catalogazione

```yaml
topic:
  - domande premiali
  - matroidi
  - greedy
  - riduzioni
  - dijkstra
difficulty: hard
exam_part: II
points: 3_bonus
status: cataloged
```

### Testo essenziale

Il PDF contiene una domanda facoltativa premiale da 3 punti, una a scelta tra:

```txt
1. Dimostrare che se un sistema di indipendenza (E,F) è un matroide, allora per ogni funzione peso w, Greedy-max restituisce una soluzione ottima.
2. Dimostrare che CLIQUE si riduce a VERTEX-COVER.
3. Dimostrare la correttezza dell'algoritmo di Dijkstra.
```

### Indicazioni per la KB

Non trattare queste domande come esercizi principali obbligatori, ma creare una sezione di pattern:

```txt
06_exam_patterns/parte_ii_bonus_questions.md
```

oppure aggiornare il file pattern Parte II se già esiste.

Per ciascuna domanda premiale, collegare a metodi già esistenti:

```md
[[metodo_greedy_matroidi_rado]]
[[metodo_riduzione_clique_vertex_cover]]
[[metodo_dimostrazione_correttezza_dijkstra]]
```

> [!Important]
> Queste domande sono ad alto valore per il ripasso orale/scritto: non sono obbligatorie nell'appello, ma rivelano dimostrazioni teoriche molto probabili.

---

## 10. Pattern da aggiornare

Aggiornare i pattern Parte II con queste ricorrenze:

### 10.1 MST / greedy

Pattern già emerso anche in altri appelli Parte II:

```txt
- Kruskal su grafo concreto.
- Teorema dell'arco sicuro.
- Dimostrazioni di correttezza per algoritmi greedy su MST.
```

Collegamenti:

```md
[[metodo_kruskal_mst]]
[[metodo_teorema_arco_sicuro]]
[[minimum_spanning_tree]]
```

### 10.2 NP-completezza e riduzioni

Pattern:

```txt
- CLIQUE -> VERTEX-COVER su grafo concreto.
- 3-SAT -> CLIQUE come costruzione generale.
- 3-SAT -> INDEPENDENT SET come alternativa.
```

Collegamenti:

```md
[[metodo_riduzione_clique_vertex_cover]]
[[metodo_riduzione_3sat_clique]]
[[metodo_riduzione_3sat_independent_set]]
[[riduzioni_np_completezza]]
```

### 10.3 Programmazione dinamica classica in Parte II

Pattern:

```txt
- Knapsack 0/1 con coefficiente OPT(i,c).
- Richiesta solo di ricorrenze, non necessariamente algoritmo completo.
```

Collegamenti:

```md
[[metodo_knapsack_01_dp]]
[[knapsack_01]]
```

### 10.4 Domande premiali

Pattern:

```txt
- Matroidi e correttezza del greedy.
- Riduzione CLIQUE -> VERTEX-COVER.
- Correttezza di Dijkstra.
```

---

## 11. Differenze rispetto agli appelli già analizzati

Rispetto a `parteII-03lug25.pdf`:

```txt
- Torna CLIQUE -> VERTEX-COVER su grafo concreto.
- Torna il teorema dell'arco sicuro.
- Al posto di Dijkstra/chiusura transitiva/P-NP, compare Knapsack 0/1.
```

Rispetto a `parteII-09giu25.pdf`:

```txt
- Torna il tema matroidi/greedy, ma come domanda premiale e non come domanda principale.
- Torna CLIQUE -> VERTEX-COVER.
- Compare Kruskal al posto di Dijkstra.
```

Rispetto a `parteII-10nov25.pdf`:

```txt
- Kruskal ha la stessa struttura, ma con pesi diversi.
- La riduzione concreta è CLIQUE -> VERTEX-COVER, mentre il 10 novembre aveva 3-SAT -> CLIQUE su formula specifica.
- Anche qui compare la costruzione generale 3-SAT -> CLIQUE / INDEPENDENT SET.
- Torna il matroide grafico/greedy solo come tema premiale indiretto, non come domanda principale.
```

---

## 12. Note metodologiche importanti

### 12.1 Non duplicare i metodi

Questo appello contiene molti pattern già comparsi negli altri Parte II.

Codex deve preferire:

```txt
aggiornare metodi esistenti
```

invece di creare:

```txt
metodo_kruskal_11_febbraio.md
metodo_vertex_cover_11_febbraio.md
```

### 12.2 Separare esercizio concreto e metodo generale

Per esempio:

```txt
exam_2025_02_11_p2_completo_recupero_e01.md
```

deve contenere i dati specifici del grafo e l'esecuzione di Kruskal.

Mentre:

```txt
04_methods/metodo_kruskal_mst.md
```

deve contenere lo schema generale applicabile a ogni grafo.

### 12.3 Usare callout Obsidian

Usare callout come:

```md
> [!Warning]
> ...

> [!Important]
> ...

> [!Example]
> ...
```

### 12.4 Formule LaTeX

Nei file Markdown usare:

```md
$...$
```

per formule inline e:

```md
$$
...
$$
```

per formule block.

---

## 13. Aggiornare PROJECT_STATUS.md

Aggiungere una riga/sezione:

```md
## Appelli Parte II

- [x] 2025-02-11 — Parte II completo/recupero — ingestion report creato
```

Se il report viene applicato subito:

```md
- [x] 2025-02-11 — Parte II completo/recupero — applicato alla KB
```

Aggiornare anche il riepilogo dei pattern Parte II:

```txt
- Kruskal / MST
- Teorema dell'arco sicuro
- Riduzioni 3-SAT, CLIQUE, VERTEX-COVER, INDEPENDENT SET
- Knapsack 0/1
- Matroidi e greedy come possibile domanda premiale
- Correttezza di Dijkstra come possibile domanda premiale
```

---

## 14. Aggiornare TODO.md

Aggiungere TODO operativi:

```md
## TODO dopo ingestion 2025-02-11 Parte II completo/recupero

- [ ] Verificare che il complementare del grafo dell'esercizio 2 sia corretto rispetto al disegno PDF.
- [ ] Collegare l'esercizio Kruskal al metodo generale MST/Kruskal.
- [ ] Collegare Knapsack 0/1 sia alla Parte II sia alla sezione DP classica.
- [ ] Consolidare le riduzioni 3-SAT -> CLIQUE e 3-SAT -> INDEPENDENT SET.
- [ ] Aggiungere una sezione di ripasso per domande premiali Parte II.
- [ ] Verificare che i metodi duplicati su arco sicuro e CLIQUE -> VERTEX-COVER siano unificati.
```

---

## 15. Commit consigliato

Messaggio commit consigliato:

```txt
Add APA 2025-02-11 Part II complete/recovery ingestion
```

Oppure, in italiano:

```txt
Aggiungi ingestion appello APA 2025-02-11 Parte II completo-recupero
```

---

## 16. Stato atteso finale

Dopo l'applicazione del piano, la repo deve avere:

```txt
- trascrizione essenziale dell'appello 2025-02-11 Parte II completo/recupero;
- 5 esercizi principali catalogati;
- 1 file per domande bonus;
- aggiornamento degli indici per esame, topic e difficoltà;
- aggiornamento dei pattern Parte II;
- collegamenti ai metodi generali già presenti o appena creati;
- TODO e PROJECT_STATUS coerenti;
- nessuna duplicazione inutile di metodi già esistenti.
```

---

## 17. Nota finale per Codex

> [!Important]
> Non inventare contenuti non presenti nel PDF.
>
> Per gli esercizi grafici, usa la soluzione proposta solo come supporto operativo e mantieni eventuali assunzioni esplicite con `[!Warning]`.
>
> La priorità è rendere la KB utile allo studio: ogni esercizio deve essere collegato a un pattern e a un metodo riusabile.
