# Piano Codex — Ingestion appello APA 2025-11-10 Parte I Tema A

## Obiettivo

Integrare nella knowledge base APA l'appello:

```txt
Analisi e Progetto di Algoritmi — Parte I, Tema A
Data: 10 novembre 2025
File sorgente: parte-I-10nov25-A.pdf
```

L'appello contiene 2 esercizi di programmazione dinamica:

1. LCS con vincolo di presenza di almeno un simbolo rosso.
2. DP su grafo con archi etichettati A/B/C e cammini in cui `#A + #B = 3`.

Questo appello va integrato senza duplicare contenuti già presenti, collegandolo ai pattern già emersi dagli appelli 2025-06-09, 2025-07-03 e 2026-01-12.

---

## 1. File da creare

Creare il report di ingestion:

```txt
09_ingestion_reports/ingestion_report_exam_2025_11_10_part1_tema_a.md
```

Creare la trascrizione dell'appello:

```txt
02_transcriptions/exams/exam_2025_11_10_part1_tema_a.md
```

Creare i due esercizi catalogati:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e01.md
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e02.md
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
```

Aggiornare o creare, se già non esiste:

```txt
06_exam_patterns/parte_i_dynamic_programming_patterns.md
```

Aggiornare metodi già esistenti, senza duplicare:

```txt
04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
04_methods/metodo_dp_cammini_colori_conteggi.md
```

Eventualmente creare solo se non esiste già un metodo equivalente:

```txt
04_methods/metodo_lcs_presenza_colore_obbligatoria.md
04_methods/metodo_dp_cammini_conteggio_aggregato_lettere.md
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
02_transcriptions/exams/exam_2025_11_10_part1_tema_a.md
```

inserire una trascrizione leggera, non verbosa, con questa struttura:

```md
# Appello 2025-11-10 — Parte I Tema A

> [!Info]
> Fonte: `parte-I-10nov25-A.pdf`
> Stato: transcribed
> Tipo: appello Parte I
> Argomenti principali: programmazione dinamica, LCS con vincoli, cammini su grafi etichettati

## Esercizio 1 — LCS con presenza obbligatoria del rosso

Date due sequenze $X = \langle x_1,\dots,x_m \rangle$ e $Y = \langle y_1,\dots,y_n \rangle$ su un alfabeto $S$, ogni simbolo ha colore:

$$
col:S \to \{R,B,N\}
$$

Si vuole determinare una più lunga sottosequenza comune di $X$ e $Y$ nella quale sia presente almeno un simbolo rosso.

Richieste:
1. coefficienti;
2. caso base;
3. passo ricorsivo;
4. soluzione in termini di lunghezza;
5. algoritmo bottom-up;
6. algoritmo ricorsivo di ricostruzione.

## Esercizio 2 — Cammini con somma di archi A/B uguale a 3

Dato un grafo $(V,E,f)$ senza cappi, ogni arco ha una lettera:

$$
f:E \to L
$$

dove:

