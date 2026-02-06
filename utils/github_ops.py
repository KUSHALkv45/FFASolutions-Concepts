from github import Github
import base64
import streamlit as st

g = Github(st.secrets["GITHUB_TOKEN"])
repo = g.get_repo(st.secrets["REPO_NAME"])

def read_file(path):
    f = repo.get_contents(path)
    return base64.b64decode(f.content).decode(), f.sha

def write_file(path, content, msg):
    repo.create_file(path, msg, content, branch="main")

def update_file(path, content, sha, msg):
    repo.update_file(path, msg, content, sha, branch="main")

def delete_path(path, sha, msg):
    repo.delete_file(path, msg, sha, branch="main")

def list_dir(path):
    try:
        return repo.get_contents(path)
    except:
        return []
