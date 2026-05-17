# Piano Codex — Ingestion appello APA 2025-02-11 Parte I scritto completo

## Obiettivo

Integrare nella knowledge base APA l'appello:

```txt
Analisi e Progetto di Algoritmi — Parte I
Data: 11 febbraio 2025
Tipo: scritto completo
File sorgente: parteI-11feb25-completo.pdf
```

L'appello contiene 2 esercizi di programmazione dinamica:

1. LCS comune a tre sequenze con vincolo di al massimo due simboli rossi.
2. DP su grafo colorato per verificare, per ogni coppia di vertici, l'esistenza di un cammino senza due archi consecutivi neri e senza due archi consecutivi blu.

Questo appello va integrato nella KB senza duplicare contenuti già presenti, collegandolo ai pattern già emersi:

- LCS con vincoli aggiuntivi;
- LCS con più sequenze;
- programmazione dinamica con stato esteso;
- DP booleana su grafi colorati;
- vincoli locali sui colori degli archi;
- Parte I come sezione ad alta resa per esercizi formali di DP.

---

## 1. File da creare

Creare il report di ingestion:

```txt
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_completo.md
```

Creare la trascrizione dell'appello:

```txt
02_transcriptions/exams/exam_2025_02_11_part1_completo.md
```

Creare i due esercizi catalogati:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e01.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e02.md
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
04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
04_methods/metodo_dp_cammini_colori_precedenze.md
```

Creare solo se non esistono già metodi equivalenti:

```txt
04_methods/metodo_lcs_tre_sequenze_vincolo_colori.md
04_methods/metodo_dp_cammini_colori_vincoli_consecutivi.md
```

Aggiornare teoria minima:

```txt
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/vincoli_su_colori.md
05_theory/grafi_colorati.md
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
02_transcriptions/exams/exam_2025_02_11_part1_completo.md
```

inserire una trascrizione leggera, non verbosa, con questa struttura:

```md
# Appello 2025-02-11 — Parte I scritto completo

> [!Info]
> Fonte: `parteI-11feb25-completo.pdf`
> Stato: transcribed
> Tipo: appello Parte I, scritto completo
> Argomenti principali: programmazione dinamica, LCS a tre sequenze, vincoli sui colori, cammini su grafi colorati

## Esercizio 1 — LCS a tre sequenze con al massimo due rossi

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

Si vuole determinare una più lunga sottosequenza comune di $X$, $Y$ e $W$ che abbia al massimo due simboli rossi.

Richieste:
1. coefficienti;
2. caso base;
3. passo ricorsivo;
4. coefficiente che fornisce il valore ottimo;
5. algoritmo bottom-up;
6. algoritmo ricorsivo di ricostruzione.

## Esercizio 2 — Cammini senza due neri o due blu consecutivi

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha colore:

$$
col:E \to C
$$

dove:

$$
C = \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ nel quale:

- non vi sono due archi consecutivi neri;
- non vi sono due archi consecutivi blu.

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
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e01.md
```

Contenuto consigliato:

```md
# exam_2025_02_11_p1_completo_e01 — LCS a tre sequenze con al massimo due rossi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_completo]]
> Stato: cataloged
> Tipologia: programmazione dinamica su sequenze
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_programmazione_dinamica_lcs_vincoli_colori]]

## Problema

Date tre sequenze $X$, $Y$ e $W$ su un alfabeto $S$, ogni simbolo ha colore rosso, blu o nero tramite:

$$
col:S \to \{R,B,N\}
$$

Si vuole trovare una sottosequenza comune di lunghezza massima tra $X$, $Y$ e $W$ che contenga al massimo due simboli rossi.

## Pattern riconosciuto

È una variante della LCS classica con due estensioni:

1. la LCS è tra tre sequenze invece che tra due;
2. lo stato deve tenere conto del numero di simboli rossi usati.

Rispetto agli altri appelli già analizzati, questa variante combina:

- LCS con vincolo di colore;
- stato di budget;
- terza dimensione di sequenza.

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

$C[i,j,k,r]$ è la lunghezza massima di una sottosequenza comune tra:

$$
X_i = \langle x_1,\dots,x_i \rangle
$$

$$
Y_j = \langle y_1,\dots,y_j \rangle
$$

$$
W_k = \langle w_1,\dots,w_k \rangle
$$

che usa al massimo $r$ simboli rossi.

