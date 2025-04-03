import os
import git

def clone_repos(repo_urls, clone_dir="repos"):
    os.makedirs(clone_dir, exist_ok=True)
    for repo_url in repo_urls:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = os.path.join(clone_dir, repo_name)
        if not os.path.exists(repo_path):
            git.Repo.clone_from(repo_url, repo_path)
