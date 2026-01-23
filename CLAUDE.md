# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NeetCode practice repository with 150 LeetCode problems organized by topic following the NeetCode roadmap. Each problem has a stub solution that returns a zero-value, with pre-written tests based on LeetCode examples.

## Commands

```bash
# Run all tests
uv run pytest

# Run tests for a specific problem
uv run pytest 00-arrays-and-hashing/0_contains_duplicate/

# Run a single test
uv run pytest 00-arrays-and-hashing/0_contains_duplicate/solution_test.py::test_example_1

# Lint
uv run ruff check .

# Format
uv run ruff format .
```

## Problem Structure

Each problem folder contains:
- `README.md` - Problem description and examples from LeetCode
- `solution.py` - Function stub with type hints, returns zero-value
- `solution_test.py` - Tests from LeetCode examples (uses relative imports)

## Topic Categories

Problems are organized in numbered directories by topic:
- `00-arrays-and-hashing`, `10-stack`, `11-two-pointers`
- `20-binary-search`, `21-sliding-window`, `22-linked-list`
- `30-trees`, `40-tries`, `41-backtracking`
- `50-heap-priority-queue`, `51-graphs`, `52-1d-dp`
- `60-intervals`, `61-greedy`, `62-advanced-graphs`
- `63-bit-manipulation`, `64-2d-dp`, `70-math-and-geometry`

## Workflow

1. Read the problem in `README.md`
2. Implement the solution in `solution.py`
3. Run tests to verify: `uv run pytest path/to/problem/`
