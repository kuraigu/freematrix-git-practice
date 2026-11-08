# Phase 6: Four Essential Power Drills

> Created with 💖 by **FreeMatrix Studios** and **[@kuraigu](https://github.com/kuraigu)**

In day-to-day work, things get interrupted, mistakes happen, and you need to investigate past changes. This phase walks you through four practical tools.

---

## Drill 1: The Temporary Pause (`git stash`)

**Scenario:** You are halfway through typing changes in your `profile.md` file, but a teammate asks you to switch branches and look at something on `main`. You don't want to make an incomplete, messy commit just to switch branches.

### The Steps:

1. Open `community/your-name/profile.md` and add a test line at the bottom:
   ```markdown
   # Testing my git stash drill
   ```
2. Run `git status`. Git will show that `profile.md` is modified.
3. Put your unfinished work into Git's temporary pocket:
   ```bash
   git stash
   ```
4. Run `git status`. Your working tree is completely clean.
5. Now you can safely switch to `main` without any errors:
   ```bash
   git switch main
   # Check whatever you need...
   git switch community/your-name
   ```
6. Pull your changes back out of your pocket:
   ```bash
   git stash pop
   ```
   Open `profile.md`. Your changes are back, exactly where you left them.

---

## Drill 2: Updating Your Last Commit (`git commit --amend`)

**Scenario:** You made a commit, but noticed a spelling mistake in your commit message or forgot to include a small 1-line update. You don't want a messy extra commit in your project history that just says *"fixed typo"*.

### The Steps:

1. Add a small line inside `community/your-name/profile.md` and save.
2. Stage the file:
   ```bash
   git add community/your-name/profile.md
   ```
3. Roll the change directly into your previous commit:
   ```bash
   git commit --amend --no-edit
   ```
   *(If you want to edit the commit message as well, run `git commit --amend -m "your new message"` instead).*

---

## Drill 3: Reading Project History (`git log`, `git blame`, `git show`)

**Scenario:** A feature changed, and you need to know who wrote that line, when they wrote it, and what commit it belonged to.

We included a sample file: [`practice/pricing_model.py`](file:///A:/Development/GitPractice/practice/pricing_model.py).

### The Steps:

1. View a compact timeline of recent project commits:
   ```bash
   git log --oneline --graph --decorate
   ```
2. See line-by-line who edited each line of code:
   ```bash
   git blame practice/pricing_model.py
   ```
   Notice the author name, date, and commit hash next to every line.
3. Inspect the full details of any commit hash you saw in the log:
   ```bash
   git show <commit-hash>
   ```

---

## Drill 4: Discarding Local Changes (`git restore`)

**Scenario:** You were experimenting with edits, made a mess, and want to discard all uncommitted changes back to the last clean snapshot.

### The Steps:

1. Add some random characters or junk text to `practice/pricing_model.py` and save.
2. Run `git status` to see that Git noticed the modification.
3. Discard your uncommitted edits:
   ```bash
   git restore practice/pricing_model.py
   ```
4. Open the file. It is back to its clean, original state.

---

## Navigation

- **Previous:** [Phase 5: Understanding .gitignore & Protecting Secrets](phase-05-gitignore-and-secrets.md)
- **Next:** [Phase 7: Syncing and Pushing to GitHub](phase-07-syncing-and-pushing.md)
