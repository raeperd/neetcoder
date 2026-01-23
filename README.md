# NeetCoder

> NeetCode 150 in your local IDE. AI assistance. Autocomplete. Your notes.

## Why Local?

- **AI pair programming** - Copilot, Claude, Cursor understand your context
- **Real autocomplete** - IDE knows your types and patterns
- **Personal notes** - Add comments, track progress in git
- **Zero config** - pytest, uv, ruff ready to go

## Quick Start

1. Click **"Use this template"** → **"Create a new repository"** on GitHub
2. Clone your new repo
3. Install dependencies:
   ```bash
   uv sync
   ```
4. Start solving:
   ```bash
   uv run pytest 00-arrays-and-hashing/0_contains_duplicate/
   ```

## Workflow

1. Read problem in `README.md`
2. Implement in `solution.py`
3. Run tests: `uv run pytest path/to/problem/`

## Project Structure

```
.
├── 00-arrays-and-hashing/     # 9 problems
│   ├── 0_contains_duplicate/
│   │   ├── README.md          # Problem description
│   │   ├── solution.py        # Your solution
│   │   └── solution_test.py   # Tests from LeetCode
│   └── ...
├── 10-stack/                  # 6 problems
├── 11-two-pointers/           # 5 problems
├── 20-binary-search/          # 7 problems
├── 21-sliding-window/         # 6 problems
├── 22-linked-list/            # 11 problems
├── 30-trees/                  # 15 problems
├── 40-tries/                  # 3 problems
├── 41-backtracking/           # 10 problems
├── 50-heap-priority-queue/    # 7 problems
├── 51-graphs/                 # 13 problems
├── 52-1d-dp/                  # 12 problems
├── 60-intervals/              # 6 problems
├── 61-greedy/                 # 8 problems
├── 62-advanced-graphs/        # 6 problems
├── 63-bit-manipulation/       # 7 problems
├── 64-2d-dp/                  # 11 problems
├── 70-math-and-geometry/      # 8 problems
└── pyproject.toml             # pytest, ruff configured
```

Folders follow the [NeetCode Roadmap](https://neetcode.io/roadmap) order - start with arrays, progress to graphs and DP.

## References

Problem descriptions and test cases were generated using:
- [wislertt/leetcode-py](https://github.com/wislertt/leetcode-py) - Problem descriptions
- [deepakness/neetcode-solutions](https://github.com/deepakness/neetcode-solutions) - Solution signatures
