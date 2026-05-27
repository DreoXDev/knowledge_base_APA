# Trascrizione - Analisi e Progettazione di Algoritmi

> [!Info]
> Fonte: `SRC-NOTE-001`  
> File: `01_sources/notes_raw/Analisi E Progettazione Di Algoritmi.pdf`  
> Tipo: appunti manoscritti della studentessa.  
> Stato: trascrizione interpretativa con marcatura delle parti ambigue.

> [!Warning]
> Il PDF e manoscritto/fotografato e l'OCR e rumoroso. Questa nota conserva una trascrizione pagina-per-pagina orientata allo studio: quando una formula non e leggibile con sicurezza, viene segnalata invece di essere completata arbitrariamente.

## Indice pagine

- Pagine 1-3: LCS base, definizioni, sottostruttura ottima.
- Pagine 4-5: Interleaving di sequenze.
- Pagina 6: LCS di lunghezza esatta.
- Pagine 7-8: LCS con somma/ingombro e LICS.
- Pagine 9-22: knapsack colori, LCS con vincoli colore, varianti LICS.
- Pagine 23-32: DP su grafi/Floyd-Warshall con stato esteso.
- Pagine 33-39: Dijkstra, Floyd-Warshall, BFS e grafi.
- Pagine 40-50: NP-completezza e riduzioni.
- Pagine 51-65: esercizi fotografati, riepiloghi e note sparse.

## Pagina 1 - LCS: definizioni

### Trascrizione interpretativa

LCS = Longest Common Subsequence. Input: due sequenze $X,Y$ su un insieme finito di simboli. Output: una sequenza $Z$ che e sottosequenza comune a $X$ e $Y$ e ha lunghezza massima.

Definizioni riconoscibili:

- sequenza su alfabeto;
- prefisso di lunghezza $i$ di una sequenza $X$: $X_i=\langle x_1,\dots,x_i\rangle$;
- $X[i]=x_i$, i-esimo simbolo;
- sottosequenza comune ottenuta eliminando zero o piu simboli, non necessariamente consecutivi.

> [!Tip]
> La LCS non e necessariamente unica come sequenza, ma la lunghezza ottima e unica.

## Pagina 2 - LCS: sottostruttura ottima

### Trascrizione interpretativa

La pagina introduce la "sottostruttura ottima", proprieta che permette di applicare programmazione dinamica.

Se gli ultimi simboli coincidono, $x_m=y_n$, una LCS termina con quel simbolo e si ottiene da una LCS di $X_{m-1}$ e $Y_{n-1}$ concatenando $x_m$.

Se gli ultimi simboli non coincidono, la soluzione ottima deriva da uno dei due sottoproblemi:

- LCS di $X_m$ e $Y_{n-1}$;
- LCS di $X_{m-1}$ e $Y_n$.

## Pagina 3 - LCS: ricorrenza

### Trascrizione interpretativa

Forma normalizzata:

$$
C[i,j]=
\begin{cases}
0 & \text{se } i=0 \lor j=0,\\
C[i-1,j-1]+1 & \text{se } x_i=y_j,\\
\max(C[i-1,j],C[i,j-1]) & \text{se } x_i\ne y_j.
\end{cases}
$$

Valore finale: $C[m,n]$.

## Pagina 4 - Interleaving: istanza

### Trascrizione interpretativa

Problema: date sequenze $X$, $Y$, $W$, stabilire se $W$ e un interleaving di $X$ e $Y$. L'interpretazione negli appunti e: $X$ e $Y$ sono due sottosequenze disgiunte di $W$ la cui unione delle posizioni copre tutto $W$.

## Pagina 5 - Interleaving: DP booleana

### Trascrizione interpretativa

Sottoproblema:

$$
S[i,j]=true
$$

sse $W_{i+j}$ e interleaving di $X_i$ e $Y_j$.

Passo:

$$
S[i,j] =
(x_i=w_{i+j}\land S[i-1,j]) \lor (y_j=w_{i+j}\land S[i,j-1]).
$$

> [!Warning]
> La pagina mostra casi separati per ultimo simbolo preso da $X$, da $Y$, da entrambi o da nessuno. La forma con OR e la normalizzazione compatta.

## Pagina 6 - LCS di lunghezza esatta

### Trascrizione interpretativa

Problema: date $X,Y$ e $L\ge 0$, stabilire se esiste una LCS di lunghezza $L$.

Stato:

$$
B[i,j,\ell]=true
$$

sse esiste una sottosequenza comune di $X_i,Y_j$ di lunghezza $\ell$.

