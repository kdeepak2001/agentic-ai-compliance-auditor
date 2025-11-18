from google_adk.core import Agent, Message
import json
from datetime import datetime

class ReportAgent(Agent):
    def __init__(self):
        super().__init__()

    async def on_message(self, message: Message) -> str:
        # Placeholder report aggregation: expects message.text to be JSON or plain text
        timestamp = datetime.utcnow().isoformat() + "Z"
        return json.dumps({
            "report_time": timestamp,
            "summary": f"Report received length={len((message.text or '').strip())}"
        })
