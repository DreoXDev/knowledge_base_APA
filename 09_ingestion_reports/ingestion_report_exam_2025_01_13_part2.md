# Ingestion Report — Appello 13 Gennaio 2025 (Parte II)

## Metadata della Fonte
- **Source ID**: `SRC-EXAM-002`
- **File**: `parteII-13gen25.pdf`
- **Data**: `2025-01-13`
- **Parte**: `Parte II`
- **Corso**: `Analisi e Progetto di Algoritmi`
- **Stato**: `applicato`
- **Catalogatore**: `Antigravity`
- **Data Ingestione**: `2026-05-17`

---

## Analisi del Contenuto

L'appello si compone di 5 esercizi principali a risposta aperta o simulazione su foglio, più una sezione contenente 4 domande bonus teoriche a scelta (sezione premiale).

### Esercizi Principali:
1. **Esercizio 1 (val 6)**: Esecuzione manuale di **Dijkstra** con tracciamento passo-passo dei valori dell'attributo $d$ in corrispondenza delle estrazioni dei nodi e identificazione degli archi effettivamente rilassati.
2. **Esercizio 2 (val 6)**: Disegno del grafo ottenuto dalla riduzione polinomiale di Karp da **3-SAT** a **CLIQUE** applicata alla formula $\varphi = (\neg x_1 \lor \neg x_2 \lor x_3) \land (x_1 \lor x_2 \lor x_3) \land (\neg x_1 \lor x_2 \lor \neg x_3)$, con disposizione geometrica specifica delle clausole (sinistra, alto, destra).
3. **Esercizio 3 (val 7)**: Formulazione delle equazioni di ricorrenza (casi base e passo ricorsivo) per il calcolo della **chiusura transitiva/riflessiva-transitiva** di un grafo, usando i coefficienti $e_{ij}^{k}$.
4. **Esercizio 4 (val 7)**: Risposta teorica sintetica sul criterio formale per dimostrare che un problema $A$ è **NP-completo** (appartenenza a NP e riduzione polinomiale $B \le_p A$ da un problema noto).
5. **Esercizio 5 (val 7)**: Definizione e dimostrazione formale dei tre assiomi del **matroide grafico** su un grafo non orientato.

### Domande Bonus Premiali (val 3 punti):
1. **Opzione 1**: Enunciato e dimostrazione della proprietà della sottostruttura ottima della **LCS**.
2. **Opzione 2**: Prova formale che se un sistema di indipendenza è un matroide, l'algoritmo **Greedy-max** restituisce una soluzione ottima (Teorema di Rado-Edmonds).
3. **Opzione 3**: Dimostrazione della riduzione polinomiale **3-SAT $\le_p$ Independent Set**.
4. **Opzione 4**: Dimostrazione della riduzione polinomiale **CLIQUE $\le_p$ Vertex Cover**.

---

## Mappatura File Creati/Aggiornati

### Trascrizioni ed Ingestione:
- **Trascrizione**: `02_transcriptions/exams/exam_2025_01_13_part2.md` [NEW]
- **Esercizi Catalogati**:
  - `03_exercise_catalog/exercises/exam_2025_01_13_p2_e01.md` [NEW]
  - `03_exercise_catalog/exercises/exam_2025_01_13_p2_e02.md` [NEW]
  - `03_exercise_catalog/exercises/exam_2025_01_13_p2_e03.md` [NEW]
  - `03_exercise_catalog/exercises/exam_2025_01_13_p2_e04.md` [NEW]
  - `03_exercise_catalog/exercises/exam_2025_01_13_p2_e05.md` [NEW]
  - `03_exercise_catalog/exercises/exam_2025_01_13_p2_bonus.md` [NEW]

### Collegamento a Metodi e Teoria Centrali:
- **Dijkstra step-by-step**: Collegato a `04_methods/metodo_dijkstra.md` e `05_theory/dijkstra_correttezza.md`
- **Riduzione 3-SAT to CLIQUE**: Collegato a `04_methods/metodo_riduzione_3sat_clique.md`
- **Chiusura Transitiva (Warshall)**: Collegato a `04_methods/metodo_equazioni_ricorrenza_chiusura_transitiva.md`
- **Dimostrazione NP-completezza**: Collegato a `04_methods/metodo_dimostrare_np_completezza.md`
- **Dimostrazione Matroide Grafico**: Collegato a `04_methods/metodo_dimostrazione_matroide_grafico.md`
- **Bonus LCS**: Collegato a `04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md`
- **Bonus Greedy Matroidi**: Collegato a `04_methods/metodo_greedy_matroidi_rado.md`
- **Bonus 3-SAT to IS**: Collegato a `04_methods/metodo_riduzione_3sat_independent_set.md`
- **Bonus CLIQUE to VC**: Collegato a `04_methods/metodo_riduzione_clique_vertex_cover.md`
