# Piano Codex — Ingestion appello APA 2025-01-13 Parte II

> [!Info]
> Piano operativo per aggiornare la repository `knowledge_base_APA` con il contenuto del PDF:
>
> `parteII-13gen25.pdf`
>
> Appello: **Analisi e Progetto di Algoritmi — Parte II — 13 gennaio 2025**

---

## Obiettivo

Integrare nella knowledge base Obsidian l'appello **Parte II del 13 gennaio 2025**, mantenendo coerenza con gli altri appelli Parte II già analizzati.

Il PDF contiene 5 domande principali più una sezione di domande facoltative premiali. I temi principali sono:

```txt
- Dijkstra su grafo orientato pesato;
- riduzione 3-CNF-SAT / 3-SAT → CLIQUE;
- chiusura transitiva / riflessiva-transitiva tramite programmazione dinamica;
- criterio per dimostrare che un problema A è NP-completo;
- matroide grafico e dimostrazione che è un matroide;
- domande bonus su LCS, matroidi/greedy, 3-SAT → Independent Set, CLIQUE → Vertex Cover.
```

> [!Important]
> Questo appello Parte II conferma alcuni pattern forti già emersi:
>
> - esercizio pratico su algoritmo classico, qui Dijkstra;
> - esercizio pratico su riduzioni NP-complete;
> - domanda teorica standard su chiusura transitiva;
> - domanda teorica standard su NP-completezza;
> - domanda lunga su matroidi;
> - domande bonus su dimostrazioni classiche.

---

## 1. File da creare

Creare il report di ingestion:

```txt
09_ingestion_reports/ingestion_report_exam_2025_01_13_part2.md
```

Creare la trascrizione essenziale dell'appello:

```txt
02_transcriptions/exams/exam_2025_01_13_part2.md
```

Creare i file degli esercizi catalogati:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_e01.md
03_exercise_catalog/exercises/exam_2025_01_13_p2_e02.md
03_exercise_catalog/exercises/exam_2025_01_13_p2_e03.md
03_exercise_catalog/exercises/exam_2025_01_13_p2_e04.md
03_exercise_catalog/exercises/exam_2025_01_13_p2_e05.md
```

Creare eventualmente un file separato per le domande bonus, se la struttura della repo lo supporta:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_bonus.md
```

oppure, in alternativa, inserirle come sezione finale nella trascrizione:

```txt
02_transcriptions/exams/exam_2025_01_13_part2.md
```

> [!Warning]
> Se esiste già una convenzione nella repo per le domande bonus/premiali, seguire quella convenzione invece di crearne una nuova.

---

## 2. File da aggiornare

Aggiornare gli indici degli esercizi:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

Aggiornare i pattern Parte II:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
```

Se già presenti, aggiornare anche i file specifici Parte II, ad esempio:

```txt
06_exam_patterns/parte_ii_patterns.md
06_exam_patterns/parte_ii_reductions_patterns.md
06_exam_patterns/parte_ii_greedy_mst_matroids_patterns.md
06_exam_patterns/parte_ii_np_completezza_patterns.md
```

Se non esistono, non crearli automaticamente tutti: creare solo quelli coerenti con la struttura attuale della repo.

Aggiornare o creare riferimenti nei metodi già esistenti:

```txt
04_methods/metodo_dijkstra_tracciamento_estrazioni.md
04_methods/metodo_riduzione_3sat_clique.md
04_methods/metodo_chiusura_transitiva_dp.md
04_methods/metodo_dimostrare_np_completezza.md
04_methods/metodo_matroide_grafico.md
04_methods/metodo_riduzione_3sat_independent_set.md
04_methods/metodo_riduzione_clique_vertex_cover.md
04_methods/metodo_greedy_max_matroidi.md
04_methods/metodo_lcs_sottostruttura_ottima.md
```

> [!Important]
> Prima di creare nuovi metodi, cercare nella repo se esistono già file equivalenti.
> Se esistono, aggiornarli invece di duplicarli.

Aggiornare la teoria collegata, se già presente:

```txt
05_theory/dijkstra.md
05_theory/shortest_paths.md
05_theory/np_completezza.md
05_theory/riduzioni_polynomiali.md
05_theory/3sat_clique_independent_set.md
05_theory/matroidi.md
05_theory/greedy.md
05_theory/lcs.md
05_theory/chiusura_transitiva.md
```

Aggiornare stato progetto e TODO:

```txt
PROJECT_STATUS.md
TODO.md
README.md
```

---

## 3. Trascrizione essenziale dell'appello

Creare il file:

```txt
02_transcriptions/exams/exam_2025_01_13_part2.md
```

Contenuto consigliato:

```md
# Appello APA — Parte II — 13 gennaio 2025

