def judge(debated_results, confidence_threshold=0.7):
    # Check for issues in debated_results
    has_issues = any(agent.get("issues") for agent in debated_results if isinstance(agent, dict))
    verdict = "Inconsistent" if has_issues else "Consistent"
    confidence = 0.9 if has_issues else 0.8
    issues = []
    for agent in debated_results:
        if isinstance(agent, dict) and agent.get("issues"):
            issues.extend(agent["issues"])
    return {"verdict": verdict, "confidence": confidence, "issues": issues}

def compute_score(verdict):
    if verdict.get("issues"):
        return max(20, 100 - len(verdict["issues"]) * 25)
    return 95


def generate_report(pipeline_id, score, verdict, processing_time):
    return {
        "pipeline_id": pipeline_id,
        "score": score,
        "verdict": verdict,
        "processing_time": processing_time
    }