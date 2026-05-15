---
type: pattern
topic: programmazione-dinamica-su-grafi
status: scaffold
tags:
  - apa
  - pattern
  - topic/programmazione-dinamica
  - topic/grafi
  - topic/grafi-colorati
  - topic/problema-ausiliario
---

# Pattern - DP booleana su grafi con vincoli locali

## Descrizione

Variante di DP booleana su grafi in cui la validita di un cammino dipende da coppie di archi consecutivi o da informazioni locali agli estremi del sottocammino.

## Appelli in cui compare

| Appello | Esercizio | Variante |
|---|---|---|
| [[exam_2025_06_09_part1]] | [[exam_2025_06_09_p1_e02]] | Vincoli di precedenza tra colori degli archi |

## Metodo principale

- [[metodo_dp_cammini_colori_precedenze]]

## Varianti collegate

- [[dp_booleana_su_grafi]]
- [[dp_booleana_su_grafi_con_conteggi_colori]]

> [!Warning]
> Probabile necessita di un problema ausiliario con colore iniziale e/o finale del cammino.