> [!Info]
> Fonte: `parteII-13gen25.pdf`
>
> Appello di Analisi e Progetto di Algoritmi, Parte II, 13 gennaio 2025.

## Struttura

| Esercizio | Valore | Tema |
|---|---:|---|
| 1 | 6 | Dijkstra su grafo orientato pesato |
| 2 | 6 | Riduzione 3-CNF-SAT / 3-SAT → CLIQUE |
| 3 | 7 | Chiusura transitiva / riflessiva-transitiva |
| 4 | 7 | Criterio per mostrare NP-completezza |
| 5 | 7 | Matroide grafico |
| Bonus | 3 | Dimostrazioni teoriche a scelta |

## Esercizio 1

Applicare l'algoritmo di Dijkstra al grafo orientato pesato indicato nel testo, usando il nodo `s` come sorgente.

Il testo richiede di mostrare, dopo ogni estrazione, il valore dell'attributo `d` in ogni nodo, specificare il nodo estratto e indicare gli archi effettivamente rilassati.

## Esercizio 2

Data la formula:

$$
\varphi =
(\neg x_1 \vee \neg x_2 \vee x_3)
\wedge
(x_1 \vee x_2 \vee x_3)
\wedge
(\neg x_1 \vee x_2 \vee \neg x_3)
$$

disegnare il grafo ottenuto dalla riduzione polinomiale da 3-CNF-SAT a CLIQUE.

Il testo richiede di posizionare:
- i vertici della prima clausola a sinistra;
- i vertici della seconda clausola in alto;
- i vertici della terza clausola a destra.

## Esercizio 3

Scrivere le equazioni di ricorrenza per calcolare la chiusura transitiva o riflessiva-transitiva di un grafo, usando coefficienti del tipo $e_{ij}^{k}$.

## Esercizio 4

Dato un problema specifico $A$ visto a lezione, indicare cosa è sufficiente mostrare per stabilire che $A$ è NP-completo.

## Esercizio 5

Definire il matroide grafico di un grafo non orientato $G=(V,E)$ e dimostrare che è effettivamente un matroide.

## Domande facoltative premiali

Una a scelta tra:

1. enunciare e dimostrare la proprietà della sottostruttura ottima della LCS;
2. dimostrare che se un sistema di indipendenza è un matroide, allora Greedy-max restituisce una soluzione ottima;
3. dimostrare che 3-SAT si riduce a Independent Set;
4. dimostrare che CLIQUE si riduce a Vertex Cover.
```

---

## 4. Esercizio 1 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_e01.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-01-13 Parte II — E01

> [!Info]
> Tema: Dijkstra con tracciamento delle estrazioni.
>
> Fonte: `parteII-13gen25.pdf`

## Richiesta

Eseguire l'algoritmo di Dijkstra su un grafo orientato pesato, usando `s` come sorgente.

Per ogni passo bisogna:

1. indicare il nodo estratto;
2. scrivere dentro ogni nodo il valore corrente dell'attributo $d$;
3. evidenziare gli archi effettivamente rilassati.

## Tipo di esercizio

```txt
Algoritmi su grafi
Dijkstra
Cammini minimi da sorgente singola
Tracciamento manuale
```

## Metodo collegato

Collegare a:

```md
[[metodo_dijkstra_tracciamento_estrazioni]]
```

oppure al metodo equivalente già presente nella repo.

## Note operative

Per risolvere correttamente:

1. inizializzare $d(s)=0$ e $d(v)=+\infty$ per ogni altro vertice;
2. mantenere l'insieme dei nodi non ancora estratti;
3. a ogni passo estrarre il nodo con valore $d$ minimo;
4. rilassare solo gli archi uscenti dal nodo appena estratto;
5. segnare come effettivamente rilassati solo gli archi che migliorano davvero il valore $d$ del nodo destinazione.

> [!Warning]
> Non basta indicare gli archi esaminati: il testo chiede gli archi effettivamente rilassati.
```