> [!Question]
> La consegna manoscritta usa la parola LCS; se si intende "sottosequenza comune di lunghezza $L$" la DP booleana basta. Se si intende "una LCS ottima lunga esattamente $L$", va confrontato anche $L$ con la lunghezza ottima.

## Pagina 7 - LCS con somma minore o uguale a K

### Trascrizione interpretativa

Problema: date due sequenze numeriche $X,Y$, trovare la lunghezza di una LCS con somma complessiva dei numeri $\le K$.

Stato:

$$
C[i,j,k]=\text{lunghezza massima di una LCS tra }X_i,Y_j\text{ con somma}\le k.
$$

Se $x_i=y_j$ e $x_i\le k$, si confronta prendere il simbolo con non prenderlo. Se $x_i>k$, non si prende.

## Pagina 8 - LICS

### Trascrizione interpretativa

Problema: date due sequenze numeriche $X,Y$, fornire una LCS crescente.

Problema ausiliario: $C[i,j]$ e la lunghezza di una LCS crescente che termina con $x_i=y_j$.

$$
C[i,j]=
\begin{cases}
0 & \text{se } x_i\ne y_j,\\
1+\max\{C[h,k]\mid h<i,\ k<j,\ x_h<x_i\} & \text{se } x_i=y_j.
\end{cases}
$$

Soluzione: $\max_{i,j}C[i,j]$.

## Pagina 9 - Knapsack colori: istanza

### Trascrizione interpretativa

Esercizio di knapsack: oggetti $1,\dots,n$, valore $v_i$, peso/ingombro $w_i$, colore $col(i)\in\{red,blue\}$, capacita $C$, vincolo sul numero di oggetti rossi $R$.

## Pagina 10 - Knapsack colori: sottoproblema

### Trascrizione interpretativa

Stato:

$$
OPT[i,c,r]=\text{valore massimo con i primi }i\text{ oggetti, capacita }c\text{ e al massimo }r\text{ rossi}.
$$

Il passo distingue: oggetto troppo pesante, oggetto rosso con $r>0$, rosso con $r=0$, non rosso.

## Pagina 11 - LCS con vincoli rossi/blu/neutri

### Trascrizione interpretativa

La pagina usa uno stato del tipo $C[i,j,r,b]$ per una LCS con limiti sui colori. Il testo riconoscibile indica rossi, blu e neutri e una sequenza soluzione associata.

> [!Warning]
> Alcuni indici e condizioni colore sono disturbati dall'OCR. La versione normalizzata e in [[dp_lcs_vincoli_colore]].

## Pagina 12 - LCS colori: ricostruzione

### Trascrizione interpretativa

La pagina prosegue con il caso ricorsivo e una variabile per la sequenza soluzione. L'idea operativa e memorizzare quale ramo produce il massimo per poter stampare una soluzione.

## Pagina 13 - LICS con valore massimo e vincoli locali

### Trascrizione interpretativa

Compare una variante in cui la sottosequenza crescente massimizza un valore complessivo e non contiene due numeri consecutivi rossi. La soluzione termina con $x_i=y_j$.

> [!Warning]
> La condizione "due numeri consecutivi rossi" va verificata: puo significare consecutivi nella sottosequenza o nel dominio originale.

## Pagina 14 - LICS con alternanza/intervalli

### Trascrizione interpretativa

Variante LICS in cui i numeri appaiono alternando valori o classi. Si usa ancora il pattern "termina in $x_i=y_j$" e un massimo sui predecessori compatibili.

## Pagina 15 - LICS decrescente con vincoli colore/parita

### Trascrizione interpretativa

Esercizio: sottosequenza comune decrescente con condizioni aggiuntive: non ci sono due numeri consecutivi rossi ne dispari. Stato $C[i,j]$ con soluzione che termina in $x_i=y_j$.

> [!Warning]
> Formula parzialmente leggibile; usare come pattern, non come ricorrenza definitiva senza controllo.

## Pagina 16 - Ricostruzione top-down

### Trascrizione interpretativa

Sono presenti pseudocodice bottom-up e procedura `PRINT` top-down con matrice dei predecessori $H$ o $B$.

## Pagina 17 - LCS con al massimo K rossi

### Trascrizione interpretativa

Stato riconoscibile:

$$
C[i,j,k]=\text{lunghezza massima di una LCS tra }X_i,Y_j\text{ con al massimo }k\text{ rossi}.
$$

Il caso base usa $0$ per prefissi vuoti.

## Pagina 18 - LCS con esattamente K rossi

### Trascrizione interpretativa

Variante esatta: per prefissi vuoti, $0$ se $k=0$ e $-\infty$ se $k>0$.

## Pagina 19 - LCS con parita dei rossi

### Trascrizione interpretativa

