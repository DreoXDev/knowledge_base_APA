# Piano Codex — Aggiornamento teoria APA da PDF prioritari

## Scopo

Aggiornare la parte teorica della Knowledge Base/RAG APA usando i file di priorità alta presenti in `01_sources/notes_raw`.

Questa fase viene dopo l’analisi dettagliata degli esercizi ufficiali. Quindi l’obiettivo non è creare riassunti enormi, ma completare la KB con teoria essenziale, definizioni, teoremi, proof sketch e collegamenti utili agli esercizi.

Repo:

```text
https://github.com/DreoXDev/knowledge_base_APA
```

## PDF analizzati

### Blocco Knapsack / DP

- `Knapsack-29-ottobre-2025.pdf`

Contenuto principale:
- problema dello zaino;
- oggetti `e_i`;
- valore `v_i`;
- peso `w_i`;
- capacità `W`;
- confronto tra obiettivo di massimizzazione del valore e vincolo di capacità;
- fallimento del greedy sullo zaino 0/1;
- impostazione DP con matrice;
- coefficiente `V[i,p]`;
- ricorrenza include/esclude;
- valore ottimo in `V[n,W]`.

### Blocco Greedy / Matroidi / Kruskal

- `lezione-greedy19-11-25.pdf`
- `lezione-greedy19-11-25-2.pdf`
- `Kruskal-26-11-25.pdf`
- `Kruskal-parte2.pdf`

Contenuto principale:
- quando si applica greedy;
- differenza tra programmazione dinamica e greedy;
- esempi di applicazioni greedy;
- change-making;
- knapsack frazionario vs knapsack 0/1;
- sistemi di indipendenza;
- matroidi;
- proprietà ereditaria;
- proprietà di scambio;
- algoritmo greedy su matroidi;
- dimostrazione che greedy è corretto su matroidi;
- matroide grafico;
- collegamento con Kruskal;
- union-find / `make-set`, `find-set`, `union`;
- Kruskal come greedy su matroide grafico.

### Blocco P, NP, NP-completezza e riduzioni

- `P-NP-10-12-25.pdf`
- `P-NP-10-12-25parte2a.pdf`
- `Riduzioni.pdf`
- `Riduzioni2-1.pdf`
- `Riduzioni2-2.pdf`

Contenuto principale:
- problemi di decisione;
- classi `P` e `NP`;
- certificati e verificatori polinomiali;
- cammino/ciclo Hamiltoniano;
- Clique;
- SAT e 3SAT;
- teorema di Cook;
- definizione di NP-completezza;
- riduzioni polinomiali;
- riduzione `3SAT <=p CLIQUE`;
- relazione tra Vertex Cover, Clique e Independent Set tramite grafo complemento;
- dimostrazioni di appartenenza a NP;
- struttura standard per dimostrare che un problema è NP-completo.

---

## Ruolo nella KB

Questi file servono a completare tre blocchi teorici molto importanti:

1. **Programmazione dinamica**
   - zaino base;
   - collegamento con variante già analizzata “zaino con al massimo 3 oggetti rossi”;
   - distinzione tra zaino 0/1 e zaino frazionario.

2. **Greedy**
   - teoria generale;
   - matroidi;
   - correttezza di greedy su matroidi;
   - Kruskal come applicazione al matroide grafico;
   - collegamento con MST/Prim già analizzati.

3. **Complessità e NP-completezza**
   - P/NP;
   - riduzioni;
   - problemi classici;
   - metodo standard di dimostrazione NP-completezza;
   - collegamenti tra Clique, Vertex Cover, Independent Set, SAT/3SAT.

Questa fase deve aumentare la qualità della KB per rispondere a domande teoriche e per giustificare correttamente gli esercizi, senza trasformare la repo in un manuale troppo lungo.

---

# Strategia generale

## Cosa deve fare Codex

Codex deve:

1. Cercare nella repo i file teorici già presenti.
2. Integrare la teoria nei file esistenti se sono già coerenti.
3. Creare nuovi file solo quando manca una pagina chiara.
4. Aggiornare il RAG solo per concetti importanti.
5. Aggiungere warning dove c’è rischio di confusione.
6. Collegare teoria e metodi esercizi già presenti.
7. Evitare duplicazioni con i master plan sugli esercizi.

## Cosa NON deve fare Codex

Codex non deve:

