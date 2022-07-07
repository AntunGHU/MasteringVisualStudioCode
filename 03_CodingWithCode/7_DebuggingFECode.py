# 9'23''
# za browserske appse uvjek mozemo koristiti builtin debugere (u firefoxa nakon inspect otvara se niz tabova sa Inspector, Console i odmah i Debuger, u opere malo drugacije i debuger-a eksplicitno nema)
# problem je sto za vece projekte i frameworkove sve postane pretrpano i tesko naci ponesto
# srecom vsc tu uskace: Klik DebugView, kl "create launch.json" i bira Chrome(preview), brise sve u configu i ide s novom: "type":"chrome" (odmah pobuna - nema extensije pa instalira Debugger for Chrome), "request":"launch" (kad pritisnemo debugrunner lansirace tj otvoriti nas browser), "name":"Launch local file"(radi displey imena kad pocne), i sad najvazniji korak - "fajl":"${workspaceFolder}/index.html" (vsc sam prepoznaje koji fajl!!!)
# ponovo klikamo na DebugView i na vrhu se odmah uocava ime  "Launch local file" pored Debugrunnera, klik na runera i prvo u DebugConsole se pocinje desavati a potom se ukljucuje browser sa nasim index-fajlom, status bar vsc-orange!
# Bira neki drugi fajl projekta (DataService.js) i stavlja BP i klika na brovser tag - hita se BP!!!
# Huge Step for WebDevlopment, 
# Ponovo iddemo u DebugView i pregledavamo! Istice jedan trik koji mi sad nista neznaci ali povratit cemo se!
# Zaustavlja  i pravi novu konfiguraciju kako bi pokazao debug programa koji run-a inside server!? Zato je instalirao ekstenziiju LiveServer. Nakon instala klikam na GoLive i project run-a unutar servera na 127.0.0.1:5500. Potpuno je isto!
# Kad je to ostvario pokazuje kako debugamo projekt koji runa unutar LiveServera:NovaConfiguracija:"type":"chrome", "request":"launch", "name":"AtachToChrome", "webRoot":"${workspaceFolder}", "url":"http://localhost:5500"(LiveServer po defu 8080)
# DebugView, AtachedToChrome, klik DebugRuner, browserOn, orangeStatusBar, klik ponovo na nas DebugView i BP je hitan