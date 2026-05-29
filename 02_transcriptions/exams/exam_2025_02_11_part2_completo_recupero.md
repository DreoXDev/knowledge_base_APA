---
type: exam_transcription
course: Analisi e Progettazione di Algoritmi
part: II
date: 2025-02-11
variant: completo_recupero
source_pdf: parteII-11feb25-completo-recupero.pdf
status: transcribed
---

# Appello APA — Parte II (scritto completo e recupero) — 11 febbraio 2025

Fonte: `parteII-11feb25-completo-recupero.pdf`

---

## Esercizio 1 (valore: 6 punti)

Si consideri un grafo non orientato, connesso e pesato $G = (V,E)$ con archi:
* $(b,c)$ di peso 4,
* $(b,d)$ di peso 1,
* $(a,c)$ di peso 6,
* $(a,b)$ di peso 7,
* $(c,d)$ di peso 2,
* $(d,e)$ di peso 5,
* $(c,e)$ di peso 3.

Mostrare nello schema sotto riportato l’ordine con cui l’algoritmo di **Kruskal** aggiunge (uno dopo l’altro) gli archi del *Minimum Spanning Tree*.

Avete a disposizione un numero di quadrati pari al numero di archi di $G$ (cioè 7 quadrati: Q1, Q2, Q3, Q4, Q5, Q6, Q7), contenente ciascuno i vertici di $G$. 

**DOVETE** riportare:
* nel quadrato **Q1** il primo arco aggiunto,
* nel quadrato **Q2** i primi due archi aggiunti,
* nel quadrato **Q3** i primi tre archi aggiunti,
* ...
* nel quadrato **Qi** i primi $i$ archi aggiunti,
* ...
* fino a mostrare l’intero MST costruito.

*Nota Bene: Non verranno considerate risposte che non seguono questo schema.*

---

## Esercizio 2 (valore: 6 punti)

Dato il grafo $G$ sotto riportato, disegnare il grafo $G'$ che si ottiene nella riduzione da **CLIQUE** a **VERTEX COVER**, indicando quanti e quali sono i vertici della copertura di vertici di G'.

La copertura di vertici di $G'$ è composta dai seguenti vertici: .............................................................. in numero pari a ......

---

## Esercizio 3 (valore: 7 punti)

Siano dati $C \in \mathbb{N}$ ($C > 0$) e un insieme $X = \{1, \dots, n\}$ di oggetti tali che ad ogni oggetto $i$ è associato un valore $v_i \in \mathbb{N}$ ed un ingombro $w_i \in \mathbb{N}$, $v_i > 0$ e $w_i > 0$.

Mediante programmazione dinamica, si vuole determinare il valore complessivo di un sottoinsieme $S$ di $X$ di valore complessivo massimo e di ingombro complessivo al più $C$ (**Knapsack 0/1**).

Scrivere le equazioni di ricorrenza per trovare tale valore ottimo, indicando in esse con $OPT(i,c)$ il coefficiente relativo al generico sottoproblema $(i,c)$.

---

## Esercizio 4 (valore: 7 punti)

Data una generica formula 3-SAT (o 3-CNF-SAT) $f = C_1 \land \dots \land C_k$ dove per ogni $r \in \{1,\dots,k\}$, la $r$-esima clausola è $C_r = l^r_1 \lor l^r_2 \lor l^r_3$, definire il grafo $G$ utilizzato nella riduzione da **3-SAT** a **CLIQUE** oppure da **3-SAT** a **INDEPENDENT SET** (a scelta dello studente).

---

## Esercizio 5 (valore: 7 punti)

Enunciare e dimostrare il **teorema dell'arco sicuro** (SUL FOGLIO PROTOCOLLO).

---

## Domanda Facoltativa Premiale (valore: 3 punti bonus, una a scelta)

*Nota Bene: La domanda è riservata a chi risponde ad ognuna delle domande precedenti, conseguendo per ciascuna un punteggio non nullo e conseguendo il superamento dell'intera Parte II. In presenza di risposte a più domande, verrà presa in considerazione solo la prima presente sul foglio protocollo. Il bonus ottenuto verrà sommato al voto finale, dato dalla media dei voti della Parte I e della Parte II.*

Scegliere **UNA** tra le seguenti domande da svolgere:

1. **(3 punti)** Dimostrare che se un sistema di indipendenza $(E,F)$ è un matroide allora per ogni funzione peso $w: E \to \mathbb{R}^+ \cup \{0\}$ (oppure $w: E \to \mathbb{R}$), l’algoritmo **Greedy** (si intende Greedy-max) restituisce una soluzione ottima (ossia risolve il problema di massimo associato a $(E,F)$ e $w$).
2. **(3 punti)** Dimostrare che **CLIQUE** si riduce a **VERTEX-COVER** ($CLIQUE \le_p VERTEX-COVER$).
3. **(3 punti)** Dimostrare la correttezza dell'algoritmo di **Dijkstra** *(Nota Bene: non occorre dimostrare le proprietà del limite superiore, della convergenza, e la disuguaglianza triangolare).*