> [!Note]
> Si usa una semantica "al massimo $r$ rossi" perché il problema chiede al massimo due rossi. In alternativa si potrebbe usare una semantica "esattamente $r$ rossi", ma in questo caso la soluzione finale dovrebbe prendere un massimo tra $r=0,1,2$.

## Caso base

Se almeno una delle tre sequenze considerate è vuota:

$$
C[0,j,k,r] = 0
$$

$$
C[i,0,k,r] = 0
$$

$$
C[i,j,0,r] = 0
$$

per ogni valore valido di $i,j,k,r$.

## Passo ricorsivo

Se i tre simboli finali non coincidono, cioè non vale:

$$
x_i = y_j = w_k
$$

allora:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r]
\end{cases}
$$

Se invece:

$$
x_i = y_j = w_k
$$

e il simbolo comune non è rosso:

$$
col(x_i) \ne R
$$

allora:

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

Se invece:

$$
x_i = y_j = w_k
$$

e il simbolo comune è rosso:

$$
col(x_i) = R
$$

allora, per $r>0$:

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

Per $r=0$, il simbolo rosso non può essere preso:

$$
C[i,j,k,0] =
\max
\begin{cases}
C[i-1,j,k,0] \\
C[i,j-1,k,0] \\
C[i,j,k-1,0]
\end{cases}
$$

## Soluzione

La lunghezza della soluzione è:

$$
C[m,n,d,2]
$$

## Collegamenti

- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[metodo_lcs_tre_sequenze_vincolo_colori]]
```

---

## 5. Esercizio 2 — Catalogazione

Creare:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e02.md
```

Contenuto consigliato:

```md
# exam_2025_02_11_p1_completo_e02 — Cammini senza due neri o due blu consecutivi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_completo]]
> Stato: cataloged
> Tipologia: programmazione dinamica su grafi
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_dp_cammini_colori_precedenze]]

## Problema

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha colore:

$$
col:E \to \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ nel quale:

- non compaiono due archi consecutivi neri;
- non compaiono due archi consecutivi blu.

Gli archi rossi non sono vietati in coppia dal testo.

## Pattern riconosciuto

È una DP booleana su grafi colorati con vincolo locale di consecutività.

Il vincolo non dipende solo dalla coppia di vertici, ma anche dal colore dell'ultimo arco usato. Serve quindi uno stato ausiliario che ricordi il colore finale del cammino.

## Coefficienti consigliati

Numerare i vertici come:

$$
V = \{1,\dots,n\}
$$

Definire:

$$
D[k,i,j,c]
$$

dove:

- $0 \le k \le n$;
- $i,j \in V$;
- $c \in \{R,N,B,\bot\}$.

$D[k,i,j,c]$ è vero se e solo se esiste un cammino valido da $i$ a $j$ che usa come vertici intermedi solo vertici in $\{1,\dots,k\}$ e il cui ultimo arco ha colore $c$.

Il simbolo $\bot$ può essere usato per il cammino vuoto da un vertice a sé stesso.

> [!Warning]
> Il vincolo riguarda due archi consecutivi. Per comporre due cammini o estendere un cammino con un arco, bisogna sapere il colore dell'ultimo arco della parte sinistra e il colore del primo arco della parte destra oppure usare una formulazione alternativa con stato più ricco.

## Variante consigliata più robusta

Per evitare ambiguità nella composizione tipo Floyd-Warshall, usare uno stato che memorizza sia primo sia ultimo colore:

$$
D[k,i,j,a,b]
$$

dove:

- $a \in \{R,N,B,\bot\}$ è il colore del primo arco del cammino;
- $b \in \{R,N,B,\bot\}$ è il colore dell'ultimo arco del cammino.

$D[k,i,j,a,b]$ è vero se e solo se esiste un cammino valido da $i$ a $j$, con intermedi in $\{1,\dots,k\}$, il cui primo arco ha colore $a$ e il cui ultimo arco ha colore $b$.

Questa variante permette di concatenare due cammini controllando solo la compatibilità tra:

- ultimo colore del primo cammino;
- primo colore del secondo cammino.

## Predicato di compatibilità

Definire:

$$
compatibile(c_1,c_2)
$$

vero se non si crea una coppia vietata.

Sono vietate solo:

$$
(N,N)
$$

e:

$$
(B,B)
$$

Quindi:

$$
compatibile(c_1,c_2) =
\begin{cases}
falso & \text{se } c_1=N \land c_2=N \\
falso & \text{se } c_1=B \land c_2=B \\
vero & \text{altrimenti}
\end{cases}
$$

## Caso base

Cammino vuoto:

$$
D[0,i,i,\bot,\bot] = vero
$$

Arco diretto $(i,j) \in E$ con colore $c = col(i,j)$:

$$
D[0,i,j,c,c] = vero
$$

Tutti gli altri coefficienti sono falsi.

## Passo ricorsivo

Per $k \ge 1$:

$$
D[k,i,j,a,b] =
D[k-1,i,j,a,b]
\lor
\bigvee_{\alpha,\beta}
\bigvee_{\gamma,\delta}
\left(
D[k-1,i,k,\alpha,\beta]
\land
D[k-1,k,j,\gamma,\delta]
\land
compatibile(\beta,\gamma)
\land
a = \alpha
\land
b = \delta
\right)
$$

Bisogna gestire separatamente i casi in cui una delle due parti è un cammino vuoto, perché il colore $\bot$ non rappresenta un arco reale.

> [!Note]
> In alternativa, Codex può usare una formulazione con problema ausiliario basato su ultimo colore e ricorrenza per estensione di archi, purché sia chiaro che lo stato deve impedire le coppie consecutive $NN$ e $BB$.

## Soluzione

Per ogni coppia $(i,j)$, la risposta è vera se esistono colori $a,b$ tali che:

$$
D[n,i,j,a,b] = vero
$$

cioè:

$$
\bigvee_{a,b \in \{R,N,B,\bot\}} D[n,i,j,a,b]
$$

è vero.

## Collegamenti

- [[grafi_colorati]]
- [[metodo_dp_cammini_colori_precedenze]]
- [[metodo_dp_cammini_colori_vincoli_consecutivi]]
- [[parte_i_dynamic_programming_patterns]]
```

