# 2. Testowanie w cyklu wytwarzania oprogramowania – 130 minut

## Słowa kluczowe

poziom testów, przedmiot testów, przesunięcie w lewo, testowanie akceptacyjne, testowanie białoskrzynkowe, testowanie czarnoskrzynkowe, testowanie funkcjonalne, testowanie integracji modułów, testowanie integracji systemów, testowanie integracyjne, testowanie modułowe, testowanie niefunkcjonalne, testowanie pielęgnacyjne, testowanie potwierdzające, testowanie regresji, testowanie systemowe, typ testów

## Cele nauczania dla rozdziału 2

2.1 Testowanie w kontekście cyklu wytwarzania oprogramowania
   FL-2.1.1 (K2) Wyjaśnić wpływ wybranego modelu cyklu wytwarzania oprogramowania na testowanie.
   FL-2.1.2 (K1) Pamiętać dobre praktyki testowania mające zastosowanie do wszystkich modeli cyklu wytwarzania oprogramowania.
   FL-2.1.3 (K1) Podać przykłady podejść typu „najpierw test” w kontekście wytwarzania oprogramowania.
   FL-2.1.4 (K2) Podsumować, w jaki sposób metodyka DevOps może wpłynąć na testowanie.
   FL-2.1.5 (K2) Wyjaśnić, na czym polega przesunięcie w lewo.
   FL-2.1.6 (K2) Wyjaśnić, w jaki sposób retrospektywy mogą posłużyć jako mechanizmy doskonalenia procesów.
2.2 Poziomy testów i typy testów
   FL-2.2.1 (K2) Rozróżniać poszczególne poziomy testów.
   FL-2.2.2 (K2) Rozróżniać poszczególne typy testów.
   FL-2.2.3 (K2) Odróżniać testowanie potwierdzające od testowania regresji.
2.3 Testowanie pielęgnacyjne
   FL-2.3.1 (K2) Podsumować testowanie pielęgnacyjne i zdarzenia je wyzwalające.

## 2.1. Testowanie w kontekście modelu cyklu wytwarzania oprogramowania

Model cyklu wytwarzania oprogramowania jest abstrakcyjnym, wysokopoziomowym
przedstawieniem procesu wytwarzania oprogramowania. Model ten określa, w jaki sposób różne fazy rozwoju i rodzaje czynności wykonywanych w ramach procesu wytwarzania oprogramowania odnoszą się do siebie zarówno pod względem logicznym, jak i chronologicznym. Przykłady obejmują: sekwencyjne modele wytwarzania oprogramowania (np. model kaskadowy, model V), iteracyjne modele wytwarzania oprogramowania (np. model spiralny, prototypowanie) oraz przyrostowe modele wytwarzania oprogramowania (np. Unified Process).

Niektóre czynności w ramach procesów wytwarzania oprogramowania można również opisać za pomocą bardziej szczegółowych metod wytwarzania oprogramowania i praktyk zwinnych. Przykłady obejmują: wytwarzanie sterowane testami akceptacyjnymi (ang. acceptance test-driven development, ATDD), wytwarzanie sterowane zachowaniem (ang. behavior-driven development, BDD), projektowanie oparte na domenie (ang. domain-driven design, DDD), programowanie ekstremalne (ang. eXtreme Programming, XP), wytwarzanie oparte na cechach (ang. feature-driven development, FDD), Kanban, Lean IT, Scrum oraz wytwarzanie sterowane testami (ang. test-driven development, TDD).

### 2.1.1. Wpływ cyklu wytwarzania oprogramowania na testowanie

Warunkiem powodzenia procesu testowego jest jego dostosowanie do przyjętego cyklu
wytwarzania oprogramowania. Wybór modelu cyklu wytwarzania oprogramowania ma wpływ na:

* zakres i harmonogram działań testowych (np. poziomy testów i typy testów),
* poziom szczegółowości dokumentacji testowej,
* wybór technik testowania i podejścia do testów,
* zakres automatyzacji testów,
* rolę i obowiązki testera.

W sekwencyjnych modelach wytwarzania oprogramowania, w początkowych fazach procesu, testerzy zazwyczaj uczestniczą w przeglądach wymagań, analizie testów i projektowaniu testów. Wykonywalny kod jest zazwyczaj tworzony w późniejszych fazach, więc zazwyczaj testowanie dynamiczne może być przeprowadzane dopiero na późniejszych etapach cyklu wytwarzania oprogramowania.