Pattern:

```txt
Parte II / Dijkstra / tracciamento estrazioni
```

Difficoltà stimata:

```txt
media
```

Collegamenti:

```md
[[Dijkstra]]
[[cammini minimi]]
[[rilassamento]]
```

---

## 5. Esercizio 2 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_e02.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-01-13 Parte II — E02

> [!Info]
> Tema: riduzione da 3-CNF-SAT a CLIQUE.
>
> Fonte: `parteII-13gen25.pdf`

## Richiesta

Data la formula:

$$
\varphi =
(\neg x_1 \vee \neg x_2 \vee x_3)
\wedge
(x_1 \vee x_2 \vee x_3)
\wedge
(\neg x_1 \vee x_2 \vee \neg x_3)
$$

disegnare il grafo ottenuto dalla riduzione polinomiale da 3-CNF-SAT a CLIQUE.

## Tipo di esercizio

```txt
NP-completezza
Riduzioni polinomiali
3-SAT
CLIQUE
Costruzione del grafo
```

## Metodo collegato

Collegare a:

```md
[[metodo_riduzione_3sat_clique]]
```

oppure al metodo equivalente già presente nella repo.

## Regola della riduzione

Per una formula con $k$ clausole:

1. creare un vertice per ogni letterale di ogni clausola;
2. non collegare vertici della stessa clausola;
3. collegare vertici di clausole diverse se i letterali non sono in conflitto;
4. una clique di dimensione $k$ corrisponde a una scelta consistente di un letterale vero per ogni clausola.

## Note specifiche

In questo appello ci sono tre clausole, quindi la clique cercata ha dimensione:

$$
k = 3
$$

Il disegno richiesto usa una disposizione grafica vincolata:

```txt
C1 a sinistra
C2 in alto
C3 a destra
```

> [!Warning]
> Prestare attenzione ai conflitti tra letterali complementari, ad esempio $x_i$ e $\neg x_i$.
```

Pattern:

```txt
Parte II / Riduzione 3-SAT → CLIQUE / costruzione grafo
```

Difficoltà stimata:

```txt
media
```

Collegamenti:

```md
[[3-SAT]]
[[CLIQUE]]
[[riduzioni polinomiali]]
[[NP-completezza]]
```

---

## 6. Esercizio 3 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_e03.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-01-13 Parte II — E03

> [!Info]
> Tema: chiusura transitiva / riflessiva-transitiva tramite ricorrenza.
>
> Fonte: `parteII-13gen25.pdf`

## Richiesta

Dato un grafo $G=(V,E)$, scrivere le equazioni di ricorrenza per stabilire, per ogni coppia $(i,j)$ di vertici, se esiste un cammino da $i$ a $j$.

Il testo usa coefficienti del tipo:

$$
e_{ij}^{k}
$$

## Tipo di esercizio

```txt
Programmazione dinamica
Grafi
Chiusura transitiva
Warshall / Floyd-Warshall booleano
Ricorrenze formali
```

## Metodo collegato

Collegare a:

```md
[[metodo_chiusura_transitiva_dp]]
```

oppure al metodo equivalente già presente nella repo.

## Significato del coefficiente

Il coefficiente $e_{ij}^{k}$ indica se esiste un cammino da $i$ a $j$ che usa come vertici intermedi solo vertici appartenenti all'insieme:

$$
\{1,2,\dots,k\}
$$

## Ricorrenza standard

Caso base:

$$
e_{ij}^{0} =
\begin{cases}
1 & \text{se } i=j \text{ oppure } (i,j) \in E \\
0 & \text{altrimenti}
\end{cases}
$$

Passo ricorsivo:

$$
e_{ij}^{k} =
e_{ij}^{k-1}
\vee
\left(e_{ik}^{k-1} \wedge e_{kj}^{k-1}\right)
$$

Soluzione:

$$
e_{ij}^{n}
$$

per ogni coppia $(i,j)$.

> [!Important]
> Questo esercizio è molto ricorrente nella Parte II e va collegato al pattern generale della chiusura transitiva.
```

Pattern:

```txt
Parte II / Chiusura transitiva / Ricorrenza Warshall
```

