---
type: method
status: interpreted
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/grafi-colorati
  - topic/cammini-su-grafi
  - topic/vincoli-su-colori
  - topic/stato-di-parita
---

# Metodo — DP su cammini con vincoli di parità sui colori

> [!Info]
> Stato: interpreted
> Famiglia: programmazione dinamica su grafi
> Appelli collegati:
> - [[exam_2025_09_17_p1_e02]]
> - [[exam_2025_02_11_p1_recupero_e02]]

## Quando usarlo

Usare questo metodo quando il testo dell'esercizio richiede di stabilire se esiste o qual è il cammino ottimo (es. minimo peso) in un grafo che soddisfa una proprietà legata alla parità (pari o dispari) del numero di archi di un certo colore o tipo, ad esempio:

- cammini con numero pari o dispari di archi totali;
- cammini in cui il numero di archi blu è dispari;
- cammini con un certo colore avente occorrenze di parità specifica.

## Idea

Partire dalla struttura classica dell'algoritmo di chiusura transitiva o di cammini minimi (Floyd-Warshall o DP bottom-up) ed estendere la definizione dello stato aggiungendo una dimensione per memorizzare la parità modulo 2 del conteggio degli archi specificati.

Rappresentiamo la parità modulo 2 tramite un indice:

$$
p \in \{0, 1\}
$$

dove:
- $p=0$ rappresenta un numero **pari** di archi target;
- $p=1$ rappresenta un numero **dispari** di archi target.

## Significato dello stato

Definire la ricorrenza:

$$
D[k, i, j, p]
$$

che indica se esiste (o il peso minimo di) un cammino dal vertice $i$ al vertice $j$ che:
- utilizza come vertici intermedi solo elementi del sottoinsieme $\{1, \dots, k\}$;
- soddisfa lo stato di parità $p$ modulo 2 per il conteggio degli archi target.

## Caso base ($k = 0$)

Considera i cammini senza vertici intermedi (archi diretti e cammini vuoti):

1. **Cammino vuoto da un vertice a sé stesso ($i = j$)**:
   Ha lunghezza 0 e non contiene archi target, quindi ha 0 archi target. Di conseguenza, ha parità pari ($p=0$):
   $$
   D[0, i, i, 0] = vero
   $$
   $$
   D[0, i, i, 1] = falso
   $$
2. **Archi diretti ($i \ne j$)**:
   - Se l'arco $(i,j) \in E$ è di tipo target (cambia la parità):
     $$
     D[0, i, j, 1] = vero
     $$
   - Se l'arco $(i,j) \in E$ non è di tipo target (non cambia la parità):
     $$
     D[0, i, j, 0] = vero
     $$
   - Le altre combinazioni e le coppie senza arco diretto sono impostate a `falso` (o $\infty$ per i pesi minimi).

## Passo ricorsivo

Durante la concatenazione dei cammini da $i$ a $k$ e da $k$ a $j$, le parità dei due sottocammini si sommano modulo 2. 
L'operazione matematica modulo 2 si traduce nell'operatore bitwise XOR $\oplus$:

$$
p_{totale} = q \oplus (p \oplus q)
$$

Pertanto, per stabilire l'esistenza nel passo ricorsivo:

$$
D[k, i, j, p] = D[k-1, i, j, p] \lor \bigvee_{q \in \{0,1\}} \left( D[k-1, i, k, q] \land D[k-1, k, j, p \oplus q] \right)
$$

### Esplicitazione per le due parità:

- **Per parità pari ($p=0$)**:
  Le due parti devono avere la stessa parità per annullarsi a vicenda modulo 2:
  $$
  D[k, i, j, 0] = D[k-1, i, j, 0] \lor (D[k-1, i, k, 0] \land D[k-1, k, j, 0]) \lor (D[k-1, i, k, 1] \land D[k-1, k, j, 1])
  $$
- **Per parità dispari ($p=1$)**:
  Una parte deve essere pari e l'altra dispari:
  $$
  D[k, i, j, 1] = D[k-1, i, j, 1] \lor (D[k-1, i, k, 0] \land D[k-1, k, j, 1]) \lor (D[k-1, i, k, 1] \land D[k-1, k, j, 0])
  $$

---

## Errori comuni

> [!Warning]
> **Errore di granularità dello stato**: Non basta calcolare se esiste un cammino e poi controllarne la lunghezza. Lo stato della parità deve far parte della tabella DP altrimenti i cammini validi vengono sovrascritti o ignorati nel passo ricorsivo.

> [!Warning]
> **Cammino vuoto**: Il cammino vuoto da un vertice a sé stesso ha sempre parità pari (0 archi target). Impostare a `falso` $D[0, i, i, 0]$ rende l'algoritmo errato.

> [!Warning]
> **Ignorare archi non target**: Gli archi non target (es. neri o rossi se si contano i blu) non modificano la parità ma consentono comunque la raggiungibilità. Devono essere censiti come cammini validi con parità pari ($p=0$) nel caso base.
