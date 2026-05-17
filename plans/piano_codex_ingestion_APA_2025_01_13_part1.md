# Piano Codex — Ingestion appello APA 2025-01-13 Parte I

## Obiettivo

Integrare nella knowledge base APA l'appello:

```txt
Analisi e Progetto di Algoritmi — Parte I
Data: 13 gennaio 2025
File sorgente: parteI-13gen25.pdf
```

L'appello contiene 2 esercizi di programmazione dinamica:

1. LCS tra due sequenze con vincoli:
   - al massimo 3 simboli rossi;
   - al massimo 2 simboli blu.
2. DP su grafo colorato per stabilire, per ogni coppia di vertici, se esiste un cammino in cui:
   - un arco nero non è mai seguito da un arco rosso;
   - un arco rosso non è mai seguito da un arco blu.

Questo appello va integrato nella KB collegandolo ai pattern già emersi:

- LCS con vincoli aggiuntivi sui colori;
- programmazione dinamica con stato esteso;
- DP booleana su grafi colorati;
- vincoli locali o di precedenza sui colori degli archi;
- Parte I come sezione ad alta resa per esercizi formali di DP.

---

## 1. File da creare

Creare il report di ingestion:

```txt
09_ingestion_reports/ingestion_report_exam_2025_01_13_part1.md
```

Creare la trascrizione dell'appello:

```txt
02_transcriptions/exams/exam_2025_01_13_part1.md
```

Creare i due esercizi catalogati:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p1_e01.md
03_exercise_catalog/exercises/exam_2025_01_13_p1_e02.md
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

Eventualmente creare solo se non esiste già una nota equivalente:

```txt
04_methods/metodo_lcs_budget_multipli_colori.md
04_methods/metodo_dp_cammini_colori_vincoli_di_sequenza.md
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
02_transcriptions/exams/exam_2025_01_13_part1.md
```

inserire una trascrizione leggera, non verbosa, con questa struttura:

```md
# Appello 2025-01-13 — Parte I

> [!Info]
> Fonte: `parteI-13gen25.pdf`
> Stato: transcribed
> Tipo: appello Parte I
> Argomenti principali: programmazione dinamica, LCS con vincoli sui colori, cammini su grafi colorati

## Esercizio 1 — LCS con al massimo 3 rossi e al massimo 2 blu

Date due sequenze:

$$
X = \langle x_1,\dots,x_m \rangle
$$

$$
Y = \langle y_1,\dots,y_n \rangle
$$

su un alfabeto $S$, ogni simbolo ha colore:

$$
col:S \to \{R,B,N\}
$$

Si vuole determinare una più lunga sottosequenza comune di $X$ e $Y$ nella quale vi siano:

- al massimo 3 simboli rossi;
- al massimo 2 simboli blu.

Richieste:
1. coefficienti;
2. caso base;
3. passo ricorsivo;
4. coefficiente che fornisce il valore ottimo;
5. algoritmo bottom-up;
6. algoritmo ricorsivo di ricostruzione.

## Esercizio 2 — Cammini con vincoli di precedenza sui colori degli archi

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha colore:

$$
col:E \to C
$$

dove:

$$
C = \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ nel quale:

- un arco nero non è mai seguito da un arco rosso;
- un arco rosso non è mai seguito da un arco blu.

Il testo specifica che è necessario considerare il problema opportunamente vincolato tramite un problema ausiliario.

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
03_exercise_catalog/exercises/exam_2025_01_13_p1_e01.md
```

Contenuto consigliato:

