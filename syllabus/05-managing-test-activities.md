# 5. Zarządzanie czynnościami testowymi – 335 minut

## Słowa kluczowe

analiza ryzyka, identyfikacja ryzyka, kontrola ryzyka, kryteria wejścia, kryteria wyjścia, kwadranty testowe, łagodzenie ryzyka, monitorowanie ryzyka, monitorowanie testów, nadzór nad testami, ocena ryzyka, piramida testów, plan testów, planowanie testów, podejście do testowania, poziom ryzyka, raport o defekcie, raport o postępie testów, ryzyko, ryzyko produktowe, ryzyko projektowe, strategia testów, sumaryczny raport z testów, testowanie oparte na ryzyku, zarządzanie defektami, zarządzanie ryzykiem

## Cele nauczania dla rozdziału 5

5.1 Planowanie testów
    FL-5.1.1 (K2) Omówić na przykładach cel i treść planu testów.
    FL-5.1.2 (K1) Rozpoznawać, jaki jest wkład testera w planowanie iteracji i wydań.
    FL-5.1.3 (K2) Porównać i zestawiać ze sobą kryteria wejścia i kryteria wyjścia.
    FL-5.1.4 (K3) Obliczyć pracochłonność testowania przy użyciu technik szacowania.
    FL-5.1.5 (K3) Stosować priorytetyzację przypadków testowych.
    FL-5.1.6 (K1) Pamiętać pojęcia związane z piramidą testów.
    FL-5.1.7 (K2) Podsumować kwadranty testowe oraz ich relację do poziomów testów i typów testów.
5.2 Zarządzanie ryzykiem
    FL-5.2.1 (K1) Określać poziom ryzyka na podstawie prawdopodobieństwa ryzyka i wpływu ryzyka.
    FL-5.2.2 (K2) Rozróżniać ryzyka projektowe i produktowe.
    FL-5.2.3 (K2) Wyjaśnić potencjalny wpływ analizy ryzyka produktowego na staranność i zakres testów.
    FL-5.2.4 (K2) Wyjaśnić, jakie środki można podjąć w odpowiedzi na przeanalizowane ryzyka produktowe.
5.3 Monitorowanie testów, nadzór nad testami i ukończenie testów
    FL-5.3.1 (K1) Pamiętać metryki stosowane w odniesieniu do testowania.
    FL-5.3.2 (K2) Podsumować cele i treść raportów z testów oraz wskazać ich odbiorców.
    FL-5.3.3 (K2) Omówić na przykładach sposób przekazywania informacji o statusie testowania.
5.4 Zarządzanie konfiguracją
    FL-5.4.1 (K2) Podsumować, w jaki sposób zarządzanie konfiguracją wspomaga testowanie.
5.5 Zarządzanie defektami
    FL-5.5.1 (K3) Sporządzić raport o defekcie.

## 5.1. Planowanie testów

### 5.1.1. Cel i treść planu testów

Plan testów opisuje cele, zasoby i procesy związane z projektem testowym. Plan testów:

* dokumentuje sposób i harmonogram realizacji celów testów,
* pomaga zapewnić, że przeprowadzone czynności testowe spełnią ustalone kryteria,
* służy jako środek komunikacji z członkami zespołu i innymi interesariuszami,
* pozwala wykazać, że testowanie będzie zgodne z istniejącą polityką testów i strategią testów (lub wyjaśnia ewentualne odstępstwa od nich).

Planowanie testów kierunkuje myślenie testerów i zmusza ich do zmierzenia się z przyszłymi wyzwaniami związanymi z ryzykami, harmonogramami, relacjami interpersonalnymi,
narzędziami, kosztami, wysiłkiem itp. Proces przygotowywania planu testów (planowanie) pomaga przemyśleć działania niezbędne do osiągnięcia celów testów.

Typowy plan testów dokumentuje:

* kontekst testowania (np. zakres testów, cele testów, podstawa testów),
* założenia i ograniczenia projektu testowego,
* analizę interesariuszy (np. role, obowiązki, znaczenie dla testowania, potrzeby w zakresie zatrudniania i szkoleń),
* sposób komunikacji (np. forma i częstotliwość, szablony dokumentacji),
* rejestr ryzyk (np. ryzyk produktowych i projektowych),
* podejście do testowania (np. poziomy testów, typy testów, techniki testowania, testalia, kryteria wejścia i wyjścia, niezależność testowania, zbierane metryki, wymagania dotyczące danych testowych i środowiska testowego, odstępstwa od polityki testów i strategii testów obowiązujących w organizacji),
* budżet i harmonogram.

Więcej szczegółów na temat planu testów i jego zawartości można znaleźć w normie ISO/IEC/IEEE 29119-3.

### 5.1.2. Wkład testera w planowanie iteracji i wydań

W iteracyjnych modelach wytwarzania oprogramowania zazwyczaj występują dwa rodzaje planowania: planowanie wydania i planowanie iteracji.