W niektórych iteracyjnych modelach wytwarzania oprogramowania i przyrostowych modelach wytwarzania oprogramowania zakłada się, że każda iteracja dostarcza działający prototyp lub przyrost produktu. Oznacza to, że w każdej iteracji można przeprowadzać zarówno testowanie statyczne, jak i testowanie dynamiczne na wszystkich poziomach testów. Częste dostarczanie przyrostów wymaga szybkiej informacji zwrotnej i szeroko zakrojonego testowania regresji.

Zwinne wytwarzanie oprogramowania zakłada, że w trakcie projektu mogą wystąpić zmiany. Dlatego w projektach zwinnych preferowana jest lekka dokumentacja produktu oraz szeroko zakrojona automatyzacja testów, ułatwiająca testowanie regresji. Ponadto większość testów manualnych jest zazwyczaj wykonywana przy użyciu technik testowania opartych na doświadczeniu (patrz podrozdział 4.4), które nie wymagają wcześniejszego podjęcia szeroko zakrojonej analizy i projektowania testów.

### 2.1.2. Model cyklu wytwarzania oprogramowania i dobre praktyki testowania

Poniżej przedstawiono dobre praktyki testowania, niezależnie od wybranego modelu cyklu wytwarzania oprogramowania:
* Każdej czynności związanej z wytwarzaniem oprogramowania odpowiada czynność testowa, dzięki czemu wszystkie czynności wytwórcze podlegają kontroli jakości.
* Różne poziomy testów (patrz sekcja 2.2.1) mają określone i różne cele testowania, co pozwala na szeroki zakres testów przy jednoczesnym uniknięciu redundancji.
* Analiza i projektowanie testów dla danego poziomu testów rozpoczynają się podczas odpowiadającej mu fazy cyklu wytwarzania oprogramowania, co zapewnia zgodność z zasadą wczesnego testowania (patrz podrozdział 1.3).
* Testerzy są zaangażowani w przeglądanie produktów pracy natychmiast po udostępnieniu ich projektów, dzięki czemu wcześniejsze testowanie i wykrywanie defektów wspiera przesunięcie w lewo (ang. shift-left, patrz sekcja 2.1.5).

### 2.1.3. Testowanie jako czynnik określający sposób wytwarzania oprogramowania

Wytwarzanie sterowane testami (TDD), wytwarzanie sterowane testami akceptacyjnymi (ATDD) oraz wytwarzanie sterowane zachowaniem (BDD) to podobne podejścia do wytwarzania
oprogramowania, w których testy są czynnikiem określającym kierunek prac programistycznych. Każde z tych podejść realizuje zasadę wczesnego testowania (patrz podrozdział 1.3) i stosuje zasadę przesunięcia w lewo (patrz sekcja 2.1.5), ponieważ testy są definiowane przed napisaniem kodu. Podejścia te wspierają iteracyjny model wytwarzania oprogramowania i charakteryzują się następującymi cechami:

**Wytwarzanie sterowane testami (TDD):**

* Kodowanie kierowane jest poprzez przypadki testowe zamiast przez rozbudowany projekt oprogramowania (Beck 2003)
* Najpierw pisane są testy, następnie kod, tak, aby zaliczyć testy, a na końcu testy i kod są refaktoryzowane.

**Wytwarzanie sterowane testami akceptacyjnymi (ATDD) (patrz sekcja 4.5.3):**

* Testy wyprowadzane są z kryteriów akceptacji w ramach procesu projektowania systemu (Gärtner 2011).
* Testy są pisane przed wytworzeniem części aplikacji, która ma je pomyślnie przejść.

**Wytwarzanie sterowane zachowaniem (BDD):**

* Pożądane zachowanie aplikacji wyraża się za pomocą przypadków testowych napisanych w prostej formie, językiem naturalnym, który jest łatwy do zrozumienia dla interesariuszy – zazwyczaj przy użyciu formatu Given/When/Then (Chelimsky 2010).
* Przypadki testowe powinny być automatycznie przekształcane w wykonywalne testy.

W przypadku wszystkich powyższych podejść testy mogą pozostać testami automatycznymi, aby zapewnić jakość kodu w przyszłych adaptacjach bądź refaktoryzacjach.

### 2.1.4. Metodyka DevOps a testowanie

