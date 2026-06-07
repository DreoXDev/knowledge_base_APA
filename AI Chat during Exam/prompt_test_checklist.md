# Checklist test prompt APA

Usare questi casi dopo ogni modifica al prompt finale.

- [ ] LCS con presenza del rosso: non deve aggiungere il blu.
- [ ] LCS con `Sigma -> {R,B,N}` e presenza del rosso: deve scrivere `rho(a)=0 altrimenti`, non solo `rho(a)=0 se blu`.
- [ ] LCS con `Sigma -> {R,B,N}` e presenza del blu: deve scrivere `beta(a)=1 se blu, beta(a)=0 altrimenti`.
- [ ] LCS con almeno un rosso: soluzione `C[m,n,1]`, non un massimo su stati che non garantiscono il rosso.
- [ ] LCS con rosso e blu: deve usare due flag o due stati solo se entrambi sono richiesti.
- [ ] LCS con esattamente k: deve distinguere da al massimo k e gestire stati impossibili.
- [ ] LCS con al massimo k: deve usare budget/massimo ammesso senza imporre esattamente k.
- [ ] LCS tre sequenze: deve usare `C[i,j,k]`, non due LCS successive.
- [ ] LICS: non deve usare LCS standard e deve restituire un massimo globale.
- [ ] Knapsack 0/1: non deve usare greedy.
- [ ] Knapsack con colore: deve decrementare il budget solo quando prende un oggetto vincolato.
- [ ] Floyd-Warshall esistenza: deve usare `OR/AND`.
- [ ] Floyd-Warshall cammino minimo: deve usare `min/+`.
- [ ] Floyd-Warshall con colori: deve distinguere colori su archi e colori su vertici.
- [ ] Dijkstra: deve estrarre il minimo globale tra i non definitivi.
- [ ] Dijkstra: deve rilassare solo archi uscenti dal nodo estratto.
- [ ] Prim: deve usare `key`, non distanze dalla sorgente.
- [ ] Kruskal: deve scartare cicli e fermarsi a `n-1` archi.
- [ ] Greedy teorico: deve includere criterio e prova di correttezza/scambio.
- [ ] Matroide: deve includere ereditarieta e scambio.
- [ ] Clique -> Vertex Cover: deve usare complemento e parametro `n-k`.
- [ ] 3SAT -> Clique: deve creare vertici per letterali e archi solo tra clausole diverse non contraddittorie.
- [ ] NP-completezza: deve includere NP + NP-hard + doppia implicazione.
- [ ] Teoria breve: deve restare in 5-8 righe se la domanda vale pochi punti.
- [ ] Risposta generale: deve essere copiabile a mano e non stampare checklist interne.

## Test DP sequenze - LCS con budget

- [ ] Se la traccia contiene "ingombro complessivo <= W", lo stato contiene un indice `p=0,...,W`.
- [ ] La ricorrenza consuma budget quando prende un simbolo: `p-w(a)`.
- [ ] La soluzione finale e `C[m,n,W]`, non `max C[i,j]`.
- [ ] Non compare `w(prev)<=w(curr)`, salvo che la traccia chieda esplicitamente monotonia/crescenza.
- [ ] Il caso base con sequenza vuota vale `0` per ogni budget `p`.
- [ ] La stampa parte da `STAMPA(m,n,W)`.

### Test negativo

Traccia:

```text
Ogni simbolo a ha ingombro w(a). Trovare una piu lunga sottosequenza comune
con ingombro complessivo <= W.
```

Risposta da rifiutare:

```text
C[i,j] con condizione w(X[h]) <= w(X[i])
```

Motivo:

```text
Confonde budget totale con monotonia locale.
```

## Test - LCS con colori R/B/N e presenza del rosso

Traccia sintetica:

```text
Due sequenze X,Y su Sigma. Ogni simbolo ha colore in {R,B,N}.
Determinare una LCS che contiene almeno un simbolo rosso.
```

Risposta attesa:

- Stato: `C[i,j,r]` con `r in {0,1}`.
- Indicatore: `rho(a)=1 se a e rosso, rho(a)=0 altrimenti`, cioe se blu o nero.
- Base: `C[0,j,0]=C[i,0,0]=0`, `C[0,j,1]=C[i,0,1]=-infinito`.
- Ricorrenza LCS con diagonale: `1 + C[i-1,j-1,max(0,r-rho(a))]`.
- Soluzione: `C[m,n,1]`.

Errore da bloccare:

- Scrivere `rho(a)=0` solo se `a` e blu.
