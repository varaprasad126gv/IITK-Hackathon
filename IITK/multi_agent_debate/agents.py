def run_agents(chunks, entities):
    issues = []

    flat_sentences = []
    for chunk in chunks:
        flat_sentences.extend(chunk)

    normalized = [s.lower().strip(".") for s in flat_sentences]

    for s in normalized:
        if " not " in s:
            # Find the position of " not "
            parts = s.split(" not ")
            if len(parts) == 2:
                opposite = parts[0] + " " + parts[1]
                if opposite in normalized:
                    issues.append(f"Contradiction detected: '{opposite}' vs '{s}'")

    return [{
        "agent": "ContradictionAgent",
        "issues": issues,
        "confidence": 0.9 if issues else 0.8
    }]