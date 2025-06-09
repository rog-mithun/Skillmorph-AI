import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = "rog-mithun"  # Optional, for authenticated user

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_github_stats():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url, headers=headers)
    repos = response.json()
    languages = set()
    repo_count = len(repos)
    for repo in repos:
        if repo.get("language"):
            languages.add(repo["language"])
    return {
        "total_repos": repo_count,
        "languages": list(languages)
    }

def get_public_github_stats(username):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    headers = {"Accept": "application/vnd.github.v3+json"}

    user_res = requests.get(user_url, headers=headers)
    repos_res = requests.get(repos_url, headers=headers)

    user_data = user_res.json()
    repos = repos_res.json()


    languages = set()
    repo_count = len(repos)
    for repo in repos:
        if repo.get("language"):
            languages.add(repo["language"])

    return {
        "username": user_data.get("login", username),
        "total_repos": repo_count,
        "languages": list(languages)
    }

