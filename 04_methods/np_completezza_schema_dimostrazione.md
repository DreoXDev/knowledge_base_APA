---
type: method
topic: np_completezza_schema_dimostrazione
status: complete
source_id: SRC-NOTE-001
tags:
  - apa
  - metodo
  - topic/np-completezza
  - topic/riduzioni
---

# Metodo — Dimostrare che un Problema è NP-completo

Questo metodo definisce la struttura formale passo-passo necessaria per dimostrare che un nuovo problema decisionale $\Pi$ è **NP-completo**.

---

## I Due Requisiti Fondamentali

Un problema $\Pi$ è NP-completo se e solo se soddisfa contemporaneamente:
1. **$\Pi \in NP$**: Il problema appartiene alla classe NP (verificabile in tempo polinomiale).
2. **$\Pi$ è NP-hard**: Il problema è difficile almeno quanto qualsiasi problema in NP.

---

## Schema Formale di Dimostrazione (I 5 Pilastri)

Seguire rigorosamente questa struttura durante l'esame:

### Passo 1: Dimostrare l'appartenenza a NP ($\Pi \in NP$)
Fornire una prova costruttiva che una soluzione proposta può essere verificata in tempo polinomiale.
1. **Definire il Certificato ($y$)**: Descrivere quale informazione aggiuntiva (es. la sequenza di vertici in un ciclo, l'insieme di vertici in una clique) funge da prova della risposta positiva. Specificare che la dimensione del certificato $|y|$ è polinomiale rispetto alla dimensione dell'input $|x|$.
2. **Definire il Verificatore ($V$)**: Scrivere lo pseudocodice o i passaggi operativi deterministici per verificare il certificato.
3. **Dimostrare la Complessità del Verificatore**: Mostrare che tutti i controlli del verificatore richiedono un tempo polinomiale rispetto a $|x|$.

### Passo 2: Scegliere un Problema Noto NP-completo ($\Pi'$)
Selezionare dalla teoria del corso un problema già dimostrato essere NP-completo. Esempi ricorrenti:
* `SAT` o `3SAT`
* `CLIQUE`
* `VERTEX-COVER` (VC)
* `INDEPENDENT-SET` (IS)

### Passo 3: Costruire la Riduzione Polinomiale ($\Pi' \le_p \Pi$)
Definire una funzione di trasformazione $f$ che converte ogni istanza del problema noto in un'istanza del problema target.
* **Input della trasformazione**: Un'istanza generica $I_{\Pi'}$ di $\Pi'$.
* **Output della trasformazione**: Un'istanza specifica $I_{\Pi} = f(I_{\Pi'})$ di $\Pi$.
* **Complessità**: Spiegare perché la costruzione di $I_{\Pi}$ richiede tempo polinomiale rispetto alla dimensione di $I_{\Pi'}$.

### Passo 4: Dimostrare la Correttezza della Riduzione (Se e Solo Se)
Dimostrare che la trasformazione preserva la risposta del problema decisionale. È **obbligatorio** dimostrare entrambi i versi dell'implicazione:
* **Direzione Diretta ($\implies$)**: Se l'istanza $I_{\Pi'}$ è positiva per $\Pi'$ (risposta YES), allora l'istanza costruita $f(I_{\Pi'})$ è positiva per $\Pi$ (risposta YES).
* **Direzione Inversa ($\impliedby$)**: Se l'istanza costruita $f(I_{\Pi'})$ è positiva per $\Pi$ (risposta YES), allora l'istanza $I_{\Pi'}$ era positiva per $\Pi'$ (risposta YES).

### Passo 5: Conclusione
Concludere con la formula di chiusura formale:
> *"Poiché il problema $\Pi$ appartiene alla classe NP, e il problema NP-completo $\Pi'$ è riducibile polinomialmente a $\Pi$ ($\Pi' \le_p \Pi$), allora $\Pi$ è NP-completo."*

---

## Errori Comuni da Evitare (Warning d'Esame)

> [!CAUTION]
> * **Inversione della direzione**: Rilanciare la riduzione come $\Pi \le_p \Pi'$. Questo dimostra che $\Pi$ non è più difficile di $\Pi'$ (il che è ovvio, ma inutile per mostrare la durezza di $\Pi$). La direzione corretta deve essere sempre:
>   $$\text{PROBLEMA NOTO } (\Pi') \le_p \text{ NUOVO PROBLEMA } (\Pi)$$
> * **Saltare il Passo 1**: Mostrare solo la durezza qualifica il problema come *NP-hard*, ma non come *NP-completo*.
> * **Dimostrare un solo verso**: Limitarsi a mostrare che una soluzione di $\Pi'$ produce una soluzione di $\Pi$ senza dimostrare che ogni soluzione di $\Pi$ deriva necessariamente da una soluzione valida di $\Pi'$.

---

## Collegamenti

- Teoria complessità e Cook: [[p_np_np_completezza]]
- Teoria riduzioni: [[riduzioni_np_completezza]]
- Esempio schema di dimostrazione: [[np_completezza_schema]]
- Esempio riduzione 3SAT -> Clique: [[riduzione_3sat_clique_schema]]
- Relazioni VC / Clique / IS: [[riduzioni_vertex_cover_clique_independent_set]]
