---
type: theory
topic: lcs
status: scaffold
tags:
  - apa
  - teoria
  - topic/lcs
  - topic/programmazione-dinamica
---

# Teoria - LCS

## Definizione minima

La Longest Common Subsequence e una sottosequenza comune di lunghezza massima tra due sequenze.

## Definizioni ufficiali LCS

- Sequenza: lista ordinata di elementi.
- Prefisso `X_i`: sequenza `<x_1,...,x_i>`.
- Sottosequenza: sequenza ottenuta eliminando zero o piu elementi senza cambiare l'ordine relativo.
- Sottosequenza comune: sottosequenza di entrambe le sequenze.
- LCS: sottosequenza comune di lunghezza massima.

Come problema di ottimizzazione, si calcola prima la lunghezza `c_{m,n}` e poi, se richiesto, si ricostruisce una soluzione.

## Collegamenti agli esercizi

- [[exam_2025_07_03_p1_e01]]
- [[exam_2025_06_09_p1_e01]]
- [[exam_2025_11_10_p1_tema_a_e01]]
- [[exam_2025_02_11_p1_completo_e01]]
- [[exam_2025_02_11_p1_recupero_e01]]
- [[exam_2025_01_13_p1_e01]]
- [[exam_2025_09_17_p1_e01]]

## Collegamenti ai metodi

- [[dp_lcs_base]]
- [[dp_lcs_tre_sequenze]]
- [[dp_lcs_due_rossi_consecutivi]]
- [[dp_lcs_dispari_pari_alternati]]
- [[metodo_programmazione_dinamica_lcs_vincolo_ingombro]]
- [[metodo_programmazione_dinamica_lcs_vincoli_colori]]
- [[metodo_lcs_tre_sequenze_vincolo_colori]]

## LCS su piu sequenze

La LCS standard su due sequenze si generalizza aggiungendo una dimensione della tabella DP per ogni sequenza.

Per tre sequenze:

- sottoproblema: `LCS(X_i,Y_j,W_h)`;
- coefficiente: `c_{i,j,h}`;
- casi base: almeno un prefisso vuoto;
- match: tutti e tre gli ultimi elementi sono uguali;
- mismatch: massimo tra i sottoproblemi ottenuti scartando un ultimo elemento da una sequenza.

La complessita cresce come prodotto delle lunghezze.

## Varianti con vincoli sulla sottosequenza

Quando il vincolo riguarda proprieta interne della sottosequenza, spesso non basta il sottoproblema classico `LCS(X_i,Y_j)`.

Esempi ufficiali:

- due rossi consecutivi: stati `c_ij1` e `c_ij0`, vincolati a terminare nel match corrente;
- dispari in posizioni dispari e pari in posizioni pari: stato `c_ij`, vincolato a terminare, con controllo sulla lunghezza precedente.

In queste varianti il valore ottimo puo essere un massimo globale sugli stati validi, non necessariamente `c_{m,n}`.

## Nota da esame - costruzione DP ufficiale

Per costruire una DP su varianti LCS con vincoli, il professore usa la sequenza:

1. sottoproblemi;
2. coefficienti;
3. valore ottimo;
4. casi base;
5. passo ricorsivo;
6. algoritmo bottom-up;
7. ricostruzione.

Per LCS con al massimo `k` rossi, la fonte ufficiale `SRC-LECTURE-001` usa uno stato con significato "al massimo r rossi" e valore finale `C[m,n,k]`.

> [!Warning]
> Nota scaffold: completare solo con le varianti richieste dagli appelli.
