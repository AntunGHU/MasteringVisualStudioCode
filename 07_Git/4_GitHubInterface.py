# 4'46

# ulazimo u GH i kreiramo repo istog imena, ja odustajem od gitvjezbe i kreiram ga za Mastering... ali posto se odmah nakon kde 
#? git init
# pojavilo gomila fajlova (preko 2K) odlucio sam projekte izmjestiti u negitivanu istoimenu paralelnu mapu Mastering...Projects
# Potom sam sa VSC add-ao sve Unstagane a potom komitao sa porukom "Prvi komit". VSC odmah ponudio opciju publish koju sam ja kliknuo i dobio opciju na GH-private i opciju GH-public. Izabrao public i sve je odradjeno bez greske (zato sto VSC ima moje GH kredencije od prije apravljenje je sam odradio) # ulazim na gh i uvjeravam se da je sve ok

# dalje nastavljam pisati kao da sam s Ath nastavio preko terminala, nakon sto smo rucno napravili istoimeni project na GH

# kopiramo sa buttonom "copy" url novostvorenog projecta, moj je
#? https://github.com/AntunGHU/MasteringVisualStudioCode.git
#todo Upada u oci da su repoi prvi level github-a pa se pitam sta su onda projecti, trebalo bi to malo pogledati, napamet mi dolazi onaj dobri glas i tecaj o GH. 
# S Kopiranim url pravimo kdu
#? git remote add origin https://github.com/AntunGHU/MasteringVisualStudioCode.git
# nista se ne desava osim sto git upisuje u config fajl url naseg remote repoa. Sad mozemo pushati sa
#? git push origin master

# Ath je morao dodavati username i pass, ja prije VSC-koda sam morao username i token u termu, sada se kroz vsc jednom daju vjerodajnice GH-u i poslije ide bez zadrske!
# Ath osvjezava i pokazuje da je na GH doputovao repo, te koristi priliku da malo explora GH
# GH: username/remoterepo, code, commits, issues, pull request...
# Pokazuje jedan malo veci projest u JS i pulla ga nakon sto je kopirao url na svoj pc s k-dom u koju sam ja namjerno stavio url svog projecta
#? git clone https://github.com/AntunGHU/MasteringVisualStudioCode.git      # Cloning into 'imerepoakoji se clonira' ...
#? ls   # 'imerepoakoji se clonirao'
#? cd imerepoakoji se clonirao      # ls i sve je tu
#? code .       # otvaram ga u vsc!

# Sjetio se konacno pokusati naci odgovor na moju zbunjolsku ideju kodiranja sa dva Pcia i nasao!!!

# How do I code against one github repo on 2 computers?
    # To keep both repositories in sync you should to pull the latest changes to your machine whenever you start working on the code. To do this you want to execute
    #? git pull
    # ...which is usually set up to pull from the default remote (origin) to your current branch. Git might complain if this isn't the case, and so the longer version will work as well:
    #? git pull origin {branch_name}
    # Note: this is the same process that you would use if two or more people were working on the same repo. Which is essentially what is happening, instead of two different people working on the same repository, you have two different machines working on the same repository. If you are starting out fresh on a new machine all you need to do is clone the repo to it first:
    #? git clone {remote_url}
    # You get this url from your GitHub repo's home page. This command will make a complete working copy of the repo in a subdirectory.
    
# Yes you can either call "git init" and then the "git pull" you stated or you can use "git clone" both essentially will get you to the same spot. Just remember to setup your remote origin. 
#? git remote add origin git@github.com:username/reponame.git 
# so that you have a place to push your changes to. – Nick Berardi;  May 16, 2011 at 0:10

# You need to clone the repository on your second computer.
#? git clone git@github.com:myusername/myrepo.git
# Now you can use "git pull" and "git push" to keep your local repository in sync with the one on GitHub.

# More or less the same process. If you were done for the night on computer1, you want to make sure you push it to the remote branch so you have access to it on computer2. Often times if my stopping point is time, (like bedtime) and not a ready to go point, i personally just decided to call those commit messages (nightly commit <and description what I'm working on/left off>). Than when I see a nightly commit, I know it's not a good bookmark, and it's certainly not complete. Make sure to push to the branch by git push origin branch-name before closing down.
# Than when you get to computer2, you can fetch and merge, or pull (which is a fetch and merge done automatically by git) the remote branch, and continue your work on it.

