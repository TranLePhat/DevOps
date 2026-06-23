# Git

## 1. What is Git?

Git is a distributed Version Control System (VCS) created by Linus Torvalds.

It tracks changes made to files over time and allows multiple people to collaborate on the same project safely.

Git is commonly used for:

* Source code management
* Infrastructure as Code (IaC)
* Configuration management
* Documentation
* DevOps projects

---
## 2. Why is it Important?

Git solves several critical problems:

* Tracks file changes
* Enables team collaboration
* Prevents accidental data loss
* Supports rollback to previous versions
* Allows parallel development using branches

---
## 3. How Does It Work Internally?

When a repository is initialized:
git init
```
Git creates a hidden directory:

.git/
```

This directory stores:

* Commit history
* Branch information
* Configuration
* Object database

Unlike centralized systems, every developer has a complete copy of the repository.

This means:

* Work can continue offline
* History is stored locally
* Synchronization happens only when needed

Example:

Developer A
      ↕
Developer B
      ↕
GitHub / GitLab
```

---
## 4. Core Components

### Repository

A repository contains:

* Project files
* Git metadata

Example:

git init
```
---
### Commit

A commit is a snapshot of changes at a specific point in time.

Example:
git commit -m "Add monitoring script"
```

---
### Branch

A branch represents an independent line of development.

Common branches:

```text id="rn5o31"
main
develop
feature/*
hotfix/*
```

Example:

```bash id="krgx2y"
git checkout -b feature/docker-support
```

---
### Remote Repository

A remote repository is hosted on platforms such as:

* GitHub
* GitLab
* Bitbucket

Example:

```bash id="bn4qvi"
git remote -v
```

---

### Staging Area

Changes are first added to the staging area before being committed.

Example:

```bash id="xqmgdi"
git add .
```

Workflow:

```text id="7wg2em"
Working Directory
        ↓
Staging Area
        ↓
Commit
```

---

## 5. Dependencies and Related Concepts

### File Systems

Git tracks changes made to files and directories.

---

### Diff

Git compares file versions to identify changes.

Example:

```bash id="kw2jiv"
git diff
```

---

### Hashing

Every Git object is identified by a SHA hash.

Example:

```text id="3st5k9"
f7a9c8b...
```

This guarantees data integrity.

---

### Distributed Systems

Git allows repositories to be synchronized across multiple machines.

---

## 6. Common Misconceptions

### Git and GitHub Are the Same Thing

Incorrect.

Git:

```text id="stlhdi"
Version Control System
```

GitHub:

```text id="cv8w3s"
Cloud hosting platform for Git repositories
```

Git works without GitHub.

---

### Commits Are Backups

Partially true.

Commits are snapshots of changes, not traditional backups.

Git is designed for version tracking, not disaster recovery.

---

### Git Automatically Prevents Conflicts

Incorrect.

Git helps manage conflicts, but developers still need to resolve them manually.

---

## 7. Common Production Issues

### Direct Push to Main

Bad practice:

```text id="sdt7m7"
Developer
      ↓
main
      ↓
Production
```

Risks:

* Unreviewed changes
* Accidental outages
* Difficult rollbacks

---

### Long-Lived Branches

Developers keep branches for weeks or months.

Result:

```text id="wzktff"
Merge Conflicts
Integration Problems
```

This is often called:

```text id="dz2q74"
Integration Hell
```

---

### Poor Commit Messages

Bad:

```text id="8p1qv8"
fix
update
test
```

Good:

```text id="bqv03k"
Fix nginx log parser bug
Add Docker monitoring support
```

---

## 8. Troubleshooting Runbook

### Check Repository Status

```bash id="ukjmg6"
git status
```

Shows:

* Current branch
* Modified files
* Untracked files

---

### Inspect Changes

```bash id="6frh91"
git diff
```

Shows line-by-line differences.

Symbols:

```text id="c2j3al"
- Removed line
+ Added line
```

---

### View Commit History

```bash id="6tjj3r"
git log --oneline
```

---

### Identify Current Branch

```bash id="4r5m7e"
git branch
```

---

### Check Remote Configuration

```bash id="k3nfhw"
git remote -v
```

---

### Roll Back Changes

Discard local modifications:

```bash id="dfgbqe"
git restore file.txt
```

Revert a commit:

```bash id="i8qgcw"
git revert <commit-id>
```

---

## 9. Build It Yourself

### Step 1

Create a repository.

```bash id="1m5ttj"
git init
```

---

### Step 2

Create a feature branch.

```bash id="a3s3db"
git checkout -b develop
```

---

### Step 3

Modify files.

```bash id="9rnn1m"
echo "Hello Git" > app.txt
```

---

### Step 4

Stage changes.

```bash id="jlwm2x"
git add .
```

---

### Step 5

Create a commit.

```bash id="aq78vu"
git commit -m "Initial commit"
```

---

### Step 6

Push to remote repository.

```bash id="j9u4bg"
git push origin develop
```

---

### Step 7

Create a Pull Request.

Workflow:

```text id="cy31zm"
Feature Branch
      ↓
Pull Request
      ↓
Code Review
      ↓
Merge
```

---

## Frequently Used Commands

```bash id="pgcc98"
git init

git clone <repo>

git status

git add .

git commit -m "message"

git push

git pull

git fetch

git branch

git checkout -b <branch>

git merge

git diff

git log --oneline

git remote -v
```

---

## Git Workflow for DevOps

Recommended workflow:

```text id="q6oxjp"
main
│
├── feature/*
│
├── bugfix/*
│
└── hotfix/*
```

Development Flow:

```text id="1a3oyc"
Create Branch
      ↓
Make Changes
      ↓
Commit
      ↓
Push
      ↓
Pull Request
      ↓
Review
      ↓
Merge
```

Never push directly to production branches without review.
