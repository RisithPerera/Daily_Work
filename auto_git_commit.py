#!/usr/bin/env python3
import os
import random
import subprocess
import time
from datetime import datetime

# ─── CONFIG ────────────────────────────────────────────────────────────────
REPO_PATH = os.path.dirname(os.path.realpath(__file__))
TEXT_FILES = [f for f in os.listdir(REPO_PATH) if f.endswith('.txt')]
MIN_WAIT = 60 * 30     # 120 minutes, in seconds
MAX_WAIT = 60 * 250   # 1440 minutes, in seconds
COMMIT_MESSAGES = [
    "Update content",
    "Minor fix",
    "Small edit",
    "Adjust wording",
    "Improve formatting",
    "Fix formatting issue",
    "Add comment",
    "Edit note",
    "Tweak text",
    "Update info",
    "Refactor comment",
    "Polish text",
    "Fix typo",
    "Cleanup file",
    "Update entry",
    "Adjust sentence",
    "More updates",
    "Fix small issue",
    "Reword note",
    "Final edit",
    "Fix whitespace",
    "Touch up",
    "Update with timestamp",
    "Refresh file",
    "Keep it fresh",
    "Test commit",
    "Another small change",
    "Make a small tweak",
    "Adjust text formatting",
    "Keep it going",
    "Commit for activity"
]

# ────────────────────────────────────────────────────────────────────────────

def choose_file():
    return os.path.join(REPO_PATH, random.choice(TEXT_FILES))

def edit_file(path):
    """Append a timestamp line at the end."""
    with open(path, 'a') as f:
        f.write(f"\n# updated at {datetime.utcnow().isoformat()}Z")

def git(cmd):
    """Run a git command in the repo."""
    return subprocess.run(['git'] + cmd, cwd=REPO_PATH)

def main():
    if not TEXT_FILES:
        print("No .txt files found in", REPO_PATH)
        return

    while True:
        wait = random.uniform(MIN_WAIT, MAX_WAIT)
        print(f"Waiting {wait/60} minutes")
        time.sleep(wait)

        file_to_edit = choose_file()
        print(f"Editing the file {file_to_edit}")
        edit_file(file_to_edit)

        git(['add', os.path.relpath(file_to_edit, REPO_PATH)])
        msg = random.choice(COMMIT_MESSAGES)
        git(['commit', '-m', msg])
        print(f"Committing {file_to_edit} with “{msg}”")

        git(['push', 'origin', 'main'])  # or your default branch
        print(f"Pushed {file_to_edit} with “{msg}” after waiting {int(wait)}s")

if __name__ == '__main__':
    main()
