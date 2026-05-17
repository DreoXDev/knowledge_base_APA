# Piano Codex — Ingestion appello APA 2025-02-11 Parte I recupero parziale

## Obiettivo

Integrare nella knowledge base APA l'appello:

```txt
Analisi e Progetto di Algoritmi — Parte I
Data: 11 febbraio 2025
Tipo: recupero parziale
File sorgente: parteI-11feb25-recupero.pdf
```

L'appello contiene 2 esercizi di programmazione dinamica:

1. LCS comune a tre sequenze con vincolo di al massimo due simboli rossi.
2. Cammini minimi su grafo pesato con due vincoli:
   - numero dispari di archi blu;
   - assenza di due vertici consecutivi rossi.

> [!Important]
> L'esercizio 1 è sostanzialmente identico a quello dello scritto completo `parteI-11feb25-completo.pdf`.
> Codex non deve duplicare metodo e teoria: deve collegare questo esercizio allo stesso pattern/metodo già usato per `exam_2025_02_11_p1_completo_e01`.

L'appello va integrato nella KB come fonte distinta, ma riusando i contenuti metodologici già presenti quando coincidono.

---

## 1. File da creare

Creare il report di ingestion:

```txt
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_recupero.md
```

Creare la trascrizione dell'appello:

```txt
02_transcriptions/exams/exam_2025_02_11_part1_recupero.md
```

Creare i due esercizi catalogati:

```txt
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e01.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e02.md
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

Creare o aggiornare un metodo specifico per il secondo esercizio:

```txt
04_methods/metodo_cammini_minimi_vincoli_colori_parita.md
```

Eventualmente creare solo se non esiste già un metodo equivalente:

```txt
04_methods/metodo_floyd_warshall_stato_esteso.md
```

Aggiornare teoria minima:

```txt
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/vincoli_su_colori.md
05_theory/grafi_colorati.md
05_theory/cammini_minimi.md
05_theory/floyd_warshall.md
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
02_transcriptions/exams/exam_2025_02_11_part1_recupero.md
```

inserire una trascrizione leggera, non verbosa, con questa struttura:

```md
# Appello 2025-02-11 — Parte I recupero parziale

> [!Info]
> Fonte: `parteI-11feb25-recupero.pdf`
> Stato: transcribed
> Tipo: appello Parte I, recupero parziale
> Argomenti principali: programmazione dinamica, LCS a tre sequenze, vincoli sui colori, cammini minimi vincolati

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

> [!Note]
> Questo esercizio coincide con l'esercizio 1 dello scritto completo dell'11 febbraio 2025.

## Esercizio 2 — Cammini minimi con numero dispari di archi blu e senza due vertici rossi consecutivi

Dato un grafo pesato sugli archi:

$$
(V,E,W,f,g)
$$

senza cappi e senza cicli di peso negativo.

Ogni vertice ha un colore:

$$
f:V \to C
$$

dove:

$$
C = \{R,N\}
$$

Ogni arco ha un colore:

$$
g:E \to D
$$

dove:

$$
D = \{M,B\}
$$

Si vuole calcolare, per ogni coppia di vertici $(i,j)$, il peso di un cammino minimo da $i$ a $j$ che soddisfi entrambe le condizioni:

- il cammino contiene un numero dispari di archi blu;
- nel cammino non vi sono due vertici consecutivi rossi.

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
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e01.md
```

Contenuto consigliato:

```md
# exam_2025_02_11_p1_recupero_e01 — LCS a tre sequenze con al massimo due rossi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_recupero]]
> Stato: cataloged
> Tipologia: programmazione dinamica su sequenze
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_lcs_tre_sequenze_vincolo_colori]]

## Problema

Date tre sequenze $X$, $Y$ e $W$ su un alfabeto $S$, ogni simbolo ha colore rosso, blu o nero tramite:

$$
col:S \to \{R,B,N\}
$$

Si vuole trovare una sottosequenza comune di lunghezza massima tra $X$, $Y$ e $W$ che contenga al massimo due simboli rossi.

## Nota di duplicazione controllata

Questo esercizio coincide con:

```txt
exam_2025_02_11_p1_completo_e01
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
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e02.md
```

Contenuto consigliato:

```md
# exam_2025_02_11_p1_recupero_e02 — Cammini minimi con parità blu e vincolo sui vertici rossi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_recupero]]
> Stato: cataloged
> Tipologia: programmazione dinamica su grafi pesati
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_cammini_minimi_vincoli_colori_parita]]

## Problema

Dato un grafo pesato sugli archi:

$$
(V,E,W,f,g)
$$

senza cappi e senza cicli di peso negativo.

Ogni vertice ha un colore:

$$
f:V \to \{R,N\}
$$

Ogni arco ha un colore:

$$
g:E \to \{M,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole calcolare il peso di un cammino minimo da $i$ a $j$ tale che:

1. il numero di archi blu sia dispari;
2. non vi siano due vertici consecutivi rossi.

## Pattern riconosciuto

È una variante di cammini minimi con programmazione dinamica in stile Floyd-Warshall, ma con stato esteso.

Rispetto a Floyd-Warshall classico, lo stato deve ricordare:

- la parità del numero di archi blu;
- la validità del vincolo locale sui vertici rossi consecutivi.

Il vincolo sui vertici consecutivi può essere controllato localmente quando si considera un arco diretto o quando si concatena due sottocammini.

## Predicati e funzioni ausiliarie

Definire il peso dell'arco:

$$
W(i,j)
$$

se $(i,j) \in E$.

Definire il contributo di parità dell'arco:

$$
blu(i,j) =
\begin{cases}
1 & \text{se } g(i,j)=B \\
0 & \text{se } g(i,j)=M
\end{cases}
$$

Definire il predicato che vieta due vertici rossi consecutivi:

$$
ok(i,j) =
\neg(f(i)=R \land f(j)=R)
$$

per ogni arco o concatenazione in cui $i$ e $j$ diventano consecutivi.

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

$D[k,i,j,p]$ è il peso minimo di un cammino da $i$ a $j$ che:

- usa come vertici intermedi solo vertici in $\{1,\dots,k\}$;
- contiene un numero di archi blu con parità $p$;
- non contiene due vertici consecutivi rossi.

Dove:

- $p=0$ indica numero pari di archi blu;
- $p=1$ indica numero dispari di archi blu.

Usare $+\infty$ per stati impossibili.

## Caso base

Per $k=0$, sono ammessi solo cammini diretti e cammini vuoti.

Cammino vuoto:

$$
D[0,i,i,0] = 0
$$

$$
D[0,i,i,1] = +\infty
$$

Arco diretto $(i,j) \in E$:

se:

$$
ok(i,j)
$$

allora:

$$
D[0,i,j,blu(i,j)] = W(i,j)
$$

Gli altri coefficienti sono:

$$
+\infty
$$

Se esistono più archi tra la stessa coppia, usare il minimo tra gli archi compatibili con lo stato di parità.

## Passo ricorsivo

Per $k \ge 1$:

$$
D[k,i,j,p] =
\min
\left(
D[k-1,i,j,p],
\min_{q \in \{0,1\}}
\left[
D[k-1,i,k,q] + D[k-1,k,j,p \oplus q]
\right]
\right)
$$

dove $\oplus$ è lo XOR/parità modulo 2.

> [!Warning]
> Questa ricorrenza è valida assumendo che i due sottocammini siano già validi rispetto al vincolo "nessuna coppia di vertici rossi consecutivi".
> La concatenazione in $k$ non crea una nuova coppia di vertici consecutivi non già presente, perché il vertice $k$ è endpoint del primo sottocammino ed endpoint del secondo sottocammino.
> Le coppie consecutive rilevanti sono già state controllate nei sottocammini e negli archi diretti del caso base.

## Soluzione

Per ogni coppia $(i,j)$, il peso richiesto è:

$$
D[n,i,j,1]
$$

perché $p=1$ corrisponde a un numero dispari di archi blu.

Se:

$$
D[n,i,j,1] = +\infty
$$

allora non esiste alcun cammino da $i$ a $j$ che soddisfi entrambi i vincoli.

## Collegamenti

- [[cammini_minimi]]
- [[floyd_warshall]]
- [[grafi_colorati]]
- [[metodo_cammini_minimi_vincoli_colori_parita]]
- [[metodo_floyd_warshall_stato_esteso]]
- [[parte_i_dynamic_programming_patterns]]
```

