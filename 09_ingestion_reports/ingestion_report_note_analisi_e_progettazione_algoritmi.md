# Ingestion Report - SRC-NOTE-001 - Analisi E Progettazione Di Algoritmi

## Fonte

- Source ID: `SRC-NOTE-001`
- File: `01_sources/notes_raw/Analisi E Progettazione Di Algoritmi.pdf`
- Tipo: appunti manoscritti metodologici
- Pagine: 65
- Stato: applicato con warning di lettura
- Ruolo nella KB: fonte privilegiata per sintassi d'esame, metodi DP, ricorrenze, pseudocodice, teoria grafi e NP-completezza.

## Sintesi

> [!Summary]
> Il PDF contiene appunti lunghi e non lineari. Le pagine iniziali consolidano LCS, interleaving e varianti DP su sequenze; la parte centrale contiene LCS con vincoli di risorsa/colore, LICS e zaino; la parte finale contiene DP su grafi stile Floyd-Warshall, Dijkstra/Floyd-Warshall, controlli BFS e schemi di NP-completezza.

## Mappa delle pagine

| Pagina | Tipo contenuto | Tema | Azione KB |
|---|---|---|---|
| 1 | teoria/metodo | LCS: input, output, sequenza, prefisso, sottosequenza | integrare in [[dp_lcs_base]] |
| 2 | teoria/metodo | sottostruttura ottima LCS, casi sugli ultimi simboli | integrare in [[dp_lcs_base]] |
| 3 | metodo | ricorrenza LCS e scelta del massimo | integrare in [[dp_lcs_base]] |
| 4 | metodo | Interleaving: istanza $X,Y,W$ e sottosequenze disgiunte | creare [[dp_interleaving_sequenze]] |
| 5 | metodo | Interleaving: $S[i,j]$, casi base, passo ricorsivo | creare esempio [[interleaving_SRC_NOTE_001]] |
| 6 | metodo | LCS di lunghezza richiesta $L$ | creare [[dp_lcs_lunghezza_esatta_booleana]] |
| 7 | metodo | LCS con somma/ingombro $\le K$ | creare [[dp_lcs_vincolo_somma_ingombro]] |
| 8 | metodo | LICS: problema ausiliario che termina in match | creare [[dp_lcs_crescente_lics]] |
| 9 | esercizio | Knapsack con colore e vincolo sui rossi | creare [[dp_knapsack_colori]] |
| 10 | metodo | Knapsack: $OPT[i,c,r]$ e casi di presa/non presa | esempio [[knapsack_colori_SRC_NOTE_001]] |
| 11 | metodo | LCS con rossi/blu/neutri e stato esteso | aggiornare [[dp_lcs_vincoli_colore]] |
| 12 | metodo | LCS con conteggi e ricostruzione della sequenza | aggiornare metodi colore |
| 13 | metodo | LCS con valore massimo e vincoli locali sui rossi | collegare a LICS/colore |
| 14 | metodo | LICS con alternanza/intervalli di valori | collegare a [[dp_lcs_crescente_lics]] |
| 15 | esercizio | LICS decrescente con vincoli colore/parita | warning, collegare a LICS |
| 16 | esercizio | LCS/LICS con stampa top-down | collegare a ricostruzione DP |
| 17 | metodo | LCS con al massimo $K$ rossi | aggiornare [[dp_lcs_vincoli_colore]] |
| 18 | metodo | LCS con esattamente $K$ rossi | aggiornare [[dp_lcs_vincoli_colore]] |
| 19 | metodo | LCS con parita dei rossi | aggiornare [[dp_lcs_vincoli_colore]] |
| 20 | metodo | Print/ricostruzione LCS con vincoli | collegare a [[metodo_ricostruzione_soluzione_dp]] |
| 21 | metodo | Varianti LCS con budget colore multiplo | collegare appelli Parte I |
| 22 | metodo | Pattern "aggiungo dimensione di stato" | aggiornare pattern DP |
| 23 | esercizio | Cammini/grafi con colori | creare [[dp_grafi_floyd_warshall_stato_esteso]] |
| 24 | metodo | Floyd-Warshall con vertici intermedi | creare metodo grafi |
| 25 | metodo | Caso base $k=0$ nei cammini | creare esempio grafi |
| 26 | metodo | Passo: passa/non passa dal vertice $k$ | creare esempio grafi |
| 27 | metodo | Stato esteso per colori archi | collegare appelli grafi colorati |
| 28 | metodo | Cammini senza consecutivi vietati | collegare Parte I grafi |
| 29 | metodo | Cammini con coppie consecutive uguali | creare esempio coppie colori |
| 30 | metodo | Variabili $D^k(i,j,\dots)$ | aggiornare metodo grafi |
| 31 | esercizio | Applicazione Floyd-Warshall esteso | collegare esempi |
| 32 | esercizio | Ricorrenza booleana su grafi | collegare pattern |
| 33 | teoria | Dijkstra: idea e correttezza | aggiornare teoria Dijkstra |
| 34 | teoria | Dijkstra vs Floyd-Warshall | aggiornare flashcard |
| 35 | teoria | Cammini minimi e complessita | aggiornare teoria grafi |
| 36 | teoria/metodo | BFS per verificare se un grafo e albero | creare [[bfs_tree_check]] |
| 37 | teoria | Alberi, visita, connettivita/cicli | creare review grafi |
| 38 | teoria | Floyd-Warshall classico | aggiornare [[floyd_warshall]] |
| 39 | teoria | Chiusura transitiva/ricorrenze su grafi | collegare pattern |
| 40 | teoria | NP, certificati, verificatore | aggiornare [[np_completezza]] |
| 41 | teoria | Schema NP-completezza | creare [[np_completezza_schema_dimostrazione]] |
| 42 | teoria | Riduzione polinomiale | aggiornare metodo NP |
| 43 | teoria | SAT, Cook, problemi noti | aggiornare teoria |
| 44 | teoria/esempio | 3-CNF-SAT | collegare riduzioni |
| 45 | teoria/esempio | CLIQUE | collegare esercizi |
| 46 | teoria/esempio | VERTEX-COVER | collegare esercizi |
| 47 | metodo | Riduzione CLIQUE/VC | collegare metodi esistenti |
| 48 | metodo | Dimostrazione se e solo se | aggiornare schema NP |
| 49 | teoria | Errori comuni NP-completezza | aggiornare checklist |
| 50 | teoria | Riepilogo riduzioni grafiche | aggiornare flashcard |
| 51 | esercizio | Appello fotografato con svolgimento DP | collegare mapping |
| 52 | esercizio | Appello fotografato con svolgimento grafi | collegare mapping |
| 53 | esercizio | Appello fotografato con riduzioni | collegare mapping |
| 54 | metodo | Ricostruzione soluzione DP | collegare metodi |
| 55 | metodo | Pseudocodice bottom-up | collegare checklist |
| 56 | teoria | Complessita temporale/spaziale | aggiornare review |
| 57 | teoria | Domande orali su grafi | aggiornare flashcard |
| 58 | teoria | Domande orali su NP | aggiornare flashcard |
| 59 | sintesi | Pattern DP sequenze | creare indice SRC-NOTE |
| 60 | sintesi | Pattern DP grafi | creare indice SRC-NOTE |
| 61 | sintesi | Pattern NP/grafi | creare indice SRC-NOTE |
| 62 | appunti | Note miste/facoltativo | trascrizione con warning |
| 63 | appunti | Note miste/facoltativo | trascrizione con warning |
| 64 | appunti | Ripasso finale | aggiornare review |
| 65 | appunti | Pagina finale / note sparse | trascrizione con warning |

