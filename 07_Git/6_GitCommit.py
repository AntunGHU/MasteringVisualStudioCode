# 4'15

# sada Ath pokazuje dogadjanja kad se fajlovi modificiraju, odmah se pojavi M uz fajl, i ako sad ja kliknem na GitView  pa na njega (fajl sa M) u glavnom djelu se pojavi podjeljeno GitCommit verzija fajla i WorkingTree verzija tako da mozemo uociti modificirane razlike fajla u odnosu na vrijeme njegova komitanja
# Ako zelimo da uz Addanje i Commitamo promjene dodajemo tekst i klik na zakacku
# Preporuka je da commit-tekst bude jasan ali sto manji
#! Preporuka je i da kommit bude sto cesci, cim napravimo promjene unutar jednog projektnog fajla, nikako raditi gomilu promjena na gomili fajlova pa onda komitati!

# Discard-anje ucinjenih promjena se radi prije stage for commit klikom na ukrivljenu strelicu u redu "Changes".  Ako promjene zelimo stage-ti klik na + pojedinacnog fajla ili na + "Changes" linije sto ce stage-ati sve modificirane fajlove.
#todo U liniji "Changes" uz plus i Discard strelicu imamo i kombinatorni znak ukrivljene strelice sa plusom koji se zove "Stash All Changes" i koji jos nije razjasnjen!!!

# Ath jos istice vaznost odvajanja systemskih fajlova od projekta (instalirao u mapu projekta npm-modul i dobio novih 2K nestage-ani fajlova) i njihovog izuzeca kroz fajl ".gitignore". Kod Ath se automatski pojavilo upozorenje i prijedlog da se ta mapa nastala instalacijom npm-a smjesti u .gitignore
# Klik na Yes i stvara se fajl ".gitignore" (svaki repo ga mora imati) a stvorena mapa npm-a se vise ne prati u git-u

#  isao bih i ja instalirati nesto  da isprovociram stvarnje ".gitignore" ali bojim se da ce zavrsiti globalno posto nemam virtenv a napamet vec ne znam, zaboravio!!!
#todo .gitignore