**Planowanie wydania** obejmuje perspektywę przyszłego wydania produktu, definiuje i redefiniuje backlog projektu i może obejmować doprecyzowanie większych historyjek użytkownika poprzez ich podział na zestaw mniejszych historyjek użytkownika. Opracowany w ten sposób plan służy też jako podstawa podejścia do testowania i planu testów we wszystkich iteracjach w ramach wydania. Testerzy zaangażowani w planowanie wydania uczestniczą w pisaniu testowalnych historyjek użytkownika i kryteriów akceptacji (patrz podrozdział 4.5), uczestniczą w analizie ryzyka projektowego i produktowego (patrz podrozdział 5.2), szacują wysiłek związany z testowaniem historyjek użytkownika (patrz sekcja 5.1.4), określają podejście do testów i planują testowanie związane z danym wydaniem.

**Planowanie iteracji** obejmuje perspektywę pojedynczej iteracji i dotyczy backlogu tej iteracji (backlogu sprintu). Testerzy zaangażowani w planowanie iteracji uczestniczą w szczegółowej analizie ryzyka związanego z historyjkami użytkownika, określają testowalność historyjek użytkownika, dzielą historyjki użytkownika na zadania (w szczególności na zadania testowe), szacują pracochłonność wszystkich zadań testowych w iteracji oraz identyfikują i udoskonalają funkcjonalne i niefunkcjonalne aspekty przedmiotu testów.

### 5.1.3. Kryteria wejścia i kryteria wyjścia

Kryteria wejścia określają warunki wstępne podjęcia danego działania. Jeśli kryteria wejścia nie są spełnione, prawdopodobnie wykonywana czynność okaże się trudniejsza, bardziej
czasochłonna, kosztowna i ryzykowna. Kryteria wyjścia określają, co należy osiągnąć, aby uznać czynność za zakończoną. Kryteria wejścia i wyjścia powinny być określone dla każdego poziomu testów i będą się różnić w zależności od celów testów.

Typowe kryteria wejścia obejmują: dostępność zasobów (np. ludzi, narzędzi, środowisk, danych testowych, budżetu, czasu), dostępność testaliów (np. podstawy testów, testowalnych wymagań, historyjek użytkownika, przypadków testowych) oraz początkowy poziom jakości przedmiotu testów (np. zaliczenie wszystkich testów dymnych).

Typowe kryteria wyjścia obejmują: miary staranności (np. osiągnięty poziom pokrycia, liczba nieusuniętych defektów, gęstość defektów, liczba niezaliczonych przypadków testowych) oraz kryteria binarne „tak/nie” (np. wykonanie wszystkich zaplanowanych testów, przeprowadzenie testowania statycznego, zgłoszenie wszystkich znalezionych defektów, zautomatyzowanie wszystkich testów regresji).

Wyczerpanie czasu lub przekroczenie budżetu można również uznać za poprawne kryteria wyjścia. Zakończenie testowania w takich okolicznościach, nawet jeśli inne kryteria wyjścia nie
zostały spełnione, może być dopuszczalne, jeśli interesariusze przeanalizowali i zaakceptowali ryzyko związane z zakończeniem danego etapu bez dalszych testów.

W zwinnym wytwarzaniu oprogramowania kryteria wyjścia są często nazywane definicją ukończenia (ang. Definition of Done, DoD) i określają obiektywne metryki dla elementu, który
można uznać za zakończony lub przekazać do eksploatacji. Kryteria wejścia, które historyjka użytkownika musi spełnić, aby rozpocząć działania związane z jej implementacją lub testowaniem, nazywane są definicją gotowości (ang. Definition of Ready, DoR).

### 5.1.4. Techniki szacowania

Szacowanie pracochłonności testów (ang. test effort) polega na przewidywaniu ilości pracy związanej z testowaniem, niezbędnej do osiągnięcia celów projektu testowego. Ważne jest, aby wyjaśnić interesariuszom, że szacunki opierają się na szeregu założeń i zawsze są obarczone błędem szacowania. Oszacowania dotyczące małych zadań są zazwyczaj dokładniejsze niż
w przypadku dużych zadań. Dlatego też, szacując duże zadanie, można je najpierw rozbić na zestaw mniejszych zadań, które można oszacować indywidualnie z mniejszym błędem.

W niniejszym sylabusie opisano cztery następujące techniki szacowania.

**Szacowanie na podstawie proporcji**. W tej technice opartej na metrykach gromadzone są dane z poprzednich projektów realizowanych w organizacji, co pozwala uzyskać „standardowe” stosunki współczynników dla podobnych projektów. Stosunki współczynników własnych projektów organizacji (np. zaczerpnięte z danych historycznych) są zazwyczaj najlepszym źródłem
informacji wykorzystywanym w procesie szacowania. Te standardowe stosunki współczynników można następnie wykorzystać do oszacowania wysiłku testowego nowego projektu. Na przykład,
jeśli w poprzednim projekcie stosunek pracochłonności wytwarzania do testowania wynosił 3:2, a w bieżącym projekcie wysiłek związany z wytwarzaniem ma wynieść 600 osobodni pracochłonność testowania można oszacować na 400 osobodni.