- trascrivere integralmente i PDF;
- fare OCR massivo non necessario;
- creare una pagina per ogni singola slide;
- duplicare le stesse definizioni in più file;
- modificare metodi esercizi già validati se i PDF non li contraddicono;
- aggiungere teoria generale esterna non presente o non necessaria;
- rendere il prompt da esame troppo lungo.

---

# File principali da creare o aggiornare

## Cartella teoria

Creare o aggiornare:

```text
05_theory/dp_knapsack_base.md
05_theory/greedy_teoria_base.md
05_theory/matroidi_e_greedy.md
05_theory/kruskal_matroide_grafico.md
05_theory/p_np_np_completezza.md
05_theory/riduzioni_np_completezza.md
```

Se alcuni file equivalenti esistono già, usare quelli e non duplicare.

## Cartella metodi

Aggiornare solo se serve:

```text
04_methods/dp_knapsack_vincoli_colore.md
04_methods/mst_greedy_base.md
04_methods/mst_kruskal.md
04_methods/mst_prim.md
```

Creare se manca:

```text
04_methods/dp_knapsack_base.md
04_methods/np_completezza_schema_dimostrazione.md
```

## Esempi / schemi

Creare o aggiornare:

```text
07_solved_examples/knapsack_base_schema.md
07_solved_examples/kruskal_schema_esecuzione.md
07_solved_examples/np_completezza_schema.md
07_solved_examples/riduzione_3sat_clique_schema.md
07_solved_examples/riduzioni_vertex_cover_clique_independent_set.md
```

## RAG

Creare o aggiornare:

```text
10_rag/RAG_METHOD_CARDS/dp_knapsack.md
10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md
10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md
```

Aggiornare:

```text
10_rag/RAG_RETRIEVAL_INDEX.md
10_rag/RAG_PATTERN_MAP.md
10_rag/RAG_EXAM_ANSWER_STYLE.md
AI Chat during Exam/Final Prompt.md
AI Chat during Exam/prompt_sections/
```

---

# Parte 1 — Knapsack base e collegamento con DP

## File di riferimento

```text
Knapsack-29-ottobre-2025.pdf
```

## Concetti da integrare

Il PDF imposta il problema dello zaino con:
- insieme di elementi/oggetti;
- valore `v_i`;
- peso `w_i`;
- capacità `W`;
- obiettivo di massimizzare il valore totale rispettando il vincolo di capacità.

Va chiarita la differenza tra:
- **zaino 0/1**, dove ogni oggetto viene preso o non preso;
- **zaino frazionario**, dove si possono prendere frazioni e il greedy può funzionare;
- varianti con vincoli extra, come “al massimo 3 oggetti rossi”, già analizzata nei PDF esercizi.

## File da creare o aggiornare

### `05_theory/dp_knapsack_base.md`

Contenuto consigliato:

```md
# Knapsack 0/1 — teoria base

## Problema

Input:
- oggetti `e_1, ..., e_n`;
- valore `v_i` per ogni oggetto;
- peso `w_i` per ogni oggetto;
- capacità `W`.

Output:
un sottoinsieme `S` di oggetti tale che:

```text
Σ_{e_i ∈ S} w_i <= W
```

e che massimizza:

```text
Σ_{e_i ∈ S} v_i
```

## Stato DP

`V[i,p]` rappresenta il massimo valore ottenibile usando solo i primi `i` oggetti e capacità massima `p`.

## Casi base

```text
V[0,p] = 0
V[i,0] = 0
```

## Ricorrenza

Se `w_i > p`:

```text
V[i,p] = V[i-1,p]
```

Se `w_i <= p`:

```text
V[i,p] = max(
  V[i-1,p],
  V[i-1,p-w_i] + v_i
)
```

## Valore ottimo

```text
V[n,W]
```

## Warning

Lo zaino 0/1 non si risolve in generale con greedy.
Il greedy funziona invece nello zaino frazionario, dove è possibile prendere frazioni di oggetto.
```

### `04_methods/dp_knapsack_base.md`

Creare se manca. Deve essere più operativo del file teorico:

```md
# Metodo — Knapsack 0/1

## Schema da esame

1. Definire lo stato `V[i,p]`.
2. Scrivere casi base.
3. Separare il caso `w_i > p`.
4. Se `w_i <= p`, confrontare:
   - non prendo `i`;
   - prendo `i`.
5. Restituire `V[n,W]`.
6. Per ricostruire, risalire confrontando `V[i,p]` e `V[i-1,p]`.
```

### Aggiornare `04_methods/dp_knapsack_vincoli_colore.md`

Collegare la variante “al massimo 3 oggetti rossi” allo zaino base:

