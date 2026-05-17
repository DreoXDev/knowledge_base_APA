---
type: method
topic: Requirements to prove NP-completeness
status: draft
tags:
  - apa
  - metodo
  - topic/np_completezza
  - topic/teoria
---

# Metodo - Come dimostrare la NP-completezza di un problema A

## Quando si usa

Questo metodo si applica quando un quesito d'esame teorico richiede di descrivere cosa sia necessario mostrare formalmente per stabilire che un problema specifico $A$ è **NP-completo**.

---

## 1. Definizione Formale di NP-completezza

Un problema decisionale $A$ è **NP-completo** se e solo se soddisfa contemporaneamente due proprietà fondamentali:
1. $A$ appartiene alla classe **NP** ($A \in NP$).
2. $A$ è **NP-difficile** (NP-hard), ovvero per ogni problema $B \in NP$ si ha che $B \le_p A$ (riduzione polinomiale).

---

## 2. Requisiti Operativi per la Dimostrazione

Per dimostrare che un problema specifico $A$ è NP-completo, è sufficiente e necessario mostrare i seguenti due passi:

### Passo 1: Dimostrare l'appartenenza ad NP ($A \in NP$)
- **Cosa fare**: Mostrare che il problema $A$ può essere verificato in tempo polinomiale.
- **Dettagli**: Dato un input (istanza) del problema $x$ e una soluzione proposta (certificato/testimone) $c$, si deve definire un algoritmo di verifica $V(x,c)$ tale che:
  - $V(x,c)$ restituisce `true` se $c$ è una prova valida che $x$ è un'istanza positiva per il problema.
  - Il tempo di esecuzione di $V(x,c)$ è polinomiale rispetto alla dimensione dell'istanza $|x|$.

### Passo 2: Dimostrare la NP-durezza ($A$ è NP-hard)
- **Cosa fare**: Mostrare che il problema è almeno altrettanto difficile di un qualsiasi problema in NP.
- **Dettagli**:
  1. Selezionare un problema $B$ che sia **già noto** per essere NP-completo (es. SAT, 3-SAT, CLIQUE, VERTEX-COVER, INDEPENDENT-SET).
  2. Costruire una **riduzione polinomiale** da $B$ ad $A$ ($B \le_p A$). Questo richiede di definire una funzione $f$ computabile in tempo polinomiale che trasforma istanze di $B$ in istanze di $A$ tale che:
     $$\forall x, \quad x \in B \iff f(x) \in A$$
  3. Dimostrare la correttezza della riduzione nelle due direzioni:
     - **Direzione diretta ($\implies$)**: Se $x$ è un'istanza positiva di $B$, allora $f(x)$ è un'istanza positiva di $A$.
     - **Direzione inversa ($\impliedby$)**: Se $f(x)$ è un'istanza positiva di $A$, allora $x$ è un'istanza positiva di $B$.
  4. Mostrare che la costruzione di $f(x)$ richiede tempo polinomiale rispetto a $|x|$.

---

## Esercizi collegati

- [[exam_2025_06_09_p2_e04]]
- [[exam_2025_07_03_p2_e04]]
- [[exam_2026_01_12_e06]]
- [[exam_2025_11_10_p2_e04]]

## Errori comuni

> [!Warning]
> **Inversione della riduzione**: Sbagliare la direzione della riduzione polinomiale. Per dimostrare che $A$ è NP-hard, bisogna ridurre un problema noto $B$ al problema incognito $A$ ($B \le_p A$), e **NON** viceversa. Ridurre $A \le_p B$ non dimostra nulla sulla durezza di $A$.
> Dimenticare il Passo 1 ($A \in NP$). Mostrare solo la NP-durezza classifica il problema come NP-difficile, ma non come NP-completo.
