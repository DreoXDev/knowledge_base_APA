# Varianti LCS con vincoli

Fonte principale: [[source_inventory]] / SRC-EXTRA-001 / esercizi APA.pdf.

| Variante | Coefficiente | Stato extra | Caso base speciale | Passo chiave | Fonte |
|---|---|---|---|---|---|
| LCS base | $C_{i,j}$ | nessuno | $0$ su riga/colonna 0 | match/mismatch | SRC-EXTRA-001 p.3 |
| LCS esattamente 3 rossi | $C_{i,j,r}$ | conteggio rossi | $-\infty$ per $r>0$ | match rosso scala $r-1$ | SRC-EXTRA-001 pp.4-6 |
| Tutte le LCS almeno 3 rossi | $B_{i,j,r}$ | booleano + soglia | true per $r=0$ | AND sui rami ottimi | SRC-EXTRA-001 p.7 |
| Tutte le LCS parita rossi | $B_{i,j,p}$ | parita | dipende da convenzione | flip parita se match rosso | SRC-EXTRA-001 pp.8-10 |
| LCS ingombro $\le C$ | $L_{i,j,c}$ | budget | 0 su prefisso vuoto | match con peso | SRC-EXTRA-001 p.11 |
| LICS | $C_{i,j}$ termina in match | ordine crescente | 0 se mismatch | max su predecessori minori | SRC-EXTRA-001 p.15 |
| LCS alternanza pari/dispari | da verificare | parita ultimo elemento | da verificare | da verificare | SRC-EXTRA-001 pp.17-18 |

> [!Warning]
> Le varianti "tutte le LCS" richiedono di ragionare solo sui rami che producono LCS ottime. Non basta applicare AND/OR su tutti i sottoproblemi.

