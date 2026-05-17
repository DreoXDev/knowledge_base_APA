# Piano Codex — Ingestion appello APA 2025-09-17 Parte I

## Obiettivo

Integrare nella knowledge base APA l'appello:

```txt
Analisi e Progetto di Algoritmi — Parte I
Data: 17 settembre 2025
File sorgente: parteI-17set25.pdf
```

L'appello contiene 2 esercizi di programmazione dinamica:

1. LCS comune a tre sequenze con vincolo di al massimo 2 simboli rossi.
2. DP booleana su grafo colorato per stabilire, per ogni coppia di vertici, se esiste un cammino con numero dispari di archi blu.

> [!Important]
> L'esercizio 1 coincide con il pattern già visto in:
>
> - `parteI-11feb25-completo.pdf`;
> - `parteI-11feb25-recupero.pdf`.
>
> Codex deve quindi trattarlo come ripetizione/conferma del pattern, evitando duplicazioni metodologiche.

Questo appello va integrato nella KB collegandolo ai pattern già emersi:

- LCS a tre sequenze;
- LCS con vincolo di budget sui colori;
- programmazione dinamica con stato esteso;
- DP booleana su grafi colorati;
- cammini con vincolo di parità;
- Parte I come sezione ad alta resa per esercizi formali di DP.

---

## 1. File da creare

Creare il report di ingestion:

```txt
09_ingestion_reports/ingestion_report_exam_2025_09_17_part1.md
```

Creare la trascrizione dell'appello:

```txt
02_transcriptions/exams/exam_2025_09_17_part1.md
```

Creare i due esercizi catalogati:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p1_e01.md
03_exercise_catalog/exercises/exam_2025_09_17_p1_e02.md
```

---

## 2. File da aggiornare

Aggiornare gli indici:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

Aggiornare i pattern:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
06_exam_patterns/parte_i_dynamic_programming_patterns.md
```

Aggiornare metodi già esistenti, senza duplicare:

```txt
04_methods/metodo_lcs_tre_sequenze_vincolo_colori.md
04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
```

Creare o aggiornare un metodo per la DP su grafi con parità:

```txt
04_methods/metodo_dp_cammini_colori_parita.md
```

Eventualmente aggiornare, se già esistente:

```txt
04_methods/metodo_dp_cammini_colori_conteggi.md
04_methods/metodo_floyd_warshall_stato_esteso.md
```

Aggiornare teoria minima:

```txt
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/vincoli_su_colori.md
05_theory/grafi_colorati.md
05_theory/cammini_su_grafi.md
```

Aggiornare stato progetto:

```txt
PROJECT_STATUS.md
TODO.md
01_sources/source_inventory.md
```

---

## 3. Trascrizione essenziale dell'appello

Nel file:

```txt
02_transcriptions/exams/exam_2025_09_17_part1.md
```

inserire una trascrizione leggera, non verbosa, con questa struttura:

```md
# Appello 2025-09-17 — Parte I

> [!Info]
> Fonte: `parteI-17set25.pdf`
> Stato: transcribed
> Tipo: appello Parte I
> Argomenti principali: programmazione dinamica, LCS a tre sequenze, vincoli sui colori, cammini su grafi colorati, parità

## Esercizio 1 — LCS a tre sequenze con al massimo 2 rossi

Date tre sequenze:

$$
X = \langle x_1,\dots,x_m \rangle
$$

$$
Y = \langle y_1,\dots,y_n \rangle
$$

$$
W = \langle w_1,\dots,w_d \rangle
$$

su un alfabeto $S$, ogni simbolo ha colore:

$$
col:S \to \{R,B,N\}
$$

Si vuole determinare una più lunga sottosequenza comune di $X$, $Y$ e $W$ nella quale vi siano al massimo 2 simboli rossi.

Richieste:
1. coefficienti;
2. caso base;
3. passo ricorsivo;
4. coefficiente che fornisce il valore ottimo;
5. algoritmo bottom-up;
6. algoritmo ricorsivo di ricostruzione.

> [!Note]
> Questo esercizio coincide con il pattern della LCS a tre sequenze con massimo 2 rossi già comparso negli appelli dell'11 febbraio 2025.

## Esercizio 2 — Cammini con numero dispari di archi blu

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha colore:

$$
col:E \to C
$$

dove:

$$
C = \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ nel quale vi è un numero dispari di archi blu.

Richieste:
1. coefficienti;
2. caso base;
3. passo ricorsivo;
4. soluzione del problema.
```

