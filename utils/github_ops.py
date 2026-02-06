"""GitHub operations module for managing repository files and directories."""

import base64
import streamlit as st
from github import Github
from github.GithubException import GithubException

# Initialize GitHub client
g = Github(st.secrets["GITHUB_TOKEN"])
repo = g.get_repo(st.secrets["REPO_NAME"])
BRANCH = "main"


def list_dir(path):
    """
    List contents of a directory in the GitHub repository.
    
    Args:
        path: Directory path in the repository
        
    Returns:
        List of file/directory objects, or empty list if path doesn't exist
    """
    try:
        return repo.get_contents(path, ref=BRANCH)
    except GithubException:
        return []


def read_file(path):
    """
    Read a file from the GitHub repository.
    
    Args:
        path: File path in the repository
        
    Returns:
        Tuple of (decoded_content, sha)
        
    Raises:
        GithubException: If file doesn't exist or can't be read
    """
    file_obj = repo.get_contents(path, ref=BRANCH)
    content = base64.b64decode(file_obj.content).decode("utf-8")
    return content, file_obj.sha


def ensure_dir(path):
    """
    Ensure a directory exists in GitHub repository.
    Creates directory with .gitkeep file if it doesn't exist.
    
    Args:
        path: Directory path to ensure exists
        
    Raises:
        GithubException: For errors other than 404
    """
    try:
        repo.get_contents(path, ref=BRANCH)
        # Directory exists, nothing to do
    except GithubException as e:
        if e.status == 404:
            # Directory doesn't exist - create it with .gitkeep
            repo.create_file(
                f"{path}/.gitkeep",
                f"Create directory {path}",
                "",
                branch=BRANCH,
            )
        else:
            raise


def create_file(path, content, msg):
    """
    Create a new file in the GitHub repository.
    Automatically creates parent directories if they don't exist.
    
    Args:
        path: File path to create
        content: File content
        msg: Commit message
        
    Raises:
        GithubException: If file already exists or other GitHub error
    """
    # Ensure all parent directories exist
    parts = path.split("/")[:-1]
    current_path = ""
    for part in parts:
        current_path = f"{current_path}/{part}" if current_path else part
        ensure_dir(current_path)
    
    # Create the file
    repo.create_file(path, msg, content, branch=BRANCH)


def update_file(path, content, sha, msg):
    """
    Update an existing file in the GitHub repository.
    
    Args:
        path: File path to update
        content: New file content
        sha: Current file SHA (for conflict detection)
        msg: Commit message
        
    Raises:
        GithubException: If SHA mismatch or other GitHub error
    """
    repo.update_file(path, msg, content, sha, branch=BRANCH)


def delete_file(path, sha, msg):
    """
    Delete a file from the GitHub repository.
    
    Args:
        path: File path to delete
        sha: Current file SHA (for conflict detection)
        msg: Commit message
        
    Raises:
        GithubException: If SHA mismatch or other GitHub error
    """
    repo.delete_file(path, msg, sha, branch=BRANCH)
