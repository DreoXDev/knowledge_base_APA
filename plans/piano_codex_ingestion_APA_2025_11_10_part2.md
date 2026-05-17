# Piano Codex — Ingestion appello APA 2025-11-10 Parte II

> [!Info]
> Piano operativo per aggiornare la repository `knowledge_base_APA` a partire dal PDF:
>
> `parteII-10nov25.pdf`
>
> Appello: **Analisi e Progetto di Algoritmi — Parte II — 10 novembre 2025**

---

## Obiettivo

Integrare nella knowledge base l'appello **Parte II del 10 novembre 2025**, mantenendo coerenza con gli ingestion report già creati per gli altri appelli di Parte II.

Questo appello è importante perché conferma vari pattern già emersi nella Parte II:

```txt
- MST / Kruskal;
- riduzione 3-CNF-SAT → CLIQUE;
- chiusura transitiva / riflessiva-transitiva;
- criterio per dimostrare NP-completezza di un problema noto;
- matroide grafico.
```

> [!Important]
> Questo report non deve inventare soluzioni complete dove il PDF richiede disegni o dimostrazioni estese.
>
> Codex deve catalogare l'appello, aggiornare indici e pattern, e creare collegamenti verso metodi/teoria esistenti o da creare.

---

## 1. File da creare

Creare i seguenti file:

```txt
09_ingestion_reports/ingestion_report_exam_2025_11_10_part2.md
02_transcriptions/exams/exam_2025_11_10_part2.md
03_exercise_catalog/exercises/exam_2025_11_10_p2_e01.md
03_exercise_catalog/exercises/exam_2025_11_10_p2_e02.md
03_exercise_catalog/exercises/exam_2025_11_10_p2_e03.md
03_exercise_catalog/exercises/exam_2025_11_10_p2_e04.md
03_exercise_catalog/exercises/exam_2025_11_10_p2_e05.md
```

Se non esistono già, valutare la creazione o l'aggiornamento dei metodi:

```txt
04_methods/metodo_kruskal_mst.md
04_methods/metodo_riduzione_3sat_clique.md
04_methods/metodo_chiusura_transitiva_floyd_warshall.md
04_methods/metodo_dimostrare_np_completezza.md
04_methods/metodo_matroide_grafico.md
```

Se questi metodi esistono già con nomi simili, **non duplicarli**: aggiornare i file esistenti e collegare gli esercizi a quelli.

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
PROJECT_STATUS.md
TODO.md
```

Se esiste una pagina specifica per la Parte II, aggiornare anche:

```txt
06_exam_patterns/parte_ii_patterns.md
```

Se non esiste, Codex può crearla solo se coerente con la struttura già presente nella repo.

---

## 3. Trascrizione essenziale dell'appello

Creare `02_transcriptions/exams/exam_2025_11_10_part2.md` con frontmatter simile:

```md
---
type: exam_transcription
course: Analisi e Progettazione di Algoritmi
part: II
date: 2025-11-10
source_pdf: parteII-10nov25.pdf
status: transcribed
---

# Appello APA — Parte II — 10 novembre 2025

Fonte: [[parteII-10nov25.pdf]]

## Esercizi

1. Kruskal su grafo non orientato, connesso e pesato.
2. Riduzione polinomiale da 3-CNF-SAT a CLIQUE.
3. Ricorrenza per chiusura transitiva / riflessiva-transitiva.
4. Criterio sufficiente per stabilire che un problema specifico A è NP-completo.
5. Definizione e dimostrazione del matroide grafico.
```

---

## 4. Esercizio 1 — Kruskal / Minimum Spanning Tree

File:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p2_e01.md
```

### Trascrizione essenziale

Il PDF chiede di considerare un grafo non orientato, connesso e pesato:

```txt
V = {a, b, c, d, e}

Archi pesati:
(b,c) peso 4
(b,d) peso 6
(a,c) peso 1
(a,b) peso 2
(c,d) peso 7
(d,e) peso 3
(c,e) peso 5
```

Bisogna mostrare, nello schema dei quadrati `Q1, Q2, ..., Q7`, l'ordine con cui l'algoritmo di **Kruskal** aggiunge gli archi del Minimum Spanning Tree.

Regola richiesta dal testo:

