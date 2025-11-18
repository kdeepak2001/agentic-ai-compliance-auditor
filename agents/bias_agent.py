# agents/bias_agent.py
class BiasAgent:
    def __init__(self):
        pass

    async def on_message(self, message: str) -> str:
        text = message or ""
        flagged = "prefer" in text.lower()
        return f"bias_agent: flagged={flagged}"
