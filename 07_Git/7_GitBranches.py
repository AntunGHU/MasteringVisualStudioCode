# 6'13

# Ath in GH i govori o opciji kreiranja new brancha. Idem i ja na ghub i pokusati isto s ovim projektom. Grane su jako korisne pri stvaranju novih funkcionalnosti appova jer omogucavaju samostalan rad i provjeru tih vlastitih promjena izvan tima. Ako se pokazu ok pokazemo! Klika na mater i pisemo "feature/neka_osobina" i klikamo "create branch 'feature/neka_osobina' from master", sto zanci da zadrazava sadasnje stanje mastera. Sad u vsc!

# u vsc kodu pokazuje da smo trenutno na masteru (status bar lijevo) i nakon klika na njega da nam se nude opcije lokalnog kreiranja brancha ali novo kreiranog ogranka na GH nema. Kao trebalo bi da se Pojavljuje se nakon klika na sincronize button! ali nije nam radilo pa 
#? git pull
# kod njega se tekstom pojavljuje obavjest o novoj grani a kod mena samo "Already up to date." Kod njega se nakon klika na master sad nudi nova grana a kod mene ne!?!? Ipak nakon 3 il 4. pokusaja i sync-a pojavilo se!!! Prelazim na novu granu i pisem # Added new usless granu! u poseban red. Pri pokusaju prelaska na novu granu kuzim da je mozda bila tu cijelo vrijeme ali ja nisam sve do sad scrolao i skuzio da ima jos u padajucem izborniku!
#! ADDED NEW USLESS GRANU i vratio se u master
# vratio sam se u master i s iznenadjenjem otkrio da crvena Linija koji sam dodao u /feature... granu postoji i u masteru!?!?. #? kasnija ponavljanja i razmisljanja donijela objasnjenje za ovo: prije komita editirani tekst potencijalno moze zavrsiti bilo gdje, i u mastera i u granama, pa zato prebacivanja na njega ne utjecu, on ostaje potencijal za upis svakome!
# medjutim, jos jedno iznenadjenje, nakon komita u grani i prebacivanja nazad na mastera nisam nasao skoro nista sto sam pisao nakon kreiranja grane na GH!? #? Ovo pak je takodjer normalno - upisao si promjenu i ona se vidi tamo gdje smo htjeli kao i sto se vise nevidi tamo gdje nismo htjeli, tamo se vidi staro stanje!  Zato moram nastaviti pisati u grani (da ne izgubim napisano) s namjerom da kad zavrsim objedinim grane i opet sve imam samo u masteru

# nova Ath ideja: sef rekao da imamo kritikal bug i hitno popravak. nismo bili pazljivi i popravak nastavljamo na masteru. Ovdje tekst u grani zavrsavam i komitam kako bih imao clean state.
 
# Nastavljam u masteru nakon sto sam sav svoj danasnji rad komitao u granu. Nastavak hitnog popravka kritikal-buga! Aut pise svoj scenario a ja opisujem i dosta mi je to kao paralela. Ok, primjetili smo da smo da smo pisali direktno u master sto nesmijemo i nije pametno. Sad cemo sve promjene baciti u novu granu "FeaturFix/DugaGrana" sa komandom
#? git checkout -b FeaturFix/DugaGrana
# svich -b je build branch
# odmah sam se i nasao u toj grani i nastavljam pisati u njoj. Dakle, sve do sada sto sam napravio nalazi mi se u granama. Master od jucer nema nikakvih promjena! Mnogo fajlova i teksta! Hm hm! Komitam ovaj dio rada u drugoj grani. Pojavljuje mi se plavi "PublishBranch" kojeg moram zapisati i napraviti drugi kommit druge grane kako bih imao sve cisto prije daljnjeg. Klikam na Publis isto radi i  Ath. Na kraju pokazuje da su publish-anjem obe grane u GH i da kad budemo htjeli sve u masterati pojavit ce se konflikt koje cemo rjesavati u sljedecoj lekciji. Evo konacno ja sada zavrsavam sa 2. granom i kliknut cu publish nakon sto prvo komitam 2put 2granu!!!