```md
Questa variante estende lo stato base `V[i,p]` aggiungendo una dimensione `r`, che rappresenta il budget massimo di oggetti rossi ancora utilizzabile o ammesso.
```

## Warning da inserire nel RAG

```md
Non confondere:
- zaino 0/1: scelta sì/no per ogni oggetto;
- zaino frazionario: si possono prendere frazioni;
- zaino con vincoli extra: aggiunge dimensioni allo stato DP.
```

```md
Nel knapsack base il valore ottimo è `V[n,W]`.
Nella variante con al massimo 3 rossi il valore ottimo è `d_{n,C,3}`.
```

---

# Parte 2 — Greedy, matroidi e Kruskal

## File di riferimento

```text
lezione-greedy19-11-25.pdf
lezione-greedy19-11-25-2.pdf
Kruskal-26-11-25.pdf
Kruskal-parte2.pdf
```

## Concetti da integrare

Questi PDF vanno trattati come un unico blocco teorico:

1. Greedy come tecnica per problemi di ottimizzazione.
2. Differenza tra DP e greedy.
3. Necessità di dimostrazione formale della correttezza greedy.
4. Sistema di indipendenza.
5. Matroide.
6. Proprietà ereditaria.
7. Proprietà di scambio.
8. Teorema: greedy è corretto su matroidi pesati.
9. Matroide grafico.
10. Kruskal come greedy su matroide grafico.
11. Union-Find per implementare Kruskal.

## File da creare o aggiornare

### `05_theory/greedy_teoria_base.md`

Contenuto consigliato:

```md
# Greedy — teoria base

## Idea

Un algoritmo greedy costruisce la soluzione per aggiunta, facendo ogni volta una scelta localmente ottima.

## Quando si applica

Si applica a problemi di ottimizzazione, ma non basta riconoscere un problema di ottimizzazione: serve dimostrare che la scelta locale produce una soluzione globale ottima.

## Differenza con programmazione dinamica

| Aspetto | Programmazione dinamica | Greedy |
|---|---|---|
| Costruzione | risolve sottoproblemi e combina risultati | costruisce per aggiunta |
| Scelte | considera molte possibilità | fa una scelta locale |
| Correttezza | ricorrenza e sottostruttura ottima | richiede dimostrazione della scelta greedy |
| Tipico vantaggio | evita ricalcoli | spesso riduce tempo/spazio rispetto a DP |

## Esempi

- MST;
- cammini minimi;
- scheduling;
- change-making;
- knapsack frazionario.

## Warning

Il greedy non funziona automaticamente.
Esempio classico: knapsack 0/1.
```

### `05_theory/matroidi_e_greedy.md`

Contenuto consigliato:

```md
# Matroidi e correttezza del greedy

## Sistema di indipendenza

Un sistema di indipendenza è una coppia:

```text
<E, F>
```

dove:
- `E` è l'insieme degli elementi;
- `F` è una famiglia di sottoinsiemi di `E`, detti indipendenti.

Proprietà ereditaria:

```text
A ∈ F and B ⊆ A => B ∈ F
```

## Matroide

Un matroide è un sistema `<E,F>` che soddisfa:

1. proprietà ereditaria;
2. proprietà di scambio.

## Proprietà di scambio

Per ogni `A,B ∈ F`, se:

```text
|B| > |A|
```

allora esiste:

```text
b ∈ B \ A
```

tale che:

```text
A ∪ {b} ∈ F
```

## Conseguenza importante

Tutti gli insiemi massimali di un matroide hanno la stessa cardinalità.

## Greedy su matroidi

Dato:
- matroide `<E,F>`;
- peso `w : E -> R+`.

L'algoritmo greedy ordina gli elementi per peso decrescente e aggiunge un elemento se mantiene l'indipendenza.

## Teorema

Se `<E,F>` è un matroide, allora greedy restituisce una soluzione ottima.

## Proof sketch

1. Sia `S` la soluzione prodotta da greedy.
2. Sia `A` una soluzione ottima.
3. Usare la proprietà di scambio per confrontare progressivamente gli elementi scelti da greedy e quelli di `A`.
4. Poiché greedy considera gli elementi in ordine di peso, ogni scambio non peggiora il peso totale.
5. Quindi `w(S) = w(A)` e `S` è ottima.
```

### `05_theory/kruskal_matroide_grafico.md`

Contenuto consigliato:

