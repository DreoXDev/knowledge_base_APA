# Ingestion Report — Appello 2025-09-17 (Parte I)

## Dati della fonte

- **Source ID**: `SRC-EXAM-010`
- **Data dell'appello**: 17 Settembre 2025
- **Parte**: I
- **File sorgente**: `01_sources/exams_raw/parteI-17set25.pdf`

## Analisi strutturale degli esercizi

### Esercizio 1 — LCS a tre sequenze con al massimo 2 rossi
- **Tipologia**: Programmazione dinamica su sequenze
- **Problema**: Determinare una più lunga sottosequenza comune di $X$, $Y$ e $W$ nella quale vi siano al massimo 2 simboli rossi.
- **Pattern**: LCS a tre sequenze con budget di colore.
- **Deduplicazione**: Coincide esattamente con lo stesso schema degli appelli di febbraio 2025 (`exam_2025_02_11_p1_completo_e01` ed `exam_2025_02_11_p1_recupero_e01`). Verrà mappato sul metodo esistente [[metodo_lcs_tre_sequenze_vincolo_colori]] senza alcuna duplicazione di note metodologiche generiche.

### Esercizio 2 — Cammini con numero dispari di archi blu
- **Tipologia**: Programmazione dinamica su grafi
- **Problema**: Per ogni coppia di vertici $(i,j)$ stabilire se esiste un cammino da $i$ a $j$ nel quale vi è un numero dispari di archi blu.
- **Pattern**: DP booleana di esistenza su grafi con stato esteso per la parità modulo 2 del conteggio degli archi blu.
- **Metodo**: Introdotta la nuova nota metodologica comune [[metodo_dp_cammini_colori_parita]] che funge da modello base pulito per tutte le varianti di parità (esistenza e cammino minimo pesato).

## Tracciabilità e Collegamenti

- **Trascrizione**: [[exam_2025_09_17_part1]]
- **Esercizio 1**: [[exam_2025_09_17_p1_e01]]
- **Esercizio 2**: [[exam_2025_09_17_p1_e02]]
- **Metodo collegato Es. 1**: [[metodo_lcs_tre_sequenze_vincolo_colori]] e [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- **Metodo creato Es. 2**: [[metodo_dp_cammini_colori_parita]]

## Stato validazione trascrizione
La trascrizione è stata controllata ed è coerente con l'originale cartaceo. Le formule LaTeX sono state formalizzate in modo rigoroso, definendo la parità modulo 2 tramite addizione bitwise XOR $\oplus$ per il passo ricorsivo.
