from agents.agent_base import Agent

class FactChecker(Agent):
    def __init__(self):
        super().__init__("Fact Checker")

    def respond(self, claims):
        verified = []
        for claim in claims:
            if "always" in claim.lower() or "never" in claim.lower():
                verified.append((claim, "Suspicious"))
            else:
                verified.append((claim, "Likely True"))
        return verified