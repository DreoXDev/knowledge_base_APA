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

Initialize the repository structure, create templates, write folder README files, and define the workflow.

## Standard Chain

```txt
Appello -> Esercizio -> Pattern -> Metodo -> Teoria -> Esempio svolto -> Errori comuni
```

