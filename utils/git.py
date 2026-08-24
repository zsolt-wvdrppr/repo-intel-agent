import subprocess


def git(repo_path, *args, check=True):
    # Run a git command against repo_path and return stdout (stripped).
    result = subprocess.run(
        ["git", "-C", str(repo_path)] + list(args),
        capture_output=True,
        text=True,
    )

    return result.stdout
