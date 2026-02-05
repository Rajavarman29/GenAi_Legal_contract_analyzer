# GenAI Legal Contract Analyzer (SME Edition)

## 📌 Overview
This project is a GenAI-powered legal contract analysis system designed to help small and medium enterprises (SMEs) understand complex legal contracts. The system analyzes contracts clause-by-clause, identifies potential legal and commercial risks, and explains them in simple business language.

The solution is built as a **document analysis pipeline**, not a chatbot, with a strong focus on auditability, deterministic logic, and confidentiality.

---

## 🎯 Problem Statement
Small business owners often struggle to understand legal contracts due to complex language and hidden risks. This project helps SMEs by:
- Breaking contracts into clauses
- Highlighting unfavorable or risky terms
- Explaining clauses in plain English
- Suggesting safer alternative wording
- Providing an overall contract risk score

---

## 🛠️ Key Features

- Contract type classification (NDA, Employment, Vendor, Lease, Partnership)
- Clause and sub-clause extraction
- Named Entity Recognition (Parties, Dates, Amounts, Jurisdiction, Liabilities)
- Clause classification (Obligation / Right / Prohibition)
- Rule-based risk detection and scoring
- Ambiguity detection (vague legal language)
- Clause similarity matching with SME-friendly templates
- Multilingual support (English & Hindi)
- Clause-by-clause explanations using GenAI
- Suggested renegotiation alternatives
- Simplified contract summary
- PDF export for legal review
- JSON-based audit logging

---

## 🧠 Architecture Overview

The system follows a modular pipeline architecture:

1. File Ingestion (PDF / DOCX / TXT)
2. Language Detection & Normalization
3. Clause & Sub-Clause Extraction
4. Deterministic NLP & Rule-Based Risk Analysis
5. GenAI-based Explanation & Summarization
6. UI Presentation
7. Audit Logging & Export

---

## 🤖 GenAI Usage (Strictly Controlled)

Large Language Models (GPT-4 / Claude 3) are used **only** for:
- Explaining clauses in simple business language
- Explaining why a clause is risky
- Suggesting safer alternative wording
- Generating a simplified contract summary

LLMs are **not used** for:
- Parsing documents
- Risk scoring
- Clause classification
- Legal compliance checks
- Citing laws or case references

---

## 🔒 Privacy & Compliance

- Fully local-first processing
- No external legal APIs or datasets
- No cloud storage
- JSON-based audit logs
- Deterministic and explainable logic

---

## 🌐 Tech Stack

- Python
- Streamlit (UI)
- spaCy & NLTK (NLP preprocessing)
- Rule-based risk engine
- TF-IDF (clause similarity)
- Local file storage

---

## 🚀 Running the Application

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