---

## 6. Pattern da aggiornare

Aggiornare:

```txt
06_exam_patterns/recurring_exercise_types.md
```

aggiungendo l'appello 2025-02-11 alla famiglia:

```md
## Programmazione dinamica Parte I

Appelli collegati:

- [[exam_2026_01_12]]
- [[exam_2025_11_10_part1_tema_a]]
- [[exam_2025_07_03_part1]]
- [[exam_2025_06_09_part1]]
- [[exam_2025_02_11_part1_completo]]

Pattern ricorrente:

1. definizione dei coefficienti;
2. caso base;
3. passo ricorsivo;
4. coefficiente soluzione;
5. bottom-up;
6. ricostruzione, se richiesta.
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
| 2025-02-11 Parte I scritto completo | LCS a tre sequenze con al massimo 2 rossi |
```

Aggiornare la sezione grafi:

```md
## DP booleana su grafi con stato esteso

Varianti osservate:

| Appello | Variante |
|---|---|
| 2026-01-12 | cammino con numero pari di archi |
| 2025-07-03 Parte I | cammino con esattamente 2 rossi e 2 blu |
| 2025-06-09 Parte I | cammino con vincoli di precedenza tra colori |
| 2025-11-10 Parte I Tema A | cammino con $\#A + \#B = 3$ |
| 2025-02-11 Parte I scritto completo | cammino senza due neri consecutivi e senza due blu consecutivi |
```

---

## 7. Differenza rispetto agli appelli già analizzati

Aggiungere in:

```txt
06_exam_patterns/variations_by_appeal.md
```

una nota del tipo:

```md
## 2025-02-11 Parte I scritto completo

Questo appello conferma la centralità della programmazione dinamica nella Parte I e introduce due varianti importanti.

### Esercizio 1

La variante LCS è più ricca delle precedenti perché combina:

- tre sequenze invece di due;
- vincolo di colore;
- budget massimo di simboli rossi.

Rispetto a `2025-06-09 Parte I`, dove il vincolo era su massimo 2 rossi e massimo 3 blu in due sequenze, qui il vincolo resta solo sui rossi ma la LCS è tra tre sequenze.

### Esercizio 2

La variante sui grafi non richiede conteggi esatti, ma vincoli locali di consecutività.

La difficoltà principale è che per verificare il vincolo non basta sapere se esiste un cammino da $i$ a $j$: bisogna ricordare almeno informazioni sul colore degli archi estremi del cammino, oppure usare un problema ausiliario equivalente.
```

---

## 8. Note metodologiche importanti

Codex deve evitare questi errori:

