# orchestrator/orchestrator.py
import asyncio
import json

# import the lightweight agent classes
from agents.nlp_auditor import NLPAuditorAgent
from agents.privacy_agent import PrivacyAgent
from agents.bias_agent import BiasAgent
from agents.security_agent import SecurityAgent
from agents.report_agent import ReportAgent

class ComplianceOrchestrator:
    """
    Local orchestrator using plain async agent classes (no ADK).
    Each agent exposes async on_message(message: str) -> str
    """

    def __init__(self):
        self.agents = {
            "nlp": NLPAuditorAgent(),
            "privacy": PrivacyAgent(),
            "bias": BiasAgent(),
            "security": SecurityAgent(),
            "report": ReportAgent(),
        }

    async def dispatch(self, text: str) -> dict:
        async def call_agent(name: str, agent):
            try:
                result = await agent.on_message(text)
            except Exception as e:
                result = f"ERROR: {e}"
            return name, result

        tasks = [call_agent(name, agent) for name, agent in self.agents.items()]
        pairs = await asyncio.gather(*tasks)
        return {name: res for name, res in pairs}

async def demo_run():
    orch = ComplianceOrchestrator()
    test_text = (
        "Hello team,\n"
        "Please review the attached policy update. Contact me at dev@example.com.\n"
        "Note: we prefer internal candidates and do not share the password here.\n"
        "Thanks."
    )
    print("Dispatching test message to agents...\n")
    results = await orch.dispatch(test_text)
    print("Aggregated results:\n")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    asyncio.run(demo_run())
