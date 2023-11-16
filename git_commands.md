# Git Commands for Common Tasks

## Fetching and Merging Changes from Remote Main
git fetch origin main
git merge origin/main
- This sequence of commands first fetches the latest changes from the `main` branch of the remote repository (`origin`) and then merges these changes into your current branch.

## Staging, Committing, and Pushing Changes to Remote Main
git add .
git commit -m "Your commit message"
git push origin main
- `git add .` stages all your modified files for the next commit.
- `git commit -m "Your commit message"`: Replace `"Your commit message"` with a meaningful description of the changes you're committing.
- `git push origin main` pushes your committed changes to the `main` branch of the remote repository.

## Pushing to a Non-Main Branch on Remote
git push origin your-branch-name
- Replace `your-branch-name` with the name of the branch you want to push to.