```md
# Kruskal e matroide grafico

## Matroide grafico

Dato un grafo non orientato:

```text
G = (V,E)
```

si definisce:

```text
F = { A ⊆ E | (V,A) è una foresta }
```

La coppia:

```text
<E,F>
```

è un matroide grafico.

## Proprietà ereditaria

Se `A` è una foresta, ogni sottoinsieme `B ⊆ A` è ancora una foresta.

## Proprietà di scambio

Se `A` e `B` sono foreste e `|B| > |A|`, allora esiste un arco:

```text
b ∈ B \ A
```

tale che:

```text
A ∪ {b}
```

è ancora una foresta.

## Collegamento con MST

Kruskal applica greedy al matroide grafico:
- considera gli archi in ordine di peso crescente;
- aggiunge un arco se non crea cicli;
- alla fine ottiene un MST.

## Implementazione con Union-Find

Per ogni vertice:

```text
Make-Set(v)
```

Per ogni arco `(u,v)` in ordine crescente:

```text
if Find-Set(u) != Find-Set(v):
    aggiungi (u,v)
    Union(u,v)
```

## Warning

Kruskal è greedy su archi.
Prim è greedy su vertici/componenti.
Entrambi calcolano MST, ma mantengono strutture diverse.
```

### `04_methods/mst_kruskal.md`

Creare o aggiornare con schema operativo:

```md
# Metodo — Kruskal

## Input

Grafo non orientato, connesso e pesato.

## Procedura

1. Ordinare gli archi per peso crescente.
2. Inizializzare `A = ∅`.
3. Creare un insieme disgiunto per ogni vertice.
4. Scorrere gli archi in ordine:
   - se gli estremi sono in componenti diverse, aggiungere l'arco;
   - unire le componenti.
5. Fermarsi quando `|A| = |V|-1`.

## Output

`(V,A)` è un MST.

## Correttezza

La correttezza segue:
- dal teorema dell'arco sicuro;
- oppure dalla correttezza del greedy su matroide grafico.
```

## Warning da inserire nel RAG

```md
Greedy richiede dimostrazione.
Non basta dire "scelgo localmente il migliore".
```

```md
Kruskal usa ordinamento crescente degli archi per MST minimo.
La forma generale del greedy su matroidi può essere presentata come massimizzazione con pesi decrescenti: per MST minimo si adatta usando pesi crescenti o pesi trasformati.
```

```md
Nel matroide grafico gli insiemi indipendenti sono sottoinsiemi di archi che non formano cicli, cioè foreste.
```

---

# Parte 3 — P, NP, NP-completezza e riduzioni

## File di riferimento

```text
P-NP-10-12-25.pdf
P-NP-10-12-25parte2a.pdf
Riduzioni.pdf
Riduzioni2-1.pdf
Riduzioni2-2.pdf
```

## Concetti da integrare

Questo blocco va trattato come teoria d’esame compatta ma precisa.

Temi da coprire:

1. Problemi di decisione.
2. Classe `P`.
3. Classe `NP`.
4. Certificati.
5. Verificatori polinomiali.
6. Problemi in `NP` non noti in `P`.
7. Problema SAT.
8. Teorema di Cook.
9. Definizione di riduzione polinomiale.
10. Definizione di NP-completezza.
11. Schema per dimostrare che un problema è NP-completo.
12. Esempi:
    - Hamiltonian Path/Cycle in NP;
    - Clique in NP;
    - SAT/3SAT;
    - `3SAT <=p CLIQUE`;
    - relazioni tra Vertex Cover, Clique e Independent Set.

## File da creare o aggiornare

### `05_theory/p_np_np_completezza.md`

Contenuto consigliato:

```md
# P, NP e NP-completezza

## Problemi di decisione

Un problema di decisione ha output:

```text
YES / NO
```

Le classi `P` e `NP` si definiscono su problemi di decisione.

## Classe P

`P` è la classe dei problemi di decisione risolvibili in tempo polinomiale.

## Classe NP

`NP` è la classe dei problemi di decisione per cui una risposta `YES` ha un certificato verificabile in tempo polinomiale.

## Certificato

Un certificato è una informazione aggiuntiva che permette a un verificatore di controllare in tempo polinomiale che la risposta sia `YES`.

## Verificatore polinomiale

Un algoritmo `A(x,y)` è un verificatore polinomiale se:
- prende in input l'istanza `x` e il certificato `y`;
- verifica la correttezza del certificato;
- lavora in tempo polinomiale nella dimensione dell'input.

## Relazione tra P e NP

```text
P ⊆ NP
```

Non è noto se:

```text
P = NP
```

## SAT

SAT è il problema di soddisfacibilità di una formula booleana.

SAT appartiene a `NP` perché, data un'assegnazione delle variabili, si può verificare in tempo polinomiale se la formula è soddisfatta.

## Teorema di Cook

SAT è NP-completo.

Significato:
ogni problema in `NP` si riduce polinomialmente a SAT.
```

