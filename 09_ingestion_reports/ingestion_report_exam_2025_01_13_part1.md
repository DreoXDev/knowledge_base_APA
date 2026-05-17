# Ingestion Report — Appello 2025-01-13 (Parte I)

> [!Info]
> * **Source ID**: `SRC-EXAM-001`
> * **File originale**: `parteI-13gen25.pdf`
> * **Data esame**: 13 Gennaio 2025
> * **Stato**: Ingested & Cataloged
> * **Tipo**: Scritto Parte I (Programmazione Dinamica)

---

## 1. Contesto e Argomenti Principali

L'appello del **13 Gennaio 2025 (Parte I)** presenta due classici problemi di Programmazione Dinamica da formulare con estremo rigore:
1. **LCS con budget multi-colore**: Un esercizio su sequenze dove la più lunga sottosequenza comune (LCS) deve rispettare due contatori di colore indipendenti: al più 3 simboli rossi e al più 2 simboli blu.
2. **DP booleana su grafi colorati**: Un problema di connettività in cui le coppie di archi consecutivi nel cammino non devono violare regole di sequenza locali: nero non può essere seguito da rosso $(N,R)$ e rosso non può essere seguito da blu $(R,B)$.

---

## 2. Analisi degli Esercizi

### Esercizio 1 — LCS con budget $\le 3$ rossi e $\le 2$ blu
* **Tipo**: DP su sequenze (Stato Esteso).
* **Stato**: Catalogato come [[exam_2025_01_13_p1_e01]].
* **Fattibilità formale**: Altissima. La ricorrenza standard per la LCS viene estesa introducendo due dimensioni extra nello stato:
  $$C[i, j, r, b]$$
  dove $r$ rappresenta i rossi utilizzabili (da 0 a 3) e $b$ i blu utilizzabili (da 0 a 2). La propagazione delle risorse avviene solo nel caso in cui i caratteri finali delle sequenze coincidono e vengono scelti per estendere la LCS.

### Esercizio 2 — Cammini con esclusione di transizioni consecutive di colore
* **Tipo**: DP su grafi (Problema Ausiliario / Stato Esteso).
* **Stato**: Catalogato come [[exam_2025_01_13_p1_e02]].
* **Fattibilità formale**: Altissima. Poiché il vincolo è locale e dipende dal colore di archi consecutivi, è necessario definire un problema ausiliario:
  $$D[k, i, j, a, b]$$
  vero se esiste un cammino valido da $i$ a $j$ con nodi intermedi in $\{1,\dots,k\}$, avente primo arco di colore $a$ e ultimo arco di colore $b$.
  I vincoli vietano le coppie consecutive $(N,R)$ e $(R,B)$, rendendo la propagazione tramite nodo intermedio $k$ controllabile validando la compatibilità tra l'ultimo arco della prima metà e il primo della seconda metà: $compatibile(\beta, \gamma)$.

---

## 3. Azioni Eseguite e Collegamenti

* **Trascrizione**: Creata trascrizione pulita ed essenziale in [[exam_2025_01_13_part1]].
* **Catalogazione**:
  * Esercizio 1: [[exam_2025_01_13_p1_e01]].
  * Esercizio 2: [[exam_2025_01_13_p1_e02]].
* **Metodi**: Aggiornati i metodi esistenti [[metodo_programmazione_dinamica_lcs_vincoli_colori]] e [[metodo_dp_cammini_colori_precedenze]].
* **Pattern**: Registrata la presenza in [[recurring_exercise_types]], [[variations_by_appeal]], [[high_yield_topics]] e [[parte_i_dynamic_programming_patterns]].