```txt
Q1: primo arco aggiunto
Q2: primi due archi aggiunti
Q3: primi tre archi aggiunti
...
Qi: primi i archi aggiunti
...
fino a mostrare l'intero MST costruito
```

> [!Warning]
> Il testo dice che non verranno considerate risposte che non seguono lo schema dei quadrati.
> Nella knowledge base bisogna quindi annotare che questo esercizio valuta anche il formato di risposta, non solo il risultato.

### Catalogazione

```md
---
type: exercise
exam: 2025-11-10 Parte II
exercise_number: 1
topic:
  - MST
  - Kruskal
  - greedy
  - grafi pesati
difficulty: medium
status: cataloged
method:
  - [[metodo_kruskal_mst]]
---
```

### Pattern

Aggiornare i pattern con:

```txt
MST con Kruskal in formato operativo:
- ordinare gli archi per peso crescente;
- aggiungere un arco solo se non crea ciclo;
- mostrare lo stato progressivo della foresta/MST.
```

### Nota metodologica

Per questo esercizio conviene creare/aggiornare un metodo che includa:

```txt
1. Ordinamento archi per peso.
2. Inizializzazione foresta con tutti i vertici isolati.
3. Scansione degli archi in ordine crescente.
4. Aggiunta se collega componenti diverse.
5. Scarto se crea ciclo.
6. Stop quando sono stati aggiunti |V|-1 archi.
```

> [!Important]
> L'esercizio ha 7 quadrati perché il grafo ha 7 archi, ma l'MST finale contiene solo `|V|-1 = 4` archi.
> Codex deve evitare di scrivere che Kruskal aggiunge tutti e 7 gli archi: i quadrati successivi servono per mostrare che dopo il completamento dell'MST non vengono aggiunti altri archi.

---

## 5. Esercizio 2 — Riduzione 3-CNF-SAT → CLIQUE

File:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p2_e02.md
```

### Trascrizione essenziale

La formula data è:

$$
\varphi =
(\neg x_1 \lor x_2 \lor x_3)
\land
(x_1 \lor \neg x_2 \lor x_3)
\land
(x_1 \lor x_2 \lor \neg x_3)
$$

Il PDF chiede di disegnare il grafo ottenuto dalla riduzione polinomiale da **3-CNF-SAT / 3-SAT** a **CLIQUE**.

Indicazione di layout:

```txt
- vertici della prima clausola a sinistra;
- vertici della seconda clausola in alto;
- vertici della terza clausola a destra.
```

### Catalogazione

```md
---
type: exercise
exam: 2025-11-10 Parte II
exercise_number: 2
topic:
  - NP-completezza
  - riduzioni polinomiali
  - 3-CNF-SAT
  - CLIQUE
difficulty: medium
status: cataloged
method:
  - [[metodo_riduzione_3sat_clique]]
---
```

### Pattern

Aggiungere o aggiornare il pattern:

```txt
Riduzione 3-CNF-SAT → CLIQUE:
- creare un vertice per ogni letterale di ogni clausola;
- collegare solo vertici appartenenti a clausole diverse;
- non collegare letterali complementari;
- una clique di dimensione m corrisponde alla scelta di un letterale compatibile per ciascuna delle m clausole.
```

### Nota metodologica

Nel metodo dedicato, includere:

```txt
Input: formula 3-CNF con m clausole.
Output: grafo G' e intero k = m.

Costruzione:
1. Per ogni clausola C_i e per ogni letterale l_{i,j}, creare un vertice v_{i,j}.
2. Per ogni coppia di vertici di clausole diverse, aggiungere un arco se i letterali non sono complementari.
3. Cercare una clique di dimensione m.
```

> [!Warning]
> Il PDF richiede un disegno. Nel catalogo esercizi si può descrivere la costruzione e indicare quali archi sono esclusi, ma non bisogna inventare un'immagine se la repo non contiene un sistema standard per diagrammi.
>
> Se la repo usa Mermaid o Graphviz, Codex può aggiungere un blocco di diagramma solo se coerente con lo stile già adottato.

---

## 6. Esercizio 3 — Chiusura transitiva / riflessiva-transitiva

File:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p2_e03.md
```

### Trascrizione essenziale

