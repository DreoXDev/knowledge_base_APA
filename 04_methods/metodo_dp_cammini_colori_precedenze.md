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
  - topic/problema-ausiliario
---

# Metodo - DP su cammini con vincoli di precedenza tra colori

## Quando si usa

Quando bisogna stabilire l'esistenza di un cammino tra coppie di vertici che rispetta vincoli locali tra colori di archi consecutivi.

## Vincoli tipici

Nel caso dell'appello 2025-06-09 non sono ammesse le coppie consecutive:

$$
(R,N) \quad \text{e} \quad (B,R)
$$

Nel caso dell'appello 2025-02-11 (completo), non sono ammesse le coppie consecutive identiche di colore nero o blu:

$$
(N,N) \quad \text{e} \quad (B,B)
$$

## Problema ausiliario

Il problema principale "esiste un cammino valido da $i$ a $j$?" può richiedere un problema ausiliario che tenga traccia di informazioni aggiuntive sui colori agli estremi del cammino.

Un possibile stato contiene:

- vertici estremi $i,j$;
- limite sui vertici intermedi;
- colore del primo arco del cammino;
- colore dell'ultimo arco del cammino.

Queste informazioni permettono di verificare se due sottocammini possono essere concatenati senza violare i vincoli locali.

## Esercizi collegati

- [[exam_2025_06_09_p1_e02]]
- [[exam_2025_07_03_p1_e02]]
- [[exam_2026_01_12_e02]]
- [[exam_2025_02_11_p1_completo_e02]]

## Teoria necessaria

- [[grafi]]
- [[grafi_colorati]]
- [[vincoli_su_colori]]
- [[programmazione_dinamica_su_grafi]]

## Errori comuni

- Non introdurre il problema ausiliario nonostante il vincolo locale.
- Verificare solo il colore dell'arco corrente senza sapere il colore precedente.
- Confondere "preceduto da" con "seguito da".
- Dimenticare che il vincolo riguarda archi consecutivi nel cammino, non tutti gli archi del grafo.

> [!Warning]
> Verificare la notazione specifica del corso prima di trasformarlo in metodo definitivo.

