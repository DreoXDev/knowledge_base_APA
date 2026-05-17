---
type: method
status: scaffold
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/cammini-minimi
  - topic/colori
  - topic/parita
---

# Metodo — Cammini minimi con vincoli di colore e parità

## Quando usarlo

Usare questo metodo quando il testo chiede un cammino minimo tra coppie di vertici su grafi colorati e pesati, con vincoli aggiuntivi come:

- parità del numero di archi di un certo colore (es. dispari o pari);
- numero pari/dispari di archi totali;
- vincoli locali su archi o vertici consecutivi;
- assenza di coppie consecutive vietate.

## Schema generale (Floyd-Warshall Esteso)

Si estende l'algoritmo di Floyd-Warshall aggiungendo dimensioni allo stato per tenere traccia delle proprietà accumulate.

Esempio di stato:

$$
D[k,i,j,p]
$$

dove:
- $k$ indica i vertici intermedi utilizzabili $\{1,\dots,k\}$;
- $i,j$ sono la sorgente e la destinazione;
- $p$ rappresenta lo stato di parità o di conteggio (es. $p \in \{0,1\}$ per pari/dispari).

## Caso base ($k=0$)

Si considerano solo i cammini vuoti e gli archi diretti:

- Cammino vuoto:
  $$
  D[0,i,i,0] = 0
  $$
  $$
  D[0,i,i,1] = +\infty
  $$
- Archi diretti: per ogni $(i,j) \in E$, se rispettano i vincoli locali (es. non sono entrambi rossi):
  $$
  D[0,i,j,blu(i,j)] = W(i,j)
  $$
- Tutti gli altri valori sono impostati a $+\infty$.

## Passo ricorsivo ($k \ge 1$)

Concatenare due cammini parziali passanti per il vertice $k$ combinando gli stati tramite l'operazione di combinazione corretta (es. XOR per la parità modulo 2):

$$
D[k,i,j,p] =
\min
\left(
D[k-1,i,j,p],
\min_{q}
\left[
D[k-1,i,k,q] + D[k-1,k,j,p \oplus q]
\right]
\right)
$$

## Errori comuni da evitare

> [!Warning]
> **DP Booleana**: Non usare una tabella booleana (0/1 o True/False) se il problema richiede di trovare un cammino minimo di peso $W$. I coefficienti devono contenere i pesi effettivi del cammino.

> [!Warning]
> **Parità nello Stato**: Non fare l'errore di calcolare il cammino minimo assoluto tramite Floyd-Warshall classico per poi verificare se soddisfa la parità. Il cammino con il peso minimo assoluto potrebbe avere un numero pari di archi blu, mentre un cammino leggermente più pesante potrebbe rispettare il vincolo dispari. La parità va integrata nello stato DP.

> [!Warning]
> **Vincoli locali**: I vincoli locali su vertici o archi consecutivi vanno garantiti già sugli archi diretti del caso base.

## Esercizi collegati

- [[exam_2025_02_11_p1_recupero_e02]]
- [[exam_2026_01_12_e02]]

## Teoria collegata

- [[cammini_minimi]]
- [[floyd_warshall]]
- [[grafi_colorati]]
