# Continuity Context — knowledge_base_APA dopo completamento PDF Parte I

> [!Info]
> Questo file serve come contesto da passare a una nuova chat quando si continua il progetto `knowledge_base_APA`.
>
> Stato importante: **i PDF della Parte I sono stati completati nella fase di ingestion/reporting**.  
> La prossima fase deve passare ai PDF della **Parte II**.

---

## 1. Repository di riferimento

Repository GitHub:

```txt
https://github.com/DreoXDev/knowledge_base_APA
```

Pagina commit:

```txt
https://github.com/DreoXDev/knowledge_base_APA/commits/master/
```

La repo contiene una knowledge base Obsidian per preparare l'esame:

```txt
Analisi e Progettazione di Algoritmi
Università di Milano-Bicocca
```

---

## 2. Obiettivo generale del progetto

L'obiettivo è costruire una knowledge base in Markdown compatibile con Obsidian per preparare l'esame tramite:

```txt
Appelli passati
    ↓
Trascrizione essenziale
    ↓
Catalogo esercizi
    ↓
Pattern ricorrenti
    ↓
Metodi risolutivi
    ↓
Teoria necessaria
    ↓
Esempi svolti
    ↓
Ripasso finale
```

La strategia decisa è:

1. analizzare prima gli appelli raw;
2. trascriverli in modo leggero ma utile;
3. catalogare tutti gli esercizi;
4. estrarre pattern ricorrenti;
5. solo dopo analizzare appunti e materiali teorici;
6. usare gli appunti per completare metodi, soluzioni e teoria;
7. creare soluzioni strutturate per gli esercizi non coperti direttamente dagli appunti;
8. rifinire la teoria solo in base a ciò che serve davvero negli appelli.

> [!Summary]
> Gli appelli dicono **cosa viene chiesto davvero**.  
> Gli appunti dicono **come risolverlo**.

---

## 3. Workflow operativo scelto

Il workflow operativo usato finora è:

```txt
PDF sorgente
    ↓
lettura / interpretazione da parte della chat AI
    ↓
creazione di un ingestion report Markdown
    ↓
Codex applica il report alla knowledge base
    ↓
repo aggiornata e coerente
```

La chat AI deve:

1. leggere un PDF alla volta;
2. interpretare il contenuto;
3. distinguere testo certo da testo dubbio;
4. identificare esercizi, argomenti, teoria e pattern;
5. creare un piano/report `.md` scaricabile;
6. indicare esattamente a Codex:
   - file da creare;
   - file da aggiornare;
   - indici da modificare;
   - parti dubbie;
   - contenuti da non inventare.

Codex deve:

1. leggere il piano/report;
2. creare o aggiornare i file della knowledge base;
3. mantenere link Obsidian coerenti;
4. aggiornare indici, pattern, `PROJECT_STATUS.md` e `TODO.md`;
5. non inventare contenuti mancanti;
6. segnare con `[!Warning]` ciò che è incerto.

> [!Important]
> Codex non deve essere usato come lettore principale dei PDF manoscritti o complessi.
>
> Codex deve ricevere report chiari e applicarli.

---

## 4. Stato attuale della fase Parte I

La fase di analisi dei PDF della **Parte I** è da considerare completata a livello di:

```txt
lettura PDF
    ↓
analisi contenuto
    ↓
piano/report per Codex
```

Sono stati generati piani Markdown scaricabili per tutti i PDF Parte I caricati nella chat.

La prossima chat deve partire dal presupposto che:

```txt
I PDF della Parte I sono finiti.
Il prossimo blocco riguarda i PDF della Parte II.
```

> [!Warning]
> Prima di iniziare davvero la Parte II, può essere utile chiedere a Codex o alla chat di controllare che tutti i piani della Parte I siano stati applicati alla repo senza duplicazioni, link rotti o incoerenze negli indici.

---

## 5. Appelli Parte I analizzati prima di questa fase

Dal contesto precedente risultavano già analizzati/catalogati:

| Appello | File PDF | Esercizi | Stato |
|---|---|---:|---|
| 2026-01-12 | `esame_apa_12_01_2026.pdf` | 7 | catalogato |
| 2025-07-03 Parte I | `parteI-03lug25.pdf` | 2 | catalogato |
| 2025-06-09 Parte I | `parteI-09giu25.pdf` | 2 | catalogato |

