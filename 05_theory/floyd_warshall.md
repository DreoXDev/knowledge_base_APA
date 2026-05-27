---
type: theory
topic: floyd-warshall
status: scaffold
tags:
  - apa
  - teoria
  - topic/grafi
  - topic/floyd-warshall
---

# Teoria — Floyd-Warshall

## Definizione minima

L'algoritmo di Floyd-Warshall è un algoritmo di programmazione dinamica che risolve il problema dei cammini minimi tra tutte le coppie di nodi in un grafo pesato (All-Pairs Shortest Path), gestendo anche pesi negativi (purché non vi siano cicli di peso negativo).

La sua formulazione standard si basa su un coefficiente $d_{i,j}^{(k)}$ che rappresenta il peso del cammino minimo da $i$ a $j$ usando solo nodi intermedi nell'insieme $\{1,\dots,k\}$.

## Floyd-Warshall Esteso

Nei problemi di esame APA, l'algoritmo viene spesso esteso aggiungendo indici di stato per tracciare proprietà accumulative (es. parità modulo 2, conteggio esatto, o consecutività locali), che consentono di filtrare i cammini intermedi validi in base a vincoli aggiuntivi.

## Collegamenti agli esercizi

- [[exam_2025_02_11_p1_recupero_e02]]
- [[exam_2026_01_12_e02]]
- [[exam_2025_07_03_p1_e02]]
- [[exam_2025_07_03_p2_e03]]
- [[exam_2025_06_09_p1_e02]]
- [[exam_2025_11_10_p1_tema_a_e02]]
- [[exam_2025_02_11_p1_completo_e02]]

## Collegamenti ai metodi

- [[metodo_cammini_minimi_vincoli_colori_parita]]
- [[metodo_dp_cammini_colori_conteggi]]
- [[metodo_dp_cammini_colori_precedenze]]
- [[metodo_equazioni_ricorrenza_chiusura_transitiva]]

> [!Warning]
> Nota scaffold: completare con la ricorrenza standard per il confronto nei riassunti di teoria.

## Integrazione SRC-NOTE-001

Fonte: [[source_inventory]] / SRC-NOTE-001, pagine 24-32 e 38-39.

## Ricorrenza classica

$$
D^k[i,j]=\min(D^{k-1}[i,j],D^{k-1}[i,k]+D^{k-1}[k,j]).
$$

Nella versione booleana:

$$
R^k[i,j]=R^{k-1}[i,j]\lor(R^{k-1}[i,k]\land R^{k-1}[k,j]).
$$

## Variante con stato esteso

Vedi [[dp_grafi_floyd_warshall_stato_esteso]].
