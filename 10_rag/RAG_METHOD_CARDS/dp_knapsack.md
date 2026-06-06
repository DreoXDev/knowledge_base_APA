# Method Card — Knapsack (Zaino 0/1 e Varianti)

## Triggers (Parole Chiave)

* `zaino`, `knapsack`, `capacità`, `peso`, `ingombro`, `valore`, `profitto`, `oggetti`, `0/1`
* `al massimo 3 rossi`, `oggetti colorati`

---

## Decisione Rapida e Criteri di Scelta

1. **Zaino 0/1 Base**:
   - Gli oggetti sono indivisibili (sì/no).
   - Risolvere tramite **Programmazione Dinamica** bottom-up con stato $V[i, p]$ (valore massimo con i primi $i$ oggetti e capacità $p$).
   - Valore ottimo finale: $V[n, W]$.
   - **Greedy NON funziona** per lo zaino 0/1.

2. **Zaino Frazionario** (Fractional Knapsack):
   - È possibile prendere frazioni di oggetti.
   - Risolvere tramite **algoritmo Greedy** ordinando gli oggetti per densità di valore $v_i/w_i$ decrescente.

3. **Variante con Vincoli di Colore** (es. "Al massimo $K$ oggetti rossi"):
   - Estendere lo stato base aggiungendo una dimensione $r$ per il budget residuo o massimo di oggetti rossi utilizzabili: $V[i, c, r]$.
   - Se l'oggetto $i$ è rosso, la transizione per includerlo riduce $r$ di 1. Se non è rosso, $r$ resta invariato.
   - Valore ottimo finale: $V[n, C, K]$.

---

## Formulario ed Equazioni di Ricorrenza

### 1. Zaino 0/1 Base
Stato: $V[i, p]$ per $0 \le i \le n$, $0 \le p \le W$.
Casi base: $V[0, p] = 0 \quad \forall p$; $V[i, 0] = 0 \quad \forall i$.
Ricorrenza:
$$
V[i, p] =
\begin{cases}
V[i-1, p] & \text{se } w_i > p \\
\max\{V[i-1, p], \ V[i-1, p-w_i] + v_i\} & \text{se } w_i \le p
\end{cases}
$$

### 2. Zaino con "Al Massimo 3 Oggetti Rossi"
Stato: $d[i, c, r]$ per $0 \le i \le n, 0 \le c \le C, 0 \le r \le 3$.
Ricorrenza (se $w_i \le c$):
- Se $Col(i) \ne \text{red}$:
  $$d[i, c, r] = \max\{d[i-1, c, r], \ d[i-1, c-w_i, r] + v_i\}$$
- Se $Col(i) = \text{red}$ e $r > 0$:
  $$d[i, c, r] = \max\{d[i-1, c, r], \ d[i-1, c-w_i, r-1] + v_i\}$$
- Se $Col(i) = \text{red}$ e $r = 0$:
  $$d[i, c, 0] = d[i-1, c, 0]$$

---

## Errori Comuni da Evitare

> [!WARNING]
> * **Tentare il greedy sullo zaino 0/1**: Errore gravissimo d'esame. Usare sempre la programmazione dinamica.
> * **Dimenticare casi base**: Scrivere solo $V[0,p]=0$ omettendo $V[i,0]=0$ (o viceversa).
> * **Confondere "Al massimo" con "Esattamente"**: "Al massimo" consente di ritornare il valore finale direttamente (es. $d[n,C,3]$). "Esattamente" richiede l'uso di $-\infty$ come inizializzazione per stati non validi.

---

## Riferimenti nella KB

* Teoria base: [[zaino_01]]
* Metodo base: [[metodo_programmazione_dinamica_zaino_01]]
* Metodo variante colore: [[dp_knapsack_vincoli_colore]]
* Esempio svolto base: [[knapsack_base_schema]]
* Esempio svolto variante colore: [[knapsack_al_massimo_3_rossi_schema]]
