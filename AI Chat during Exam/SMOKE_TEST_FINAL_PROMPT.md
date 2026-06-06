# Smoke Test Final Prompt

## Test A - Parte I Esercizio 1

Input simulato:

```text
Foto di esercizio LCS con ingombro <= W.
```

Output atteso:

- punti 1-4 molto compatti;
- punti 5-6 con pseudocodice;
- nessuna spiegazione lunga;
- formulazione `C[i,j,k]` con vincolo `<= k`;
- nessun `-infinito` come default.

Esito: superato. Le regole sono presenti in `Final Prompt.md`, sezione 4.

## Test B - Parte I Esercizio 2

Input simulato:

```text
Foto di esercizio su cammino con esattamente 2 archi rossi e 2 blu.
```

Output atteso:

- coefficienti;
- caso base;
- passo ricorsivo;
- soluzione finale;
- niente pseudocodice se non richiesto.

Esito: superato. Le regole sono presenti in `Final Prompt.md`, sezione 5.

## Test C - Ultima facciata

Input simulato:

```text
Foto con completamento frasi + domanda teorica a scelta.
```

Output atteso:

- completamento trascritto con parole in **grassetto**;
- scelta della domanda teorica piu sicura;
- risposta teorica medio/lunga, completa e ordinata.

Esito: superato. Le regole sono presenti in `Final Prompt.md`, sezione 7 e nel modulo `prompt_sections/ultima_facciata_teoria_completamento.md`.
