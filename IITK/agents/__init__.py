from .llm_agent import analyze_claims


def run_agents(chunks, entities):
    claims = []
    for chunk in chunks:
        claims.extend(chunk)

    return analyze_claims(claims)
