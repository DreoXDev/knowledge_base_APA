# Ingestion Report — parteI-03lug25

> [!Info]
> Report finale per l'ingestione dell'appello `parteI-03lug25.pdf` nella knowledge base Obsidian `knowledge_base_APA`.
>
> Stato report: `ready_for_codex`
>
> Obiettivo: catalogare la Parte I dell'appello del 3 luglio 2025, aggiornare trascrizioni, catalogo esercizi, pattern ricorrenti, metodi e teoria minima.

---

## 1. Metadata

- Source ID: `exam_2025_07_03_part1`
- File sorgente consigliato nella repo: `01_sources/exams_raw/parteI-03lug25.pdf`
- File PDF analizzato: `parteI-03lug25.pdf`
- Tipo fonte: `appello_raw`
- Corso: `Analisi e Progettazione di Algoritmi`
- Data appello: `2025-07-03`
- Parte: `Parte I`
- Numero pagine: `2`
- Stato fonte: `report_creato`
- Stato report: `ready_for_codex`
- Priorità: `alta`
- Nome report consigliato: `09_ingestion_reports/ingestion_report_exam_2025_07_03_part1.md`

---

## 2. Nota di audit repo prima dell'applicazione

Prima di applicare questo report, Codex deve verificare che il report precedente sull'appello `2026-01-12` sia stato applicato in modo coerente.

Dalla verifica della repo pubblica risultano già presenti:

```txt
02_transcriptions/exams/exam_2026_01_12.md
03_exercise_catalog/exercises/exam_2026_01_12_e01.md
03_exercise_catalog/exercises/exam_2026_01_12_e02.md
03_exercise_catalog/exercises/exam_2026_01_12_e03.md
03_exercise_catalog/exercises/exam_2026_01_12_e04.md
03_exercise_catalog/exercises/exam_2026_01_12_e05.md
03_exercise_catalog/exercises/exam_2026_01_12_e06.md
03_exercise_catalog/exercises/exam_2026_01_12_bonus_matroidi.md
04_methods/metodo_programmazione_dinamica_zaino_01.md
04_methods/metodo_dp_cammini_con_parita.md
04_methods/metodo_kruskal_mst.md
04_methods/metodo_riduzione_clique_vertex_cover.md
04_methods/metodo_dimostrare_np_completezza.md
05_theory/programmazione_dinamica.md
05_theory/zaino_01.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/kruskal.md
05_theory/minimum_spanning_tree.md
05_theory/np_completezza.md
05_theory/clique.md
05_theory/vertex_cover.md
05_theory/matroidi.md
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/recurring_theory_questions.md
06_exam_patterns/high_yield_topics.md
```

> [!Warning]
> Nella root pubblica della repo non è chiaramente visibile `09_ingestion_reports/`.
> Se manca, crearla ora e salvarci sia il report precedente sia questo report.
>
> Inoltre `TODO.md` e `PROJECT_STATUS.md` risultano ancora abbastanza generici: aggiornarli con i prossimi step specifici dei due appelli catalogati.

---

## 3. Sintesi contenuto

L'appello contiene solo la Parte I e presenta due esercizi, entrambi di programmazione dinamica:

```txt
Parte I — 3 luglio 2025

Esercizio 1:
- LCS tra due sequenze X e Y con vincolo di ingombro totale al più W.
- Richiede coefficienti, caso base, ricorrenza, coefficiente ottimo, algoritmo bottom-up e ricostruzione della soluzione.

Esercizio 2:
- Grafo con archi colorati R/N/B.
- Stabilire per ogni coppia di vertici se esiste un cammino con esattamente 2 archi rossi e 2 archi blu.
- Richiede coefficienti, caso base, ricorrenza e soluzione finale.
```

Pattern forti:

- programmazione dinamica tabellare;
- definizione formale dei coefficienti;
- casi base e passo ricorsivo;
- ricostruzione della soluzione;
- DP su sequenze con vincolo aggiuntivo;
- DP booleana su grafi con stato esteso da conteggi.

---

## 4. Pagine / sezioni analizzate

| Pagina PDF | Contenuto |
|---|---|
| 1 | Parte I, Esercizio 1: LCS con vincolo di ingombro massimo $W$ |
| 2 | Parte I, Esercizio 2: cammini in grafo con esattamente 2 archi rossi e 2 archi blu |

---

## 5. Argomenti individuati

