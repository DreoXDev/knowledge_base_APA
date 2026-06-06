# RAG Smoke Test - Parte I 2025-07-03

Fonte:

- `02_transcriptions/exams/exam_2025_07_03_part1.md`
- `03_exercise_catalog/exercises/exam_2025_07_03_p1_e01.md`
- `03_exercise_catalog/exercises/exam_2025_07_03_p1_e02.md`

## Test 1 - Esercizio 1

Pattern riconosciuto:

`LCS con budget di ingombro`.

Card recuperata:

`10_rag/RAG_METHOD_CARDS/dp_lcs_ingombro.md`.

Controllo chiave:

- usa la formulazione primaria `C[i,j,k]` con ingombro `<= k`;
- non usa la variante "esattamente b" come default;
- coefficiente finale `C[m,n,W]`;
- risposta divisa nei 6 punti della traccia.

### Output atteso

```text
1)
- X_i = <x_1,...,x_i>, con 0 <= i <= m.
- Y_j = <y_1,...,y_j>, con 0 <= j <= n.
- C[i,j,k] = lunghezza di una LCS di X_i e Y_j con ingombro <= k, con 0 <= k <= W.

2)
- C[0,j,k] = 0 per ogni j,k.
- C[i,0,k] = 0 per ogni i,k.

3)
Per i>0, j>0, 0 <= k <= W:

- Se x_i != y_j:
  C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])

- Se x_i = y_j e w(x_i) <= k:
  C[i,j,k] = max(
    C[i-1,j,k],
    C[i,j-1,k],
    1 + C[i-1,j-1,k-w(x_i)]
  )

- Se x_i = y_j e w(x_i) > k:
  C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])

4)
C[m,n,W]

5)
LCS-INGOMBRO(X, Y, W)
    m = length(X)
    n = length(Y)

    for k = 0 to W
        for j = 0 to n
            C[0,j,k] = 0
        for i = 0 to m
            C[i,0,k] = 0

    for i = 1 to m
        for j = 1 to n
            for k = 0 to W
                if x_i != y_j then
                    C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])
                else
                    if w(x_i) <= k then
                        C[i,j,k] = max(C[i-1,j,k],
                                        C[i,j-1,k],
                                        1 + C[i-1,j-1,k-w(x_i)])
                    else
                        C[i,j,k] = max(C[i-1,j,k], C[i,j-1,k])

    return C

6)
STAMPA-LCS-INGOMBRO(C, X, Y, i, j, k)
    if i = 0 then
        return
    if j = 0 then
        return

    if x_i != y_j then
        if C[i,j,k] = C[i-1,j,k] then
            STAMPA-LCS-INGOMBRO(C, X, Y, i-1, j, k)
        else
            STAMPA-LCS-INGOMBRO(C, X, Y, i, j-1, k)
    else
        if w(x_i) <= k and C[i,j,k] = 1 + C[i-1,j-1,k-w(x_i)] then
            STAMPA-LCS-INGOMBRO(C, X, Y, i-1, j-1, k-w(x_i))
            print x_i
        else
            if C[i,j,k] = C[i-1,j,k] then
                STAMPA-LCS-INGOMBRO(C, X, Y, i-1, j, k)
            else
                STAMPA-LCS-INGOMBRO(C, X, Y, i, j-1, k)
```

Esito: superato.

## Test 2 - Esercizio 2

Pattern riconosciuto:

`DP/Floyd-Warshall con stato esteso su grafi colorati`.

Card recuperata:

`10_rag/RAG_METHOD_CARDS/dp_grafi_stato_esteso.md`.

Controllo chiave:

- risposta divisa nei 4 punti della traccia;
- stato esteso con conteggi di rossi e blu;
- soluzione finale per ogni coppia `(i,j)` con esattamente 2 rossi e 2 blu.

### Output atteso

```text
1)
C[k,i,j,r,b] = true se esiste un cammino da i a j che usa solo vertici intermedi in {1,...,k} e contiene esattamente r archi rossi e b archi blu.

Indici:
- 0 <= k <= |V|
- 0 <= r <= 2
- 0 <= b <= 2

2)
Per k = 0:
- C[0,i,i,0,0] = true per ogni i.
- Se (i,j) in E e col(i,j)=R, allora C[0,i,j,1,0] = true.
- Se (i,j) in E e col(i,j)=B, allora C[0,i,j,0,1] = true.
- Se (i,j) in E e col(i,j)=N, allora C[0,i,j,0,0] = true.
- Tutti gli altri coefficienti sono false.

3)
Per k >= 1:

C[k,i,j,r,b] =
C[k-1,i,j,r,b] OR
OR su r1+r2=r, b1+b2=b di
(C[k-1,i,k,r1,b1] AND C[k-1,k,j,r2,b2]).

4)
Per ogni coppia (i,j), esiste un cammino richiesto se e solo se:

C[|V|,i,j,2,2] = true.
```

Esito: superato.