---

## 6. Metodo da creare o aggiornare per l'esercizio 2

Creare, se non esiste già:

```txt
04_methods/metodo_cammini_minimi_vincoli_colori_parita.md
```

Struttura consigliata:

```md
# Metodo — Cammini minimi con vincoli di colore e parità

> [!Info]
> Stato: interpreted
> Famiglia: programmazione dinamica su grafi pesati
> Appelli collegati:
> - [[exam_2025_02_11_p1_recupero_e02]]

## Quando usarlo

Usare questo metodo quando il testo chiede un cammino minimo tra coppie di vertici con vincoli aggiuntivi come:

- parità del numero di archi di un certo colore;
- numero pari/dispari di archi;
- vincoli locali su vertici o archi consecutivi;
- assenza di coppie vietate.

## Schema generale

Partire da Floyd-Warshall e aggiungere dimensioni allo stato.

Esempio:

$$
D[k,i,j,p]
$$

dove $p$ rappresenta una proprietà accumulata lungo il cammino, per esempio la parità degli archi blu.

## Caso base

Inizializzare:

- cammini vuoti;
- archi diretti;
- stati impossibili a $+\infty$;
- vincoli locali sugli archi diretti.

## Passo ricorsivo

Concatenare sottocammini passando per il vertice $k$:

$$
D[k,i,j,p] =
\min
\left(
D[k-1,i,j,p],
\min_q D[k-1,i,k,q] + D[k-1,k,j,p \oplus q]
\right)
$$

## Errori comuni

> [!Warning]
> Non usare una DP booleana se il problema chiede il peso minimo.

> [!Warning]
> Non dimenticare lo stato per la parità: il cammino minimo assoluto potrebbe non avere un numero dispari di archi blu.

> [!Warning]
> I vincoli locali sui vertici consecutivi vanno controllati già sugli archi diretti del caso base.
```

---

## 7. Pattern da aggiornare

Aggiornare:

```txt
06_exam_patterns/recurring_exercise_types.md
```

aggiungendo l'appello 2025-02-11 recupero alla famiglia:

```md
## Programmazione dinamica Parte I

Appelli collegati:

- [[exam_2026_01_12]]
- [[exam_2025_11_10_part1_tema_a]]
- [[exam_2025_07_03_part1]]
- [[exam_2025_06_09_part1]]
- [[exam_2025_02_11_part1_completo]]
- [[exam_2025_02_11_part1_recupero]]
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
```

Aggiungere o rafforzare una sottosezione:

```md
## Cammini minimi vincolati

Il recupero parziale del 2025-02-11 introduce una variante più pesata della famiglia DP su grafi:

- non si chiede solo esistenza;
- si chiede il peso minimo;
- il grafo è pesato;
- non ci sono cicli di peso negativo;
- lo stato deve mantenere la parità degli archi blu.
```

---

## 8. Differenza rispetto agli appelli già analizzati

Aggiungere in:

```txt
06_exam_patterns/variations_by_appeal.md
```

una nota del tipo:

```md
## 2025-02-11 Parte I recupero parziale

Questo appello è molto simile allo scritto completo dell'11 febbraio 2025 per quanto riguarda l'esercizio 1, ma cambia in modo significativo l'esercizio 2.

### Esercizio 1

L'esercizio 1 coincide con la variante:

```txt
LCS a tre sequenze con al massimo due rossi
```

già presente nello scritto completo.

Va quindi collegato allo stesso metodo senza creare duplicati inutili.

### Esercizio 2

L'esercizio 2 introduce una variante più complessa della DP su grafi:

- il grafo è pesato;
- si chiede un cammino minimo, non solo l'esistenza di un cammino;
- il vincolo sugli archi è di parità: numero dispari di archi blu;
- il vincolo sui vertici è locale: non ci sono due vertici consecutivi rossi;
- la tecnica naturale è una variante di Floyd-Warshall con stato esteso per la parità.

Questa variante è importante perché collega le DP booleane su grafi già viste con il tema dei cammini minimi.
```

---

## 9. Note metodologiche importanti

Codex deve evitare questi errori:

