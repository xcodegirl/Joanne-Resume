# T0507 — Version Control with Git and GitHub
**Program:** Full Stack Development (FSD)  
**Hours:** 20 hrs (1 week)  
**Delivery:** Online Instructor-Guided

---

## Description

Students learn to manage code and collaborate using Git and GitHub — the industry-standard tools for version control and team development. The course covers core Git workflows, branching strategies, pull requests, and resolving merge conflicts. Students leave with a functioning GitHub profile and the habits professional developers use every day.

**Rationale:** Version control is a foundational professional skill. All subsequent FSD courses require students to submit work via GitHub repositories. This course gives students the vocabulary, mental model, and hands-on practice to use Git confidently from day one of the next course.

---

## Learning Outcomes

**Outcome 1: Use Git to track and manage changes to code**
- Explain the purpose of version control and the Git object model
- Initialise a repository with `git init` and configure identity
- Stage and commit changes with meaningful commit messages
- Inspect repository history with `git log`, `git diff`, and `git status`
- Undo changes with `git restore`, `git revert`, and `git reset`
- Use `.gitignore` to exclude files from tracking

**Outcome 2: Collaborate using GitHub and a branching workflow**
- Create and clone remote repositories on GitHub
- Push and pull changes between local and remote
- Create, switch, and merge branches
- Open, review, and merge pull requests on GitHub
- Resolve merge conflicts
- Apply the Feature Branch Workflow to a small team project

---

## Assessment

| Assessment | Description | Weight |
|---|---|---|
| Assignment: Git Workflow Portfolio | A GitHub repository demonstrating all required Git operations: commits, branches, pull request, conflict resolution, and a clean history | 100% |

**Minimum passing grade:** 70%

---

## Course Schedule

### Module 1 — Git Fundamentals (Days 1–3, ~12 hrs)

**Topics:**
- What is version control? Distributed vs centralised
- Git's three areas: working directory, staging area, repository
- `git init`, `git config`, and first commit
- The commit lifecycle: `add`, `commit`, `status`, `log`
- Reading `git diff`: staged vs unstaged changes
- Undoing work: `restore`, `revert`, `reset --soft / --mixed / --hard`
- `.gitignore` patterns and common entries
- Navigating history: `git log --oneline --graph`

**Activities:**
- Initialise a project repository and make a series of meaningful commits
- Stage selective changes using `git add -p`
- Intentionally make and then undo a bad commit using `git revert`
- Configure a `.gitignore` for a typical project

---

### Module 2 — GitHub and Collaborative Workflows (Days 4–5, ~8 hrs)

**Topics:**
- GitHub: repositories, README, and the GitHub UI
- `git remote`, `git push`, and `git pull`
- Branches: `git branch`, `git switch -c`, `git merge`
- Fast-forward vs three-way merges
- Pull requests: creating, reviewing, and merging on GitHub
- Merge conflicts: how they arise and how to resolve them
- The Feature Branch Workflow
- GitHub profile hygiene: pinned repos, README, commit history

**Activities:**
- Push a local repository to GitHub; write a README
- Create a feature branch, make commits, and open a pull request
- Simulate a merge conflict and resolve it
- Review a partner's pull request (or self-review with two local clones)
- Submit the completed repository URL as the assignment deliverable

---

## Required Materials

- **Software:** Git; GitHub account (free); VS Code with GitLens extension (recommended); GitHub Desktop (optional)
- **Equipment:** Laptop/Computer

---

## Tips for Success

- Write commit messages in the imperative mood: **"Add login form"** not "Added login form"
- Commit early and often — small, focused commits are easier to understand and revert
- Never commit directly to `main` on a shared repository — use branches
- A good `.gitignore` entry saves your teammates from seeing `node_modules/` or `.DS_Store`

---

## Academic Policies

- **Grading:** Minimum 70% to pass
- **Attendance:** Active participation is tracked
- **Copyright:** Unauthorized copies of course materials are a violation of the Copyright Act and may constitute academic misconduct
- See the [Robertson College Student Guide](https://www.robertsoncollege.com/help/student-resources/student-guide/) for full policies
