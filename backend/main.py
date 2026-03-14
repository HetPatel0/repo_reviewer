from fastapi import FastAPI
from github_loader import get_repo_files
from repo_filter import filter_files
from repo_parser import extract_code
from code_splitter import split_code

app = FastAPI()


@app.get("/repo")
def load_repo(repo_url: str):

    files = get_repo_files(repo_url)

    filtered = filter_files(files)

    code_files = extract_code(filtered)

    chunks = split_code(code_files)

    return {
        "total_files": len(files),
        "code_files": len(code_files),
        "chunks": len(chunks)
    }