Pattern già emersi prima di questa fase:

```txt
- DP formale con coefficienti, caso base, passo ricorsivo.
- LCS con vincoli aggiuntivi.
- DP booleana su grafi con stato esteso.
- Kruskal / MST.
- Riduzioni CLIQUE / VERTEX-COVER.
- Dimostrazione NP-completezza.
- Matroidi e greedy.
```

---

## 6. Nuovi appelli Parte I analizzati in questa chat

In questa chat sono stati analizzati i seguenti PDF Parte I e per ciascuno è stato generato un piano Markdown scaricabile per Codex.

---

### 6.1 Appello 2025-11-10 — Parte I Tema A

PDF:

```txt
parte-I-10nov25-A.pdf
```

Piano generato:

```txt
piano_codex_ingestion_APA_2025_11_10_part1_tema_a.md
```

File attesi nella repo dopo applicazione Codex:

```txt
09_ingestion_reports/ingestion_report_exam_2025_11_10_part1_tema_a.md
02_transcriptions/exams/exam_2025_11_10_part1_tema_a.md
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e01.md
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e02.md
```

Contenuto:

1. `exam_2025_11_10_p1_tema_a_e01`
   - LCS tra due sequenze con vincolo di presenza obbligatoria di almeno un simbolo rosso.
2. `exam_2025_11_10_p1_tema_a_e02`
   - DP su grafo con archi etichettati A/B/C.
   - Per ogni coppia `(i,j)`, stabilire se esiste un cammino con `#A + #B = 3`.

Pattern:

```txt
- LCS con presenza obbligatoria di un colore.
- DP su grafi con conteggio aggregato.
- Cammini con vincolo esatto sul numero di archi di certi tipi.
```

---

### 6.2 Appello 2025-02-11 — Parte I scritto completo

PDF:

```txt
parteI-11feb25-completo.pdf
```

Piano generato:

```txt
piano_codex_ingestion_APA_2025_02_11_part1_completo.md
```

File attesi nella repo dopo applicazione Codex:

```txt
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_completo.md
02_transcriptions/exams/exam_2025_02_11_part1_completo.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e01.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e02.md
```

Contenuto:

1. `exam_2025_02_11_p1_completo_e01`
   - LCS comune a tre sequenze con al massimo due simboli rossi.
2. `exam_2025_02_11_p1_completo_e02`
   - DP su grafo colorato.
   - Per ogni coppia `(i,j)`, stabilire se esiste un cammino senza due archi consecutivi neri e senza due archi consecutivi blu.

Pattern:

```txt
- LCS a tre sequenze.
- LCS con budget su colore.
- DP su grafi con vincoli locali di consecutività.
- Necessità di problema ausiliario con informazione sui colori estremi del cammino.
```

---

### 6.3 Appello 2025-02-11 — Parte I recupero parziale

PDF:

```txt
parteI-11feb25-recupero.pdf
```

Piano generato:

```txt
piano_codex_ingestion_APA_2025_02_11_part1_recupero.md
```

File attesi nella repo dopo applicazione Codex:

```txt
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_recupero.md
02_transcriptions/exams/exam_2025_02_11_part1_recupero.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e01.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e02.md
```

Contenuto:

1. `exam_2025_02_11_p1_recupero_e01`
   - LCS comune a tre sequenze con al massimo due simboli rossi.
   - È sostanzialmente uguale all'esercizio 1 dello scritto completo dell'11 febbraio 2025.
2. `exam_2025_02_11_p1_recupero_e02`
   - Grafo pesato sugli archi, senza cappi e senza cicli di peso negativo.
   - Ogni vertice ha colore rosso/nero.
   - Ogni arco ha colore marrone/blu.
   - Per ogni coppia `(i,j)`, calcolare il peso di un cammino minimo tale che:
     - il numero di archi blu sia dispari;
     - non vi siano due vertici consecutivi rossi.

Pattern:

```txt
- Deduplicazione del metodo LCS a tre sequenze con massimo due rossi.
- Cammini minimi vincolati.
- Floyd-Warshall con stato esteso.
- Stato di parità per archi blu.
- Vincolo locale sui vertici consecutivi.
```