Difficoltà stimata:

```txt
facile-media
```

Collegamenti:

```md
[[chiusura transitiva]]
[[Warshall]]
[[programmazione dinamica su grafi]]
```

---

## 7. Esercizio 4 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_e04.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-01-13 Parte II — E04

> [!Info]
> Tema: criterio per dimostrare che un problema è NP-completo.
>
> Fonte: `parteII-13gen25.pdf`

## Richiesta

Considerando un problema specifico $A$ tra quelli visti a lezione, dire cosa è sufficiente mostrare per stabilire che $A$ è NP-completo.

Non è richiesta alcuna dimostrazione.

## Tipo di esercizio

```txt
Teoria
NP-completezza
Riduzioni polinomiali
Schema di dimostrazione
```

## Metodo collegato

Collegare a:

```md
[[metodo_dimostrare_np_completezza]]
```

oppure al metodo equivalente già presente nella repo.

## Risposta attesa

Per stabilire che $A$ è NP-completo è sufficiente mostrare che:

1. $A \in NP$;
2. esiste un problema $B$ già noto NP-completo tale che:

$$
B \leq_p A
$$

cioè $B$ si riduce polinomialmente ad $A$.

In questo modo si mostra che $A$ è NP-hard e, insieme ad $A \in NP$, si conclude che $A$ è NP-completo.

> [!Warning]
> La direzione della riduzione è fondamentale:
>
> bisogna ridurre un problema già noto NP-completo verso il problema nuovo $A$, non il contrario.
```

Pattern:

```txt
Parte II / NP-completezza / schema dimostrativo
```

Difficoltà stimata:

```txt
facile
```

Collegamenti:

```md
[[P]]
[[NP]]
[[NP-completo]]
[[riduzioni polinomiali]]
```

---

## 8. Esercizio 5 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_e05.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-01-13 Parte II — E05

> [!Info]
> Tema: matroide grafico.
>
> Fonte: `parteII-13gen25.pdf`

## Richiesta

Dato un grafo non orientato $G=(V,E)$:

1. definire il matroide grafico;
2. dimostrare che è effettivamente un matroide.

Il testo specifica che non occorre dimostrare che il numero di alberi in una foresta è pari alla differenza tra il numero di vertici e il numero di archi.

## Tipo di esercizio

```txt
Matroidi
Greedy
Grafi
Dimostrazione teorica
```

## Metodo collegato

Collegare a:

```md
[[metodo_matroide_grafico]]
```

oppure al metodo equivalente già presente nella repo.

## Definizione

Dato un grafo non orientato $G=(V,E)$, il matroide grafico è il sistema:

$$
M(G) = (E, \mathcal{F})
$$

dove:

$$
\mathcal{F} = \{ A \subseteq E \mid A \text{ non contiene cicli} \}
$$

cioè gli insiemi indipendenti sono gli insiemi di archi che formano una foresta.

## Dimostrazione richiesta

Bisogna mostrare che $(E,\mathcal{F})$ soddisfa gli assiomi di matroide:

1. $\emptyset \in \mathcal{F}$;
2. ereditarietà: se $A \in \mathcal{F}$ e $B \subseteq A$, allora $B \in \mathcal{F}$;
3. proprietà di scambio: se $A,B \in \mathcal{F}$ e $|A|<|B|$, allora esiste $e \in B \setminus A$ tale che $A \cup \{e\} \in \mathcal{F}$.

> [!Important]
> Questo esercizio è ricorrente e va collegato sia ai matroidi sia alla correttezza degli algoritmi greedy.
```

Pattern:

```txt
Parte II / Matroide grafico / dimostrazione assiomi
```

Difficoltà stimata:

```txt
alta
```

Collegamenti:

```md
[[matroidi]]
[[matroide grafico]]
[[greedy]]
[[foreste]]
```

---

## 9. Domande bonus — Catalogazione

Se viene creato un file separato:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p2_bonus.md
```

Contenuto consigliato:

```md
# Domande bonus — Appello 2025-01-13 Parte II

> [!Info]
> Fonte: `parteII-13gen25.pdf`
>
> Domanda facoltativa premiale: una a scelta tra quattro.
>
> Valore: 3 punti.

## Condizione di accesso al bonus

La domanda bonus è riservata a chi:

