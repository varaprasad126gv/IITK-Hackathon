import json
from main import narrative_consistency_pipeline

with open("data/test_cases.json") as f:
    tests = json.load(f)

correct = 0

for t in tests:
    result = narrative_consistency_pipeline(t["text"])
    verdict = result["verdict"]["verdict"]

    if t["expected"].lower() in verdict.lower():
        correct += 1

accuracy = (correct / len(tests)) * 100
print(f"Accuracy: {accuracy}%")