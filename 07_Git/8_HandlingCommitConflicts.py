# 5'20

# Ovu lekciju pocinjem u master branchu koji prema radu gita logicno nema nista sto sam danas radio, sve se nalazi u granama. Nadam se da cemo uspjeti sve to zamesateljstvo srediti i u konacnici imati gdje treba tj u masteru.

# Ath lekciju pocinje u GH i ukazivanjem na zute novoformirane grane sa buttonom "Compare and PullRequest". Klikamo na Fix-granu sto formira "PullRequest" gdje klikamo na "Create Pull Request". I kod njeg i kod mene se pojavljuje izvjesce da druga grana nema konflikata sa masterom (logicno jer smo master uredno napustili i nastavili u 2.grani). Malo me brine kako ce se to odraziti na sadasnje promjene mastera koje ovaj pull reguest nevidi ali idem dalje... Pull request se vjerovatno odnosi na master i branch na GH, a naknadne ove moje promjene ce se pojaviti kao 1 za gore a promjene mastera na GH bit ce 1 za dole!
# Klikamo na GH na "merge pull request" i "confirm"-amo. Dolazi do pojave poruke o uspjesnom merganju "Pull request successfully merged and closed" i ponude da obrisemo granu. Ath ne brise ali ja cu kasnije
# sad idemo ponovo na nas repo (u GH) gdje vidimo da jos uvijek imamo zutim prvu branchu. On klika ponovo na Compare and request al ja necu prije nego sve opisem jer se bojim da ove moje tekuce promjene previse ne iskopliciraju sve. 
# Njegov klik dovodi do pojave poruke o konfliktu i da se ne moze automatski mergati jer ima koflikte koji se trebaju resolvati. To resolvanje mozemo raditi i na GH ali Ath bira to pokazati na lokalnom nivou. Mjenja brench na feature branch, sto zanci da i ja trebam preci tamo. Ok, preci cu i nastaviti pisati u ovaj fajl unutar feature-grane. Sad zavrsavam, komitam i sinkroniziram mastere, pa cu onda kliknuti na PullRequest i prijeci na feature lokal granu.

# Kao sto sam i obecao, nastavljam rad u ovom fajlu ali u feature grani koja ima konflikt u gh. Zaista se i kod mene sve pojavilo kao i u ath.
# 1'51: najbolji nacin za razrjesavanje konflikta je da osobine koje imamo sada u masteru integriramo u feature-granu cime ce konfllikt presti. Naravno to ce za mene zanciti prvo jos jedno clean-commitanje u ovoj grani kako bih imao sve ovo sto pisem.
# Ath prvo obavjestava vsc i local git sa k-dom
#? git checkout master
# da je doslo do promjena na GH-masteru i da se one prvo usklade. To sam ja odradio sa sincom koji je imao 3dole i 1 gor. Ocekujem da se nakon odrade ove k-de takodjer git prebaci ponovo na master te pojavi ista poruka kao i u Ath tj da je master up to date sa GH-musterom. Kad sam to probao git tj bash su to abortali s upozorenjem da bih tako ostao bez ovih promjena tj ovog teksta. Vidi: 
# error: Your local changes to the following files would be overwritten by checkout:
        # 07_Git/8_HandlingCommitConflicts.py
# Please commit your changes or stash them before you switch branches.
# Aborting
# idem komitati ove pisanije pa ponoviti k-du

# ostavljam malo prostora za ubacivanje teksta iz prve grane i nastavljam sa opisom
# Zaista sam dobio poruku istu kao i Ath. Vidi
# Switched to branch 'master'
# Your branch is up to date with 'origin/master'.
# Dalje Ath ukucava dok smo na master-branchu kdu:
#? git pull
# pa cu i ja iako mi se cini da je to meni suvisno. I zaista dobio
# Already up to date.
# Sad cekout-amo feature tj 1 granu sa kdom
#? git checkout feature/neka_osobina
# Dobio isti odgovor kao i ath. Vidi
#Switched to branch 'feature/neka_osobina'
# Your branch is up to date with 'origin/feature/neka_osobina'.
# Sad idemo mergati master u "feature.." dok se nalazimo u toj "feature..." grani komandom:
#? git merge master
# Izmedju ostalih na kraju poruka:"Automatic merge failed; fix conflicts and then commit results" 
# Taj se konflict pojavljuje na nasem "source_control_view" kao izdvojeni fajlovi u view-dijelu i sa detaljima u glavnom (HEADCurrent Change, masterIncoming change) i menijem iznad sa: "AcceptCurrent", "AcceptIncoming", "Accept both", "CompareChanges"
# Ath i ja prihvacamo both changes nakon cega ih u View-djelu Stage-amo (i tako sa svakim fajlom u konfliktu pojedinacno) a potom i komitamo (uz komit poruku!
# Ako sada idemo u GH vidimo da se pojavila poruka da je Automtski merge moguc, da se u dijalogu o merganju takodjer pojavio Commit mesage napravljen tjekom merganja i da mozemo kliknuti na Marge button. To i cinimo i time smo ucunili da je master na gh sada sa svim i nekonfliktnim promjenama!!!
# To dokazujemo prelaskom na master(GH) i uocavajuci da su u njemu sada sve promjene napravljene kroz Fix i feature granu!!!
# Meni se cini da je jos nedoreceno to da moramo pull-ati master(GH) na local master!!
