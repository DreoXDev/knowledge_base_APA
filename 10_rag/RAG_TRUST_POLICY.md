# RAG Trust Policy

## Gerarchia delle fonti

Quando rispondi a un esercizio, usa le fonti in questo ordine:

1. Esempio svolto verificato in `07_solved_examples/`
2. Metodo specifico completo in `04_methods/`
3. Pattern ricorrente in `06_exam_patterns/`
4. Catalogo esercizio in `03_exercise_catalog/`
5. Trascrizione appello in `02_transcriptions/`
6. Teoria generale in `05_theory/`

## Regole

- Non inventare metodi non presenti nella KB.
- Non usare file con `status: draft` se esiste un metodo specifico `complete`.
- Se un file contiene warning, riporta internamente il warning e usa la variante piu prudente.
- Se non trovi un metodo collegato, rispondi con un template generale ma considera la soluzione ricostruita da pattern, non da esempio identico.
- Non dare spiegazioni lunghe: durante l'esame servono formule, pseudocodice, complessita e breve correttezza.
- Se ci sono piu varianti possibili, scegli quella piu simile agli appelli gia catalogati.
