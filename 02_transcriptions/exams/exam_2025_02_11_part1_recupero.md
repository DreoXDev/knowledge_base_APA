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

---

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
