---
type: method
status: scaffold
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/vincoli-di-budget
---

# Metodo - LCS con vincolo di ingombro

## Quando si usa

Quando si cerca una sottosequenza comune massima tra due sequenze, ma la soluzione deve rispettare un vincolo di costo, peso o ingombro.

Parole chiave forti: "ingombro complessivo", "peso totale", "costo complessivo", "somma dei pesi", "budget W", "`<= W`".

La parola "complessivo" e un trigger per una somma/budget, non per un confronto locale tra pesi consecutivi.

## Stato tipico

$$
c_{i,j,k}
$$

dove $i$ e $j$ indicano i prefissi delle due sequenze e $k$ indica il budget massimo disponibile.

Non usare uno stato solo $c_{i,j}$ con vincolo $w(prev)\le w(curr)$, salvo richiesta esplicita di monotonia/crescenza rispetto al peso.

## Esercizi collegati

- [[exam_2025_07_03_p1_e01]]
- [[exam_2025_06_09_p1_e01]]

## Varianti collegate

- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]

## Teoria necessaria

- [[programmazione_dinamica]]
- [[lcs]]
- [[sottosequenze_comuni]]

## Errori comuni

- Dimenticare la dimensione del budget.
- Usare $w(x_i)$ anche quando $x_i \ne y_j$.
- Confondere "ingombro complessivo" con "pesi non decrescenti".
- Ricostruire la sequenza senza controllare se il simbolo e stato effettivamente scelto.

> [!Warning]
> Metodo da completare durante la fase di soluzione.

## Integrazione da SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 11.

### Coefficiente

$$
L_{i,j,c} = \text{lunghezza di una LCS tra } X_i,Y_j \text{ con ingombro complessivo al massimo } c.
$$

### Caso base

$$
L_{i,j,c}=0 \quad \text{se } i=0 \text{ oppure } j=0.
$$

### Passo ricorsivo

$$
L_{i,j,c} =
\begin{cases}
\max(L_{i-1,j,c},L_{i,j-1,c}) & \text{se } x_i \ne y_j,\\
\max(L_{i-1,j,c},L_{i,j-1,c},L_{i-1,j-1,c-w(x_i)}+1) & \text{se } x_i=y_j,\ w(x_i)\le c,\\
\max(L_{i-1,j,c},L_{i,j-1,c}) & \text{se } x_i=y_j,\ w(x_i)>c.
\end{cases}
$$

> [!Info]
> La forma con massimo a tre termini e prudente: anche quando c'e match, l'ottimo puo non usare quel simbolo.

### Esempio collegato

- [[lcs_ingombro_SRC_EXTRA_001]]
