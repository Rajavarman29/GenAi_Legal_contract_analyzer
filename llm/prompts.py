CLAUSE_EXPLANATION_PROMPT = """
Explain the following contract clause in simple business English.
Clause:
{clause}
"""

RISK_EXPLANATION_PROMPT = """
Explain why this clause may be risky for a small business.
Clause:
{clause}
"""

REWRITE_PROMPT = """
Suggest a safer alternative wording for this clause suitable for an SME.
Clause:
{clause}
"""

SUMMARY_PROMPT = """
Summarize this contract in plain business language for an SME owner.
{text}
"""
