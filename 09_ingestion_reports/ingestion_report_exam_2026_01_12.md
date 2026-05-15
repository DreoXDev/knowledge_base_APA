# Ingestion Report — esame_apa_12_01_2026

> [!Info]
> Report finale per l'ingestione dell'appello `esame_apa_12_01_2026.pdf` nella knowledge base Obsidian `knowledge_base_APA`.
>
> Stato report: `ready_for_codex`
>
> Obiettivo: creare trascrizione essenziale, catalogare gli esercizi, aggiornare gli indici e iniziare la mappa dei pattern ricorrenti.

---

## 1. Metadata

- Source ID: `exam_2026_01_12`
- File sorgente: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Tipo fonte: `appello_raw`
- Corso: `Analisi e Progettazione di Algoritmi`
- Università: `Università di Milano-Bicocca`
- Data appello: `2026-01-12`
- Numero pagine: `4`
- Stato fonte: `report_creato`
- Stato report: `ready_for_codex`
- Priorità: `alta`
- Nome report consigliato: `09_ingestion_reports/ingestion_report_exam_2026_01_12.md`

---

## 2. Sintesi contenuto

L'appello contiene:

```txt
Parte I — 12 gennaio 2026
- Esercizio 1: programmazione dinamica su problema tipo zaino 0/1.
- Esercizio 2: programmazione dinamica su cammini di lunghezza pari in un grafo.

Parte II — scritto completo e seconda prova parziale — 12 gennaio 2026
- Esercizio 1: esecuzione dell'algoritmo di Kruskal per MST.
- Esercizio 2: riduzioni tra CLIQUE e VERTEX-COVER con grafo complementare.
- Esercizio 3: ricorrenza di programmazione dinamica per zaino 0/1.
- Esercizio 4: dimostrazione che CLIQUE è NP-completo.
- Domanda facoltativa premiale: una tra due domande sui matroidi.
```

Pattern forti già evidenti:

- programmazione dinamica con definizione coefficienti, casi base, ricorrenza, valore ottimo e ricostruzione;
- grafi e algoritmi greedy, in particolare Kruskal/MST;
- riduzioni NP-complete tra CLIQUE e VERTEX-COVER;
- dimostrazioni di appartenenza a NP e NP-hardness;
- teoria sui matroidi collegata a greedy e foreste.

---

## 3. Pagine / sezioni analizzate

| Pagina PDF | Contenuto |
|---|---|
| 1 | Parte I, Esercizio 1: DP zaino 0/1 completo con richieste a punti |
| 2 | Parte I, Esercizio 2: DP su cammini pari in grafo |
| 3 | Parte II, Esercizi 1 e 2: Kruskal MST; riduzioni CLIQUE/VERTEX-COVER |
| 4 | Parte II, Esercizi 3 e 4; domanda facoltativa premiale sui matroidi |

---

## 4. Argomenti individuati

```md
- #topic/programmazione-dinamica
- #topic/zaino-01
- #topic/ricorrenze-dp
- #topic/ricostruzione-soluzione
- #topic/grafi
- #topic/cammini
- #topic/parita
- #topic/chiusura-transitiva
- #topic/greedy
- #topic/kruskal
- #topic/mst
- #topic/np-completezza
- #topic/riduzioni
- #topic/clique
- #topic/vertex-cover
- #topic/matroidi
- #topic/correttezza
```

---

## 5. Trascrizione appello da creare

Codex deve creare:

```txt
02_transcriptions/exams/exam_2026_01_12.md
```

Contenuto consigliato:

```md
---
type: exam_transcription
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
status: transcribed
tags:
  - apa
  - appello
  - exam/raw
---

# Appello 2026-01-12

> [!Info]
> Fonte originale: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`

## Struttura dell'appello

| ID | Parte | Argomento principale | Punti | Stato |
|---|---|---|---:|---|
| [[exam_2026_01_12_e01]] | Parte I | Programmazione dinamica, zaino 0/1 | 31 | cataloged |
| [[exam_2026_01_12_e02]] | Parte I | Programmazione dinamica, cammini pari | 31 | cataloged |
| [[exam_2026_01_12_e03]] | Parte II | Kruskal, MST | 6 | cataloged |
| [[exam_2026_01_12_e04]] | Parte II | Riduzioni CLIQUE/VERTEX-COVER | 6 | cataloged |
| [[exam_2026_01_12_e05]] | Parte II | Programmazione dinamica, zaino 0/1 | 7 | cataloged |
| [[exam_2026_01_12_e06]] | Parte II | CLIQUE NP-completo | 14 | cataloged |
| [[exam_2026_01_12_bonus_matroidi]] | Bonus | Matroidi | 3 | cataloged |

## Parte I

### Esercizio 1

