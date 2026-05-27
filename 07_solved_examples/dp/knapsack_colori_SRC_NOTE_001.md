# Knapsack con colori - SRC-NOTE-001

## Fonte

SRC-NOTE-001, pagine 9-10.

## Istanza

Oggetti con valore, peso e colore; capacita $C$; massimo $R$ oggetti rossi.

## Soluzione richiesta

Sottoinsieme di valore massimo rispettando capacita e vincolo sui rossi.

## Definizione coefficienti

$$
OPT[i,c,r]=\text{valore massimo con i primi }i\text{ oggetti, capacita }c\text{ e al massimo }r\text{ rossi}.
$$

## Passo ricorsivo

Vedi [[dp_knapsack_colori]].

## Ricostruzione

Confrontare presa e non presa; scalare $r$ solo per oggetti rossi.

## Collegamenti

- [[knapsack_max_R_rossi_SRC_EXTRA_001]]

