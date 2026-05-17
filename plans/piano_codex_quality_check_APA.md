# Piano Codex — Quality check dopo applicazione report APA

## Obiettivo

Verificare che i report già applicati nella repo `knowledge_base_APA` siano coerenti tra loro e che la knowledge base sia pronta per continuare con il prossimo PDF raw.

Non creare nuovi esercizi se non mancano davvero.  
Non duplicare file già esistenti.  
Non risolvere gli esercizi.  
Fare solo controllo qualità, correzioni leggere e normalizzazione.

Repository:

```txt
https://github.com/DreoXDev/knowledge_base_APA
```

---

## Step 1 — Verifica stato reale della repo

Esegui:

```bash
git status
git branch --show-current
git log --oneline -5
find 09_ingestion_reports -maxdepth 1 -type f | sort
find 02_transcriptions/exams -maxdepth 1 -type f | sort
find 03_exercise_catalog/exercises -maxdepth 1 -type f | sort
find 04_methods -maxdepth 1 -type f | sort
find 05_theory -maxdepth 1 -type f | sort
find 06_exam_patterns -maxdepth 1 -type f | sort
```

Verifica che siano presenti almeno:

```txt
09_ingestion_reports/ingestion_report_exam_2026_01_12.md
09_ingestion_reports/ingestion_report_exam_2025_07_03_part1.md
09_ingestion_reports/ingestion_report_exam_2025_06_09_part1.md

02_transcriptions/exams/exam_2026_01_12.md
02_transcriptions/exams/exam_2025_07_03_part1.md
02_transcriptions/exams/exam_2025_06_09_part1.md

03_exercise_catalog/exercises/exam_2026_01_12_e01.md
03_exercise_catalog/exercises/exam_2026_01_12_e02.md
03_exercise_catalog/exercises/exam_2026_01_12_e03.md
03_exercise_catalog/exercises/exam_2026_01_12_e04.md
03_exercise_catalog/exercises/exam_2026_01_12_e05.md
03_exercise_catalog/exercises/exam_2026_01_12_e06.md
03_exercise_catalog/exercises/exam_2026_01_12_bonus_matroidi.md

03_exercise_catalog/exercises/exam_2025_07_03_p1_e01.md
03_exercise_catalog/exercises/exam_2025_07_03_p1_e02.md

03_exercise_catalog/exercises/exam_2025_06_09_p1_e01.md
03_exercise_catalog/exercises/exam_2025_06_09_p1_e02.md
```

---

## Step 2 — Controllare coerenza degli indici

Controlla questi file:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

Devono contenere tutti e tre gli appelli:

```txt
2026-01-12
2025-07-03 Parte I
2025-06-09 Parte I
```

Controlla che gli esercizi siano linkati con i nomi corretti:

```txt
[[exam_2026_01_12_e01]]
[[exam_2026_01_12_e02]]
[[exam_2026_01_12_e03]]
[[exam_2026_01_12_e04]]
[[exam_2026_01_12_e05]]
[[exam_2026_01_12_e06]]
[[exam_2026_01_12_bonus_matroidi]]
[[exam_2025_07_03_p1_e01]]
[[exam_2025_07_03_p1_e02]]
[[exam_2025_06_09_p1_e01]]
[[exam_2025_06_09_p1_e02]]
```

Se trovi link rotti o nomi diversi, correggili preferendo i nomi file già presenti.

---

## Step 3 — Controllare pattern ricorrenti

Controlla:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
```

Devono emergere chiaramente questi pattern:

```txt
DP formale Parte I
LCS con vincoli aggiuntivi
DP booleana su grafi con stato esteso
Zaino 0/1
Kruskal / MST
Riduzioni CLIQUE / VERTEX-COVER
NP-completezza
Matroidi
```

In particolare aggiorna `variations_by_appeal.md` se manca questa tabella concettuale:

```md
## Programmazione dinamica su sequenze

| Appello | Esercizio | Variante |
|---|---|---|
| 2025-07-03 Parte I | [[exam_2025_07_03_p1_e01]] | LCS con vincolo di ingombro |
| 2025-06-09 Parte I | [[exam_2025_06_09_p1_e01]] | LCS con massimo 2 rossi e 3 blu |

## Programmazione dinamica su grafi