DevOps to podejście organizacyjne mające na celu stworzenie synergii poprzez współpracę zespołów: wytwarzającego (w tym testowania) i operacyjnego (zajmującego się wdrażaniem
i utrzymaniem), by osiągnąć wspólne cele. DevOps wymaga zmiany kulturowej w organizacji, aby wypełnić lukę między tymi dwoma zespołami, traktując ich funkcje jako równo istotne. DevOps promuje autonomię zespołów, szybką informację zwrotną, zintegrowane łańcuchy narzędzi oraz praktyki techniczne, takie jak ciągła integracja (ang. Continuous Integration, CI) i ciągłe dostarczanie (ang. Continuous Delivery, CD). Umożliwia to zespołom szybsze tworzenie, testowanie i wydawanie wysokiej jakości kodu poprzez dostarczania DevOps (Kim 2016).

Z punktu widzenia testowania korzyści płynące z DevOps to:

* szybka informacja zwrotna na temat jakości kodu oraz tego, czy zmiany mają negatywny wpływ na istniejący kod,
* CI, która promuje przesunięcie w lewo (patrz sekcja 2.1.5), zachęcając programistów do przesyłania wysokiej jakości kodu wraz z testami modułowymi i analizą statyczną,
* promowanie zautomatyzowanych procesów, takich jak CI/CD, które ułatwiają tworzenie stabilnych środowisk testowych,
* zwiększenie widoczności niefunkcjonalnych charakterystyk jakościowych (np. wydajności, niezawodności),
* zmniejszona potrzeba powtarzalnych testów manualnych dzięki automatyzacji poprzez potok dostarczania (ang. delivery pipeline),
* minimalizacja ryzyka regresji dzięki skali i zakresowi zautomatyzowanych testów regresji.

DevOps nie jest jednak pozbawiony ryzyk i wyzwań, do których można zaliczyć:

* konieczność zdefiniowania i ustanowienia potoku dostarczania DevOps,
* konieczność wprowadzenia i utrzymywania narzędzi CI / CD,
* konieczność przeznaczenia dodatkowych zasobów na automatyzację testów oraz trudności związane z wdrożeniem i utrzymaniem automatyzacji.

Chociaż DevOps zapewnia wysoki udział testów automatycznych, nadal konieczne są testy manualne, zwłaszcza z perspektywy użytkownika.

### 2.1.5. Przesunięcie w lewo

Zasada wczesnego testowania (patrz podrozdział 1.3) jest czasami nazywana „przesunięciem w lewo” (ang. shift left), ponieważ jest to podejście, w którym testowanie odbywa się
na wcześniejszym etapie cyklu wytwarzania oprogramowania. Przesunięcie w lewo sugeruje, że testowanie powinno odbywać się wcześniej (np. nie czekając na implementację kodu lub integrację modułów), ale nie oznacza to, że należy zaniedbywać testowanie na późniejszych etapach cyklu wytwarzania oprogramowania.

Dobre praktyki, które ilustrują, jak osiągnąć „przesunięcie w lewo” w testowaniu, to m.in.:

* przegląd specyfikacji z perspektywy testerów, co pozwala wykryć potencjalne defekty, takie jak niejasności, braki i niespójności,
* pisanie przypadków testowych przed rozpoczęciem pisania kodu i uruchamianie kodu w jarzmie testowym podczas implementacji,
* wykorzystanie CI, a jeszcze lepiej CD, ponieważ zapewnia ono szybką informację zwrotną i automatyczne testy modułowe kodu przesyłanego do repozytorium kodu,
* przeprowadzenie analizy statycznej kodu źródłowego przed rozpoczęciem testowania dynamicznego lub w ramach zautomatyzowanego procesu,
* przeprowadzanie testowania niefunkcjonalnego, zaczynając już od poziomu testów modułowych, jeśli to możliwe (jest to przesunięcie w lewo, ponieważ tego typu testy są
zazwyczaj przeprowadzane w późniejszych fazach cyklu wytwarzania oprogramowania, kiedy dostępny jest kompletny system i reprezentatywne środowisko testowe).

Przesunięcie w lewo może wymagać dodatkowych szkoleń, wysiłku lub kosztów na wcześniejszym etapie procesu, ale oczekuje się, że pozwoli zaoszczędzić wysiłek lub koszty na
etapach późniejszych.

W przypadku przesunięcia w lewo ważne jest, aby interesariusze byli przekonani do tej koncepcji i ją akceptowali.

### 2.1.6. Retrospektywy i doskonalenie procesów

