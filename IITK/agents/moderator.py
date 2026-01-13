from agents.agent_base import Agent

class Moderator(Agent):
    def __init__(self):
        super().__init__("Moderator")

    def respond(self, claims, facts, contradictions):
        report = {
            "total_claims": len(claims),
            "verified_claims": facts,
            "contradictions_found": contradictions,
            "consistency_score": max(0, 100 - (len(contradictions) * 20))
        }
        return report