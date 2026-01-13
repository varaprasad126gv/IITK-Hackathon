KNOWN_FACTS = {
    "modi is the prime minister of india": "True",
    "rishi sunak is the prime minister of uk": "True"
}


def fact_check(sentences):
    issues = []

    for s in sentences:
        key = s.lower().strip()
        if "prime minister" in key:
            if key not in KNOWN_FACTS:
                issues.append(f"Fact-check failed: '{s}'")

    return issues