---
type: solved-example
topic: knapsack-al-massimo-3-rossi
status: official_confirmed
source_id: SRC-OFFICIAL-EX-012
source_file: 01_sources/extra_materials/knapsack-atmost-3-red.pdf
tags:
  - apa
  - esempio-svolto
  - topic/zaino-01
  - topic/colori
---

# Schema soluzione - Zaino con al massimo 3 oggetti rossi

## Riconoscimento

Traccia tipica: "Dato uno zaino 0/1 con oggetti colorati, scegliere un sottoinsieme di valore massimo con al massimo 3 oggetti rossi."

## Schema da esame

1. Definire `S_{i,c,r}` sui primi `i` oggetti, capacita `c`, al massimo `r` rossi.
2. Definire `d_{i,c,r}` come valore di `S_{i,c,r}`.
3. Casi base: `d_{0,c,r}=0` e `d_{i,0,r}=0`.
4. Se `w_i > c`, non posso prendere l'oggetto.
5. Se `i` non e rosso, includerlo non cambia `r`.
6. Se `i` e rosso, includerlo consuma una unita di `r`.
7. Valore ottimo: `d_{n,C,3}`.

## Warning

Per "al massimo 3 rossi" non prendere `max_{r<=3}` se lo stato significa gia "al massimo r": il coefficiente finale e `d_{n,C,3}`.

Metodo: [[dp_knapsack_vincoli_colore]].