## Pattern metodologici estratti

- DP su sequenze con prefissi: LCS, interleaving, LCS lunghezza esatta.
- DP su sequenze con risorsa residua: somma/ingombro, conteggi colore.
- DP con soluzione che termina in un match: LICS e varianti crescenti/decrescenti.
- DP su zaino con stato aggiuntivo di colore.
- DP su grafi con vertici intermedi e stato esteso.
- Schema standard per NP-completezza.

## Esercizi svolti / semi-svolti estratti

- LCS base.
- Interleaving.
- LCS al massimo/esattamente $K$ rossi.
- LCS somma $\le K$.
- LICS.
- Knapsack con rossi.
- Cammini colorati Floyd-Warshall.
- Schema NP-completezza.

## Teoria estratta

- Dijkstra, Floyd-Warshall, BFS tree check.
- NP, NP-completezza, SAT/3-SAT, CLIQUE, VERTEX-COVER.

## Ricorrenze e pseudocodice normalizzati

Le ricorrenze normalizzate sono state inserite nei metodi operativi collegati, mantenendo warning nei punti in cui la lettura OCR/manoscritta non e certa.

## Collegamenti da creare nella KB

- [[_index_methods_from_SRC_NOTE_001]]
- [[mapping_appelli_to_SRC_NOTE_001]]
- review e flashcard dedicate a SRC-NOTE-001.

## Dubbi di lettura / parti ambigue

> [!Warning]
> Le pagine con esercizi fotografati e annotazioni sovrapposte sono meno leggibili. Le formule che coinvolgono vincoli multipli colore/parita e alcune ricostruzioni top-down richiedono verifica manuale.

## Azioni Codex

- Creare trascrizione interpretativa completa.
- Creare/aggiornare metodi operativi.
- Creare esempi svolti prioritari.
- Aggiornare teoria, review, mapping, inventario fonti, TODO e stato progetto.
