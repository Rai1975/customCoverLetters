# customCoverLetters
Script to automate making PDF cover letters

This is a script I use personally to create custom cover letters. Works best if you host your agents on AWS Bedrock.

This script uses:
1. AWS Strands SDK
2. AWS Bedrock
3. Beautifulsoup (Frontend scraping)
4. pdflatex as a subprocess

### General Agent Workflow

```mermaid
flowchart TD

A[Job application link provided]
B[Agent scrape application description]
C[Agent checks experiences, coursework and projects to find relevant experiences]
D[Agent generates body for cover letter]
E[Script lints and decodes latex]
F[Script applies body to latex template and renders to PDF via pdflatex]

A --> B
B --> C
C --> D
D --> E
E --> F
```