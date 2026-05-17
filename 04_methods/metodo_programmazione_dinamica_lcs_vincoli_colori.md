---
type: method
status: scaffold
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/vincoli-di-conteggio
  - topic/colori
---

# Metodo - LCS con vincoli sui colori

## Quando si usa

Quando si cerca una sottosequenza comune massima tra due sequenze, ma la soluzione deve rispettare vincoli sul numero di simboli di certi colori.

## Stato tipico

Un possibile stato e:

$$
c_{i,j,r,b}
$$

dove:

- $i$ e $j$ indicano i prefissi delle due sequenze;
- $r$ e il numero massimo di simboli rossi utilizzabili;
- $b$ e il numero massimo di simboli blu utilizzabili.

## Soluzione finale tipica

Per il caso dell'appello 2025-06-09:

$$
c_{m,n,2,3}
$$

Per il caso dell'appello 2025-11-10 (presenza obbligatoria, stato booleano):

$$
c_{m,n,1}
$$

## Esercizi collegati

- [[exam_2025_06_09_p1_e01]]
- [[exam_2025_07_03_p1_e01]]
- [[exam_2025_11_10_p1_tema_a_e01]]

## Teoria necessaria

- [[programmazione_dinamica]]
- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]

## Errori comuni

- Dimenticare di diminuire il contatore corretto quando si sceglie un simbolo rosso o blu.
- Diminuire un contatore quando il simbolo e nero.
- Trattare come scegliibile un simbolo se $x_i \ne y_j$.
- Ricostruire la soluzione senza verificare quale caso della ricorrenza ha prodotto il massimo.

> [!Warning]
> Metodo da completare durante la fase di soluzione.

