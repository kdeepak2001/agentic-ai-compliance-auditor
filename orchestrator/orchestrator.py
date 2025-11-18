# orchestrator/orchestrator.py
import asyncio
import json
from google.agents.core import Message

# import agent classes from agents package
from agents.nlp_auditor import NLPAuditorAgent
from agents.privacy_agent import PrivacyAgent
from agents.bias_agent import BiasAgent
from agents.security_agent import SecurityAgent
from agents.report_agent import ReportAgent

class ComplianceOrchestrator:
    """
    Minimal orchestrator that instantiates agents and dispatches
    incoming messages to them in parallel, then aggregates results.
    This is a local/demo friendly orchestrator (no ADK runtime started).
    """

    def __init__(self):
        # instantiate agents
        self.agents = {
            "nlp": NLPAuditorAgent(),
            "privacy": PrivacyAgent(),
            "bias": BiasAgent(),
            "security": SecurityAgent(),
            "report": ReportAgent(),
        }

    async def dispatch(self, text: str) -> dict:
        """
        Send the same message to all agents concurrently and collect responses.
        Returns a dictionary of agent_name -> response_text
        """
        msg = Message(text=text)

        async def call_agent(name: str, agent):
            try:
                result = await agent.on_message(msg)
            except Exception as e:
                result = f"ERROR: {e}"
            return name, result

        tasks = [call_agent(name, agent) for name, agent in self.agents.items()]
        pairs = await asyncio.gather(*tasks)
        return {name: res for name, res in pairs}

# Demo runner for quick local test
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