Si introduce uno stato di parita $p\in\{0,1\}$ per contare i rossi modulo 2. Un match rosso cambia parita; un match non rosso la conserva.

## Pagina 20 - Print di una LCS vincolata

### Trascrizione interpretativa

La pagina contiene ricostruzione/stampa della soluzione partendo dai coefficienti e dai predecessori.

## Pagina 21 - Budget colori multipli

### Trascrizione interpretativa

Pattern generale: per ogni vincolo di conteggio si aggiunge una dimensione allo stato DP, ad esempio rossi e blu.

## Pagina 22 - Riepilogo stato esteso su sequenze

### Trascrizione interpretativa

Riepilogo operativo: prefissi + dimensioni extra; caso base coerente con "al massimo", "esattamente" o booleano; soluzione nella cella finale o massimo globale.

## Pagina 23 - Grafi colorati

### Trascrizione interpretativa

Inizio blocco su cammini in grafi con vincoli sui colori degli archi/vertici.

## Pagina 24 - Floyd-Warshall con stato esteso

### Trascrizione interpretativa

Stato:

$$
D^k[i,j,\sigma]
$$

con vertici intermedi ammessi in $\{1,\dots,k\}$ e stato aggiuntivo $\sigma$.

## Pagina 25 - Caso base k=0

### Trascrizione interpretativa

Il caso base considera cammini diretti da $i$ a $j$ senza vertici intermedi. Lo stato extra viene inizializzato dal colore/peso/proprieta dell'arco diretto.

## Pagina 26 - Passo passa/non passa da k

### Trascrizione interpretativa

Schema:

$$
D^k[i,j,\sigma]=D^{k-1}[i,j,\sigma]\lor \bigvee_{\sigma_1\oplus\sigma_2=\sigma}
D^{k-1}[i,k,\sigma_1]\land D^{k-1}[k,j,\sigma_2].
$$

## Pagina 27 - Colori degli archi

### Trascrizione interpretativa

Lo stato extra registra conteggi, parita, primo/ultimo colore o transizioni vietate.

## Pagina 28 - Consecutivita vietate

### Trascrizione interpretativa

Variante con divieto di due archi consecutivi di certi colori. Serve salvare almeno il colore iniziale/finale del cammino parziale.

## Pagina 29 - Coppie consecutive di ugual colore

### Trascrizione interpretativa

Variante con numero di coppie consecutive di ugual colore. Lo stato extra conta le coppie e richiede controllo al punto di concatenazione.

## Pagina 30 - Notazione d^k(i,j,a,b)

### Trascrizione interpretativa

Gli appunti usano variabili tipo $d^k(i,j,a,b)$ o simili per rappresentare cammini tra $i$ e $j$ con stato extra.

## Pagina 31 - Applicazione Floyd-Warshall esteso

### Trascrizione interpretativa

Esempio applicativo del pattern grafi. Le formule sono da riportare nei metodi normalizzati.

## Pagina 32 - DP booleana su grafi

### Trascrizione interpretativa

Riepilogo di ricorrenza booleana: OR tra "non uso $k$" e "uso $k$".

## Pagina 33 - Dijkstra

### Trascrizione interpretativa

Appunti su Dijkstra: algoritmo per cammini minimi da sorgente singola con pesi non negativi, scelta greedy del vertice con distanza temporanea minima.

## Pagina 34 - Dijkstra vs Floyd-Warshall

### Trascrizione interpretativa

Dijkstra risolve single-source shortest paths; Floyd-Warshall risolve all-pairs shortest paths e usa programmazione dinamica sui vertici intermedi.

## Pagina 35 - Cammini minimi e complessita

### Trascrizione interpretativa

Note su complessita e condizioni d'uso. Dijkstra richiede pesi non negativi; Floyd-Warshall gestisce struttura matriciale e tutti i cammini.

## Pagina 36 - BFS tree check

### Trascrizione interpretativa

Possibile domanda: modificare BFS per verificare se un grafo non orientato e un albero. Controllare connettivita e assenza di cicli, oppure $|E|=|V|-1$ piu connettivita.

## Pagina 37 - Alberi e visite

### Trascrizione interpretativa

Note su visita, predecessori, cicli e connettivita.

## Pagina 38 - Floyd-Warshall classico

### Trascrizione interpretativa

Ricorrenza classica:

$$
D^k[i,j]=\min(D^{k-1}[i,j],D^{k-1}[i,k]+D^{k-1}[k,j]).
$$

## Pagina 39 - Chiusura transitiva

### Trascrizione interpretativa

Versione booleana di Floyd-Warshall per esistenza di cammini.

## Pagina 40 - NP e certificati

### Trascrizione interpretativa

