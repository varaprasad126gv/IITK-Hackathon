from openai import OpenAI
from memory_store import load_memory, save_fact

client = OpenAI(api_key="YOUR_API_KEY_HERE")

SYSTEM_PROMPT = """
You are a fact-checking and prediction system.

Classify each statement as:
- Correct
- Incorrect
- Opinion
- Future Prediction

Return confidence between 0 and 1.
"""

def analyze_claims(claims):
    memory = load_memory()
    results = []

    for claim in claims:
        context = "\n".join(memory[-5:])  # last 5 memories

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "system", "content": f"Known facts:\n{context}"},
                {"role": "user", "content": claim}
            ]
        )

        output = response.choices[0].message.content

        if "Correct" in output:
            save_fact(claim)

        results.append({
            "claim": claim,
            "analysis": output
        })

    return results