from google_adk.core import Agent, Message

class BiasAgent(Agent):
    def __init__(self):
        super().__init__()

    async def on_message(self, message: Message) -> str:
        # Placeholder bias detection: later we will sample and run fairness tests
        text = message.text or ""
        # trivial heuristic: flag if the word "prefer" appears
        flagged = "prefer" in text.lower()
        return f"bias_agent: flagged={flagged}"
