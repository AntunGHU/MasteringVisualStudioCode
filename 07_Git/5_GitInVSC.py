# 4'41
# Ath je u term-djelu gitovanja dosao do dva fatal outputa kad je pokusao git status i git push. Takodjer je imao niz drugih k-di i radnji. sad sve to pokusavamo kroz VSC. 
# On ide u proizvoljnu  mapu bez gita a ja idem u Mosha sa drugim prozorom vsc
# Prije iniciranja gita postavljamo term na output i gitview sto nam pokazuje da je git samim klikom na git na acitity baru isao provjeriti stanje mape-projecta po pitanju pracenja koda. Niz je izlaza koje je napravio:
#todo  [2022-07-07T07:00:58.888Z] Log level: Info;
#todo  [2022-07-07T07:00:58.889Z] [info] Validating found git in: git
#todo  [2022-07-07T07:00:58.917Z] [info] Using git 2.25.1 from git
#todo  [2022-07-07T07:00:58.949Z] > git rev-parse --show-toplevel [23ms]
#todo  [2022-07-07T07:00:58.949Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.004Z] > git rev-parse --show-toplevel [49ms]
#todo  [2022-07-07T07:00:59.004Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.031Z] > git rev-parse --show-toplevel [22ms]
#todo  [2022-07-07T07:00:59.031Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.081Z] > git rev-parse --show-toplevel [44ms]
#todo  [2022-07-07T07:00:59.081Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.101Z] > git rev-parse --show-toplevel [15ms]
#todo  [2022-07-07T07:00:59.101Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.108Z] > git rev-parse --show-toplevel [1ms]
#todo  [2022-07-07T07:00:59.108Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.144Z] > git rev-parse --show-toplevel [29ms]
#todo  [2022-07-07T07:00:59.144Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.221Z] > git rev-parse --show-toplevel [71ms]
#todo  [2022-07-07T07:00:59.221Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.231Z] > git rev-parse --show-toplevel [5ms]
#todo  [2022-07-07T07:00:59.231Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.307Z] > git rev-parse --show-toplevel [69ms]
#todo  [2022-07-07T07:00:59.307Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.324Z] > git rev-parse --show-toplevel [9ms]
#todo  [2022-07-07T07:00:59.324Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.334Z] > git rev-parse --show-toplevel [3ms]
#todo  [2022-07-07T07:00:59.334Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.342Z] > git rev-parse --show-toplevel [1ms]
#todo  [2022-07-07T07:00:59.342Z] fatal: not a git repository (or any of the parent directories): .git
#todo  [2022-07-07T07:00:59.350Z] > git rev-parse --show-toplevel [1ms]
#todo  [2022-07-07T07:00:59.350Z] fatal: not a git repository (or any of the parent directories): .git

# dakle vidi se da je sami klik na /activitybar/git proizveo 1. fatal
# unutar polja GitView pojavljuju se plave opcije: "InitializeRepository" i "Publish to GitHub"
# Ath nema plave opcije (starija verzija VSC) pa bira s padajuceg izbornika. Ja klikam na plavi button "Initialze.." pa stageam u changed i commitam sa kvacicvom. Oba dobivamo na izlazu niz komandi a glavna je init, pa add pa commit:
#todo [2022-07-07T07:13:16.143Z] > git init [10ms]
#todo [2022-07-07T07:13:16.277Z] > git rev-parse --show-toplevel [1ms]
#todo [2022-07-07T07:13:16.289Z] > git rev-parse --git-dir --git-common-dir [1ms]
#todo [2022-07-07T07:13:16.294Z] [info] Open repository: /home/antun/Documents/aCod/HsomPy
#todo [2022-07-07T07:13:16.323Z] > git status -z -uall [1ms]
#todo [2022-07-07T07:13:16.333Z] > git fetch [20ms]
#todo [2022-07-07T07:13:16.334Z] > git config --global user.email [31ms]
#todo [2022-07-07T07:13:16.345Z] > git symbolic-ref --short HEAD [12ms]
#todo [2022-07-07T07:13:16.355Z] > git config --global user.name [11ms]
#todo [2022-07-07T07:13:16.356Z] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%#todo (upstream:remotename)%00%(upstream:remoteref) refs/heads/master refs/remotes/master [1ms]
#todo [2022-07-07T07:13:16.376Z] > git for-each-ref --sort -committerdate --format %(refname) %(objectname) %(*objectname) [10ms]
#todo [2022-07-07T07:13:16.376Z] > git remote --verbose [1ms]
#todo [2022-07-07T07:13:16.444Z] > git config --get commit.template [57ms]
#todo [2022-07-07T07:13:16.454Z] > git status -z -uall [1ms]
#todo [2022-07-07T07:13:16.464Z] > git symbolic-ref --short HEAD [2ms]
#todo [2022-07-07T07:13:16.473Z] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%#todo (upstream:remotename)%00%(upstream:remoteref) refs/heads/master refs/remotes/master [1ms]
#todo [2022-07-07T07:13:16.492Z] > git for-each-ref --sort -committerdate --format %(refname) %(objectname) %(*objectname) [9ms]
#todo [2022-07-07T07:13:16.492Z] > git remote --verbose [1ms]
#todo [2022-07-07T07:13:16.503Z] > git config --get commit.template [1ms]
#todo [2022-07-07T07:13:16.513Z] > git status -z -uall [1ms]
#todo [2022-07-07T07:13:16.524Z] > git symbolic-ref --short HEAD [1ms]
#todo [2022-07-07T07:13:16.537Z] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%#todo (upstream:remotename)%00%(upstream:remoteref) refs/heads/master refs/remotes/master [1ms]
#todo [2022-07-07T07:13:16.561Z] > git for-each-ref --sort -committerdate --format %(refname) %(objectname) %(*objectname) [13ms]
#todo [2022-07-07T07:13:16.561Z] > git remote --verbose [3ms]
#todo [2022-07-07T07:13:16.585Z] > git config --get commit.template [1ms]
#todo [2022-07-07T07:13:17.095Z] > git check-ignore -v -z --stdin [3ms]

# jednostavno je teko navesti sve razlike starije i novije verzije, ali rad s git i vsc je jednostavan pogotovo danas
# Ath probava pushati pa dobije upozorenje da nema remote repo, ide i kreira ga kao mjesto gdje ce pushati. Copira njegov url!
# Ide u csp i kuca "git add remote" (to je ono sto bih ja trebao na poslu napraviti da sve ide odande!!!) Dakle
#! git add remote
#! paste url remote repoa!!!
#! paste remote name (obicno "origin")
#! pogledati u config fajl jeli tamo naveden pravi origin i pushati!