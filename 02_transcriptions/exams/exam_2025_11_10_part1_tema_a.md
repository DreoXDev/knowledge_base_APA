---
type: exam_transcription
source: 01_sources/exams_raw/parte-I-10nov25-A.pdf
source_id: SRC-EXAM-012
exam_date: 2025-11-10
part: Parte I
theme: Tema A
status: transcribed
tags:
  - apa
  - appello
  - exam/raw
  - parte-i
---

# Appello 2025-11-10 — Parte I Tema A

> [!Info]
> Fonte: `parte-I-10nov25-A.pdf`
> Stato: transcribed
> Tipo: appello Parte I
> Argomenti principali: programmazione dinamica, LCS con vincoli, cammini su grafi etichettati

## Esercizio 1 — LCS con presenza obbligatoria del rosso

Date due sequenze $X = \langle x_1,\dots,x_m \rangle$ e $Y = \langle y_1,\dots,y_n \rangle$ su un alfabeto $S$, a ogni simbolo è associato un colore tramite la funzione:

$$
col:S \to \{R,B,N\}
$$

che indica se il simbolo è rosso ($R$), blu ($B$) o nero ($N$).

Mediante programmazione dinamica, si vuole determinare una più lunga sottosequenza comune di $X$ e $Y$ nella quale sia presente almeno un simbolo rosso.

Richieste:
1. definire i coefficienti, ognuno contenente la lunghezza di un'opportuna LCS in un sottoproblema;
2. scrivere il caso base;
3. scrivere il passo ricorsivo;
4. specificare la soluzione in termini di lunghezza;
5. scrivere l'algoritmo bottom-up;
6. scrivere l'algoritmo ricorsivo di ricostruzione della soluzione del generico sottoproblema.

## Esercizio 2 — Cammini con somma di archi A/B uguale a 3

Dato un grafo $(V,E,f)$ senza cappi, in cui a ogni arco è associata una lettera tramite la funzione:

$$
f:E \to L
$$

dove:

$$
L = \{A,B,C\}
$$

Mediante programmazione dinamica, si vuole stabilire per ogni coppia di vertici $(i,j)$ se esiste un cammino da $i$ a $j$ nel quale la somma tra il numero di archi con lettera A e il numero di archi con lettera B sia uguale a 3.

Richieste:
1. definire i coefficienti;
2. scrivere il caso base;
3. scrivere il passo ricorsivo;
4. indicare qual è la soluzione del problema.
