import argparse
from pathlib import Path
from langchain.agents import create_agent

print("--- START ---")

parser = argparse.ArgumentParser(description="This is a Repository Intelligence Agent. It can analyse multiple repositories and provide insights about them.")
parser.add_argument("mode", choices=["scan", "analyse"], help="Mode of operation: 'scan' to scan repositories, 'analyse' to analyse scanned data.")
parser.add_argument("path", type=str, help="Path to the repository folder to analyze")

args = parser.parse_args()

print(f"Mode: {args.mode}")
print(f"Directory to scan: {args.path}")

path = Path(args.path)
if not path.exists() or not path.is_dir():
    print(f"Error: The provided path '{args.path}' does not exist or is not a directory.")
    exit(1)

print(f"Scanning directory: {list(path.iterdir())}")