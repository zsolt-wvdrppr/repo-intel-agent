import subprocess


def git(repo_path, *args):
    # Run a git command against repo_path and return stdout (stripped).
    try:
        result = subprocess.run(
        ["git", "-C", str(repo_path)] + list(args),
        capture_output=True,
        text=True,
        )

        if result.returncode != 0:
            raise Exception(result.returncode, result.args)

        return result.stdout

    except Exception as e:
        print(f"\n\nError running git command: {e}\n\n")