> [!Important]
> Questo appello è importante perché sposta la famiglia “DP su grafi” dal caso booleano/esistenza al caso di ottimizzazione con cammini minimi.

---

### 6.4 Appello 2025-01-13 — Parte I

PDF:

```txt
parteI-13gen25.pdf
```

Piano generato:

```txt
piano_codex_ingestion_APA_2025_01_13_part1.md
```

File attesi nella repo dopo applicazione Codex:

```txt
09_ingestion_reports/ingestion_report_exam_2025_01_13_part1.md
02_transcriptions/exams/exam_2025_01_13_part1.md
03_exercise_catalog/exercises/exam_2025_01_13_p1_e01.md
03_exercise_catalog/exercises/exam_2025_01_13_p1_e02.md
```

Contenuto:

1. `exam_2025_01_13_p1_e01`
   - LCS tra due sequenze con:
     - al massimo 3 simboli rossi;
     - al massimo 2 simboli blu.
2. `exam_2025_01_13_p1_e02`
   - DP su grafo colorato.
   - Stabilire se esiste un cammino in cui:
     - un arco nero non è mai seguito da un arco rosso;
     - un arco rosso non è mai seguito da un arco blu.

Pattern:

```txt
- LCS con budget multipli sui colori.
- DP su grafi con vincoli di precedenza tra colori.
- L'ordine conta: vietato (N,R), vietato (R,B).
```

---

### 6.5 Appello 2025-09-17 — Parte I

PDF:

```txt
parteI-17set25.pdf
```

Piano generato:

```txt
piano_codex_ingestion_APA_2025_09_17_part1.md
```

File attesi nella repo dopo applicazione Codex:

```txt
09_ingestion_reports/ingestion_report_exam_2025_09_17_part1.md
02_transcriptions/exams/exam_2025_09_17_part1.md
03_exercise_catalog/exercises/exam_2025_09_17_p1_e01.md
03_exercise_catalog/exercises/exam_2025_09_17_p1_e02.md
```

Contenuto:

1. `exam_2025_09_17_p1_e01`
   - LCS comune a tre sequenze con al massimo 2 simboli rossi.
   - Ripete il pattern già visto negli appelli dell'11 febbraio 2025.
2. `exam_2025_09_17_p1_e02`
   - DP booleana su grafo colorato.
   - Per ogni coppia `(i,j)`, stabilire se esiste un cammino con numero dispari di archi blu.

Pattern:

```txt
- Deduplicazione del metodo LCS a tre sequenze con massimo due rossi.
- DP su grafi con stato di parità.
- Cammini con numero dispari di archi blu.
```

---

## 7. Stato complessivo appelli Parte I

Dopo questa fase, gli appelli Parte I considerati sono:

| Appello | File PDF | Esercizi | Note principali |
|---|---|---:|---|
| 2026-01-12 | `esame_apa_12_01_2026.pdf` | 7 | DP, MST, NP-completezza, matroidi |
| 2025-11-10 Parte I Tema A | `parte-I-10nov25-A.pdf` | 2 | LCS presenza rosso, grafi con `#A + #B = 3` |
| 2025-09-17 Parte I | `parteI-17set25.pdf` | 2 | LCS tre sequenze max 2 rossi, grafi parità blu |
| 2025-07-03 Parte I | `parteI-03lug25.pdf` | 2 | LCS con ingombro, grafi con 2 rossi e 2 blu |
| 2025-06-09 Parte I | `parteI-09giu25.pdf` | 2 | LCS max 2 rossi e max 3 blu, grafi con precedenze |
| 2025-02-11 Parte I completo | `parteI-11feb25-completo.pdf` | 2 | LCS tre sequenze max 2 rossi, grafi con divieto NN e BB |
| 2025-02-11 Parte I recupero | `parteI-11feb25-recupero.pdf` | 2 | LCS tre sequenze max 2 rossi, cammini minimi vincolati |
| 2025-01-13 Parte I | `parteI-13gen25.pdf` | 2 | LCS max 3 rossi e max 2 blu, grafi con precedenze |

> [!Summary]
> La Parte I è dominata dalla programmazione dinamica formale.  
> I due macro-pattern più ricorrenti sono:
>
> 1. LCS con stato esteso;
> 2. cammini su grafi con stato esteso.

---

## 8. Pattern forti emersi dalla Parte I

