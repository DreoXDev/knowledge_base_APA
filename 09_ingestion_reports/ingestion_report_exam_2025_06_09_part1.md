# Ingestion Report — parteI-09giu25

> [!Info]
> Report finale per l'ingestione dell'appello `parteI-09giu25.pdf` nella knowledge base Obsidian `knowledge_base_APA`.
>
> Stato report: `ready_for_codex`
>
> Obiettivo: catalogare la Parte I dell'appello del 9 giugno 2025, aggiornando trascrizioni, catalogo esercizi, pattern ricorrenti, metodi e teoria minima.

---

## 1. Metadata

- Source ID: `exam_2025_06_09_part1`
- File sorgente consigliato nella repo: `01_sources/exams_raw/parteI-09giu25.pdf`
- File PDF analizzato: `parteI-09giu25.pdf`
- Tipo fonte: `appello_raw`
- Corso: `Analisi e Progetto di Algoritmi`
- Data appello: `2025-06-09`
- Parte: `Parte I`
- Numero pagine: `2`
- Stato fonte: `report_creato`
- Stato report: `ready_for_codex`
- Priorità: `alta`
- Nome report consigliato: `09_ingestion_reports/ingestion_report_exam_2025_06_09_part1.md`

---

## 2. Nota di audit repo prima dell'applicazione

Prima di applicare questo report, Codex deve verificare se il report precedente `ingestion_report_exam_2025_07_03_part1.md` è stato applicato localmente e se le modifiche sono state pushate.

Dalla repo pubblica risultano visibili:

```txt
02_transcriptions/exams/exam_2026_01_12.md
03_exercise_catalog/exercises/exam_2026_01_12_*.md
04_methods/metodo_programmazione_dinamica_zaino_01.md
04_methods/metodo_dp_cammini_con_parita.md
04_methods/metodo_kruskal_mst.md
04_methods/metodo_riduzione_clique_vertex_cover.md
04_methods/metodo_dimostrare_np_completezza.md
05_theory/programmazione_dinamica.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/zaino_01.md
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
```

Dalla repo pubblica NON risultano ancora visibili:

```txt
09_ingestion_reports/
02_transcriptions/exams/exam_2025_07_03_part1.md
03_exercise_catalog/exercises/exam_2025_07_03_p1_e01.md
03_exercise_catalog/exercises/exam_2025_07_03_p1_e02.md
04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md
04_methods/metodo_dp_cammini_colori_conteggi.md
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/grafi_colorati.md
```

> [!Warning]
> Se Codex ha davvero applicato il report precedente, probabilmente le modifiche non sono state pushate oppure sono su un branch diverso da `master`.
>
> Prima di applicare questo nuovo report, verificare:
>
> 1. `git status`
> 2. `git branch`
> 3. `git log --oneline -5`
> 4. presenza locale dei file del report `2025-07-03`
> 5. eventuale push su GitHub

---

## 3. Sintesi contenuto

L'appello contiene solo la Parte I e presenta due esercizi, entrambi di programmazione dinamica:

```txt
Parte I — 9 giugno 2025

Esercizio 1:
- LCS tra due sequenze X e Y.
- Ogni simbolo ha colore rosso, blu o nero.
- Si vuole una più lunga sottosequenza comune con al massimo 2 simboli rossi e al massimo 3 simboli blu.
- Richiede coefficienti, caso base, passo ricorsivo, coefficiente ottimo, algoritmo bottom-up e ricostruzione.

Esercizio 2:
- Grafo con archi colorati R/N/B.
- Stabilire per ogni coppia di vertici se esiste un cammino in cui:
  - un arco nero non è mai preceduto da un arco rosso;
  - un arco rosso non è mai preceduto da un arco blu.
- Il testo segnala esplicitamente la necessità di considerare un problema ausiliario opportunamente vincolato.
- Richiede coefficienti, caso base, passo ricorsivo e soluzione finale.
```

Pattern forti:

- programmazione dinamica tabellare;
- LCS con stato esteso da vincoli sui colori;
- ricostruzione della soluzione in DP;
- DP booleana su grafi colorati;
- problema ausiliario per gestire vincoli locali tra archi consecutivi;
- ricorrenza stile Floyd-Warshall estesa con informazioni aggiuntive.

