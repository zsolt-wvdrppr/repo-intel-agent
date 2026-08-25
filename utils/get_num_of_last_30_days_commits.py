from utils.git import git

def get_num_of_last_30_days_commits(repo_path):
    result = git(repo_path, "rev-list", "--count", "--since=30.days", "--all")
    return int(result.strip())