---

## 4. Esercizio 1 — Catalogazione

Creare:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p1_e01.md
```

Contenuto consigliato:

```md
# exam_2025_09_17_p1_e01 — LCS a tre sequenze con al massimo 2 rossi

> [!Info]
> Fonte: [[exam_2025_09_17_part1]]
> Stato: cataloged
> Tipologia: programmazione dinamica su sequenze
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_lcs_tre_sequenze_vincolo_colori]]

## Problema

Date tre sequenze $X$, $Y$ e $W$ su un alfabeto $S$, ogni simbolo ha colore rosso, blu o nero tramite:

$$
col:S \to \{R,B,N\}
$$

Si vuole trovare una sottosequenza comune di lunghezza massima tra $X$, $Y$ e $W$ che contenga al massimo 2 simboli rossi.

## Nota di duplicazione controllata

Questo esercizio coincide con lo stesso pattern già osservato in:

```txt
exam_2025_02_11_p1_completo_e01
exam_2025_02_11_p1_recupero_e01
```

Non creare un nuovo metodo separato se `metodo_lcs_tre_sequenze_vincolo_colori.md` esiste già.

## Coefficienti consigliati

Definire:

$$
C[i,j,k,r]
$$

dove:

- $0 \le i \le m$;
- $0 \le j \le n$;
- $0 \le k \le d$;
- $r \in \{0,1,2\}$.

$C[i,j,k,r]$ è la lunghezza massima di una sottosequenza comune tra i prefissi $X_i$, $Y_j$, $W_k$ che usa al massimo $r$ simboli rossi.

## Caso base

Se almeno una sequenza è vuota:

$$
C[0,j,k,r] = 0
$$

$$
C[i,0,k,r] = 0
$$

$$
C[i,j,0,r] = 0
$$

per ogni $r \in \{0,1,2\}$.

## Passo ricorsivo

Se non vale $x_i = y_j = w_k$:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r]
\end{cases}
$$

Se $x_i = y_j = w_k$ e $col(x_i) \ne R$:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r] \\
1 + C[i-1,j-1,k-1,r]
\end{cases}
$$

Se $x_i = y_j = w_k$ e $col(x_i)=R$, per $r>0$:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r] \\
1 + C[i-1,j-1,k-1,r-1]
\end{cases}
$$

Per $r=0$, il simbolo rosso non può essere preso.

## Soluzione

La lunghezza della soluzione è:

$$
C[m,n,d,2]
$$

## Collegamenti

