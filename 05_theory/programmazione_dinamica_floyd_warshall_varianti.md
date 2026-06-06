---
type: theory
topic: floyd-warshall-varianti
status: official_confirmed
tags:
  - apa
  - teoria
  - topic/floyd-warshall
---

# Programmazione dinamica - varianti Floyd-Warshall

Ogni variante Floyd-Warshall conserva il significato di `k`: i vertici intermedi ammessi sono nell'insieme `{1,...,k}`.

La ricorrenza ha sempre due casi:

- `E1`: il cammino non usa il vertice `k`;
- `E2`: il cammino usa `k` e viene concatenato come `i -> k` seguito da `k -> j`.

Per cammini minimi si usano `min`, somma dei pesi e `+infinito`.

Per esistenza si usano `OR`, `AND` e `FALSE`.

Gli stati extra servono solo per ricordare le informazioni necessarie a verificare il vincolo quando si concatenano i due sottocammini.

Collegamenti: [[fw_varianti_vincoli_colori]], [[fw_varianti_vincoli_colori_schema]].
