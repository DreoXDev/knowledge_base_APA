# Ingestion Report — Exam 2025-02-11 Part I (Recupero Parziale)

## Metadata della fonte

- **Source ID**: `SRC-EXAM-004`
- **File**: `01_sources/exams_raw/parteI-11feb25-recupero.pdf`
- **Tipo**: appello esame scritto (Parte I, recupero parziale)
- **Data appello**: 11 febbraio 2025
- **Parte**: I (programmazione dinamica)
- **Stato**: applicato
- **Data ingestion**: 17 maggio 2026

---

## Analisi del contenuto

L'appello di recupero parziale della Parte I dell'11 febbraio 2025 contiene due esercizi di programmazione dinamica:

### Esercizio 1: LCS a tre sequenze con al massimo due rossi
- **Tipologia**: Sottosequenza comune massima (LCS) a tre sequenze ($X$, $Y$ e $W$) con vincolo di colore sui simboli dell'alfabeto.
- **Dettagli**: Ogni simbolo ha colore rosso ($R$), blu ($B$) o nero ($N$). Si richiede una LCS con al massimo due simboli rossi.
- **Valutazione di coincidenza**: Questo esercizio è del tutto coincidente con l'Esercizio 1 dello scritto completo dello stesso giorno. Viene censito come esercizio a sé per completezza, ma farà riferimento allo stesso metodo `metodo_lcs_tre_sequenze_vincolo_colori` per evitare duplicazioni.

### Esercizio 2: Cammini minimi vincolati su grafo colorato e pesato
- **Tipologia**: Ricerca di cammini minimi tra tutte le coppie $(i,j)$ su un grafo pesato con vincoli di colore aggiuntivi sia sugli archi che sui vertici.
- **Dettagli**:
  - Vertici colorati in $\{R,N\}$ (rosso, nero) con vincolo: esclusi cammini con due vertici rossi consecutivi.
  - Archi colorati in $\{M,B\}$ (marrone, blu) con vincolo: il cammino deve contenere un numero dispari di archi blu.
  - Obiettivo: calcolare il peso minimo per ciascuna coppia.
- **Valutazione metodologica**: Richiede una formulazione in stile Floyd-Warshall con stato esteso per tenere traccia della parità modulo 2 del numero di archi blu ($p \in \{0,1\}$). Il vincolo sui vertici consecutivi rossi viene verificato localmente sugli archi del caso base.

---

## Mappatura dei file della Knowledge Base

- **Trascrizione**: [[exam_2025_02_11_part1_recupero]] in `02_transcriptions/exams/`
- **Esercizio 1**: [[exam_2025_02_11_p1_recupero_e01]] in `03_exercise_catalog/exercises/`
- **Esercizio 2**: [[exam_2025_02_11_p1_recupero_e02]] in `03_exercise_catalog/exercises/`
- **Metodi associati**:
  - Esercizio 1: [[metodo_lcs_tre_sequenze_vincolo_colori]] (già esistente)
  - Esercizio 2: [[metodo_cammini_minimi_vincoli_colori_parita]] (nuovo)