```md
- #topic/programmazione-dinamica
- #topic/lcs
- #topic/sottosequenze
- #topic/vincoli-di-budget
- #topic/ricorrenze-dp
- #topic/ricostruzione-soluzione
- #topic/grafi
- #topic/grafi-colorati
- #topic/cammini
- #topic/dp-booleana
- #topic/stato-esteso
```

---

## 6. Trascrizione appello da creare

Codex deve creare:

```txt
02_transcriptions/exams/exam_2025_07_03_part1.md
```

Contenuto consigliato:

```md
---
type: exam_transcription
source: 01_sources/exams_raw/parteI-03lug25.pdf
exam_date: 2025-07-03
part: Parte I
status: transcribed
tags:
  - apa
  - appello
  - exam/raw
  - parte-i
---

# Appello 2025-07-03 — Parte I

> [!Info]
> Fonte originale: `01_sources/exams_raw/parteI-03lug25.pdf`

## Struttura dell'appello

| ID | Parte | Argomento principale | Punti | Stato |
|---|---|---|---:|---|
| [[exam_2025_07_03_p1_e01]] | Parte I | DP, LCS con vincolo di ingombro | 31 | cataloged |
| [[exam_2025_07_03_p1_e02]] | Parte I | DP su grafi colorati, cammini con conteggi esatti | 31 | cataloged |

## Esercizio 1

Sia $W$ un numero intero non negativo. Siano:

$$
X = \langle x_1,\dots,x_m\rangle
$$

e

$$
Y = \langle y_1,\dots,y_n\rangle
$$

due sequenze su un alfabeto $S$ di simboli. A ogni simbolo è associato un numero intero non negativo detto ingombro, ricavabile tramite una funzione nota e calcolabile:

$$
w:S \to \mathbb{N}
$$

Si vuole determinare, mediante programmazione dinamica, una più lunga sottosequenza comune di $X$ e $Y$ con ingombro complessivo minore o uguale a $W$.

Richieste:

1. definire i coefficienti, ognuno contenente la lunghezza di un'opportuna LCS in un sottoproblema;
2. scrivere il caso base;
3. scrivere il passo ricorsivo;
4. specificare il coefficiente che fornisce il valore ottimo;
5. scrivere l'algoritmo bottom-up;
6. scrivere l'algoritmo ricorsivo che ricostruisce/stampa la soluzione del generico sottoproblema.

## Esercizio 2

Dato un grafo $(V,E,col)$ senza cappi, in cui a ogni arco è associato un colore tramite:

$$
col:E \to C
$$

dove $C=\{R,N,B\}$ rappresenta rosso, nero e blu.

Mediante programmazione dinamica, si vuole stabilire per ogni coppia di vertici $(i,j)$ se esiste un cammino da $i$ a $j$ nel quale vi sono esattamente 2 archi rossi ed esattamente 2 archi blu.

Richieste:

1. definire i coefficienti;
2. scrivere il caso base;
3. scrivere il passo ricorsivo;
4. indicare qual è la soluzione del problema.
```

---

## 7. Esercizi da creare

### 7.1 `exam_2025_07_03_p1_e01`

- File da creare: `03_exercise_catalog/exercises/exam_2025_07_03_p1_e01.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/parteI-03lug25.pdf`
- Pagina: `1`
- Parte: `Parte I`
- Punti: `31`
- Titolo: `DP per LCS con vincolo di ingombro`
- Argomento principale: `programmazione dinamica`
- Argomenti secondari:
  - `LCS`
  - `sottosequenze comuni`
  - `vincolo di budget`
  - `ricorrenze DP`
  - `ricostruzione soluzione`
- Tipo richiesta:
  - definire coefficienti;
  - caso base;
  - passo ricorsivo;
  - coefficiente soluzione;
  - algoritmo bottom-up;
  - algoritmo ricorsivo di ricostruzione.
- Metodo probabile:
  - `[[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]`
  - `[[metodo_ricostruzione_soluzione_dp]]`
- Teoria collegata:
  - `[[programmazione_dinamica]]`
  - `[[lcs]]`
  - `[[sottosequenze_comuni]]`
- Pattern sospetto:
  - `DP su sequenze con stato esteso da budget`