1. risponde a ognuna delle domande precedenti;
2. ottiene un punteggio non nullo in ciascuna;
3. supera l'intera Parte II.

Se sono presenti più risposte bonus, viene considerata solo la prima sul foglio protocollo.

## Bonus 1 — Sottostruttura ottima della LCS

Richiesta:

```txt
Siano X=<x1,...,xm> e Y=<y1,...,yn> due sequenze e sia Z=<z1,...,zk> una LCS di X e Y.
Enunciare e dimostrare la proprietà della sottostruttura ottima di Z.
```

Collegare a:

```md
[[metodo_lcs_sottostruttura_ottima]]
[[LCS]]
```

## Bonus 2 — Ottimalità di Greedy-max sui matroidi

Richiesta:

```txt
Dimostrare che se un sistema di indipendenza (E,F) è un matroide allora,
per ogni funzione peso w, Greedy-max restituisce una soluzione ottima.
```

Collegare a:

```md
[[metodo_greedy_max_matroidi]]
[[teorema_di_Rado]]
[[matroidi]]
```

## Bonus 3 — Riduzione 3-SAT → Independent Set

Richiesta:

```txt
Dimostrare che 3-SAT si riduce a Independent Set.
```

Collegare a:

```md
[[metodo_riduzione_3sat_independent_set]]
[[3-SAT]]
[[Independent Set]]
```

## Bonus 4 — Riduzione CLIQUE → Vertex Cover

Richiesta:

```txt
Dimostrare che CLIQUE si riduce a VERTEX-COVER.
```

Collegare a:

```md
[[metodo_riduzione_clique_vertex_cover]]
[[CLIQUE]]
[[Vertex Cover]]
```

> [!Summary]
> Le domande bonus sono altamente utili per il ripasso teorico perché raccolgono dimostrazioni classiche ricorrenti.
```

---

## 10. Pattern da aggiornare

Aggiornare i pattern ricorrenti con questo appello.

### Pattern pratici

```txt
- Dijkstra con compilazione tabellare/grafica dopo ogni estrazione.
- Riduzione 3-SAT → CLIQUE con costruzione esplicita del grafo.
```

### Pattern teorici

```txt
- Chiusura transitiva/riflessiva-transitiva con coefficiente e_ij^k.
- Criterio standard per dimostrare NP-completezza.
- Matroide grafico e verifica degli assiomi.
```

### Pattern bonus

```txt
- Sottostruttura ottima della LCS.
- Teorema di ottimalità Greedy-max su matroidi.
- Riduzione 3-SAT → Independent Set.
- Riduzione CLIQUE → Vertex Cover.
```

Aggiornare almeno:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
```

Aggiungere una riga nella tabella degli appelli Parte II:

```md
| 2025-01-13 Parte II | Dijkstra, 3-SAT→CLIQUE, chiusura transitiva, NP-completezza, matroide grafico | bonus: LCS, matroidi/greedy, 3-SAT→IS, CLIQUE→VC |
```

---

## 11. Differenze rispetto agli appelli Parte II già analizzati

Questo appello è molto simile agli appelli Parte II già emersi nella fase corrente.

Somiglianze:

```txt
- come 2025-06-09 e 2025-07-03, contiene Dijkstra come esercizio pratico;
- come 2025-11-10, contiene una riduzione da 3-SAT a CLIQUE;
- come 2025-11-10 e 2025-06-09, contiene la domanda sul criterio di NP-completezza;
- come 2025-11-10 e 2025-06-09, contiene il matroide grafico;
- come 2025-07-03 e 2025-11-10, contiene la chiusura transitiva.
```

Differenze:

```txt
- include una sezione bonus esplicita con 4 possibili dimostrazioni;
- l'esercizio pratico su riduzioni usa 3-SAT → CLIQUE, non CLIQUE → VERTEX-COVER;
- l'esercizio 1 usa Dijkstra, non Kruskal;
- la domanda sul matroide grafico è obbligatoria, non bonus.
```

> [!Important]
> Il pattern più forte da deduplicare è la domanda teorica sul matroide grafico, che compare in più appelli Parte II.
> Non creare note quasi identiche per ogni appello: creare un metodo centrale e collegare gli esercizi a quel metodo.

---

## 12. Note metodologiche importanti

### Dijkstra

