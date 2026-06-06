---
type: method
topic: floyd-warshall-varianti-vincoli-colori
status: official_confirmed
source_id:
  - SRC-OFFICIAL-EX-003
  - SRC-OFFICIAL-EX-004
  - SRC-OFFICIAL-EX-005
  - SRC-OFFICIAL-EX-006
  - SRC-OFFICIAL-EX-007
  - SRC-OFFICIAL-EX-008
  - SRC-OFFICIAL-EX-009
  - SRC-OFFICIAL-EX-010
  - SRC-OFFICIAL-EX-011
tags:
  - apa
  - metodo
  - topic/floyd-warshall
  - topic/programmazione-dinamica
  - topic/grafi-colorati
---

# Floyd-Warshall - base e varianti con vincoli

## Idea unificata

Tutte le varianti mantengono lo schema:

```text
k = massimo vertice intermedio ammesso
intermedi ammessi in {1,...,k}
```

Per ogni coppia `i,j`:

```text
E1 = cammino ottimo/esistente che non usa k
E2 = cammino che usa k, spezzato in i -> k e k -> j
```

La differenza tra le varianti e lo stato extra.

## Semiring operativo

| Tipo | Coefficiente | Scelta | Composizione | Impossibile |
|---|---|---|---|---|
| Cammino minimo | `d` | `min` | `+` | `+infinito` |
| Esistenza | `e` | `OR` | `AND` | `FALSE` |

## Tabella decisionale

| Variante | Tipo | Stato | Stato extra | Finale |
|---|---|---|---|---|
| FW standard | minimo | `d_ij^k` | nessuno | `d_ij^n` |
| Archi alternati | minimo | `d_ij^{k,f,l}` | primo/ultimo colore arco | `min_{f,l} d_ij^{n,f,l}`, con `d_ii=0` |
| Archi alternati | esistenza | `e_ij^{k,f,l}` | primo/ultimo colore arco | `OR_{f,l} e_ij^{n,f,l}`, con `e_ii=TRUE` |
| Vertici alternati | minimo | `d_ij^k` | nessuno | `d_ij^n` |
| Vertici alternati | esistenza | `e_ij^k` | nessuno | `e_ij^n` |
| Pari archi rossi + vertici alternati | minimo | `d_ij^{k,p}` | parita archi rossi | `d_ij^{n,0}` |
| Esattamente 3 coppie vertici rossi consecutivi | minimo | `d_ij^{k,r}` | conteggio coppie rosse consecutive | `d_ij^{n,3}` |
| Esattamente 3 archi rossi | minimo | `d_ij^{k,r}` | conteggio archi rossi | `d_ij^{n,3}` |
| Presenza archi rossi e blu | esistenza | `e_ij^{k,r,b}` | flag presenza red/blue | `e_ij^{n,1,1}` |

## Floyd-Warshall standard

Sottoproblema:

```text
P_ij^k = cammino minimo da i a j con intermedi in {1,...,k}
```

Ricorrenza:

```text
d_ij^0 = W[i,j]
d_ij^k = min(d_ij^{k-1}, d_ik^{k-1} + d_kj^{k-1})
```

Per predecessori:

```text
se resta d_ij^{k-1}: pi_ij^k = pi_ij^{k-1}
se passa da k:       pi_ij^k = pi_kj^{k-1}
```

## Alternanza del colore degli archi

Colore sugli archi: `Col : E -> {red, green}`.

Per concatenare `i -> k` e `k -> j` serve sapere:

- `f`: colore del primo arco;
- `l`: colore dell'ultimo arco.

### Cammini minimi

Stato:

```text
d_ij^{k,f,l}
```

Caso base `k=0`:

```text
i = j:
  d_ij^{0,f,l} = +infinito

i != j and (i,j) in E:
  se f = l and f = Col(i,j): d_ij^{0,f,l} = w_ij
  altrimenti:                d_ij^{0,f,l} = +infinito

i != j and (i,j) notin E:
  d_ij^{0,f,l} = +infinito
```

Passo:

```text
E1 = d_ij^{k-1,f,l}
E2 = min { d_ik^{k-1,f,a} + d_kj^{k-1,b,l} | a,b in C and a != b }
d_ij^{k,f,l} = min(E1,E2)
```

Finale:

```text
i != j: d_ij = min { d_ij^{n,f,l} | f,l in C }
i = j:  d_ii = 0
```

### Esistenza

Stato:

```text
e_ij^{k,f,l}
```

Caso base `k=0`:

```text
i = j:
  e_ij^{0,f,l} = FALSE

i != j and (i,j) in E:
  se f = l and f = Col(i,j): e_ij^{0,f,l} = TRUE
  altrimenti:                e_ij^{0,f,l} = FALSE

i != j and (i,j) notin E:
  e_ij^{0,f,l} = FALSE
```

Passo:

```text
E1 = e_ij^{k-1,f,l}
E2 = OR { e_ik^{k-1,f,a} AND e_kj^{k-1,b,l} | a,b in C and a != b }
e_ij^{k,f,l} = E1 OR E2
```

Finale:

```text
i != j: e_ij = OR { e_ij^{n,f,l} | f,l in C }
i = j:  e_ii = TRUE
```

## Alternanza del colore dei vertici

Colore sui vertici: `Col : V -> {red, green}`.

Non servono stati `f,l`: quando si concatena in `k`, il vertice di giunzione e lo stesso.

### Cammini minimi

Caso base:

