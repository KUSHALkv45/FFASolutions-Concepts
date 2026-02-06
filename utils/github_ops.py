from github import Github
import base64
import streamlit as st

g = Github(st.secrets["GITHUB_TOKEN"])
repo = g.get_repo(st.secrets["REPO_NAME"])
BRANCH = "main"


def list_dir(path):
    try:
        return repo.get_contents(path)
    except:
        return []


def read_file(path):
    f = repo.get_contents(path)
    return base64.b64decode(f.content).decode("utf-8"), f.sha


def ensure_dir(path):
    """
    Ensure a directory exists by creating a .gitkeep if needed
    """
    try:
        repo.get_contents(path)
    except:
        repo.create_file(
            f"{path}/.gitkeep",
            f"Create directory {path}",
            "",
            branch=BRANCH,
        )


def create_file(path, content, msg):
    # ensure all parent dirs exist
    parts = path.split("/")[:-1]
    cur = ""
    for p in parts:
        cur = f"{cur}/{p}" if cur else p
        ensure_dir(cur)

    repo.create_file(path, msg, content, branch=BRANCH)


def update_file(path, content, sha, msg):
    repo.update_file(path, msg, content, sha, branch=BRANCH)


def delete_file(path, sha, msg):
    repo.delete_file(path, msg, sha, branch=BRANCH)