Per mostrare che un problema e in NP: descrivere un certificato di dimensione polinomiale e un verificatore polinomiale.

## Pagina 41 - Schema NP-completezza

### Trascrizione interpretativa

Schema: mostrare $A\in NP$, scegliere $B$ NP-completo noto, costruire una riduzione polinomiale $B\le_p A$, dimostrare doppia implicazione.

## Pagina 42 - Riduzione polinomiale

### Trascrizione interpretativa

La trasformazione deve essere calcolabile in tempo polinomiale e preservare la risposta si/no.

## Pagina 43 - SAT e Cook

### Trascrizione interpretativa

SAT e indicato come problema NP-completo fondamentale; 3-SAT e problema noto da cui ridurre.

## Pagina 44 - 3-CNF-SAT

### Trascrizione interpretativa

Formula in clausole, ogni clausola con tre letterali. Usata per costruzioni grafiche.

## Pagina 45 - CLIQUE

### Trascrizione interpretativa

Problema CLIQUE: esiste un sottoinsieme di $k$ vertici tutti adiacenti a coppie?

## Pagina 46 - VERTEX-COVER

### Trascrizione interpretativa

Problema VERTEX-COVER: esiste un insieme di $k$ vertici che copre tutti gli archi?

## Pagina 47 - Riduzione CLIQUE / VERTEX-COVER

### Trascrizione interpretativa

Relazione standard tramite complemento: clique in $G$ corrisponde a independent set nel complemento, e independent set complementare a vertex cover.

## Pagina 48 - Dimostrazione se e solo se

### Trascrizione interpretativa

Le riduzioni vanno dimostrate in entrambi i versi: se l'istanza di partenza e positiva allora lo e quella costruita; e viceversa.

## Pagina 49 - Errori comuni NP

### Trascrizione interpretativa

Non basta dire "sembra difficile"; bisogna dimostrare appartenenza a NP e NP-hardness tramite riduzione.

## Pagina 50 - Riepilogo riduzioni

### Trascrizione interpretativa

Riepilogo dei problemi noti e delle riduzioni ricorrenti: SAT, 3-SAT, CLIQUE, VERTEX-COVER.

## Pagina 51 - Appello fotografato DP

### Trascrizione interpretativa

Pagina con esercizio d'appello e annotazioni. Tema DP su sequenze o zaino.

> [!Warning]
> Lettura incerta: usare come collegamento metodologico, non come trascrizione ufficiale d'appello.

## Pagina 52 - Appello fotografato grafi

### Trascrizione interpretativa

Pagina con esercizio su grafi e cammini vincolati.

## Pagina 53 - Appello fotografato riduzioni

### Trascrizione interpretativa

Pagina con esercizio di riduzione/NP-completezza.

## Pagina 54 - Ricostruzione DP

### Trascrizione interpretativa

Appunti su stampa di una soluzione tramite matrice predecessori.

## Pagina 55 - Pseudocodice bottom-up

### Trascrizione interpretativa

Schema di cicli annidati per riempire tabelle DP secondo l'ordine degli indici.

## Pagina 56 - Complessita

### Trascrizione interpretativa

Note su complessita temporale e spaziale: prodotto delle dimensioni dello stato, moltiplicato per il costo del massimo interno.

## Pagina 57 - Domande orali grafi

### Trascrizione interpretativa

Promemoria su Dijkstra, Floyd-Warshall, BFS e cammini minimi.

## Pagina 58 - Domande orali NP

### Trascrizione interpretativa

Promemoria su NP, NP-completo, riduzioni e certificati.

## Pagina 59 - Sintesi DP sequenze

### Trascrizione interpretativa

Riepilogo dei pattern DP su sequenze: prefissi, stato extra, casi base, soluzione finale.

## Pagina 60 - Sintesi DP grafi

### Trascrizione interpretativa

Riepilogo del pattern con vertici intermedi.

## Pagina 61 - Sintesi NP/grafi

### Trascrizione interpretativa

Collegamento tra esercizi grafi e teoria NP.

## Pagina 62 - Note miste

### Trascrizione interpretativa

Contenuto misto/facoltativo.

> [!Warning]
> Lettura incerta.

## Pagina 63 - Note miste

### Trascrizione interpretativa

Contenuto misto/facoltativo.

> [!Warning]
> Lettura incerta.

## Pagina 64 - Ripasso finale

### Trascrizione interpretativa

Checklist implicita: istanza, soluzione, sottoproblema, coefficienti, caso base, passo, soluzione, algoritmo, complessita.

## Pagina 65 - Note finali

### Trascrizione interpretativa

Pagina finale con note sparse e richiami.

> [!Question]
> Verificare manualmente le pagine 51-65 se servono per completare esercizi specifici.
