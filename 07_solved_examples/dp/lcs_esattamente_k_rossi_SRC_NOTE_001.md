# LCS con esattamente K rossi - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagina 18; collegato a SRC-EXTRA-001.

> [!Info]
> Questo esempio riguarda "esattamente K rossi". Non usarlo come fonte primaria per tracce "al massimo K rossi"; per quelle usare `SRC-LECTURE-001` e [[lcs_al_massimo_3_rossi_SRC_LECTURE_001]].

## Istanza

Sequenze $X,Y$, funzione colore, valore $K$.

## Soluzione richiesta

Lunghezza massima di una LCS con esattamente $K$ rossi.

## Caso base

$$
C[0,j,0]=C[i,0,0]=0,\qquad C[0,j,k]=C[i,0,k]=-\infty \text{ per }k>0.
$$

## Passo ricorsivo

Come la variante al massimo $K$, ma il significato del contatore e esatto.

## Valore della soluzione

$$
C[m,n,K].
$$

## Collegamenti

- [[dp_lcs_vincoli_colore]]
- [[lcs_esattamente_3_rossi_SRC_EXTRA_001]]
