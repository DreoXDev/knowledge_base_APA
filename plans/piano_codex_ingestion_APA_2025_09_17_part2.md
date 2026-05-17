# Piano Codex — Ingestion appello APA 2025-09-17 Parte II

> [!Info]
> Piano operativo per aggiornare la repository `knowledge_base_APA` con il contenuto del PDF:
>
> `parteII-17set25.pdf`
>
> Appello: **Analisi e Progetto di Algoritmi — Parte II — 17 settembre 2025**

---

## Obiettivo

Integrare nella knowledge base Obsidian l'appello **Parte II del 17 settembre 2025**, mantenendo coerenza con gli altri appelli Parte II già analizzati.

Il PDF contiene 5 esercizi:

```txt
1. Kruskal / Minimum Spanning Tree;
2. riduzione 3-CNF-SAT / 3-SAT → CLIQUE;
3. algoritmo GREEDY-MAX e teorema di Rado;
4. criterio per stabilire che un problema A è NP-completo;
5. matroide grafico e dimostrazione che è un matroide.
```

> [!Summary]
> Questo appello conferma un pattern molto forte della Parte II:
>
> - esercizio pratico su MST/Kruskal;
> - esercizio pratico su riduzione 3-SAT → CLIQUE;
> - teoria su greedy e matroidi;
> - schema standard per NP-completezza;
> - dimostrazione del matroide grafico.

---

## 1. File da creare

Creare il report di ingestion:

```txt
09_ingestion_reports/ingestion_report_exam_2025_09_17_part2.md
```

Creare la trascrizione essenziale dell'appello:

```txt
02_transcriptions/exams/exam_2025_09_17_part2.md
```

Creare i file degli esercizi catalogati:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p2_e01.md
03_exercise_catalog/exercises/exam_2025_09_17_p2_e02.md
03_exercise_catalog/exercises/exam_2025_09_17_p2_e03.md
03_exercise_catalog/exercises/exam_2025_09_17_p2_e04.md
03_exercise_catalog/exercises/exam_2025_09_17_p2_e05.md
```

> [!Warning]
> Prima di creare i file, verificare se esistono già file con naming simile per evitare duplicazioni.

---

## 2. File da aggiornare

Aggiornare gli indici:

```txt
03_exercise_catalog/index_by_exam.md
03_exercise_catalog/index_by_topic.md
03_exercise_catalog/index_by_difficulty.md
```

Aggiornare i pattern:

```txt
06_exam_patterns/recurring_exercise_types.md
06_exam_patterns/variations_by_appeal.md
06_exam_patterns/high_yield_topics.md
```

Se presenti nella repo, aggiornare anche i pattern specifici della Parte II:

```txt
06_exam_patterns/parte_ii_patterns.md
06_exam_patterns/parte_ii_reductions_patterns.md
06_exam_patterns/parte_ii_greedy_mst_matroids_patterns.md
06_exam_patterns/parte_ii_np_completezza_patterns.md
```

Aggiornare o collegare i metodi rilevanti:

```txt
04_methods/metodo_kruskal_tracciamento_mst.md
04_methods/metodo_riduzione_3sat_clique.md
04_methods/metodo_greedy_max_sistemi_indipendenza.md
04_methods/metodo_teorema_rado.md
04_methods/metodo_dimostrare_np_completezza.md
04_methods/metodo_matroide_grafico.md
```

Aggiornare o collegare la teoria:

```txt
05_theory/kruskal.md
05_theory/minimum_spanning_tree.md
05_theory/greedy.md
05_theory/matroidi.md
05_theory/np_completezza.md
05_theory/riduzioni_polynomiali.md
05_theory/3sat_clique_independent_set.md
```

Aggiornare stato progetto e TODO:

```txt
PROJECT_STATUS.md
TODO.md
README.md
```

> [!Important]
> Se i metodi esistono già, non creare duplicati. Aggiornare le note esistenti e aggiungere link agli esercizi di questo appello.

---

## 3. Trascrizione essenziale dell'appello

Creare il file:

```txt
02_transcriptions/exams/exam_2025_09_17_part2.md
```

Contenuto consigliato:

```md
# Appello APA — Parte II — 17 settembre 2025

