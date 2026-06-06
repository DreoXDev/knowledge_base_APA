# RAG Trust Policy

## Gerarchia delle fonti

Quando rispondi a un esercizio, usa le fonti in questo ordine:

1. Esempio svolto verificato in `07_solved_examples/`
2. Metodo specifico completo in `04_methods/`
3. Pattern ricorrente in `06_exam_patterns/`
4. Catalogo esercizio in `03_exercise_catalog/`
5. Trascrizione appello in `02_transcriptions/`
6. Teoria generale in `05_theory/`

## Regole

- Per varianti LCS con vincoli di colore, se la traccia parla di "al massimo k rossi", preferire la formulazione ufficiale da `SRC-LECTURE-001`: stato `C[i][j][r]` = LCS dei prefissi con al massimo `r` rossi e soluzione `C[m][n][k]`.
- Per LCS di tre sequenze, due rossi consecutivi o dispari/pari per posizione, preferire `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md` e i metodi ufficiali collegati.
- Se una variante LCS usa stati vincolati a terminare nel match corrente, controllare se il valore finale e un massimo globale invece di `c_{m,n}`.
- Per MST, Prim e arco sicuro preferire `10_rag/RAG_METHOD_CARDS/mst_prim.md`, `04_methods/mst_greedy_base.md`, `04_methods/mst_prim.md` e `05_theory/teorema_arco_sicuro_mst.md`.
- Per LICS e varianti preferire `10_rag/RAG_METHOD_CARDS/dp_lics_varianti.md` e `04_methods/dp_lics_e_varianti.md`.
- Per zaino con al massimo 3 rossi preferire `10_rag/RAG_METHOD_CARDS/dp_knapsack_vincoli_colore.md`: lo stato ufficiale significa "al massimo r" e la risposta e `d_{n,C,3}`.
- Per Floyd-Warshall base e varianti ufficiali preferire `10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md`, `04_methods/fw_base_bottom_up.md` e `04_methods/fw_varianti_vincoli_colori.md`.
- Non inventare metodi non presenti nella KB.
- Non usare file con `status: draft` se esiste un metodo specifico `complete`.
- Se un file contiene warning, riporta internamente il warning e usa la variante piu prudente.
- Se non trovi un metodo collegato, rispondi con un template generale ma considera la soluzione ricostruita da pattern, non da esempio identico.
- Non dare spiegazioni lunghe: durante l'esame servono formule, pseudocodice, complessita e breve correttezza.
- Se ci sono piu varianti possibili, scegli quella piu simile agli appelli gia catalogati.