### 8.1 Struttura standard degli esercizi Parte I

La struttura richiesta è quasi sempre:

```txt
1. Definire i coefficienti.
2. Scrivere il caso base.
3. Scrivere il passo ricorsivo.
4. Indicare il coefficiente soluzione.
5. Scrivere algoritmo bottom-up.
6. Scrivere ricostruzione, se richiesta.
```

> [!Important]
> La Parte I richiede forma, precisione e notazione.  
> Non basta l'intuizione: bisogna saper impostare coefficienti, casi base e ricorrenze.

---

### 8.2 Famiglia LCS con vincoli

Varianti osservate:

| Appello | Variante |
|---|---|
| 2025-07-03 Parte I | LCS con vincolo di ingombro massimo $W$ |
| 2025-06-09 Parte I | LCS con massimo 2 rossi e massimo 3 blu |
| 2025-11-10 Parte I Tema A | LCS con presenza obbligatoria di almeno un rosso |
| 2025-09-17 Parte I | LCS a tre sequenze con al massimo 2 rossi |
| 2025-02-11 Parte I completo | LCS a tre sequenze con al massimo 2 rossi |
| 2025-02-11 Parte I recupero | LCS a tre sequenze con al massimo 2 rossi |
| 2025-01-13 Parte I | LCS con massimo 3 rossi e massimo 2 blu |

Pattern comune:

```txt
LCS classica
    ↓
aggiunta di una o più dimensioni allo stato
    ↓
vincolo gestito quando si decide di prendere il simbolo comune
    ↓
soluzione come coefficiente finale con budget/flag appropriato
```

---

### 8.3 Famiglia DP su grafi con stato esteso

Varianti osservate:

| Appello | Variante |
|---|---|
| 2026-01-12 | cammino con numero pari di archi |
| 2025-09-17 Parte I | cammino con numero dispari di archi blu |
| 2025-07-03 Parte I | cammino con esattamente 2 rossi e 2 blu |
| 2025-06-09 Parte I | cammino con vincoli di precedenza tra colori |
| 2025-11-10 Parte I Tema A | cammino con `#A + #B = 3` |
| 2025-02-11 Parte I completo | cammino senza due neri consecutivi e senza due blu consecutivi |
| 2025-02-11 Parte I recupero | cammino minimo con numero dispari di archi blu e senza due vertici rossi consecutivi |
| 2025-01-13 Parte I | cammino in cui nero non è seguito da rosso e rosso non è seguito da blu |

Pattern comune:

```txt
Chiusura transitiva / Floyd-Warshall
    ↓
stato esteso per proprietà del cammino
    ↓
composizione di sottocammini
    ↓
controllo di conteggi, parità, vincoli locali o vincoli di precedenza
```

---

### 8.4 Conteggi, budget e parità

Le varianti si possono raggruppare così:

```txt
Budget:
- massimo k rossi/blu in LCS;
- massimo ingombro W.

Conteggi esatti:
- esattamente 2 rossi e 2 blu;
- #A + #B = 3.

Parità:
- numero pari di archi;
- numero dispari di archi blu.

Presenza obbligatoria:
- almeno un simbolo rosso.

Vincoli locali:
- no NN;
- no BB;
- no due vertici rossi consecutivi.

Vincoli di precedenza:
- nero non seguito da rosso;
- rosso non seguito da blu.
```

---

## 9. Deduplicazioni importanti da mantenere

### 9.1 LCS a tre sequenze con massimo 2 rossi

Questo pattern compare in:

```txt
exam_2025_02_11_p1_completo_e01
exam_2025_02_11_p1_recupero_e01
exam_2025_09_17_p1_e01
```

Deve puntare a un unico metodo, ad esempio:

```txt
04_methods/metodo_lcs_tre_sequenze_vincolo_colori.md
```

Non creare tre metodi separati.

---

### 9.2 LCS con budget multipli di colore

Pattern collegati:

```txt
exam_2025_06_09_p1_e01
exam_2025_01_13_p1_e01
```

Metodo possibile:

```txt
04_methods/metodo_lcs_budget_multipli_colori.md
```

oppure consolidamento in:

```txt
04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
```

---

### 9.3 DP su grafi con parità

Pattern collegati:

