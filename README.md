# Repo Intel Agent

A Repository Intelligence Agent that analyses git repositories and reports insights such as language breakdown, lines of code, commit activity, and top contributors.

## Requirements

### Python dependencies

Install with:

```bash
pip install -r requirements.txt
```

### System dependencies

- **[cloc](https://github.com/AlDanial/cloc)** — used by [utils/get_langs.py](utils/get_langs.py) to compute per-language line counts. It's a standalone CLI tool, not a Python package, so it isn't listed in `requirements.txt`. Install it separately:

  ```bash
  brew install cloc       # macOS
  apt install cloc        # Debian/Ubuntu
  ```

  `cloc` must be available on your `PATH` for language/LOC analysis to work.

## Usage

```bash
python main.py scan <path-to-repo>
```
