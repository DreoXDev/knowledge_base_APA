---
type: ingestion_report
source_id: SRC-EXTRA-001
status: applied_with_warnings
tags:
  - apa
  - ingestion-report
  - source/SRC-EXTRA-001
---

# Ingestion report - esercizi APA

Fonte: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf

## Sintesi

> [!Summary]
> La fonte manoscritta `esercizi APA.pdf` e stata integrata come riferimento metodologico per esercizi di Programmazione Dinamica di Parte I. Sono stati creati trascrizione pagina-per-pagina, metodi mancanti, esempi svolti, review comparative e collegamenti agli esercizi gia catalogati.

## File creati

- [[esercizi_APA_SRC_EXTRA_001]]
- [[metodo_lcs_base]]
- [[metodo_lis_lds]]
- [[metodo_lics]]
- [[metodo_hateville_vincoli_colori]]
- [[metodo_lcs_alternanza_pari_dispari]]
- [[lcs_crescente_esempio_SRC_EXTRA_001]]
- [[lis_esempio_SRC_EXTRA_001]]
- [[lds_esempio_SRC_EXTRA_001]]
- [[lcs_esattamente_3_rossi_SRC_EXTRA_001]]
- [[lcs_tutte_almeno_3_rossi_SRC_EXTRA_001]]
- [[lcs_tutte_parita_rossi_SRC_EXTRA_001]]
- [[lcs_ingombro_SRC_EXTRA_001]]
- [[hateville_senza_due_rossi_consecutivi_SRC_EXTRA_001]]
- [[knapsack_max_R_rossi_SRC_EXTRA_001]]
- [[lics_SRC_EXTRA_001]]
- [[lcs_alternanza_pari_dispari_SRC_EXTRA_001]]
- [[parte_i_dp_checklist]]
- [[varianti_lcs_con_vincoli]]
- [[flashcards_parte_i_dp]]

## File aggiornati

- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]
- [[metodo_programmazione_dinamica_zaino_01]]
- [[parte_i_dynamic_programming_patterns]]
- [[TODO]]
- [[PROJECT_STATUS]]
- indici in `03_exercise_catalog/`, `04_methods/`, `07_solved_examples/`, `08_review/`, `09_ingestion_reports/`

## Ambiguita preservate

> [!Warning]
> Hateville senza due rossi consecutivi: il passo ricorsivo di pagina 12 non e completamente leggibile.

> [!Warning]
> Parita dei rossi in tutte le LCS: le pagine 08-10 sembrano usare convenzioni potenzialmente invertite. La KB normalizza $p=0$ pari e $p=1$ dispari.

> [!Warning]
> LCS con alternanza pari/dispari: la fonte non basta per fissare una ricorrenza definitiva. Il metodo e stato creato in stato draft.

## Collegamenti principali

| Pattern | Fonte | Metodo | Esempio |
|---|---|---|---|
| LCS base | p.3 | [[metodo_lcs_base]] | - |
| LIS/LDS | pp.1-2 | [[metodo_lis_lds]] | [[lis_esempio_SRC_EXTRA_001]], [[lds_esempio_SRC_EXTRA_001]] |
| LICS | pp.1,15 | [[metodo_lics]] | [[lics_SRC_EXTRA_001]] |
| LCS esattamente 3 rossi | pp.4-6 | [[metodo_programmazione_dinamica_lcs_vincoli_colori]] | [[lcs_esattamente_3_rossi_SRC_EXTRA_001]] |
| Tutte le LCS almeno 3 rossi | p.7 | [[metodo_programmazione_dinamica_lcs_vincoli_colori]] | [[lcs_tutte_almeno_3_rossi_SRC_EXTRA_001]] |
| Tutte le LCS con parita rossi | pp.8-10 | [[metodo_programmazione_dinamica_lcs_vincoli_colori]] | [[lcs_tutte_parita_rossi_SRC_EXTRA_001]] |
| LCS con ingombro | p.11 | [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]] | [[lcs_ingombro_SRC_EXTRA_001]] |
| Hateville con colori | p.12 | [[metodo_hateville_vincoli_colori]] | [[hateville_senza_due_rossi_consecutivi_SRC_EXTRA_001]] |
| Knapsack max rossi | pp.13-14,16-17 | [[metodo_programmazione_dinamica_zaino_01]] | [[knapsack_max_R_rossi_SRC_EXTRA_001]] |
| LCS alternanza pari/dispari | pp.17-18 | [[metodo_lcs_alternanza_pari_dispari]] | [[lcs_alternanza_pari_dispari_SRC_EXTRA_001]] |

## TODO residui

- Verificare manualmente la ricorrenza di Hateville.
- Verificare la convenzione di parita nelle pagine 08-10.
- Completare LCS alternanza pari/dispari con SRC-NOTE-001 o derivazione separata.
- Confrontare le varianti "esattamente", "al massimo" e "tutte" nei prossimi esercizi svolti.