```text
i = j: d_ij^0 = 0

i != j and (i,j) in E and Col(i) != Col(j): d_ij^0 = w_ij
i != j and (i,j) in E and Col(i) = Col(j):  d_ij^0 = +infinito
i != j and (i,j) notin E:                    d_ij^0 = +infinito
```

Passo:

```text
d_ij^k = min(d_ij^{k-1}, d_ik^{k-1} + d_kj^{k-1})
```

### Esistenza

Caso base:

```text
i = j: e_ij^0 = TRUE

i != j and (i,j) in E and Col(i) != Col(j): e_ij^0 = TRUE
i != j and (i,j) in E and Col(i) = Col(j):  e_ij^0 = FALSE
i != j and (i,j) notin E:                    e_ij^0 = FALSE
```

Passo:

```text
e_ij^k = e_ij^{k-1} OR (e_ik^{k-1} AND e_kj^{k-1})
```

## Numero pari di archi rossi + alternanza vertici

Stato:

```text
d_ij^{k,p}
p = 0 pari, p = 1 dispari
```

Finale:

```text
d_ij^{n,0}
```

Base:

```text
i = j:
  d_ij^{0,0} = 0
  d_ij^{0,1} = +infinito

i != j and (i,j) in E and ColV(i) != ColV(j):
  se ColE(i,j) = red: d_ij^{0,1} = w_ij
  se ColE(i,j) != red: d_ij^{0,0} = w_ij

tutti gli altri stati: +infinito
```

Passo:

```text
E1 = d_ij^{k-1,p}
E2 = min { d_ik^{k-1,p1} + d_kj^{k-1,p2}
           | (p1 + p2) mod 2 = p }
d_ij^{k,p} = min(E1,E2)
```

## Esattamente 3 coppie di vertici rossi consecutivi

Stato:

```text
d_ij^{k,r}, 0 <= r <= 3
```

Una coppia rossa consecutiva e una coppia adiacente nel cammino `(v_t,v_{t+1})` con entrambi i vertici rossi.

Finale:

```text
d_ij^{n,3}
```

Base:

```text
i = j:
  d_ij^{0,0} = 0
  d_ij^{0,r} = +infinito per r > 0

i != j and (i,j) in E and Col(i)=red and Col(j)=red:
  d_ij^{0,1} = w_ij
  altri r: +infinito

i != j and (i,j) in E and non entrambi rossi:
  d_ij^{0,0} = w_ij
  altri r: +infinito

i != j and (i,j) notin E:
  d_ij^{0,r} = +infinito per ogni r
```

Passo:

```text
E1 = d_ij^{k-1,r}
E2 = min { d_ik^{k-1,r1} + d_kj^{k-1,r2} | r1 + r2 = r }
d_ij^{k,r} = min(E1,E2)
```

## Esattamente 3 archi rossi

Stato:

```text
d_ij^{k,r}, 0 <= r <= 3
```

Finale:

```text
d_ij^{n,3}
```

Base:

```text
i = j:
  d_ij^{0,0} = 0
  d_ij^{0,r} = +infinito per r > 0

i != j and (i,j) in E and Col(i,j)=red:
  d_ij^{0,1} = w_ij
  altri r: +infinito

i != j and (i,j) in E and Col(i,j)!=red:
  d_ij^{0,0} = w_ij
  altri r: +infinito

i != j and (i,j) notin E:
  d_ij^{0,r} = +infinito per ogni r
```

Passo:

```text
E1 = d_ij^{k-1,r}
E2 = min { d_ik^{k-1,r1} + d_kj^{k-1,r2} | r1 + r2 = r }
d_ij^{k,r} = min(E1,E2)
```

## Esistenza con archi rossi e blu presenti

Stato booleano:

```text
e_ij^{k,r,b}
r = 1 se e presente almeno un arco rosso
b = 1 se e presente almeno un arco blu
```

Finale:

```text
e_ij^{n,1,1}
```

Base:

```text
i = j:
  e_ij^{0,0,0} = TRUE
  e_ij^{0,r,b} = FALSE per (r,b) != (0,0)

i != j and (i,j) in E:
  se Col(i,j)=red:  e_ij^{0,1,0} = TRUE
  se Col(i,j)=blue: e_ij^{0,0,1} = TRUE
  altrimenti:       e_ij^{0,0,0} = TRUE
  tutti gli altri stati: FALSE

i != j and (i,j) notin E:
  e_ij^{0,r,b} = FALSE per ogni r,b
```

Passo:

```text
E1 = e_ij^{k-1,r,b}
E2 = OR { e_ik^{k-1,r1,b1} AND e_kj^{k-1,r2,b2}
          | r = (r1 OR r2), b = (b1 OR b2) }
e_ij^{k,r,b} = E1 OR E2
```

## Warning

- Archi colorati alternati: servono `f,l`; il cammino banale non ha primo/ultimo arco.
- Vertici colorati alternati: non servono `f,l`.
- Esistenza: non usare pesi.
- Conteggio esatto: provare tutte le decomposizioni `r = r1 + r2`.
- Parita: combinare con `(p1+p2) mod 2`.
- Presenza: usare flag booleani, non contatori.
- Coppie di vertici rossi consecutivi: contare coppie adiacenti nel cammino, non vertici rossi totali.

Collegamenti: [[fw_base_bottom_up]], [[fw_varianti_vincoli_colori_schema]], [[dp_grafi_floyd_warshall_stato_esteso]].