> [!Info]
> Fonte: `parteII-17set25.pdf`
>
> Appello di Analisi e Progetto di Algoritmi, Parte II, 17 settembre 2025.

## Struttura

| Esercizio | Valore | Tema |
|---|---:|---|
| 1 | 6 | Kruskal / Minimum Spanning Tree |
| 2 | 6 | Riduzione 3-CNF-SAT / 3-SAT → CLIQUE |
| 3 | 7 | GREEDY-MAX e teorema di Rado |
| 4 | 7 | Criterio per dimostrare NP-completezza |
| 5 | 7 | Matroide grafico |

## Esercizio 1

Dato un grafo non orientato, connesso e pesato $G=(V,E)$ con archi:

| Arco | Peso |
|---|---:|
| $(b,c)$ | 3 |
| $(b,d)$ | 1 |
| $(a,c)$ | 6 |
| $(a,b)$ | 6 |
| $(c,d)$ | 4 |
| $(d,e)$ | 5 |
| $(c,e)$ | 1 |
| $(a,e)$ | 10 |

Mostrare, nello schema con i quadrati $Q_1,\dots,Q_8$, l'ordine con cui Kruskal aggiunge gli archi del Minimum Spanning Tree.

## Esercizio 2

Data la formula:

$$
\varphi =
(x_1 \vee \neg x_2 \vee x_3)
\wedge
(\neg x_1 \vee x_2 \vee \neg x_3)
\wedge
(x_1 \vee \neg x_2 \vee x_3)
$$

disegnare il grafo ottenuto dalla riduzione polinomiale da 3-CNF-SAT a CLIQUE.

Il testo richiede di rappresentare:

- i vertici della prima clausola a sinistra;
- i vertici della seconda clausola in alto;
- i vertici della terza clausola a destra.

## Esercizio 3

Scrivere l'algoritmo GREEDY-MAX associato a un sistema di indipendenza $(E,\mathcal{F})$ e a una funzione peso $w:E \to \mathbb{R}^{+}$.

Enunciare il teorema di Rado. Non è richiesta la dimostrazione.

## Esercizio 4

Considerando un problema specifico $A$ tra quelli visti a lezione, indicare cosa è sufficiente mostrare per stabilire che $A$ è NP-completo.

Non è richiesta alcuna dimostrazione.

## Esercizio 5

Dato un grafo non orientato $G=(V,E)$, definire il matroide grafico e dimostrare che è effettivamente un matroide.

