# AI Context - APA Knowledge Base

## Project Goal

The goal is to build an Obsidian-compatible Markdown knowledge base for the university exam "Analisi e Progettazione di Algoritmi".

The student does not plan to watch all lectures. The study strategy is based on:

- past exams;
- handwritten iPad notes from a student who already passed the exam;
- recurring exercise patterns;
- operational solution methods;
- theory questions that frequently appear in exams.

## Source Types

1. Clean past exams, without execution or official solutions.
2. Handwritten PDF notes from a student.
3. Future manually added interpretations and solved examples.

## Main Task

Transform raw sources into a structured knowledge base:

- catalog known exercises;
- identify recurring exercise families;
- document variations between exams;
- extract theory requirements;
- create practical methods for solving each exercise type.

## Style Rules

- Markdown must be Obsidian-compatible.
- Use Obsidian callouts such as `[!Info]`, `[!Question]`, `[!Warning]`, `[!Todo]`, `[!Summary]`.
- Use internal links with `[[Nome Nota]]`.
- Use consistent tags.
- Use LaTeX for math.
- Never mix raw source material with processed notes.
- Always preserve references to the original source.
- Use clear and concise Italian for study notes.

## Current Priority

Complete the PDF ingestion setup, then process sources one by one through ingestion reports.

## PDF Ingestion Workflow

The repository uses a staged ingestion workflow.

ChatGPT or another AI may analyze one PDF at a time and produce an ingestion report file inside `09_ingestion_reports/`.

Codex should then apply that report to the knowledge base by creating or updating:

- exercise notes;
- method notes;
- theory notes;
- exam pattern notes;
- solved examples;
- indexes;
- project status files.

Codex should not independently interpret handwritten PDFs unless explicitly instructed. Its main role is to apply structured ingestion reports.

## Ingestion Rules

- Every source must have a stable Source ID in `01_sources/source_inventory.md`.
- Every ingestion report must reference one or more Source IDs.
- Every exercise, method, theory note or pattern created from a PDF must preserve the source reference.
- Ambiguous interpretation must be marked with `[!Warning]`.
- Do not invent missing steps, solutions or theory.
- If an instruction in an ingestion report is unclear, create a TODO entry instead of guessing.

## Standard Chain

```txt
Appello -> Esercizio -> Pattern -> Metodo -> Teoria -> Esempio svolto -> Errori comuni
```