Codex non deve cercare di ricostruire automaticamente una soluzione completa se non è già presente una soluzione verificata.

Per ora catalogare:

```txt
- grafo;
- sorgente;
- richiesta;
- metodo di risoluzione;
- attenzione agli archi effettivamente rilassati.
```

Se si decide di aggiungere una soluzione, marcarla come:

```md
> [!Warning]
> Soluzione da verificare graficamente sul PDF originale.
```

### Riduzione 3-SAT → CLIQUE

La costruzione può essere descritta in modo generale e poi applicata alla formula specifica.

Non inventare un disegno ASCII complesso se rischia di essere ambiguo. Meglio:

```txt
- elenco vertici;
- regola archi;
- conflitti esclusi;
- indicazione della clique cercata.
```

### Chiusura transitiva

La ricorrenza deve essere una nota ad alto rendimento perché compare più volte.

### NP-completezza

Mettere bene in evidenza la direzione della riduzione:

```txt
problema noto NP-completo ≤p nuovo problema A
```

### Matroide grafico

Usare un metodo unico per:

```txt
definizione;
assioma vuoto;
ereditarietà;
scambio.
```

Non duplicare dimostrazioni lunghe in ogni esercizio.

---

## 13. Aggiornare PROJECT_STATUS.md

Aggiungere una riga o sezione che dica:

```md
## Appelli Parte II

- [x] 2025-01-13 Parte II — report creato / da applicare
```

Se i report precedenti della Parte II sono già stati applicati, mantenere lo stato coerente, ad esempio:

```txt
2025-01-13 Parte II: ingestion report creato
```

Aggiornare anche la prossima azione:

```md
> [!Todo]
> Applicare il report dell'appello 2025-01-13 Parte II e verificare che i pattern Parte II siano deduplicati.
```

---

## 14. Aggiornare TODO.md

Aggiungere task:

```md
# TODO — Appello 2025-01-13 Parte II

- [ ] Creare ingestion report `ingestion_report_exam_2025_01_13_part2.md`.
- [ ] Creare trascrizione `exam_2025_01_13_part2.md`.
- [ ] Creare esercizi E01-E05 nel catalogo.
- [ ] Decidere se creare un file separato per le domande bonus.
- [ ] Collegare Dijkstra al metodo già esistente.
- [ ] Collegare 3-SAT→CLIQUE al metodo già esistente.
- [ ] Collegare chiusura transitiva al metodo già esistente.
- [ ] Collegare NP-completezza allo schema standard.
- [ ] Collegare matroide grafico al metodo già esistente.
- [ ] Aggiornare indici per appello, topic e difficoltà.
- [ ] Aggiornare pattern Parte II.
- [ ] Verificare deduplicazione con appelli 2025-06-09, 2025-07-03, 2025-11-10 e 2025-02-11.
```

---

## 15. Commit consigliato

Commit consigliato:

```txt
ingest APA 2025-01-13 part2 exam
```

Descrizione:

```txt
- add transcription for 2025-01-13 Parte II
- catalog Dijkstra, 3-SAT to CLIQUE, transitive closure, NP-completeness, graphic matroid exercises
- add optional bonus questions
- update Parte II patterns and indices
```

---

## 16. Stato atteso finale

Dopo l'applicazione del piano:

```txt
- il PDF 2025-01-13 Parte II è rappresentato nella KB;
- tutti i 5 esercizi principali sono catalogati;
- le domande bonus sono registrate;
- gli esercizi sono collegati a metodi e teoria già presenti o da creare;
- i pattern Parte II sono aggiornati;
- non ci sono duplicazioni inutili di metodi già esistenti;
- PROJECT_STATUS.md e TODO.md riflettono il nuovo stato.
```

---

## 17. Nota finale per Codex

> [!Important]
> Non inventare soluzioni complete non richieste dal piano.
>
> L'obiettivo di questo step è ingestion/catalogazione coerente dell'appello.
>
> Se nella repo esistono già metodi o note teoriche equivalenti, aggiornarle e collegarle invece di creare duplicati.
>
> Per le parti grafiche, in particolare Dijkstra e la riduzione 3-SAT → CLIQUE, mantenere una trascrizione essenziale e una descrizione metodologica. Se una soluzione grafica viene aggiunta, segnalarla come da verificare.