### `05_theory/riduzioni_np_completezza.md`

Contenuto consigliato:

```md
# Riduzioni polinomiali e NP-completezza

## Riduzione polinomiale

Una riduzione polinomiale da un problema `A` a un problema `B` è una funzione:

```text
f
```

calcolabile in tempo polinomiale tale che:

```text
x ∈ A  sse  f(x) ∈ B
```

Si scrive:

```text
A <=p B
```

Interpretazione:
se so risolvere `B`, allora posso risolvere `A` trasformando le istanze di `A` in istanze di `B`.

## Come usare le riduzioni per NP-completezza

Per dimostrare che un problema `B` è NP-completo:

1. Dimostrare che `B ∈ NP`.
2. Prendere un problema `A` già noto NP-completo.
3. Costruire una riduzione polinomiale:

```text
A <=p B
```

4. Dimostrare la doppia implicazione:

```text
x risponde YES per A  sse  f(x) risponde YES per B
```

## Warning

La direzione della riduzione è fondamentale.

Per dimostrare che `B` è NP-completo, bisogna ridurre un problema noto NP-completo `A` a `B`, non il contrario.
```

### `04_methods/np_completezza_schema_dimostrazione.md`

Contenuto operativo:

```md
# Metodo — Dimostrare che un problema è NP-completo

## Schema

Per dimostrare che un problema `Π` è NP-completo:

1. Dimostrare `Π ∈ NP`.
   - definire un certificato;
   - descrivere un verificatore polinomiale.

2. Scegliere un problema `Π'` noto NP-completo.

3. Costruire una funzione di trasformazione:

```text
f : istanze di Π' -> istanze di Π
```

4. Dimostrare che `f` è calcolabile in tempo polinomiale.

5. Dimostrare la correttezza della riduzione:

```text
istanza x di Π' è YES
sse
istanza f(x) di Π è YES
```

6. Concludere che `Π` è NP-completo.
```

## Esempi specifici da integrare

### Hamiltonian Cycle / Path in NP

Aggiungere in `05_theory/p_np_np_completezza.md` o in `07_solved_examples/np_appartenenza_np_schema.md`:

```md
## Esempio — Ciclo Hamiltoniano è in NP

Certificato:
una sequenza di vertici.

Verificatore:
- controlla che ogni arco consecutivo esista;
- controlla che ogni vertice compaia una sola volta;
- controlla che il ciclo torni al vertice iniziale;
- lavora in tempo polinomiale.
```

### Clique in NP

```md
## Esempio — Clique è in NP

Input:
- grafo `G=(V,E)`;
- intero `k`.

Certificato:
un insieme di `k` vertici.

Verificatore:
- controlla che l'insieme abbia cardinalità `k`;
- controlla tutte le coppie di vertici;
- verifica che ogni coppia sia collegata da un arco;
- tempo `O(k^2)` più accesso alla struttura del grafo.
```

### Riduzione `3SAT <=p CLIQUE`

Creare:

```text
07_solved_examples/riduzione_3sat_clique_schema.md
```

Contenuto:

```md
# Schema — Riduzione 3SAT <=p CLIQUE

## Obiettivo

Dimostrare che `CLIQUE` è NP-completo.

## Passi

1. `CLIQUE ∈ NP`.
2. `3SAT` è noto NP-completo.
3. Costruire una riduzione polinomiale:

```text
3SAT <=p CLIQUE
```

## Costruzione

Data una formula 3SAT con `k` clausole:
- creare un vertice per ogni letterale di ogni clausola;
- collegare vertici appartenenti a clausole diverse;
- non collegare letterali contraddittori, come `x` e `¬x`;
- impostare il parametro della clique a `k`.

## Correttezza

La formula è soddisfacibile se e solo se il grafo costruito contiene una clique di dimensione `k`.

## Intuizione

Una clique di dimensione `k` sceglie un letterale compatibile da ciascuna clausola.
```

### Vertex Cover, Clique, Independent Set

Creare:

```text
07_solved_examples/riduzioni_vertex_cover_clique_independent_set.md
```

Contenuto:

```md
# Relazioni tra Vertex Cover, Clique e Independent Set