Il testo specifica che non occorre dimostrare che il numero di alberi in una foresta è pari alla differenza tra il numero di vertici e il numero di archi.
```

---

## 4. Esercizio 1 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p2_e01.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-09-17 Parte II — E01

> [!Info]
> Tema: Kruskal e costruzione progressiva del Minimum Spanning Tree.
>
> Fonte: `parteII-17set25.pdf`

## Richiesta

Dato un grafo non orientato, connesso e pesato $G=(V,E)$, mostrare l'ordine con cui l'algoritmo di Kruskal aggiunge gli archi del Minimum Spanning Tree.

Il testo richiede di compilare i quadrati:

```txt
Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8
```

dove $Q_i$ contiene i primi $i$ archi aggiunti o considerati secondo lo schema dell'esercizio, fino a mostrare l'MST costruito.

> [!Warning]
> Il testo dice che sono disponibili quadrati pari al numero di archi del grafo, ma l'MST finale ha solo $|V|-1$ archi. Seguire lo schema richiesto dal PDF e, se necessario, distinguere tra archi considerati e archi effettivamente aggiunti.
>
> Non inventare una soluzione grafica definitiva senza verifica.

## Dati del grafo

| Arco | Peso |
|---|---:|
| $(b,c)$ | 3 |
| $(b,d)$ | 1 |
| $(a,c)$ | 6 |
| $(a,b)$ | 6 |
| $(c,d)$ | 4 |
| $(d,e)$ | 5 |
| $(c,e)$ | 1 |
| $(a,e)$ | 10 |

## Tipo di esercizio

```txt
Algoritmi greedy
Kruskal
Minimum Spanning Tree
Tracciamento manuale
```

## Metodo collegato

Collegare a:

```md
[[metodo_kruskal_tracciamento_mst]]
```

oppure al metodo equivalente già presente nella repo.

## Note operative

Per risolvere:

1. ordinare gli archi per peso crescente;
2. inizializzare una foresta con tutti i vertici isolati;
3. considerare gli archi in ordine crescente;
4. aggiungere un arco solo se non crea ciclo;
5. fermarsi quando sono stati aggiunti $|V|-1$ archi all'MST.

> [!Important]
> In presenza di archi con lo stesso peso, possono esistere più ordini validi se il testo non specifica un tie-break. Segnalare eventuali ambiguità.
```

Pattern:

```txt
Parte II / Kruskal / MST / tracciamento progressivo
```

Difficoltà stimata:

```txt
media
```

Collegamenti:

```md
[[Kruskal]]
[[Minimum Spanning Tree]]
[[greedy]]
[[arco sicuro]]
```

---

## 5. Esercizio 2 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p2_e02.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-09-17 Parte II — E02

> [!Info]
> Tema: riduzione da 3-CNF-SAT a CLIQUE.
>
> Fonte: `parteII-17set25.pdf`

## Richiesta

Data la formula:

$$
\varphi =
(x_1 \vee \neg x_2 \vee x_3)
\wedge
(\neg x_1 \vee x_2 \vee \neg x_3)
\wedge
(x_1 \vee \neg x_2 \vee x_3)
$$

disegnare il grafo ottenuto dalla riduzione polinomiale da 3-CNF-SAT a CLIQUE.

## Tipo di esercizio

```txt
NP-completezza
Riduzioni polinomiali
3-SAT
CLIQUE
Costruzione del grafo
```

## Metodo collegato

Collegare a:

```md
[[metodo_riduzione_3sat_clique]]
```

oppure al metodo equivalente già presente nella repo.

## Regola della riduzione

Per una formula con $k$ clausole:

1. creare un vertice per ogni letterale di ogni clausola;
2. non collegare vertici appartenenti alla stessa clausola;
3. collegare vertici appartenenti a clausole diverse se i letterali non sono complementari;
4. una clique di dimensione $k$ corrisponde a una scelta consistente di un letterale per ogni clausola.

## Note specifiche

La formula contiene tre clausole:

```txt
C1 = (x1 ∨ ¬x2 ∨ x3)
C2 = (¬x1 ∨ x2 ∨ ¬x3)
C3 = (x1 ∨ ¬x2 ∨ x3)
```

Quindi il grafo ha:

```txt
3 clausole × 3 letterali = 9 vertici
```

e la clique cercata ha dimensione:

$$
k=3
$$

