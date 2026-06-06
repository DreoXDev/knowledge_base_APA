# Piano finale Codex/Antigravity — Verifica, pulizia e completamento KB/RAG APA

## Scopo

Questo è il piano finale di chiusura per la repository:

```text
https://github.com/DreoXDev/knowledge_base_APA
```

Dopo l’applicazione dei piani sugli esercizi e dei piani teorici prioritari, il modello deve fare un controllo complessivo della repo e completare solo ciò che manca davvero.

L’obiettivo non è aggiungere nuovo contenuto massivo, ma verificare che la Knowledge Base APA sia:
- coerente;
- navigabile;
- pronta per lo studio;
- pronta per essere usata come contesto RAG;
- pronta per aiutare nella risoluzione di esercizi e domande teoriche;
- priva di duplicazioni e contraddizioni evidenti.

---

## Stato atteso prima di iniziare

Dovrebbero essere già stati applicati, o essere in corso di applicazione, i piani relativi a:

### Esercizi

- LCS standard e varianti;
- LCS con vincoli di colore;
- LCS con vincoli di consecutività;
- LCS dispari/pari;
- LCS su tre sequenze;
- Floyd-Warshall base e varianti;
- MST;
- Prim;
- Kruskal;
- LICS;
- Knapsack base e varianti con colori.

### Teoria prioritaria

- Knapsack 0/1;
- greedy;
- matroidi;
- matroide grafico;
- Kruskal;
- P/NP;
- SAT/3SAT;
- NP-completezza;
- riduzioni;
- Clique;
- Vertex Cover;
- Independent Set.

---

# Fase 1 — Audit iniziale della repo

## Obiettivo

Prima di modificare qualsiasi file, guardare la repo e capire lo stato reale.

## Comandi consigliati

```bash
git status
find . -maxdepth 3 -type f | sort
find 04_methods 05_theory 06_exam_patterns 07_solved_examples 10_rag -type f | sort
```

Controllare anche:

```bash
grep -R "TODO\|FIXME\|DA VERIFICARE\|path da verificare\|contraddizione\|duplic" -n .
```

## Cose da verificare

- Tutti i piani applicati hanno prodotto file nei path corretti.
- Non ci sono file duplicati con nomi quasi uguali.
- Non ci sono file vuoti o placeholder.
- Non ci sono path rotti nei link Markdown.
- Le cartelle principali sono coerenti:
  - `04_methods/`
  - `05_theory/`
  - `06_exam_patterns/`
  - `07_solved_examples/`
  - `09_ingestion_reports/`
  - `10_rag/`
  - `AI Chat during Exam/`

## Output richiesto

Creare o aggiornare un file di audit finale:

```text
09_ingestion_reports/final_repo_audit.md
```

Contenuto minimo:

```md
# Final repo audit — APA KB/RAG

## Data

...

## Stato generale

- [ ] Methods completi
- [ ] Theory essenziale completa
- [ ] Solved examples/schemi completi
- [ ] RAG aggiornato
- [ ] Prompt finale aggiornato
- [ ] README aggiornato
- [ ] Nessuna duplicazione pesante
- [ ] Nessun link rotto evidente

## Problemi trovati

...

## Modifiche applicate

...

## Modifiche rimandate

...
```

---

# Fase 2 — Controllo struttura e duplicazioni

## Obiettivo

Evitare che l’applicazione di tanti piani abbia creato contenuti ridondanti.

## Controlli specifici

Cercare file duplicati o sovrapposti su:

```text
LCS
LICS
Floyd-Warshall
Knapsack
MST
Prim
Kruskal
Greedy
Matroidi
P/NP
Riduzioni
```

Comandi utili:

```bash
find . -iname "*lcs*" -o -iname "*lics*" -o -iname "*floyd*" -o -iname "*fw*" -o -iname "*knapsack*" -o -iname "*zaino*" -o -iname "*mst*" -o -iname "*prim*" -o -iname "*kruskal*" -o -iname "*greedy*" -o -iname "*matroid*" -o -iname "*riduz*" -o -iname "*np*"
```

## Regola

Se ci sono due file simili:
- mantenere un file principale autorevole;
- trasformare l’altro in indice/sintesi/link;
- non duplicare ricorrenze, teoremi o definizioni in più punti.

## Esempi

Per Floyd-Warshall, il file principale dovrebbe essere:

```text
04_methods/fw_varianti_vincoli_colori.md
10_rag/RAG_METHOD_CARDS/fw_varianti_vincoli_colori.md
```

