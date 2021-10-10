# ase-fall21
lab1 ase

## Specification

Calculator perform 4 operations: + - * /

## Note on merging no common history

It is not possibile to merge completely different commits, that share not a common history. The only option is to use rebase (`git rebase main`), but it gives error because of "no shared history" (again), so the command is

> git rebase --continue

This does not solve conflict between the branches/commits: conflict must be solved by hand and then `git stage conflictingfile.ext` for each conflictingfile.

At the end is possible to use `git merge fromrebasedbranch`, and things works smoothly.