- Difficoltà stimata: `alta`
- Priorità: `alta`
- Note:
  - È una variante della LCS classica con una dimensione aggiuntiva di capacità/ingombro.
  - Stato probabile: $c_{i,j,k}$ = lunghezza massima di una sottosequenza comune tra $X[1..i]$ e $Y[1..j]$ con ingombro al più $k$.
  - La ricostruzione richiede di distinguere se il simbolo comune viene scelto oppure se si eredita da uno dei sottoproblemi.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/parteI-03lug25.pdf
exam_date: 2025-07-03
part: Parte I
exercise_number: 1
points: 31
status: cataloged
difficulty: alta
tags:
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/sottosequenze
  - topic/vincoli-di-budget
  - topic/ricostruzione-soluzione
  - status/cataloged
---

# Exam 2025-07-03 — Parte I — Esercizio 1

## Testo essenziale

Determinare una più lunga sottosequenza comune tra due sequenze $X$ e $Y$, con vincolo di ingombro complessivo al più $W$.

Ogni simbolo $s \in S$ ha ingombro intero non negativo $w(s)$.

## Richieste

1. Definire i coefficienti.
2. Scrivere il caso base.
3. Scrivere il passo ricorsivo.
4. Specificare il coefficiente della soluzione ottima.
5. Scrivere algoritmo bottom-up.
6. Scrivere algoritmo ricorsivo di ricostruzione.

## Classificazione

