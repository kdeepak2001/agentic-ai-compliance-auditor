from google_adk.core import Agent, Message

class SecurityAgent(Agent):
    def __init__(self):
        super().__init__()

    async def on_message(self, message: Message) -> str:
        # Placeholder security linter: later we will check config snippets and CVE lookups
        text = message.text or ""
        # trivial heuristic: flag "password" or "secret"
        insecure = any(k in text.lower() for k in ("password", "secret", "api_key"))
        return f"security_agent: insecure={insecure}"
