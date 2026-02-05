import re

CLAUSE_HEADER = re.compile(r"^\s*(\d+(\.\d+)*|\([a-z]\))[\.\)]?\s*(.*)$")

def extract_clauses(text):
    lines = text.splitlines()
    clauses = []

    current_clause = None

    for line in lines:
        header_match = CLAUSE_HEADER.match(line.strip())

        if header_match:
            if current_clause:
                clauses.append(current_clause)

            current_clause = {
                "clause_id": header_match.group(1),
                "text": header_match.group(3).strip()
            }
        else:
            if current_clause and line.strip():
                current_clause["text"] += " " + line.strip()

    if current_clause:
        clauses.append(current_clause)

    return clauses