$$
L = \{A,B,C\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ nel quale la somma tra il numero di archi con lettera A e il numero di archi con lettera B sia uguale a 3.

Richieste:
1. coefficienti;
2. caso base;
3. passo ricorsivo;
4. soluzione.
```

---

## 4. Esercizio 1 — Catalogazione

Creare:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e01.md
```

Contenuto consigliato:

```md
# exam_2025_11_10_p1_tema_a_e01 — LCS con presenza obbligatoria del rosso

> [!Info]
> Fonte: [[exam_2025_11_10_part1_tema_a]]
> Stato: cataloged
> Tipologia: programmazione dinamica su sequenze
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_programmazione_dinamica_lcs_vincoli_colori]]

## Problema

Date due sequenze $X$ e $Y$ su un alfabeto $S$, ogni simbolo ha colore rosso, blu o nero tramite:

$$
col:S \to \{R,B,N\}
$$

Si vuole trovare una sottosequenza comune di lunghezza massima che contenga almeno un simbolo rosso.

## Pattern riconosciuto

È una variante della LCS classica con vincolo aggiuntivo.

Rispetto alla LCS standard, lo stato deve ricordare se nella sottosequenza costruita è già stato usato almeno un simbolo rosso.

## Coefficienti consigliati

Definire:

$$
C[i,j,r]
$$

dove:

- $0 \le i \le m$;
- $0 \le j \le n$;
- $r \in \{0,1\}$;
- $r=0$ indica che la sottosequenza non contiene ancora simboli rossi;
- $r=1$ indica che la sottosequenza contiene almeno un simbolo rosso.

$C[i,j,r]$ è la lunghezza massima di una sottosequenza comune tra $X_i$ e $Y_j$ con stato di presenza del rosso pari a $r$.

Usare $-\infty$ per stati impossibili.

## Caso base

Per ogni $i,j$:

$$
C[0,j,0] = 0
$$

$$
C[i,0,0] = 0
$$

$$
C[0,j,1] = -\infty
$$

$$
C[i,0,1] = -\infty
$$

perché con una sequenza vuota non è possibile avere una sottosequenza contenente un simbolo rosso.

## Passo ricorsivo

Se $x_i \ne y_j$:

$$
C[i,j,r] = \max \{ C[i-1,j,r], C[i,j-1,r] \}
$$

per $r \in \{0,1\}$.

Se $x_i = y_j$, bisogna considerare anche la scelta del simbolo comune.

Per $r=0$:

$$
C[i,j,0] =
\max
\begin{cases}
C[i-1,j,0] \\
C[i,j-1,0] \\
1 + C[i-1,j-1,0] & \text{se } col(x_i) \ne R
\end{cases}
$$

Per $r=1$:

se $col(x_i)=R$:

$$
C[i,j,1] =
\max
\begin{cases}
C[i-1,j,1] \\
C[i,j-1,1] \\
1 + C[i-1,j-1,0] \\
1 + C[i-1,j-1,1]
\end{cases}
$$

se $col(x_i)\ne R$:

$$
C[i,j,1] =
\max
\begin{cases}
C[i-1,j,1] \\
C[i,j-1,1] \\
1 + C[i-1,j-1,1]
\end{cases}
$$

## Soluzione

La lunghezza della soluzione è:

$$
C[m,n,1]
$$

Se $C[m,n,1] = -\infty$, allora non esiste una sottosequenza comune contenente almeno un simbolo rosso.

## Collegamenti

- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
```

---

## 5. Esercizio 2 — Catalogazione

Creare:

```txt
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e02.md
```

Contenuto consigliato:

```md
# exam_2025_11_10_p1_tema_a_e02 — Cammini con #A + #B = 3

> [!Info]
> Fonte: [[exam_2025_11_10_part1_tema_a]]
> Stato: cataloged
> Tipologia: programmazione dinamica su grafi
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_dp_cammini_colori_conteggi]]

## Problema

Dato un grafo $(V,E,f)$ senza cappi, ogni arco ha una lettera:

$$
f:E \to \{A,B,C\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ tale che:

$$
\#A + \#B = 3
$$

dove $\#A$ è il numero di archi con lettera A nel cammino e $\#B$ è il numero di archi con lettera B.

Gli archi con lettera C non contribuiscono al conteggio.

## Pattern riconosciuto

È una DP booleana su grafi con stato esteso.

Rispetto alla chiusura transitiva classica, lo stato deve ricordare il numero complessivo di archi di tipo A o B usati nel cammino.

## Funzione costo degli archi

Definire:

$$
peso(e) =
\begin{cases}
1 & \text{se } f(e)=A \text{ oppure } f(e)=B \\
0 & \text{se } f(e)=C
\end{cases}
$$

Il vincolo diventa trovare un cammino con peso totale esattamente 3.

## Coefficienti consigliati

Numerare i vertici come:

$$
V = \{1,\dots,n\}
$$

Definire:

$$
D[k,i,j,h]
$$

dove:

- $0 \le k \le n$;
- $i,j \in V$;
- $h \in \{0,1,2,3\}$.

$D[k,i,j,h]$ è vero se e solo se esiste un cammino da $i$ a $j$ che usa come vertici intermedi solo vertici nell'insieme $\{1,\dots,k\}$ e tale che la somma tra archi A e archi B sia esattamente $h$.

## Caso base

Per $k=0$, si considerano solo cammini diretti, senza vertici intermedi.

Cammino vuoto:

$$
D[0,i,i,0] = vero
$$

Arco diretto $(i,j) \in E$:

$$
D[0,i,j,peso(i,j)] = vero
$$

Tutti gli altri coefficienti sono falsi.

## Passo ricorsivo

Per $k \ge 1$:

$$
D[k,i,j,h] =
D[k-1,i,j,h]
\lor
\bigvee_{a=0}^{h}
\left(
D[k-1,i,k,a]
\land
D[k-1,k,j,h-a]
\right)
$$

per ogni:

$$
h \in \{0,1,2,3\}
$$

## Soluzione

Per ogni coppia $(i,j)$, la risposta è:

$$
D[n,i,j,3]
$$

Se $D[n,i,j,3]$ è vero, allora esiste un cammino da $i$ a $j$ in cui la somma tra il numero di archi A e il numero di archi B è uguale a 3.

## Collegamenti

- [[grafi_colorati]]
- [[metodo_dp_cammini_colori_conteggi]]
- [[parte_i_dynamic_programming_patterns]]
```

---

## 6. Pattern da aggiornare

Aggiornare:

```txt
06_exam_patterns/recurring_exercise_types.md
```

aggiungendo l'appello 2025-11-10 alla famiglia:

```md
## Programmazione dinamica Parte I

Appelli collegati:

- [[exam_2026_01_12]]
- [[exam_2025_07_03_part1]]
- [[exam_2025_06_09_part1]]
- [[exam_2025_11_10_part1_tema_a]]

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
```

---

## 7. Differenza rispetto agli appelli già analizzati

Aggiungere in:

```txt
06_exam_patterns/variations_by_appeal.md
```

una nota del tipo:

```md
## 2025-11-10 Parte I Tema A

Questo appello conferma fortemente la centralità della programmazione dinamica nella Parte I.

Rispetto agli appelli di giugno e luglio 2025:

- l'esercizio LCS non impone un limite massimo, ma una presenza obbligatoria;
- il vincolo sul colore è booleano: rosso già presente / rosso non ancora presente;
- l'esercizio sui grafi non richiede conteggi separati per più colori, ma un conteggio aggregato;
- gli archi A e B hanno lo stesso ruolo rispetto al vincolo;
- gli archi C hanno peso zero rispetto al conteggio.
```

---

## 8. Note metodologiche importanti

Codex deve evitare questi errori:

```md
> [!Warning]
> Nell'esercizio 1 non basta calcolare una LCS qualunque e poi controllare se contiene rosso.
> Bisogna integrare il vincolo nella DP, perché una LCS massima senza rosso potrebbe impedire di trovare correttamente la migliore LCS con rosso.

> [!Warning]
> Nell'esercizio 2 non servono due dimensioni separate per A e B, perché il testo chiede solo la somma `#A + #B = 3`.
> È sufficiente una dimensione di budget aggregato da 0 a 3.

> [!Warning]
> Gli archi C non vanno ignorati: possono comparire nel cammino, ma contribuiscono con peso 0.
```

---

## 9. Aggiornare PROJECT_STATUS.md

Aggiungere una riga nella tabella degli appelli:

```md
| 2025-11-10 Parte I Tema A | `parte-I-10nov25-A.pdf` | 2 | DP LCS con presenza colore, DP grafi con conteggio aggregato | cataloged |
```

Aggiornare il conteggio sintetico:

```md
Appelli analizzati:
- 2026-01-12
- 2025-07-03 Parte I
- 2025-06-09 Parte I
- 2025-11-10 Parte I Tema A
```

---

## 10. Aggiornare TODO.md

Aggiungere tra le possibili priorità future:

```md
## Soluzioni ad alta priorità

- [ ] Risolvere completamente `exam_2025_11_10_p1_tema_a_e01`
      perché è una variante semplice ma molto istruttiva di LCS con stato booleano.
- [ ] Risolvere completamente `exam_2025_11_10_p1_tema_a_e02`
      perché è una variante compatta della DP su grafi con conteggio esatto.
```

---

## 11. Commit consigliato

Dopo aver applicato tutte le modifiche:

```bash
git status
git add .
git commit -m "Ingest 2025-11-10 APA Parte I Tema A"
```

Prima del commit controllare:

```bash
find . -name "*2025_11_10*"
grep -R "exam_2025_11_10" .
grep -R "parte-I-10nov25-A" .
```

Verificare che non siano stati creati duplicati con nomi simili, per esempio:

```txt
exam_2025_11_10.md
exam_2025_11_10_part1.md
exam_2025_11_10_tema_a.md
```

Il naming standard da mantenere è:

```txt
exam_2025_11_10_part1_tema_a
```

---

## 12. Stato atteso finale

Dopo l'applicazione del piano, la KB deve contenere:

```txt
09_ingestion_reports/ingestion_report_exam_2025_11_10_part1_tema_a.md
02_transcriptions/exams/exam_2025_11_10_part1_tema_a.md
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e01.md
03_exercise_catalog/exercises/exam_2025_11_10_p1_tema_a_e02.md
```

e gli indici devono collegare correttamente il nuovo appello ai pattern:

```txt
- LCS con vincolo aggiuntivo
- LCS con presenza obbligatoria di colore
- DP booleana su grafi
- cammini con conteggio esatto
- programmazione dinamica Parte I
```
