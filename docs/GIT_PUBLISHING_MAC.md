# How to commit and publish Project 1 on macOS

These steps assume you already made the first Git commit in your existing `ai-customer-feedback-lab-starter` project and have since added `challenge_lab`, `holdout_lab`, model outputs, and other files. **Do not run `git init` again.** The provided finalization pack contains documentation and a verified output-audit result, not your `.git` history.

## Mental model: four states of a Git file

```text
Edit/create file -> Working directory
          git add -> Staging area
       git commit -> Local repository history
         git push -> GitHub remote history
```

- `git status` inspects what changed.
- `git add` chooses what goes into the next snapshot. It does not upload anything.
- `git commit` creates a named local snapshot. It does not upload anything.
- `git push` sends committed history to a configured remote repository.

## Step 1. Open the existing local project

In VS Code, choose **File > Open Folder** and open your current `ai-customer-feedback-lab-starter` folder. Then **Terminal > New Terminal**.

```bash
pwd
git rev-parse --show-toplevel
git status
git log --oneline -3
git remote -v
```

**Expected:** `git rev-parse` reports your existing project directory, and `git log` shows at least the original first commit. If you get `not a git repository`, you are in the wrong folder. **Do not fix that by making a fresh repo unless you truly lost the original Git directory.**

## Step 2. Merge this pack into your existing repo

Download `AI_PM_Project_01_Finalization_Pack.zip` from ChatGPT and move it to your `~/Downloads` folder if macOS did not save it there.

```bash
mkdir -p "$HOME/Downloads/project01-finalization"
unzip -o "$HOME/Downloads/AI_PM_Project_01_Finalization_Pack.zip" \
  -d "$HOME/Downloads/project01-finalization"
```

**Important:** Back up your own edited README before applying the replacement. From the existing project root:

```bash
cp README.md "$HOME/Downloads/Project_01_README_backup.md"
rsync -av "$HOME/Downloads/project01-finalization/repo_overlay/" ./
```

The `rsync` command copies new documentation into your **existing project directory**, not into a new repository, so your prior code, result files, and `.git` history remain in place. It **will replace** matching files such as `README.md`; check the diff afterward. The pack does not include any `.git` folder.

If you made manual corrections to outputs or documentation after uploading them to ChatGPT, keep those local files as the authority and review any overwritten files before committing.

## Step 3. Run all the tests and refresh the audit

From the same existing project root:

```bash
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s challenge_lab/tests -v
python3 -m unittest discover -s holdout_lab/tests -v

python3 holdout_lab/audit_outputs.py \
  --feedback holdout_lab/data/holdout_feedback.csv \
  --v3 outputs/holdout_v3.json \
  --v4 outputs/holdout_v4.json \
  --out outputs/holdout_quality_audit.json
```

**Why:** We want a commit that contains tested code plus its supporting evidence. The combined tests are expected to report **2 + 2 + 5 = 9 passing tests** if your files match the current supplied project. The output quality audit will report one H216 exact-quote failure per version, six v3 insights versus five allowed, and v4's missing `mobile_accessibility` insight summary.

If `outputs/holdout_v3.json` or `outputs/holdout_v4.json` is missing, copy your saved run into `outputs/` or follow the holdout instructions to regenerate it. Do not fabricate a run.

## Step 4. Inspect every change before staging

```bash
git status --short
git diff --stat
git diff -- README.md
```

Make sure only project sources, documentation, and synthetic results are present. Your `.gitignore` should exclude `.venv/`, `.env`, compiled Python files, and temporary drafts. **Never** stage credentials, personal customer records, or private employer data.

Now stage the changed files:

```bash
git add -A
git diff --cached --stat
git diff --cached --check
git status
```

`git add -A` also stages deletions, so **review the staged list** before committing. If something is wrong:

```bash
git restore --staged path/to/unwanted-file
```

You can also reset the entire staging area without deleting local work:

```bash
git restore --staged .
```

## Step 5. Commit the project progress

```bash
git commit -m "Complete AI feedback classification evaluation and PM case study"
git log --oneline -3
```

This creates your **second local commit** (or the next commit after your previous history). It should preserve the first commit; we do not amend or rewrite that history.

If Git says `nothing to commit`, check `git status` and that you copied the files into the correct repository.

## Step 6. Push to GitHub

Check whether the `origin` remote already exists:

```bash
git remote -v
```

### Case A: `origin` exists

If you already created and linked your GitHub repo, simply run:

```bash
git push -u origin "$(git branch --show-current)"
```

You do **not** need to create a new GitHub repo or reinitialize Git.

### Case B: `git remote -v` shows nothing

If you have GitHub CLI installed, authenticate if needed and create a new public repo from your existing project:

```bash
gh auth status
gh auth login
gh repo create ai-customer-feedback-intelligence \
  --public --source=. --remote=origin --push
```

If `gh auth status` already shows valid authentication, you can skip `gh auth login`. Creating a public repo makes its contents accessible to others. Review the project and results for privacy before choosing `--public`. Alternatively use `--private` until you are ready to showcase it.

If you already created the remote repository on GitHub.com but haven't connected it locally, use its **exact** URL (replace the placeholder):

```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin "$(git branch --show-current)"
```

**Do not run `gh repo create` when an appropriate remote repository already exists.**

## Step 7. Verify the publication

```bash
git status
git log --oneline -3
git remote -v
```

If using GitHub CLI:

```bash
gh repo view --web
```

On the GitHub page confirm that `README.md`, `docs/`, `challenge_lab/`, `holdout_lab/`, and the permitted synthetic result files appear. The primary page should render the new README with links to the case study and evaluation report. A clean working tree after the push indicates that local tracked changes are committed, although you should still verify the remote contains the intended commit.

## Future daily Git workflow

After you finish a meaningful piece of work:

```bash
git status
git add -A
git diff --cached --stat
git commit -m "Describe the actual change"
git push
```

A good commit message describes the outcome, e.g., `Add output QA tests`, `Document human-review decision`, or `Fix exact-quote validation`.

## Common problems

| Symptom | Diagnosis | Next move |
|---|---|---|
| `fatal: not a git repository` | Terminal is not inside the existing repo | Open correct folder and check `git rev-parse --show-toplevel` |
| `nothing to commit` | Files may not have been copied, or already staged/committed | Check `git status --short` and `pwd` |
| `fatal: 'origin' does not appear...` | No usable remote configured | Check `git remote -v`; add remote or create GitHub repo |
| `src refspec main does not match` | Branch name differs or no commit exists | Use `git branch --show-current`; confirm `git log` |
| Git push rejected due to remote changes | Remote is ahead or history diverged | Inspect remote, then coordinate a safe pull/rebase. Don't force-push blindly |
| `.env` was already committed | `.gitignore` does not erase tracked history | Stop and remediate credentials; `git rm --cached` only stops tracking in new commits, not old history |
| Generated outputs not showing in Git | `.gitignore` patterns or wrong path | Run `git status --ignored` and review patterns |

**Official references:** [GitHub documentation on adding and committing files](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository), [GitHub CLI repo creation manual](https://cli.github.com/manual/gh_repo_create), [Git staging documentation](https://git-scm.com/docs/git-add).