## Grafo complemento

Dato un grafo:

```text
G = (V,E)
```

il complemento è:

```text
Gbar = (V, Ebar)
```

dove:

```text
(u,v) ∈ Ebar  sse  (u,v) ∉ E
```

per `u != v`.

## Vertex Cover e Independent Set

`S` è un vertex cover di `G` se e solo se `V \ S` è un independent set di `G`.

Quindi:

```text
G ha vertex cover di dimensione k
sse
G ha independent set di dimensione |V|-k
```

## Independent Set e Clique

`S` è un independent set in `G` se e solo se `S` è una clique nel complemento `Gbar`.

Quindi:

```text
G ha independent set di dimensione k
sse
Gbar ha clique di dimensione k
```

## Vertex Cover e Clique

Combinando le due relazioni:

```text
G ha vertex cover di dimensione k
sse
Gbar ha clique di dimensione |V|-k
```
```

## Warning da inserire nel RAG

```md
NP non significa "non polinomiale".
NP significa verificabile in tempo polinomiale tramite certificato.
```

```md
Per dimostrare NP-completezza, la direzione della riduzione è:
problema noto NP-completo <=p problema da dimostrare NP-completo.
```

```md
Una riduzione `A <=p B` significa: se so risolvere `B`, allora posso risolvere `A`.
```

```md
Clique e Vertex Cover spesso si collegano tramite il grafo complemento e il parametro cambia da `k` a `|V|-k`.
```

---

# Aggiornamenti RAG

## `10_rag/RAG_METHOD_CARDS/dp_knapsack.md`

Creare o aggiornare:

```md
# Method card — Knapsack

## Trigger

- "zaino"
- "knapsack"
- "capacità"
- "valore"
- "peso"
- "oggetti"
- "al massimo 3 rossi"
- "0/1"

## Decisione rapida

- Knapsack 0/1 base: stato `V[i,p]`.
- Variante con colore: aggiungere stato extra `r`.
- Se è "al massimo", `r` è budget massimo.
- Se è "esattamente", bisogna cambiare semantica/casi base.
- Greedy non funziona in generale per 0/1.
- Greedy funziona per knapsack frazionario.
```

## `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md`

Creare o aggiornare:

```md
# Method card — Greedy, matroidi, Kruskal

## Trigger

- "greedy"
- "ingordo"
- "matroide"
- "sistema di indipendenza"
- "proprietà di scambio"
- "Kruskal"
- "MST"
- "foresta"
- "Union-Find"

## Decisione rapida

- Greedy richiede dimostrazione.
- Se il sistema è un matroide, greedy è corretto.
- Nel matroide grafico gli indipendenti sono foreste.
- Kruskal è greedy sul matroide grafico.
- Kruskal aggiunge archi crescenti se non creano cicli.
```

## `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md`

Creare:

```md
# Method card — P, NP, NP-completezza e riduzioni

## Trigger

- "P"
- "NP"
- "NP-completo"
- "riduzione polinomiale"
- "SAT"
- "3SAT"
- "CLIQUE"
- "Vertex Cover"
- "Independent Set"
- "Hamiltoniano"

## Decisione rapida

Per dimostrare NP-completezza:
1. mostrare appartenenza a NP;
2. scegliere un problema noto NP-completo;
3. ridurlo al problema target;
4. dimostrare doppia implicazione;
5. concludere.

Warning:
la direzione della riduzione è la parte più importante.
```

---

# Aggiornamenti `10_rag/RAG_RETRIEVAL_INDEX.md`

Aggiungere entry:

```md
| Knapsack base | zaino, knapsack, capacità, peso, valore, V[i,p], programmazione dinamica, 0/1 | `05_theory/dp_knapsack_base.md`, `04_methods/dp_knapsack_base.md`, `10_rag/RAG_METHOD_CARDS/dp_knapsack.md` |
| Knapsack con vincoli colore | zaino al massimo 3 rossi, oggetti rossi, d_i_c_r, budget rossi | `04_methods/dp_knapsack_vincoli_colore.md`, `10_rag/RAG_METHOD_CARDS/dp_knapsack.md` |
| Greedy teoria | greedy, algoritmo ingordo, scelta locale, greedy choice, knapsack frazionario, change-making | `05_theory/greedy_teoria_base.md`, `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md` |
| Matroidi | matroide, sistema di indipendenza, proprietà ereditaria, proprietà di scambio, greedy corretto | `05_theory/matroidi_e_greedy.md`, `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md` |
| Kruskal e matroide grafico | Kruskal, MST, matroide grafico, foresta, union-find, find-set, union | `05_theory/kruskal_matroide_grafico.md`, `04_methods/mst_kruskal.md`, `10_rag/RAG_METHOD_CARDS/greedy_matroidi_mst.md` |
| P NP NP-completezza | P, NP, certificato, verificatore, SAT, Cook, NP-completo | `05_theory/p_np_np_completezza.md`, `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md` |
| Riduzioni polinomiali | riduzione polinomiale, <=p, 3SAT Clique, Vertex Cover, Independent Set, complemento | `05_theory/riduzioni_np_completezza.md`, `04_methods/np_completezza_schema_dimostrazione.md`, `10_rag/RAG_METHOD_CARDS/np_completezza_riduzioni.md` |
```

---

# Aggiornamenti `10_rag/RAG_PATTERN_MAP.md`

Aggiungere pattern:

```md
### Pattern: Knapsack 0/1