**Ekstrapolacja**. W tej technice opartej na metrykach pomiary są wykonywane jak najwcześniej w bieżącym projekcie w celu zebrania niezbędnych danych. Dysponując wystarczającą liczbą obserwacji, pracochłonność wymaganą do wykonania pozostałych zadań można oszacować poprzez ekstrapolację tych danych, zwykle poprzez zastosowanie modelu matematycznego.
Metoda ta dobrze się sprawdza w iteracyjnych modelach wytwarzania oprogramowania. Na przykład zespół może ekstrapolować pracochłonność testowania w nadchodzącej iteracji jako
średnią pracochłonność z ostatnich trzech iteracji.

**Szerokopasmowa technika delficka** (ang. Wideband Delphi). W tej iteracyjnej technice opartej na wiedzy ekspertów, eksperci dokonują szacunków opartych na doświadczeniu. Każdy ekspert szacuje pracochłonność niezależnie od innych. Wyniki są gromadzone i prezentowane, a jeśli szacunki odbiegają od uzgodnionych granic, eksperci omawiają swoje aktualne szacunki. Następnie każdy ekspert jest proszony o indywidualne dokonanie nowego oszacowania na podstawie tych informacji zwrotnych. Proces ten jest powtarzany do momentu osiągnięcia konsensusu. Odmianą tej techniki jest poker planistyczny (ang. Planning Poker), powszechnie stosowany w zwinnym wytwarzaniu oprogramowania. W odmianie tej szacunki są zazwyczaj dokonywane przy użyciu kart z liczbami reprezentującymi wielkość pracochłonności.

**Szacowanie trójpunktowe**. W tej technice opartej na wiedzy ekspertów eksperci dokonują trzech oszacowań: najbardziej optymistycznego (a), najbardziej prawdopodobnego (m) i najbardziej pesymistycznego (b). Ostateczna ocena (E) jest ich ważoną średnią arytmetyczną. W najpopularniejszej wersji tej techniki ocena jest obliczana jako E = (a + 4\*m + b) / 6. Zaletą tej techniki jest to, że pozwala ekspertom obliczyć błąd pomiaru: SD = (b – a) / 6. Na przykład, jeśli szacunki (w osobogodzinach) wynoszą: 𝑎 = 6, 𝑚 = 9 i 𝑏 = 18, to ostateczny szacunek wynosi 10±2 osobogodzin (tj. od 8 do 12 osobogodzin), ponieważ E = (6 + 4\*9 + 18) / 6 = 10, a SD = (18 – 6) / 6 = 2.

Więcej informacji na temat tych i wielu innych technik szacowania wysiłku testowego można znaleźć w (Kan 2003, Koomen 2006, Westfall 2009).

### 5.1.5. Priorytetyzacja przypadków testowych

Po wyspecyfikowaniu przypadków testowych i procedur testowych oraz zorganizowaniu ich w zestawy testowe, zestawy te można uporządkować w harmonogramie wykonywania testów,
który określa kolejność uruchamiania testów. Przy priorytetyzacji przypadków testowych można wziąć pod uwagę różne czynniki.

Najczęściej stosowane strategie ustalania priorytetów przypadków testowych są następujące:

* **Priorytetyzacja oparta na ryzyku**, w której kolejność wykonywania testów wyznaczana jest na podstawie wyników analizy ryzyka (patrz sekcja 5.2.3). Najpierw wykonywane są
przypadki testowe pokrywające najważniejsze ryzyka.
* **Priorytetyzacja oparta na pokryciu**, w której kolejność wykonywania testów wynika z pokrycia (np. pokrycia instrukcji). Najpierw wykonywane są przypadki testowe
osiągające najwyższe pokrycie. W wariancie zwanym priorytetyzacją opartą na dodatkowym pokryciu najpierw wykonywany jest przypadek testowy osiągający najwyższe pokrycie, a każdy kolejny to taki, który osiąga najwyższe dodatkowe pokrycie (tzn. pokrycie obszarów dotąd niepokrytych przez wcześniej wykonane testy).
* **Priorytetyzacja oparta na wymaganiach**, gdzie kolejność wykonywania testów wyznaczana jest na podstawie priorytetów wymagań powiązanych z tymi przypadkami testowymi.Priorytety wymagań są definiowane przez interesariuszy. Najpierw wykonywane są przypadki testowe związane z wymaganiami uznanymi za najważniejsze.

