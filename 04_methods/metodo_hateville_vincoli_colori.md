---
type: method
status: draft
source_id: SRC-EXTRA-001
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/hateville
  - topic/colori
---

# Metodo - Hateville con vincoli sui colori

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf, pagina 12.

## Quando si usa

Quando una variante di Hateville aggiunge un vincolo locale sui colori delle case scelte. Nella fonte: non scegliere due case rosse consecutive.

## Sottoproblema certo

$$
OPT_i = \max\{D(A)\mid A\subseteq \{1,\dots,i\},\ A \text{ ammissibile}\}.
$$

dove $D(A)$ e la somma delle donazioni delle case in $A$.

## Casi base

- $OPT_0=0$.
- $OPT_1=d_1$ se scegliere la prima casa e ammesso.
- Per $i=2$ bisogna distinguere il vincolo di adiacenza e il colore delle due case.

## Passo ricorsivo

> [!Warning]
> Il passo ricorsivo di pagina 12 non e sufficientemente leggibile. Non fissare una ricorrenza unica da questa nota.

Una derivazione sicura probabilmente richiede uno stato aggiuntivo che ricordi se l'ultima casa scelta e rossa, oppure una distinzione tra prendere/non prendere la casa $i$.

> [!Todo]
> Verificare in SRC-NOTE-001 o completare con ragionamento separato prima di usarlo in una soluzione d'esame.

