# Git Branches

## What is a Branch?

A branch is an independent line of development.

It allows developers to work on features without affecting the main codebase.

---

## Why Branches Exist

Without branches:

- Experimental code can break stable code.

With branches:

- Work is isolated.
- Main branch remains stable.

---

## Common Branches

```text
master/main
```

Stable code.

```text
feature/post-movie-api
```

Feature development.

---

## Creating a Branch

```bash
git checkout -b feature/git-practice
```

Creates and switches to a new branch.

---

## Viewing Branches

```bash
git branch
```

Example:

```text
* feature/git-practice
  master
```

The * indicates the current branch.

---

## Switching Branches

```bash
git checkout master
```

```bash
git checkout feature/git-practice
```

---

## Important Learning

Branches separate commits.

Branches do NOT separate uncommitted changes.

Uncommitted changes belong to the working directory.

---

## Git Stash

Temporarily stores uncommitted work.

Save:

```bash
git stash
```

Restore:

```bash
git stash pop
```

Useful when switching tasks before committing.

---

## Merging Branches

```bash
git merge master
```

Brings changes from master into the current branch.

---

## Fast-Forward Merge

Occurs when the target branch is simply ahead.

Git moves the branch pointer forward without creating a merge commit.

---

## Industry Workflow

```text
master/main
        ↓
feature branch
        ↓
commit work
        ↓
merge
        ↓
master/main
```

---

## Interview Definition

A Git branch is an independent line of development used to isolate features, bug fixes, or experiments from the main codebase.