# 4'03
#? mkdir gitvjezba
#? cd gitvjezba
#? git status   # fatal: not a git repository (or any of the parent directories): .git
#? git init     # Initialized empty Git repository in /home/antun/Documents/aCod/zGitVsc/MasteringVisualStudioCode/gitvjezba/.git/
# kreirao se skriveni folder .git unutar koga se nalaze mape: branches, hooks, info, objects, refs te fajlovi config, description i HEAD
#? git status   # On branch master; No commits yet; nothing to commit (create/copy files and use "git add" to track)
#? touch initgitf.txt
#? git status   # On branch master; No commits yet; Untracked files:(use "git add <file>..." to include in what will be committed) initgitf.txt; nothing added to commit but untracked files present (use "git add" to track)
#? git add .
#? git status   # On branch master; No commits yet; Changes to be committed: ;   (use "git rm --cached <file>..." to unstage) ; new file:   initgitf.txt
#? git commit -m "First commit"     # [master (root-commit) cf8c52f] First commit;  1 file changed, 0 insertions(+), 0 deletions(-);  create mode 100644 initgitf.txt
#? git status   # On branch master; nothing to commit, working tree clean
#? git push     # fatal: No configured push destination.; Either specify the URL from the command-line or configure a remote repository using; git remote add <name> <url>; and then push using the remote name; git push <name>
# da bi ovo napravili trebamo remote repo in GitHub istog imena kao nasa mapa "gitvjezba" Uci cemo na GH i napraviti je! (next lekcija)