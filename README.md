# Repo Intel Agent

A Repository Intelligence Agent that analyses git repositories and reports insights such as language breakdown, lines of code, commit activity, and top contributors.

It's a Python CLI with two modes: `scan` and `ask`. They're linked only through JSON metadata files, though the agent in `ask` mode can also trigger a scan itself.

## Requirements

### Python dependencies

Install with:

```bash
pip install -r requirements.txt
```

### System dependencies

- **[cloc](https://github.com/AlDanial/cloc)** — used by [utils/get_langs_and_lines.py](utils/get_langs_and_lines.py) to compute per-language line counts. It's a standalone CLI tool, not a Python package, so it isn't listed in `requirements.txt`. Install it separately:

  ```bash
  brew install cloc       # macOS
  apt install cloc        # Debian/Ubuntu
  ```

  `cloc` must be available on your `PATH` for language/LOC analysis to work.

- **[Ollama](https://ollama.com)** — `ask` mode runs a local model through LangChain's `ChatOllama`, so nothing is sent externally. Make sure Ollama is installed and running with a suitable model pulled.

### Makefile

`make install` sets up a virtual environment, installs the Python requirements, and installs `cloc` if it's missing. Handy for getting a new machine ready quickly.

## Usage

### Scan mode

Walks the given folder and finds git repositories by checking for a `.git` folder (skipping a predefined list of folders to save time). For each repository it writes one JSON metadata file into `/metadata`.

```bash
python main.py scan <path-to-repos>
```

Each piece of metadata is gathered by its own utility function in `/utils`, one job per file. Most use a shared `git()` helper that runs git commands via `subprocess`. Two exceptions:

- the file checker (README, LICENSE, Dockerfile, CI, etc.), which calls `subprocess` directly and checks for each file
- the language/LOC counter, which uses `cloc` to count lines of code

### Ask mode

Ask questions about repositories that have already been scanned:

```bash
python main.py ask <metadata-path> "<question>"
```

The agent has three tools:

1. **Get repo names** — returns the repo names, mainly so the agent can confirm it has the right one
2. **Get insights** — takes the metadata path, a list of keys (`languages`, `loc_total`, `commits_last_30_days`, `top_authors`, `has_readme`, `has_tests`, `has_ci`, `has_dockerfile`), and an optional list of repos (empty means all), and returns `{repo_name: {key: value}}`
3. **Run a scan** — lets the agent generate metadata straight from `ask` mode if given a folder to scan

If you misspell a repo name, the agent finds the closest match and tells you it corrected it. This works but isn't always reliable.

## What's next

- Add a confidence score to the name-matching: above ~60%, go with it and flag the fix; below that, list the repos and let the user pick instead of guessing
- Make the file checker read a list of target files instead of hardcoding them
- Write tests for each util and tool on their own, not just through the agent
- Better error handling
- Still outstanding from the brief: Docker, YAML config