Sia `G = (V,E)` un grafo.

Il PDF chiede di scrivere le equazioni di ricorrenza, caso base e passo ricorsivo, per stabilire per ogni coppia `(i,j)` di vertici se esiste un cammino da `i` a `j`.

In altri termini, bisogna scrivere le ricorrenze per il calcolo della:

```txt
chiusura transitiva / riflessiva-transitiva di G
```

usando coefficienti del tipo:

```txt
e^k_{ij}
```

### Catalogazione

```md
---
type: exercise
exam: 2025-11-10 Parte II
exercise_number: 3
topic:
  - chiusura transitiva
  - Floyd-Warshall
  - programmazione dinamica su grafi
  - ricorrenze
difficulty: medium
status: cataloged
method:
  - [[metodo_chiusura_transitiva_floyd_warshall]]
---
```

### Pattern

Questo esercizio è molto simile all'esercizio 3 dell'appello Parte II del 3 luglio 2025.

Aggiornare i pattern con:

```txt
Ricorrenza standard per chiusura transitiva:
- coefficiente e^k_{ij};
- k indica l'insieme di vertici intermedi ammessi;
- caso base da archi diretti e/o riflessività;
- passo ricorsivo con alternativa: non usare k oppure usare k.
```

### Nota metodologica

Nel metodo, includere la forma standard:

```md
Significato possibile:

$e^k_{ij} = 1$ se esiste un cammino da $i$ a $j$ i cui vertici intermedi appartengono all'insieme $\{1,\dots,k\}$.

Caso base:

$$
e^0_{ij} =
\begin{cases}
1 & \text{se } i=j \text{ oppure } (i,j)\in E,\\
0 & \text{altrimenti.}
\end{cases}
$$

Passo ricorsivo:

$$
e^k_{ij} =
e^{k-1}_{ij}
\lor
(e^{k-1}_{ik} \land e^{k-1}_{kj})
$$
```

> [!Warning]
> Verificare se nella repo si è scelto di trattare la chiusura come transitiva pura o riflessiva-transitiva.
> Il testo dell'appello cita entrambe le formulazioni; per sicurezza annotare la variante usata.

---

## 7. Esercizio 4 — Criterio per dimostrare NP-completezza

File:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p2_e04.md
```

### Trascrizione essenziale

Il PDF chiede:

```txt
Considerando un problema specifico A, tra quelli visti a lezione,
cosa è sufficiente mostrare relativamente ad A per stabilire che A è NP-completo?
```

Nota:

```txt
Non è richiesta alcuna dimostrazione.
```

### Catalogazione

```md
---
type: exercise
exam: 2025-11-10 Parte II
exercise_number: 4
topic:
  - NP-completezza
  - riduzioni polinomiali
  - teoria della complessità
difficulty: medium
status: cataloged
method:
  - [[metodo_dimostrare_np_completezza]]
---
```

### Pattern

Questo esercizio ricorre anche nell'appello Parte II del 9 giugno 2025.

Aggiornare i pattern con:

```txt
Domanda teorica breve su NP-completezza:
- mostrare che A appartiene a NP;
- scegliere un problema B già noto NP-completo;
- costruire una riduzione polinomiale B <=p A;
- concludere che A è NP-hard e quindi NP-completo.
```

### Nota metodologica

La risposta attesa deve essere breve e precisa:

```txt
Per dimostrare che A è NP-completo è sufficiente:
1. mostrare che A ∈ NP;
2. mostrare che A è NP-hard riducendo polinomialmente ad A un problema B già noto NP-completo.
```

> [!Important]
> Attenzione alla direzione della riduzione:
>
> `B <=p A`, dove `B` è noto NP-completo.
>
> Non scrivere `A <=p B`, perché questa direzione non basta per dimostrare che A è NP-hard.

---

## 8. Esercizio 5 — Matroide grafico

File:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p2_e05.md
```

### Trascrizione essenziale

Sia `G = (V,E)` un grafo non orientato.

Il PDF chiede di:

```txt
1. definire il matroide grafico;
2. dimostrare che è effettivamente un matroide.
```

Nota del testo:

```txt
Non occorre dimostrare che il numero di alberi in una foresta è pari alla differenza tra il numero di vertici e il numero di archi.
```

