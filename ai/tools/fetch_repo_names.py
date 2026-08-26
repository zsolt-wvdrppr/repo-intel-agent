from langchain.tools import tool
from pathlib import Path
import subprocess

@tool
def fetch_repo_names(path: str):
    """Get available repository or repo names.
    
    Args:
         path: Path to metadata. Must use the user provided path.
    """

    repo_root = Path(__file__).resolve().parent.parent.parent
    meta_files_path = repo_root / path.lstrip("/")


    try:
        result = subprocess.run(
            ["ls", str(meta_files_path)],
            capture_output=True,
            text=True
        )

        if result.returncode !=0:
            raise Exception(result.returncode, result.stderr)

        list_of_files = result.stdout.splitlines()

        repo_names = []

        for file_name_with_ext in list_of_files:
            file_name = file_name_with_ext.split(".")[0]
            repo_names.append(file_name)

    except Exception as e:
        return f"Error running command: {e}"

    return repo_names