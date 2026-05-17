# exam_2025_02_11_p1_recupero_e01 — LCS a tre sequenze con al massimo due rossi

> [!Info]
> Fonte: [[exam_2025_02_11_part1_recupero]]
> Stato: cataloged
> Tipologia: programmazione dinamica su sequenze
> Pattern: [[parte_i_dynamic_programming_patterns]], [[metodo_lcs_tre_sequenze_vincolo_colori]]

## Problema

Date tre sequenze $X$, $Y$ e $W$ su un alfabeto $S$, ogni simbolo ha colore rosso, blu o nero tramite:

$$
col:S \to \{R,B,N\}
$$

Si vuole trovare una sottosequenza comune di lunghezza massima tra $X$, $Y$ e $W$ che contenga al massimo due simboli rossi.

## Nota di duplicazione controllata

Questo esercizio coincide con:

```txt
exam_2025_02_11_p1_completo_e01
```

e fa riferimento allo stesso metodo senza duplicazioni.

## Coefficienti consigliati

Definire:

$$
C[i,j,k,r]
$$

dove:

- $0 \le i \le m$;
- $0 \le j \le n$;
- $0 \le k \le d$;
- $r \in \{0,1,2\}$.

$C[i,j,k,r]$ è la lunghezza massima di una sottosequenza comune tra i prefissi $X_i$, $Y_j$, $W_k$ che usa al massimo $r$ simboli rossi.

## Caso base

Se almeno una sequenza è vuota:

$$
C[0,j,k,r] = 0
$$

$$
C[i,0,k,r] = 0
$$

$$
C[i,j,0,r] = 0
$$

per ogni $r \in \{0,1,2\}$.

## Passo ricorsivo

Se non vale $x_i = y_j = w_k$:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r]
\end{cases}
$$

Se $x_i = y_j = w_k$ e $col(x_i) \ne R$:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r] \\
1 + C[i-1,j-1,k-1,r]
\end{cases}
$$

Se $x_i = y_j = w_k$ e $col(x_i)=R$, per $r>0$:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r] \\
1 + C[i-1,j-1,k-1,r-1]
\end{cases}
$$

Per $r=0$, il simbolo rosso non può essere preso.

## Soluzione

La lunghezza della soluzione è:

$$
C[m,n,d,2]
$$

## Collegamenti

- [[exam_2025_02_11_p1_completo_e01]]
- [[lcs]]
- [[sottosequenze_comuni]]
- [[vincoli_su_colori]]
- [[metodo_lcs_tre_sequenze_vincolo_colori]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