W idealnej sytuacji przypadki testowe są wykonywane w kolejności wyznaczonej przez priorytety, na przykład przy użyciu jednej z wyżej wymienionych strategii priorytetyzacji. Jednak praktyka ta może nie sprawdzić się, jeśli pomiędzy przypadkami testowymi lub testowanymi przez nie funkcjami występują zależności. Jeśli przypadek testowy o wyższym priorytecie jest zależny od przypadku testowego o niższym priorytecie, przypadek testowy o niższym priorytecie musi zostać wykonany jako pierwszy.

Kolejność wykonywania testów powinna również uwzględniać dostępność zasobów. Na przykład, wymagane narzędzia testowe, środowiska testowe lub osoby mogą być dostępne tylko w określonym przedziale czasowym.

### 5.1.6. Piramida testów

Piramida testów to model pokazujący, że różne testy mogą mieć różną szczegółowość. Model ten wspiera zespół w automatyzacji testów i określaniu ich pracochłonności pokazując, że różne cele testów są wspierane przez różne poziomy automatyzacji testów. Warstwy piramidy testów reprezentują grupy testów. Im wyższa warstwa, tym mniejsza szczegółowość testu, niższa izolacja testu (tj. stopień zależności od innych elementów systemu) i dłuższy czas wykonania testu. Testy w dolnej warstwie są małe, odizolowane, szybkie i sprawdzają niewielką część funkcjonalności, więc zazwyczaj potrzeba ich wiele, aby osiągnąć rozsądny poziom pokrycia. Górna warstwa reprezentuje złożone, wysokopoziomowe, kompleksowe testy. Ich wykonywanie jest zazwyczaj wolniejsze niż wykonywanie testów z niższych warstw i zazwyczaj sprawdzają one dużą część funkcjonalności, więc zazwyczaj potrzeba niewielu takich testów, aby osiągnąć rozsądny poziom pokrycia. Liczba i nazwy warstw mogą się różnić. Na przykład, oryginalny model piramidy testów (Cohn 2009) definiuje trzy warstwy: „testy modułowe”, „testy usług” i „testy interfejsu użytkownika”. Inny popularny model definiuje testy jednostkowe (modułowe), testy integracyjne (testy integracji modułów) i testy kompleksowe (ang. end-to-end). Można również stosować inne poziomy testów (patrz sekcja 2.2.1).

### 5.1.7. Kwadranty testowe

Kwadranty testowe (Marick 2003, Crispin 2008) grupują poziomy testów z typami testów, czynnościami, technikami testowania i produktami pracy w kontekście zwinnego wytwarzania oprogramowania. Model ten wspiera zarządzanie testami poprzez ich wizualizację, aby zapewnić uwzględnienie wszystkich odpowiednich typów testów i poziomów testów w cyklu wytwarzania oprogramowania oraz uświadomienie testerom, że niektóre typy testów są bardziej istotne na niektórych poziomach testów niż inne. Model ten zapewnia również sposób rozróżnienia i opisania poszczególnych rodzajów testów wszystkim interesariuszom, w tym programistom, testerom i przedstawicielom jednostek biznesowych.

W tym modelu testy mogą być zorientowane na biznes lub na technologię. Testy mogą również wspierać zespół (np. poprzez ukierunkowanie wytwarzania oprogramowania) lub krytykować
produkt (np. poprzez pomiar zachowania przedmiotu testów w stosunku do oczekiwań). Wypadkowa tych dwóch punktów widzenia określa cztery kwadranty:

* **Kwadrant Q1 (zorientowany na technologię, wspierający zespół)** obejmuje testy modułowe i testy integracji modułów. Testy te powinny być zautomatyzowane i objęte
procesem ciągłej integracji.
* **Kwadrant Q2 (zorientowany na biznes, wspierający zespół)** obejmuje testy funkcjonalne, przykłady, testy oparte na historyjkach użytkownika, prototypy doświadczeń użytkowników, testy API i symulacje. Testy te sprawdzają spełnienie kryteriów akceptacji i mogą być wykonywane manualnie lub automatycznie.
* **Kwadrant Q3 (zorientowany na biznes, krytykujący produkt)** obejmuje testy eksploracyjne, testy użyteczności i testy akceptacyjne użytkownika. Testy te są zorientowane na użytkownika i często wykonywane manualnie.
* **Kwadrant Q4 (zorientowany na technologię, krytykujący produkt)** obejmuje testy dymne i testy niefunkcjonalne (z wyjątkiem testów użyteczności). Testy te są często zautomatyzowane.

## 5.2. Zarządzanie ryzykiem

Organizacje borykają się z wieloma czynnikami wewnętrznymi i zewnętrznymi, które powodują niepewność co do tego, czy i kiedy osiągną swoje cele (ISO 31 000). Zarządzanie ryzykiem pozwala organizacjom zwiększyć prawdopodobieństwo osiągnięcia celów, poprawić jakość swoich produktów oraz zwiększyć zaufanie interesariuszy.

Główne czynności w zakresie zarządzania ryzykiem to:

