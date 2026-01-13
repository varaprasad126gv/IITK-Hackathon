def compute_score(verdict):
    if verdict["verdict"] == "Inconsistent":
        return int(100 * (1 - verdict["confidence"]))

    if verdict["verdict"] == "Predictive":
        return 70

    return 95


def generate_report(pipeline_id, score, verdict, processing_time):
    """Generate a comprehensive report of the analysis"""
    return {
        "pipeline_id": pipeline_id,
        "score": score,
        "verdict": verdict,
        "processing_time": processing_time
    }
