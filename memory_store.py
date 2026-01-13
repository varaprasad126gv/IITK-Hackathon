import json
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")

def load_memory():
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text())
    return []

def save_fact(text):
    memory = load_memory()
    if text not in memory:
        memory.append(text)
        MEMORY_FILE.write_text(json.dumps(memory, indent=2))