---
type: solved-example
topic: lcs-due-rossi-consecutivi
status: official_confirmed
source_id: SRC-OFFICIAL-EX-014
source_file: 01_sources/extra_materials/lcs-atleast-2-consecutive-red.pdf
tags:
  - apa
  - esempio-svolto
  - topic/lcs
  - topic/colori
---

# Schema soluzione - LCS con due rossi consecutivi

## Riconoscimento

Traccia tipica: "Date due sequenze `X,Y` e una funzione colore, trovare una LCS in cui siano presenti due elementi rossi consecutivi."

## Soluzione da esame

1. Definire stati ausiliari vincolati a terminare con `x_i = y_j`.
2. Usare `c_ij1` per sottosequenze dove la coppia di rossi consecutivi e gia presente.
3. Usare `c_ij0` per sottosequenze dove la coppia non e ancora presente.
4. Mettere `-infinito` quando lo stato non esiste, in particolare se `x_i != y_j`.
5. Scrivere le ricorrenze distinguendo `col(x_i)=red` e `col(x_i)!=red`.
6. Calcolare il valore ottimo come massimo globale dei `c_ij1`.

## Warning

- "Consecutivi" significa consecutivi nella sottosequenza.
- Non basta contare almeno due rossi totali.
- Non usare `c_{m,n}`.

Metodo: [[dp_lcs_due_rossi_consecutivi]].
