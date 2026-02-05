import json
from datetime import datetime

def log_event(event, metadata, path="audit/sample_audit_log.json"):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event,
        "metadata": metadata
    }
    with open(path, "a") as f:
        f.write(json.dumps(log) + "\n")
