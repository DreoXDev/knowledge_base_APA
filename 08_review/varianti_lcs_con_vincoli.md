# Varianti LCS con vincoli

Fonti: [[source_inventory]] / SRC-EXTRA-001 / SRC-NOTE-001.

| Variante | Stato | Dimensioni DP | Casi base | Match | Non match | Soluzione | Esempi |
|---|---|---|---|---|---|---|---|
| LCS base | $C[i,j]$ | 2D | prefisso vuoto a $0$ | $C[i-1,j-1]+1$ | max alto/sinistra | $C[m,n]$ | [[lcs_base_SRC_NOTE_001]] |
| LCS esattamente K rossi | $C[i,j,k]$ | 3D | $-\infty$ per $k>0$ | consuma $k$ se rosso | max | $C[m,n,K]$ | [[lcs_esattamente_k_rossi_SRC_NOTE_001]] |
| LCS al massimo K rossi | $C[i,j,k]$ | 3D | $0$ | consuma se possibile | max | $C[m,n,K]$ | [[lcs_al_massimo_k_rossi_SRC_NOTE_001]] |
| Tutte le LCS almeno K rossi | booleano + lunghezze LCS | 3D/ausiliario | true per soglia 0 | attenzione a "tutte" | AND sui rami ottimi | booleano | [[lcs_tutte_almeno_3_rossi_SRC_EXTRA_001]] |
| Parita rossi | $B[i,j,p]$ | 3D | convenzione pari/dispari | flip parita se rosso | dipende dai rami ottimi | $B[m,n,pari]$ | [[lcs_tutte_parita_rossi_SRC_EXTRA_001]] |
| Ingombro/somma | $C[i,j,c]$ | 3D | $0$ | consuma peso | max | $C[m,n,C]$ | [[lcs_somma_leq_k_SRC_NOTE_001]] |
| LICS | $C[i,j]$ che termina in match | 2D ausiliaria | $0$ se mismatch | max precedente minore | non si usa classico max | $\max C[i,j]$ | [[lics_SRC_NOTE_001]] |
| 3 sequenze | $C[i,j,k,\dots]$ | 3D+ | prefisso vuoto | match triplo | max rami | valore finale | [[mapping_appelli_to_SRC_NOTE_001]] |

## Come riconoscere quale variante usare

- Se la consegna dice "piu lunga sottosequenza comune", partire da [[metodo_lcs_base]].
- Se aggiunge conteggi di colori, aggiungere una dimensione per ogni budget.
- Se dice "esattamente", usare stati impossibili con $-\infty$ nei massimi.
- Se dice "tutte le LCS", calcolare prima le lunghezze ottime e usare AND solo sui rami ottimi.
- Se chiede crescente/decrescente, usare il pattern LICS: la risposta e un massimo globale, non necessariamente $C[m,n]$.
- Se chiede somma, peso o ingombro, aggiungere una dimensione di capacita residua.

## Warning aperti

> [!Warning]
> La parita dei rossi nelle fonti manoscritte ha convenzioni da verificare. Usare $p=0$ pari e $p=1$ dispari solo dichiarandolo.