* **analiza ryzyka** (obejmuje identyfikację ryzyka i ocenę ryzyka; zob. sekcja 5.2.3),
* **kontrola ryzyka** (obejmuje łagodzenie ryzyka i monitorowanie ryzyka; zob. sekcja 5.2.4).

Podejście do testów, w którym działania testowe są wybierane, priorytetyzowane i zarządzane w oparciu o analizę ryzyka i kontrolę ryzyka, nazywane jest testowaniem opartym na ryzyku.

### 5.2.1. Definicja i atrybuty ryzyka

Ryzyko to potencjalne zdarzenie, zagrożenie, niebezpieczeństwo lub sytuacja, której wystąpienie powoduje niekorzystny skutek. Ryzyko można scharakteryzować za pomocą dwóch czynników:

* prawdopodobieństwo ryzyka, czyli prawdopodobieństwo wystąpienia ryzyka (większe od zera i mniejsze niż jeden),
* wpływ ryzyka (szkoda), czyli konsekwencje jego wystąpienia.

Te dwa czynniki określają poziom ryzyka, który jest miarą ryzyka. Im wyższy poziom ryzyka, tym ważniejsze jest uwzględnienie w testach działań łagodzących to ryzyko.

### 5.2.2. Ryzyka projektowe i produktowe

W testowaniu zazwyczaj rozróżnia się dwa rodzaje ryzyka: projektowe i produktowe.

**Ryzyka projektowe** dotyczą zarządzania i nadzoru nad projektem. Ryzyka te obejmują:

* problemy organizacyjne (np. opóźnienia w dostawach produktów pracy, niedokładne szacunki, cięcia kosztów),
* problemy kadrowe (np. niewystarczające umiejętności, konflikty, problemy komunikacyjne, niedobór personelu),
* problemy techniczne (np. rozszerzenie zakresu projektu, słabe wsparcie narzędziowe),
* problemy związane z dostawcami (np. niedostarczenie niezbędnego elementu przez stronę trzecią, upadłość firmy wspierającej).

Wystąpienie ryzyk projektowych może mieć wpływ na harmonogram, budżet lub zakres projektu, a tym samym na zdolność projektu do osiągnięcia jego celów.

**Ryzyka produktowe** dotyczą charakterystyk jakościowych produktu (np. opisanych w modelu jakości ISO 25010). Przykłady ryzyk produktowych obejmują: 

* brakującą lub nieprawidłową funkcjonalność,
* błędne obliczenia,
* błędy wykonania,
* niedopracowaną architekturę,
* nieefektywne algorytmy,
* zbyt długi czas reakcji,
* niski poziom doświadczenia użytkownika (ang. user experience, UX),
* luki w zabezpieczeniach.

Wystąpienie ryzyk produktowych może skutkować różnymi negatywnymi konsekwencjami, w tym:

* niezadowoleniem użytkowników,
* utratą przychodów, zaufania, reputacji,
* szkodami wyrządzonymi stronom trzecim,
* wysokimi kosztami utrzymania, przeciążeniem działu pomocy technicznej,
* odpowiedzialnością karną,
* w skrajnych przypadkach – szkodami materialnymi, utratą zdrowia, a nawet życia.

### 5.2.3. Analiza ryzyka produktowego

Z punktu widzenia testowania celem analizy ryzyka produktowego jest uzyskanie wiedzy na temat tego ryzyka, aby koncentrować wysiłki testowe w sposób minimalizujący poziom ryzyka
rezydualnego (pozostającego wciąż w produkcie). Analiza ryzyka produktowego powinna rozpocząć się na wczesnym etapie cyklu wytwarzania oprogramowania.

Analiza ryzyka produktowego obejmuje identyfikację ryzyka (ang. risk identification) i ocenę ryzyka (ang. risk assessment). 

Identyfikacja ryzyka polega na stworzeniu kompleksowej listy ryzyk. Interesariusze mogą identyfikować te ryzyka przy użyciu różnych technik, np. burzy mózgów, warsztatów, wywiadów lub diagramów przyczynowo-skutkowych. 

Ocena ryzyka obejmuje: klasyfikację zidentyfikowanych ryzyk, określenie prawdopodobieństwa ich wystąpienia, wpływu i poziomu ryzyka, ustalenie priorytetów oraz zaproponowanie sposobów łagodzenia tych ryzyk. Klasyfikacja pomaga w przypisaniu działań łagodzących ryzyko, ponieważ zazwyczaj ryzyka należące do tej samej kategorii można ograniczyć przy użyciu podobnego podejścia.

Ocena ryzyka może opierać się na podejściu ilościowym, jakościowym lub mieszanym. W podejściu ilościowym poziom ryzyka oblicza się jako iloczyn prawdopodobieństwa wystąpienia
ryzyka i jego wpływu wyrażonych liczbowo. W podejściu jakościowym poziom ryzyka określa się za pomocą macierzy ryzyka.

Analiza ryzyka produktowego może mieć wpływ na staranność i zakres testowania. Jej wyniki są wykorzystywane do:

