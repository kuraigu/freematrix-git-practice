# FreeMatrix Git & GitHub Quick Reference

> Created with 💖 by **FreeMatrix Studios** and **[@kuraigu](https://github.com/kuraigu)**

Keep this open whenever you're touching the terminal. 95% of your daily workflow boils down to these commands.

---

## 1. The Everyday 5-Step Loop

```bash
# 1. Always pull latest main before starting new work
git switch main
git pull origin main

# 2. Create and jump to a fresh branch for your work
git switch -c community/your-name

# 3. Check what you changed (do this often!)
git status
git diff

# 4. Stage and commit your changes
git add community/your-name/
git commit -m "feat: add user onboarding questionnaire"

# 5. Push your branch to GitHub
git push -u origin community/your-name
```

---

## 2. Managing Branches

| Goal | Command | Why / Notes |
| :--- | :--- | :--- |
| **List all branches** | `git branch` | Shows local branches; asterisk `*` marks where you are. |
| **Create & switch branch** | `git switch -c <name>` | Modern way. Older alternative: `git checkout -b <name>`. |
| **Switch to existing branch** | `git switch <name>` | Switch back and forth (e.g. `git switch main`). |
| **Delete local branch** | `git branch -d <name>` | Safe delete (won't let you delete unmerged work by accident). |

---

## 3. Remotes, Syncing & Forking

| Goal | Command | Why / Notes |
| :--- | :--- | :--- |
| **View remote URLs** | `git remote -v` | See where `origin` (and `upstream`) point. |
| **Download team updates** | `git pull origin main` | Fetches and merges latest commits from GitHub `main`. |
| **Inspect without merging** | `git fetch origin` | Downloads commit info without touching local files. |
| **Add original repo to a fork** | `git remote add upstream <url>` | Connects your fork to the original source repo. |
| **Sync fork with upstream** | `git fetch upstream && git merge upstream/main` | Pulls original updates into your fork. |

---

## 4. Working With Stashes (Pause & Resume)

Use this when you are halfway through some code or notes, but suddenly need to pull updates from main or switch branches without committing messy, broken work.

| Goal | Command |
| :--- | :--- |
| **Shelve current work** | `git stash` (or `git stash save "wip onboarding flow"`) |
| **See what is shelved** | `git stash list` |
| **Restore stashed work & delete stash** | `git stash pop` |
| **Peek inside the stash** | `git stash show -p` |
| **Discard the latest stash** | `git stash drop` |

---

## 5. Inspecting History & Blaming

| Goal | Command | What it tells you |
| :--- | :--- | :--- |
| **Visual commit history** | `git log --oneline --graph --decorate` | Compact tree view of recent commits. |
| **Inspect a specific commit** | `git show <commit-hash>` | Exact lines added/deleted in that commit. |
| **Line-by-line blame** | `git blame <filename>` | Shows who touched which line, when, and in which commit. |
| **Check staged changes** | `git diff --staged` | Review exactly what is about to be committed. |

---

## 6. Quick Fixes (Before Pushing)

- **Fixed a typo in your last commit message?**
  ```bash
  git commit --amend -m "Fixed message here"
  ```
- **Forgot to add a file to the last commit?**
  ```bash
  git add forgotten-file.md
  git commit --amend --no-edit
  ```
- **Messed up a local file and want to revert it back to the last commit?**
  ```bash
  git restore <filename>
  ```
- **Staged a file by mistake and want to unstage it?**
  ```bash
  git restore --staged <filename>
  ```
