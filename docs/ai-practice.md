# Practice with AI

The repository includes three workflows:

| Workflow | Example request |
| --- | --- |
| Coach | "Help me approach Contains Duplicate. Give me one hint at a time." |
| Review | "Review my Two Sum attempt and explain its time and space complexity." |
| Interview | "Run a 30-minute mock interview using a medium problem." |

Choose a problem by name or file path. Coaching leaves the implementation to you;
you can request a full explanation or ask the assistant to edit your solution at
any point. Review feedback includes local test results when the assistant can run
commands. Interview feedback includes the hints you used.

## Load the workflows

- **Codex:** Open this repository. Project skills live in `.agents/skills/`; invoke
  `$practice-coach`, `$solution-review`, or `$mock-interview`, or use the example
  requests above. See [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills).
- **Claude Code:** The root `CLAUDE.md` imports `AGENTS.md`, which points to the
  appropriate workflow for each request. Use the example requests above; this
  setup uses file-based guidance rather than registering slash commands.
  See [Claude Code imports](https://code.claude.com/docs/en/memory#import-additional-files).
- **Other assistants:** Ask the assistant to read `AGENTS.md` and the selected
  `.agents/skills/<workflow>/SKILL.md` file. For chat tools without repository
  access, attach those files, the problem statement, and your attempt. Supply
  your local test output when the assistant cannot run commands.

The shared defaults live in `AGENTS.md`; each workflow lives in its own `SKILL.md`.
Edit these files to adapt the template to your learning style.
