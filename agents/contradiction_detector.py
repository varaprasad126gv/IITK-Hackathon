from agents.agent_base import Agent

class ContradictionDetector(Agent):
    def __init__(self):
        super().__init__("Contradiction Detector")

    def respond(self, claims):
        contradictions = []
        for i in range(len(claims)):
            for j in range(i + 1, len(claims)):
                if "not" in claims[i].lower() and claims[j].lower() in claims[i].lower():
                    contradictions.append((claims[i], claims[j]))
        return contradictions