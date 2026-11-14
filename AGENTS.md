# AGENTS.md

## Purpose

This file guides AI coding agents working in `notion_calendar_desktop_bridge`.
All work must follow best practices and industry standards where
applicable.

## Scope

This file covers repository-wide expectations for code, docs, and git
work.
It does not replace verified instructions in source files, tooling
configs,
or release automation.

## Formatting Rules

- Keep lines at 80 characters or fewer when practical.
- Allow longer lines only for URLs, code blocks, hashes, or commands
  that cannot be wrapped cleanly.

## Quick Start

- Read `README.md` first for project context and setup notes.
- Run `git status --short --branch` before editing to confirm repo
  state.
- Run `git diff --stat` before committing to review the change scope.
- Load `extension/` unpacked in a Chromium 111+ browser.
- Run `npm test` for the Node test suite.

## Environment

- Git is required for day-to-day work in this repository.
- Node.js with `node:test` is required for tests.
- Python 3 is required for installation and installer tests.
- A registered `notion://` desktop handler is required for live handoff.
- No required environment variables are defined.

## Repository Overview

- `extension/` holds the browser extension.
- `tests/` holds isolated Node browser simulations.
- `docs/` links root documentation; `site/` is generated docs output.
- Root files hold repository tooling and documentation.

## Tracked Files Overview

- `.github/workflows/docs.yml`: Zensical Pages build and deployment.
- `.gitignore`: local dependency and cache exclusions.
- `.husky/commit-msg`: commitlint hook.
- `AGENTS.md`: repository instructions.
- `LICENSE`: repository license.
- `README.md`: installation and maintenance guide.
- `commitlint.config.cjs`: Conventional Commit validation.
- `docs/AGENTS.md`, `docs/README.md`: root documentation symlinks.
- `done.txt`: bootstrap completed-task placeholder.
- `extension/background.mjs`: fallback navigation worker.
- `extension/direct.js`: user-gesture desktop handoff.
- `extension/launch.html`: desktop and web fallback page.
- `extension/launch.mjs`: launch-page behavior.
- `extension/links.mjs`: validated URL conversion.
- `extension/manifest.json`: MV3 permissions and entry points.
- `inbox.txt.tuxedo-lock`: bootstrap inbox lock placeholder.
- `install.py`: copies extension files to the stable XDG data path.
- `package-lock.json`: npm dependency lock.
- `package.json`: metadata, test command, and commitlint dependencies.
- `site/`: generated documentation; contents omitted from per-file listing.
- `tests/notion-calendar-desktop-bridge.cjs`: mocked browser regression suite.
- `tests/test_install.py`: isolated installation and update checks.
- `todo.txt`: user-only task file; agents must not touch it.
- `zensical.toml`: documentation site configuration.

## Architecture

- A MAIN-world handler intercepts Calendar clicks during user activation.
- The worker backs up direct handoff with a launch page and web fallback.
- Keep `direct.js` and `links.mjs` URL conversion behavior aligned.
- Session storage retains source tab IDs, not task URLs.

## Commands

- `git status --short --branch`: show the current branch and worktree
  state.
- `git diff --stat`: review the size and spread of pending changes.
- `git log --oneline --decorate -5`: inspect recent commit history.
- `npm test`: run isolated regression tests.
- `zensical build --clean`: build documentation when installed.

## Testing

- `npm test` covers URL validation, activation, races, and fallback.
- Confirm live Calendar and desktop protocol prompts manually.
- Do not claim coverage, test gates, or suites that are not verified.

## Linting and Formatting

- Commitlint validates messages through the Husky commit hook.
- No source formatter is configured.
- Keep changes minimal and consistent with the existing code style.

## CI and Release

- `.github/workflows/docs.yml` builds Zensical on `main` and `master`.
- User installation and update instructions must use the `main` branch.
- Releases are manual; release-note filters are not defined here.
- Use Conventional Commits for every commit. Prefer a scope when it
  adds clarity.
- Never create, edit, or update `CHANGELOG.md` manually.
- `CHANGELOG.md` is generated and maintained by release tooling only.
- If release automation adds or changes generated files, let the
  tooling own those updates.

## Conventions

- Use small, correct changes that fit the existing project structure.
- Agents must never read, create, edit, delete, move, stage, commit, or
  otherwise touch `todo.txt`; only the user may modify it manually.
- Prefer amending small related corrections into the relevant unshared
  current-branch commit instead of separate fixup or cleanup commits.
- Use standalone, changelog-ready Conventional Commit headers.
- Verify behavior from the actual codebase before documenting or
  changing it.
- Keep `AGENTS.md` as instructions, not as a changelog, diary, or work
  log.
- Do not add update notes, status logs, or change summaries to
  `AGENTS.md`.

## Security and Compliance

- Never commit secrets, credentials, tokens, or private keys.
- Verify new dependencies, automation, and scripts before trusting
  them.

## Dependencies and Services

- Notion Calendar and Notion Desktop provide the live integration.
- No background service, server, or database is installed.
- Releases are manual; do not change versions as part of migration.

## Troubleshooting

- If repo behavior is unclear, inspect tracked files and git history
  before making assumptions.
- If a generated or managed file changes unexpectedly, verify which
  tool owns it before editing.

## Refining Existing AGENTS.md

- Re-check every statement against the repository before keeping it.
- Remove stale, duplicated, or vague guidance.
- Replace placeholders with exact commands, paths, and verified
  workflows.
- Keep bullets short and easy for AI agents to scan.
- Preserve this section order when improving the file.

## Maintenance

- After any code, config, or doc change, verify that `AGENTS.md` still
  matches the repository.
- When `AGENTS.md` needs an update, make it in a separate `docs`
  Conventional Commit such as `docs(agents): update repo instructions`.
- Keep `AGENTS.md` out of mixed code commits whenever possible.
- Remove stale instructions instead of appending historical notes.