* określenia zakresu wykonywanych testów,
* określenia poziomów testów i typów testów, które należy wykonać,
* określenia technik testowania i zakładanego poziomu pokrycia,
* oszacowania pracochłonności testowania w odniesieniu do każdego zadania,
* ustalenia priorytetów testowania, aby jak najwcześniej wykryć krytyczne defekty,
* określenia, czy w celu zmniejszenia ryzyka można zastosować inne niż testowanie czynności łagodzące.

### 5.2.4. Kontrola ryzyka produktowego

Kontrola ryzyka produktowego obejmuje wszystkie środki podejmowane w odpowiedzi na zidentyfikowane i ocenione ryzyka produktowe. Kontrola ryzyka produktowego obejmuje
łagodzenie ryzyka i monitorowania ryzyka. Łagodzenie ryzyka polega na wdrażaniu działań zaproponowanych podczas oceny ryzyka w celu zmniejszenia poziomu ryzyka. Celem
monitorowania ryzyka jest zapewnienie skuteczności działań łagodzących ryzyko, uzyskanie dalszych informacji pozwalających usprawnić ocenę ryzyka oraz identyfikację nowych ryzyk.

Po przeanalizowaniu danego ryzyka, w ramach procesu kontroli ryzyka produktowego, może być zaproponowane podjęcie różnych działań łagodzących, np. ograniczenie ryzyka poprzez
testowanie, akceptacja ryzyka, przeniesienie ryzyka lub plany awaryjne (Veenendaal 2012). Działania, które można podjąć w celu ograniczenia ryzyk produktowych poprzez testowanie to:

* wybór testerów posiadających poziom doświadczenia i umiejętności odpowiedni do danego rodzaju ryzyka,
* zastosowanie odpowiedniego poziomu niezależności testowania,
* przeprowadzenie przeglądów i analizy statycznej,
* zastosowanie odpowiednich technik testowania i poziomów pokrycia,
* zastosowanie odpowiednich typów testów uwzględniających charakterystyki jakościowe, na które ryzyko ma wpływ,
* wykonanie testowania dynamicznego, w tym testowania regresji.

## 5.3. Monitorowanie testów, nadzór nad testami i ukończenie testów

**Monitorowanie testów** polega na gromadzeniu informacji dotyczących testowania. Informacje te służą do oceny postępu testów oraz do pomiaru spełnienia kryteriów wyjścia lub wykonania zadań testowych związanych z kryteriami wyjścia (np. osiągnięcie zakładanego pokrycia ryzyk produktowych, wymagań lub kryteriów akceptacji).

**Nadzór nad testami** wykorzystuje informacje uzyskane podczas monitorowania testów w celu określenia, w formie tzw. dyrektyw nadzoru, niezbędnych działań korygujących, aby osiągnąć maksymalną efektywność i wydajność testowania. Przykłady dyrektyw nadzoru obejmują:

* zmianę priorytetów testów, gdy zidentyfikowane ryzyko faktycznie wystąpi,
* ponowną ocenę, czy element testowy spełnia kryteria wejścia lub wyjścia w związku z wprowadzeniem do niego poprawek,
* modyfikację harmonogramu testów w celu uwzględnienia opóźnienia w dostarczeniu środowiska testowego,
* dodanie nowych zasobów w razie potrzeby.

**Ukończenie testów** polega na zebraniu danych z zakończonych czynności testowych w celu zebrania doświadczeń, testaliów i innych istotnych informacji. Czynności związane
z ukończeniem testów mają miejsce w kluczowych momentach projektu, takich jak ukończenie poziomu testów, zakończenie iteracji w projekcie zwinnym, zakończenie (lub anulowanie) projektu testowego, wydanie oprogramowania lub zakończenie prac nad wydaniem pielęgnacyjnym (ang. maintenance release).

### 5.3.1. Metryki stosowane w testowaniu

Metryki testowe są gromadzone w celu pomiaru postępów w stosunku do planowanego harmonogramu i budżetu, aktualnej jakości przedmiotu testów oraz skuteczności czynności
testowych w odniesieniu do celów testów lub celu iteracji. W ramach monitorowania testów gromadzi się różne metryki w celu wsparcia nadzoru nad testami i ukończenia testów.

Metryki testowe mierzą w szczególności:

* postęp projektu (np. realizacja zadań, wykorzystanie zasobów, pracochłonność),
* postęp testów (np. postęp implementacji przypadków testowych, postęp przygotowania środowiska testowego, liczba wykonanych/niewykonanych przypadków testowych, liczba, zaliczonych/niezaliczonych przypadków testowych, czas wykonywania testów),
* jakość produktu (np. dostępność, czas odpowiedzi, średni czas do awarii),
* defekty (np. liczba i priorytety wykrytych/usuniętych defektów, gęstość defektów, odsetek wykrytych defektów),
* ryzyko (np. poziom ryzyka rezydualnego),
* pokrycie (np. pokrycie wymagań, pokrycie kodu),
* koszty (np. koszt testowania, koszt jakości ponoszony przez organizację).