Trigger:
- "zaino"
- "capacità"
- "peso"
- "valore"
- "sottoinsieme di oggetti"

Metodo:
- stato `V[i,p]`;
- include/esclude oggetto;
- valore finale `V[n,W]`;
- per vincoli extra aggiungere dimensione allo stato.
```

```md
### Pattern: Greedy / Matroide

Trigger:
- "greedy"
- "matroide"
- "proprietà di scambio"
- "sistema di indipendenza"

Metodo:
- definire `<E,F>`;
- verificare ereditarietà;
- verificare scambio;
- se è matroide, greedy è corretto.
```

```md
### Pattern: Kruskal

Trigger:
- "Kruskal"
- "MST"
- "arco minimo"
- "ciclo"
- "foresta"

Metodo:
- ordinare archi crescenti;
- aggiungere arco se non crea ciclo;
- usare union-find;
- output con `|V|-1` archi.
```

```md
### Pattern: Dimostrazione NP-completezza

Trigger:
- "dimostrare che è NP-completo"
- "riduzione"
- "SAT"
- "3SAT"
- "Clique"
- "Vertex Cover"

Metodo:
1. dimostrare appartenenza a NP;
2. ridurre da problema noto NP-completo;
3. costruire trasformazione polinomiale;
4. dimostrare sì-se-e-solo-se;
5. concludere.
```

---

# Aggiornamenti `10_rag/RAG_EXAM_ANSWER_STYLE.md`

Aggiungere:

```md
## Risposte su Greedy

Quando la traccia chiede greedy:
- non limitarti a dire “scelgo localmente il migliore”;
- specifica criterio di scelta;
- spiega perché la scelta è sicura/corretta;
- se si parla di matroidi, usa ereditarietà e scambio.
```

```md
## Risposte su Knapsack

Quando la traccia chiede zaino:
- distinguere 0/1 da frazionario;
- per 0/1 usare DP;
- definire stato, casi base, ricorrenza;
- per vincoli extra aggiungere dimensioni allo stato.
```

```md
## Risposte su NP-completezza

Quando la traccia chiede NP-completezza:
- separare sempre `Π ∈ NP` da `NP-hard`;
- indicare certificato e verificatore;
- indicare problema noto da cui si riduce;
- scrivere la direzione della riduzione;
- dimostrare entrambe le implicazioni.
```

---

# Aggiornamento prompt da esame

Aggiornare `AI Chat during Exam/Final Prompt.md` o la sezione corrispondente.

Aggiungere:

```md
## Teoria APA — regole rapide

### Knapsack
Se compare zaino 0/1:
- usare DP `V[i,p]`;
- non usare greedy salvo zaino frazionario;
- con vincoli extra aggiungere dimensione allo stato.

### Greedy
Se compare greedy:
- controllare se esiste struttura di matroide o teorema dell'arco sicuro;
- indicare criterio locale;
- giustificare formalmente la correttezza.

### Kruskal
Se compare Kruskal:
- ordinare archi per peso crescente;
- aggiungere solo archi che non creano cicli;
- usare union-find se richiesto;
- collegare al matroide grafico o all'arco sicuro.

### NP-completezza
Se compare NP-completezza:
1. mostrare appartenenza a NP;
2. scegliere problema noto NP-completo;
3. ridurre dal noto al target;
4. dimostrare doppia implicazione;
5. concludere.

