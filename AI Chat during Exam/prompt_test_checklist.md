# Checklist test prompt APA

Usare questi casi dopo ogni modifica al prompt finale.

- [ ] LCS con presenza del rosso: non deve aggiungere il blu.
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
