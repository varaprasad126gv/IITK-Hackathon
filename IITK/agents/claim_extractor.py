from agents.agent_base import Agent

class ClaimExtractor(Agent):
    def __init__(self):
        super().__init__("Claim Extractor")

    def respond(self, text):
        sentences = text.split(".")
        claims = [s.strip() for s in sentences if len(s.strip()) > 10]
        return claims