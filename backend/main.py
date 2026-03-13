from fastapi import FastAPI
from github_loader import get_repo_files
from repo_parser import extract_code

app = FastAPI()


@app.get("/repo")

def load_repo(repo_url: str):

    files = get_repo_files(repo_url)

    code_files = extract_code(files)

    return {
        "total_files": len(files),
        "code_files": len(code_files)
    }