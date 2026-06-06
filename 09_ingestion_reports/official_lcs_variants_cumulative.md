# Ingestion report - varianti LCS ufficiali cumulative

## Fonti

| Source ID | PDF | Variante | Stato |
|---|---|---|---|
| SRC-OFFICIAL-EX-016 | `01_sources/extra_materials/lcs-three-sequences-20ott25.pdf` | LCS di 3 sequenze | applicato |
| SRC-OFFICIAL-EX-014 | `01_sources/extra_materials/lcs-atleast-2-consecutive-red.pdf` | LCS con due rossi consecutivi | applicato |
| SRC-OFFICIAL-EX-015 | `01_sources/extra_materials/lcs-even-odd.pdf` | LCS dispari/pari per posizione | applicato |

## Piano cumulativo applicato

I tre piani sono stati unificati nella famiglia "varianti LCS ufficiali con stati estesi".

Decisioni:

- creare `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md` come card generale;
- lasciare `dp_lcs_colori.md` per conteggi/budget di colore e collegare la variante dei due rossi consecutivi dalla card generale;
- creare tre metodi separati in `04_methods/`;
- creare tre schemi da esame in `07_solved_examples/dp/`;
- aggiornare retrieval, pattern map, stile risposta e prompt durante esame.

## File principali creati

- `10_rag/RAG_METHOD_CARDS/dp_lcs_varianti.md`
- `04_methods/dp_lcs_tre_sequenze.md`
- `04_methods/dp_lcs_due_rossi_consecutivi.md`
- `04_methods/dp_lcs_dispari_pari_alternati.md`
- `07_solved_examples/dp/lcs_tre_sequenze_schema.md`
- `07_solved_examples/dp/lcs_due_rossi_consecutivi_schema.md`
- `07_solved_examples/dp/lcs_dispari_pari_alternati_schema.md`

## Note di affidabilita

Le varianti sono marcate `official_confirmed` perche derivate da PDF ufficiali. Le vecchie note draft su alternanza pari/dispari da `SRC-EXTRA-001` restano non primarie.
