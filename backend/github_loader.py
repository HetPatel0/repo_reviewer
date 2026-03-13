from github import Github
from config import GITHUB_TOKEN


g = Github(GITHUB_TOKEN)


def get_repo_files(repo_url):

    repo_name = repo_url.replace("https://github.com/", "")
    repo = g.get_repo(repo_name)

    files = []

    def fetch_contents(path=""):

        contents = repo.get_contents(path)

        for item in contents:

            if item.type == "dir":
                fetch_contents(item.path)

            else:
                files.append(item)

    fetch_contents()

    return files