---
name: solution-review
description: Review a learner's NeetCoder attempt when they ask for code feedback, help diagnosing a failing test, or time and space complexity analysis. Keep an active mock interview in its interview workflow.
---

# Solution review

1. Read the problem contract, the attempt, and the relevant tests or supplied
   failure. For review-only requests where the implementation is still a stub,
   identify the missing method and ask for their approach before reviewing an
   algorithm that is not there.
2. Run the selected problem's tests when execution is available. Distinguish an
   assertion failure from an unfinished method or an environment/import failure;
   report unavailable execution as unverified.
3. Check the attempt against the stated constraints, mutation and identity rules,
   and allowed output order. For each correctness finding, give a concrete valid
   counterexample and the expected behavior. If a test rejects a valid solution,
   identify the test defect separately from the learner's code.
4. Explain worst-case time and auxiliary space using the input dimensions,
   including recursion and library operations. Separate measured results from
   complexity inferred by inspection.
5. Return the most consequential findings first, with the smallest useful next
   step. A review is complete when correctness findings have evidence, complexity
   is explained, and the test result and its limits are stated. If no issue was
   found, say what was checked instead of claiming the solution is proven correct.

Keep review feedback separate from edits. When the learner asks for a fix, make
the requested change and rerun the affected tests. Preserve existing test
expectations unless a demonstrated conflict with the problem contract justifies
a test correction.
