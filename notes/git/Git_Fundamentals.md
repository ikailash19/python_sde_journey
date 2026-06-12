# Git Fundamentals

## Why Git?

Git is a distributed version control system used to track code changes and enable collaboration between developers.

Benefits:

1. Collaboration
2. History Tracking
3. Rollback
4. Safe Code Sharing

---

## Git Workflow

```text
Working Directory
        ↓
git add .
        ↓
Staging Area
        ↓
git commit
        ↓
Local Repository
        ↓
git push
        ↓
Remote Repository (GitHub)
```

---

## git add

```bash
git add .
```

Moves changes into the staging area.

Git now knows which changes should be included in the next commit.

---

## git commit

```bash
git commit -m "Add MovieService"
```

Creates a local snapshot.

Important:

```text
Commit does NOT send code to GitHub.
```

---

## git push

```bash
git push
```

Uploads local commits to GitHub.

Only after push can teammates see the changes.

---

## Local vs Remote Repository

After:

```bash
git commit
```

Code exists only on your machine.

After:

```bash
git push
```

Code becomes available in GitHub.

---

## Merge Conflict

Occurs when two developers modify the same code region.

Git cannot decide automatically.

Example:

```python
<<<<<<< HEAD
return movie
=======
return {"movie": movie}
>>>>>>> branch-name
```

Developer must choose the correct final version.

---

## Interview Definitions

### What is Git?

A distributed version control system used to track code changes and collaborate with multiple developers.

### What is a Commit?

A snapshot of code changes stored in the local repository.

### What is Push?

Uploading local commits to a remote repository.

### What is a Merge Conflict?

A situation where Git cannot automatically combine changes and requires manual resolution.

---

## Important Distinction

```bash
git add .
```

Stages changes.

```bash
git commit
```

Creates a local snapshot.

```bash
git push
```

Uploads commits to GitHub.

---

## Common Interview Question

Question:

If you commit but do not push, can teammates see your code?

Answer:

```text
No
```

Because commits exist only in the local repository until pushed.