# Knowledge Base APA

## Scopo

Questa repository contiene la Knowledge Base Obsidian per preparare l'esame di **Analisi e Progettazione di Algoritmi** (APA). 

Obiettivi principali:
* **Studio personale** strutturato per pattern ed esercizi;
* **Risoluzione rapida degli esercizi** durante le simulazioni e lo studio;
* **Recupero immediato dei metodi** risolutivi standard;
* **Supporto RAG** (Retrieval-Augmented Generation) per assistenti AI;
* **Preparazione delle domande teoriche** aperte dell'esame.

---

## Struttura della Repository

| Cartella | Contenuto |
|---|---|
| [`01_sources/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/01_sources) | PDF originali ed inventario delle fonti (da non modificare) |
| [`04_methods/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods) | Metodi operativi standardizzati per la risoluzione degli esercizi |
| [`05_theory/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/05_theory) | Teoria compatta focalizzata sulle domande tipiche d'esame |
| [`06_exam_patterns/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/06_exam_patterns) | Pattern ricorrenti e variazioni identificate tra gli appelli |
| [`07_solved_examples/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/07_solved_examples) | Schemi d'esecuzione ed esempi svolti passo-passo |
| [`09_ingestion_reports/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/09_ingestion_reports) | Report di ingestion delle fonti e audit finale |
| [`10_rag/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/10_rag) | Entrypoint RAG, prompt da telefono, indici di ricerca e method card |
| [`AI Chat during Exam/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/AI%20Chat%20during%20Exam) | Prompt pre-configurato e sezioni per l'uso dell'AI |

---

## Come Studiare e Utilizzare la KB

1. **Punto d'Ingresso**: Partire da [`10_rag/RAG_ENTRYPOINT.md`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/10_rag/RAG_ENTRYPOINT.md) per l'interazione RAG, o da [`00_meta/STUDY_DASHBOARD.md`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/00_meta/STUDY_DASHBOARD.md) per un ripasso sistematico.
2. **Esercizi**: Usare le guide in [`04_methods/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/04_methods) per comprendere gli algoritmi operativi.
3. **Teoria**: Consultare [`05_theory/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/05_theory) per formule, definizioni e proof sketch di teoremi.
4. **Schemi d'Esame**: Riferirsi a [`07_solved_examples/`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/07_solved_examples) per vedere come strutturare la scrittura sul foglio protocollo.
5. **Retrieval Veloce**: Consultare [`10_rag/RAG_RETRIEVAL_INDEX.md`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/10_rag/RAG_RETRIEVAL_INDEX.md) per associare immediatamente una parola chiave d'esame al file corretto della repo.

---

## Gerarchia di Affidabilità delle Fonti

In caso di incongruenze, fare sempre riferimento alle fonti secondo questa priorità (si veda anche la RAG Trust Policy):
1. **PDF ufficiali del Professore** (es. lezioni e dispense caricate in `01_sources/`);
2. **Testi d'appello ufficiali** (formulazioni storiche degli esercizi);
3. **Appunti manoscritti** (interpretati con warning se ambigui);
4. **Integrazioni e inferenze Codex/AI** (da verificare).

---

## Stato del Progetto

La repo è completamente integrata e aggiornata con gli esercizi passati, le trascrizioni degli appunti manoscritti e tutte le dispense ufficiali per i blocchi di programmazione dinamica, Floyd-Warshall, matroidi, Kruskal/Prim e NP-completezza.

I risultati dettagliati del controllo di navigabilità e consistenza sono disponibili nel report:
👉 **[`09_ingestion_reports/final_repo_audit.md`](file:///c:/Users/User/Desktop/Knowledge%20Bases/knowledge_base_APA/09_ingestion_reports/final_repo_audit.md)**

---

## Regola Guida d'Esame

> [!TIP]
> **Workflow RAG**: Traccia d'esame $\to$ Retrieval Index $\to$ Method Card $\to$ Esempio Svolto $\to$ Risposta compatta da copiare.

