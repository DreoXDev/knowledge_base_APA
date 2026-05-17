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

su un alfabeto $S$, ogni simbolo ha colore rosso ($R$), blu ($B$) o nero ($N$) definito da una funzione:

$$
col:S \to \{R,B,N\}
$$

Si vuole determinare la lunghezza di una più lunga sottosequenza comune di $X$, $Y$ e $W$ che contenga al massimo due simboli rossi.

Fornire:
1. la definizione dei coefficienti che si intendono calcolare;
2. la definizione del caso base;
3. il passo ricorsivo, spiegando chiaramente le scelte effettuate;
4. il coefficiente della tabella che fornisce il valore ottimo cercato;
5. un algoritmo in pseudocodice bottom-up per il calcolo del valore ottimo;
6. un algoritmo ricorsivo in pseudocodice per la ricostruzione di una sottosequenza ottima.

---

## Esercizio 2 — Cammini senza due neri o due blu consecutivi

Dato un grafo $(V,E,col)$ senza cappi, ogni arco ha un colore rosso ($R$), nero ($N$) o blu ($B$) definito da una funzione:

$$
col:E \to C
$$

dove:

$$
C = \{R,N,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole stabilire se esiste un cammino da $i$ a $j$ nel quale:

- non vi sono due archi consecutivi neri ($NN$);
- non vi sono due archi consecutivi blu ($BB$).

Fornire:
1. la definizione dei coefficienti che si intendono calcolare;
2. la definizione del caso base;
3. il passo ricorsivo, spiegando chiaramente le scelte effettuate;
4. la soluzione finale per ogni coppia di vertici $(i,j)$.