> [!Warning]
> La prima e la terza clausola sono uguali. Questo non significa che i vertici siano gli stessi: nella riduzione si crea comunque un gruppo separato di vertici per ogni occorrenza di clausola.
```

Pattern:

```txt
Parte II / Riduzione 3-SAT → CLIQUE / costruzione grafo
```

Difficoltà stimata:

```txt
media
```

Collegamenti:

```md
[[3-SAT]]
[[3-CNF-SAT]]
[[CLIQUE]]
[[riduzioni polinomiali]]
[[NP-completezza]]
```

---

## 6. Esercizio 3 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p2_e03.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-09-17 Parte II — E03

> [!Info]
> Tema: GREEDY-MAX e teorema di Rado.
>
> Fonte: `parteII-17set25.pdf`

## Richiesta

Scrivere l'algoritmo GREEDY-MAX associato a un sistema di indipendenza $(E,\mathcal{F})$ e a una funzione peso:

$$
w:E \to \mathbb{R}^{+}
$$

Enunciare inoltre il teorema di Rado.

Non è richiesta la dimostrazione.

## Tipo di esercizio

```txt
Greedy
Sistemi di indipendenza
Matroidi
Teorema di Rado
```

## Metodo collegato

Collegare a:

```md
[[metodo_greedy_max_sistemi_indipendenza]]
[[metodo_teorema_rado]]
```

oppure ai metodi equivalenti già presenti nella repo.

## Algoritmo atteso

Schema standard:

```txt
GREEDY-MAX(E, F, w)
    ordina gli elementi di E per peso non crescente
    S = ∅
    per ogni elemento e in E nell'ordine scelto:
        se S ∪ {e} ∈ F:
            S = S ∪ {e}
    restituisci S
```

## Teorema di Rado

Forma da enunciare:

```txt
Un sistema di indipendenza (E,F) è un matroide se e solo se,
per ogni funzione peso w non negativa, l'algoritmo GREEDY-MAX
restituisce una soluzione ottima del problema di massimo peso associato.
```

> [!Warning]
> Verificare nella teoria della repo la formulazione esatta usata a lezione, soprattutto il dominio della funzione peso e la variante max/min.
```

Pattern:

```txt
Parte II / GREEDY-MAX / Rado / matroidi
```

Difficoltà stimata:

```txt
media
```

Collegamenti:

```md
[[greedy]]
[[sistemi di indipendenza]]
[[matroidi]]
[[teorema di Rado]]
```

---

## 7. Esercizio 4 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p2_e04.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-09-17 Parte II — E04

> [!Info]
> Tema: criterio per dimostrare che un problema è NP-completo.
>
> Fonte: `parteII-17set25.pdf`

## Richiesta

Considerando un problema specifico $A$ tra quelli visti a lezione, dire cosa è sufficiente mostrare per stabilire che $A$ è NP-completo.

Non è richiesta alcuna dimostrazione.

## Tipo di esercizio

```txt
Teoria
NP-completezza
Riduzioni polinomiali
Schema di dimostrazione
```

## Metodo collegato

Collegare a:

```md
[[metodo_dimostrare_np_completezza]]
```

oppure al metodo equivalente già presente nella repo.

## Risposta attesa

Per stabilire che $A$ è NP-completo è sufficiente mostrare che:

1. $A \in NP$;
2. esiste un problema $B$ già noto NP-completo tale che:

$$
B \leq_p A
$$

cioè $B$ si riduce polinomialmente ad $A$.

Così si ottiene che $A$ è NP-hard e, insieme all'appartenenza a NP, si conclude che $A$ è NP-completo.

> [!Important]
> La direzione della riduzione è cruciale:
>
> bisogna ridurre un problema noto NP-completo al problema nuovo $A$.
```

Pattern:

```txt
Parte II / NP-completezza / schema dimostrativo
```

Difficoltà stimata:

```txt
facile
```

Collegamenti:

```md
[[P]]
[[NP]]
[[NP-completo]]
[[riduzioni polinomiali]]
```

---

## 8. Esercizio 5 — Catalogazione

File:

```txt
03_exercise_catalog/exercises/exam_2025_09_17_p2_e05.md
```

Contenuto consigliato:

```md
# Esercizio — Appello 2025-09-17 Parte II — E05

> [!Info]
> Tema: matroide grafico.
>
> Fonte: `parteII-17set25.pdf`

## Richiesta

Dato un grafo non orientato $G=(V,E)$:

1. definire il matroide grafico;
2. dimostrare che è effettivamente un matroide.

