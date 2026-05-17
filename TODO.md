# TODO

## Setup

- [x] Create folder structure
- [x] Create `_README.md` in every main folder
- [x] Create all templates
- [x] Create initial indexes

## PDF ingestion setup

- [x] Verify all PDFs are placed in the correct source folders
- [x] Populate `01_sources/source_inventory.md`
- [x] Create `09_ingestion_reports/`
- [x] Create `09_ingestion_reports/_README.md`
- [x] Create `09_ingestion_reports/ingestion_report_template.md`
- [x] Update `AI_CONTEXT.md` with ingestion workflow
- [x] Update `PROJECT_STATUS.md` with PDF processing status

## Applied ingestion reports

- [x] Apply `2026-01-12` full exam report
- [x] Apply `2025-07-03 Parte I` report
- [x] Apply `2025-06-09 Parte I` report
- [x] Apply `2025-11-10 Parte I Tema A` report
- [x] Apply `2025-02-11 Parte I completo` report
- [x] Apply `2025-02-11 Parte I recupero` report
- [x] Apply `2025-01-13 Parte I` report

## Prossimi step

- [ ] Verificare manualmente trascrizione dell'appello `2025-06-09 Parte I`
- [ ] Risolvere `exam_2025_06_09_p1_e01` LCS con vincoli sui colori
- [ ] Risolvere `exam_2025_06_09_p1_e02` cammini con vincoli di precedenza tra colori
- [ ] Consolidare metodo comune per LCS con vincoli aggiuntivi
- [ ] Consolidare metodo comune per DP booleana su grafi con stato esteso
- [x] Creare una nota di sintesi sui pattern di Parte I (Risolto con [[parte_i_dynamic_programming_patterns]])
- [ ] Verificare manualmente trascrizione dell'appello `2025-07-03 Parte I`
- [ ] Risolvere `exam_2025_07_03_p1_e01` LCS con vincolo di ingombro
- [ ] Risolvere `exam_2025_07_03_p1_e02` cammini con conteggi di colori
- [ ] Verificare manualmente trascrizione dell'appello `2026-01-12`
- [ ] Risolvere `exam_2026_01_12_e05` come base per zaino 0/1
- [ ] Risolvere completamente `exam_2025_11_10_p1_tema_a_e01` (presenza del rosso nella LCS)
- [ ] Risolvere completamente `exam_2025_11_10_p1_tema_a_e02` (cammini con #A + #B = 3)
- [ ] Verificare manualmente trascrizione dell'appello `2025-02-11 Parte I`
- [ ] Risolvere completamente `exam_2025_02_11_p1_completo_e01` (LCS a tre sequenze)
- [ ] Risolvere completamente `exam_2025_02_11_p1_completo_e02` (cammini senza NN/BB consecutivi)
- [ ] Risolvere completamente `exam_2025_02_11_p1_recupero_e02` (cammini minimi con parità ed esclusione)
- [ ] Verificare deduplicazione tra `exam_2025_02_11_p1_completo_e01` ed `exam_2025_02_11_p1_recupero_e01`
- [ ] Risolvere completamente `exam_2025_01_13_p1_e01` (LCS budget 3R/2B)
- [ ] Risolvere completamente `exam_2025_01_13_p1_e02` (cammini con esclusione transizioni)
- [ ] Creare tabella comparativa varianti LCS con budget (2R/3B, 3R/2B, 3 sequenze con 2R, rosso obbligatorio)
- [ ] Creare tabella comparativa varianti DP su grafi (esistenza, parità, cammini minimi, precedenze di sequenza, consecutività)
- [ ] Analizzare prossimo PDF in `01_sources/exams_raw/`

## Cataloging

- [ ] Catalog each remaining exercise from past exams
- [ ] Assign each remaining exercise a topic
- [ ] Identify recurring patterns across multiple exams
- [ ] Link exercises to methods and theory notes

## Study material

- [ ] Complete method notes from applied ingestion reports
- [ ] Complete theory notes from applied ingestion reports
- [ ] Write solved examples from applied ingestion reports
- [ ] Create pre-exam checklist

