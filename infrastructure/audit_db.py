# infrastructure/audit_db.py
from sqlalchemy import (
    create_engine, Column, String, Integer, DateTime, Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import uuid
import json

Base = declarative_base()

class AuditRecord(Base):
    __tablename__ = "audit_records"
    id = Column(String(36), primary_key=True)  # UUID
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    source = Column(String(128), nullable=False)
    input_text = Column(Text, nullable=False)
    results_json = Column(Text, nullable=False)
    risk_score = Column(Integer, nullable=True)

def get_engine(db_path: str = "sqlite:///./audit.db"):
    return create_engine(db_path, connect_args={"check_same_thread": False})

def init_db(db_path: str = "sqlite:///./audit.db"):
    engine = get_engine(db_path)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

def create_audit_record(session, source: str, input_text: str, results: dict, risk_score: int = None):
    rec = AuditRecord(
        id=str(uuid.uuid4()),
        timestamp=datetime.utcnow(),
        source=source,
        input_text=input_text,
        results_json=json.dumps(results),
        risk_score=risk_score
    )
    session.add(rec)
    session.commit()
    return rec.id
