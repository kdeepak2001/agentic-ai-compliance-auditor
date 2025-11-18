# agents/security_agent.py
class SecurityAgent:
    def __init__(self):
        pass

    async def on_message(self, message: str) -> str:
        text = message or ""
        insecure = any(k in text.lower() for k in ("password", "secret", "api_key"))
        return f"security_agent: insecure={insecure}"
