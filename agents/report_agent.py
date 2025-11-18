# agents/report_agent.py
import json
from datetime import datetime

class ReportAgent:
    def __init__(self):
        pass

    async def on_message(self, message: str) -> str:
        timestamp = datetime.utcnow().isoformat() + "Z"
        summary = f"Report received length={len((message or '').strip())}"
        return json.dumps({"report_time": timestamp, "summary": summary})
