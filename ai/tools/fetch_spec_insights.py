from langchain.tools import tool
from pathlib import Path
from utils.get_combined_meta import get_combined_meta

@tool
def fetch_spec_insights(path: str, keys: list, repos: list = []):
    """Get specific details from all repository
    
    Args:
        path: Path to metadata

        keys: A list of keys to retrieve their values from metadata. Adjust the required key to the the information the user requested. The available keys are the following:

            - name: Name of the repository,
            - path: Path to the repository,
            - languages: The languages used in the repository along with the line of codes of each language,
            - loc_total: Total amount of line of code in the repository,
            - commits_last_30_days: Number of commits in the last 30 days,
            - top_authors: Names of the top 3 authors who made the most commit,
            - has_readme: The value is "true" if it has a README file or False if not,
            - has_tests: The value is "true" if it has TEST or False if it doesn't,
            - has_ci: The value is "true" if it has CI/CD or False if doesn't,
            - has_dockerfile: The value is "true" if it has a Dockerfile or False if it does not.

        repos: A list of the specified repos to look into. By default if this arg is not defined it looks into all repos. If repo name is specified by user, must validate correct names using the fetch_repo_names tool. If there's a typo in the user prompt, DO correct it based on available repos, and MUST make a note of it in your response!
    """

    return get_combined_meta(path, keys, repos)



