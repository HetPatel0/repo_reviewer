IGNORED_DIRS = [
    "node_modules",
    ".git",
    "dist",
    "build",
    "__pycache__",
    "venv"
]

ALLOWED_EXTENSIONS = (
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".md",
    ".json",
    ".html",
    ".css"
)



def filter_files(files):

    filtered = []

    for file in files:

        # skip ignored directories
        if any(folder in file.path for folder in IGNORED_DIRS):
            continue

        # keep only allowed code files
        if file.name.endswith(ALLOWED_EXTENSIONS):
            filtered.append(file)

    return filtered