from pathlib import Path
import subprocess
import json

def scan_repositories(path):
    path = Path(path)
    if not path.exists() or not path.is_dir():
        print(f"Error: The provided path '{path}' does not exist or is not a directory.")
        exit(1)

    root_content = list(path.iterdir())
    print(f"Scanning directory: {root_content}")

    for item in root_content:

        repo_details = {
            "name": "",
            "path": "",
            "language": {},
            "loc_total": 0,
            "commits_last_30_days": 0,
            "top_authors": [],
            "has_readme": False,
            "has_claude": False,
            "has_license": False,
            "has_tests": False,
            "has_ci": False,
            "has_dockerfile": False
            }

        if item.is_dir():
            print(f"Found directory: {item.name}")
            # Recursively scan subdirectories
            repo_content = list(item.iterdir())

            # Check if it contains .git directory to identify it as a repository
            if any(sub_item.name == '.git' for sub_item in repo_content):
                print(f"Repository found: {item.name}")
                repo_details["name"] = item.name
                repo_details["path"] = str(item.resolve())
                get_git_info(str(item.resolve()))

def get_git_info(repo_path):
    result = subprocess.run(
        ["github-linguist", repo_path, "--json"],
        capture_output=True,
        text=True
    )

    print(f"Git info result: {result.stdout}")