---
name: practice-coach
description: Coach a learner through a NeetCoder exercise when they ask for an explanation, a hint, or help getting unstuck. Use solution-review for feedback on an existing attempt and mock-interview for a requested interview session.
---

# Practice coach

1. Read the selected problem's `README.md` and the learner's current attempt, if
   present. If the target is missing, ask which problem they want to practice.
   For a question about the statement or an example, answer that question and
   finish. For help solving it, continue once their current sticking point is known.
2. Start from the approach already supplied. If none is supplied, ask how they
   would solve a small example and wait for their response.
3. Give one hint addressing the identified gap, then ask them to apply it to a
   concrete input. End the turn there so they can attempt the next step.
   On follow-up, progress from an observation, to an invariant or data structure,
   to pseudocode only as the learner needs more help.
4. When the learner has an implementation, run the selected problem's tests if
   execution is available. Report the actual result and ask them to explain its
   time and space costs. Finish with the remaining gap or one useful review note.

For an explicit request for the full answer, explain the algorithm and its
complexity directly. Edit `solution.py` when implementation changes are requested.
Preserve the exercise's public signature and test expectations. Describe passing
results as local test evidence; online-judge acceptance requires a submission result.
