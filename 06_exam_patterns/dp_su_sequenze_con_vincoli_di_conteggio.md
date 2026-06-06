---
type: pattern
topic: programmazione-dinamica
status: scaffold
tags:
  - apa
  - pattern
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/vincoli-di-conteggio
---

# Pattern - DP su sequenze con vincoli di conteggio

## Descrizione

Variante di DP su sequenze in cui lo stato tiene traccia di quanti simboli di certe classi possono ancora essere usati.

## Appelli in cui compare

| Appello | Esercizio | Variante |
|---|---|---|
| [[exam_2025_06_09_part1]] | [[exam_2025_06_09_p1_e01]] | LCS con al massimo 2 simboli rossi e 3 simboli blu |

## Metodo principale

- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]

## Pattern ufficiale: LCS con al massimo k elementi di un colore

Trigger:

- "LCS(X,Y,3)";
- "al massimo 3 elementi rossi";
- funzione `col` sui simboli;
- sequenze `X`, `Y` e colore dei simboli.

Metodo:

- DP tridimensionale `C[i][j][r]`;
- `r` = numero massimo ammesso di rossi;
- risposta `C[m][n][k]`.

Fonte ufficiale: `SRC-LECTURE-001`.

## Varianti collegate

- [[dp_su_sequenze_con_budget]]

> [!Warning]
> Per tracce "al massimo" usare la formulazione ufficiale con stato cumulativo. Per tracce "esattamente" usare invece caso base con stati impossibili.
