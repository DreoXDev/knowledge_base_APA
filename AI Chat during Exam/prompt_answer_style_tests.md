# Test stile risposta prompt APA

- [ ] Esercizio DP sequenze: la risposta contiene coefficienti, base, ricorrenza, soluzione finale.
- [ ] Esercizio DP sequenze: se la traccia e numerata, la risposta segue i numeri.
- [ ] Esercizio DP sequenze: definisce prefissi e domini degli indici prima del coefficiente.
- [ ] LCS con solo rosso: non compare un flag blu.
- [ ] LCS con `Sigma -> {R,B,N}` e presenza del rosso: `rho(a)=0` copre blu e nero con "altrimenti".
- [ ] La definizione di ogni funzione indicatrice copre tutti i casi della traccia, anche quelli irrilevanti per il vincolo.
- [ ] LCS con "al massimo": non usa esattamente.
- [ ] LCS con "esattamente": usa stati impossibili se necessari.
- [ ] Esercizio grafi booleano: usa TRUE/FALSE, non min.
- [ ] Esercizio grafi cammino minimo: usa min, non TRUE/FALSE.
- [ ] Teoria: risposta in definizione/proprieta/conclusione.
- [ ] Correttezza: usa invariante/inizializzazione/mantenimento/terminazione se richiesto.
- [ ] Complessita: distingue numero di esecuzioni e costo di una esecuzione.
- [ ] Completamento testo: frase completa, non solo parole isolate.
- [ ] Disegno/grafo: risposta operativa e breve.
- [ ] Risposta generale: non stampa la checklist interna.

## Answer style test - LCS con ingombro complessivo <= W

Input:

```text
Date X e Y e una funzione w: Sigma -> N. Determinare una LCS di X e Y
con ingombro complessivo <= W.
```

Output accettato deve contenere:

```text
C[i,j,p]
p=0,...,W
C[m,n,W]
p-w(a)
STAMPA(m,n,W)
```

Output non accettato se contiene solo:

```text
C[i,j]
w(prev)<=w(curr)
max C[i,j]
```