Dato un numero naturale $K > 0$ e un insieme $X = \{1,2,\dots,n\}$ di $n$ oggetti. A ogni oggetto $i$ sono associati un valore $v_i > 0$, un ingombro intero $w_i > 0$ e un colore `rosso`, `blu` o `nero`.

Si vuole calcolare, mediante programmazione dinamica, un sottoinsieme di valore complessivo massimo tra tutti i sottoinsiemi di $X$ con ingombro complessivo inferiore o uguale a $K$ e in cui tra i colori degli oggetti vi è la presenza del rosso.

Richieste:
1. definire i coefficienti/variabili dei sottoproblemi;
2. scrivere il caso base;
3. scrivere il passo ricorsivo;
4. specificare il coefficiente che fornisce il valore ottimo;
5. scrivere l'algoritmo bottom-up;
6. scrivere l'algoritmo ricorsivo di ricostruzione/stampa del sottoinsieme soluzione.

### Esercizio 2

Dato un grafo $G=(V,E)$ senza cappi, mediante programmazione dinamica si vuole stabilire, per ogni coppia di vertici $(i,j)$, se esiste un cammino da $i$ a $j$ composto da un numero pari di archi.

Richieste:
1. definire i coefficienti;
2. scrivere il caso base;
3. scrivere il passo ricorsivo;
4. indicare qual è la soluzione del problema.

## Parte II

### Esercizio 1

Dato il grafo non orientato, connesso e pesato $G=(V,E)$ con archi:

- $(b,c)$ peso 4
- $(b,d)$ peso 1
- $(a,c)$ peso 6
- $(a,b)$ peso 7
- $(c,d)$ peso 2
- $(d,e)$ peso 5
- $(c,e)$ peso 3

Mostrare l'ordine con cui Kruskal aggiunge o scarta gli archi del Minimum Spanning Tree, riportando ogni passaggio negli schemi $Q1, Q2, \dots$.

### Esercizio 2

Dato un grafo $G$ con $k=3$, disegnare il grafo $G'$ ottenuto tramite la riduzione richiesta:

- turno AL: da CLIQUE a VERTEX-COVER;
- turno MZ: da VERTEX-COVER a CLIQUE.

Il grafo disegnato ha vertici $a,b,c,d,e,f$ e archi:

- $(a,b)$
- $(a,f)$
- $(f,e)$
- $(b,e)$
- $(b,c)$
- $(e,c)$
- $(e,d)$

Richieste:
- indicare quanti e quali sono i vertici della copertura di $G'$;
- indicare quanti e quali sono i vertici della clique di $G'$.

> [!Warning]
> La soluzione specifica dei vertici va verificata in fase di soluzione. Per la catalogazione basta registrare che l'esercizio richiede il grafo complementare e la relazione tra dimensione della clique e dimensione del vertex cover.

### Esercizio 3

Siano dati un numero naturale $K>0$ e un insieme $X=\{1,2,\dots,n\}$ di oggetti. A ogni oggetto $i$ sono associati un valore $v_i>0$ e un ingombro intero $w_i>0$.

Mediante programmazione dinamica, si vuole determinare il valore complessivo massimo di un sottoinsieme di $X$ con ingombro complessivo inferiore o uguale a $K$.

Scrivere le equazioni di ricorrenza, per caso base e passo ricorsivo, usando $c_{i,k}$ come coefficiente relativo al generico sottoproblema $(i,k)$.

### Esercizio 4

Dimostrare che CLIQUE è NP-completo:

- 4.A: dimostrare che CLIQUE è in NP;
- 4.B: dimostrare che CLIQUE è NP-hard mediante una riduzione.

## Domanda facoltativa premiale

Una e una sola a scelta tra:

1. Dimostrare che se un sistema di indipendenza $(E,F)$ è un matroide, allora per ogni funzione peso $w:E \to \mathbb{R}^+ \cup \{0\}$, oppure $w:E \to \mathbb{R}$, l'algoritmo `Greedy(E,F,w)` restituisce una soluzione ottima al problema di massimo associato a $(E,F)$ e $w$.

2. Dimostrare che, dati un grafo non orientato $G=(V,E)$ e l'insieme $F=\{A \subseteq E : (V,A) \text{ è una foresta}\}$, la coppia $(E,F)$ è un matroide.
```

---

## 6. Esercizi da creare

### 6.1 `exam_2026_01_12_e01`

- File da creare: `03_exercise_catalog/exercises/exam_2026_01_12_e01.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Pagina: `1`
- Parte: `Parte I`
- Punti: `31`
- Titolo: `DP zaino 0/1 con vincolo di presenza del colore rosso`
- Argomento principale: `programmazione dinamica`
- Argomenti secondari:
  - `zaino 0/1`
  - `vincoli aggiuntivi`
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
  - `[[metodo_programmazione_dinamica_zaino_01]]`
  - `[[metodo_ricostruzione_soluzione_dp]]`