---

## 4. Pagine / sezioni analizzate

| Pagina PDF | Contenuto |
|---|---|
| 1 | Parte I, Esercizio 1: LCS con al massimo 2 simboli rossi e al massimo 3 simboli blu |
| 2 | Parte I, Esercizio 2: cammini in grafo colorato con vincoli di precedenza tra colori degli archi |

---

## 5. Argomenti individuati

```md
- #topic/programmazione-dinamica
- #topic/lcs
- #topic/sottosequenze
- #topic/vincoli-di-conteggio
- #topic/colori
- #topic/ricorrenze-dp
- #topic/ricostruzione-soluzione
- #topic/grafi
- #topic/grafi-colorati
- #topic/cammini
- #topic/dp-booleana
- #topic/stato-esteso
- #topic/problema-ausiliario
```

---

## 6. Trascrizione appello da creare

Codex deve creare:

```txt
02_transcriptions/exams/exam_2025_06_09_part1.md
```

Contenuto consigliato:

```md
---
type: exam_transcription
source: 01_sources/exams_raw/parteI-09giu25.pdf
exam_date: 2025-06-09
part: Parte I
status: transcribed
tags:
  - apa
  - appello
  - exam/raw
  - parte-i
---

# Appello 2025-06-09 — Parte I

> [!Info]
> Fonte originale: `01_sources/exams_raw/parteI-09giu25.pdf`

## Struttura dell'appello

| ID | Parte | Argomento principale | Punti | Stato |
|---|---|---|---:|---|
| [[exam_2025_06_09_p1_e01]] | Parte I | DP, LCS con vincoli sui colori | 31 | cataloged |
| [[exam_2025_06_09_p1_e02]] | Parte I | DP su grafi colorati, cammini con vincoli di precedenza | 31 | cataloged |

## Esercizio 1

Siano:

$$
X = \langle x_1,\dots,x_m\rangle
$$

e

$$
Y = \langle y_1,\dots,y_n\rangle
$$

due sequenze su un alfabeto $S$ di simboli.

A ogni simbolo è associato un colore, tra rosso, blu e nero, ricavabile tramite una funzione nota e calcolabile:

$$
col:S \to \{R,B,N\}
$$

Mediante programmazione dinamica, si vuole determinare una più lunga sottosequenza comune di $X$ e $Y$ nella quale vi sono al massimo 2 simboli rossi e al massimo 3 simboli blu.

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

Mediante programmazione dinamica, si vuole stabilire per ogni coppia di vertici $(i,j)$ se esiste un cammino da $i$ a $j$ nel quale:

- un arco nero non è mai preceduto da un arco rosso;
- un arco rosso non è mai preceduto da un arco blu.

Il testo specifica che sarà necessario considerare il problema opportunamente vincolato, cioè un problema ausiliario.

Richieste:

1. definire i coefficienti;
2. scrivere il caso base;
3. scrivere il passo ricorsivo;
4. indicare qual è la soluzione del problema.
```

---

## 7. Esercizi da creare

### 7.1 `exam_2025_06_09_p1_e01`

- File da creare: `03_exercise_catalog/exercises/exam_2025_06_09_p1_e01.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/parteI-09giu25.pdf`
- Pagina: `1`
- Parte: `Parte I`
- Punti: `31`
- Titolo: `DP per LCS con al massimo 2 simboli rossi e 3 simboli blu`
- Argomento principale: `programmazione dinamica`
- Argomenti secondari:
  - `LCS`
  - `sottosequenze comuni`
  - `vincoli di conteggio`
  - `colori`
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
  - `[[metodo_programmazione_dinamica_lcs_vincoli_colori]]`
  - `[[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]`
  - `[[metodo_ricostruzione_soluzione_dp]]`
- Teoria collegata:
  - `[[programmazione_dinamica]]`
  - `[[lcs]]`
  - `[[sottosequenze_comuni]]`
- Pattern sospetto:
  - `DP su sequenze con stato esteso da vincoli di conteggio`
