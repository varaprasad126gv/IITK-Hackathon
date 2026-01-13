"""Test script for the narrative consistency pipeline"""

def test_imports():
    """Test that all modules can be imported"""
    try:
        from main import narrative_consistency_pipeline
        from scoring import compute_score, generate_report
        from judge import judge
        from agents import run_agents
        from utils import preprocess_and_chunk, extract_entities
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_preprocessing():
    """Test text preprocessing"""
    try:
        from utils import preprocess_and_chunk
        text = "This is sentence one. This is sentence two. This is sentence three."
        chunks = preprocess_and_chunk(text, max_chunk_size=2)
        print(f"✅ Preprocessing successful: {len(chunks)} chunks created")
        return True
    except Exception as e:
        print(f"❌ Preprocessing error: {e}")
        return False

def test_scoring():
    """Test scoring function"""
    try:
        from scoring import compute_score
        
        # Test inconsistent verdict
        verdict1 = {"verdict": "Inconsistent", "confidence": 0.8}
        score1 = compute_score(verdict1)
        print(f"✅ Inconsistent score: {score1}")
        
        # Test predictive verdict
        verdict2 = {"verdict": "Predictive", "confidence": 0.9}
        score2 = compute_score(verdict2)
        print(f"✅ Predictive score: {score2}")
        
        # Test consistent verdict
        verdict3 = {"verdict": "Consistent", "confidence": 0.95}
        score3 = compute_score(verdict3)
        print(f"✅ Consistent score: {score3}")
        
        return True
    except Exception as e:
        print(f"❌ Scoring error: {e}")
        return False

def test_judge():
    """Test judge function"""
    try:
        from judge import judge
        
        agent_results = [
            {"verdict": "Correct", "confidence": 0.9, "claim": "Test claim 1", "type": "Fact"},
            {"verdict": "Correct", "confidence": 0.85, "claim": "Test claim 2", "type": "Fact"}
        ]
        
        verdict = judge(agent_results)
        print(f"✅ Judge verdict: {verdict}")
        return True
    except Exception as e:
        print(f"❌ Judge error: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    import os
    
    required_files = [
        "agents",
        "data",
        "app.py",
        "main.py",
        "judge.py",
        "scoring.py",
        "requirements.txt",
        "Dockerfile",
        ".dockerignore"
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            all_exist = False
    
    return all_exist

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Multi-Agent Debate System")
    print("=" * 50)
    
    print("\n1. Testing File Structure:")
    test_file_structure()
    
    print("\n2. Testing Imports:")
    test_imports()
    
    print("\n3. Testing Preprocessing:")
    test_preprocessing()
    
    print("\n4. Testing Scoring:")
    test_scoring()
    
    print("\n5. Testing Judge:")
    test_judge()
    
    print("\n" + "=" * 50)
    print("Testing Complete!")
    print("=" * 50)