Retrospektywy często odbywają się pod koniec projektu lub iteracji, w momencie osiągnięcia kamienia milowego związanego z wydaniem, ale mogą być też organizowane w razie potrzeby.
Termin i przebieg retrospektyw zależą od przyjętego modelu cyklu wytwarzania oprogramowania. Podczas retrospektyw uczestnicy (nie tylko testerzy, ale także np. programiści, architekci, właściciele produktu, analitycy biznesowi) omawiają:

* Co się udało i powinno zostać zachowane?
* Co się nie udało i można to poprawić?
* Jak wdrożyć udoskonalenia i wykorzystać pomyślnie zrealizowane elementy w przyszłości?

Wyniki retrospektywy powinny być dokumentowane i zazwyczaj stanowią część sumarycznego raportu z testów (patrz sekcja 5.3.2). Retrospektywy mają kluczowe znaczenie dla pomyślnego
wdrożenia ciągłego doskonalenia i ważne jest, aby wszelkie zalecane udoskonalenia były realizowane.

Typowe korzyści płynące z retrospektyw dla testowania obejmują:

* zwiększoną skuteczność i wydajność testów (np. poprzez wdrożenie sugestii dotyczących doskonalenia procesów),
* zwiększoną jakość testaliów (np. poprzez wspólną weryfikację procesów testowych),
* budowanie więzi w zespole i uczenie się (np. dzięki możliwości zgłaszania problemów i proponowania usprawnień),
* poprawę jakości podstawy testów (np. dzięki możliwości identyfikacji i rozwiązania niedociągnięć związanych z jakością i z zakresem wymagań),
* polepszenie współpracy między zespołem wytwórczym a zespołem testowym (np. dzięki regularnemu przeglądowi i optymalizacji zasad współpracy).

## 2.2. Poziomy testów i typy testów

Poziomy testów to grupy czynności testowych, które są organizowane i zarządzane wspólnie. Każdy poziom testów jest instancją procesu testowego, wykonywaną w odniesieniu do oprogramowania na danym etapie wytwarzania, od poszczególnych modułów po kompletne systemy lub systemy systemów.

Poziomy testów są powiązane z innymi czynnościami w ramach cyklu wytwarzania oprogramowania. W sekwencyjnych modelach wytwarzania oprogramowania poziomy testów są często definiowane w taki sposób, że kryteria wyjścia jednego poziomu stanowią część kryteriów wejścia do następnego poziomu. W niektórych iteracyjnych modelach cyklu wytwarzania
oprogramowania może to nie mieć zastosowania. Czynności związane z wytwarzaniem oprogramowania mogą obejmować wiele poziomów testów, a poziomy testów mogą na siebie nachodzić w czasie.

Typy testów to grupy czynności testowych związanych z określonymi charakterystykami jakościowymi, a większość tych czynności można wykonać na każdym poziomie testów.

### 2.2.1. Poziomy testów

W niniejszym sylabusie opisano pięć następujących poziomów testów:

* **Testowanie modułowe** (zwane również testowaniem jednostkowym) koncentruje się na testowaniu modułów w izolacji. Często wymaga to specjalnego wsparcia, takiego jak jarzma testowe lub struktury do testów jednostkowych. Testowanie modułowe jest zazwyczaj wykonywane przez programistów w ich środowiskach programistycznych.
* **Testowanie integracji modułów** (zwane również testowaniem integracji jednostek) koncentruje się na testowaniu interfejsów i interakcji między modułami. Testowanie to jest w dużym stopniu uzależnione od strategii integracji, takiej jak strategia wstępująca (ang. bottom-up), zstępująca (ang. top-down) lub wielkiego wybuchu (ang. big-bang).
* **Testowanie systemowe** koncentruje się na ogólnym zachowaniu i możliwościach systemu lub produktu jako całości, często obejmując testowanie funkcjonalne zadań typu end-to-end oraz testowanie niefunkcjonalne charakterystyk jakościowych. W przypadku niektórych niefunkcjonalnych charakterystyk jakościowych, zaleca się testowanie ich w reprezentatywnym środowisku testowym (np. użyteczność). Możliwe jest również wykorzystanie symulacji podsystemów. Testowanie systemu może być przeprowadzane przez niezależny zespół testowy i jest związane ze specyfikacjami systemu.
* **Testowanie integracji systemów** koncentruje się na testowaniu interfejsów między testowanym systemem a innymi systemami i usługami zewnętrznymi. Testy integracji
systemów wymagają odpowiednich środowisk testowych, najlepiej podobnych do środowiska operacyjnego.
* **Testowanie akceptacyjne** koncentruje się na walidacji i wykazaniu gotowości do wdrożenia, co oznacza, że system spełnia potrzeby biznesowe użytkownika. Idealnie, jeśli testy akceptacyjne są przeprowadzane przez docelowych użytkowników. Główne formy testów akceptacyjnych to: testowanie akceptacyjne użytkownika (ang. User Acceptance Testing, UAT), operacyjne testy akceptacyjne (ang. Operational Acceptance Testing, OAT), testowanie akceptacyjne zgodności z umową, testowanie akceptacyjne zgodności z prawem, testowanie alfa i testowanie beta.