```txt
exam_2026_01_12_e02
exam_2025_09_17_p1_e02
exam_2025_02_11_p1_recupero_e02
```

Metodo possibile:

```txt
04_methods/metodo_dp_cammini_colori_parita.md
04_methods/metodo_floyd_warshall_stato_esteso.md
```

---

## 10. Quality check consigliato prima di passare alla Parte II

Prima di iniziare la Parte II, far fare a Codex un controllo leggero.

Obiettivo:

```txt
Non rifare l'applicazione dei report.
Non duplicare esercizi.
Fare solo controllo qualità su link, nomi file, indici, pattern, metodi, teoria, accenti, PROJECT_STATUS e TODO.
```

Controlli consigliati:

```bash
find . -name "*2025_11_10*"
find . -name "*2025_09_17*"
find . -name "*2025_02_11*"
find . -name "*2025_01_13*"

grep -R "exam_2025_11_10" .
grep -R "exam_2025_09_17" .
grep -R "exam_2025_02_11" .
grep -R "exam_2025_01_13" .
```

Verificare che esistano:

```txt
09_ingestion_reports/ingestion_report_exam_2025_11_10_part1_tema_a.md
09_ingestion_reports/ingestion_report_exam_2025_09_17_part1.md
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_completo.md
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_recupero.md
09_ingestion_reports/ingestion_report_exam_2025_01_13_part1.md
```

Verificare che gli indici siano aggiornati:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

Verificare che i pattern siano aggiornati:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
06_exam_patterns/parte_i_dynamic_programming_patterns.md
```

Verificare che `PROJECT_STATUS.md` dica chiaramente:

```txt
Parte I: PDF analizzati / ingestion reports generati / in applicazione o applicati
Prossima fase: Parte II
```

---

## 11. Prossima fase: Parte II

La prossima chat deve iniziare l'analisi dei PDF della **Parte II**.

### 11.1 Obiettivo della Parte II

Per ogni PDF Parte II:

1. leggere il PDF;
2. identificare gli esercizi;
3. capire se sono teoria, dimostrazioni, NP-completezza, greedy, grafi, MST, matroidi, complessità, ricorrenze o altro;
4. creare un piano/report Markdown scaricabile per Codex;
5. aggiornare la KB mantenendo coerenza con la Parte I, ma separando chiaramente i pattern.

### 11.2 Possibili differenze rispetto alla Parte I

La Parte I era fortemente centrata su:

```txt
programmazione dinamica formale
```

La Parte II potrebbe essere più centrata su:

```txt
- NP-completezza;
- riduzioni;
- greedy;
- MST;
- matroidi;
- complessità;
- dimostrazioni teoriche;
- algoritmi classici;
- correttezza;
- ricorrenze;
- analisi di algoritmi.
```

> [!Warning]
> Non assumere che la Parte II abbia la stessa struttura della Parte I.
>
> Per ogni PDF Parte II bisogna prima leggere il testo e solo dopo definire pattern e metodo.

---

## 12. Naming consigliato per la Parte II

Se un PDF è chiaramente Parte II, usare naming coerente:

```txt
exam_YYYY_MM_DD_part2.md
exam_YYYY_MM_DD_p2_e01.md
exam_YYYY_MM_DD_p2_e02.md
```

Per ingestion report:

```txt
ingestion_report_exam_YYYY_MM_DD_part2.md
```

Se il PDF ha varianti tipo tema A/B, recupero, completo:

```txt
exam_YYYY_MM_DD_part2_tema_a.md
exam_YYYY_MM_DD_part2_recupero.md
exam_YYYY_MM_DD_part2_completo.md
```

Esercizi:

```txt
exam_YYYY_MM_DD_p2_tema_a_e01.md
exam_YYYY_MM_DD_p2_recupero_e01.md
exam_YYYY_MM_DD_p2_completo_e01.md
```

---

## 13. Struttura dei piani per Codex da continuare a usare

Per ogni nuovo PDF Parte II, generare un file `.md` con questa struttura:

```md
# Piano Codex — Ingestion appello APA YYYY-MM-DD Parte II

## Obiettivo

## 1. File da creare

## 2. File da aggiornare

## 3. Trascrizione essenziale dell'appello

## 4. Esercizio 1 — Catalogazione

## 5. Esercizio 2 — Catalogazione