### 5.3.2. Cel, treść i odbiorcy raportów z testów
Raporty z testów służą do podsumowania i przekazania informacji dotyczących testów w trakcie ich trwania i po ich zakończeniu. Raporty o postępie testów wspierają w sposób ciągły nadzór nad testami, więc muszą zawierać informacje niezbędne do umożliwienia wprowadzenia zmian w harmonogramie testów, zasobach lub planie testów, gdy takie zmiany są konieczne ze względu na odstępstwa od planu lub zmianę okoliczności. Sumaryczne raporty z testów zawierają podsumowanie konkretnej czynności testowej (np. poziomu testów, cyklu testowego, iteracji) i mogą dostarczyć informacji przydatnych do testów w kolejnych etapach.

Podczas monitorowania testów i nadzoru nad testami zespół testowy generuje raporty o postępie testów, aby zapewnić interesariuszom bieżące informacje o postępie. Raporty o postępie testów są zazwyczaj generowane regularnie (np. codziennie, co tydzień itp.) i zawierają między innymi informacje na temat:

* okresu testowania,
* postępu testów (np. wyprzedzenie lub opóźnienie w stosunku do harmonogramu), w tym wszelkich istotnych odchyleń,
* przeszkód w testowaniu i sposobów ich obejścia,
* metryk testowych (przykłady metryk podano w sekcji 5.3.1),
* nowych i zmienionych ryzyk w okresie testowania,
* testów zaplanowanych na następny okres.

Sumaryczny raport z testów jest przygotowywany na etapie ukończenia testów, gdy projekt, poziom testów lub typ testów został zakończony i, w idealnym przypadku, spełnione zostały
kryteria wyjścia. Raport ten wykorzystuje dane z raportów o postępie testów, a także inne dane. Typowy sumaryczny raport z testów zawiera między innymi informacje dotyczące:

* podsumowania testów,
* oceny testowania i jakości produktu w oparciu o pierwotny plan testów (tj. cele testów i kryteria wyjścia),
* odchyleń od planu testów (np. różnice w stosunku do planowanego harmonogramu testów, czasu trwania i pracochłonności),
* przeszkód w testowaniu i sposobach ich obejścia,
* metryk testowych określonych na podstawie raportów o postępie testów,
* niezłagodzonych ryzyk i nieusuniętych usterek,
* wniosków istotnych dla testowania.

Różne grupy odbiorców wymagają różnych informacji w raportach, co wpływa też na stopień sformalizowania oraz częstotliwość raportowania testów. Raportowanie postępu testów
w obrębie zespołu jest zwykle częste i nieformalne. Raportowanie ukończenia testów odbywa się zazwyczaj według ustalonego szablonu i ma miejsce tylko raz.

Norma ISO/IEC/IEEE 29119-3 zawiera wzory i przykłady raportu o postępie testów (zwanego w tej normie raportem o statusie testów) oraz sumarycznego raportu z testów.

### 5.3.3. Przekazywanie informacji o statusie testowania

Optymalny sposób komunikowania statusu testowania różni się w zależności od kwestii związanych z zarządzaniem testami, strategii testów, obowiązujących norm prawnych,
a w przypadku samoorganizujących się zespołów (patrz sekcja 1.5.2), od samego zespołu. Dostępne opcje obejmują:

* komunikację werbalną z członkami zespołu i innymi interesariuszami,
* tablice wskaźników (ang. dashboards), np. kokpity menedżerskie, tablice zadań i wykresy spalania (ang. burn-down charts),
* kanały komunikacji elektronicznej (np. e-mail, czat),
* dokumentacja online,
* formalne raporty z testów (patrz sekcja 5.3.2).

Zależnie od sytuacji można skorzystać z jednej lub kilku z powyższych opcji. Bardziej formalna komunikacja może być bardziej odpowiednia dla zespołów rozproszonych, w których
bezpośrednia komunikacja twarzą w twarz nie zawsze jest możliwa ze względu na odległość geograficzną lub różnice czasowe. Zazwyczaj różni interesariusze są zainteresowani różnymi
rodzajami informacji, dlatego komunikacja powinna być zawsze odpowiednio dostosowana.

## 5.4. Zarządzanie konfiguracją

W kontekście testowania zarządzanie konfiguracją to proces zapewniający identyfikację, kontrolę i śledzenie produktów pracy, takich jak plany testów, strategie testów, warunki testowe, przypadki testowe, skrypty testowe, wyniki testów, dzienniki testów i raporty z testów. W ramach zarządzania konfiguracji te produkty pracy nazywane są elementami konfiguracji.

