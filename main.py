import argparse
from modes.scan import scan_repositories
from modes.ask import ask

parser = argparse.ArgumentParser(description="This is a Repository Intelligence Agent. It can analyse multiple repositories and provide insights about them.")
parser.add_argument("mode", choices=["scan", "ask"], help="Mode of operation: 'scan' to scan repositories, 'ask' to ask for insights.")
parser.add_argument("path", type=str, help="Path to the parent folder.")
parser.add_argument("question", nargs="?", type=str, help="Question about insights.", default="")

args = parser.parse_args()

print(f"\n*** Mode selected: {args.mode} ***")

if args.mode == "scan":
    print(f"\nScanning for repositories in: {args.path}\n")
    scan_repositories(parent_path=args.path)

if args.mode == "ask":
    print(f"\n\n{ask(args)}\n\n")


