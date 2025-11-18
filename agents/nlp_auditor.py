# agents/nlp_auditor.py
# Lightweight local agent skeleton (no ADK dependency)
# Keeps the async on_message(interface) used by the orchestrator.

class NLPAuditorAgent:
    def __init__(self):
        pass

    async def on_message(self, message: str) -> str:
        # Placeholder NLP auditor: simple token count
        text = message or ""
        token_count = len(text.split())
        return f"nlp_auditor: token_count={token_count}"
