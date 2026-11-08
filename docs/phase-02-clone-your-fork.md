# Phase 2: Clone Your Fork to Your Laptop

> Created with 💖 by **FreeMatrix Studios** and **[@kuraigu](https://github.com/kuraigu)**

Now that you have your own fork in the cloud, you will download it onto your computer so you can edit files locally in your code editor.

---

## 1. Copy Your Fork's URL

1. On GitHub, make sure you are viewing **your personal fork** (the URL should include your username, not the original owner's).
2. Click the green **`<> Code`** button.
3. Make sure **HTTPS** is selected, then click the copy icon to copy the URL.

The URL will look like this:
```text
https://github.com/<your-username>/freematrix-git-practice.git
```

---

## 2. Choose Where to Put the Project

Open your terminal. Navigate to the folder where you want to keep your project files. For example, your user home directory or a dedicated development folder:

```bash
# Move to your home folder:
cd ~

# Or if you have a projects folder:
cd ~/projects
```

---

## 3. Run the Clone Command

Type `git clone` followed by the URL you copied:

```bash
git clone https://github.com/<your-username>/freematrix-git-practice.git
```

Git will download the files and complete history onto your machine.

---

## 4. Move into the Project Folder

Move your terminal into the newly created project folder:

```bash
cd freematrix-git-practice
```

---

## 5. Check Your Status

Run the single most useful command in Git:

```bash
git status
```

Git should output:
```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This confirms you are inside the repository and everything is clean.

---

## Navigation

- **Previous:** [Phase 1: Fork the Repository](phase-01-fork-repository.md)
- **Next:** [Phase 3: Branching](phase-03-branching.md)
