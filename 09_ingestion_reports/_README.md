# Ingestion Reports

> [!Info]
> Questa cartella contiene report intermedi generati dopo l'analisi di uno o piu PDF sorgente.
>
> I report non sono note finali di studio: sono istruzioni operative per trasformare le informazioni lette nei PDF in modifiche ordinate alla knowledge base.

## Scopo

Un ingestion report serve a dire a Codex:

- quali esercizi creare;
- quali metodi creare o aggiornare;
- quali note teoriche creare o aggiornare;
- quali pattern d'esame aggiungere;
- quali indici aggiornare;
- quali dubbi lasciare aperti.

## Workflow

```txt
PDF sorgente
    ->
analisi da parte di ChatGPT
    ->
creazione ingestion report
    ->
Codex applica il report
    ->
knowledge base aggiornata
```

## Regole

- Non inserire qui PDF originali.
- Non usare questi report come note finali di studio.
- Ogni report deve indicare chiaramente la fonte analizzata.
- Ogni report deve collegarsi a uno o piu Source ID presenti in `01_sources/source_inventory.md`.
- Se una parte del PDF non e chiara, segnalarla con `[!Warning]`.
- Codex deve applicare solo istruzioni esplicite e non inventare contenuti mancanti.

## Naming

Usare nomi stabili:

```txt
ingestion_SRC-EXAM-001.md
ingestion_SRC-NOTE-001.md
ingestion_batch_appelli_2025.md
```

## Report extra

- [[ingestion_report_extra_esercizi_APA_SRC_EXTRA_001]]
- [[ingestion_report_note_analisi_e_progettazione_algoritmi]]
