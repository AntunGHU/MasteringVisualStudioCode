# 4'46
# ulazimo u GH i kreiramo repo istog imena, ja odustajem od gitvjezbe i kreiram ga za Mastering... ali posto se odmah nakon kde 
#? git init
# pojavilo gomila fajlova (preko 2K) odlucio sam projekte izmjestiti u negitivanu istoimenu paralelnu mapu Mastering...Projects
# Potom sam sa VSC add-ao sve Unstagane a potom komitao sa porukom "Prvi komit". VSC odmah ponudio opciju publish koju sam ja kliknuo i dobio opciju na GH-private i opciju GH-public. Izabrao public i sve je odradjeno bez greske (zato sto VSC ima moje GH kredencije od prije apravljenje je sam odradio)
# ulazim na gh i uvjeravam se da je sve ok
# dalje nastavljam pisati kao da sam s Ath nastavio preko terminala, nakon sto smo rucno napravili istoimeni project na GH
# kopiramo sa buttonom "copy" url novostvorenog projecta, moj je
#? https://github.com/AntunGHU/MasteringVisualStudioCode.git
# Upada u oci da su repoi prvi level github-a pa se pitam sta su onda projecti, trebalo bi to malo pogledati, napamet mi dolazi onaj dobri glas i tecaj o GH. S Kopiranim url pravimo kodu
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