- Teoria collegata:
  - `[[programmazione_dinamica]]`
  - `[[zaino_01]]`
- Pattern sospetto:
  - `DP tabellare con stato esteso da un vincolo logico`
- Difficoltà stimata: `alta`
- Priorità: `alta`
- Note:
  - Richiede di gestire non solo peso e prefisso di oggetti, ma anche la presenza di almeno un oggetto rosso.
  - Possibili stati: aggiungere una dimensione booleana `r` che indica se è già stato scelto almeno un oggetto rosso.
  - Non risolvere completamente in questa fase se il file è solo di catalogazione.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
part: Parte I
exercise_number: 1
points: 31
status: cataloged
difficulty: alta
tags:
  - topic/programmazione-dinamica
  - topic/zaino-01
  - topic/ricostruzione-soluzione
  - status/cataloged
---

# Exam 2026-01-12 — Esercizio 1

## Testo essenziale

Problema di zaino 0/1 con oggetti aventi valore, peso intero e colore tra rosso, blu, nero. Cercare un sottoinsieme di valore massimo con peso totale al più $K$ e contenente almeno un oggetto rosso.

## Richieste

1. Definire i coefficienti.
2. Scrivere il caso base.
3. Scrivere il passo ricorsivo.
4. Specificare il coefficiente della soluzione ottima.
5. Scrivere algoritmo bottom-up.
6. Scrivere algoritmo ricorsivo di ricostruzione.

## Classificazione

