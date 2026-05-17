# exam_2025_02_11_p1_recupero_e02 — Cammini minimi con parità blu e vincolo sui vertici rossi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_recupero]]
> Stato: cataloged
> Tipologia: programmazione dinamica su grafi pesati
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_cammini_minimi_vincoli_colori_parita]]

## Problema

Dato un grafo pesato sugli archi:

$$
(V,E,W,f,g)
$$

senza cappi e senza cicli di peso negativo.

Ogni vertice ha un colore:

$$
f:V \to \{R,N\}
$$

Ogni arco ha un colore:

$$
g:E \to \{M,B\}
$$

Per ogni coppia di vertici $(i,j)$ si vuole calcolare il peso di un cammino minimo da $i$ a $j$ tale che:

1. il numero di archi blu sia dispari;
2. non vi siano due vertici consecutivi rossi.

## Pattern riconosciuto

È una variante di cammini minimi con programmazione dinamica in stile Floyd-Warshall, ma con stato esteso.

Rispetto a Floyd-Warshall classico, lo stato deve ricordare:

- la parità del numero di archi blu;
- la validità del vincolo locale sui vertici rossi consecutivi.

Il vincolo sui vertici consecutivi viene garantito localmente controllando gli archi diretti e le transizioni. Poiché il vertice $k$ intermediario è unico in ogni punto di concatenazione, l'unione di due cammini che finiscono e iniziano in $k$ non introduce nuove consecutività adiacenti oltre a quelle già presenti nei sottocammini (in quanto $k$ non è adiacente ad altri nodi se non tramite gli archi già controllati).

## Predicati e funzioni ausiliarie

Definire il peso dell'arco:

$$
W(i,j)
$$

se $(i,j) \in E$.

Definire il contributo di parità dell'arco:

$$
blu(i,j) =
\begin{cases}
1 & \text{se } g(i,j)=B \\
0 & \text{se } g(i,j)=M
\end{cases}
$$

Definire il predicato che vieta due vertici rossi consecutivi:

$$
ok(i,j) =
\neg(f(i)=R \land f(j)=R)
$$

per ogni arco in cui $i$ e $j$ diventano consecutivi.

## Coefficienti consigliati

Numerare i vertici come $V = \{1,\dots,n\}$.

Definire:

$$
D[k,i,j,p]
$$

dove:

- $0 \le k \le n$;
- $i,j \in V$;
- $p \in \{0,1\}$.

$D[k,i,j,p]$ è il peso minimo di un cammino da $i$ a $j$ che:

- usa come vertici intermedi solo vertici in $\{1,\dots,k\}$;
- contiene un numero di archi blu con parità $p$ ($p=0$ pari, $p=1$ dispari);
- non contiene due vertici consecutivi rossi.

Usare $+\infty$ per indicare che non esiste alcun cammino valido con tali caratteristiche.

## Caso base

Per $k=0$, ammettiamo solo cammini vuoti e archi diretti.

Cammino vuoto:

$$
D[0,i,i,0] = 0
$$

$$
D[0,i,i,1] = +\infty
$$

Arco diretto $(i,j) \in E$:

se $ok(i,j)$:

$$
D[0,i,j,blu(i,j)] = W(i,j)
$$

Tutti gli altri coefficienti per $k=0$ sono $+\infty$.
Se esistono più archi paralleli compatibili con lo stesso stato di parità, si sceglie il minimo peso.

## Passo ricorsivo

Per $k \ge 1$:

$$
D[k,i,j,p] =
\min
\left(
D[k-1,i,j,p],
\min_{q \in \{0,1\}}
\left[
D[k-1,i,k,q] + D[k-1,k,j,p \oplus q]
\right]
\right)
$$

dove $\oplus$ è lo XOR/somma modulo 2.

> [!Note]
> La consecutività tra vertici rossi non viene violata nella concatenazione in $k$ poiché il vertice $k$ è l'ultimo nodo del primo sottocammino e il primo del secondo. Non vi sono altri nodi consecutivi creati oltre a quelli già controllati nei sottoproblemi.

## Soluzione

Per ogni coppia $(i,j)$, il peso richiesto è:

$$
D[n,i,j,1]
$$

Se $D[n,i,j,1] = +\infty$, non esiste alcun cammino valido.

## Collegamenti

- [[cammini_minimi]]
- [[floyd_warshall]]
- [[grafi_colorati]]
- [[metodo_cammini_minimi_vincoli_colori_parita]]
- [[metodo_floyd_warshall_stato_esteso]]
- [[parte_i_dynamic_programming_patterns]]
