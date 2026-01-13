def judge(agent_results, confidence_threshold=0.7):
    """
    Judge function that evaluates agent results and produces a final verdict.
    
    Handles two input formats:
    1. Results with 'issues' field (from debate_manager)
    2. Results with 'verdict', 'confidence', 'claim', 'type' fields (from agents)
    """
    issues = []
    min_confidence = 1.0
    verdict = "Consistent"
    
    for r in agent_results:
        # Handle format 1: results with 'issues' field
        if "issues" in r:
            issues.extend(r.get("issues", []))
            min_confidence = min(min_confidence, r.get("confidence", 1.0))
        
        # Handle format 2: results with 'verdict' field
        elif "verdict" in r:
            min_confidence = min(min_confidence, r.get("confidence", 1.0))
            
            if r["verdict"] in ["Incorrect"]:
                verdict = "Inconsistent"
                issues.append(r.get("claim", "Unknown claim"))
            
            if r.get("type") == "Future Prediction":
                verdict = "Predictive"
    
    return {
        "verdict": verdict,
        "confidence": round(min_confidence, 2),
        "issues": issues
    }
