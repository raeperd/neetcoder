# Maintaining practice tests

## Starter implementations

Unimplemented exercise methods raise `NotImplementedError`, including constructors
in design exercises. Keep supplied `ListNode`, `TreeNode`, and `Node` constructors
functional so tests can build inputs. Preserve public signatures and docstrings.

A fresh template intentionally fails exercise tests. `NotImplementedError` means
the learner has work to do; collection/import errors mean the test setup is broken.
Keep failures visible instead of skipping or marking unfinished exercises as xfail.

## Test contracts

Read the problem's `README.md` before adding cases. Use inputs within its constraints.
Check the behavior the statement requires, including:

- Deep copies: every copied node is new, copied edges stay within the copy, and
  the original structure is preserved after the call. Bound traversals so a broken
  cyclic result fails an assertion instead of hanging the test helper.
- Serialization: the wire value is a string, and a fresh decoder reconstructs
  the input. Allow any valid encoding. Interleave multiple inputs to expose state
  accidentally shared between calls.
- In-place operations: assert the caller's object after the call. For operations
  returning an existing node, assert object identity rather than only its value.
- Multiple valid answers: validate the required properties or normalize permitted
  ordering instead of requiring one arbitrary answer.
- Boundaries: use minimum sizes, zeros, duplicates, disconnected components, and
  cycles where valid. Prefer deterministic larger cases over timing thresholds;
  a passing test does not prove the required asymptotic complexity.

## Validate a test change

1. Run `uv run pytest --collect-only -q`, `uv run ruff check .`, and
   `uv run ruff format --check .`. Resolve collection and tool failures.
2. In a temporary copy of the affected exercises, run every affected test against
   a correct implementation. Also try a valid alternative when the contract permits
   different orderings or encodings. Keep those implementations out of the template.
3. Run a deliberately incorrect implementation for each contract being strengthened.
   Confirm the test rejects it for the intended assertion, rather than an unrelated
   import error or unfinished stub. Record the tested defects and results in the PR.
4. Run the template's exercise suite and distinguish expected unfinished-method
   failures from regressions in tests. Report the actual results without treating
   expected failures as a green suite.