Poziomy testów rozróżnia się na podstawie poniższej, niewyczerpującej listy atrybutów, aby uniknąć nakładania się działań testowych:

* przedmiot testów,
* cele testów,
* podstawa testów,
* defekty i awarie,
* podejście i odpowiedzialności.

### 2.2.2. Typy testów

Istnieje wiele typów testów. W niniejszym sylabusie omówiono cztery z nich. 

**Testowanie funkcjonalne** ocenia funkcje, które powinien wykonywać moduł lub system. Funkcje te opisują, „co” powinien robić przedmiot testów. Głównym celem testowania funkcjonalnego jest sprawdzenie kompletności funkcjonalnej, poprawności funkcjonalnej i adekwatności funkcjonalnej.

**Testowanie niefunkcjonalne** ocenia inne niż funkcjonalność charakterystyki modułu lub systemu. Testowanie niefunkcjonalne sprawdza, „jak dobrze” zachowuje się system. Głównym
celem testów niefunkcjonalnych jest sprawdzenie niefunkcjonalnych charakterystyk jakościowych. Norma ISO/IEC 25010 zawiera następującą klasyfikację niefunkcjonalnych charakterystyk jakościowych:

* wydajność,
* kompatybilność,
* użyteczność (znana również jako zdolność do interakcji),
* niezawodność,
* zabezpieczenia,
* utrzymywalność,
* przenaszalność (znana również jako elastyczność),
* bezpieczeństwo.

Czasami wskazane jest rozpoczęcie testów niefunkcjonalnych na wczesnym etapie cyklu wytwarzania oprogramowania (np. w ramach przeglądów lub testowania modułowego). Podstawą
wielu testów niefunkcjonalnych są testy funkcjonalne – w praktyce wykorzystywane są te same testy funkcjonalne, ale celem jest sprawdzenie, czy podczas wykonywania danej funkcji spełniane są wymagania niefunkcjonalne (np. sprawdzenie, czy funkcja jest wykonywana w określonym czasie lub czy można ją przenieść na nową platformę). Późne wykrycie defektów
niefunkcjonalnych może stanowić poważne zagrożenie dla powodzenia projektu. Testy niefunkcjonalne wymagają czasami bardzo specyficznego środowiska testowego, takiego jak laboratorium użyteczności do testowania użyteczności.

**Testowanie czarnoskrzynkowe** (patrz podrozdział 4.2) jest oparte na specyfikacjach. Testy wyprowadza się na podstawie dokumentacji niezwiązanej z wewnętrzną strukturą przedmiotu
testów. Głównym celem testowania czarnoskrzynkowego jest sprawdzenie zachowania systemu pod kątem zgodności z jego specyfikacją.

**Testowanie białoskrzynkowe** (patrz podrozdział 4.3) opiera się na strukturze przedmiotu testów. Testy wyprowadza się z implementacji systemu lub jego wewnętrznej struktury (np. kodu, architektury, przepływów pracy, przepływów danych). Głównym celem testowania białoskrzynkowego jest uzyskanie akceptowalnego poziomu pokrycia testami tej struktury.

Wszystkie cztery wyżej wymienione typy testów mogą być stosowane na wszystkich poziomach testów, chociaż działania na każdym poziomie będą inaczej ukierunkowane. Do wyprowadzenia
warunków testowych i przypadków testowych dla wszystkich wymienionych typów testów można stosować różne techniki testowania.

### 2.2.3. Testowanie potwierdzające i testowanie regresji

W modułach lub systemach często wprowadza się zmiany w celu ich ulepszenia poprzez dodanie nowej funkcjonalności lub naprawienie poprzez usunięcie defektu. Testowanie powinno wówczas obejmować testowanie potwierdzające i testowanie regresji.

