# infrastructure/test_db.py
from audit_db import init_db, get_session, create_audit_record, AuditRecord
from sqlalchemy.orm import sessionmaker
import os
import json

def run_test():
    engine = init_db("sqlite:///./audit.db")
    session = get_session(engine)
    sample_results = {
        "nlp": "nlp_auditor: token_count=25",
        "privacy": "privacy_agent: found_pii=True",
        "bias": "bias_agent: flagged=True",
        "security": "security_agent: insecure=True",
        "report": {"report_time": "2025-11-18T07:20:39Z", "summary": "Report received"}
    }
    rec_id = create_audit_record(session, source="demo_orchestrator", input_text="sample input", results=sample_results, risk_score=5)
    print("Inserted audit record id:", rec_id)
    # print count
    count = session.query(AuditRecord).count()
    print("Total audit records:", count)

if __name__ == "__main__":
    run_test()
