import os

# Define directory and file structure
structure = {
    "config": ["__init__.py", "settings.py", "logging_config.py"],
    "data/raw": [],
    "data/processed": [],
    "data/vector_store": [],
    "docs": ["setup.md", "api_reference.md"],
    "src/ingestion": ["__init__.py", "loader.py", "splitter.py", "preprocessor.py"],
    "src/retrieval": ["__init__.py", "embedder.py", "vector_db.py", "reranker.py"],
    "src/generation": ["__init__.py", "llm_client.py", "prompt_engineer.py"],
    "src/orchestration": ["__init__.py", "rag_chain.py"],
    "src/evaluation": ["__init__.py", "metrics.py", "eval_runner.py"],
    "src/api": ["__init__.py", "schemas.py", "endpoints.py"],
    "src/utils": ["__init__.py", "logger.py", "helpers.py"],
    "tests/unit": ["test_retrieval.py", "test_generation.py"],
    "tests/integration": ["test_rag_flow.py", "test_api.py"],
    "tests/fixtures/sample_docs": [],
    "scripts": ["ingest.py", "run_api.py", "evaluate.py"],
}

root_files = [
    ".env",
    "requirements.txt",
    "Dockerfile",
    "README.md"
]

# Create project structure
def create_structure():
    for path, files in structure.items():
        os.makedirs(path, exist_ok=True)
        for file in files:
            full_path = os.path.join(path, file)
            with open(full_path, 'w') as f:
                if file == "__init__.py":
                    f.write("# Package init\n")
                else:
                    f.write(f"# {file}\n")
    for file in root_files:
        with open(file, 'w') as f:
            if file == "README.md":
                f.write("# RAG Project\n\nGenerated with template.py")
            elif file == "requirements.txt":
                f.write("# Add your dependencies here\n")
            elif file == ".env":
                f.write("# Add your environment variables here\n")
            elif file == "Dockerfile":
                f.write("FROM python:3.10\n\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"python\", \"scripts/run_api.py\"]")

if __name__ == "__main__":
    create_structure()
    print("✅ Project structure created successfully.")