Eventuali file come:

```text
fw_alternanza_colori.md
fw_varianti_conteggi_colori.md
```

devono essere ridotti a supporto o link, se esistono ancora.

Per Knapsack, distinguere:

```text
04_methods/dp_knapsack_base.md
04_methods/dp_knapsack_vincoli_colore.md
```

ma evitare di ripetere tutta la teoria base nel file della variante.

---

# Fase 3 — Verifica contenuti esercizi

## Obiettivo

Controllare che i metodi principali per gli esercizi siano tutti presenti e recuperabili.

## Checklist metodi

Verificare che esistano o siano coperti da file equivalenti:

```text
04_methods/dp_lcs_base.md
04_methods/dp_lcs_vincoli_colore.md
04_methods/dp_lcs_due_rossi_consecutivi.md
04_methods/dp_lcs_dispari_pari_alternati.md
04_methods/dp_lcs_tre_sequenze.md
04_methods/dp_lics_e_varianti.md
04_methods/fw_base_bottom_up.md
04_methods/fw_varianti_vincoli_colori.md
04_methods/dp_knapsack_base.md
04_methods/dp_knapsack_vincoli_colore.md
04_methods/mst_greedy_base.md
04_methods/mst_prim.md
04_methods/mst_kruskal.md
04_methods/np_completezza_schema_dimostrazione.md
```

Se i nomi reali sono diversi, non rinominare necessariamente: aggiornare gli indici/RAG in modo che puntino ai path reali.

## Controlli qualitativi

Per ogni metodo importante verificare che contenga:

- problema;
- input/output;
- stato/sottoproblema;
- coefficiente;
- casi base;
- ricorrenza o algoritmo;
- valore finale;
- complessità;
- warning/errori comuni;
- collegamento al RAG o ad altri file.

---

# Fase 4 — Verifica teoria essenziale

## Obiettivo

Controllare che la teoria sia sufficiente per rispondere a domande teoriche senza diventare troppo lunga.

## File teorici attesi o equivalenti

```text
05_theory/dp_knapsack_base.md
05_theory/greedy_teoria_base.md
05_theory/matroidi_e_greedy.md
05_theory/kruskal_matroide_grafico.md
05_theory/teorema_arco_sicuro_mst.md
05_theory/p_np_np_completezza.md
05_theory/riduzioni_np_completezza.md
05_theory/programmazione_dinamica_floyd_warshall_varianti.md
```

## Regola

I file teorici devono essere:
- compatti;
- utili per domande d’esame;
- collegati ai metodi;
- non pieni di testo narrativo inutile.

## Controlli specifici

### Greedy

Verificare che siano presenti:
- idea di scelta locale;
- necessità di dimostrazione;
- differenza con DP;
- esempi;
- warning su knapsack 0/1.

### Matroidi

Verificare:
- sistema di indipendenza;
- proprietà ereditaria;
- proprietà di scambio;
- greedy corretto su matroidi;
- matroide grafico.

### NP-completezza

Verificare:
- problemi di decisione;
- P;
- NP;
- certificato;
- verificatore;
- riduzione polinomiale;
- NP-completezza;
- direzione corretta della riduzione;
- schema `problema noto NP-completo <=p problema target`.

---

# Fase 5 — Aggiornamento README

## Obiettivo

Il README deve spiegare come usare la repo per studiare e come usarla come KB/RAG.

## File da aggiornare

```text
README.md
```

## Contenuto consigliato

Aggiornare il README con sezioni compatte:

```md
# Knowledge Base APA

## Scopo

Questa repo contiene una Knowledge Base per l’esame di Analisi e Progettazione di Algoritmi.

Obiettivi:
- studio personale;
- risoluzione esercizi;
- recupero rapido di metodi;
- supporto RAG per AI;
- preparazione domande teoriche.

## Struttura

| Cartella | Contenuto |
|---|---|
| `01_sources/` | PDF e fonti raw |
| `04_methods/` | metodi operativi per esercizi |
| `05_theory/` | teoria essenziale |
| `06_exam_patterns/` | pattern ricorrenti d’esame |
| `07_solved_examples/` | schemi ed esempi svolti |
| `09_ingestion_reports/` | report di analisi e audit |
| `10_rag/` | entrypoint, method card, index, prompt e regole RAG |
| `AI Chat during Exam/` | prompt finale e sezioni per uso AI |

## Come studiare

1. Partire da `10_rag/RAG_ENTRYPOINT.md` o equivalente.
2. Usare `04_methods/` per gli esercizi.
3. Usare `05_theory/` per domande teoriche.
4. Usare `07_solved_examples/` per schemi da esame.
5. Usare `10_rag/RAG_RETRIEVAL_INDEX.md` per cercare rapidamente il file giusto.

## Fonti

Ordine di affidabilità:
1. PDF ufficiali del professore;
2. appelli ufficiali;
3. appunti della compagna, se coerenti;
4. inferenze/integrazioni Codex.

## Stato

Indicare che la repo è stata aggiornata con:
- esercizi passati;
- appunti;
- PDF ufficiali di esercizi;
- teoria prioritaria.

Linkare `09_ingestion_reports/final_repo_audit.md`.
```

