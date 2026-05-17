---
type: method
status: scaffold
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/grafi-colorati
  - topic/dp-booleana
---

# Metodo - DP su cammini con conteggi di colori

## Quando si usa

Quando bisogna stabilire l'esistenza di un cammino tra coppie di vertici che rispetta vincoli sul numero di archi di certi colori.

## Stato tipico

Un possibile stato e:

$$
c_{h,i,j,r,b}
$$

dove:

- $h$ limita i vertici intermedi utilizzabili;
- $i,j$ sono estremi del cammino;
- $r$ e il numero di archi rossi usati;
- $b$ e il numero di archi blu usati.

Nel caso di somme o conteggi aggregati (es. appello 2025-11-10, somma archi A e B uguale a 3), lo stato si semplifica riducendo le dimensioni a una sola variabile di budget aggregato $h \in \{0,\dots,W\}$:

$$
c_{k,i,j,h}
$$

## Esercizi collegati

- [[exam_2025_07_03_p1_e02]]
- [[exam_2025_06_09_p1_e02]]
- [[exam_2026_01_12_e02]]
- [[exam_2025_11_10_p1_tema_a_e02]]

## Varianti collegate

- [[metodo_dp_cammini_colori_precedenze]]

## Teoria necessaria

- [[grafi]]
- [[grafi_colorati]]
- [[programmazione_dinamica_su_grafi]]

## Errori comuni

- Non contare correttamente gli archi rossi e blu nei casi base.
- Confondere cammino con arco diretto.
- Dimenticare che gli archi neri non aumentano ne il conteggio rosso ne il conteggio blu.
- Non considerare la composizione di due cammini passando per un vertice intermedio.

> [!Warning]
> Verificare la notazione specifica del corso prima di trasformarlo in metodo definitivo.
