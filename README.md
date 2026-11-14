# Notion Calendar → Desktop

Open Notion task links from Notion Calendar in Notion Desktop rather than
opening another browser tab. Both `calendar.notion.com` and
`calendar.notion.so` are supported.

## Install

Install Git and Python 3 first, then clone from GitHub:

```sh
mkdir -p ~/Documents/github_repositories
cd ~/Documents/github_repositories
git clone https://github.com/iop098321qwe/notion_calendar_desktop_bridge.git
cd notion_calendar_desktop_bridge
git switch develop
python3 install.py
```

Until a release is cut, use `develop`, where the extension source lives.
Private repository access requires GitHub authentication.
The installer copies files to `~/.local/share/notion-calendar-desktop-bridge`;
`XDG_DATA_HOME` overrides the data directory. Keep the checkout separate from
that installation directory. No administrator privileges are needed.

Requires a Chromium-based browser supporting MAIN-world content scripts
(Chromium 111 or newer), plus Notion Desktop registered for `notion://` URLs.

1. Open `brave://extensions` (or `chrome://extensions`).
2. Enable **Developer mode** and choose **Load unpacked**.
3. Select the installed directory printed by `python3 install.py`.
4. Reload Notion Calendar and click a linked Notion task.
5. Approve the browser's external-application prompt when requested.

To check the desktop protocol handler on Linux:

```sh
xdg-mime query default x-scheme-handler/notion
```

## How it works

- `extension/direct.js` intercepts Calendar task clicks at document start,
  during the original user gesture, and hands off in the existing tab.
- `extension/links.mjs` validates supported HTTPS Notion task URLs and
  converts their page IDs into desktop URLs.
- `extension/background.mjs` handles otherwise unhandled Calendar navigations.
- `extension/launch.html` and `launch.mjs` provide desktop-launch and explicit
  web-fallback links when the direct route cannot be used.

The worker remembers source tab IDs in session storage across suspension,
not task URLs. Independently opened Notion tabs are left unchanged.
The extension uses only the scoped Notion hosts declared in its manifest.

## Tests

Requires Node.js with the built-in test runner and Python 3; no npm
dependencies are needed to execute the tests.

```sh
npm test
```

The suite covers URL validation, direct handoff, user activation, converter
parity, source-tab scoping, navigation races, worker restart, and fallback.
Browser APIs are mocked; authenticated Calendar behavior and desktop protocol
prompts still need a manual browser check.

## Update and troubleshoot

Run these commands from your GitHub checkout:

```sh
cd ~/Documents/github_repositories/notion_calendar_desktop_bridge
git switch develop
git pull --ff-only origin develop
python3 install.py
```

Then open `brave://extensions` (or `chrome://extensions`), click **Reload**
on **Notion Calendar → Desktop**, approve any requested permissions, and
reload Calendar. If Brave Origin loads it through launch flags, fully exit
all Brave Origin windows, including web apps, and reopen instead.
Unpacked extensions do not update automatically from GitHub.
If handoff is blocked, use the launch page's desktop button and check the
OS protocol handler. Remove the extension in browser settings to uninstall.

## Repository maintenance

This repository maintains the extension previously stored in Chezmoi at
`dot_local/share/notion-calendar-desktop-bridge`. The manifest version is
unchanged; releases are cut manually.

Chezmoi no longer installs or updates this extension. The repository installer
retains the old installed path, so existing browser loading flags still work.
Do not load the checkout's `extension/` directory as a second copy: its
unpacked extension ID may differ. Existing installs only need the update steps.
