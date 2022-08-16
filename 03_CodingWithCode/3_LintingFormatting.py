# 8'27

# Linting=StaticCodeAnalysisTool - tj gleda jel po standardu s uvlakama i sl tj prema best-practices
# Za JS imamo ESLint a za ostale dolazi u njihovim ekstenzijama. Instaliarmo ekstenziju
# ESLint slicno kao i Py-ext, samo je tek prvi korak poslije kojeg treba u termu vrsiti globalne ili lokalne instalacije (u paket package.json) s k-dom u termu
# ? npm install  --save-dev eslint
# sto instalira paket (ili u) package.json (lokalno)
# dalje pokazuje postelavanje ESLint-a: 1)sa comandom iz komandpalete ESLint Configuration sto u terminalu dovodi do pojave prompta
# ? eslint --init
# i niza pitanja za konfig eslinta (kod mene jos ne jer nisam instalirao npm itd, kasnije):
# How would you like to use ESLint
# What type of modules does your project use
# Which framework does your proj..
# TypeScript?
# Where does your project run?
# How would you like to define a style for your project
# Which style guide would you like to follow?
# What format do you want your config-file to be in? json
# pojavljuje se u projektu fajl "".eslint.json"
# otvara js-fajl i za pocetak primjene eslint-a jos treba ikonu ESLint u status bar kliknuti i odabrati "Allow ESLint evrywhere" (u fajlu se pojavljuje gomila gresaka...)(zato se ESLint koristi na pocetku projekta...)
# U problemView i pregledanje... koristenje "QuickFix-a" (ako postoji) ili "check fix all autofixable problems"
# pokazuje da se cak i u eslint.json fajlu moze komentirati!!!, komentirao strogi arbnb guide i ide na odjeljak rules i koristenjem spacea tj autocompletion-a pokazuje sve moguce opcije koje mu se pojavljuju: izabrao "no-trailing-spaces" i potom ide (ispred) i bira "csp" i "format Document"
