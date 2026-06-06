---
type: pattern
status: scaffold
tags:
  - apa
  - pattern
  - topic/programmazione-dinamica
---

# Pattern - Programmazione Dinamica in Parte I

> [!Info]
> Guida ai pattern e alle strutture standard per gli esercizi di Programmazione Dinamica (DP) nella Parte I degli appelli di APA.

---

## 1. Struttura Generale Richiesta

Tutti gli esercizi di DP in Parte I richiedono un'impostazione formale rigorosa divisa in:

1. **Definizione dei coefficienti**: Spiegare chiaramente cosa rappresenta ogni cella della tabella DP (es. $c_{i,j}$ è la lunghezza del sottoproblema prefisso).
2. **Caso base**: Definire le condizioni iniziali della tabella (es. quando una delle sequenze è vuota, o per $k=0$ intermedi nei grafi).
3. **Passo ricorsivo**: Esprimere i coefficienti del problema corrente in funzione di quelli dei sottoproblemi più piccoli, coprendo tutti i casi.
4. **Soluzione finale**: Indicare l'esatta coordinata o formula che restituisce il valore cercato.
5. **Algoritmo bottom-up**: Scrivere l'algoritmo iterativo per riempire la tabella.
6. **Algoritmo di ricostruzione**: Scrivere la procedura ricorsiva o iterativa all'indietro per stampare la soluzione ottima.

---

## 2. Pattern su Sequenze (LCS con Vincoli)

### Stato esteso
Quando oltre alla sequenza si hanno vincoli di budget o presenza (es. rossi, blu, ingombro), lo stato si estende aggiungendo dimensioni:

$$
C[i,j,v]
$$

dove:
- $i,j$ indicano i prefissi delle sequenze $X_i$ e $Y_j$.
- $v$ è la variabile del vincolo (contatore di rosso/blu, budget residuo, o stato booleano).

### Esempi e Variazioni:
*   **Vincolo di ingombro massimo (Budget)**: $C[i,j,w]$ = lunghezza LCS con ingombro $\le w$. 
    *   *Appello*: [[exam_2025_07_03_p1_e01]]
*   **Vincoli di conteggio massimo**: $C[i,j,r,b]$ = lunghezza LCS con al più $r$ rossi e $b$ blu.
    *   *Appelli*: [[exam_2025_06_09_p1_e01]], [[exam_2025_01_13_p1_e01]]
*   **Vincolo di presenza obbligatoria**: $C[i,j,r]$ con $r \in \{0,1\}$ dove $r=1$ indica presenza obbligatoria di almeno un rosso.
    *   *Appello*: [[exam_2025_11_10_p1_tema_a_e01]]
*   **LCS a tre sequenze con budget massimo**: $C[i,j,k,r]$ = lunghezza LCS a tre sequenze con al più $r$ rossi.
    *   *Appelli*: [[exam_2025_02_11_p1_completo_e01]], [[exam_2025_02_11_p1_recupero_e01]], [[exam_2025_09_17_p1_e01]]
*   **LCS di 3 sequenze senza altri vincoli**: DP tridimensionale `c_{i,j,h}`, casi base su ogni prefisso vuoto, match solo se gli ultimi tre elementi coincidono, valore finale `c_{m,n,l}`.
    *   *Fonte ufficiale*: [[dp_lcs_tre_sequenze]]
*   **LCS con due rossi consecutivi**: stati vincolati a terminare nel match corrente, `c_ij1` per vincolo gia soddisfatto e `c_ij0` per vincolo non ancora soddisfatto; valore finale come massimo globale.
    *   *Fonte ufficiale*: [[dp_lcs_due_rossi_consecutivi]]
*   **LCS con dispari/pari per posizione**: vincolo sulle posizioni della sottosequenza; `x_i mod 2` controlla il valore, `c_hk mod 2` controlla la posizione successiva; valore finale come massimo globale.
    *   *Fonte ufficiale*: [[dp_lcs_dispari_pari_alternati]]
*   **LICS e varianti simili**: sottoproblema vincolato a terminare nel match corrente, `c_ij=0` se `x_i != y_j`, massimo sui predecessori compatibili e valore finale come massimo globale.
    *   *Fonte ufficiale*: [[dp_lics_e_varianti]]
*   **Zaino con al massimo 3 rossi**: stato `d_{i,c,r}` con `r` budget massimo di rossi; se si prende un rosso si decrementa `r`, se si prende un non rosso `r` resta invariato.
    *   *Fonte ufficiale*: [[dp_knapsack_vincoli_colore]]

---

## 3. Pattern su Grafi (DP Booleana / Stato Esteso)

