# Errori comuni APA

## DP su sequenze

- Confondere sottosequenza con sottostringa.
- Usare $C[m,n]$ quando la risposta e $\max_{i,j} C[i,j]$.
- Dimenticare $-\infty$ nei vincoli esatti.
- Trattare "tutte le LCS" come "esiste una LCS".
- Sbagliare il consumo della risorsa residua.
- Non distinguere al massimo / esattamente / almeno.
- Dimenticare la ricostruzione della soluzione.
- Scalare un contatore colore quando il simbolo scelto non ha quel colore.

## DP su grafi

- Confondere $k$ vertice intermedio con lunghezza del cammino.
- Usare OR quando serve min.
- Non definire bene il caso base.
- Dimenticare colori iniziali/finali nei vincoli su archi consecutivi.
- Concatenare due cammini senza aggiornare conteggi o parita.

## Parte II

- Riduzione NP nel verso sbagliato.
- Non dimostrare appartenenza a NP.
- Scrivere solo intuizione senza doppia implicazione.
- Usare Dijkstra con pesi negativi.
- Saltare step di Kruskal.
- Confondere matroide grafico con generico grafo.

## Warning da fonti manoscritte

> [!Warning]
> Restano da verificare Hateville senza due rossi consecutivi, parita dei rossi in tutte le LCS, LCS alternanza pari/dispari e alcune ricostruzioni top-down da SRC-NOTE-001.
