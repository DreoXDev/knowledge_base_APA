---
type: pattern
topic: programmazione-dinamica
status: scaffold
tags:
  - apa
  - pattern
  - topic/programmazione-dinamica
  - topic/lcs
---

# Pattern - DP su sequenze con budget

## Descrizione

Variante di un problema classico su sequenze in cui allo stato viene aggiunto un vincolo di budget, peso o ingombro.

## Appelli in cui compare

| Appello | Esercizio | Variante |
|---|---|---|
| [[exam_2025_07_03_part1]] | [[exam_2025_07_03_p1_e01]] | LCS con vincolo di ingombro |

## Metodo principale

- [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]

## Riconoscimento rapido vincoli LCS

| Parole nella traccia | Significato | Stato consigliato |
|---|---|---|
| presenza del rosso | almeno un simbolo rosso | `C[i,j,r]` con `r in {0,1}` |
| esattamente k rossi | conteggio esatto | `C[i,j,k]` |
| al piu k rossi | budget/count massimo | `C[i,j,k]` oppure stato di capacita |
| ingombro complessivo <= W | somma dei pesi <= W | `C[i,j,p]` |
| peso totale <= W | somma dei pesi <= W | `C[i,j,p]` |
| peso non decrescente | monotonia locale/globale | DP tipo LICS |
| crescente rispetto a w | ordine sui pesi | DP con ultimo elemento/terminazione |

> [!Warning]
> La parola "complessivo" e un trigger forte per una somma/budget, non per un confronto locale.

> [!Warning]
> Pattern scaffold: completare dopo la soluzione dell'esercizio.