### Chiusura transitiva modificata (Floyd-Warshall esteso)
Per stabilire l'esistenza di cammini con proprietà specifiche, si estende l'algoritmo di Floyd-Warshall definendo:

$$
D[k,i,j,h]
$$

dove:
- $k$ indica che i vertici intermedi utilizzabili sono solo nell'insieme $\{1,\dots,k\}$.
- $i,j$ sono i vertici sorgente e destinazione.
- $h$ è lo stato esteso (es. parità della lunghezza, conteggio archi colorati).

### Esempi e Variazioni:
*   **Vincolo di parità**: $D[k,i,j,p]$ con $p \in \{0,1\}$ indicante se il cammino ha numero pari ($0$) o dispari ($1$) di archi target.
    *   *Appelli*: [[exam_2026_01_12_e02]] (numero pari di archi totali), [[exam_2025_09_17_p1_e02]] (numero dispari di archi blu)
*   **Conteggio esatto di archi colorati**: $D[k,i,j,r,b]$ = esistenza cammino con esattamente $r$ rossi e $b$ blu.
    *   *Appello*: [[exam_2025_07_03_p1_e02]]
*   **Regole locali tra archi consecutivi**: Esistenza cammino senza transizioni vietate (es. $(R,N)$ o $(B,R)$, divieto di consecutivi identici $NN$ e $BB$, o divieto di $(N,R)$ e $(R,B)$). Richiede di salvare il colore del primo e dell'ultimo arco dello stato.
    *   *Appelli*: [[exam_2025_06_09_p1_e02]], [[exam_2025_02_11_p1_completo_e02]], [[exam_2025_01_13_p1_e02]]
*   **Somma aggregata di archi specifici**: $D[k,i,j,h]$ con $h \in \{0,1,2,3\}$ indicante che la somma degli archi A e B è esattamente $h$.
    *   *Appello*: [[exam_2025_11_10_p1_tema_a_e02]]
*   **Cammini minimi pesati con vincolo di parità ed esclusione locale**: $D[k,i,j,p]$ = peso minimo di un cammino con parità $p$ modulo 2 di archi blu, senza due vertici rossi consecutivi.
    *   *Appello*: [[exam_2025_02_11_p1_recupero_e02]]

---

## 4. Integrazione SRC-EXTRA-001

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf.

Pattern operativi aggiunti:

- LCS base: [[metodo_lcs_base]]
- LIS/LDS: [[metodo_lis_lds]]
- LICS: [[metodo_lics]]
- LCS con esattamente $R$ rossi: [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- LCS con quantificatore "tutte le LCS": [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- LCS con ingombro: [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]
- Zaino 0/1 con massimo numero di oggetti rossi: [[metodo_programmazione_dinamica_zaino_01]]
- Hateville con vincoli sui colori: [[metodo_hateville_vincoli_colori]]
- LCS con alternanza pari/dispari: [[metodo_lcs_alternanza_pari_dispari]]

> [!Warning]
> Restano draft Hateville e LCS alternanza pari/dispari da fonte manoscritta. Per la variante ufficiale "dispari in posizioni dispari e pari in posizioni pari" usare [[dp_lcs_dispari_pari_alternati]].

## 5. Integrazione SRC-NOTE-001

Fonte: [[source_inventory]] / SRC-NOTE-001 / `Analisi E Progettazione Di Algoritmi.pdf`.

- Sequenze base: [[dp_lcs_base]], [[dp_interleaving_sequenze]], [[dp_lcs_lunghezza_esatta_booleana]]
- Sequenze con vincoli: [[dp_lcs_vincoli_colore]], [[dp_lcs_vincolo_somma_ingombro]], [[dp_lcs_crescente_lics]]
- Zaino: [[dp_knapsack_colori]]
- Grafi: [[dp_grafi_floyd_warshall_stato_esteso]]
- Mapping appelli: [[mapping_appelli_to_SRC_NOTE_001]]

## 6. Integrazione PDF ufficiali Floyd-Warshall

Fonte: PDF ufficiali `SRC-OFFICIAL-EX-003` ... `SRC-OFFICIAL-EX-011`.

Metodo primario: [[fw_varianti_vincoli_colori]].

Regola fissa:

- `k` indica i vertici intermedi ammessi `{1,...,k}`;
- `E1`: il cammino non usa `k`;
- `E2`: il cammino usa `k` e concatena `i -> k` con `k -> j`;
- cammini minimi: `d`, `min`, `+`, `+infinito`;
- esistenza: `e`, `OR`, `AND`, `FALSE`.

Scelta dello stato extra:

- alternanza archi: `f,l`;
- alternanza vertici: nessuno stato `f,l`;
- conteggio esatto: `r`;
- parita: `p`;
- presenza: flag booleani.
