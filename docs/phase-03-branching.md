# Phase 3: Branching

> Created with 💖 by **FreeMatrix Studios** and **[@kuraigu](https://github.com/kuraigu)**

In this phase, you will create a separate workspace inside the project called a **branch**.

---

## 1. Why Do We Use Branches?

In shared projects, the **`main`** branch represents tested, stable code. We avoid building new features or writing drafts directly on `main`. 

Instead, we create a branch. A branch is like a parallel sandbox. You can edit, experiment, make mistakes, and commit as much as you like on your branch without touching the stable `main` branch.

---

## 2. Check Your Current Branch

Inside your terminal in the project directory, run:

```bash
git branch
```

Output:
```text
* main
```

The asterisk `*` shows which branch you are currently on. Right now, you are on `main`.

---

## 3. Create and Switch to a New Branch

Create a branch using the naming pattern `community/your-name`:

```bash
git switch -c community/your-name
```

*(Note: Older tutorials often use `git checkout -b community/your-name`. Both do the same thing, but `git switch -c` is the clearer, modern command).*

---

## 4. Confirm You Switched

Run `git branch` again:

```bash
git branch
```

Output:
```text
* community/your-name
  main
```

The asterisk is now on `community/your-name`. Anything you do from this moment forward will stay safely contained on your branch.

---

## Navigation

- **Previous:** [Phase 2: Clone Your Fork to Your Laptop](phase-02-clone-your-fork.md)
- **Next:** [Phase 4: Making Changes and Commits](phase-04-changes-and-commits.md)
