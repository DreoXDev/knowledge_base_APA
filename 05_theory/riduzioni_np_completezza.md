---
type: theory
topic: riduzioni_np_completezza
status: complete
tags:
  - apa
  - teoria
  - topic/np-completezza
  - topic/riduzioni
---

# Teoria — Riduzioni Polinomiali e NP-completezza

Le **riduzioni polinomiali** sono lo strumento matematico fondamentale per stabilire la difficoltà relativa tra problemi e per dimostrare l'NP-completezza.

---

## Definizione di Riduzione Polinomiale (Riduzione di Karp)

Siano $A$ e $B$ due problemi di decisione. Una **riduzione polinomiale** da $A$ a $B$ è una funzione:
$$f : \Sigma^* \to \Sigma^*$$
tale che:
1. Per ogni istanza $x$ del problema $A$, si ha che:
   $$x \in A \iff f(x) \in B$$
   *(Ovvero: la risposta per $x$ su $A$ è YES se e solo se la risposta per $f(x)$ su $B$ è YES).*
2. La funzione $f$ è calcolabile in tempo polinomiale rispetto alla dimensione dell'input ($|x|$).

Si scrive:
$$A \le_p B$$

### Interpretazione
La relazione $A \le_p B$ significa che il problema $A$ **non è più difficile** del problema $B$ (a meno di un fattore polinomiale). Infatti, se disponessimo di un algoritmo polinomiale per risolvere $B$, potremmo risolvere anche $A$ in tempo polinomiale:
1. Prendendo l'input $x$ per $A$ e calcolando $f(x)$ in tempo polinomiale.
2. Risolvendo $f(x)$ usando l'algoritmo per $B$.

---

## Come Usare le Riduzioni per Provare l'NP-completezza

Per definizione, un problema $B$ è **NP-completo** se $B \in NP$ e per ogni $C \in NP$ si ha $C \le_p B$.
Operativamente, per dimostrare che un nuovo problema $B$ è NP-completo, non riduciamo tutti gli infiniti problemi in NP. Sfruttiamo invece la transitività delle riduzioni tramite questo schema fisso:

1. **Appartenenza a NP**: Dimostrare che $B \in NP$ (fornendo certificato e verificatore polinomiale).
2. **Scelta del problema noto**: Scegliere un problema $A$ che sia **già noto** per essere NP-completo (es. SAT, 3SAT, CLIQUE, VERTEX-COVER).
3. **Costruzione della riduzione**: Definire una trasformazione polinomiale $f$ che mappa istanze di $A$ in istanze di $B$ ($A \le_p B$).
4. **Dimostrazione di correttezza**: Dimostrare la doppia implicazione:
   - **Direzione diretta ($\implies$)**: Se $x \in A \implies f(x) \in B$.
   - **Direzione inversa ($\impliedby$)**: Se $f(x) \in B \implies x \in A$.
5. **Complessità della riduzione**: Verificare che il tempo per calcolare $f(x)$ sia polinomiale in $|x|$.

---

## Warning d'Esame Critico

> [!CAUTION]
> **Attenzione alla Direzione della Riduzione!**
> Questo è l'errore più comune e più grave commesso durante l'esame.
> * Per dimostrare che **$B$ è NP-hard**, la riduzione deve andare **dal problema noto $A$ al problema incognito $B$**:
>   $$A \le_p B$$
> * Ridurre al contrario ($B \le_p A$) dimostra soltanto che $B$ non è più difficile di $A$ (il che è ovvio, visto che $A \in NPC$), ma **non** dimostra che $B$ è NP-hard.

---

## Collegamenti

- Teoria P, NP e Cook: [[p_np_np_completezza]]
- Metodo operativo dimostrazione: [[np_completezza_schema_dimostrazione]]
- Schema Clique, VC, IS: [[riduzioni_vertex_cover_clique_independent_set]]
- Esempio riduzione 3SAT -> Clique: [[riduzione_3sat_clique_schema]]