- Difficoltà stimata: `alta`
- Priorità: `altissima`
- Note:
  - È fortemente collegato a `exam_2025_07_03_p1_e01`.
  - In entrambi i casi il pattern è LCS con una o più dimensioni aggiuntive nello stato.
  - Stato probabile: $c_{i,j,r,b}$ = lunghezza massima di una sottosequenza comune tra $X[1..i]$ e $Y[1..j]$ usando al massimo $r$ simboli rossi e al massimo $b$ simboli blu.
  - La soluzione finale dovrebbe essere collegata al coefficiente $c_{m,n,2,3}$.
  - Il colore nero non consuma budget sui contatori rosso/blu.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/parteI-09giu25.pdf
exam_date: 2025-06-09
part: Parte I
exercise_number: 1
points: 31
status: cataloged
difficulty: alta
tags:
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/sottosequenze
  - topic/vincoli-di-conteggio
  - topic/colori
  - topic/ricostruzione-soluzione
  - status/cataloged
---

# Exam 2025-06-09 — Parte I — Esercizio 1

## Testo essenziale

Determinare una più lunga sottosequenza comune tra due sequenze $X$ e $Y$, con vincoli:

- al massimo 2 simboli rossi;
- al massimo 3 simboli blu.

Ogni simbolo $s \in S$ ha colore $col(s) \in \{R,B,N\}$.

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
- Metodo probabile: [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- Pattern: [[dp_su_sequenze_con_vincoli_di_conteggio]]

## Collegamenti utili

- [[exam_2025_07_03_p1_e01]] — variante LCS con vincolo di ingombro
- [[metodo_ricostruzione_soluzione_dp]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato

> [!Warning]
> Soluzione non ancora inserita. Verificare se il docente preferisce coefficienti con contatori "al massimo" o "esattamente" e conversione finale.
```

---

### 7.2 `exam_2025_06_09_p1_e02`

- File da creare: `03_exercise_catalog/exercises/exam_2025_06_09_p1_e02.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/parteI-09giu25.pdf`
- Pagina: `2`
- Parte: `Parte I`
- Punti: `31`
- Titolo: `DP su grafi colorati con vincoli di precedenza tra colori`
- Argomento principale: `programmazione dinamica su grafi`
- Argomenti secondari:
  - `grafi`
  - `grafi colorati`
  - `cammini`
  - `vincoli locali`
  - `problema ausiliario`
  - `dp booleana`
  - `stato esteso`
- Tipo richiesta:
  - definire coefficienti;
  - caso base;
  - passo ricorsivo;
  - indicare soluzione finale.
- Metodo probabile:
  - `[[metodo_dp_cammini_colori_precedenze]]`
  - `[[metodo_dp_cammini_colori_conteggi]]`
  - `[[metodo_dp_cammini_con_parita]]`
- Teoria collegata:
  - `[[grafi]]`
  - `[[grafi_colorati]]`
  - `[[cammini]]`
  - `[[programmazione_dinamica_su_grafi]]`
- Pattern sospetto:
  - `DP booleana su grafi con vincoli locali sulle sequenze di archi`
- Difficoltà stimata: `alta`
- Priorità: `altissima`
- Note:
  - È collegato a:
    - `exam_2026_01_12_e02`: cammini con numero pari di archi;
    - `exam_2025_07_03_p1_e02`: cammini con esattamente 2 rossi e 2 blu.
  - Qui il vincolo non è un conteggio, ma una regola locale tra colori consecutivi.
  - Il testo segnala esplicitamente la necessità di un problema ausiliario vincolato.
  - Stato probabile: booleano con vertici estremi, insieme di intermedi ammessi e informazione sui colori iniziale/finale del cammino, così da poter verificare le transizioni vietate quando si concatenano sottocammini.
  - Transizioni vietate:
    - rosso seguito da nero;
    - blu seguito da rosso.
  - Formulazione equivalente: lungo il cammino non devono comparire coppie consecutive di colori $(R,N)$ né $(B,R)$.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/parteI-09giu25.pdf
exam_date: 2025-06-09
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
  - topic/problema-ausiliario
  - topic/stato-esteso
  - status/cataloged
---

# Exam 2025-06-09 — Parte I — Esercizio 2

## Testo essenziale

Dato un grafo $(V,E,col)$ senza cappi, con archi colorati rosso, nero o blu, stabilire per ogni coppia di vertici $(i,j)$ se esiste un cammino da $i$ a $j$ in cui:

- un arco nero non è mai preceduto da un arco rosso;
- un arco rosso non è mai preceduto da un arco blu.

## Interpretazione del vincolo

Non devono comparire due archi consecutivi con colori:

$$
(R,N)
$$

oppure

$$
(B,R)
$$

## Richieste

1. Definire i coefficienti.
2. Scrivere il caso base.
3. Scrivere il passo ricorsivo.
4. Indicare la soluzione.

## Classificazione

- Argomento: [[programmazione_dinamica_su_grafi]]
- Teoria: [[grafi_colorati]]
- Metodo probabile: [[metodo_dp_cammini_colori_precedenze]]
- Pattern: [[dp_booleana_su_grafi_con_vincoli_locali]]

## Collegamenti utili

- [[exam_2026_01_12_e02]] — cammini con numero pari di archi
- [[exam_2025_07_03_p1_e02]] — cammini con conteggi esatti di colori
- [[metodo_dp_cammini_colori_conteggi]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato

> [!Warning]
> Verificare la formulazione esatta del problema ausiliario preferita dal corso. Probabilmente serve memorizzare il colore del primo e/o dell'ultimo arco del cammino per poter concatenare sottocammini nel passo ricorsivo.
```

---

## 8. Metodi da creare o aggiornare

### 8.1 Nuovi metodi da creare

Creare se assenti:

```txt
04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
04_methods/metodo_dp_cammini_colori_precedenze.md
```

### 8.2 Metodi esistenti da aggiornare

Aggiornare se esistono:

```txt
04_methods/dynamic_programming.md
04_methods/metodo_ricostruzione_soluzione_dp.md
04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md
04_methods/metodo_dp_cammini_colori_conteggi.md
04_methods/metodo_dp_cammini_con_parita.md
```

> [!Warning]
> Se i metodi `metodo_programmazione_dinamica_lcs_vincolo_ingombro.md` e `metodo_dp_cammini_colori_conteggi.md` non esistono ancora, significa che il report del 3 luglio 2025 non è stato applicato o pushato. In quel caso applicare prima o insieme le modifiche mancanti del report precedente.

### 8.3 Contenuto minimo per `metodo_programmazione_dinamica_lcs_vincoli_colori.md`

```md
---
type: method
status: scaffold
tags:
  - method
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/vincoli-di-conteggio
  - topic/colori
---

# Metodo — LCS con vincoli sui colori

## Quando si usa

Quando si cerca una sottosequenza comune massima tra due sequenze, ma la soluzione deve rispettare vincoli sul numero di simboli di certi colori.

## Stato tipico

Un possibile stato è:

$$
c_{i,j,r,b}
$$

dove:
- $i$ e $j$ indicano i prefissi delle due sequenze;
- $r$ è il numero massimo di simboli rossi utilizzabili;
- $b$ è il numero massimo di simboli blu utilizzabili.

## Soluzione finale tipica

Per il caso dell'appello 2025-06-09:

$$
c_{m,n,2,3}
$$

## Esercizi collegati

- [[exam_2025_06_09_p1_e01]]
- [[exam_2025_07_03_p1_e01]]

## Teoria necessaria

- [[programmazione_dinamica]]
- [[lcs]]
- [[sottosequenze_comuni]]

## Errori comuni

- Dimenticare di diminuire il contatore corretto quando si sceglie un simbolo rosso o blu.
- Diminuire un contatore quando il simbolo è nero.
- Trattare come scegliibile un simbolo se $x_i \ne y_j$.
- Ricostruire la soluzione senza verificare quale caso della ricorrenza ha prodotto il massimo.

> [!Warning]
> Metodo da completare durante la fase di soluzione.
```

### 8.4 Contenuto minimo per `metodo_dp_cammini_colori_precedenze.md`

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
  - topic/problema-ausiliario
---

# Metodo — DP su cammini con vincoli di precedenza tra colori

## Quando si usa

Quando bisogna stabilire l'esistenza di un cammino tra coppie di vertici che rispetta vincoli locali tra colori di archi consecutivi.

## Vincoli tipici

Nel caso dell'appello 2025-06-09 non sono ammesse le coppie consecutive:

$$
(R,N)
$$

e

$$
(B,R)
$$

## Problema ausiliario

Il problema principale "esiste un cammino valido da $i$ a $j$?" può richiedere un problema ausiliario che tenga traccia di informazioni aggiuntive sui colori agli estremi del cammino.

Un possibile stato contiene:

- vertici estremi $i,j$;
- limite sui vertici intermedi;
- colore del primo arco del cammino;
- colore dell'ultimo arco del cammino.

Queste informazioni permettono di verificare se due sottocammini possono essere concatenati senza violare i vincoli locali.

## Esercizi collegati

- [[exam_2025_06_09_p1_e02]]
- [[exam_2025_07_03_p1_e02]]
- [[exam_2026_01_12_e02]]

## Teoria necessaria

- [[grafi]]
- [[grafi_colorati]]
- [[programmazione_dinamica_su_grafi]]

## Errori comuni

- Non introdurre il problema ausiliario nonostante il vincolo locale.
- Verificare solo il colore dell'arco corrente senza sapere il colore precedente.
- Confondere "preceduto da" con "seguito da".
- Dimenticare che il vincolo riguarda archi consecutivi nel cammino, non tutti gli archi del grafo.

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
05_theory/vincoli_su_colori.md
```

Aggiornare:

```txt
05_theory/programmazione_dinamica.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/grafi.md
```

> [!Important]
> La teoria deve restare minima e collegata agli esercizi.
> Non creare una dispensa completa su LCS o grafi colorati; creare solo definizioni e schemi utili agli appelli.

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
06_exam_patterns/dp_su_sequenze_con_vincoli_di_conteggio.md
06_exam_patterns/dp_booleana_su_grafi_con_vincoli_locali.md
```

### 10.1 Pattern esercizi ricorrenti

Aggiungere o aggiornare in `06_exam_patterns/recurring_exercise_types.md`:

```md
## DP — Definizione coefficienti, casi base e ricorrenza

- Esercizi collegati:
  - [[exam_2026_01_12_e01]]
  - [[exam_2026_01_12_e02]]
  - [[exam_2026_01_12_e05]]
  - [[exam_2025_07_03_p1_e01]]
  - [[exam_2025_07_03_p1_e02]]
  - [[exam_2025_06_09_p1_e01]]
  - [[exam_2025_06_09_p1_e02]]
- Frequenza osservata: `3 appelli`
- Priorità: `altissima`
- Descrizione:
  - Gli esercizi di Parte I sono quasi interamente basati sull'impostazione formale della DP: coefficienti, casi base, passo ricorsivo, soluzione finale e spesso ricostruzione.

## LCS con vincoli aggiuntivi

- Esercizi collegati:
  - [[exam_2025_07_03_p1_e01]]
  - [[exam_2025_06_09_p1_e01]]
- Frequenza osservata: `2 appelli`
- Priorità: `altissima`
- Varianti osservate:
  - LCS con vincolo di ingombro massimo;
  - LCS con vincoli sul numero massimo di simboli rossi e blu.

## DP booleana su grafi con proprietà del cammino

- Esercizi collegati:
  - [[exam_2026_01_12_e02]]
  - [[exam_2025_07_03_p1_e02]]
  - [[exam_2025_06_09_p1_e02]]
- Frequenza osservata: `3 appelli`
- Priorità: `altissima`
- Varianti osservate:
  - esistenza di cammino con numero pari di archi;
  - esistenza di cammino con esattamente 2 archi rossi e 2 archi blu;
  - esistenza di cammino senza certe precedenze tra colori di archi.
```

### 10.2 Aggiornare `variations_by_appeal.md`

```md
## Programmazione dinamica su sequenze

| Appello | Esercizio | Variante |
|---|---|---|
| 2025-07-03 Parte I | [[exam_2025_07_03_p1_e01]] | LCS con vincolo di ingombro |
| 2025-06-09 Parte I | [[exam_2025_06_09_p1_e01]] | LCS con al massimo 2 rossi e 3 blu |

## Programmazione dinamica su grafi

| Appello | Esercizio | Variante |
|---|---|---|
| 2026-01-12 | [[exam_2026_01_12_e02]] | cammino con numero pari di archi |
| 2025-07-03 Parte I | [[exam_2025_07_03_p1_e02]] | cammino con esattamente 2 archi rossi e 2 archi blu |
| 2025-06-09 Parte I | [[exam_2025_06_09_p1_e02]] | cammino con vincoli di precedenza tra colori |
```

### 10.3 Aggiornare `high_yield_topics.md`

Aggiungere o aumentare priorità:

```md
## Altissima resa

- Programmazione dinamica Parte I:
  - coefficienti;
  - caso base;
  - passo ricorsivo;
  - coefficiente soluzione;
  - bottom-up;
  - ricostruzione.
- LCS con vincoli aggiuntivi:
  - vincoli di budget;
  - vincoli di conteggio;
  - dimensioni extra nello stato.
- DP booleana su grafi:
  - proprietà dei cammini;
  - stato esteso con informazioni aggiuntive;
  - problemi ausiliari per vincoli non locali.
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
## 2025-06-09 — Parte I

| Esercizio | Parte | Argomento | Punti | Difficoltà | Stato |
|---|---|---|---:|---|---|
| [[exam_2025_06_09_p1_e01]] | Parte I | DP LCS con vincoli sui colori | 31 | alta | cataloged |
| [[exam_2025_06_09_p1_e02]] | Parte I | DP cammini con vincoli di precedenza tra colori | 31 | alta | cataloged |
```

### 11.2 `index_by_topic.md`

Aggiungere:

```md
## Programmazione dinamica

- [[exam_2025_06_09_p1_e01]] — LCS con vincoli sui colori
- [[exam_2025_06_09_p1_e02]] — cammini con vincoli di precedenza tra colori

## LCS / Sottosequenze comuni

- [[exam_2025_06_09_p1_e01]]

## Grafi

- [[exam_2025_06_09_p1_e02]]

## Grafi colorati

- [[exam_2025_06_09_p1_e02]]

## DP booleana su grafi

- [[exam_2025_06_09_p1_e02]]
```

### 11.3 `index_by_difficulty.md`

Aggiungere:

```md
## Alta

- [[exam_2025_06_09_p1_e01]]
- [[exam_2025_06_09_p1_e02]]
```

---

## 12. Esempi svolti da creare

Non creare ancora soluzioni complete, salvo scaffold futuro.

Possibili file futuri:

```txt
07_solved_examples/solved_exam_2025_06_09_p1_e01_lcs_colori.md
07_solved_examples/solved_exam_2025_06_09_p1_e02_cammini_precedenze_colori.md
```

Priorità consigliata:

1. `exam_2025_06_09_p1_e01` — da confrontare con `exam_2025_07_03_p1_e01`;
2. `exam_2025_06_09_p1_e02` — da confrontare con le altre DP su grafi;
3. creare metodo unificato per:
   - LCS con vincoli aggiuntivi;
   - DP booleana su grafi con stato esteso.

---

## 13. Dubbi e parti da verificare

> [!Warning]
> Il PDF è leggibile tramite testo estratto, ma resta necessario verificare la notazione matematica definitiva usata dal docente.

Punti da verificare:

- In `exam_2025_06_09_p1_e01`, verificare se conviene usare coefficienti con contatori "al massimo" o "esattamente" per i simboli rossi/blu.
- In `exam_2025_06_09_p1_e01`, verificare come gestire simboli neri nel passo ricorsivo: non consumano nessun contatore.
- In `exam_2025_06_09_p1_e02`, verificare il problema ausiliario richiesto dal docente:
  - tracciare il colore dell'ultimo arco;
  - oppure tracciare colore iniziale e finale del cammino;
  - oppure altra formulazione equivalente.
- In `exam_2025_06_09_p1_e02`, verificare il caso base per cammini di lunghezza 0 e per archi singoli.
- Verificare se le regole "preceduto da" vanno interpretate solo su archi consecutivi, come sembra naturale, o in senso più globale nel cammino.

---

## 14. Istruzioni operative per Codex

Codex deve:

1. Verificare o creare:

```txt
09_ingestion_reports/
```

2. Salvare questo report come:

```txt
09_ingestion_reports/ingestion_report_exam_2025_06_09_part1.md
```

3. Verificare che il PDF sia presente o copiarlo in:

```txt
01_sources/exams_raw/parteI-09giu25.pdf
```

4. Prima di applicare il report, controllare se il report precedente del 3 luglio 2025 è stato applicato localmente:

```txt
02_transcriptions/exams/exam_2025_07_03_part1.md
03_exercise_catalog/exercises/exam_2025_07_03_p1_e01.md
03_exercise_catalog/exercises/exam_2025_07_03_p1_e02.md
```

5. Se i file del 3 luglio 2025 mancano, non cancellare nulla: applicare anche quel report oppure segnalare che manca lo step precedente.

6. Creare la trascrizione:

```txt
02_transcriptions/exams/exam_2025_06_09_part1.md
```

7. Creare i file esercizio:

```txt
03_exercise_catalog/exercises/exam_2025_06_09_p1_e01.md
03_exercise_catalog/exercises/exam_2025_06_09_p1_e02.md
```

8. Aggiornare gli indici:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

9. Aggiornare pattern:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
```

10. Creare o aggiornare metodi:

```txt
04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
04_methods/metodo_dp_cammini_colori_precedenze.md
04_methods/dynamic_programming.md
04_methods/metodo_ricostruzione_soluzione_dp.md
04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md
04_methods/metodo_dp_cammini_colori_conteggi.md
04_methods/metodo_dp_cammini_con_parita.md
```

11. Creare o aggiornare teoria minima:

```txt
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/grafi_colorati.md
05_theory/vincoli_su_colori.md
05_theory/programmazione_dinamica.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/grafi.md
```

12. Aggiornare `PROJECT_STATUS.md`:

```md
## Stato aggiornato

- Appello analizzato: `01_sources/exams_raw/parteI-09giu25.pdf`
- Data: `2025-06-09`
- Parte: `Parte I`
- Report creato: `09_ingestion_reports/ingestion_report_exam_2025_06_09_part1.md`
- Trascrizione creata: `02_transcriptions/exams/exam_2025_06_09_part1.md`
- Esercizi catalogati: `2`
- Stato: `terzo appello catalogato`
```

13. Aggiornare `TODO.md`:

```md
## Prossimi step

- [ ] Verificare manualmente trascrizione dell'appello `2025-06-09 Parte I`
- [ ] Risolvere `exam_2025_06_09_p1_e01` LCS con vincoli sui colori
- [ ] Risolvere `exam_2025_06_09_p1_e02` cammini con vincoli di precedenza tra colori
- [ ] Consolidare metodo comune per LCS con vincoli aggiuntivi
- [ ] Consolidare metodo comune per DP booleana su grafi con stato esteso
- [ ] Aggiornare mappa pattern dopo almeno 3 appelli
- [ ] Analizzare prossimo PDF in `01_sources/exams_raw/`
```

---

## 15. Definition of Done

Questo ingestion report è considerato applicato quando Codex ha:

- [ ] salvato il report nella repo;
- [ ] verificato presenza di `09_ingestion_reports/`;
- [ ] verificato se il report del 3 luglio 2025 è stato applicato;
- [ ] creato la trascrizione essenziale dell'appello;
- [ ] creato i due file esercizio;
- [ ] aggiornato indici per esame, topic e difficoltà;
- [ ] aggiornato pattern ricorrenti e variazioni per appello;
- [ ] creato scaffold dei nuovi metodi;
- [ ] creato teoria minima per LCS, sottosequenze comuni, grafi colorati e vincoli sui colori;
- [ ] aggiornato `PROJECT_STATUS.md`;
- [ ] aggiornato `TODO.md`;
- [ ] mantenuto `[!Warning]` sulle parti da verificare;
- [ ] non creato soluzioni complete non richieste.

---

## 16. Prossima azione consigliata

Dopo applicazione del report da parte di Codex:

1. fare commit e push della repo;
2. controllare i link Obsidian;
3. verificare che siano presenti tutti e tre gli appelli catalogati:
   - `2026-01-12`;
   - `2025-07-03 Parte I`;
   - `2025-06-09 Parte I`;
4. creare una nota di sintesi sui pattern di Parte I:
   - LCS con vincoli;
   - DP su grafi con stato esteso;
5. procedere con il prossimo appello raw.
