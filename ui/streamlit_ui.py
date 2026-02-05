import streamlit as st
import tempfile
import os

from core.file_loader import load_file
from core.language_detector import detect_language
from core.hindi_normalizer import normalize_hindi
from core.clause_extractor import extract_clauses
from core.contract_classifier import classify_contract
from core.similarity_engine import match_clause

from risk_engine.scorer import score_clause, contract_score
from audit.logger import log_event
from audit.knowledge_base import update_kb
from utils.hash_utils import hash_document

from llm.llm_client import call_llm
from llm.prompts import (
    CLAUSE_EXPLANATION_PROMPT,
    RISK_EXPLANATION_PROMPT,
    REWRITE_PROMPT,
    SUMMARY_PROMPT
)

def run_app():
    st.title("GenAI Legal Contract Analyzer (SME Edition)")

    uploaded = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

    if uploaded:
        suffix = os.path.splitext(uploaded.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded.read())
            temp_path = tmp.name

        raw_text = load_file(temp_path)
        lang = detect_language(raw_text)

        text = normalize_hindi(raw_text) if lang == "hi" else raw_text

        doc_hash = hash_document(text)
        log_event("DOCUMENT_UPLOADED", {"document_hash": doc_hash})

        contract_type = classify_contract(text)
        clauses = extract_clauses(text)

        st.subheader(f"Contract Type: {contract_type}")

        scores = []

        for c in clauses:
            level, score, flags = score_clause(c["text"])
            scores.append(score)
            update_kb(flags)

            color = {"Low": "green", "Medium": "orange", "High": "red"}[level]
            st.markdown(f"**Clause {c['clause_id']}** : :{color}[{level}]")

            with st.expander("Details"):
                st.write(c["text"])

                explanation = call_llm(
                    CLAUSE_EXPLANATION_PROMPT.format(clause=c["text"])
                )
                risk_reason = call_llm(
                    RISK_EXPLANATION_PROMPT.format(clause=c["text"])
                )
                rewrite = call_llm(
                    REWRITE_PROMPT.format(clause=c["text"])
                )

                st.write("Explanation:", explanation)
                st.write("Why risky:", risk_reason)
                st.write("Safer alternative:", rewrite)
                st.write("Flags:", flags)

        overall = contract_score(scores)
        st.metric("Overall Risk Score", overall)

        summary = call_llm(
            SUMMARY_PROMPT.format(text=text[:4000])
        )

        st.subheader("Contract Summary")
        st.write(summary)

        log_event(
            "ANALYSIS_COMPLETED",
            {
                "document_hash": doc_hash,
                "contract_type": contract_type,
                "clause_count": len(clauses),
                "risk_score": overall
            }
        )
