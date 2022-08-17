
# * Git MERGE vs REBASE
# ? git branch
# ? git log
# ? git checkout branchname
# ? git log
# ? git add .
# ? git commit -m "novi commit grane"
# ponovni prelazak na master sad samo sa
# ? git master
# sto kod mene ne prolazi!?!? pa moram upotrijebiti
# ? git checkout master
# i ako bi sada sa
# ? git merge grana
# stvorio bih jedinstvenu granu u kojoj bi vremenski bili poredani svi komiti mastera i svi komiti grane sa zadnjim komitom tijekom merganja!!!
# To nije losa opcija jer nam daje punu povijest projekta ali ako zelim komite grane spremiti u jedan komit a potom ga mergati sa master-komitima tijekom zadnjeg mergajuceg komita koristim
# ? git merge --squash grana
# na sto je lorenco dobio odgovor
# ? Automatic merge went well; stopped before committing as required
# kad treba unijeti opis tog commit-a
# ? git commit -m "npr grana i master merged"


# kad zelimo da od master-a i njegovog komita-a koji je posluzio kao osnova-basa stvaranja grane potegnemo noviji kommit koji je naknadno nastao u masteru, dok smo u grana-branch-u koristimo komandu
# ? git rebase master
# zahvaljujuci tome prvi komit grana-brancha postaje najnoviji komit u masteru (doslo je do rebase-anja)
# sad kad odemo u master i tamo odradimo istu komandu ali prema branch-u
# ? git rebase grana
# master i grana imat ce zadnji isti zadnji zajednicki komit pa ce do merganja naknadnih komita grane doci bez problema! Master ce imati sve svoje komite + komite grane a HEAD ce biti na grani i master-u

# posle sve price na kraju napomena da rebase mozemo samo u svojim samostalnim i nepublic repoima. Ako bi to radili na drugim mozemo uzrokovati velike zbrke!

# * GIT STASH
# commiti bez komitanja! Ako smo nesto radili ali nismo gotovi, komitanje bi bilo ala dirty-pristup. Zato, "stash"
# ? git stash
# ? Saved working directory and index state WIP on master: a86cvf9 starting code
# promjene koje smo napravili u fajlu ala nestaju a git log pokazuje samo stare komite! Ali ako odradimo
# ? git stash apply
# sve promjene se vracaju u fajl!!! i sad mozemo nastaviti . Ako dodamo jos nesta ali jos uvjek nismo gotovi pa opet stashamo opet sve nase promjene nestaju ali sad imamo sa komandom
# ? git stash list
# mogucnost biranja u koji stash se zelimo vratiti (ala kao komit). Ako samo ponovimo "# ? git stash apply"
# obe promjene se vracaju ali ako koristimo "# ? git stash apply 1"
# tada se mozemo vratiti onoj promjeni koju zelimo!!! prije zadnje stashirane promjene
# ako zelimo stash-zapisima dodati opis onda k-da
# ? git stash push -m "opis"
# ako ne zelimo da se stash-list-a povecava i zelimo izbaciti stare stash-ove k-a
# ? git stash drop 2
# i stash-a 2 vise nese biti na listi, njegov br 2 preuzet ce drugi stash
# ako zelimo konacno izabrati jedan u nas kod to radimo sa
# ? git stash pop(0)
# cime ce stash-verzija 0 biti cut-ana sa stash liste. Ako listu zelimo skroz izbrisati
# ? git stash clear
