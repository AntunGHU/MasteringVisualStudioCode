# 
# Kao sto sam i obecao, nastavljam rad u ovom fajlu ali u feature grani koja ima konflikt u gh. Zaista se i kod mene sve pojavilo kao i u ath.
# najbolji nacin za razrjesavanje konflikta je da osobine koje imamo sada u masteru integriramo u feature-granu cime ce konfllikt presti. Naravno to ce za mene zanciti prvo jos jedno clean-commitanje u ovoj grani kako bih imao sve ovo sto pisem.
# Ath prvo obavjestava vsc i local git sa k-dom
#? git checkout master
# da je doslo do promjena na GH-masteru i da se one prvo usklade. To sam ja odradio sa sincom koji je imao 3dole i 1 gor. Ocekujem da se nakon odrade ove k-de takodjer git prebaci ponovo na master te pojavi ista poruka kao i u Ath tj da je master up to date sa GH-musterom. Kad sam to probao git tj bash su to abortali s upozorenjem da bih tako ostao bez ovih promjena tj ovog teksta. Vidi: 
# error: Your local changes to the following files would be overwritten by checkout:
        # 07_Git/8_HandlingCommitConflicts.py
# Please commit your changes or stash them before you switch branches.
# Aborting
# idem komitati ove pisanije pa ponoviti k-du