# Utils package
from .preprocess import preprocess_and_chunk

def extract_entities(chunks):
    """Extract entities from chunks (placeholder implementation)"""
    entities = []
    for chunk in chunks:
        entities.append({"chunk": chunk, "entities": []})
    return entities

__all__ = ['preprocess_and_chunk', 'extract_entities']