- Argomento: [[programmazione_dinamica]]
- Metodo probabile: [[metodo_programmazione_dinamica_zaino_01]]
- Pattern: [[dp_con_stato_esteso]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato

> [!Warning]
> Soluzione non ancora inserita. Verificare come codificare il vincolo "almeno un rosso".
```

---

### 6.2 `exam_2026_01_12_e02`

- File da creare: `03_exercise_catalog/exercises/exam_2026_01_12_e02.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Pagina: `2`
- Parte: `Parte I`
- Punti: `31`
- Titolo: `DP su esistenza di cammini di lunghezza pari`
- Argomento principale: `programmazione dinamica su grafi`
- Argomenti secondari:
  - `grafi`
  - `cammini`
  - `parità`
  - `chiusura transitiva`
- Tipo richiesta:
  - definire coefficienti;
  - caso base;
  - passo ricorsivo;
  - indicare soluzione.
- Metodo probabile:
  - `[[metodo_dp_cammini_con_parita]]`
  - possibile variante di `[[metodo_floyd_warshall]]` con stato di parità.
- Teoria collegata:
  - `[[grafi]]`
  - `[[cammini]]`
  - `[[programmazione_dinamica_su_grafi]]`
- Pattern sospetto:
  - `DP booleana su grafi con informazione aggiuntiva di parità`
- Difficoltà stimata: `alta`
- Priorità: `alta`
- Note:
  - Il testo chiede esistenza per ogni coppia $(i,j)$.
  - Probabile stato booleano per prefisso di vertici intermedi e parità del numero di archi.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
part: Parte I
exercise_number: 2
points: 31
status: cataloged
difficulty: alta
tags:
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/cammini
  - topic/parita
  - status/cataloged
---

# Exam 2026-01-12 — Esercizio 2

## Testo essenziale

Dato un grafo $G=(V,E)$ senza cappi, stabilire tramite programmazione dinamica, per ogni coppia di vertici $(i,j)$, se esiste un cammino da $i$ a $j$ composto da un numero pari di archi.

## Richieste

1. Definire i coefficienti.
2. Scrivere il caso base.
3. Scrivere il passo ricorsivo.
4. Indicare la soluzione.

## Classificazione

- Argomento: [[programmazione_dinamica_su_grafi]]
- Metodo probabile: [[metodo_dp_cammini_con_parita]]
- Pattern: [[dp_booleana_su_grafi]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato

> [!Warning]
> Verificare se il corso imposta questa ricorrenza come variante di Floyd-Warshall o con altra notazione specifica.
```

---

### 6.3 `exam_2026_01_12_e03`

- File da creare: `03_exercise_catalog/exercises/exam_2026_01_12_e03.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Pagina: `3`
- Parte: `Parte II`
- Punti: `6`
- Titolo: `Esecuzione di Kruskal su grafo pesato`
- Argomento principale: `Kruskal / MST`
- Argomenti secondari:
  - `grafi pesati`
  - `greedy`
  - `minimum spanning tree`
- Tipo richiesta:
  - ordinare gli archi per peso;
  - simulare Kruskal;
  - indicare quali archi vengono aggiunti al MST e quali vengono scartati.
- Metodo probabile:
  - `[[metodo_kruskal_mst]]`
- Teoria collegata:
  - `[[minimum_spanning_tree]]`
  - `[[algoritmi_greedy]]`
- Pattern sospetto:
  - `simulazione manuale di algoritmo greedy`
- Difficoltà stimata: `bassa-media`
- Priorità: `alta`
- Dati del grafo:
  - Vertici: deducibili dagli archi, `a,b,c,d,e`.
  - Archi:
    - $(b,c)$ peso 4
    - $(b,d)$ peso 1
    - $(a,c)$ peso 6
    - $(a,b)$ peso 7
    - $(c,d)$ peso 2
    - $(d,e)$ peso 5
    - $(c,e)$ peso 3

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
part: Parte II
exercise_number: 1
points: 6
status: cataloged
difficulty: bassa-media
tags:
  - topic/grafi
  - topic/greedy
  - topic/kruskal
  - topic/mst
  - status/cataloged
---

# Exam 2026-01-12 — Esercizio 3

## Testo essenziale

Dato un grafo non orientato, connesso e pesato, eseguire Kruskal mostrando l'ordine con cui gli archi vengono aggiunti o scartati dal MST.

## Dati

Archi:

| Arco | Peso |
|---|---:|
| $(b,d)$ | 1 |
| $(c,d)$ | 2 |
| $(c,e)$ | 3 |
| $(b,c)$ | 4 |
| $(d,e)$ | 5 |
| $(a,c)$ | 6 |
| $(a,b)$ | 7 |

## Classificazione

- Argomento: [[minimum_spanning_tree]]
- Metodo probabile: [[metodo_kruskal_mst]]
- Pattern: [[simulazione_kruskal]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato
```

---

### 6.4 `exam_2026_01_12_e04`

- File da creare: `03_exercise_catalog/exercises/exam_2026_01_12_e04.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Pagina: `3`
- Parte: `Parte II`
- Punti: `6`
- Titolo: `Riduzioni CLIQUE/VERTEX-COVER tramite grafo complementare`
- Argomento principale: `NP-completezza / riduzioni`
- Argomenti secondari:
  - `CLIQUE`
  - `VERTEX-COVER`
  - `grafo complementare`
  - `riduzioni polinomiali`
- Tipo richiesta:
  - disegnare $G'$;
  - indicare dimensione e vertici della copertura o della clique a seconda del turno.
- Metodo probabile:
  - `[[metodo_riduzione_clique_vertex_cover]]`
- Teoria collegata:
  - `[[clique]]`
  - `[[vertex_cover]]`
  - `[[grafo_complementare]]`
  - `[[riduzioni_np_completezza]]`
- Pattern sospetto:
  - `riduzione standard tra CLIQUE e VERTEX-COVER`
- Difficoltà stimata: `media`
- Priorità: `alta`
- Dati del grafo:
  - $k=3$
  - Vertici: $a,b,c,d,e,f$
  - Archi:
    - $(a,b)$
    - $(a,f)$
    - $(f,e)$
    - $(b,e)$
    - $(b,c)$
    - $(e,c)$
    - $(e,d)$

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
part: Parte II
exercise_number: 2
points: 6
status: cataloged
difficulty: media
tags:
  - topic/np-completezza
  - topic/riduzioni
  - topic/clique
  - topic/vertex-cover
  - status/cataloged
---

# Exam 2026-01-12 — Esercizio 4

## Testo essenziale

Dato un grafo $G$ e $k=3$, costruire il grafo $G'$ richiesto dalla riduzione:

- da CLIQUE a VERTEX-COVER;
- da VERTEX-COVER a CLIQUE.

Indicare quanti e quali sono i vertici della copertura o della clique nel grafo trasformato.

## Dati

Vertici:

$$
V = \{a,b,c,d,e,f\}
$$

Archi:

$$
E = \{(a,b),(a,f),(f,e),(b,e),(b,c),(e,c),(e,d)\}
$$

## Classificazione

- Argomento: [[np_completezza]]
- Metodo probabile: [[metodo_riduzione_clique_vertex_cover]]
- Pattern: [[riduzione_clique_vertex_cover]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato

> [!Warning]
> In fase di soluzione verificare attentamente se il turno richiede di partire dal grafo originale o dal complementare e come viene definito $G'$ nel protocollo del corso.
```

---

### 6.5 `exam_2026_01_12_e05`

- File da creare: `03_exercise_catalog/exercises/exam_2026_01_12_e05.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Pagina: `4`
- Parte: `Parte II`
- Punti: `7`
- Titolo: `Ricorrenza DP per zaino 0/1`
- Argomento principale: `programmazione dinamica`
- Argomenti secondari:
  - `zaino 0/1`
  - `ricorrenze`
  - `caso base`
  - `passo ricorsivo`
- Tipo richiesta:
  - scrivere equazioni di ricorrenza;
  - indicare caso base e passo ricorsivo;
  - usare coefficiente $c_{i,k}$.
- Metodo probabile:
  - `[[metodo_programmazione_dinamica_zaino_01]]`
- Teoria collegata:
  - `[[zaino_01]]`
  - `[[programmazione_dinamica]]`
- Pattern sospetto:
  - `ricorrenza classica zaino 0/1`
- Difficoltà stimata: `bassa-media`
- Priorità: `altissima`
- Note:
  - Questo è una versione più semplice e diretta dell'Esercizio 1 della Parte I.
  - Molto utile per creare il metodo base prima di affrontare la variante con vincolo sul colore rosso.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
part: Parte II
exercise_number: 3
points: 7
status: cataloged
difficulty: bassa-media
tags:
  - topic/programmazione-dinamica
  - topic/zaino-01
  - topic/ricorrenze-dp
  - status/cataloged
---

# Exam 2026-01-12 — Esercizio 5

## Testo essenziale

Dato un problema di zaino 0/1 con capacità $K$, valori $v_i$ e pesi interi $w_i$, scrivere la ricorrenza per il valore massimo ottenibile con peso al più $K$, usando il coefficiente $c_{i,k}$.

## Classificazione

- Argomento: [[zaino_01]]
- Metodo probabile: [[metodo_programmazione_dinamica_zaino_01]]
- Pattern: [[ricorrenza_zaino_01]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato
```

---

### 6.6 `exam_2026_01_12_e06`

- File da creare: `03_exercise_catalog/exercises/exam_2026_01_12_e06.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Pagina: `4`
- Parte: `Parte II`
- Punti: `14`
- Titolo: `Dimostrazione che CLIQUE è NP-completo`
- Argomento principale: `NP-completezza`
- Argomenti secondari:
  - `CLIQUE`
  - `NP`
  - `NP-hard`
  - `riduzioni`
  - `dimostrazioni`
- Tipo richiesta:
  - dimostrare che CLIQUE è in NP;
  - dimostrare che CLIQUE è NP-hard mediante riduzione.
- Metodo probabile:
  - `[[metodo_dimostrare_np_completezza]]`
  - `[[metodo_riduzione_vertex_cover_clique]]`
- Teoria collegata:
  - `[[clique]]`
  - `[[np_completezza]]`
  - `[[riduzioni_polinomiali]]`
- Pattern sospetto:
  - `dimostrazione standard di NP-completezza`
- Difficoltà stimata: `alta`
- Priorità: `altissima`
- Note:
  - Da collegare direttamente alla domanda precedente sulle riduzioni CLIQUE/VERTEX-COVER.
  - Richiede una risposta teorica formale, non solo esercizio operativo.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
part: Parte II
exercise_number: 4
points: 14
status: cataloged
difficulty: alta
tags:
  - topic/np-completezza
  - topic/clique
  - topic/riduzioni
  - topic/correttezza
  - status/cataloged
---

# Exam 2026-01-12 — Esercizio 6

## Testo essenziale

Dimostrare che CLIQUE è NP-completo:

1. dimostrare che CLIQUE è in NP;
2. dimostrare che CLIQUE è NP-hard mediante una riduzione.

## Classificazione

- Argomento: [[np_completezza]]
- Metodo probabile: [[metodo_dimostrare_np_completezza]]
- Pattern: [[dimostrazione_np_completezza]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato
```

---

### 6.7 `exam_2026_01_12_bonus_matroidi`

- File da creare: `03_exercise_catalog/exercises/exam_2026_01_12_bonus_matroidi.md`
- Stato iniziale: `cataloged`
- Fonte: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Pagina: `4`
- Parte: `Domanda facoltativa premiale`
- Punti: `3`
- Titolo: `Domande facoltative sui matroidi`
- Argomento principale: `matroidi`
- Argomenti secondari:
  - `greedy`
  - `sistemi di indipendenza`
  - `foreste`
  - `correttezza`
- Tipo richiesta:
  - dimostrazione teorica a scelta tra due alternative.
- Metodo probabile:
  - `[[metodo_dimostrazione_greedy_matroidi]]`
  - `[[metodo_dimostrare_matroide_foreste]]`
- Teoria collegata:
  - `[[matroidi]]`
  - `[[algoritmi_greedy]]`
  - `[[foreste]]`
- Pattern sospetto:
  - `domanda teorica bonus sui matroidi`
- Difficoltà stimata: `alta`
- Priorità: `media`
- Note:
  - Essendo facoltativa, va catalogata separatamente dagli esercizi principali.
  - Utile per ripasso avanzato, ma non prioritaria rispetto ai pattern ricorrenti principali.

Contenuto file consigliato:

```md
---
type: exercise
source: 01_sources/exams_raw/esame_apa_12_01_2026.pdf
exam_date: 2026-01-12
part: Domanda facoltativa premiale
exercise_number: bonus
points: 3
status: cataloged
difficulty: alta
tags:
  - topic/matroidi
  - topic/greedy
  - topic/correttezza
  - status/cataloged
---

# Exam 2026-01-12 — Bonus Matroidi

## Testo essenziale

Domanda facoltativa premiale: scegliere una sola tra due dimostrazioni.

1. Se $(E,F)$ è un matroide, dimostrare che `Greedy(E,F,w)` restituisce una soluzione ottima per ogni funzione peso ammessa.
2. Dato un grafo non orientato $G=(V,E)$ e $F=\{A \subseteq E : (V,A) \text{ è una foresta}\}$, dimostrare che $(E,F)$ è un matroide.

## Classificazione

- Argomento: [[matroidi]]
- Metodo probabile:
  - [[metodo_dimostrazione_greedy_matroidi]]
  - [[metodo_dimostrare_matroide_foreste]]
- Pattern: [[domanda_teorica_matroidi]]

## Stato

- [ ] Trascritto
- [ ] Catalogato
- [ ] Risolto
- [ ] Verificato
```

---

## 7. Metodi da creare o aggiornare

### 7.1 Metodi ad alta priorità

Codex deve creare se assenti:

```txt
04_methods/metodo_programmazione_dinamica_zaino_01.md
04_methods/metodo_ricostruzione_soluzione_dp.md
04_methods/metodo_dp_cammini_con_parita.md
04_methods/metodo_kruskal_mst.md
04_methods/metodo_riduzione_clique_vertex_cover.md
04_methods/metodo_dimostrare_np_completezza.md
```

### 7.2 Metodi a priorità media

```txt
04_methods/metodo_dimostrazione_greedy_matroidi.md
04_methods/metodo_dimostrare_matroide_foreste.md
```

### 7.3 Contenuto minimo consigliato per i metodi

Per ora non scrivere una dispensa completa. Creare solo note scaffold con:

```md
---
type: method
status: scaffold
tags:
  - method
---

# Nome metodo

## Quando si usa

## Schema ricorrente

## Esercizi collegati

## Teoria necessaria

## Errori comuni

> [!Warning]
> Metodo da completare dopo analisi di altri appelli o degli appunti.
```

---

## 8. Teoria da creare o aggiornare

Creare o aggiornare, se assenti:

```txt
05_theory/programmazione_dinamica.md
05_theory/zaino_01.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/grafi.md
05_theory/minimum_spanning_tree.md
05_theory/kruskal.md
05_theory/np_completezza.md
05_theory/clique.md
05_theory/vertex_cover.md
05_theory/riduzioni_polinomiali.md
05_theory/matroidi.md
```

> [!Important]
> In questa fase creare solo teoria minima collegata agli esercizi.
> Non generare una dispensa teorica lunga e generica.

---

## 9. Pattern d'esame da aggiornare

Aggiornare:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/recurring_theory_questions.md
06_exam_patterns/high_yield_topics.md
```

### 9.1 Pattern esercizi ricorrenti

Aggiungere o aggiornare:

```md
## DP — Definizione coefficienti, casi base e ricorrenza

- Esercizi collegati:
  - [[exam_2026_01_12_e01]]
  - [[exam_2026_01_12_e02]]
  - [[exam_2026_01_12_e05]]
- Frequenza osservata: `1 appello`
- Priorità: `altissima`
- Descrizione:
  - Il compito chiede spesso di impostare la programmazione dinamica formalmente, non solo di dare il risultato.
  - Ricorrono: coefficienti, caso base, passo ricorsivo, soluzione finale e talvolta ricostruzione.

## Zaino 0/1

- Esercizi collegati:
  - [[exam_2026_01_12_e01]]
  - [[exam_2026_01_12_e05]]
- Frequenza osservata: `1 appello`
- Priorità: `altissima`
- Varianti:
  - versione classica;
  - versione con vincolo aggiuntivo di presenza di un oggetto rosso.

## DP su grafi e proprietà dei cammini

- Esercizi collegati:
  - [[exam_2026_01_12_e02]]
- Frequenza osservata: `1 appello`
- Priorità: `alta`

## Simulazione Kruskal / MST

- Esercizi collegati:
  - [[exam_2026_01_12_e03]]
- Frequenza osservata: `1 appello`
- Priorità: `alta`

## Riduzioni CLIQUE / VERTEX-COVER

- Esercizi collegati:
  - [[exam_2026_01_12_e04]]
  - [[exam_2026_01_12_e06]]
- Frequenza osservata: `1 appello`
- Priorità: `altissima`

## Dimostrazione NP-completezza

- Esercizi collegati:
  - [[exam_2026_01_12_e06]]
- Frequenza osservata: `1 appello`
- Priorità: `altissima`

## Matroidi e greedy

- Esercizi collegati:
  - [[exam_2026_01_12_bonus_matroidi]]
- Frequenza osservata: `1 appello`
- Priorità: `media`
```

### 9.2 Domande teoriche ricorrenti

Aggiungere a `06_exam_patterns/recurring_theory_questions.md`:

```md
## CLIQUE è NP-completo

- Collegato a:
  - [[exam_2026_01_12_e06]]
- Richiesta tipica:
  - dimostrare appartenenza a NP;
  - dimostrare NP-hardness tramite riduzione.
- Priorità: `altissima`

## Teorema greedy per matroidi

- Collegato a:
  - [[exam_2026_01_12_bonus_matroidi]]
- Richiesta tipica:
  - dimostrare correttezza dell'algoritmo greedy su matroidi.
- Priorità: `media`

## Foreste come matroide grafico

- Collegato a:
  - [[exam_2026_01_12_bonus_matroidi]]
- Richiesta tipica:
  - dimostrare che l'insieme delle foreste forma un matroide.
- Priorità: `media`
```

---

## 10. Indici da aggiornare

Aggiornare o creare:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

### 10.1 `index_by_exam.md`

Aggiungere:

```md
## 2026-01-12

| Esercizio | Parte | Argomento | Punti | Difficoltà | Stato |
|---|---|---|---:|---|---|
| [[exam_2026_01_12_e01]] | Parte I | DP zaino 0/1 con vincolo colore rosso | 31 | alta | cataloged |
| [[exam_2026_01_12_e02]] | Parte I | DP cammini pari in grafo | 31 | alta | cataloged |
| [[exam_2026_01_12_e03]] | Parte II | Kruskal MST | 6 | bassa-media | cataloged |
| [[exam_2026_01_12_e04]] | Parte II | Riduzioni CLIQUE/VERTEX-COVER | 6 | media | cataloged |
| [[exam_2026_01_12_e05]] | Parte II | Ricorrenza zaino 0/1 | 7 | bassa-media | cataloged |
| [[exam_2026_01_12_e06]] | Parte II | CLIQUE NP-completo | 14 | alta | cataloged |
| [[exam_2026_01_12_bonus_matroidi]] | Bonus | Matroidi | 3 | alta | cataloged |
```

### 10.2 `index_by_topic.md`

Aggiungere sotto i topic pertinenti:

```md
## Programmazione dinamica

- [[exam_2026_01_12_e01]] — zaino 0/1 con vincolo colore rosso
- [[exam_2026_01_12_e02]] — cammini pari in grafo
- [[exam_2026_01_12_e05]] — ricorrenza zaino 0/1

## Zaino 0/1

- [[exam_2026_01_12_e01]]
- [[exam_2026_01_12_e05]]

## Grafi

- [[exam_2026_01_12_e02]]
- [[exam_2026_01_12_e03]]
- [[exam_2026_01_12_e04]]

## Greedy / MST

- [[exam_2026_01_12_e03]]

## NP-completezza

- [[exam_2026_01_12_e04]]
- [[exam_2026_01_12_e06]]

## Matroidi

- [[exam_2026_01_12_bonus_matroidi]]
```

### 10.3 `index_by_difficulty.md`

Aggiungere:

```md
## Alta

- [[exam_2026_01_12_e01]]
- [[exam_2026_01_12_e02]]
- [[exam_2026_01_12_e06]]
- [[exam_2026_01_12_bonus_matroidi]]

## Media

- [[exam_2026_01_12_e04]]

## Bassa-media

- [[exam_2026_01_12_e03]]
- [[exam_2026_01_12_e05]]
```

---

## 11. Esempi svolti da creare

Non creare ancora soluzioni complete, salvo scaffold.

Possibili file futuri:

```txt
07_solved_examples/solved_exam_2026_01_12_e05_zaino_01.md
07_solved_examples/solved_exam_2026_01_12_e03_kruskal.md
07_solved_examples/solved_exam_2026_01_12_e06_clique_np_completo.md
```

Priorità consigliata per prossima fase di soluzione:

1. `exam_2026_01_12_e05` — zaino 0/1 classico, perché è base per `e01`;
2. `exam_2026_01_12_e01` — variante con vincolo rosso;
3. `exam_2026_01_12_e03` — Kruskal, veloce e standard;
4. `exam_2026_01_12_e04` + `e06` — riduzioni e NP-completezza;
5. `exam_2026_01_12_e02` — DP grafi con parità;
6. `exam_2026_01_12_bonus_matroidi` — solo dopo pattern principali.

---

## 12. Dubbi e parti da verificare

> [!Warning]
> Il PDF è una scansione. La trascrizione è stata fatta da lettura visuale delle pagine.
> Alcuni dettagli grafici o simbolici possono richiedere verifica manuale.

Punti da verificare:

- In `exam_2026_01_12_e02`, verificare la notazione attesa dal docente per la DP sui cammini pari.
- In `exam_2026_01_12_e04`, verificare il protocollo esatto del corso per i turni `AL` e `MZ`.
- In `exam_2026_01_12_bonus_matroidi`, verificare se nella funzione peso del primo quesito il testo ammette sia $w:E \to \mathbb{R}^+ \cup \{0\}$ sia $w:E \to \mathbb{R}$.
- In `exam_2026_01_12_e01`, verificare se il vincolo "presenza del rosso" deve essere gestito con coefficiente booleano o con altra codifica preferita dal corso.

---

## 13. Istruzioni operative per Codex

Codex deve:

1. Creare, se assente:

```txt
09_ingestion_reports/
```

2. Salvare questo report come:

```txt
09_ingestion_reports/ingestion_report_exam_2026_01_12.md
```

3. Creare, se assente:

```txt
02_transcriptions/exams/
03_exercise_catalog/exercises/
```

4. Creare la trascrizione:

```txt
02_transcriptions/exams/exam_2026_01_12.md
```

5. Creare i file esercizio:

```txt
03_exercise_catalog/exercises/exam_2026_01_12_e01.md
03_exercise_catalog/exercises/exam_2026_01_12_e02.md
03_exercise_catalog/exercises/exam_2026_01_12_e03.md
03_exercise_catalog/exercises/exam_2026_01_12_e04.md
03_exercise_catalog/exercises/exam_2026_01_12_e05.md
03_exercise_catalog/exercises/exam_2026_01_12_e06.md
03_exercise_catalog/exercises/exam_2026_01_12_bonus_matroidi.md
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
06_exam_patterns/recurring_theory_questions.md
06_exam_patterns/high_yield_topics.md
```

8. Creare scaffold dei metodi mancanti in:

```txt
04_methods/
```

9. Creare scaffold della teoria minima mancante in:

```txt
05_theory/
```

10. Aggiornare `PROJECT_STATUS.md`:

```md
## Stato aggiornato

- Primo appello analizzato: `01_sources/exams_raw/esame_apa_12_01_2026.pdf`
- Report creato: `09_ingestion_reports/ingestion_report_exam_2026_01_12.md`
- Trascrizione prevista: `02_transcriptions/exams/exam_2026_01_12.md`
- Esercizi catalogati: `7` inclusa domanda bonus
- Stato: `appello catalogato`
```

11. Aggiornare `TODO.md`:

```md
## Prossimi step

- [ ] Verificare manualmente trascrizione dell'appello `2026-01-12`
- [ ] Risolvere `exam_2026_01_12_e05` come base per zaino 0/1
- [ ] Risolvere `exam_2026_01_12_e01` come variante con vincolo rosso
- [ ] Risolvere `exam_2026_01_12_e03` Kruskal
- [ ] Risolvere `exam_2026_01_12_e04` riduzione CLIQUE/VERTEX-COVER
- [ ] Risolvere `exam_2026_01_12_e06` CLIQUE NP-completo
- [ ] Analizzare prossimo PDF in `01_sources/exams_raw/`
```

---

## 14. Definition of Done

Questo ingestion report è considerato completo quando Codex ha:

- [ ] creato il file report nella repo;
- [ ] creato la trascrizione essenziale dell'appello;
- [ ] creato tutti i file esercizio;
- [ ] aggiornato gli indici per esame, topic e difficoltà;
- [ ] aggiornato i pattern d'esame;
- [ ] creato scaffold dei metodi mancanti;
- [ ] creato scaffold della teoria minima mancante;
- [ ] aggiornato `PROJECT_STATUS.md`;
- [ ] aggiornato `TODO.md`;
- [ ] lasciato come `Warning` le parti non ancora risolte o da verificare.

---

## 15. Prossima azione consigliata

Dopo applicazione del report da parte di Codex:

1. fare commit della repo;
2. verificare link Obsidian;
3. risolvere prima `exam_2026_01_12_e05`, perché è la base dello zaino 0/1;
4. usare la soluzione di `e05` per completare `e01`;
5. poi passare al prossimo appello raw in `01_sources/exams_raw/`.
