# Troubleshooting & "Don't Panic" Guide

> Created with 💖 by **FreeMatrix Studios** and **[@kuraigu](https://github.com/kuraigu)**

When something looks wrong in Git, take a breath. Git almost never loses your work once it has been committed or stashed.

---

### 1. "Vim opened in my terminal and I'm trapped"
If your terminal shows a strange screen with squiggles (`~`) and you can't type normal commands:
1. Press `Esc` twice.
2. Type `:wq` and press `Enter` (saves and exits).
3. If you want to cancel without saving, press `Esc`, type `:q!`, and press `Enter`.

> **Pro Tip:** Tell Git to use VS Code or Nano instead of Vim:
> ```bash
> git config --global core.editor "code --wait"
> ```

---

### 2. "Your local changes would be overwritten by checkout / merge"
**Why it happens:** You made uncommitted changes in your working tree, and switching branches would overwrite those files.

**How to solve it:**
- If you want to keep your work:
  ```bash
  git stash
  git switch <other-branch>
  # when you switch back later:
  git stash pop
  ```
- If you want to throw away your uncommitted edits:
  ```bash
  git restore .
  ```

---

### 3. "HEAD detached at [hash]"
**Why it happens:** You checked out a specific commit instead of a branch name. You're in "read-only snapshot" mode.

**How to solve it:**
Just switch back to your branch:
```bash
git switch main
# or
git switch your-branch-name
```

---

### 4. "I accidentally committed a secret or sensitive file (.env, API key)"
**Stop! Do not push to GitHub yet.**

1. Remove the file from Git tracking without deleting it from your computer:
   ```bash
   git rm --cached .env
   ```
2. Make sure `.env` is listed in `.gitignore`.
3. Amend your commit or make a new commit:
   ```bash
   git commit --amend -m "chore: remove untracked secret file"
   ```
*(If you already pushed the secret to a public GitHub repo, assume that key is compromised immediately. Rotate the API key in the third-party dashboard right away).*

---

### 5. "Merge conflict! What do I do?"
When Git cannot automatically combine two different changes to the exact same line, it marks the conflict in the file:

```
<<<<<<< HEAD (Current change on your branch)
Scale tier ($299/mo)
=======
Scale tier ($349/mo)
>>>>>>> main (Incoming change from remote)
```

**How to solve it:**
1. Open the file in VS Code or your editor.
2. Decide which version is right (or combine both).
3. Delete the marker lines (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Save the file.
5. Stage and finish the merge:
   ```bash
   git add <conflicted-file>
   git commit -m "fix: resolve pricing tier merge conflict"
   ```
