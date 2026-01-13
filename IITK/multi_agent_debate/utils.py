def preprocess_and_chunk(text, max_chunk_size=5):
    sentences = text.split('.')
    chunks = []
    chunk = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            chunk.append(sentence)
            if len(chunk) >= max_chunk_size:
                chunks.append(chunk)
                chunk = []
    if chunk:
        chunks.append(chunk)
    return chunks

def extract_entities(chunks):
    entities = []
    for chunk in chunks:
        # Simple entity extraction (placeholder)
        entities.append({"chunk": chunk, "entities": []})
    return entities