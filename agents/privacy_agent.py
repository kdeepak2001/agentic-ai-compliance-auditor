# agents/privacy_agent.py
class PrivacyAgent:
    def __init__(self):
        pass

    async def on_message(self, message: str) -> str:
        text = message or ""
        found_pii = "@" in text or "ssn" in text.lower()
        return f"privacy_agent: found_pii={found_pii}"