La risposta va data sul foglio protocollo.

### Catalogazione

```md
---
type: exercise
exam: 2025-11-10 Parte II
exercise_number: 5
topic:
  - matroidi
  - matroide grafico
  - greedy
  - indipendenza
difficulty: hard
status: cataloged
method:
  - [[metodo_matroide_grafico]]
---
```

### Pattern

Questo esercizio è sostanzialmente lo stesso dell'esercizio 5 dell'appello Parte II del 9 giugno 2025.

Aggiornare i pattern con:

```txt
Matroide grafico:
- insieme base E = archi del grafo;
- famiglia indipendente F = sottoinsiemi di archi aciclici;
- dimostrare ereditarietà;
- dimostrare proprietà di scambio;
- collegamento a foreste e MST.
```

### Nota metodologica

Nel metodo, includere la struttura:

```txt
Dato G=(V,E), il matroide grafico è M(G)=(E,F), dove:
F = { A ⊆ E : (V,A) è una foresta }.

Assiomi:
1. ∅ ∈ F.
2. Se A ∈ F e B ⊆ A, allora B ∈ F.
3. Se A,B ∈ F e |A| < |B|, allora esiste e ∈ B\A tale che A ∪ {e} ∈ F.
```

Per la proprietà di scambio, indicare che si usa il fatto che una foresta con più archi ha meno componenti connesse, quindi deve esistere un arco di `B` che collega due componenti distinte di `A`, senza creare ciclo.

> [!Warning]
> Non estendere troppo la dimostrazione nel catalogo esercizi: la dimostrazione completa può stare in `05_theory/` o in un metodo dedicato.
```

---

## 9. Pattern da aggiornare

Aggiornare `06_exam_patterns/recurring_exercise_types.md` con una sezione o sottosezione per la Parte II:

```md
## Parte II — Pattern ricorrenti

### MST / Kruskal

Ricorre in appelli Parte II come esercizio operativo su grafi pesati.

### Riduzioni NP-complete

Varianti osservate:
- CLIQUE → VERTEX-COVER;
- 3-CNF-SAT → CLIQUE.

### Chiusura transitiva

Richiesta come ricorrenza formale con coefficiente $e^k_{ij}$.

### NP-completezza teorica

Domanda breve sul criterio sufficiente:
- appartenenza a NP;
- riduzione da problema noto NP-completo.

### Matroidi

Richiesta frequente:
- GREEDY-MAX e teorema di Rado;
- matroide grafico e dimostrazione degli assiomi.
```

Aggiornare `06_exam_patterns/variations_by_appeal.md` aggiungendo:

```md
## 2025-11-10 — Parte II

| Esercizio | Tema | Pattern |
|---|---|---|
| 1 | Kruskal / MST | Algoritmo greedy operativo |
| 2 | 3-CNF-SAT → CLIQUE | Riduzione polinomiale con costruzione grafica |
| 3 | Chiusura transitiva | Ricorrenza Floyd-Warshall booleana |
| 4 | NP-completezza | Criterio sufficiente |
| 5 | Matroide grafico | Definizione e dimostrazione |
```

Aggiornare `06_exam_patterns/high_yield_topics.md` segnalando come ad alta resa:

```txt
- Kruskal e MST;
- riduzioni standard tra problemi NP-completi;
- chiusura transitiva con ricorrenze;
- criterio per NP-completezza;
- matroide grafico.
```

---

## 10. Differenze rispetto agli appelli Parte II già analizzati

Rispetto a `parteII-03lug25.pdf`:

```txt
- L'esercizio 1 non è Dijkstra ma Kruskal/MST.
- L'esercizio 2 non è CLIQUE → VERTEX-COVER ma 3-CNF-SAT → CLIQUE.
- L'esercizio 3 è ancora chiusura transitiva.
- L'esercizio 4 è simile alla domanda teorica su NP-completezza vista il 9 giugno.
- L'esercizio 5 coincide come tema con il matroide grafico del 9 giugno.
```

Rispetto a `parteII-09giu25.pdf`:

```txt
- L'esercizio 1 passa da Dijkstra a Kruskal.
- L'esercizio 2 passa da CLIQUE → VERTEX-COVER a 3-CNF-SAT → CLIQUE.
- Non compare GREEDY-MAX/Rado.
- Ricompaiono NP-completezza e matroide grafico.
```

---

## 11. Note metodologiche importanti

### 11.1 Separare esercizi operativi e teoria

Questo appello contiene sia esercizi operativi sia domande teoriche.

Classificazione consigliata:

```txt
Operativi:
- E1 Kruskal;
- E2 riduzione 3-SAT → CLIQUE;
- E3 ricorrenza chiusura transitiva.

