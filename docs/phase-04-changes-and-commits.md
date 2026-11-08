# Phase 4: Making Changes and Commits

> Created with 💖 by **FreeMatrix Studios** and **[@kuraigu](https://github.com/kuraigu)**

In this phase, you will create your personal profile folder, review your changes, and make your first Git commit.

---

## 1. Create Your Community Folder

To make sure everyone can submit Pull Requests without merge conflicts, each participant works inside their own folder under `community/`.

Copy the template folder to a folder named after your username:

```bash
# On macOS / Linux / Git Bash:
cp -r community/_template community/your-name

# On Windows PowerShell:
Copy-Item -Recurse community/_template community/your-name
```

---

## 2. Edit Your Profile File

Open the project folder in your code editor (like VS Code or Cursor).

Open `community/your-name/profile.md` and fill in:
- Your name and GitHub username.
- What you like creating, designing, or learning.
- A project or goal you are excited about.

Save the file.

---

## 3. Check What Git Sees

Run:
```bash
git status
```

Git will show `community/your-name/` listed in red under **"Untracked files"**. This means Git sees the new folder on your computer, but has not been told to track it yet.

---

## 4. Stage Your Folder

Staging is like placing items into a shopping cart before you check out. It tells Git: *"Include these specific changes in the next snapshot."*

Run:
```bash
git add community/your-name/
```

Now run `git status` again. Notice that `community/your-name/` turned green under **"Changes to be committed"**.

> [!WARNING]
> **Why we avoid typing `git add .` blindly:**
> Running `git add .` stages every single changed file on your machine. If you accidentally created temporary files, large logs, or secret `.env` API keys, you could accidentally commit them to GitHub. Always stage specific files or folders.

---

## 5. Review Your Staged Changes

Before locking in your snapshot, review the exact lines you are committing:

```bash
git diff --staged
```

You will see green text showing the lines you added. When you are done looking, press `q` on your keyboard to exit the diff view.

---

## 6. Make Your Commit

A commit creates a permanent snapshot in your local Git history. Always write a short, clear message explaining what changed:

```bash
git commit -m "feat: add community profile for your-name"
```

Output:
```text
[community/your-name 1a2b3c4] feat: add community profile for your-name
 2 files changed, 25 insertions(+)
 create mode 100644 community/your-name/profile.md
```

You have successfully created a permanent snapshot on your computer.

---

## Navigation

- **Previous:** [Phase 3: Branching](phase-03-branching.md)
- **Next:** [Phase 5: Understanding .gitignore & Protecting Secrets](phase-05-gitignore-and-secrets.md)