W przypadku złożonego elementu konfiguracji (np. środowiska testowego) zarządzanie konfiguracją rejestruje jego elementy składowe, ich relacje i wersje. Jeśli element konfiguracji
zostanie zatwierdzony do testowania, staje się konfiguracją bazową (ang. baseline) i może być zmieniony tylko w ramach formalnego procesu zarządzania zmianą.

Zarządzanie konfiguracją przechowuje zapis zmienionych elementów konfiguracji po utworzeniu nowej konfiguracji bazowej. Dzięki temu możliwy jest powrót do poprzedniej konfiguracji bazowej w celu odtworzenia poprzednich wyników testów.

Zarządzanie konfiguracją wspiera sprawny przebieg testowania poprzez zapewnienie, że:

* wszystkie elementy konfiguracji, w tym elementy testowe (i poszczególne elementy przedmiotu testów), są jednoznacznie identyfikowane, objęte kontrolą wersji i śledzeniem
zmian oraz powiązane z innymi elementami konfiguracji, tak aby można było zachować możliwość śledzenia w całym procesie testowania,
* wszystkie zidentyfikowane dokumenty i elementy oprogramowania są przywoływane w jednoznaczny sposób w testaliach.

Ciągła integracja, ciągłe dostarczanie, ciągłe wdrażanie i związane z nimi procesy testowania są zazwyczaj wdrażane w ramach zautomatyzowanego potoku dostarczania DevOps (patrz sekcja 2.1.4), w którym zazwyczaj uwzględnia się zautomatyzowane zarządzanie konfiguracją.

## 5.5. Zarządzanie defektami

Ponieważ jednym z głównych celów testowania jest wykrywanie defektów, niezbędne jest ustanowienie procesu zarządzania defektami. Chociaż mówimy tutaj o „defektach”, zgłaszane
anomalie mogą okazać się rzeczywistymi defektami lub czymś innym (np. wynikiem fałszywie pozytywnym lub żądaniem zmiany). Kwestia ta jest rozstrzygana podczas procesu rozpatrywania
raportów o defektach. Anomalie mogą być zgłaszane na każdym etapie cyklu wytwarzania oprogramowania, a sposób zgłoszenia zależy od tego cyklu. Proces zarządzania defektami
obejmuje co najmniej przepływ pracy związany z obsługą poszczególnych defektów lub anomalii od momentu ich wykrycia do zamknięcia zgłoszenia oraz reguły klasyfikacji anomalii. Przepływ pracy zazwyczaj obejmuje czynności związane z rejestrowaniem zgłoszonych anomalii, analizowaniem i klasyfikowaniem ich, podejmowaniem decyzji dotyczących odpowiedniej reakcji (takiej jak np. usunięcie lub pozostawienie stanu obecnego), a na koniec zamknięciem zgłoszenia defektu. Proces ten musi być przestrzegany przez wszystkich interesariuszy. Zaleca się podobne postępowanie w przypadku defektów wykrytych podczas testowania statycznego (zwłaszcza analizy statycznej).

Typowy raport o defekcie ma na celu:

* dostarczenie osobom odpowiedzialnym za obsługę i rozwiązywanie zgłoszonych defektów wystarczających informacji do rozwiązania problemu,
* zapewnienie środków umożliwiających śledzenie jakości produktu pracy,
* dostarczenie pomysłów na ulepszenie procesu wytwarzania i testowania.

Raport o defekcie zarejestrowany podczas testowania dynamicznego zazwyczaj zawiera:

* unikalny identyfikator,
* tytuł i krótkie podsumowanie zgłaszanej anomalii,
* datę zaobserwowania anomalii, organizację zgłaszającą i autora, w tym jego rolę,
* identyfikację przedmiotu testów i środowiska testowego,
* kontekst wystąpienia defektu (np. uruchomiony przypadek testowy, wykonywana czynność testowa, faza cyklu wytwarzania oprogramowania oraz inne istotne informacje, takie jak technika testowania, wykorzystana lista kontrolna lub użyte dane testowe),
* opis awarii umożliwiający jej odtworzenie i usunięcie defektu, w tym kroki testowe, które doprowadziły do wystąpienia anomalii, wszelkie istotne dzienniki testów, zrzuty baz danych, zrzuty ekranu lub nagrania,
* oczekiwane wyniki i rzeczywiste wyniki,
* krytyczność defektu, tzn. stopień wpływu na interesariuszy lub wymagania,
* priorytet naprawy (pilność),
* status defektu (np.: otwarty, odroczony, duplikat, oczekujący na poprawkę, oczekujący na testowanie potwierdzające, ponownie otwarty, zamknięty, odrzucony),
* istotne odwołania do innych elementów (np. do przypadku testowego).

Niektóre z powyższych informacji mogą być automatycznie uwzględnione podczas korzystania z narzędzi do zarządzania defektami (np. identyfikator, data, autor, początkowy status). Szablon raportu o defekcie oraz przykładowe raporty o defektach można znaleźć w normie ISO/IEC/IEEE 29119-3, w której raport o defekcie nazywany jest raportem o incydencie.