```md
# exam_2025_01_13_p1_e01 — LCS con al massimo 3 rossi e al massimo 2 blu

> [!Info]
> Fonte: [[exam_2025_01_13_part1]]
> Stato: cataloged
> Tipologia: programmazione dinamica su sequenze
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_programmazione_dinamica_lcs_vincoli_colori]]

## Problema

Date due sequenze $X$ e $Y$ su un alfabeto $S$, ogni simbolo ha colore rosso, blu o nero tramite:

$$
col:S \to \{R,B,N\}
$$

Si vuole trovare una sottosequenza comune di lunghezza massima tra $X$ e $Y$ che contenga:

- al massimo 3 simboli rossi;
- al massimo 2 simboli blu.

## Pattern riconosciuto

È una variante della LCS classica con vincoli multipli di budget sui colori.

Rispetto alla LCS standard, lo stato deve tenere conto di due risorse:

- numero massimo di simboli rossi ancora disponibili;
- numero massimo di simboli blu ancora disponibili.

Questa variante è molto vicina a:

- `exam_2025_06_09_p1_e01`, dove il vincolo era al massimo 2 rossi e al massimo 3 blu;
- `exam_2025_02_11_p1_completo_e01`, dove la LCS era a tre sequenze con massimo 2 rossi.

## Coefficienti consigliati

Definire:

$$
C[i,j,r,b]
$$

dove:

- $0 \le i \le m$;
- $0 \le j \le n$;
- $r \in \{0,1,2,3\}$;
- $b \in \{0,1,2\}$.

$C[i,j,r,b]$ è la lunghezza massima di una sottosequenza comune tra:

$$
X_i = \langle x_1,\dots,x_i \rangle
$$

e:

$$
Y_j = \langle y_1,\dots,y_j \rangle
$$

che usa al massimo $r$ simboli rossi e al massimo $b$ simboli blu.

> [!Note]
> Si usa la semantica "al massimo" perché il testo richiede budget massimi. In alternativa, si può usare la semantica "esattamente", ma poi il coefficiente soluzione deve prendere un massimo sugli stati compatibili.

## Caso base

Se una delle due sequenze è vuota:

$$
C[0,j,r,b] = 0
$$

$$
C[i,0,r,b] = 0
$$

per ogni $i,j,r,b$ valido.

## Passo ricorsivo

Se $x_i \ne y_j$:

$$
C[i,j,r,b] =
\max
\begin{cases}
C[i-1,j,r,b] \\
C[i,j-1,r,b]
\end{cases}
$$

Se $x_i = y_j$ e $col(x_i)=N$:

$$
C[i,j,r,b] =
\max
\begin{cases}
C[i-1,j,r,b] \\
C[i,j-1,r,b] \\
1 + C[i-1,j-1,r,b]
\end{cases}
$$

Se $x_i = y_j$ e $col(x_i)=R$, per $r>0$:

$$
C[i,j,r,b] =
\max
\begin{cases}
C[i-1,j,r,b] \\
C[i,j-1,r,b] \\
1 + C[i-1,j-1,r-1,b]
\end{cases}
$$

Per $r=0$, il simbolo rosso non può essere preso.

Se $x_i = y_j$ e $col(x_i)=B$, per $b>0$:

$$
C[i,j,r,b] =
\max
\begin{cases}
C[i-1,j,r,b] \\
C[i,j-1,r,b] \\
1 + C[i-1,j-1,r,b-1]
\end{cases}
$$

Per $b=0$, il simbolo blu non può essere preso.

## Soluzione

La lunghezza della soluzione è:

$$
C[m,n,3,2]
$$

## Collegamenti

- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[metodo_lcs_budget_multipli_colori]]
```

---

## 5. Esercizio 2 — Catalogazione

Creare:

```txt
03_exercise_catalog/exercises/exam_2025_01_13_p1_e02.md
```

Contenuto consigliato:

```md
# exam_2025_01_13_p1_e02 — Cammini con vincoli di precedenza sui colori degli archi

> [!Info]
> Fonte: [[exam_2025_01_13_part1]]
> Stato: cataloged
> Tipologia: programmazione dinamica su grafi
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_dp_cammini_colori_precedenze]]

## Problema

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha colore:

$$
col:E \to \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ tale che:

- un arco nero non sia mai seguito da un arco rosso;
- un arco rosso non sia mai seguito da un arco blu.

In termini di coppie consecutive di archi, sono vietate:

$$
(N,R)
$$

e:

$$
(R,B)
$$

## Pattern riconosciuto

È una DP booleana su grafi colorati con vincoli locali di sequenza tra colori degli archi.

Il testo segnala esplicitamente la necessità di un problema ausiliario: questo indica che una semplice chiusura transitiva booleana su coppie di vertici non è sufficiente.

Serve uno stato che permetta di controllare il colore dell'arco finale di un sottocammino e/o il colore dell'arco iniziale del sottocammino successivo.

## Variante robusta dei coefficienti

Numerare i vertici come:

$$
V = \{1,\dots,n\}
$$

Definire:

$$
D[k,i,j,a,b]
$$

dove:

- $0 \le k \le n$;
- $i,j \in V$;
- $a \in \{R,N,B,\bot\}$;
- $b \in \{R,N,B,\bot\}$.

$D[k,i,j,a,b]$ è vero se e solo se esiste un cammino valido da $i$ a $j$ che:

- usa come vertici intermedi solo vertici in $\{1,\dots,k\}$;
- ha primo arco di colore $a$;
- ha ultimo arco di colore $b$;
- non contiene coppie consecutive di archi vietate.

Il simbolo $\bot$ rappresenta il cammino vuoto.

## Predicato di compatibilità

Definire:

$$
compatibile(c_1,c_2)
$$

vero se una coppia di archi consecutivi con colori $c_1,c_2$ è ammessa.

Sono vietate solo:

$$
(N,R)
$$

e:

$$
(R,B)
$$

Quindi:

$$
compatibile(c_1,c_2) =
\begin{cases}
falso & \text{se } c_1=N \land c_2=R \\
falso & \text{se } c_1=R \land c_2=B \\
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
\bigvee_{\alpha,\beta,\gamma,\delta}
\left(
D[k-1,i,k,\alpha,\beta]
\land
D[k-1,k,j,\gamma,\delta]
\land
compatibile(\beta,\gamma)
\land
a=\alpha
\land
b=\delta
\right)
$$

I casi in cui uno dei due sottocammini è vuoto vanno gestiti con attenzione, perché $\bot$ non è un colore reale di arco.

> [!Note]
> È accettabile anche una formulazione alternativa con stato basato sull'ultimo colore e ricorrenza per estensione di archi, purché sia chiaro come vengono impedite le coppie vietate $(N,R)$ e $(R,B)$.

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
- [[metodo_dp_cammini_colori_vincoli_di_sequenza]]
- [[parte_i_dynamic_programming_patterns]]
```

---

## 6. Pattern da aggiornare

Aggiornare:

```txt
06_exam_patterns/recurring_exercise_types.md
```

aggiungendo l'appello 2025-01-13 alla famiglia:

```md
## Programmazione dinamica Parte I

Appelli collegati:

- [[exam_2026_01_12]]
- [[exam_2025_11_10_part1_tema_a]]
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
| 2025-07-03 Parte I | cammino con esattamente 2 rossi e 2 blu |
| 2025-06-09 Parte I | cammino con vincoli di precedenza tra colori |
| 2025-11-10 Parte I Tema A | cammino con $\#A + \#B = 3$ |
| 2025-02-11 Parte I scritto completo | cammino senza due neri consecutivi e senza due blu consecutivi |
| 2025-02-11 Parte I recupero parziale | cammino minimo con numero dispari di archi blu e senza due vertici rossi consecutivi |
| 2025-01-13 Parte I | cammino in cui nero non è seguito da rosso e rosso non è seguito da blu |
```

---

## 7. Differenza rispetto agli appelli già analizzati

Aggiungere in:

```txt
06_exam_patterns/variations_by_appeal.md
```

una nota del tipo:

```md
## 2025-01-13 Parte I

Questo appello conferma due pattern ad alta frequenza della Parte I.

### Esercizio 1

L'esercizio è una variante LCS con due budget di colore:

- massimo 3 simboli rossi;
- massimo 2 simboli blu.

È molto vicino all'appello `2025-06-09 Parte I`, che chiedeva massimo 2 rossi e massimo 3 blu.

La struttura risolutiva è la stessa: aggiungere due dimensioni allo stato della LCS.

### Esercizio 2

L'esercizio è una variante sui grafi colorati con vincoli di sequenza tra archi consecutivi.

Rispetto ad altre varianti:

- non chiede conteggi esatti;
- non chiede cammino minimo;
- chiede solo esistenza;
- richiede però un problema ausiliario perché il vincolo dipende dall'ordine dei colori degli archi nel cammino.

Le coppie di colori vietate sono:

$$
(N,R)
$$

e:

$$
(R,B)
$$
```

---

## 8. Note metodologiche importanti

Codex deve evitare questi errori:

