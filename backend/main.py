from fastapi import FastAPI
from github_loader import get_repo_files
from repo_filter import filter_files
from repo_parser import extract_code
from code_splitter import split_code
from embeddings import create_embedding_model

app = FastAPI()


@app.get("/repo")
def load_repo(repo_url: str):

    files = get_repo_files(repo_url)

    filtered = filter_files(files)

    code_files = extract_code(filtered)

    chunks = split_code(code_files)

    model = create_embedding_model()

    if not chunks:
        return {
            "error": "No code chunks found",
            "total_files": len(files),  
            "filtered_files": len(filtered),
            "code_files": len(code_files)
        }

    vector = model.encode(chunks[0]["content"])

    return {
        "chunks": len(chunks),
        "vector_size": len(vector)
    }