**Testowanie potwierdzające** ma na celu sprawdzenie, czy wykryty uprzednio defekt został pomyślnie usunięty. W zależności od ryzyka można przetestować naprawioną wersję
oprogramowania na kilka sposobów, w tym poprzez:

* wykonanie wszystkich testów, które wcześniej zakończyły się niezaliczeniem z powodu defektu,
* dodanie nowych testów obejmujących wszelkie zmiany, które były konieczne do usunięcia defektu.

Jeśli jednak na usunięcie defektu brakuje czasu lub pieniędzy, testowanie potwierdzające może ograniczać się do wykonania kroków testowych, które powinny odtworzyć awarię spowodowaną defektem, i sprawdzenia, czy awaria już nie występuje.

**Testowanie regresji** ma na celu sprawdzenie, że zmiana (w tym poprawka, która była już przedmiotem testowania potwierdzającego) nie spowodowała żadnych niekorzystnych skutków.
Te niekorzystne skutki mogą mieć wpływ na ten sam moduł, w którym wprowadzono zmianę, inne moduły w tym samym systemie, a nawet inne systemy. Testowanie regresji nie musi zatem
ograniczać się do samego przedmiotu testów, może również odnosić się do środowiska, w którym przedmiot testów się znajduje. Dlatego zaleca się najpierw przeprowadzenie analizy wpływu szacującej zasięg testowania regresji, aby rozpoznać, które części oprogramowania mogą zostać dotknięte zmianami.

Zestawy testów regresji są uruchamiane wiele razy i zazwyczaj liczba związanych z nimi przypadków testowych wzrasta wraz z każdą iteracją lub wydaniem. Dlatego testowanie regresji
jest naturalnym kandydatem do automatyzacji. Automatyzację testów należy rozpocząć na wczesnym etapie projektu. Automatyzacja testów regresji jest również dobrą praktyką w przypadku stosowania CI, np. w DevOps (patrz sekcja 2.1.4). W zależności od sytuacji może ona obejmować testy regresji na różnych poziomach testów.

Testowanie potwierdzające oraz testowanie regresji dla przedmiotu testów jest wykonywane na wszystkich poziomach testów, na których usuwano defekty lub wprowadzano zmiany.

## 2.3. Testowanie pielęgnacyjne

Istnieją różne kategorie pielęgnacji. Może ona mieć charakter korygujący (działania naprawcze), adaptacyjny (dostosowanie do zmian w środowisku) lub doskonalący (np. poprawiający wydajność lub łatwość utrzymania, patrz norma ISO/IEC 14764). Pielęgnacja może zatem obejmować zarówno planowane wydania/wdrożenia, jak i nieplanowane doraźne poprawki (ang.
hot fix). Przed dokonaniem zmiany można przeprowadzić analizę wpływu, aby ustalić, czy zmiana powinna zostać wprowadzona, w oparciu o potencjalne konsekwencje w innych obszarach
systemu. Testowanie zmian w już działającym systemie obejmuje zarówno ocenę powodzenia wdrożenia zmiany, jak i sprawdzenie ewentualnych regresji w częściach systemu, które pozostały niezmienione (co zazwyczaj dotyczy większości systemu).

Zakres testowania pielęgnacyjnego zależy zazwyczaj od:

* poziomu ryzyka związanego ze zmianą,
* wielkości istniejącego systemu,
* wielkości zmiany.

Czynniki wywołujące pielęgnację i testowanie pielęgnacyjne można sklasyfikować w następujący sposób:

* Modyfikacje, takie jak planowane ulepszenia (tj. nowe wersje systemu), zmiany korygujące lub doraźne poprawki.
* Aktualizacje lub migracje środowiska operacyjnego, np. z jednej platformy na drugą, które mogą wymagać testów związanych z nowym środowiskiem, a także ze zmienionym oprogramowaniem lub testów konwersji danych, gdy dane z innej aplikacji są migrowane do pielęgnowanego systemu.
* Wycofanie z eksploatacji, np. gdy aplikacja osiąga koniec swojego cyklu życia. Wycofanie systemu z eksploatacji może wymagać testowania archiwizacji danych, jeśli wymagane są długie okresy przechowywania danych. Testowanie procedur przywracania i odzyskiwania danych po archiwizacji może być również konieczne w przypadku, gdy w okresie archiwizacji wymagany jest dostęp do określonych danych.