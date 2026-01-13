from agents.claim_extractor import ClaimExtractor
from agents.fact_checker import FactChecker
from agents.contradiction_detector import ContradictionDetector
from agents.moderator import Moderator

class DebateManager:
    def __init__(self):
        self.extractor = ClaimExtractor()
        self.checker = FactChecker()
        self.detector = ContradictionDetector()
        self.moderator = Moderator()

    def run(self, text):
        claims = self.extractor.respond(text)
        facts = self.checker.respond(claims)
        contradictions = self.detector.respond(claims)
        final_report = self.moderator.respond(claims, facts, contradictions)
        return final_report

def debate(agent_outputs, min_agreement=0.6):
    # Placeholder debate function
    # For now, just return the agent_outputs as debated_results
    return agent_outputs