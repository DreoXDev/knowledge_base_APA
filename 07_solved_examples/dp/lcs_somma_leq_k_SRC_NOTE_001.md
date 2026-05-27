# LCS con somma <= K - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagina 7.

## Istanza

Sequenze numeriche $X,Y$ e soglia $K$.

## Soluzione richiesta

Lunghezza di una LCS con somma complessiva $\le K$.

## Definizione coefficienti

$$
C[i,j,k]=\text{lunghezza massima con somma }\le k.
$$

## Passo ricorsivo

Se $x_i=y_j$ e $x_i\le k$, confrontare presa e non presa; altrimenti non prendere.

## Collegamenti

- [[dp_lcs_vincolo_somma_ingombro]]
- [[lcs_ingombro_SRC_EXTRA_001]]

