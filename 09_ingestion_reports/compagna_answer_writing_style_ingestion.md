# Ingestion stile risposta - SRC-NOTE-001

## Scopo dell'analisi

Analisi degli appunti `SRC-NOTE-001` non per estrarre nuove formule, ma per ricavare come impostare e scrivere gli esercizi sul foglio d'esame.

Principio guida:

```text
Correttezza matematica = RAG ufficiale, method card, appelli, materiale prof.
Stile di scrittura = appunti compagna + esempi validati + preferenze utente.
```

## Fonte osservata

- Source ID: `SRC-NOTE-001`
- File: `01_sources/notes_raw/Analisi E Progettazione Di Algoritmi.pdf`
- Trascrizione: `02_transcriptions/notes/note_analisi_e_progettazione_algoritmi.md`
- Ingestion precedente: `09_ingestion_reports/ingestion_report_note_analisi_e_progettazione_algoritmi.md`

## Pagine/sezioni osservate

- Pagine 1-8: LCS base, interleaving, LCS con lunghezza/somma, LICS.
- Pagine 9-22: knapsack colori, LCS con vincoli colore, varianti LICS e ricostruzione.
- Pagine 23-32: DP su grafi/Floyd-Warshall con stato esteso.
- Pagine 33-39: Dijkstra, Floyd-Warshall, BFS e grafi.
- Pagine 40-50: NP-completezza e riduzioni.
- Pagine 51-65: esercizi fotografati, riepiloghi e note miste.

## Pattern di scrittura estratti

- Gli esercizi DP su sequenze vengono aperti chiarendo istanza, soluzione, sottoproblema e variabile.
- I prefissi vengono definiti prima del coefficiente: `Xi=<x1,...,xi>`, `Yj=<y1,...,yj>`.
- La soluzione finale viene scritta come riga autonoma, non lasciata implicita.
- I casi base hanno formule compatte con micro-giustificazione.
- Il passo ricorsivo e scritto per casi, spesso distinguendo "prendo" e "non prendo".
- La ricostruzione segue la ricorrenza al contrario e stampa gli elementi dopo la chiamata ricorsiva quando serve mantenere l'ordine.
- Le parti teoriche usano definizione/enunciato, proprieta, giustificazione e conclusione.
- I completamenti testuali devono restituire la frase completa o l'insieme/valore finale, senza teoria superflua.

## Cosa integrare nel prompt/RAG

- Nuovo file `10_rag/RAG_ANSWER_WRITING_TEMPLATES.md`.
- Regola zero di rilettura della consegna.
- Schema DP: `ISTANZA -> SOLUZIONE -> SOTTOPROBLEMA -> Def. variabile -> CASO BASE -> PASSO RICORSIVO -> SOLUZIONE FINALE`.
- Regola di rispettare l'ordine numerato della traccia.
- Uso di micro-giustificazioni solo dove utili.
- Template teoria e completamenti testuali.
- Regola che vieta stati extra non richiesti, in particolare rosso -> rosso+blu.

## Cosa non integrare come ground truth

- Formule manoscritte non validate.
- Passaggi OCR ambigui.
- Varianti colore/parita con warning nella trascrizione.
- Esempi fotografati non leggibili con certezza.
- Scelte di notazione che confliggono con method card ufficiali.

## Checklist finale

- [x] Distinzione tra stile e correttezza esplicitata.
- [x] Nuovo template RAG creato.
- [x] Stile DP su sequenze reso operativo.
- [x] Teoria e completamenti testuali coperti.
- [x] Rischio "rosso -> rosso+blu" richiamato.
- [x] Appunti della compagna usati solo come fonte di forma.