Il testo specifica che non occorre dimostrare che il numero di alberi in una foresta è pari alla differenza tra il numero di vertici e il numero di archi.

## Tipo di esercizio

```txt
Matroidi
Greedy
Grafi
Dimostrazione teorica
```

## Metodo collegato

Collegare a:

```md
[[metodo_matroide_grafico]]
```

oppure al metodo equivalente già presente nella repo.

## Definizione

Dato un grafo non orientato $G=(V,E)$, il matroide grafico è:

$$
M(G) = (E, \mathcal{F})
$$

dove:

$$
\mathcal{F} = \{ A \subseteq E \mid A \text{ non contiene cicli} \}
$$

cioè gli insiemi indipendenti sono gli insiemi di archi che formano foreste.

## Dimostrazione richiesta

Mostrare i tre assiomi:

1. $\emptyset \in \mathcal{F}$;
2. ereditarietà: se $A \in \mathcal{F}$ e $B \subseteq A$, allora $B \in \mathcal{F}$;
3. scambio: se $A,B \in \mathcal{F}$ e $|A|<|B|$, allora esiste $e \in B \setminus A$ tale che $A \cup \{e\} \in \mathcal{F}$.

> [!Important]
> Questa domanda compare in più appelli Parte II. Deve puntare a un metodo centrale unico, non a dimostrazioni duplicate.
```

Pattern:

```txt
Parte II / Matroide grafico / dimostrazione assiomi
```

Difficoltà stimata:

```txt
alta
```

Collegamenti:

```md
[[matroidi]]
[[matroide grafico]]
[[foreste]]
[[greedy]]
```

---

## 9. Pattern da aggiornare

Aggiornare i pattern ricorrenti della Parte II.

### Pattern confermati

```txt
- Kruskal con costruzione progressiva del MST.
- Riduzione 3-SAT → CLIQUE con grafo a gruppi di clausole.
- GREEDY-MAX su sistemi di indipendenza.
- Teorema di Rado.
- Schema per dimostrare NP-completezza.
- Matroide grafico e dimostrazione degli assiomi.
```

### Riga consigliata per tabella appelli Parte II

```md
| 2025-09-17 Parte II | Kruskal, 3-SAT→CLIQUE, GREEDY-MAX/Rado, NP-completezza, matroide grafico | Conferma pattern MST + riduzioni + matroidi |
```

### Pattern high-yield da rafforzare

```txt
1. Riduzioni 3-SAT → CLIQUE / Independent Set.
2. CLIQUE → Vertex Cover.
3. Schema NP-completezza.
4. Kruskal e arco sicuro.
5. Dijkstra con rilassamenti.
6. Matroidi, Rado e GREEDY-MAX.
7. Matroide grafico.
```

---

## 10. Differenze rispetto agli appelli Parte II già analizzati

Somiglianze:

```txt
- come 2025-11-10 e 2025-02-11, contiene Kruskal/MST;
- come 2025-11-10 e 2025-01-13, contiene riduzione 3-SAT → CLIQUE;
- come 2025-06-09, contiene GREEDY-MAX e teorema di Rado;
- come 2025-06-09, 2025-11-10 e 2025-01-13, contiene lo schema per NP-completezza;
- come 2025-06-09, 2025-11-10 e 2025-01-13, contiene matroide grafico.
```

Differenze:

```txt
- il grafo di Kruskal ha 8 archi invece dei 7 archi visti in altri appelli simili;
- la formula 3-SAT contiene clausole ripetute, quindi va chiarito che le occorrenze generano vertici distinti;
- non ci sono domande bonus esplicite;
- non compare la chiusura transitiva, presente invece in altri appelli Parte II.
```

> [!Summary]
> Questo appello è utile soprattutto per consolidare i blocchi Parte II più ricorrenti:
> Kruskal, riduzioni, Rado, NP-completezza e matroide grafico.

---

## 11. Note metodologiche importanti

### Kruskal

Non inserire una soluzione finale non verificata se non è stata controllata.

Si può però indicare il metodo standard e, se utile, ordinare gli archi per peso:

```txt
peso 1: (b,d), (c,e)
peso 3: (b,c)
peso 4: (c,d)
peso 5: (d,e)
peso 6: (a,c), (a,b)
peso 10: (a,e)
```

> [!Warning]
> Ci sono due archi di peso 1 e due archi di peso 6. Se l'esercizio non specifica un tie-break, più esecuzioni di Kruskal possono essere equivalenti.

### Riduzione 3-SAT → CLIQUE

Evidenziare che:

```txt
C1 = C3
```

ma nella riduzione:

```txt
le occorrenze di letterali in clausole diverse generano vertici distinti.
```

### GREEDY-MAX / Rado

Verificare che la formulazione della repo sia coerente con il corso:

```txt
w : E → R+
```

Nel PDF il simbolo viene letto come `R+`.

### Matroide grafico

Deduplicare con gli altri appelli: creare un'unica nota di metodo robusta e linkarla da tutti gli esercizi.

---

## 12. Aggiornare PROJECT_STATUS.md

Aggiungere o aggiornare la sezione Parte II:

```md
## Appelli Parte II