| Appello | Esercizio | Variante |
|---|---|---|
| 2026-01-12 | [[exam_2026_01_12_e02]] | cammino con numero pari di archi |
| 2025-07-03 Parte I | [[exam_2025_07_03_p1_e02]] | cammino con esattamente 2 archi rossi e 2 archi blu |
| 2025-06-09 Parte I | [[exam_2025_06_09_p1_e02]] | cammino con vincoli di precedenza tra colori |
```

---

## Step 4 — Controllare metodi e teoria

Verifica che esistano i metodi:

```txt
04_methods/metodo_programmazione_dinamica_zaino_01.md
04_methods/metodo_ricostruzione_soluzione_dp.md
04_methods/metodo_programmazione_dinamica_lcs_vincolo_ingombro.md
04_methods/metodo_programmazione_dinamica_lcs_vincoli_colori.md
04_methods/metodo_dp_cammini_con_parita.md
04_methods/metodo_dp_cammini_colori_conteggi.md
04_methods/metodo_dp_cammini_colori_precedenze.md
04_methods/metodo_kruskal_mst.md
04_methods/metodo_riduzione_clique_vertex_cover.md
04_methods/metodo_dimostrare_np_completezza.md
```

Verifica che esista la teoria minima:

```txt
05_theory/programmazione_dinamica.md
05_theory/programmazione_dinamica_su_grafi.md
05_theory/lcs.md
05_theory/sottosequenze_comuni.md
05_theory/grafi.md
05_theory/grafi_colorati.md
05_theory/vincoli_su_colori.md
05_theory/zaino_01.md
05_theory/kruskal.md
05_theory/minimum_spanning_tree.md
05_theory/np_completezza.md
05_theory/clique.md
05_theory/vertex_cover.md
05_theory/matroidi.md
```

Se qualche file esiste ma è troppo vuoto, aggiungi solo uno scaffold minimo con:

```md
## Quando serve

## Esercizi collegati

## Pattern collegati

> [!Warning]
> Nota da completare durante la fase di soluzione.
```

---

## Step 5 — Correggere accenti mancanti dove evidente

Nei file appena generati alcuni testi potrebbero avere parole senza accenti, per esempio:

```txt
e invece di è
piu invece di più
sara invece di sarà
cioe invece di cioè
```

Correggere solo dove è ovvio e non rischia di rompere formule, nomi file, tag o link Obsidian.

Non modificare:

```txt
nomi file
tag
frontmatter keys
link Obsidian
codice
formule LaTeX
```

---

## Step 6 — Verificare PROJECT_STATUS.md e TODO.md

`PROJECT_STATUS.md` deve dire chiaramente che sono stati catalogati:

```txt
2026-01-12
2025-07-03 Parte I
2025-06-09 Parte I
```

`TODO.md` deve contenere task concreti per:

```txt
verifica manuale trascrizioni
consolidamento pattern Parte I
prime soluzioni prioritarie
prossimo PDF raw
```

Non deve più dire che bisogna “scegliere il primo esame”, perché il primo esame è già stato analizzato.

---

## Step 7 — Report finale del controllo

Alla fine, genera o aggiorna:

```txt
00_meta/repo_quality_check.md
```

Contenuto richiesto:

```md
# Repo Quality Check

## Data

YYYY-MM-DD

## Appelli verificati

- 2026-01-12
- 2025-07-03 Parte I
- 2025-06-09 Parte I

## File verificati

- ingestion reports
- trascrizioni
- catalogo esercizi
- indici
- metodi
- teoria
- pattern
- PROJECT_STATUS
- TODO

## Problemi trovati

- ...

## Correzioni fatte

- ...

## Prossimo step consigliato

Analizzare il prossimo PDF raw in `01_sources/exams_raw/`.
```

---

## Definition of Done

Il quality check è completo quando:

- [ ] `git status` è pulito prima o dopo il commit finale;
- [ ] tutti e tre gli appelli risultano presenti in report, trascrizioni e catalogo esercizi;
- [ ] gli indici linkano tutti gli esercizi;
- [ ] pattern, metodi e teoria minima sono coerenti;
- [ ] `PROJECT_STATUS.md` non è più fermo alla fase iniziale;
- [ ] `TODO.md` contiene task attuali;
- [ ] eventuali accenti ovvi sono stati corretti;
- [ ] `00_meta/repo_quality_check.md` è stato creato o aggiornato;
- [ ] commit finale creato con messaggio tipo:

```txt
Run quality check after APA ingestion reports
```
