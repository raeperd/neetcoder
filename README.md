# NeetCoder

LeetCode practice repository with 150 problems organized by topic following the NeetCode roadmap.

## Project Structure

```
.
├── 00-arrays-and-hashing/     # 9 problems
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
└── 70-math-and-geometry/      # 8 problems
```

Each problem folder contains:
```
0_contains_duplicate/
├── README.md          # Problem description with YAML frontmatter
├── solution.py        # Solution stub with type hints
├── solution_test.py   # Tests based on LeetCode examples
└── __init__.py
```

### Why This Structure?

The folder naming follows the [NeetCode Roadmap](https://neetcode.io/roadmap) learning order:

- **Numeric prefixes** (`00-`, `10-`, `20-`, ...) define the recommended study sequence, grouping related topics together
- **Problem numbers** (`0_`, `1_`, `2_`, ...) order problems from easier to harder within each topic
- **Self-contained folders** allow running tests for individual problems without dependencies

This structure supports a progressive learning path: master fundamentals (arrays, stacks) before tackling advanced topics (graphs, dynamic programming).

## References

Problem descriptions and test cases were generated using:
- [wislertt/leetcode-py](https://github.com/wislertt/leetcode-py) - Problem descriptions
- [deepakness/neetcode-solutions](https://github.com/deepakness/neetcode-solutions) - Solution signatures
