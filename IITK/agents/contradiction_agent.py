def detect_contradictions(sentences):
    issues = []
    normalized = [s.lower().strip() for s in sentences]

    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            a = normalized[i]
            b = normalized[j]

            if a.replace(" not ", " ") == b or b.replace(" not ", " ") == a:
                issues.append(
                    f"Contradiction detected: '{sentences[i]}' vs '{sentences[j]}'"
                )

    return issues