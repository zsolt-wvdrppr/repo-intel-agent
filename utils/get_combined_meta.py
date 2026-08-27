from pathlib import Path
import subprocess
import json

def get_combined_meta(path: str, keys: list, repos : list = []):
    try:
        repo_root = Path(__file__).resolve().parent.parent
        files_raw = subprocess.run(
            ["ls", str(f"{repo_root}/{path.lstrip("/")}")],
            capture_output=True,
            text=True
        )

        files = files_raw.stdout.splitlines()

        if len(files) == 0:
            raise Exception("No metadata found, suggest to run a scan first, and make sure to use the right path.")

        meta_path_list = []

        # Gather required metadata files only and add their path to list
        for file in files:
            if len(repos) > 0 and file.split(".")[0] in repos:
                meta_path_list.append(Path(f"{repo_root}/{path.lstrip("/")}/{file}"))
            elif len(repos) == 0:
                meta_path_list.append(Path(f"{repo_root}/{path.lstrip("/")}/{file}"))

        output = {}

        # Gather required key value pairs only and combine them into final dictionary
        for meta in meta_path_list:
            with open(meta, "r") as f:
                data = json.load(f)
      
                for entry in data:
                    if entry in keys:
                        # {repo_name: entry_name: value(s)}
                        output.update({data["name"]: {entry: data[entry]}})

        return output

    except Exception as e:
        return {"error": e}