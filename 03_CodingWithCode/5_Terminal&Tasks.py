# 5'48

# otvaranje sa drag bottom line ili "c`"
# shell -bash starts in the working folder
# mozemo runati vise terminala istovremeno, mogu se i oni splitati

# posebnost mu je task menu koji nudi mogucnosti automatizacije
# vrlo dokumentirana osobina u vsc-doc: "Integrate w/ external tools via tasks"
# run task, cofigure task, create task.json file from template (MSBuild, maven, .NET Core, Others), Others, i .. stvara se fajl "task.json" koji daje template echo-shell.

# sad poslije run task imam u izborniku echo-task, klikam ga i biram opciju "continue without scanning" i u terminalu se odradjuje task echo (ispisuje se Helo!)
# sad novi "run build task" i biram "tsc:build - tsconfig.json" i odvija se kompilacija mog tsc-fajla u js-fajl
# opcija "cofigure task" omogucava koristenje other tasks kao npr npm:install sto ce popuniti "task.json" sa sadrzajem tog novog taska i izvrsit ce npm install za novi project.
# json taskovi sastoje se od json {} sekvenci koje sadrze unose kao sto su: "label", "type", "command", "script", "problemMatcher", "detail", "args", "options", "dependsOn", "cwd"

# na kraju posteno kaze da za 4 godine koristenja vsc-ea nikad nije koristio taskse ali maybe...
# posebno se zahtjeva taskanje sa C/C++
