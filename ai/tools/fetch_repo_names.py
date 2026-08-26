from langchain.tools import tool
from pathlib import Path
import subprocess

@tool
def fetch_repo_names():
    """Get available repository or repo names."""

    meta_files_path = Path("././json_outputs")

    try:
        result = subprocess.run(
            ["ls", str(meta_files_path)],
            capture_output=True,
            text=True
        )

        if result.returncode !=0:
            raise Exception(result.returncode, result.args)

        arr_of_files = result.stdout.splitlines()

        repo_names = []

        for file_name_with_ext in arr_of_files:
            file_name = file_name_with_ext.split(".")[0]
            repo_names.append(file_name)

    except Exception as e:
        return f"Error running command: {e}"

    return repo_names