- Argomento: [[programmazione_dinamica]]
- Teoria: [[lcs]]
- Metodo probabile: [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]
- Pattern: [[dp_su_sequenze_con_budget]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato

> [!Warning]
> Soluzione non ancora inserita. Verificare se il docente preferisce indicare il vincolo come "al più $k$" o "esattamente $k$" nei coefficienti.
```

---

### 7.2 `exam_2025_07_03_p1_e02`

- File da creare: `03_exercise_catalog/exercises/exam_2025_07_03_p1_e02.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/parteI-03lug25.pdf`
- Pagina: `2`
- Parte: `Parte I`
- Punti: `31`
- Titolo: `DP su grafi colorati con esattamente 2 archi rossi e 2 archi blu`
- Argomento principale: `programmazione dinamica su grafi`
- Argomenti secondari:
  - `grafi`
  - `grafi colorati`
  - `cammini`
  - `conteggi esatti`
  - `dp booleana`
  - `stato esteso`
- Tipo richiesta:
  - definire coefficienti;
  - caso base;
  - passo ricorsivo;
  - indicare soluzione finale.
- Metodo probabile:
  - `[[metodo_dp_cammini_colori_conteggi]]`
  - aggiornare anche `[[metodo_dp_cammini_con_parita]]` per collegare le due varianti di DP booleana su grafi.
- Teoria collegata:
  - `[[grafi]]`
  - `[[grafi_colorati]]`
  - `[[cammini]]`
  - `[[programmazione_dinamica_su_grafi]]`
- Pattern sospetto:
  - `DP booleana su grafi con vincoli sui colori degli archi`
- Difficoltà stimata: `alta`
- Priorità: `alta`
- Note:
  - È molto simile, come struttura d'esame, all'appello `2026-01-12` Parte I Esercizio 2, ma la proprietà richiesta cambia:
    - 2026: cammino con numero pari di archi;
    - 2025-07-03: cammino con esattamente 2 rossi e 2 blu.
  - Stato probabile: coefficiente booleano con indici per vertici, limite sugli intermedi e conteggi di archi rossi/blu.
  - Il colore nero non ha conteggio vincolato, ma può comparire nei cammini.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/parteI-03lug25.pdf
exam_date: 2025-07-03
part: Parte I
exercise_number: 2
points: 31
status: cataloged
difficulty: alta
tags:
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/grafi-colorati
  - topic/cammini
  - topic/dp-booleana
  - topic/stato-esteso
  - status/cataloged
---

# Exam 2025-07-03 — Parte I — Esercizio 2

## Testo essenziale

Dato un grafo $(V,E,col)$ senza cappi, con archi colorati rosso, nero o blu, stabilire per ogni coppia di vertici $(i,j)$ se esiste un cammino da $i$ a $j$ con esattamente 2 archi rossi ed esattamente 2 archi blu.

## Richieste

1. Definire i coefficienti.
2. Scrivere il caso base.
3. Scrivere il passo ricorsivo.
4. Indicare la soluzione.

## Classificazione

- Argomento: [[programmazione_dinamica_su_grafi]]
- Teoria: [[grafi_colorati]]
- Metodo probabile: [[metodo_dp_cammini_colori_conteggi]]
- Pattern: [[dp_booleana_su_grafi_con_conteggi_colori]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato

> [!Warning]
> Verificare se il corso imposta la ricorrenza come variante di Floyd-Warshall con vertici intermedi oppure con altra notazione.
```

---

## 8. Metodi da creare o aggiornare

### 8.1 Nuovi metodi da creare

Creare se assenti:

```txt
04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md
04_methods/metodo_dp_cammini_colori_conteggi.md
```

### 8.2 Metodi esistenti da aggiornare

Aggiornare:

```txt
04_methods/dynamic_programming.md
04_methods/metodo_ricostruzione_soluzione_dp.md
04_methods/metodo_dp_cammini_con_parita.md
```

### 8.3 Contenuto minimo per `metodo_programmazione_dinamica_lcs_vincolo_ingombro.md`

```md
---
type: method
status: scaffold
tags:
  - method
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/vincoli-di-budget
---

# Metodo — LCS con vincolo di ingombro

## Quando si usa

Quando si cerca una sottosequenza comune massima tra due sequenze, ma la soluzione deve rispettare un vincolo di costo/peso/ingombro.

## Stato tipico

$$
c_{i,j,k}
$$

dove $i$ e $j$ indicano i prefissi delle due sequenze e $k$ indica il budget massimo disponibile.

## Esercizi collegati

- [[exam_2025_07_03_p1_e01]]

## Teoria necessaria

- [[programmazione_dinamica]]
- [[lcs]]

## Errori comuni

- Dimenticare la dimensione del budget.
- Usare $w(x_i)$ anche quando $x_i \ne y_j$.
- Ricostruire la sequenza senza controllare se il simbolo è stato effettivamente scelto.

> [!Warning]
> Metodo da completare durante la fase di soluzione.
```

### 8.4 Contenuto minimo per `metodo_dp_cammini_colori_conteggi.md`

```md
---
type: method
status: scaffold
tags:
  - method
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/grafi-colorati
  - topic/dp-booleana
---

# Metodo — DP su cammini con conteggi di colori

## Quando si usa

Quando bisogna stabilire l'esistenza di un cammino tra coppie di vertici che rispetta vincoli sul numero di archi di certi colori.

## Stato tipico

Un possibile stato è:

$$
c_{h,i,j,r,b}
$$

dove:
- $h$ limita i vertici intermedi utilizzabili;
- $i,j$ sono estremi del cammino;
- $r$ è il numero di archi rossi usati;
- $b$ è il numero di archi blu usati.

## Esercizi collegati

- [[exam_2025_07_03_p1_e02]]
- [[exam_2026_01_12_e02]]

## Teoria necessaria

- [[grafi]]
- [[grafi_colorati]]
- [[programmazione_dinamica_su_grafi]]

## Errori comuni

- Non contare correttamente gli archi rossi e blu nei casi base.
- Confondere cammino con arco diretto.
- Dimenticare che gli archi neri non aumentano né il conteggio rosso né il conteggio blu.
- Non considerare la composizione di due cammini passando per un vertice intermedio.

> [!Warning]
> Verificare la notazione specifica del corso prima di trasformarlo in metodo definitivo.
```

---

## 9. Teoria da creare o aggiornare

Creare se assenti:

```txt
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/grafi_colorati.md
```

Aggiornare:

```txt
05_theory/programmazione_dinamica.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/grafi.md
```

> [!Important]
> La teoria deve restare minima e collegata agli esercizi.
> Non creare una dispensa completa su LCS o grafi colorati, ma solo definizioni e schemi usati negli appelli.

---

## 10. Pattern d'esame da aggiornare

Aggiornare:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
```

Creare se assenti:

```txt
06_exam_patterns/dp_su_sequenze_con_budget.md
06_exam_patterns/dp_booleana_su_grafi_con_conteggi_colori.md
```

### 10.1 Pattern esercizi ricorrenti

Aggiungere a `06_exam_patterns/recurring_exercise_types.md`:

```md
## DP — Definizione coefficienti, casi base e ricorrenza

- Esercizi collegati:
  - [[exam_2026_01_12_e01]]
  - [[exam_2026_01_12_e02]]
  - [[exam_2026_01_12_e05]]
  - [[exam_2025_07_03_p1_e01]]
  - [[exam_2025_07_03_p1_e02]]
- Frequenza osservata: `2 appelli`
- Priorità: `altissima`
- Descrizione:
  - Il compito chiede spesso di impostare formalmente una DP: coefficienti, casi base, passo ricorsivo, soluzione finale e talvolta ricostruzione.
  - Gli esercizi della Parte I sembrano fortemente centrati su questa struttura.

## DP su sequenze con vincolo aggiuntivo

- Esercizi collegati:
  - [[exam_2025_07_03_p1_e01]]
- Frequenza osservata: `1 appello`
- Priorità: `alta`
- Varianti osservate:
  - LCS con vincolo di ingombro massimo.

## DP booleana su grafi con proprietà del cammino

- Esercizi collegati:
  - [[exam_2026_01_12_e02]]
  - [[exam_2025_07_03_p1_e02]]
- Frequenza osservata: `2 appelli`
- Priorità: `altissima`
- Varianti osservate:
  - esistenza di cammino con numero pari di archi;
  - esistenza di cammino con esattamente 2 archi rossi e 2 archi blu.
```

### 10.2 Aggiornare `variations_by_appeal.md`

```md
## Programmazione dinamica su grafi

| Appello | Esercizio | Variante |
|---|---|---|
| 2026-01-12 | [[exam_2026_01_12_e02]] | cammino con numero pari di archi |
| 2025-07-03 Parte I | [[exam_2025_07_03_p1_e02]] | cammino con esattamente 2 archi rossi e 2 archi blu |

## Programmazione dinamica su sequenze

| Appello | Esercizio | Variante |
|---|---|---|
| 2025-07-03 Parte I | [[exam_2025_07_03_p1_e01]] | LCS con vincolo di ingombro |
```

### 10.3 Aggiornare `high_yield_topics.md`

Aggiungere o aumentare priorità:

```md
## Altissima resa

- Programmazione dinamica:
  - coefficienti;
  - caso base;
  - passo ricorsivo;
  - coefficiente soluzione;
  - bottom-up;
  - ricostruzione.
- DP booleana su grafi:
  - proprietà dei cammini;
  - stato esteso con informazioni aggiuntive.
```

---

## 11. Indici da aggiornare

Aggiornare:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

### 11.1 `index_by_exam.md`

Aggiungere:

```md
## 2025-07-03 — Parte I

| Esercizio | Parte | Argomento | Punti | Difficoltà | Stato |
|---|---|---|---:|---|---|
| [[exam_2025_07_03_p1_e01]] | Parte I | DP LCS con vincolo di ingombro | 31 | alta | cataloged |
| [[exam_2025_07_03_p1_e02]] | Parte I | DP cammini con conteggi esatti di colori | 31 | alta | cataloged |
```

> [!Warning]
> Nell'indice attuale le righe del primo appello risultano senza tabella Markdown completa.
> Se possibile, sistemare anche la sezione `2026-01-12` usando una tabella Markdown vera con separatore `|---|`.

### 11.2 `index_by_topic.md`

Aggiungere:

```md
## Programmazione dinamica

- [[exam_2025_07_03_p1_e01]] — LCS con vincolo di ingombro
- [[exam_2025_07_03_p1_e02]] — cammini con conteggi esatti di colori

## LCS / Sottosequenze comuni

- [[exam_2025_07_03_p1_e01]]

## Grafi

- [[exam_2025_07_03_p1_e02]]

## DP booleana su grafi

- [[exam_2025_07_03_p1_e02]]
```

### 11.3 `index_by_difficulty.md`

Aggiungere:

```md
## Alta

- [[exam_2025_07_03_p1_e01]]
- [[exam_2025_07_03_p1_e02]]
```

---

## 12. Esempi svolti da creare

Non creare ancora soluzioni complete, salvo scaffold futuro.

Possibili file futuri:

```txt
07_solved_examples/solved_exam_2025_07_03_p1_e01_lcs_budget.md
07_solved_examples/solved_exam_2025_07_03_p1_e02_cammini_colori.md
```

Priorità consigliata:

1. `exam_2025_07_03_p1_e01` — molto utile perché introduce LCS con budget;
2. `exam_2025_07_03_p1_e02` — utile insieme alla variante 2026 sui cammini pari;
3. creare metodo comune per "DP booleana su grafi con stato esteso".

---

## 13. Dubbi e parti da verificare

> [!Warning]
> Il PDF è leggibile tramite testo estratto, ma resta necessario verificare la notazione matematica definitiva usata dal docente.

Punti da verificare:

- In `exam_2025_07_03_p1_e01`, il testo dice che i coefficienti contengono la lunghezza di un'opportuna LCS. Verificare se conviene usare $c_{i,j,k}$ con budget "al più $k$" oppure una variante con budget "esattamente $k$".
- In `exam_2025_07_03_p1_e02`, verificare se il docente vuole una ricorrenza tipo Floyd-Warshall con vertici intermedi o una diversa DP sui cammini.
- In `exam_2025_07_03_p1_e02`, verificare come trattare il cammino vuoto nei casi base, soprattutto per $i=j$ e conteggi $(0,0)$.
- Nel caso base del grafo colorato, verificare come registrare archi neri: conteggi rosso/blu pari a $(0,0)$.

---

## 14. Istruzioni operative per Codex

Codex deve:

1. Verificare o creare:

```txt
09_ingestion_reports/
```

2. Salvare questo report come:

```txt
09_ingestion_reports/ingestion_report_exam_2025_07_03_part1.md
```

3. Verificare che il PDF sia presente o copiarlo in:

```txt
01_sources/exams_raw/parteI-03lug25.pdf
```

4. Creare la trascrizione:

```txt
02_transcriptions/exams/exam_2025_07_03_part1.md
```

5. Creare i file esercizio:

```txt
03_exercise_catalog/exercises/exam_2025_07_03_p1_e01.md
03_exercise_catalog/exercises/exam_2025_07_03_p1_e02.md
```

6. Aggiornare gli indici:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

7. Aggiornare pattern:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
```

8. Creare o aggiornare metodi:

```txt
04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md
04_methods/metodo_dp_cammini_colori_conteggi.md
04_methods/dynamic_programming.md
04_methods/metodo_ricostruzione_soluzione_dp.md
04_methods/metodo_dp_cammini_con_parita.md
```

9. Creare o aggiornare teoria minima:

```txt
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/grafi_colorati.md
05_theory/programmazione_dinamica.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/grafi.md
```

10. Aggiornare `PROJECT_STATUS.md`:

```md
## Stato aggiornato

- Appello analizzato: `01_sources/exams_raw/parteI-03lug25.pdf`
- Data: `2025-07-03`
- Parte: `Parte I`
- Report creato: `09_ingestion_reports/ingestion_report_exam_2025_07_03_part1.md`
- Trascrizione creata: `02_transcriptions/exams/exam_2025_07_03_part1.md`
- Esercizi catalogati: `2`
- Stato: `secondo appello catalogato`
```

11. Aggiornare `TODO.md`:

```md
## Prossimi step

- [ ] Verificare manualmente trascrizione dell'appello `2025-07-03 Parte I`
- [ ] Risolvere `exam_2025_07_03_p1_e01` LCS con vincolo di ingombro
- [ ] Risolvere `exam_2025_07_03_p1_e02` cammini con conteggi di colori
- [ ] Consolidare metodo comune per DP booleana su grafi
- [ ] Aggiornare mappa pattern dopo almeno 3 appelli
- [ ] Analizzare prossimo PDF in `01_sources/exams_raw/`
```

---

## 15. Definition of Done

Questo ingestion report è considerato applicato quando Codex ha:

- [ ] salvato il report nella repo;
- [ ] verificato presenza di `09_ingestion_reports/`;
- [ ] creato la trascrizione essenziale dell'appello;
- [ ] creato i due file esercizio;
- [ ] aggiornato indici per esame, topic e difficoltà;
- [ ] aggiornato pattern ricorrenti e variazioni per appello;
- [ ] creato scaffold dei due nuovi metodi;
- [ ] creato teoria minima per LCS, sottosequenze comuni e grafi colorati;
- [ ] aggiornato `PROJECT_STATUS.md`;
- [ ] aggiornato `TODO.md`;
- [ ] mantenuto `[!Warning]` sulle parti da verificare;
- [ ] non creato soluzioni complete non richieste.

---

## 16. Prossima azione consigliata

Dopo applicazione del report da parte di Codex:

1. fare commit della repo;
2. controllare i link Obsidian;
3. confrontare `exam_2025_07_03_p1_e02` con `exam_2026_01_12_e02`;
4. creare una nota metodo unica per le DP su grafi con stato esteso;
5. procedere con il prossimo appello raw.
