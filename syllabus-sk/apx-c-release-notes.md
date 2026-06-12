# Poznámky k vydaniu 

Učebné osnovy ISTQB® základnej úrovne (ISTQB® Foundation Level Syllabus) v4.0 sú významnou aktualizáciou, ktorá vychádza z predchádzajúcej verzie 3.1.1 osnov základnej úrovne a z učebných osnov Agile Tester 2014. Z tohto dôvodu neexistujú detailné poznámky k vydaniu (release notes) na úrovni jednotlivých kapitol a sekcií a prehľad zásadných zmien je uvedený v tejto kapitole.

Okrem toho poskytuje ISTQB® (v samostatných poznámkach k vydaniu) trasovateľnosť medzi študijnými cieľmi (LO) učebných osnov základnej úrovne vo verzii 3.1.1, študijnými cieľmi učebných osnov Agile Tester verzia 2014 a študijnými cieľmi učebných osnov základnej úrovne vo verzii 4.0, okrem toho sa zdôraznilo, ktoré študijné ciele boli pridané, aktualizované alebo odstránené.

V čase, keď boli tieto učebné osnovy vytvorené (2022 – 2023) bolo evidovaných viac ako 1 000 000 osôb vo viac ako 100 krajinách, ktoré absolvovali skúšku základnej úrovne. Celosvetovo existuje viac ako 800 000 certifikovaných testerov. Za predpokladu, že si všetci z nich prečítali učebné osnovy základnej úrovne s cieľom zložiť skúšku, je možné povedať, že ide pravdepodobne o najčítanejší dokument v oblasti testovania vôbec. Táto aktualizácia je vytvorená tak, aby tieto hodnoty rešpektovala a tiež, aby prispela k zlepšeniu názorov na úroveň kvality, ktorú ISTQB® prináša globálnej testovacej komunite.

V tejto verzii boli všetky študijné ciele upravené tak, aby boli atomické, a aby bola vytvorená trasovateľnosť 1:1 medzi študijnými cieľmi a kapitolami učebných osnov. Inými slovami, učebné osnovy neobsahujú kapitoly a obsah, ku ktorým neexistuje študijný cieľ. Cieľom je uľahčiť čítanie, porozumenie, učenie a preklad s dôrazom na zvýšenie praktickej užitočnosti a rovnováhy medzi znalosťami a zručnosťami.

V tejto verzii došlo k nasledujúcim zmenám:

* Zmenšenie celkovej veľkosti osnov. Učebné osnovy nie sú učebnice, ale dokument, ktorý slúži na načrtnutie základnej kostry akéhokoľvek úvodného kurzu o testovaní softvéru vrátane informácií o tom, aké témy by mali byť pokryté a na akej úrovni. To znamená nasledujúce:
	* Vo väčšine prípadov sú z textu vylúčené príklady. Úlohou poskytovateľa školenia je potom tieto príklady (vrátane praktických cvičení) poskytnúť počas školenia.
	* Bol dodržaný princíp „Veľkosť textu vzhľadom ku K-úrovni“, ktorý definuje maximálnu veľkosť textu pre študijné ciele na každej úrovni K (K1 = max. 10 riadkov, K2 = max. 15 riadkov, K3 = max. 25 riadkov).
* Zníženie počtu študijných cieľov v porovnaní s osnovami základnej úrovne (CTFL) verzie 3.1.1 a Agile Tester (CTFL-AT) verzie 2014:
	* 14 K1 cieľov (FL v3.1.1 mala 15 cieľov a AT 2014 6 cieľov),
	* 42 K2 cieľov (FL v3.1.1 mala 40 cieľov a AT 2014 13 cieľov),
	* 8 K3 cieľov (FL v3.1.1 mala 7 cieľov a AT 2014 8 cieľov).
* K dispozícii sú rozsiahlejšie odkazy na klasické a/alebo uznávané knihy a články o testovaní softvéru
a súvisiacich témach.
* Hlavné zmeny v kapitole 1 (Základy testovania)
	* Bola rozšírená a vylepšená podkapitola o testovacích zručnostiach.
	* Bola pridaná podkapitola o tímovom prístupe (K1).
	* Podkapitola o nezávislosti testovania bola presunutá z kapitoly 5 do kapitoly 1.
* Hlavné zmeny v kapitole 2 (Testovanie v rámci SDLC)
	* Podkapitoly 2.1.1 a 2.1.2 boli prepracované a vylepšené, zároveň boli upravené zodpovedajúce študijné ciele.
	* Je kladený vyšší dôraz na techniky vývoja iniciovaného testami (K1), prístupu shift-left (K2)
a retrospektívy (K2).
	* Pridaná nová podkapitola o testovaní v kontexte DevOps (K2).
	* Úroveň integračného testovania bola rozdelená do dvoch samostatných testovacích úrovní (testovanie integrácie komponentov a testovanie integrácie systému).
* Hlavné zmeny v kapitole 3 (Statické testovanie)
	* Podkapitola o technikách revízie spolu so zodpovedajúcim študijným cieľom „(K3) Použiť techniku revízie“ bola odstránená.
* Hlavné zmeny v kapitole 4 (Testovacia analýza a návrh testov)
	* Testovanie prípadov použitia bolo odstránené (ale je stále predmetom osnov Advanced Test Analyst).
	* Vyšší dôraz je kladený na techniky testovania založených na spolupráci (pridaný nový K3 študijný cieľ o použití ATDD na odvodenie testovacích prípadov a dva nové K2 ciele o užívateľských scenároch a akceptačných kritériách).
	* Testovanie a pokrytie rozhodnutí nahradené testovaním a pokrytím vetiev (po prvé, termín pokrytia vetiev sa v praxi používa viac; za druhé, rôzne štandardy definujú termín rozhodnutia odlišne od vetvy; po tretie, rieši to drobný, ale závažný nedostatok zo starých osnov základnej úrovne verzie 2018, kde je napísané, že „100% pokrytie rozhodnutia znamená 100% pokrytie príkazov“ – táto veta nie je pravdivá v prípade kódu bez podmienok alebo cyklov, teda bez bodov rozhodnutia).
	* Bola vylepšená podkapitola o hodnote testovania bielej skrinky.
* Hlavné zmeny v kapitole 5 (Manažment testovania)
	* Oddiel o testovacích stratégiách/prístupoch bol odstránený.
	* Pridaný nový K3 študijný cieľ o technikách odhadovania úsilia potrebného na testovanie.
	* Je kladený vyšší dôraz na všeobecne známe agilné koncepty a nástroje pri manažmente testovania: plánovanie iterácií a vydaní (K1), testovacia pyramída (K1) a kvadranty testovania (K2).
	* Oddiel o manažmente rizík je lepšie štruktúrovaný popisom štyroch hlavných činností: identifikácia rizík, posúdenie rizík, zmiernenie rizík a monitoring rizík.
* Hlavné zmeny v kapitole 6 (Testovacie nástroje)
	* Rozsah textu o automatizácii testov bol znížený z dôvodu príliš vysokej odbornosti nevhodnej pre učebné osnovy základnej úrovne. 
	* Podkapitola o výbere nástrojov, realizácii pilotných projektov a zavádzaní nástrojov do organizácie bola odstránená.