- [[exam_2025_02_11_p1_completo_e01]]
- [[exam_2025_02_11_p1_recupero_e01]]
- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]
- [[metodo_lcs_tre_sequenze_vincolo_colori]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
```

---

## 5. Esercizio 2 — Catalogazione

Creare:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p1_e02.md
```

Contenuto consigliato:

```md
# exam_2025_09_17_p1_e02 — Cammini con numero dispari di archi blu

> [!Info]
> Fonte: [[exam_2025_09_17_part1]]
> Stato: cataloged
> Tipologia: programmazione dinamica su grafi
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_dp_cammini_colori_parita]]

## Problema

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha colore:

$$
col:E \to \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ tale che il numero di archi blu sia dispari.

Gli archi rossi e neri non cambiano la parità del numero di archi blu.

## Pattern riconosciuto

È una DP booleana su grafi colorati con stato di parità.

Rispetto alla chiusura transitiva classica, lo stato deve ricordare se il numero di archi blu usati nel cammino è:

- pari;
- dispari.

Questa variante è una forma più semplice del pattern dei cammini con conteggio/parità, già collegabile a:

- cammini con numero pari di archi;
- cammini con conteggi esatti di colori;
- cammini minimi con numero dispari di archi blu.

## Coefficienti consigliati

Numerare i vertici come:

$$
V = \{1,\dots,n\}
$$

Definire:

$$
D[k,i,j,p]
$$

dove:

- $0 \le k \le n$;
- $i,j \in V$;
- $p \in \{0,1\}$.

$D[k,i,j,p]$ è vero se e solo se esiste un cammino da $i$ a $j$ che:

- usa come vertici intermedi solo vertici in $\{1,\dots,k\}$;
- contiene un numero di archi blu con parità $p$.

Dove:

- $p=0$ indica un numero pari di archi blu;
- $p=1$ indica un numero dispari di archi blu.

## Caso base

Per $k=0$, sono ammessi solo cammini diretti e cammini vuoti.

Cammino vuoto:

$$
D[0,i,i,0] = vero
$$

$$
D[0,i,i,1] = falso
$$

Arco diretto $(i,j) \in E$:

se:

$$
col(i,j)=B
$$

allora:

$$
D[0,i,j,1] = vero
$$

se invece:

$$
col(i,j) \in \{R,N\}
$$

allora:

$$
D[0,i,j,0] = vero
$$

Tutti gli altri coefficienti sono falsi.

## Passo ricorsivo

Per $k \ge 1$:

$$
D[k,i,j,p] =
D[k-1,i,j,p]
\lor
\bigvee_{q \in \{0,1\}}
\left(
D[k-1,i,k,q]
\land
D[k-1,k,j,p \oplus q]
\right)
$$

dove $\oplus$ indica la somma modulo 2 delle parità.

Equivalentemente:

$$
D[k,i,j,0] =
D[k-1,i,j,0]
\lor
(D[k-1,i,k,0] \land D[k-1,k,j,0])
\lor
(D[k-1,i,k,1] \land D[k-1,k,j,1])
$$

$$
D[k,i,j,1] =
D[k-1,i,j,1]
\lor
(D[k-1,i,k,0] \land D[k-1,k,j,1])
\lor
(D[k-1,i,k,1] \land D[k-1,k,j,0])
$$

## Soluzione

Per ogni coppia $(i,j)$, la risposta è:

$$
D[n,i,j,1]
$$

perché $p=1$ rappresenta un numero dispari di archi blu.

## Collegamenti

- [[grafi_colorati]]
- [[cammini_su_grafi]]
- [[metodo_dp_cammini_colori_parita]]
- [[metodo_dp_cammini_colori_conteggi]]
- [[metodo_floyd_warshall_stato_esteso]]
- [[parte_i_dynamic_programming_patterns]]
```

---

## 6. Metodo da creare o aggiornare per l'esercizio 2

Creare, se non esiste già:

```txt
04_methods/metodo_dp_cammini_colori_parita.md
```

Struttura consigliata:

```md
# Metodo — DP su cammini con vincoli di parità sui colori

> [!Info]
> Stato: interpreted
> Famiglia: programmazione dinamica su grafi
> Appelli collegati:
> - [[exam_2025_09_17_p1_e02]]
> - [[exam_2025_02_11_p1_recupero_e02]]

## Quando usarlo

Usare questo metodo quando il testo chiede di stabilire se esiste un cammino con una proprietà di parità, per esempio:

- numero pari di archi;
- numero dispari di archi blu;
- parità del numero di archi di un certo colore.

## Idea

Partire da una DP tipo Floyd-Warshall e aggiungere una dimensione di stato per la parità.

Esempio:

$$
D[k,i,j,p]
$$

dove $p \in \{0,1\}$.

## Significato dello stato

$D[k,i,j,p]$ indica se esiste un cammino da $i$ a $j$ con intermedi in $\{1,\dots,k\}$ e parità $p$ rispetto alla proprietà contata.

## Caso base

- cammino vuoto con parità pari;
- arco diretto con parità dipendente dal colore o dal tipo di arco;
- stati non raggiungibili falsi.

## Passo ricorsivo

Quando si concatena un cammino da $i$ a $k$ con uno da $k$ a $j$, le parità si combinano con XOR:

$$
p = q \oplus r
$$

Quindi:

$$
D[k,i,j,p] =
D[k-1,i,j,p]
\lor
\bigvee_q
(D[k-1,i,k,q] \land D[k-1,k,j,p \oplus q])
$$

## Errori comuni

> [!Warning]
> Non basta sapere se esiste un cammino: bisogna sapere con quale parità esiste.

> [!Warning]
> Il cammino vuoto ha parità pari.

> [!Warning]
> Gli archi che non sono del colore contato non vanno ignorati: contribuiscono con parità 0.
```

---

## 7. Pattern da aggiornare

Aggiornare:

```txt
06_exam_patterns/recurring_exercise_types.md
```

aggiungendo l'appello 2025-09-17 alla famiglia:

```md
## Programmazione dinamica Parte I

Appelli collegati:

- [[exam_2026_01_12]]
- [[exam_2025_11_10_part1_tema_a]]
- [[exam_2025_09_17_part1]]
- [[exam_2025_07_03_part1]]
- [[exam_2025_06_09_part1]]
- [[exam_2025_02_11_part1_completo]]
- [[exam_2025_02_11_part1_recupero]]
- [[exam_2025_01_13_part1]]
```

Aggiornare la sezione LCS:

```md
## LCS con vincoli aggiuntivi

Varianti osservate:

| Appello | Variante |
|---|---|
| 2025-07-03 Parte I | LCS con vincolo di ingombro massimo $W$ |
| 2025-06-09 Parte I | LCS con massimo 2 rossi e massimo 3 blu |
| 2025-11-10 Parte I Tema A | LCS con presenza obbligatoria di almeno un rosso |
| 2025-09-17 Parte I | LCS a tre sequenze con al massimo 2 rossi |
| 2025-02-11 Parte I scritto completo | LCS a tre sequenze con al massimo 2 rossi |
| 2025-02-11 Parte I recupero parziale | LCS a tre sequenze con al massimo 2 rossi |
| 2025-01-13 Parte I | LCS con massimo 3 rossi e massimo 2 blu |
```

Aggiornare la sezione grafi:

```md
## DP su grafi con stato esteso

Varianti osservate:

| Appello | Variante |
|---|---|
| 2026-01-12 | cammino con numero pari di archi |
| 2025-09-17 Parte I | cammino con numero dispari di archi blu |
| 2025-07-03 Parte I | cammino con esattamente 2 rossi e 2 blu |
| 2025-06-09 Parte I | cammino con vincoli di precedenza tra colori |
| 2025-11-10 Parte I Tema A | cammino con $\#A + \#B = 3$ |
| 2025-02-11 Parte I scritto completo | cammino senza due neri consecutivi e senza due blu consecutivi |
| 2025-02-11 Parte I recupero parziale | cammino minimo con numero dispari di archi blu e senza due vertici rossi consecutivi |
| 2025-01-13 Parte I | cammino in cui nero non è seguito da rosso e rosso non è seguito da blu |
```

Aggiungere o rafforzare una sottosezione:

```md
## Cammini con vincoli di parità

Varianti osservate:

| Appello | Variante |
|---|---|
| 2026-01-12 | numero pari di archi |
| 2025-09-17 Parte I | numero dispari di archi blu |
| 2025-02-11 Parte I recupero parziale | cammino minimo con numero dispari di archi blu |
```

---

## 8. Differenza rispetto agli appelli già analizzati

Aggiungere in:

```txt
06_exam_patterns/variations_by_appeal.md
```

una nota del tipo:

```md
## 2025-09-17 Parte I

Questo appello conferma due famiglie già forti nella Parte I.

### Esercizio 1

L'esercizio ripete il pattern:

```txt
LCS a tre sequenze con al massimo 2 simboli rossi
```

già presente negli appelli dell'11 febbraio 2025.

Va quindi trattato come conferma del pattern e non come metodo nuovo.

### Esercizio 2

L'esercizio introduce una variante essenziale e pulita della DP su grafi con parità:

- il grafo non è pesato;
- si chiede solo esistenza;
- si conta solo la parità degli archi blu;
- gli archi rossi e neri non cambiano la parità.

Questa variante è utile come base per capire esercizi più complessi, come il recupero dell'11 febbraio 2025, dove si chiedeva un cammino minimo con numero dispari di archi blu e un ulteriore vincolo sui vertici rossi consecutivi.
```

---

## 9. Note metodologiche importanti

Codex deve evitare questi errori:

```md
> [!Warning]
> Non duplicare il metodo dell'esercizio 1 se è già stato creato per gli appelli dell'11 febbraio 2025.
> L'esercizio è lo stesso pattern: LCS a tre sequenze con massimo 2 rossi.

> [!Warning]
> Nell'esercizio 2 non basta calcolare una chiusura transitiva classica.
> Bisogna distinguere cammini con parità pari e cammini con parità dispari di archi blu.

> [!Warning]
> Gli archi rossi e neri non vanno eliminati.
> Possono comparire nel cammino e contribuiscono con parità 0.

> [!Warning]
> Il cammino vuoto da un vertice a sé stesso ha numero 0 di archi blu, quindi parità pari.
```

---

## 10. Aggiornare PROJECT_STATUS.md

Aggiungere una riga nella tabella degli appelli:

```md
| 2025-09-17 Parte I | `parteI-17set25.pdf` | 2 | DP LCS a tre sequenze con budget rossi, DP grafi con parità archi blu | cataloged |
```

Aggiornare il conteggio sintetico:

```md
Appelli analizzati:
- 2026-01-12
- 2025-11-10 Parte I Tema A
- 2025-09-17 Parte I
- 2025-07-03 Parte I
- 2025-06-09 Parte I
- 2025-02-11 Parte I scritto completo
- 2025-02-11 Parte I recupero parziale
- 2025-01-13 Parte I
```

---

## 11. Aggiornare TODO.md

Aggiungere tra le possibili priorità future:

```md
## Soluzioni ad alta priorità

- [ ] Risolvere completamente `exam_2025_09_17_p1_e02`
      perché è la variante base della DP su grafi con parità degli archi blu.
```

Aggiungere anche una nota di deduplicazione:

```md
## Deduplicazione contenuti

- [ ] Verificare che `exam_2025_09_17_p1_e01`,
      `exam_2025_02_11_p1_completo_e01` e
      `exam_2025_02_11_p1_recupero_e01`
      puntino allo stesso metodo senza duplicare spiegazioni teoriche.
```

Aggiungere una possibile nota di consolidamento:

```md
## Consolidamento metodi Parte I

- [ ] Creare una tabella comparativa delle varianti di parità nei grafi:
      - cammino con numero pari di archi;
      - cammino con numero dispari di archi blu;
      - cammino minimo con numero dispari di archi blu.
```

---

## 12. Commit consigliato

Dopo aver applicato tutte le modifiche:

```bash
git status
git add .
git commit -m "Ingest 2025-09-17 APA Parte I exam"
```

Prima del commit controllare:

```bash
find . -name "*2025_09_17*"
grep -R "exam_2025_09_17" .
grep -R "parteI-17set25" .
```

Verificare che non siano stati creati duplicati con nomi simili, per esempio:

```txt
exam_2025_09_17.md
exam_2025_09_17_part1_exam.md
exam_2025_09_17_settembre.md
```

Il naming standard da mantenere è:

```txt
exam_2025_09_17_part1
```

---

## 13. Stato atteso finale

Dopo l'applicazione del piano, la KB deve contenere:

```txt
09_ingestion_reports/ingestion_report_exam_2025_09_17_part1.md
02_transcriptions/exams/exam_2025_09_17_part1.md
03_exercise_catalog/exercises/exam_2025_09_17_p1_e01.md
03_exercise_catalog/exercises/exam_2025_09_17_p1_e02.md
```

e gli indici devono collegare correttamente il nuovo appello ai pattern:

```txt
- LCS con vincolo aggiuntivo
- LCS a tre sequenze
- LCS con budget sui colori
- DP booleana su grafi
- cammini con vincoli di parità
- numero dispari di archi blu
- programmazione dinamica Parte I
```

---

## 14. Nota finale per Codex

Questo appello è utile soprattutto per due motivi:

1. conferma che la LCS a tre sequenze con massimo 2 rossi è un pattern ricorrente, non un caso isolato;
2. fornisce una versione base e pulita della DP su grafi con parità degli archi blu.

La priorità è integrare l'esercizio 2 come metodo/famiglia riutilizzabile, perché aiuta a capire anche varianti più complesse come i cammini minimi vincolati.
