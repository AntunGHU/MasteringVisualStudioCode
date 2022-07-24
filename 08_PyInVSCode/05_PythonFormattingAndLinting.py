# 5'17

# prica pocinje pokazom sto se desava ako py-fajl nije dobro spejsiran: nastaje error i javlja se ponuda instala autopep8.
# to se isto desava ako biramo csp pa "documet formate" 
# klikamo na "yes" i instaliramo autopep8; njemu javilo da nema pip instaler-a kojeg on instalira sa 
#? sudo apt install python3-pip
# ponovo provocira sa "format Document" instal autopep8 i "yes"
# pokazuje kao se ljepo poravi los spacing ali jos mu fali lintanje koje on instalira s k-dom (zaobilazi skocnu ponudu kao Mosh)
#? sudo pip install pylint
# pokazuje kao sad ako save bez formating linter podvlaci greske (orange). Dalje kreira u root-u projecta fajl ".pylintrc" i unjeg upisuje: odjeljak [MESSAGS CONTROL] i unos "disable=all" i "enable=Errors"
# ako iz nekog razloga pylint ne radi mozemo u termu provjeriti sa 
#? which pylint
# meni vratio
#? /home/antun/.local/bin/pylint
# a potom ide u settings i trazi pylintPath te path kojeg nam je term izbacio upastati u odjeljak settingsa kojeg smo dobili
# ako nam neka lintova upozorenja smetaju sa hoverom otkrijemo kako se zove, kopiramo i odemo u lokalni ".pylintrc" i dodamo unos "disable=xxx-statement"