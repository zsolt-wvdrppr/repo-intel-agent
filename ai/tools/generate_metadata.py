from modes.scan import scan_repositories
from langchain.tools import tool

@tool
def generate_metadata(path: str):
    """Identifies repositories in within provided parent directory by path parameter, and generates json metadata for each repository into the /metadata directory
    
    Args:
        path: Path to parent directory to scan
    """

    return scan_repositories(parent_path=path)