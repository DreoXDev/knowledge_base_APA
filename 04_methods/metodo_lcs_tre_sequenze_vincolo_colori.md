---
type: method
status: scaffold
tags:
  - apa
  - metodo
  - topic/programmazione-dinamica
  - topic/lcs
  - topic/sottosequenze-comuni
  - topic/vincoli-su-colori
---

# Metodo - LCS a tre sequenze con vincoli sui colori

## Quando si usa

Quando si vuole trovare la più lunga sottosequenza comune (LCS) a **tre sequenze** (invece delle classiche due) che soddisfi un vincolo aggiuntivo sul colore o sul numero di determinati simboli (stato di budget o presenza).

## Stato della DP (Coefficienti)

Dato che le sequenze sono tre, la posizione all'interno di ciascuna richiede tre indici di prefisso ($i$, $j$, $k$). Il vincolo aggiuntivo richiede un quarto indice ($r$) per memorizzare il budget residuo o lo stato di presenza dei colori:

$$
C[i,j,k,r]
$$

dove:
- $0 \le i \le m$ (prefisso della prima sequenza $X$);
- $0 \le j \le n$ (prefisso della seconda sequenza $Y$);
- $0 \le k \le d$ (prefisso della terza sequenza $W$);
- $0 \le r \le B$ (budget massimo consentito per il colore vincolato, oppure flag booleano).

## Caso base

Se una qualsiasi delle tre sequenze considerate è vuota (prefisso di lunghezza 0), la lunghezza della LCS comune è necessariamente 0, indipendentemente dal budget residuo:

$$
C[0,j,k,r] = 0 \quad \forall j,k,r
$$

$$
C[i,0,k,r] = 0 \quad \forall i,k,r
$$

$$
C[i,j,0,r] = 0 \quad \forall i,j,r
$$

## Passo ricorsivo

Il passo ricorsivo si suddivide in base alla coincidenza dei tre caratteri finali:

### 1. Se i caratteri finali NON coincidono (almeno uno è diverso, cioè non vale $x_i = y_j = w_k$):
Non è possibile estendere la LCS comune con questo carattere. Riduciamo la ricerca escludendo singolarmente il carattere finale di ciascuna sequenza:

$$
C[i,j,k,r] =
\max
\begin{cases}
C[i-1,j,k,r] \\
C[i,j-1,k,r] \\
C[i,j,k-1,r]
\end{cases}
$$

### 2. Se i caratteri finali COINCIDONO ($x_i = y_j = w_k$):
Possiamo scegliere se includere il carattere nella LCS o ignorarlo.
- **Se il carattere non è vincolato** (es. non ha il colore rosso che consuma il budget):
  $$
  C[i,j,k,r] = \max
  \begin{cases}
  C[i-1,j,k,r] \\
  C[i,j-1,k,r] \\
  C[i,j,k-1,r] \\
  1 + C[i-1,j-1,k-1,r]
  \end{cases}
  $$
- **Se il carattere è vincolato** (es. è rosso, che consuma 1 unità del budget):
  - Con budget residuo $r > 0$:
    $$
    C[i,j,k,r] = \max
    \begin{cases}
    C[i-1,j,k,r] \\
    C[i,j-1,k,r] \\
    C[i,j,k-1,r] \\
    1 + C[i-1,j-1,k-1,r-1]
    \end{cases}
    $$
  - Senza budget residuo ($r = 0$):
    Il carattere non può essere incluso. Si ricade nel caso di mancata estensione:
    $$
    C[i,j,k,0] = \max
    \begin{cases}
    C[i-1,j,k,0] \\
    C[i,j-1,k,0] \\
    C[i,j,k-1,0]
    \end{cases}
    $$

## Soluzione finale

Se il vincolo richiede "al massimo $B$ simboli colorati" ed è stata utilizzata una semantica cumulativa ("al massimo $r$"), la soluzione è semplicemente:

$$
C[m,n,d,B]
$$

## Esercizi collegati

- [[exam_2025_02_11_p1_completo_e01]]

## Teoria e Pattern collegati

- [[lcs]]
- [[vincoli_su_colori]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[parte_i_dynamic_programming_patterns]]
