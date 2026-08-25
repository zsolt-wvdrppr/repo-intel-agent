import subprocess
import json
from unittest import result

def get_langs(repo_path):
    result = subprocess.run(
        ["cloc", repo_path, "--json"],
        capture_output=True, text=True, check=True
    )

    data = json.loads(result.stdout)
    data.pop("header", None)

    output = {
        "languages": {},
        "loc_total": 0
    }

    for lang, stats in data.items():
        output["languages"][lang] = stats.get("code")
        output["loc_total"] += stats.get("code", 0)

    return output