```md
> [!Warning]
> Nell'esercizio 1 non basta calcolare una LCS classica e poi contare i colori.
> I vincoli su rossi e blu devono essere integrati nello stato della DP.

> [!Warning]
> Nell'esercizio 1 bisogna distinguere chiaramente il budget rosso dal budget blu.
> Il budget rosso è 3, il budget blu è 2.

> [!Warning]
> Nell'esercizio 2 il testo dice "seguito da", quindi l'ordine conta.
> La coppia vietata $(N,R)$ non è equivalente alla coppia $(R,N)$.

> [!Warning]
> Nell'esercizio 2 sono vietate solo le coppie $(N,R)$ e $(R,B)$.
> Non sono vietate automaticamente le coppie inverse $(R,N)$ e $(B,R)$.

> [!Warning]
> Una semplice DP $D[k,i,j]$ non è sufficiente per l'esercizio 2, perché non conserva informazioni sul colore degli archi agli estremi del cammino.
```

---

## 9. Aggiornare PROJECT_STATUS.md

Aggiungere una riga nella tabella degli appelli:

```md
| 2025-01-13 Parte I | `parteI-13gen25.pdf` | 2 | DP LCS con budget rossi/blu, DP grafi con vincoli di sequenza sui colori | cataloged |
```

Aggiornare il conteggio sintetico:

```md
Appelli analizzati:
- 2026-01-12
- 2025-11-10 Parte I Tema A
- 2025-07-03 Parte I
- 2025-06-09 Parte I
- 2025-02-11 Parte I scritto completo
- 2025-02-11 Parte I recupero parziale
- 2025-01-13 Parte I
```

---

## 10. Aggiornare TODO.md

Aggiungere tra le possibili priorità future:

```md
## Soluzioni ad alta priorità

- [ ] Risolvere completamente `exam_2025_01_13_p1_e01`
      perché è una variante molto vicina a `exam_2025_06_09_p1_e01` e permette di consolidare le LCS con budget multipli.
- [ ] Risolvere completamente `exam_2025_01_13_p1_e02`
      perché rappresenta una variante importante dei vincoli di precedenza sui colori degli archi.
```

Aggiungere anche una nota di consolidamento:

```md
## Consolidamento metodi Parte I

- [ ] Creare o aggiornare una tabella comparativa delle varianti LCS con budget:
      - massimo 2 rossi e massimo 3 blu;
      - massimo 3 rossi e massimo 2 blu;
      - massimo 2 rossi su tre sequenze;
      - presenza obbligatoria di almeno un rosso.
- [ ] Creare o aggiornare una tabella comparativa delle varianti DP su grafi con vincoli di colore:
      - conteggi esatti;
      - conteggi aggregati;
      - parità;
      - vincoli di precedenza;
      - vincoli di consecutività.
```

---

## 11. Commit consigliato

Dopo aver applicato tutte le modifiche:

```bash
git status
git add .
git commit -m "Ingest 2025-01-13 APA Parte I exam"
```

Prima del commit controllare:

```bash
find . -name "*2025_01_13*"
grep -R "exam_2025_01_13" .
grep -R "parteI-13gen25" .
```

Verificare che non siano stati creati duplicati con nomi simili, per esempio:

```txt
exam_2025_01_13.md
exam_2025_01_13_part1_exam.md
exam_2025_01_13_gennaio.md
```

Il naming standard da mantenere è:

```txt
exam_2025_01_13_part1
```

---

## 12. Stato atteso finale

Dopo l'applicazione del piano, la KB deve contenere:

```txt
09_ingestion_reports/ingestion_report_exam_2025_01_13_part1.md
02_transcriptions/exams/exam_2025_01_13_part1.md
03_exercise_catalog/exercises/exam_2025_01_13_p1_e01.md
03_exercise_catalog/exercises/exam_2025_01_13_p1_e02.md
```

e gli indici devono collegare correttamente il nuovo appello ai pattern:

```txt
- LCS con vincolo aggiuntivo
- LCS con budget multipli sui colori
- DP booleana su grafi
- cammini con vincoli locali sui colori
- vincoli di precedenza tra colori degli archi
- programmazione dinamica Parte I
```

---

## 13. Nota finale per Codex

Questo appello è importante perché consolida due famiglie già fortissime:

1. LCS con budget multipli sui colori;
2. DP su grafi colorati con vincoli di sequenza tra archi.

L'appello è particolarmente utile per confrontare varianti molto simili:

- `2025-01-13_p1_e01` rispetto a `2025-06-09_p1_e01`;
- `2025-01-13_p1_e02` rispetto a `2025-06-09_p1_e02`.

La priorità è evitare duplicazioni metodologiche e usare questo esame per rafforzare le tabelle comparative dei pattern di Parte I.