Non invertire la direzione della riduzione.
```

---

# Discrepanze da cercare nella repo

| Tema | Possibile errore | Correzione |
|---|---|---|
| Knapsack | greedy suggerito per 0/1 | correggere: usare DP |
| Knapsack | variante rossi non collegata al base | aggiungere link teorico |
| Greedy | assenza di dimostrazione | aggiungere necessità proof/correttezza |
| Matroidi | manca proprietà di scambio | aggiungere definizione |
| Matroidi | massimale confuso con massimo | aggiungere warning |
| Kruskal | non collegato a matroide grafico | aggiungere file teoria |
| Kruskal | manca union-find | aggiungere schema |
| NP | NP interpretato come “non polinomiale” | correggere |
| NP-completezza | direzione riduzione invertita | aggiungere warning |
| Clique/VC/IS | parametro `k` non trasformato | specificare `|V|-k` quando serve |
| SAT/3SAT | confusione tra formula e certificato | chiarire assegnazione booleana |

---

# Priorità

## Bloccanti

- Creare/aggiornare teoria su knapsack base.
- Creare/aggiornare teoria greedy e matroidi.
- Creare/aggiornare teoria Kruskal/matroide grafico.
- Creare/aggiornare teoria P/NP/riduzioni.
- Aggiornare retrieval index.
- Aggiornare pattern map.
- Aggiornare prompt da esame.

## Importanti

- Aggiungere warning:
  - greedy non sempre corretto;
  - zaino 0/1 non greedy;
  - direzione riduzione NP-completezza;
  - NP non significa “non polinomiale”;
  - Kruskal vs Prim;
  - massimale vs massimo.

## Utili ma non urgenti

- Aggiungere proof sketch più dettagliati.
- Aggiungere flashcard teoriche.
- Aggiungere esempi numerici completi.
- Collegare con appelli passati dove compaiono questi argomenti.

---

# Checklist Codex

- [ ] Cercare nella repo file su `knapsack`, `zaino`, `V[i,p]`.
- [ ] Cercare nella repo file su `greedy`, `matroide`, `scambio`, `ereditaria`.
- [ ] Cercare nella repo file su `Kruskal`, `MST`, `Union-Find`.
- [ ] Cercare nella repo file su `P`, `NP`, `SAT`, `3SAT`, `Clique`, `Vertex Cover`, `Independent Set`.
- [ ] Creare/aggiornare `05_theory/dp_knapsack_base.md`.
- [ ] Creare/aggiornare `04_methods/dp_knapsack_base.md`.
- [ ] Collegare `dp_knapsack_vincoli_colore.md` al knapsack base.
- [ ] Creare/aggiornare `05_theory/greedy_teoria_base.md`.
- [ ] Creare/aggiornare `05_theory/matroidi_e_greedy.md`.
- [ ] Creare/aggiornare `05_theory/kruskal_matroide_grafico.md`.
- [ ] Creare/aggiornare `04_methods/mst_kruskal.md`.
- [ ] Creare/aggiornare `05_theory/p_np_np_completezza.md`.
- [ ] Creare/aggiornare `05_theory/riduzioni_np_completezza.md`.
- [ ] Creare/aggiornare `04_methods/np_completezza_schema_dimostrazione.md`.
- [ ] Creare/aggiornare gli schemi in `07_solved_examples/`.
- [ ] Creare/aggiornare method card RAG.
- [ ] Aggiornare `10_rag/RAG_RETRIEVAL_INDEX.md`.
- [ ] Aggiornare `10_rag/RAG_PATTERN_MAP.md`.
- [ ] Aggiornare `10_rag/RAG_EXAM_ANSWER_STYLE.md`.
- [ ] Aggiornare `AI Chat during Exam/Final Prompt.md`.
- [ ] Controllare duplicazioni con file esercizi già creati.
- [ ] Fare commit.

---

# Criteri di completamento

Il lavoro è completo quando:

- una query RAG su “knapsack base” recupera stato `V[i,p]` e ricorrenza;
- una query RAG su “zaino con rossi” collega correttamente la variante allo zaino base;
- una query RAG su “greedy” recupera teoria e warning;
- una query RAG su “matroide” recupera ereditarietà, scambio e teorema greedy;
- una query RAG su “Kruskal” recupera matroide grafico e union-find;
- una query RAG su “NP-completezza” recupera lo schema standard;
- una query RAG su “3SAT Clique” recupera la riduzione;
- una query RAG su “Vertex Cover Clique Independent Set” recupera grafo complemento e trasformazione parametro;
- il prompt da esame contiene regole rapide ma non è sovraccarico;
- la teoria è compatta e utile agli esercizi.
