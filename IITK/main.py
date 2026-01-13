from datetime import datetime
from uuid import uuid4

# Assuming these modules will be created or exist in utils/agents
from utils import preprocess_and_chunk, extract_entities
from agents import run_agents
from debate_manager import debate

from judge import judge
from scoring import compute_score, generate_report

def narrative_consistency_pipeline(text, config=None):
    """
    End-to-end narrative consistency checking pipeline
    """
    if config is None:
        config = {}

    pipeline_id = str(uuid4())
    start_time = datetime.utcnow()

    # 1. Preprocessing
    chunks = preprocess_and_chunk(
        text,
        max_chunk_size=config.get("max_chunk_size", 5)
    )

    # 2. Entity Extraction
    entities = extract_entities(chunks)

    # 3. Multi-Agent Analysis
    agent_outputs = run_agents(
        chunks=chunks,
        entities=entities,
        agents=config.get("agents")
    )

    # 4. Debate Phase
    debated_results = debate(
        agent_outputs,
        min_agreement=config.get("min_agreement", 0.6)
    )

    # 5. Final Judgment
    final_verdict = judge(
        debated_results,
        confidence_threshold=config.get("confidence_threshold", 0.7)
    )

    # 6. Scoring
    score = compute_score(final_verdict)

    # 7. Report Generation
    report = generate_report(
        pipeline_id=pipeline_id,
        score=score,
        verdict=final_verdict,
        processing_time=str(datetime.utcnow() - start_time)
    )

    return report