```md
> [!Warning]
> Non duplicare il metodo dell'esercizio 1 se è già stato creato per lo scritto completo dell'11 febbraio 2025.
> L'esercizio è uguale e va collegato allo stesso metodo.

> [!Warning]
> Nell'esercizio 2 non basta calcolare un cammino minimo classico e poi controllare se rispetta i vincoli.
> I vincoli devono essere integrati nello stato della DP.

> [!Warning]
> Nell'esercizio 2 il problema chiede il peso minimo, quindi i coefficienti devono contenere valori numerici, non booleani.

> [!Warning]
> Il vincolo "numero dispari di archi blu" richiede uno stato di parità.
> Sono sufficienti due stati: pari e dispari.

> [!Warning]
> Il vincolo "non vi sono due vertici consecutivi rossi" riguarda coppie di vertici adiacenti lungo il cammino.
> Va controllato sugli archi diretti nel caso base.

> [!Warning]
> Gli archi marroni non contribuiscono alla parità degli archi blu.
> Gli archi blu cambiano la parità.
```

---

## 10. Aggiornare PROJECT_STATUS.md

Aggiungere una riga nella tabella degli appelli:

```md
| 2025-02-11 Parte I recupero parziale | `parteI-11feb25-recupero.pdf` | 2 | DP LCS a tre sequenze con budget rossi, cammini minimi con parità blu e vincoli sui vertici | cataloged |
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
```

---

## 11. Aggiornare TODO.md

Aggiungere tra le possibili priorità future:

```md
## Soluzioni ad alta priorità

- [ ] Risolvere completamente `exam_2025_02_11_p1_recupero_e02`
      perché introduce la variante dei cammini minimi pesati con stato esteso.
```

Aggiungere anche una nota di deduplicazione:

```md
## Deduplicazione contenuti

- [ ] Verificare che `exam_2025_02_11_p1_completo_e01` e `exam_2025_02_11_p1_recupero_e01`
      puntino allo stesso metodo senza duplicare spiegazioni teoriche.
```

Aggiungere una possibile nota di consolidamento:

```md
## Consolidamento metodi Parte I

- [ ] Creare una tabella comparativa delle varianti DP su grafi distinguendo:
      - problemi di esistenza;
      - problemi di conteggio/parità;
      - problemi di cammino minimo;
      - vincoli locali su archi o vertici consecutivi.
```

---

## 12. Commit consigliato

Dopo aver applicato tutte le modifiche:

```bash
git status
git add .
git commit -m "Ingest 2025-02-11 APA Parte I recovery exam"
```

Prima del commit controllare:

```bash
find . -name "*2025_02_11*"
grep -R "exam_2025_02_11_p1_recupero" .
grep -R "parteI-11feb25-recupero" .
```

Verificare che non siano stati creati duplicati con nomi simili, per esempio:

```txt
exam_2025_02_11_recupero.md
exam_2025_02_11_part1_recovery.md
exam_2025_02_11_parziale.md
```

Il naming standard da mantenere è:

```txt
exam_2025_02_11_part1_recupero
```

---

## 13. Stato atteso finale

Dopo l'applicazione del piano, la KB deve contenere:

```txt
09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_recupero.md
02_transcriptions/exams/exam_2025_02_11_part1_recupero.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e01.md
03_exercise_catalog/exercises/exam_2025_02_11_p1_recupero_e02.md
```

e gli indici devono collegare correttamente il nuovo appello ai pattern:

```txt
- LCS con vincolo aggiuntivo
- LCS a tre sequenze
- LCS con budget sui colori
- DP su grafi con stato esteso
- cammini minimi vincolati
- Floyd-Warshall con stato esteso
- parità degli archi blu
- vincolo sui vertici rossi consecutivi
- programmazione dinamica Parte I
```

---

## 14. Nota finale per Codex

Questo appello va trattato come fonte distinta, ma con attenzione alla duplicazione:

- l'esercizio 1 è una ripetizione utile del pattern LCS a tre sequenze con massimo due rossi;
- l'esercizio 2 è invece nuovo e importante perché sposta la famiglia delle DP su grafi dal caso booleano/esistenza al caso di ottimizzazione con cammini minimi.

La priorità è integrare bene l'esercizio 2 nei pattern di Parte I, perché aggiunge una variante ad alta resa per l'esame.
