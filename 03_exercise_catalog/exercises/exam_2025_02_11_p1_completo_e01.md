---
type: exercise
source: 01_sources/exams_raw/parteI-11feb25-completo.pdf
source_id: SRC-EXAM-003
exam_date: 2025-02-11
part: Parte I
exercise_number: 1
points: 31
status: cataloged
difficulty: alta
tags:
  - apa
  - esercizio
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/sottosequenze-comuni
  - topic/vincoli-su-colori
  - topic/stato-di-budget
  - status/cataloged
---

# exam_2025_02_11_p1_completo_e01 — LCS a tre sequenze con al massimo due rossi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_completo]]
> Stato: cataloged
> Tipologia: programmazione dinamica su sequenze
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_programmazione_dinamica_lcs_vincoli_colori]], [[metodo_lcs_tre_sequenze_vincolo_colori]]

## Problema

Date tre sequenze $X$, $Y$ e $W$ su un alfabeto $S$, ogni simbolo ha colore rosso ($R$), blu ($B$) o nero ($N$) tramite una funzione:

$$
col:S \to \{R,B,N\}
$$

Si vuole trovare una sottosequenza comune di lunghezza massima tra $X$, $Y$ e $W$ che contenga al massimo due simboli rossi.

## Pattern riconosciuto

È una variante della LCS classica con due estensioni:

1. la LCS è tra tre sequenze invece che tra due;
2. lo stato deve tenere conto del numero di simboli rossi usati (stato di budget).

Rispetto ad altri appelli già analizzati, questa variante combina la complessità tridimensionale degli indici di sequenza con una dimensione di budget supplementare.

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

$C[i,j,k,r]$ è la lunghezza massima di una sottosequenza comune tra i prefissi:

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
> Usiamo una semantica "al massimo $r$ rossi" perché semplifica la scrittura dei casi ricorsivi senza richiedere massimi esterni complessi alla fine.

## Caso base

Se almeno una delle tre sequenze considerate è vuota, la lunghezza della LCS è 0:

$$
C[0,j,k,r] = 0 \quad \forall j,k,r
$$

$$
C[i,0,k,r] = 0 \quad \forall i,k,r
$$

$$
C[i,j,0,r] = 0 \quad \forall i,j,r
$$

## Passo ricorsivo

Per $i \ge 1, j \ge 1, k \ge 1$:

Se i simboli finali non coincidono, cioè non vale $x_i = y_j = w_k$:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r]
\end{cases}
$$

Se invece i simboli coincidono, cioè $x_i = y_j = w_k$:

### Caso A: Il simbolo comune NON è rosso ($col(x_i) \ne R$)

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

### Caso B: Il simbolo comune È rosso ($col(x_i) = R$)

Per $r > 0$ (abbiamo budget residuo per accogliere il rosso):

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

Per $r = 0$ (non possiamo prendere il rosso poiché il budget di rossi consentiti è nullo):

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

La lunghezza della soluzione ottima cercata è memorizzata in:

$$
C[m,n,d,2]
$$

## Collegamenti

- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[metodo_lcs_tre_sequenze_vincolo_colori]]