```md
> [!Warning]
> Nell'esercizio 1 non basta applicare la LCS classica a tre sequenze e poi controllare il numero di rossi.
> Il vincolo "al massimo due rossi" deve essere integrato nello stato della DP.

> [!Warning]
> Nell'esercizio 1 il problema è su tre sequenze: la ricorrenza deve avere tre indici di posizione, non due.

> [!Warning]
> Nell'esercizio 2 il vincolo è locale su archi consecutivi.
> Una semplice chiusura transitiva booleana $D[k,i,j]$ non è sufficiente.

> [!Warning]
> Nell'esercizio 2 sono vietate solo le coppie consecutive $NN$ e $BB$.
> Le coppie $RR$, $RN$, $RB$, $NR$, $NB$, $BR$, $BN$ sono ammesse salvo diverse indicazioni nel testo.

> [!Warning]
> Prestare attenzione alla composizione dei cammini nella DP su grafi.
> Se si usa una ricorrenza tipo Floyd-Warshall, bisogna poter verificare la compatibilità tra l'ultimo arco del primo sottocammino e il primo arco del secondo sottocammino.
```

---

## 9. Aggiornare PROJECT_STATUS.md

Aggiungere una riga nella tabella degli appelli:

```md
| 2025-02-11 Parte I scritto completo | `parteI-11feb25-completo.pdf` | 2 | DP LCS a tre sequenze con budget rossi, DP grafi con vincoli consecutivi | cataloged |
```

Aggiornare il conteggio sintetico:

```md
Appelli analizzati:
- 2026-01-12
- 2025-11-10 Parte I Tema A
- 2025-07-03 Parte I
- 2025-06-09 Parte I
- 2025-02-11 Parte I scritto completo
```

---

## 10. Aggiornare TODO.md

Aggiungere tra le possibili priorità future:

```md
## Soluzioni ad alta priorità

- [ ] Risolvere completamente `exam_2025_02_11_p1_completo_e01`
      perché combina LCS a tre sequenze e vincolo di budget sui colori.
- [ ] Risolvere completamente `exam_2025_02_11_p1_completo_e02`
      perché è una variante importante della DP su grafi con vincoli locali di consecutività.
```

Aggiungere anche una possibile nota di consolidamento:

```md
## Consolidamento metodi Parte I

- [ ] Creare una tabella comparativa delle varianti LCS:
      - LCS con ingombro massimo;
      - LCS con massimo rossi/blu;
      - LCS con presenza obbligatoria di rosso;
      - LCS a tre sequenze con massimo due rossi.
- [ ] Creare una tabella comparativa delle varianti DP su grafi:
      - parità del numero di archi;
      - conteggi esatti di colori;
      - vincoli di precedenza tra colori;
      - conteggio aggregato A/B;
      - divieto di coppie consecutive di colori.
```

---

## 11. Commit consigliato

Dopo aver applicato tutte le modifiche:

```bash
git status
git add .
git commit -m "Ingest 2025-02-11 APA Parte I complete exam"
```

Prima del commit controllare:

```bash
find . -name "*2025_02_11*"
grep -R "exam_2025_02_11" .
grep -R "parteI-11feb25-completo" .
```

Verificare che non siano stati creati duplicati con nomi simili, per esempio:

```txt
exam_2025_02_11.md
exam_2025_02_11_part1.md
exam_2025_02_11_completo.md
```

Il naming standard da mantenere è:

```txt
exam_2025_02_11_part1_completo
```

---

## 12. Stato atteso finale

Dopo l'applicazione del piano, la KB deve contenere:

```txt
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_completo.md
02_transcriptions/exams/exam_2025_02_11_part1_completo.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e01.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_completo_e02.md
```

e gli indici devono collegare correttamente il nuovo appello ai pattern:

```txt
- LCS con vincolo aggiuntivo
- LCS a tre sequenze
- LCS con budget sui colori
- DP booleana su grafi
- cammini con vincoli locali sui colori
- programmazione dinamica Parte I
```

---

## 13. Nota finale per Codex

Questo appello è particolarmente importante perché amplia due famiglie già presenti nella KB:

1. la famiglia delle LCS vincolate, introducendo tre sequenze;
2. la famiglia delle DP su grafi colorati, introducendo vincoli locali di consecutività invece di semplici conteggi.

La priorità non è creare teoria generica, ma collegare il nuovo appello ai pattern già osservati e rendere evidenti le variazioni rispetto agli appelli precedenti.
