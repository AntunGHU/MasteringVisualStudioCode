# 9'22''

# DebugView - trokut sa bugicom
# Nakon klika kod Ath opcije: "Run&Debug", "JavaScriptDebugTerminal" i "DebugURL". Kod mene samo 1. opcija

# Ispod pise a i on kaze da ako nemamo nikakvu debug-configuraciju klikamo na "create launch.json file", klika i bira environment izmedju ponudjenih opcija (chrome, edge, nodejs, more..). Bira NodeJs for demo i otvara se "launch.json"
# imamo "configurations"-array u koju cemo staviti nasu debug configuraciju. Vec u array-u: "type":"node", "request":"launch"(ili "atach"), "name":"Launch Program"(on ga mjenja u "JS Debug" i to se ocitava pokraj trokuta Debug-starta), "skipFiles":["<node_internals>/**"], "program":"${workspaceFolder}/index.js" (najvazniji dio objasnjenja. on tu iz Launcher.js-a kopira relativ path i mece ga na mjesto index.js-a tako da on sad izgleda: "program":"${workspaceFolder}/dist/src/Launcher.js" )

# nakon izrade launch.json fajla idemo u debugView i klikamo green trokut uz debugrunner i debug pocinje! (status traka postaje narancasta!)
# prebacujemo se na "debug console" tab terminala i vidimo poruke poput: "started app", "server started", a u glavnom djelu se vrti fajl Launcher.js (onaj kojeg smo stavili u komandu) U tjeku toga postavljamo break pointe, on bira drugi fajl "Server.js" i stavlja BreakPoint nasumce u L55. Sad ide u browser i pravi reguest u url baru sto reruna citav projekt pa time i Server.js sto dovodi do hit-a u breakpoint!!!
# Program se zaustavlja i mozemo hooverati iznad koda i dobiti vise informacija o njemu. DebugView kaze da imamo activ-ssesion.
# Hvali DebugView kao invaluable source of informations: sto sve imamo u brekpoint-u (varijable, sessionTokene, userCredDBAccess itd) sto omogucava s lakocom uvid sto se desava u kodu!

# Osim BREAKPOINT-a u DebugView-u imamo i VARIABLES, WATCH, LOADED SCRIPTS, CALL STACK, 
# Debug traka korespodira sa brekpoint-ima: Continue, StepOver, StepInto, Stepout, Reload(rerun), StopConfig - vrlo powerfull!!
# Sad on dalje pila sa TS-projektom i ubacuje, izbacuje parametre, usput "don't try to understand!!"
# mece brakpointe - crvene tocke, kad se bp hitne pretvori se u klizac (ala pdb-stop)

# debugging je very, very complex funcionality of VSC!!! Ima puno nacina konfiguracije Debugera u TS!
# preporuca guglanje za "vsc debug recipes" i odlazak na GitHub page u kojem imamo debug-configurations za lot of different projects i bit ces u stanju debug your project no meter how complex ili koji framework you use!