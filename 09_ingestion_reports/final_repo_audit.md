# Final repo audit - APA KB/RAG

## Stato generale

- [x] README aggiornato
- [x] Methods verificati
- [x] Theory verificata
- [x] Solved examples verificati
- [x] RAG retrieval index coerente
- [x] RAG pattern map coerente
- [x] Method cards coerenti
- [x] Prompt finale aggiornato
- [x] Nessun link rotto evidente
- [x] Warning residui dichiarati

## Problemi trovati

- `RAG_RETRIEVAL_INDEX.md` era corretto nei contenuti principali, ma troppo denso: alcune entry puntavano a troppi file e aumentavano il rumore del retrieval.
- `RAG_PATTERN_MAP.md` mescolava una tabella sintetica con sezioni descrittive; e stato normalizzato nel formato Trigger/Metodo/File/Errori.
- `README.md` e `PROJECT_STATUS.md` descrivevano bene lo stato storico, ma non erano abbastanza diretti per un nuovo modello o studente.
- `AI Chat during Exam/Final Prompt.md` era troppo lungo e legato a dettagli specifici; e stato reso piu generale e operativo.
- Il check automatico ha trovato 0 wikilink rotti e 8 duplicati di nome controllati. I duplicati sono accettabili perche distinguono layer diversi: metodo, teoria e card RAG.
- La scansione temporanei ha trovato `01_sources/notes_raw/kruskal+matrodi-copia.pdf`; non e stato eliminato perche l'hash SHA256 e diverso da `01_sources/notes_raw/kruskal+matrodi.pdf`.

## Modifiche applicate

- Rigenerato `10_rag/RAG_RETRIEVAL_INDEX.md` in Markdown pulito con entry mirate e massimo 2-4 file principali per query.
- Rigenerato `10_rag/RAG_PATTERN_MAP.md` con pattern obbligatori: LCS standard, LCS con stato extra, LICS, Floyd-Warshall con stato extra, Knapsack, Greedy/Matroide, MST/Prim/Kruskal, NP-completezza e riduzioni classiche.
- Aggiornato `README.md` con stato attuale, struttura, uso della repo, fonti e warning residui.
- Aggiornato `PROJECT_STATUS.md` dichiarando la KB/RAG utilizzabile per studio ed esercizi.
- Semplificato `AI Chat during Exam/Final Prompt.md` in prompt generale da esame, senza duplicare tutte le ricorrenze delle method card.
- Verificata la presenza delle method card principali:
  - `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`
  - `10_rag/RAG_METHOD_CARDS/dp_lics_varianti.md`
  - `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`
  - `10_rag/RAG_METHOD_CARDS/dp_knapsack.md`
  - `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`
  - `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`

## Problemi rimasti

- Restano warning noti su OCR/appunti manoscritti: usare PDF ufficiali come fonte primaria quando disponibili.
- Alcuni file generali in `04_methods/` restano scaffold o supporto, non fonte primaria RAG.
- La copia PDF `kruskal+matrodi-copia.pdf` e conservata perche non identica all'originale omonimo.
- I duplicati di nome rilevati da `scripts/check_wikilinks.py` sono dichiarati e non bloccanti: i link RAG usano path espliciti.

## Query RAG testate

| Query | Retrieval index | Pattern map | File collegato | Esito |
| --- | --- | --- | --- | --- |
| LCS con due rossi consecutivi | presente | presente | `04_methods/dp_lcs_due_rossi_consecutivi.md` | OK |
| LCS tre sequenze | presente | presente | `04_methods/dp_lcs_tre_sequenze.md` | OK |
| LCS dispari pari | presente | presente | `04_methods/dp_lcs_dispari_pari_alternati.md` | OK |
| LICS | presente | presente | `04_methods/dp_lics_e_varianti.md` | OK |
| Floyd-Warshall archi alternati | presente | presente | `04_methods/fw_varianti_vincoli_colori.md` | OK |
| Floyd-Warshall esistenza | presente | presente | `04_methods/fw_varianti_vincoli_colori.md` | OK |
| Floyd-Warshall esattamente 3 archi rossi | presente | presente | `04_methods/fw_varianti_vincoli_colori.md` | OK |
| Knapsack al massimo 3 rossi | presente | presente | `04_methods/dp_knapsack_vincoli_colore.md` | OK |
| Knapsack base | presente | presente | `04_methods/dp_knapsack_base.md` | OK |
| Prim | presente | presente | `04_methods/mst_prim.md` | OK |
| Kruskal | presente | presente | `04_methods/metodo_kruskal_mst.md` | OK |
| Matroide grafico | presente | presente | `05_theory/kruskal_matroide_grafico.md` | OK |
| Greedy | presente | presente | `05_theory/greedy_teoria_base.md` | OK |
| P NP | presente | presente | `05_theory/p_np_np_completezza.md` | OK |
| NP-completezza | presente | presente | `04_methods/np_completezza_schema_dimostrazione.md` | OK |
| 3SAT Clique | presente | presente | `04_methods/metodo_riduzione_3sat_clique.md` | OK |
| Vertex Cover Independent Set | presente | presente | `05_theory/clique_vertex_cover_independent_set.md` | OK |

## Comandi eseguiti

- `git status --short`
- `rg --files`
- `rg "TODO|FIXME|DA VERIFICARE|path da verificare|MANCANTE|missing|duplic" -n .`
- `rg "RAG_METHOD_CARDS/|04_methods/|05_theory/|07_solved_examples/" 10_rag README.md "AI Chat during Exam"`
- `python scripts/check_wikilinks.py`
- scansione file temporanei/copie con PowerShell
- hash SHA256 su `kruskal+matrodi.pdf` e `kruskal+matrodi-copia.pdf`
