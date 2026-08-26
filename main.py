import argparse
from modes.scan import scan_repositories

print("\n\n*** START ***")

parser = argparse.ArgumentParser(description="This is a Repository Intelligence Agent. It can analyse multiple repositories and provide insights about them.")
parser.add_argument("mode", choices=["scan", "analyse"], help="Mode of operation: 'scan' to scan repositories, 'analyse' to analyse scanned data.")
parser.add_argument("path", type=str, help="Path to the repository folder to analyze")

args = parser.parse_args()

print(f"*** Mode: {args.mode} ***\n")

if args.mode == "scan":
    print(f"Scanning for repositories in: {args.path}\n")
    scan_repositories(args.path)


