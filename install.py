#!/usr/bin/env python3
"""Install or update the unpacked Calendar bridge without changing its path."""

import os
from pathlib import Path
import shutil


def install(data):
    destination = data / "notion-calendar-desktop-bridge"
    source = Path(__file__).resolve().parent / "extension"
    if source.resolve() == destination.resolve():
        raise ValueError("Run the installer from a separate repository checkout")
    shutil.copytree(source, destination, dirs_exist_ok=True)
    print(f"Load unpacked extension: {destination}")
    print("Reload the extension in your browser, then reload Notion Calendar.")
    return destination


if __name__ == "__main__":
    install(Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local/share"))
