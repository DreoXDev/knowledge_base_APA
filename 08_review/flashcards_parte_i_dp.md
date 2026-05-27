# Flashcards Parte I - Programmazione Dinamica

## Flashcard - LCS esattamente $K$ rossi

> [!Question]
> Quale stato aggiungo alla LCS per imporre esattamente $K$ rossi?

> [!Answer]
> Aggiungo un indice $r$: $C_{i,j,r}$ rappresenta la lunghezza di una LCS tra $X_i$ e $Y_j$ con esattamente $r$ rossi. Il caso base usa $0$ per $r=0$ e $-\infty$ per $r>0$.

## Flashcard - Tutte le LCS

> [!Question]
> Cosa cambia tra "esiste una LCS con proprieta $P$" e "tutte le LCS hanno proprieta $P$"?

> [!Answer]
> Per "tutte" devo combinare con AND tutti i rami che producono una LCS ottima. Prima filtro i rami tramite la tabella delle lunghezze LCS.

## Flashcard - LCS con ingombro

> [!Question]
> Quale stato aggiungo per vincolare l'ingombro complessivo della LCS?

> [!Answer]
> Aggiungo il budget $c$: $L_{i,j,c}$ e la lunghezza di una LCS tra $X_i,Y_j$ con ingombro al massimo $c$.

## Flashcard - LICS

> [!Question]
> Perche nella LICS conviene definire uno stato che termina nel match $x_i=y_j$?

> [!Answer]
> Per controllare il vincolo crescente sui predecessori: se prendo $x_i=y_j$, cerco il massimo tra $C_{h,k}$ con $h<i$, $k<j$ e $x_h<x_i$.

## Flashcard - Knapsack con massimo $R$ rossi

> [!Question]
> Come cambia lo zaino 0/1 se posso prendere al massimo $R$ oggetti rossi?

> [!Answer]
> Uso $OPT_{i,c,r}$. Se prendo un oggetto rosso decremento $r$; se prendo un oggetto non rosso, $r$ resta invariato.

## Flashcard - Alternanza pari/dispari

> [!Question]
> Perche una LCS alternante pari/dispari richiede stato aggiuntivo?

> [!Answer]
> Per sapere se il prossimo elemento scelto deve essere pari o dispari devo ricordare la parita dell'ultimo elemento della sottosequenza.
