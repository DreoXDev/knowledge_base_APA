# RAG Answer Writing Templates - APA

## Scopo

Questo file non insegna nuovi algoritmi: definisce come scrivere le risposte da esame in modo copiabile a mano.

Separazione delle fonti:

- Correttezza della soluzione: PDF ufficiali, appelli, method card RAG, metodi validati.
- Stile di scrittura: appunti `SRC-NOTE-001`, esempi svolti validati, preferenze dell'utente.

Gli appunti della compagna possono suggerire intestazioni, ordine logico e micro-giustificazioni. Non devono sovrascrivere formule validate dalla RAG ufficiale.

## Regola zero: rileggi la consegna

Prima di scrivere, identifica internamente:

1. Tipo di output richiesto:
   - valore ottimo;
   - esistenza TRUE/FALSE;
   - sequenza/sottoinsieme da ricostruire;
   - completamento testuale;
   - dimostrazione teorica.
2. Quantificatore del vincolo:
   - almeno;
   - al massimo;
   - esattamente;
   - presenza;
   - assenza.
3. Oggetto del vincolo:
   - simboli;
   - archi;
   - vertici;
   - colori;
   - pesi;
   - coppie consecutive;
   - numero di elementi.
4. Forma richiesta dalla traccia:
   - solo coefficienti;
   - caso base;
   - passo ricorsivo;
   - soluzione finale;
   - bottom-up;
   - ricostruzione;
   - complessita;
   - teoria.

Questo controllo non va stampato nella risposta finale, salvo richiesta esplicita.

## Template Esercizio 1 - DP su sequenze

Usa questo stile quando la traccia chiede un esercizio di DP su sequenze. Se la traccia ha sottopunti numerati, rispetta sempre quell'ordine.

```text
ISTANZA:
X=<x1,...,xm>, Y=<y1,...,yn>, [altri dati].

SOLUZIONE:
[valore/sequenza/booleano richiesto].

SOTTOPROBLEMA:
Xi=<x1,...,xi>, i=0,...,m
Yj=<y1,...,yj>, j=0,...,n
[altri parametri richiesti dalla traccia]

Def. variabile:
C[...] = soluzione del sottoproblema (...), ossia ...

SOLUZIONE DEL PROBLEMA:
[coefficiente finale, es. C[m,n,K] oppure max C[i,j]]

CASO BASE:
[formule]
Breve giustificazione: ...

PASSO RICORSIVO:
Per indici validi:
- se ...
  C[...] = ...
- se ...
  C[...] = ...
```

Regole per i coefficienti:

- Definisci prima i prefissi.
- Definisci poi eventuali parametri aggiuntivi.
- Ogni parametro aggiuntivo deve essere richiesto dalla consegna.
- Per "presenza del rosso" usa un solo flag/parametro per il rosso.
- Non aggiungere un flag blu solo perche il blu compare nell'alfabeto.

Regole per stati impossibili:

- Massimo: usa `-infinito`.
- Minimo: usa `+infinito`.
- Booleano: usa `FALSE`.
- Non usare `-infinito` se il vincolo e "al massimo" e la soluzione vuota e ammessa.

## Template Esercizio 2 - DP su grafi

```text
1) Coefficienti
D[k,i,j,...] = TRUE/valore ottimo relativo a cammini da i a j
che usano come vertici intermedi solo vertici in {1,...,k}
e rispettano ...

2) Soluzione del problema
Per ogni coppia (i,j): D[n,i,j,...]
oppure il valore richiesto dalla traccia.

3) Caso base
k=0:
- i=j: ...
- (i,j) in E: ...
- altrimenti: ...

4) Passo ricorsivo
Non uso il vertice k:
D[k-1,i,j,...]

Uso il vertice k:
combino D[k-1,i,k,...] e D[k-1,k,j,...]

Quindi:
D[k,i,j,...] = ...
```

Regole:

- Booleano: usa `TRUE/FALSE` e operatori logici.
- Cammino minimo: usa `min` e somma.
- Cammino massimo: usa `max`.
- Se c'e un budget, dividilo tra i due sottocammini quando passi da `i` a `k` e da `k` a `j`.
- Se il vincolo riguarda coppie consecutive, controlla dove nasce la coppia nella concatenazione.

## Template bottom-up

```text
Inizializzo i casi base.
for i = ...
  for j = ...
    for [altri parametri] = ...
      applico il passo ricorsivo
return [coefficiente finale]
```

Regole:

- Usa gli stessi indici definiti nei coefficienti.
- Riempi in ordine crescente rispetto alle dipendenze.
- Non scrivere pseudocodice se la traccia non lo chiede.
- Se lo spazio e poco: "Calcolo bottom-up in ordine crescente degli indici usando la ricorrenza".

## Template ricostruzione

```text
RICOSTRUISCI(stato):
  se caso base: return/stampa niente
  se il ramo "prendo" realizza il valore ottimo:
      RICOSTRUISCI(stato precedente)
      stampa elemento preso
  altrimenti:
      segui il ramo che mantiene il valore ottimo
```

Per sequenze, stampa l'elemento dopo la chiamata ricorsiva sul prefisso precedente, cosi l'ordine resta corretto.

## Template teoria

Formato stabile:

```text
Definizione/Enunciato:
...

Proprieta:
...

Dimostrazione/giustificazione:
...

Conclusione:
...
```

Domande brevi:

```text
[Definizione in 1-2 righe]
[Proprieta principale]
[Conclusione]
```

Correttezza:

```text
Invariante:
...
Inizializzazione:
...
Mantenimento:
...
Terminazione:
...
```

Complessita:

```text
Metodo:
...
Numero di esecuzioni:
...
Costo di una esecuzione:
...
Complessita totale:
...
Confronto:
...
```

Esempio Dijkstra all-pairs:

```text
Eseguo Dijkstra una volta per ogni sorgente, quindi |V| volte.
Con heap binario: O(|V|(|E| log |V|)).
Floyd-Warshall costa O(|V|^3).
Confronto in base alla densita del grafo.
```

## Template completamento testuale

Scrivi la frase completa, non solo le parole mancanti.

```text
La frase completa e: ...
```

Se sono richiesti insiemi:

```text
Il set richiesto e {...}, di cardinalita ...
```

Se sono richiesti valori:

```text
Il valore da inserire e ...
```

Regole:

- Conserva il linguaggio della traccia.
- Non aggiungere teoria non richiesta.
- Se il completamento dipende da un disegno, indica prima il risultato e poi una micro-motivazione.
- Se ci sono piu spazi vuoti, riempili nello stesso ordine.

## Disegni e parti grafiche

Per esercizi grafici/disegni, rispondi con conferma testuale operativa:

- cosa segnare;
- cosa scartare;
- valore/insieme finale;
- una motivazione breve solo se utile.

Non produrre lunghe spiegazioni.

## Checklist finale

Prima della risposta finale controlla internamente:

1. Ho rispettato l'ordine della traccia?
2. Ho scritto coefficienti, domini e significato?
3. Ho scritto la soluzione finale come riga autonoma?
4. Ho distinto almeno/al massimo/esattamente?
5. Ogni stato extra e giustificato dalla consegna?
6. I casi base usano `-infinito`, `+infinito` o `FALSE` solo quando serve?
7. La risposta e breve e ricopiabile?
