def compute_score(verdict):
    if verdict["verdict"] == "Inconsistent":
        return int(100 * (1 - verdict["confidence"]))

    if verdict["verdict"] == "Predictive":
        return 70

    return 95