## 6. Pattern da aggiornare

## 7. Differenze rispetto agli appelli già analizzati

## 8. Note metodologiche importanti

## 9. Aggiornare PROJECT_STATUS.md

## 10. Aggiornare TODO.md

## 11. Commit consigliato

## 12. Stato atteso finale

## 13. Nota finale per Codex
```

Adattare il numero di sezioni/esercizi al contenuto effettivo del PDF.

---

## 14. File e directory principali della repo

Struttura principale attesa:

```txt
00_meta/
01_sources/
02_transcriptions/
03_exercise_catalog/
04_methods/
05_theory/
06_exam_patterns/
07_solved_examples/
08_review/
09_ingestion_reports/
PDF/
templates/
plans/
AI_CONTEXT.md
PROJECT_STATUS.md
README.md
TODO.md
```

Fonti PDF:

```txt
01_sources/exams_raw/
01_sources/notes_raw/
01_sources/extra_materials/
```

---

## 15. Regole di stile Markdown / Obsidian

Continuare a usare:

```md
[[link interni]]
```

Callout Obsidian:

```md
> [!Info]
> ...

> [!Warning]
> ...

> [!Question]
> ...

> [!Example]
> ...

> [!Summary]
> ...
```

Formule inline:

```md
$O(n \log n)$
```

Formule block:

```md
$$
T(n) = 2T(n/2) + n
$$
```

No emoji nei file Markdown, salvo richiesta esplicita.

---

## 16. Stati standard

Per fonti:

```txt
da analizzare
in analisi
report creato
applicato
da verificare
completo
```

Per note:

```txt
raw
transcribed
interpreted
cataloged
solved
verified
complete
```

Per ingestion report:

```txt
draft
ready_for_codex
applied
needs_review
```

---

## 17. Prompt da usare nella prossima chat

```txt
Sto continuando il progetto knowledge_base_APA:

https://github.com/DreoXDev/knowledge_base_APA

L'obiettivo è creare una knowledge base Obsidian per preparare l'esame “Analisi e Progettazione di Algoritmi” dell'Università di Milano-Bicocca usando appelli passati e appunti PDF.

La fase dei PDF della Parte I è finita:
- sono stati analizzati gli appelli Parte I disponibili;
- sono stati generati piani Markdown per Codex;
- i pattern principali della Parte I sono LCS con vincoli e DP su grafi con stato esteso.

Ora dobbiamo iniziare la fase dei PDF della Parte II.

Workflow:
1. ti mando un PDF Parte II alla volta;
2. lo analizzi;
3. estrai esercizi, argomenti, pattern e parti dubbie;
4. generi un piano/report Markdown scaricabile per Codex;
5. il piano deve indicare file da creare, file da aggiornare, pattern da modificare, TODO e stato progetto;
6. non inventare contenuti mancanti;
7. mantieni stile Obsidian con link interni, callout e formule LaTeX.

Prima di iniziare, considera che può essere utile fare o richiedere un quality check della repo per verificare che i piani della Parte I siano stati applicati senza duplicazioni.
```

---

## 18. Formula mentale da mantenere

> [!Summary]
> Ogni informazione deve rientrare in questa catena:

```txt
Fonte PDF
    ↓
Ingestion report
    ↓
Trascrizione / esercizio catalogato
    ↓
Pattern
    ↓
Metodo
    ↓
Teoria necessaria
    ↓
Esempio svolto
    ↓
Ripasso finale
```

Se una nota non si collega a questa catena, probabilmente è troppo generica o fuori priorità.

---

## 19. Priorità immediata nella prossima chat

La prossima chat dovrebbe fare una di queste due cose:

### Opzione A — Quality check Parte I

Se Codex ha già applicato i piani Parte I, controllare la repo e generare un piano di fix se ci sono:

```txt
- duplicazioni;
- link rotti;
- indici non aggiornati;
- pattern mancanti;
- naming incoerente.
```

### Opzione B — Inizio Parte II

Se si vuole procedere subito:

```txt
Caricare il primo PDF della Parte II.
Analizzarlo.
Generare il piano Codex come fatto per la Parte I.
```

> [!Important]
> Da questo punto in poi, non continuare ad assumere che gli esercizi siano DP: la Parte II potrebbe avere pattern molto diversi.
