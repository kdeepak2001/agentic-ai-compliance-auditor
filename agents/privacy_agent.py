from google.agents.core import Agent, Message

class PrivacyAgent(Agent):
    def __init__(self):
        super().__init__()

    async def on_message(self, message: Message) -> str:
        # Placeholder privacy check: will later include regex + model-based PII detection
        text = message.text or ""
        found_pii = False
        # trivial heuristic: presence of "@" indicates an email -> PII
        if "@" in text:
            found_pii = True
        return f"privacy_agent: found_pii={found_pii}"