## Attenzione

Non trasformare il README in un riassunto del corso. Deve essere una guida di navigazione.

---

# Fase 6 — Aggiornamento RAG

## Obiettivo

Il RAG deve sapere dove trovare i contenuti e quali file sono autorevoli.

## File da controllare/aggiornare

```text
10_rag/RAG_ENTRYPOINT.md
10_rag/RAG_RETRIEVAL_INDEX.md
10_rag/RAG_PATTERN_MAP.md
10_rag/RAG_EXAM_ANSWER_STYLE.md
10_rag/RAG_TRUST_POLICY.md
10_rag/RAG_METHOD_CARDS/
```

## Controlli

### `RAG_RETRIEVAL_INDEX.md`

Deve contenere entry per almeno:

- LCS base;
- LCS con vincoli colore;
- LCS due rossi consecutivi;
- LCS dispari/pari;
- LCS tre sequenze;
- LICS;
- Floyd-Warshall base;
- Floyd-Warshall varianti;
- Knapsack base;
- Knapsack vincoli colore;
- MST;
- Prim;
- Kruskal;
- Greedy;
- Matroidi;
- P/NP;
- Riduzioni;
- NP-completezza;
- 3SAT/Clique;
- Vertex Cover/Clique/Independent Set.

### `RAG_PATTERN_MAP.md`

Deve aiutare a riconoscere rapidamente gli esercizi.

Aggiungere o verificare pattern per:
- DP su sequenze;
- DP con stato extra;
- Floyd-Warshall con stato extra;
- knapsack;
- greedy/MST;
- NP-completezza.

### `RAG_METHOD_CARDS/`

Verificare che le method card non siano troppe e duplicate.

Card consigliate:
- `dp_lcs_varianti.md`
- `dp_lics_varianti.md`
- `fw_varianti_vincoli_colori.md`
- `dp_knapsack.md`
- `greedy_matroidi_mst.md`
- `np_completezza_riduzioni.md`

Se i nomi sono diversi, aggiornare index e README con i path reali.

---

# Fase 7 — Prompt finale

## Obiettivo

Il prompt finale deve essere utile per una nuova chat/AI durante studio o simulazione, ma non deve essere un dump della KB.

Il prompt finale deve contenere soprattutto le richieste dell’utente e le regole operative generali, non tutta la teoria.

## File da controllare

```text
AI Chat during Exam/Final Prompt.md
```

o path equivalente.

## Cosa deve contenere

Il prompt finale deve dire all’AI:

```md
# Regole generali

- Rispondi in modo da esame: completo ma conciso.
- Prima riconosci il pattern dell’esercizio.
- Usa la KB/RAG come fonte primaria.
- Non inventare metodi se la KB contiene una method card rilevante.
- Se manca una fonte, dichiaralo.
- Preferisci i PDF ufficiali del professore rispetto ad appunti o inferenze.
- Se la traccia è ambigua, esplicita l’interpretazione scelta.
- Per esercizi, dai:
  1. definizione sottoproblema/stato;
  2. casi base;
  3. ricorrenza/algoritmo;
  4. valore finale;
  5. complessità;
  6. eventuale ricostruzione se richiesta.
- Per teoria, dai:
  1. definizione;
  2. intuizione;
  3. schema di dimostrazione se utile;
  4. warning/errori comuni.
```

## Cosa NON deve contenere

Non deve contenere:
- tutte le ricorrenze complete;
- tutto il catalogo dei file;
- testi lunghi copiati dalla KB;
- dettagli specifici ridondanti già presenti nelle method card.

## Regole specifiche utili da mantenere

Includere solo regole rapide come:

```md
- LCS standard: valore `c_m,n`.
- Varianti LCS vincolate a terminare: spesso valore `max c_ij`.
- Floyd-Warshall: `k` sono i vertici intermedi ammessi; distinguere `E1` e `E2`.
- Cammini minimi: `d/min/+`.
- Esistenza: `e/OR/AND`.
- Knapsack 0/1: DP, non greedy.
- Greedy: richiede dimostrazione o struttura come matroide/arco sicuro.
- MST: non è shortest path.
- NP-completezza: mostrare `in NP` e riduzione da problema noto NP-completo.
- Non invertire la direzione della riduzione.
```

---

# Fase 8 — Controllo link e consistenza Markdown

## Obiettivo

La repo deve essere navigabile in Obsidian.

## Controlli

Eseguire:

```bash
grep -R "\[\[" -n 04_methods 05_theory 06_exam_patterns 07_solved_examples 10_rag
grep -R "](.*)" -n 04_methods 05_theory 06_exam_patterns 07_solved_examples 10_rag
```

Controllare:
- link rotti;
- path rinominati;
- riferimenti a file non creati;
- duplicazioni di titoli;
- sezioni vuote.

## Stile Markdown

Applicare:
- niente emoji;
- titoli chiari;
- tabelle solo se utili;
- formule leggibili;
- blocchi codice per pseudocodice/ricorrenze;
- callout Obsidian solo se migliorano la leggibilità.

---

# Fase 9 — Mini test RAG manuale

## Obiettivo

Simulare domande tipiche e verificare che il retrieval punti ai file giusti.

## Query test

Provare a cercare nella repo:

```text
LCS con due rossi consecutivi
LCS tre sequenze
LICS
Floyd-Warshall archi alternati
Floyd-Warshall esistenza archi rossi blu
Knapsack al massimo 3 rossi
Prim
Kruskal
Matroide grafico
P NP NP-completezza
3SAT Clique
Vertex Cover Independent Set
```

Per ogni query, verificare che:
- il retrieval index abbia una entry;
- la method card sia presente;
- il metodo/esempio sia linkato;
- non vengano recuperati file sbagliati come fonte primaria.

Scrivere l’esito in:

```text
09_ingestion_reports/final_repo_audit.md
```

---

# Fase 10 — Commit finale

## Prima del commit

Eseguire:

```bash
git status
git diff --stat
```

Controllare che non siano stati modificati:
- PDF originali;
- file raw sources;
- file temporanei;
- output non richiesti.

## Commit consigliato

```bash
git add README.md 04_methods 05_theory 06_exam_patterns 07_solved_examples 09_ingestion_reports 10_rag "AI Chat during Exam"
git commit -m "Finalize APA knowledge base and RAG structure"
```

Se ci sono molte modifiche non correlate, fare più commit:
1. methods/theory cleanup;
2. RAG/prompt update;
3. README/audit final.

---

# Checklist finale

- [ ] Repo controllata con `git status`.
- [ ] File duplicati individuati e risolti.
- [ ] README aggiornato.
- [ ] `04_methods/` completo e coerente.
- [ ] `05_theory/` compatto ma sufficiente.
- [ ] `07_solved_examples/` contiene schemi utili.
- [ ] `10_rag/RAG_RETRIEVAL_INDEX.md` aggiornato.
- [ ] `10_rag/RAG_PATTERN_MAP.md` aggiornato.
- [ ] `10_rag/RAG_EXAM_ANSWER_STYLE.md` aggiornato.
- [ ] Method card RAG non duplicate.
- [ ] Prompt finale aggiornato in modo generale.
- [ ] Trust policy coerente con fonti ufficiali.
- [ ] Link Markdown controllati.
- [ ] Mini test RAG manuale completato.
- [ ] Audit finale scritto.
- [ ] Commit effettuato.

---

# Criteri di completamento

Il lavoro è completo quando:

- la repo è navigabile da README;
- un nuovo modello può capire dove trovare teoria, metodi e pattern;
- il RAG recupera i file giusti per i principali argomenti;
- il prompt finale contiene regole operative generali e non un dump della KB;
- non ci sono duplicazioni pesanti;
- non ci sono contraddizioni evidenti tra file;
- gli esercizi principali hanno method card e schema;
- la teoria prioritaria è presente ma compatta;
- il file `09_ingestion_reports/final_repo_audit.md` documenta lo stato finale;
- il commit finale è stato creato.