Teorici:
- E4 criterio NP-completezza;
- E5 matroide grafico.
```

### 11.2 Non duplicare metodi già presenti

Prima di creare nuovi metodi, cercare:

```bash
find 04_methods -iname "*kruskal*"
find 04_methods -iname "*mst*"
find 04_methods -iname "*clique*"
find 04_methods -iname "*sat*"
find 04_methods -iname "*np*"
find 04_methods -iname "*matroide*"
find 04_methods -iname "*transitiva*"
```

Se esistono già file equivalenti, aggiornare quelli.

### 11.3 Aggiornare i link Obsidian

Ogni esercizio deve puntare ai metodi rilevanti tramite link interni:

```md
[[metodo_kruskal_mst]]
[[metodo_riduzione_3sat_clique]]
[[metodo_chiusura_transitiva_floyd_warshall]]
[[metodo_dimostrare_np_completezza]]
[[metodo_matroide_grafico]]
```

---

## 12. Aggiornare PROJECT_STATUS.md

Aggiungere una voce tipo:

```md
## Stato ingestion appelli Parte II

- [x] 2025-07-03 Parte II — report creato
- [x] 2025-06-09 Parte II — report creato
- [x] 2025-11-10 Parte II — report creato
```

Se Codex applica effettivamente questo piano, segnare:

```md
- [x] 2025-11-10 Parte II — applicato alla KB
```

Aggiornare anche la sintesi dei pattern Parte II:

```txt
La Parte II mostra ricorrenza forte su:
- Dijkstra/Kruskal e algoritmi su grafi;
- riduzioni NP-complete;
- chiusura transitiva;
- definizioni e dimostrazioni su P/NP/NP-completi;
- matroidi e greedy.
```

---

## 13. Aggiornare TODO.md

Aggiungere o aggiornare task:

```md
## TODO — Parte II

- [ ] Verificare deduplicazione tra esercizi su chiusura transitiva.
- [ ] Consolidare metodo per criterio di NP-completezza.
- [ ] Consolidare metodo per matroide grafico.
- [ ] Aggiungere metodo specifico per riduzione 3-CNF-SAT → CLIQUE.
- [ ] Aggiungere metodo specifico per Kruskal/MST se assente.
- [ ] Verificare link negli indici dopo ingestion dell'appello 2025-11-10 Parte II.
```

---

## 14. Commit consigliato

Commit message consigliato:

```txt
ingest APA 2025-11-10 part II exam
```

Oppure, se il commit riguarda solo il report:

```txt
add ingestion report for APA 2025-11-10 part II
```

---

## 15. Stato atteso finale

Dopo l'applicazione del piano, la repo deve contenere:

```txt
- trascrizione essenziale dell'appello;
- 5 esercizi catalogati;
- ingestion report salvato;
- indici aggiornati;
- pattern Parte II aggiornati;
- collegamenti ai metodi teorici/operativi;
- TODO e PROJECT_STATUS aggiornati.
```

La knowledge base deve mostrare chiaramente che l'appello del **10 novembre 2025 Parte II** introduce/rafforza:

```txt
- Kruskal;
- riduzione 3-SAT → CLIQUE;
- chiusura transitiva;
- criterio standard per NP-completezza;
- matroide grafico.
```

---

## 16. Nota finale per Codex

> [!Important]
> Non inventare soluzioni grafiche complete se non sono già supportate dalla repo.
>
> Per gli esercizi che richiedono disegni, descrivere la costruzione in modo preciso e, se la repo usa diagrammi testuali, aggiungere un diagramma coerente con lo stile esistente.
>
> Evitare duplicazioni: questo appello condivide pattern con gli appelli Parte II del 3 luglio 2025 e del 9 giugno 2025.