- [x] 2025-09-17 Parte II — report creato / da applicare
```

Se i precedenti report Parte II sono già stati applicati, mantenere la cronologia coerente.

Aggiungere nota di stato:

```md
> [!Summary]
> La Parte II mostra ormai pattern ricorrenti molto stabili:
> Kruskal/Dijkstra, riduzioni NP-complete, GREEDY-MAX/Rado, matroide grafico e schema di NP-completezza.
```

---

## 13. Aggiornare TODO.md

Aggiungere:

```md
# TODO — Appello 2025-09-17 Parte II

- [ ] Creare ingestion report `ingestion_report_exam_2025_09_17_part2.md`.
- [ ] Creare trascrizione `exam_2025_09_17_part2.md`.
- [ ] Creare esercizi E01-E05 nel catalogo.
- [ ] Collegare Kruskal al metodo già esistente.
- [ ] Collegare 3-SAT→CLIQUE al metodo già esistente.
- [ ] Collegare GREEDY-MAX e Rado ai metodi già esistenti.
- [ ] Collegare NP-completezza allo schema standard.
- [ ] Collegare matroide grafico al metodo centrale.
- [ ] Aggiornare indici per appello, topic e difficoltà.
- [ ] Aggiornare pattern Parte II.
- [ ] Verificare deduplicazione con gli appelli Parte II già analizzati.
```

---

## 14. Commit consigliato

Commit consigliato:

```txt
ingest APA 2025-09-17 part2 exam
```

Descrizione:

```txt
- add transcription for 2025-09-17 Parte II
- catalog Kruskal, 3-SAT to CLIQUE, GREEDY-MAX/Rado, NP-completeness, graphic matroid exercises
- update Parte II patterns and indices
```

---

## 15. Stato atteso finale

Dopo l'applicazione del piano:

```txt
- il PDF 2025-09-17 Parte II è rappresentato nella KB;
- tutti i 5 esercizi sono catalogati;
- gli esercizi sono collegati ai metodi corretti;
- i pattern Parte II sono aggiornati;
- le ripetizioni con appelli precedenti sono deduplicate;
- PROJECT_STATUS.md e TODO.md sono coerenti con il nuovo stato.
```

---

## 16. Nota finale per Codex

> [!Important]
> Questo appello non deve generare metodi duplicati.
>
> I contenuti su Kruskal, 3-SAT→CLIQUE, GREEDY-MAX/Rado, NP-completezza e matroide grafico devono collegarsi ai metodi centrali della KB.
>
> Se una soluzione grafica completa non è verificata, limitarsi a catalogazione, metodo e note operative.
