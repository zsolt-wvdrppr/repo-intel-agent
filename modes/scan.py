from pathlib import Path
from utils.get_langs_and_lines import get_langs
from utils.get_num_of_last_30_days_commits import get_num_of_last_30_days_commits
from utils.get_top_authors import get_top_authors
import json

SKIP_DIR_PARTS = {
    "node_modules", "vendor", "dist", "build", ".venv", "venv",
    "target", ".git", "__pycache__", "coverage", ".next", ".tox",
}

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

        if item.is_dir() and item.name not in SKIP_DIR_PARTS:
            # Recursively scan subdirectories
            repo_content = list(item.iterdir())
            repo_path = str(item.resolve())

            # Check if it contains .git directory to identify it as a repository
            if any(sub_item.name == '.git' for sub_item in repo_content):
                repo_details["name"] = item.name
                repo_details["path"] = repo_path
                repo_langs = get_langs(repo_path)
                repo_details["language"] = repo_langs["languages"]
                repo_details["loc_total"] = repo_langs["loc_total"]
                repo_details["commits_last_30_days"] = get_num_of_last_30_days_commits(repo_path)
                repo_details["top_authors"] = get_top_authors(repo_path)

                print(f"Repository details: {json.dumps(repo_details, indent=4)}")