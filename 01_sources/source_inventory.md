# Source Inventory

> [!Info]
> Inventario delle fonti originali usate per costruire la knowledge base.
>
> I file originali non devono essere modificati. Ogni fonte deve avere un ID stabile.

## Stato fonti

| Source ID | Tipo | Percorso | Descrizione | Stato | Report ingestione | Note |
|---|---|---|---|---|---|---|
| SRC-EXAM-001 | appello | `01_sources/exams_raw/parteI-13gen25.pdf` | Parte I, appello 13 gennaio 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_01_13_part1.md` | Catalogata Parte I con 2 esercizi DP (LCS budget 3R/2B e cammini con esclusione transizioni) |
| SRC-EXAM-002 | appello | `01_sources/exams_raw/parteII-13gen25.pdf` | Parte II, appello 13 gennaio 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_01_13_part2.md` | Ingestita Parte II: Dijkstra, 3-SAT to CLIQUE, ricorrenza Warshall, criteri NPC, dimostrazione matroide grafico e 4 domande bonus |
| SRC-EXAM-003 | appello | `01_sources/exams_raw/parteI-11feb25-completo.pdf` | Parte I, appello completo 11 febbraio 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_completo.md` | Catalogata Parte I scritto completo con 2 esercizi DP (LCS 3 sequenze e cammini NN/BB) |
| SRC-EXAM-004 | appello | `01_sources/exams_raw/parteI-11feb25-recupero.pdf` | Parte I, recupero 11 febbraio 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_02_11_part1_recupero.md` | Catalogato recupero della Parte I con 2 esercizi DP (LCS a 3 sequenze e cammini minimi con parità) |
| SRC-EXAM-005 | appello | `01_sources/exams_raw/parteII-11feb25-completo-recupero.pdf` | Parte II, completo e recupero 11 febbraio 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_02_11_part2_completo_recupero.md` | Catalogata Parte II con 5 esercizi (Kruskal, CLIQUE-VC, zaino DP, 3-SAT, arco sicuro) e 3 domande bonus |
| SRC-EXAM-006 | appello | `01_sources/exams_raw/parteI-09giu25.pdf` | Parte I, appello 9 giugno 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_06_09_part1.md` | Parte I catalogata: 2 esercizi di programmazione dinamica |
| SRC-EXAM-007 | appello | `01_sources/exams_raw/parteII-09giu25.pdf` | Parte II, appello 9 giugno 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_06_09_part2.md` | Ingestita Parte II: Dijkstra, riduzione CLIQUE-VC, Greedy-Max & Rado, requisiti NP-completezza, dimostrazione matroide grafico |
| SRC-EXAM-008 | appello | `01_sources/exams_raw/parteI-03lug25.pdf` | Parte I, appello 3 luglio 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_07_03_part1.md` | Parte I catalogata: 2 esercizi di programmazione dinamica |
| SRC-EXAM-009 | appello | `01_sources/exams_raw/parteII-03lug25.pdf` | Parte II, appello 3 luglio 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_07_03_part2.md` | Ingestita Parte II: Dijkstra, riduzione CLIQUE-VC, ricorrenza Warshall, definizioni formali P/NP/NPC, dimostrazione Safe Edge Theorem |
| SRC-EXAM-010 | appello | `01_sources/exams_raw/parteI-17set25.pdf` | Parte I, appello 17 settembre 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_09_17_part1.md` | Catalogata Parte I con 2 esercizi DP (LCS a 3 sequenze budget rossi e cammini con parità archi blu) |
| SRC-EXAM-011 | appello | `01_sources/exams_raw/parteII-17set25.pdf` | Parte II, appello 17 settembre 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_09_17_part2.md` | Ingestita Parte II: Kruskal, 3-SAT to CLIQUE (C1=C3), GREEDY-MAX/Rado, criteri NPC, dimostrazione matroide grafico |
| SRC-EXAM-012 | appello | `01_sources/exams_raw/parte-I-10nov25-A.pdf` | Parte I, appello 10 novembre 2025, variante A | applicato | `09_ingestion_reports/ingestion_report_exam_2025_11_10_part1_tema_a.md` | Catalogata variante A della Parte I con 2 esercizi DP |
| SRC-EXAM-013 | appello | `01_sources/exams_raw/parteII-10nov25.pdf` | Parte II, appello 10 novembre 2025 | applicato | `09_ingestion_reports/ingestion_report_exam_2025_11_10_part2.md` | Ingestita Parte II: Kruskal, riduzione 3-SAT to CLIQUE, ricorrenza Warshall, requisiti NPC, dimostrazione matroide grafico |
| SRC-EXAM-014 | appello | `01_sources/exams_raw/esame_apa_12_01_2026.pdf` | Esame APA 12 gennaio 2026 | applicato | `09_ingestion_reports/ingestion_report_exam_2026_01_12.md` | Contiene Parte I, Parte II e domanda bonus; alias report originale: `exam_2026_01_12` |
| SRC-NOTE-001 | appunti | `01_sources/notes_raw/Analisi E Progettazione Di Algoritmi.pdf` | Appunti della compagna su Analisi e Progettazione di Algoritmi | applicato con warning | `09_ingestion_reports/ingestion_report_note_analisi_e_progettazione_algoritmi.md` | Trascrizione interpretativa e metodi integrati; verificare formule ambigue |
| SRC-EXTRA-001 | extra | `01_sources/extra_materials/esercizi APA.pdf` | Raccolta di esercizi APA o materiale di supporto | applicato con warning | `09_ingestion_reports/ingestion_report_extra_esercizi_APA_SRC_EXTRA_001.md` | Trascrizione e integrazione metodi Parte I; verificare punti ambigui |
