# metadata
lo: FL-1.1.1
k-level: K1
points: 1
correct: b

## question
Który z poniższych jest typowym celem testów?

## answers
a) Sprawdzenie, czy udokumentowane wymagania są spełnione.  
b) Powodowanie awarii i identyfikacja defektów.  
c) Wywoływanie błędów i identyfikacja podstawowych przyczyn.  
d) Weryfikacja, czy przedmiot testów spełnia oczekiwania użytkowników.

## justification
a) Odpowiedź niepoprawna. Sprawdzanie zgodności z udokumentowanymi wymaganiami jest niepoprawne, ponieważ walidacja dotyczy spełnienia wymagań i oczekiwań użytkowników, podczas gdy weryfikacja dotyczy spełnienia wyspecyfikowanych wymagań, więc byłoby to poprawne, gdybyśmy zastąpili „walidację" terminem „weryfikacja".  
b) Odpowiedź poprawna. Wywoływanie awarii i identyfikowanie defektów jest prawdopodobnie najczęstszym celem testowania dynamicznego.  
c) Odpowiedź niepoprawna. Wywoływanie błędów i identyfikowanie podstawowych przyczyn jest niepoprawne, ponieważ testerzy nie wywołują błędów, lecz awarie. Błędy są zazwyczaj popełniane przez programistów (i nie można ich tak naprawdę wywołać) i powodują defekty, które testerzy próbują zidentyfikować bezpośrednio poprzez testowanie statyczne lub pośrednio poprzez awarie w testowaniu dynamicznym. Identyfikowanie podstawowych przyczyn jest przydatne, ale stanowi część debugowania, które jest odrębną czynnością od testowania.  
d) Odpowiedź niepoprawna. Sprawdzanie, czy przedmiot testów spełnia oczekiwania użytkownika, jest niepoprawne, ponieważ weryfikacja dotyczy sprawdzania wyspecyfikowanych (udokumentowanych) wymagań, podczas gdy walidacja dotyczy spełnienia wymagań i oczekiwań użytkownika, więc byłoby to poprawne, gdybyśmy zastąpili „weryfikację" terminem „walidacja".

---

# metadata
lo: FL-1.1.2
k-level: K2
points: 1
correct: c

## question
Które z poniższych stwierdzeń najlepiej opisuje różnicę między testowaniem a debugowaniem?

## answers
a) Testowanie powoduje awarie, a debugowanie usuwa awarie.
b) Testowanie jest działaniem negatywnym, a debugowanie jest działaniem pozytywnym.
c) Testowanie stwierdza istnienie defektów, a debugowanie usuwa defekty.
d) Testowanie znajduje przyczynę defektu, a debugowanie usuwa przyczynę defektu.

## justification
a) Odpowiedź niepoprawna. Testowanie dynamiczne wywołuje awarie (na podstawie których można zlokalizować i usunąć defekty). Jednak debugowanie polega na lokalizowaniu defektów i ich usuwaniu. Dlatego debugowanie nie usuwa awarii.
b) Odpowiedź niepoprawna. Zarówno testowanie, jak i debugowanie przyczyniają się do poprawy jakości przedmiotu testów, dlatego też należy je traktować jako działania pozytywne. Debugowanie jest ogólnie uważane za działanie pozytywne, ponieważ polega na naprawianiu (usuwaniu) czegoś. Testowanie dynamiczne polega na celowym wywołaniu awarii w przedmiocie testów, dlatego niektórzy uważają je za działanie negatywne, ale jest to bardzo wąskie spojrzenie (i nie jest ono typowe dla testerów).
c) Odpowiedź poprawna. Testowanie pozwala stwierdzić istnienie defektów albo bezpośrednio poprzez obserwację defektu podczas przeglądów (lub za pomocą narzędzia do analizy statycznej), albo pośrednio poprzez wywołanie awarii podczas testowania dynamicznego. Debugowanie jest działaniem odrębnym od testowania (zwykle wykonywanym przez programistów) i polega na lokalizowaniu defektów (tylko w przypadku testowania dynamicznego) i ich usuwaniu.
d) Odpowiedź niepoprawna. Przyczyną defektów są zazwyczaj błędy ludzkie. Testowanie wykrywa defekty bezpośrednio poprzez testowanie statyczne lub pośrednio poprzez wywołanie awarii w testowaniu dynamicznym, a debugowanie usuwa defekty. Testowanie nie wykrywa więc przyczyn defektów, a debugowanie nie usuwa przyczyn defektów.

---

# metadata
lo: FL-1.3.1
k-level: K2
points: 1
correct: b

## question
„Przekonanie o braku defektów jest błędem" to jedna z zasad testowania.
Która z poniższych opcji stanowi przykład zastosowania tej zasady w praktyce?

## answers
a) Wyjaśnienie, że testowanie nie jest w stanie wykazać braku defektów.
b) Wspieranie użytkowników końcowych w przeprowadzaniu testów akceptacyjnych.
c) Zapewnienie, że w dostarczonym systemie nie pozostały żadne defekty.
d) Modyfikowanie zaliczonych testów, aby zapewnić, że pozostanie jak najmniej defektów.

## justification
a) Odpowiedź niepoprawna. Zasada „testowanie ujawnia defekty, ale nie może dowieść ich braku" wyjaśnia, że chociaż testowanie może wykryć istnienie defektów w przedmiotu testów, nie jest możliwe wykazanie, że nie ma w nim żadnych defektów.
b) Odpowiedź poprawna. Wspierając użytkownika końcowego w przeprowadzaniu testów akceptacyjnych, powinno być możliwe sprawdzenie, czy system spełnia potrzeby i oczekiwania użytkowników.
c) Odpowiedź niepoprawna. Nie można zapewnić, że w dostarczonym systemie nie pozostały żadne defekty implementacyjne.
d) Odpowiedź niepoprawna. Modyfikowanie testów, które nie powodują żadnych awarii w celu zapewnienia, że pozostało niewiele defektów, jest jednym ze sposobów rozwiązania problemu związanego z zasadą „testy ulegają zużyciu".

---

# metadata
lo: FL-1.4.1
k-level: K2
points: 2
correct: b, e

## question
Które dwie z poniższych czynności testowych z największym prawdopodobieństwem będą obejmowały zastosowanie analizy wartości brzegowych i podziału na klasy równoważności?

## answers
a) Implementacja testów.
b) Projektowanie testów.
c) Wykonywanie testów.
d) Monitorowanie testów.
e) Analiza testów.

## justification
a) Odpowiedź niepoprawna. Implementacja testów prawdopodobnie nie będzie wymagać zastosowania technik testowania, ponieważ dotyczy ona głównie zestawiania przypadków testowych w procedury testowe.
b) Odpowiedź poprawna. Projektowanie testów prawdopodobnie wiąże się z wykorzystaniem technik testowania w celu tworzenia przypadków testowych na podstawie warunków testowych i elementów pokrycia.
c) Odpowiedź niepoprawna. Wykonywanie testów prawdopodobnie nie wymaga stosowania technik testowania, ponieważ dotyczy głównie wykonywania procedur testowych.
d) Odpowiedź niepoprawna. Monitorowanie testów prawdopodobnie nie wymaga stosowania technik testowania. Monitorowanie testów dotyczy głównie bieżącej kontroli mającej na celu zapewnienie realizacji planu.
e) Odpowiedź poprawna. Analiza testów prawdopodobnie będzie wymagała zastosowania technik testowania w celu zidentyfikowania warunków testowych.

---

# metadata
lo: FL-1.4.3
k-level: K2
points: 1
correct: a

## question
Rozważ następujące testalia (1--4) oraz czynności testowe (A--D):
1. Elementy pokrycia.
2. Żądania zmian.
3. Harmonogram wykonywania testów.
4. Spriorytetyzowane warunki testowe.

A. Analiza testów.
B. Projektowanie testów.
C. Implementacja testów.
D. Ukończenie testów.

Która z poniższych opcji najlepiej łączy elementy z odpowiadającymi im czynnościami?

## answers
a) 1B, 2D, 3C, 4A.
b) 1B, 2D, 3A, 4C.
c) 1D, 2C, 3A, 4B.
d) 1D, 2C, 3B, 4A.

## justification
a) Odpowiedź poprawna. Prawidłowe dopasowanie to: 1B, 2D, 3C, 4A.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-1.4.5
k-level: K2
points: 1
correct: c

## question
Które z poniższych stwierdzeń dotyczących różnych ról związanych z testowaniem jest **najbardziej** poprawne?

## answers
a) W zwinnym wytwarzaniu oprogramowania rola związana z zarządzaniem testami jest głównym obowiązkiem zespołu, podczas gdy rola związana z testowaniem jest głównie obowiązkiem jednej osoby spoza zespołu.
b) Rola związana z testowaniem odpowiada przede wszystkim za monitorowanie i nadzór nad testami, natomiast rola związana z zarządzaniem testami odpowiada przede wszystkim za planowanie i ukończenie testów.
c) W zwinnym wytwarzaniu oprogramowania czynnościami związanymi z zarządzaniem testami, które obejmują wiele zespołów, zajmuje się kierownik testów spoza zespołu, natomiast niektóre zadania związane z zarządzaniem testami są wykonywane przez sam zespół.
d) Rola związana z zarządzaniem testami obejmuje przede wszystkim analizę i projektowanie testów, natomiast rola związana z testowaniem obejmuje przede wszystkim implementację i wykonywanie testów.

## justification
a) Odpowiedź niepoprawna. Chociaż prawdą jest, że w zwinnym wytwarzaniu oprogramowania niektóre zadania związane z zarządzaniem testami mogą być wykonywane przez sam zespół zwinny, rola związana z testowaniem nie jest przede wszystkim obowiązkiem jednej osoby spoza zespołu. Testowanie jest raczej wykonywane przez różnych członków zespołu zgodnie z podejściem „cały zespół”.
b) Odpowiedź niepoprawna. Rola związana z zarządzaniem testami obejmuje przede wszystkim działania związane z planowaniem testów, monitorowaniem testów i nadzorem nad testami oraz ukończeniem testów. Tak więc, chociaż stwierdzenie to jest częściowo poprawne, błędne jest twierdzenie, że rola związana z testowaniem polega przede wszystkim na monitorowaniu testów i nadzorze nad testami.
c) Odpowiedź poprawna. W zwinnym wytwarzaniu oprogramowania niektóre zadania związane z zarządzaniem testami mogą być realizowane przez sam zespół zwinny. Jednak w przypadku czynności testowych obejmujących wiele zespołów w organizacji zadania te mogą być realizowane przez kierowników testów spoza zespołu programistów.
d) Odpowiedź niepoprawna. Rola związana z zarządzaniem testami obejmuje przede wszystkim działania związane z planowaniem testów, monitorowaniem testów i nadzorem nad testami oraz ukończeniem testów, podczas gdy rola związana z testowaniem odpowiada przede wszystkim za techniczne i inżynieryjne aspekty testowania, takie jak analiza testów, projektowanie testów, implementacja testów i wykonywanie testów. Dlatego też rola związana z zarządzaniem testami nie odpowiada zazwyczaj za analizę testów i projektowanie testów, chociaż słuszne jest stwierdzenie, że rola związana z testowaniem odpowiada przede wszystkim za implementację i wykonywanie testów.

---

# metadata
lo: FL-1.5.2
k-level: K1
points: 1
correct: b

## question
Które z poniższych jest zaletą podejścia „cały zespół”?

## answers
a) Zespoły bez testerów.
b) Poprawa dynamiki zespołu.
c) Wyspecjalizowani członkowie zespołu.
d) Większe zespoły.

## justification
a) Odpowiedź niepoprawna. W podejściu „cały zespół” testerzy odgrywają kluczową rolę, dzieląc się swoją wiedzą specjalistyczną z zespołem i kierując rozwojem produktu. Współpracują z innymi członkami zespołu, aby osiągnąć pożądany poziom jakości, oraz z przedstawicielami jednostek biznesowych, aby stworzyć testy akceptacyjne. Testerzy współpracują również z programistami w celu określenia optymalnej strategii testów i podejścia do automatyzacji.
b) Odpowiedź poprawna. Wykorzystując w najbardziej efektywny sposób różnorodne umiejętności każdego członka zespołu, podejście „cały zespół” sprzyja doskonałej dynamice zespołu, promuje efektywną komunikację i współpracę oraz generuje efekt synergii, który przynosi korzyści całemu projektowi.
c) Odpowiedź niepoprawna. Podejście „cały zespół” pozwala każdemu członkowi zespołu posiadającemu wymagane umiejętności i wiedzę podjąć się wykonania dowolnego zadania, dlatego też obecność specjalistów w zespole nie stanowi zalety tego podejścia.
d) Odpowiedź niepoprawna. Nie ma konkretnych wytycznych dotyczących optymalnej wielkości zespołów stosujących podejście „cały zespół” i nie ma dowodów na to, że większe zespoły są lepsze.

---

# metadata
lo: FL-1.5.3
k-level: K2
points: 1
correct: a

## question
Które z poniższych stwierdzeń dotyczących niezależności testowania jest **poprawne**?

## answers
a) Niezależni testerzy wykryją defekty dzięki odmiennej od programistów perspektywie technicznej, ale ich niezależność może prowadzić do antagonistycznych relacji z programistami.
b) Programiści znają swój kod, więc znajdują w nim niewiele defektów, ale dzięki wspólnemu doświadczeniu w zakresie oprogramowania z testerami, defekty te zostaną również wykryte przez testerów.
c) Niezależne testowanie wymaga testerów spoza zespołu programistów, a najlepiej spoza organizacji, jednak testerom tym trudno jest zrozumieć dziedzinę biznesową aplikacji.
d) Testerzy spoza zespołu programistów są bardziej niezależni niż testerzy z zespołu, ale testerzy z zespołu są bardziej narażeni na obwinianie ich za opóźnienia w wydaniu produktu.

## justification
a) Odpowiedź poprawna. Główną zaletą niezależności testowania jest to, że testerzy mają większe szanse na wykrycie różnych rodzajów defektów niż programiści, ze względu na swoje zróżnicowane doświadczenie, techniczny punkt widzenia i potencjalne uprzedzenia, w tym uprzedzenia poznawcze. Jednak główną wadą niezależności testowania jest to, że testerzy mogą zostać odizolowani od zespołu programistów, co prowadzi do problemów z komunikacją, braku współpracy i potencjalnie wrogich relacji, w których testerzy są obwiniani za opóźnienia i stwarzanie wąskich gardeł w procesie wydawania nowych wersji.
b) Odpowiedź niepoprawna. Znajomość kodu przez programistę nie oznacza, że rzadko znajduje on w nim defekty, ale raczej, że potrafi skutecznie znaleźć wiele defektów we własnym kodzie. Ponadto, zamiast *wspólnego* doświadczenia programistów i testerów, jako powód, dla którego testerzy i programiści znajdują różne rodzaje defektów, podaje się zazwyczaj *odmienne* doświadczenie programistów i testerów.
c) Odpowiedź niepoprawna. Testowanie może być przeprowadzane na różnych poziomach niezależności, od całkowitego braku niezależności do bardzo wysokiej niezależności (np. testerzy spoza organizacji). W większości projektów wykorzystuje się wiele poziomów niezależności, przy czym programiści przeprowadzają testowanie modułowe i integracyjne modułów, zespół testujący przeprowadza testowanie systemowe i integracyjne systemów, a przedstawiciele jednostek biznesowych przeprowadzają testowanie akceptacyjne. Testerzy mogą więc należeć do zespołu programistów i nie muszą pochodzić spoza organizacji. Znajomość dziedziny biznesowej aplikacji będzie się zmieniać od przypadku do przypadku i nie zależy od poziomu niezależności.
d) Odpowiedź niepoprawna. Testowanie może być przeprowadzane na różnych poziomach niezależności, od braku niezależności do bardzo wysokiej niezależności (np. testerzy spoza organizacji), przy czym testerzy spoza zespołu programistów są zazwyczaj bardziej niezależni niż testerzy z zespołu. Istnieje jednak więcej powodów, aby sądzić, że testerzy spoza zespołu są prawdopodobnie bardziej odizolowani od programistów i dlatego są bardziej narażeni na obwinianie ich za opóźnienia w wydaniu produktu.

---

# metadata
lo: FL-2.1.2
k-level: K1
points: 1
correct: d

## question
Która z poniższych praktyk testowania jest dobrą praktyką mającą zastosowanie we wszystkich modelach wytwarzania oprogramowania?

## answers
a) Dla każdego poziomu testów istnieje odpowiadający mu poziom wytwarzania.
b) Dla każdego celu testów istnieje odpowiadający mu cel wytwarzania.
c) Dla każdej czynności testowej istnieje odpowiadająca jej czynność użytkownika.
d) Dla każdej czynności wytwórczej istnieje odpowiadająca jej czynność testowa.

## justification
a) Odpowiedź niepoprawna. Kontrola jakości dotyczy wszystkich czynności związanych z wytwarzaniem, co oznacza, że każdej czynności związanej z wytwarzaniem oprogramowania odpowiada odpowiednia czynność testowa. Jednak w tym przypadku próbujemy zrównać poziomy testów z poziomami wytwarzania i chociaż wiemy, co oznacza termin „poziomy testów”, nie ma powszechnego konsensusu w rozumieniu terminu „poziom wytwarzania”.
b) Odpowiedź niepoprawna. Każda czynność związana z wytwarzaniem oprogramowania ma odpowiadającą jej czynność testową, jednak cele testów są zupełnie inne. Na przykład celem testu może być zapewnienie, że przedmiot testów spełnia wymaganie umowy, zgodnie z którym przed dostawą należy przeprowadzić określony typ testów. W tym przypadku nie ma powodu, aby istniał odpowiadający mu cel wytwarzania.
c) Odpowiedź niepoprawna. Kontrola jakości dotyczy wszystkich czynności związanych z wytwarzaniem, co oznacza, że każdej czynności związanej z wytwarzaniem oprogramowania odpowiada czynność testowa. Jednak ta sama symetria nie dotyczy testowania i działań użytkowników. Na przykład w przypadku niektórych systemów trudno jest nawet zidentyfikować użytkowników końcowych. Ponadto niektóre czynności testowe koncentrują się na programistach (np. testowanie łatwości utrzymywania), co nie ma żadnego związku z działaniami użytkowników.
d) Odpowiedź poprawna. Kontrola jakości dotyczy wszystkich czynności związanych z wytwarzaniem, co oznacza, że każdej czynności związanej z wytwarzaniem oprogramowania odpowiada czynność testowa.

---

# metadata
lo: FL-2.1.3
k-level: K1
points: 1
correct: d

## question
Która z poniższych opcji jest przykładem podejścia „najpierw test”?

## answers
a) Wytwarzanie sterowane testami modułowymi.
b) Wytwarzanie sterowane testami integracyjnymi.
c) Wytwarzanie sterowane testami systemowymi.
d) Wytwarzanie sterowane testami akceptacyjnymi.

## justification
a) Odpowiedź niepoprawna. Wytwarzanie sterowane testami modułowymi nie jest poprawnym przykładem podejścia „najpierw test”.
b) Odpowiedź niepoprawna. Wytwarzanie sterowane testami integracyjnymi nie jest poprawnym przykładem podejścia „najpierw test”.
c) Wytwarzanie sterowane testami systemowymi nie jest poprawnym przykładem podejścia „najpierw test”.
d) Odpowiedź poprawna. Wytwarzanie sterowane testami akceptacyjnymi (ATDD) jest dobrze znanym przykładem podejścia „najpierw test”.

---

# metadata
lo: FL-2.1.5
k-level: K2
points: 1
correct: b

## question
Która z poniższych opcji **najlepiej** opisuje podejście „przesunięcie w lewo”?

## answers
a) Po uzgodnieniu z programistami manualne czynności występujące we wczesnych fazach modelu wytwarzania oprogramowania są automatyzowane, aby wspierać zasadę „wczesne testowanie oszczędza czas i pieniądze”.
b) Czynności testowe są przenoszone do wcześniejszych faz cyklu wytwórczego w celu zmniejszenia całkowitych kosztów jakości poprzez zmniejszenie liczby defektów wykrytych w fazach późniejszych.
c) W miarę możliwości testerzy są zobowiązani do automatyzacji testów regresji, zaczynając od testów modułowych i testów integracyjnych modułów.
d) W miarę możliwości testerzy są szkoleni w zakresie wykonywania zadań na wczesnym etapie cyklu wytwarzania, aby umożliwić automatyzację większej liczby czynności testowych w późniejszych etapach cyklu wytwarzania.

## justification
a) Odpowiedź niepoprawna. Praktyki związane z „przesunięciem w lewo” mają na celu wdrożenie większej liczby czynności testowych we wczesnych fazach cyklu życia oprogramowania, przedstawiając ten cykl jako proces przebiegający od lewej do prawej strony. Nie ma czegoś takiego jak „przesunięcie w lewo” procesu testowego.
b) Odpowiedź poprawna. „Przesunięcie w lewo” podkreśla znaczenie rozpoczęcia testowania na wcześniejszym etapie cyklu życia oprogramowania. Wdrożenie testowania w podejściu „przesunięcie w lewo” wymaga dodatkowych szkoleń oraz zwiększonego wysiłku i kosztów na wczesnych etapach cyklu życia oprogramowania, jednak ogólne oszczędności powinny być wyższe niż koszty.
c) Odpowiedź niepoprawna. Chociaż automatyczne testy modułowe i testy integracyjne modułów jako testy regresji są generalnie cenne, tworzenie tych testów należy zazwyczaj do obowiązków programistów, a jeśli stosuje się podejście ciągłej integracji/ciągłego dostarczania (CI/CD), testy te zostaną przesłane wraz z kodem. W niektórych sytuacjach tester może zautomatyzować testy regresji, a czasem nawet testy modułowe i testy integracyjne modułów, jednak nie jest to częścią podejścia „przesunięcie w lewo”, które przenosi testowanie na wcześniejszy etap cyklu życia oprogramowania.
d) Odpowiedź niepoprawna. Szkolenie testerów w zakresie wykonywania zadań na wczesnym etapie cyklu życia oprogramowania wspierałoby podejście „przesunięcie w lewo”, podkreślając znaczenie rozpoczęcia testowania na wcześniejszym etapie cyklu życia. Jednak automatyzacja większej liczby czynności testowych, które mają być wykonywane na późniejszym etapie cyklu życia, nie jest częścią tego podejścia.

---

# metadata
lo: FL-2.1.6
k-level: K2
points: 1
correct: c

## question
Która z poniższych opcji jest **najmniej** **prawdopodobną** konsekwencją retrospektywy?

## answers
a) Jakość przyszłych przedmiotów testów poprawia się dzięki identyfikacji usprawnień w praktykach programistycznych.
b) Wydajność testów poprawia się poprzez przyspieszenie konfiguracji środowisk testowych dzięki automatyzacji.
c) Następuje poprawa zrozumienia procesów wytwarzania i testowania oprogramowania przez użytkowników końcowych.
d) Automatyczne skrypty testowe są udoskonalone dzięki informacjom zwrotnym od programistów.

## justification
a) Odpowiedź niepoprawna. Jednym z celów retrospektyw jest identyfikacja potencjalnych udoskonaleń procesów, które po wdrożeniu powinny skutkować wyższą jakością przyszłych wyników procesu rozwoju (przedmiotów testów). Jest to więc prawdopodobne w wyniku retrospektywy.
b) Odpowiedź niepoprawna. Korzyścią płynącą z retrospektyw dla testowania jest zwiększona wydajność testów dzięki udoskonaleniom procesów. Jest to więc prawdopodobne w wyniku retrospektywy.
c) Odpowiedź poprawna. Uczestnikami retrospektyw są zazwyczaj testerzy, programiści, architekci, właściciele produktu i analitycy biznesowi, ale użytkownicy końcowi rzadko są zapraszani lub uczestniczą w tych spotkaniach -- i jest również mało prawdopodobne, aby otrzymywali jakiekolwiek raporty z tych spotkań. Jest więc bardzo mało prawdopodobne, aby dzięki retrospektywom dowiedzieli się więcej o procesach rozwoju i testowania i lepiej je zrozumieli.
d) Odpowiedź niepoprawna. Korzyścią płynącą z retrospektyw dla testowania jest poprawa jakości testaliów (w tym automatycznych skryptów testowych) poprzez wspólne przeglądy z programistami. Jest to więc prawdopodobne w wyniku retrospektywy.

---

# metadata
lo: FL-2.2.1
k-level: K2
points: 1
correct: d

## question
Który z poniższych poziomów testów jest **najprawdopodobniej** wykonywany, jeśli przyjmiemy, że testowanie koncentruje się na walidacji i nie jest wykonywane przez testerów?

## answers
a) Testowanie modułowe.
b) Testowanie integracji modułów.
c) Testowanie integracji systemów.
d) Testowanie akceptacyjne.

## justification
a) Odpowiedź niepoprawna. Testowanie modułowe (zwane również testowaniem jednostkowym) polega na testowaniu poszczególnych modułów w izolacji i polega głównie na weryfikacji zgodności ze specyfikacją, a nie na walidacji pod kątem potrzeb użytkowników. Jednak testy te nie są zazwyczaj wykonywane przez testerów, lecz programistów, którzy zazwyczaj przeprowadzają je w swoim środowisku programistycznym.
b) Odpowiedź niepoprawna. Testowanie integracyjne modułów polega na testowaniu interfejsów i interakcji między modułami oraz na weryfikacji zgodności ze specyfikacją, a nie na walidacji pod kątem potrzeb użytkowników. Jednak testy te nie są zazwyczaj przeprowadzane przez testerów, lecz programistów, którzy zazwyczaj przeprowadzają je w swoim środowisku programistycznym.
c) Odpowiedź niepoprawna. Testowanie integracyjne systemów obejmuje badanie interfejsów z innymi systemami i usługami zewnętrznymi i polega głównie na weryfikacji zgodności ze specyfikacją, a nie na walidacji zgodności z potrzebami użytkowników. Tego typu testy są również najczęściej przeprowadzane przez testerów.
d) Odpowiedź poprawna. Testowanie akceptacyjne koncentruje się na sprawdzeniu, czy system spełnia potrzeby biznesowe użytkownika i jest gotowy do wdrożenia. Idealnie byłoby, gdyby testy te były przeprowadzane przez użytkowników końcowych.

---

# metadata
lo: FL-2.2.3
k-level: K2
points: 1
correct: b

## question
Oprogramowanie systemu nawigacyjnego zostało zaktualizowane, ponieważ sugerowało trasy naruszające przepisy ruchu drogowego, np. jazdę pod prąd ulicami jednokierunkowymi.
Które z poniższych stwierdzeń najlepiej opisuje testowanie, które powinno zostać przeprowadzone?

## answers
a) Tylko testowanie potwierdzające.
b) Testowanie potwierdzające, a następnie testowanie regresji.
c) Tylko testowanie regresji.
d) Testowanie regresji, a następnie testowanie potwierdzające.

## justification
a) Odpowiedź niepoprawna. Konieczne jest przeprowadzenie testowania potwierdzającego, aby sprawdzić, czy aktualizacje doprowadziły do prawidłowej implementacji, jednak rozsądne byłoby przeprowadzenie następnie testowania regresji w celu upewnienia się, że nie wprowadzono żadnych defektów ani nie wykryto ich w niezmienionych obszarach systemu.
b) Odpowiedź poprawna. Testowanie potwierdzające sprawdza, czy aktualizacje doprowadziły do prawidłowej implementacji, a następnie przeprowadzone testowanie regresji sprawdza, czy nie wprowadzono żadnych defektów ani nie wykryto żadnych defektów w niezmienionych obszarach systemu.
c) Odpowiedź niepoprawna. Testowanie regresji powinno być wykorzystane w celu zapewnienia, że podczas aktualizacji nie wprowadzono ani nie wykryto żadnych defektów w niezmienionych obszarach systemu, jednak konieczne jest również przeprowadzenie testowania potwierdzającego, które sprawdza, czy aktualizacje doprowadziły do prawidłowej implementacji.
d) Odpowiedź niepoprawna. Testowanie potwierdzające sprawdza, czy aktualizacje doprowadziły do prawidłowej implementacji, a testowanie regresji służy do upewnienia się, że w niezmienionych obszarach systemu nie wprowadzono ani nie wykryto żadnych defektów. Jednak w przypadku ich przeprowadzenia (tj. gdy aktualizacja wymaga przetestowania) testy potwierdzające poprzedzają testy regresji.

---

# metadata
lo: FL-3.1.3
k-level: K2
points: 1
correct: d

## question
Rozważ następujące przykładowe defekty:

i. Dwie różne części specyfikacji projektu są ze sobą niezgodne ze względu na złożoność projektu.
ii. Czas odpowiedzi jest zbyt długi, co powoduje utratę cierpliwości użytkowników.
iii. Ścieżka w kodzie jest nieosiągalna podczas wykonywania.
iv. Zmienna została zadeklarowana, ale nigdy nie została użyta w programie.
v. Ilość pamięci potrzebna programowi do wygenerowania raportu jest zbyt duża.

Które z poniższych najlepiej identyfikuje przykładowe defekty, które można wykryć raczej za pomocą testowania statycznego niż testowania dynamicznego?

## answers
a) ii, v.
b) iii, v.
c) i, ii, iv.
d) i, iii, iv.

## justification
i. Dwie różne części specyfikacji projektowej są ze sobą niezgodne ze względu na złożoność projektu -- jest to przykład defektu specyfikacji, która obejmuje niespójności, niejasności, sprzeczności, pominięcia, nieścisłości i powtórzenia, które najłatwiej wykryć za pomocą testów statycznych.
ii. Czas odpowiedzi jest zbyt długi, co powoduje utratę cierpliwości użytkowników -- jest to przykład defektu czasu odpowiedzi, który można wykryć w praktyce jedynie poprzez uruchomienie programu i pomiar czasu odpowiedzi, co najłatwiej wykryć za pomocą testów dynamicznych.
iii. Ścieżka w kodzie jest nieosiągalna podczas wykonywania -- jest to przykład defektu kodowania, który obejmuje zmienne o nieokreślonych wartościach, zmienne niezadeklarowane, zduplikowany lub nieosiągalny kod oraz nadmierną złożoność kodu, które najłatwiej wykryć za pomocą testów statycznych.
iv. Zmienna została zadeklarowana, ale nigdy nie została użyta w programie -- jest to przykład defektu kodowania, który obejmuje zmienne o nieokreślonych wartościach, zmienne niezadeklarowane, zduplikowany lub nieosiągalny kod oraz nadmierną złożoność kodu, które najłatwiej wykryć za pomocą testów statycznych.
v. Ilość pamięci potrzebna programowi do wygenerowania raportu jest zbyt duża -- jest to przykład defektu wydajności, który można wykryć w praktyce jedynie poprzez uruchomienie programu i pomiar wykorzystanej pamięci, co najłatwiej wykryć za pomocą testów dynamicznych.

Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-3.2.1
k-level: K1
points: 1
correct: a

## question
Która z poniższych opcji jest zaletą wczesnego i częstego otrzymywania informacji zwrotnych od interesariuszy?

## answers
a) Zmiany wymagań są lepiej rozumiane i szybciej wdrażane.
b) Interesariusze biznesowi rozumieją wymagania użytkowników.
c) Właściciele produktu mogą zmieniać wymagania dowolnie często.
d) Użytkownicy końcowi są informowani przed wydaniem produktu, które wymagania nie zostaną wdrożone.

## justification
a) Odpowiedź poprawna. Uzyskiwanie wczesnych i częstych informacji zwrotnych od interesariuszy może być bardzo korzystne. Ułatwia wczesną komunikację potencjalnych problemów związanych z jakością, może zapobiec nieporozumieniom dotyczącym wymagań i zapewnia, że wszelkie zmiany w wymaganiach interesariuszy są lepiej zrozumiałe i wdrażane szybciej.
b) Odpowiedź niepoprawna. Informacje zwrotne pochodzą od interesariuszy, a przekazywanie przez nich informacji zwrotnych raczej nie poprawi zrozumienia ich własnych wymagań.
c) Odpowiedź niepoprawna. Uzyskiwanie wczesnych i częstych informacji zwrotnych od interesariuszy może być bardzo korzystne. Ułatwia wczesną komunikację potencjalnych problemów związanych z jakością, może zapobiec nieporozumieniom dotyczącym wymagań i zapewnia, że wszelkie zmiany w wymaganiach interesariuszy są lepiej zrozumiałe i wdrażane szybciej. Jednak fakt, że zmiany w wymaganiach mogą być lepiej zrozumiałe i szybciej wdrażane, nie oznacza, że zachęca się do nieograniczonych zmian w wymaganiach.
d) Odpowiedź niepoprawna. Informacje zwrotne pochodzą od interesariuszy i nie obejmują komunikacji z nimi. Komunikacja z użytkownikami końcowymi może obejmować poinformowanie ich o tym, które wymagania nie zostaną wdrożone przed wydaniem produktu, ale w idealnym przypadku nie powinno to mieć miejsca.

---

# metadata
lo: FL-3.2.4
k-level: K2
points: 1
correct: b

## question
Rozważ następujące rodzaje przeglądów (1--4) oraz opisy przeglądów (A--D).

1. Przegląd techniczny.
2. Przegląd nieformalny.
3. Inspekcja.
4. Przejrzenie.

A. Obejmuje takie cele, jak osiągnięcie konsensusu, generowanie nowych pomysłów i motywowanie autorów do doskonalenia się.
B. Obejmuje takie cele, jak edukacja przeglądających, osiągnięcie konsensusu, generowanie nowych pomysłów i wykrywanie potencjalnych defektów.
C. Głównym celem jest wykrywanie potencjalnych defektów i wymaga gromadzenia zestawu metryk w celu wsparcia doskonalenia procesów.
D. Głównym celem jest wykrywanie potencjalnych defektów i nie generuje żadnych formalnych, udokumentowanych wyników.

Która z poniższych opcji najlepiej przyporządkowuje typy przeglądów do ich opisów?

## answers
a) 1A, 2B, 3C, 4D.
b) 1A, 2D, 3C, 4B.
c) 1B, 2C, 3D, 4A.
d) 1C, 2D, 3A, 4B.

## justification
Biorąc pod uwagę każdy z wymienionych typów przeglądów:
1. Przegląd techniczny -- ten typ przeglądu jest przeprowadzany przez przeglądających posiadających kwalifikacje techniczne i prowadzony przez moderatora. Jego celem jest osiągnięcie konsensusu i podjęcie decyzji dotyczących problemów technicznych, a także ocena jakości i budowanie zaufania do produktu pracy, generowanie nowych pomysłów, motywowanie i umożliwianie autorom doskonalenia się oraz wykrywanie anomalii.
2. Przegląd nieformalny -- głównym celem jest wykrycie anomalii. Proces nie jest zdefiniowany i nie wymaga formalnego, udokumentowanego wyniku.
3. Inspekcja -- jest to najbardziej formalny typ przeglądu, który przebiega zgodnie z kompletnym procesem przeglądu. Głównym celem jest wykrycie jak największej liczby anomalii, a inne cele obejmują ocenę jakości i budowanie zaufania do produktu pracy, motywowanie i umożliwianie autorom doskonalenia się oraz gromadzenie metryk, które można wykorzystać do usprawnienia cyklu wytwarzania oprogramowania, w tym procesu samej inspekcji. Autor nie może pełnić funkcji lidera przeglądu ani protokolanta.
4. Przejrzenie -- ten typ przeglądu, prowadzony przez autora, służy różnym celom, takim jak ocena jakości i budowanie zaufania do produktu pracy, edukacja przeglądających, osiągnięcie konsensusu, generowanie nowych pomysłów, motywowanie i umożliwianie autorom doskonalenia się oraz wykrywanie anomalii. Przeglądający mogą przeprowadzić indywidualny przegląd przed przejrzeniem (np. w ramach spotkania przeglądowego), ale nie jest to obowiązkowe.

A. Obejmuje takie cele, jak osiągnięcie konsensusu, generowanie nowych pomysłów i motywowanie autorów do doskonalenia się.
B. Obejmuje takie cele, jak edukacja przeglądających, osiągnięcie konsensusu, generowanie nowych pomysłów i wykrywanie anomalii.
C. Głównym celem jest wykrywanie anomalii i wymaga gromadzenia metryk w celu wsparcia usprawniania procesów.
D. Głównym celem jest wykrywanie anomalii i nie generuje żadnych formalnych, udokumentowanych wyników.

W związku z tym:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-3.2.5
k-level: K1
points: 1
correct: b

## question
Który z poniższych czynników przyczynia się do pomyślnego przeprowadzenia przeglądu?

## answers
a) Zapewnienie udziału kierownictwa jako przeglądających w procesie przeglądu.
b) Podział dużych produktów pracy na mniejsze części.
c) Ustanowienie oceny przeglądającego jako celu.
d) Zaplanowanie przeglądu jednego dokumentu na raz.

## justification
a) Odpowiedź niepoprawna. Aby zapewnić pomyślny przebieg przeglądów, ważne jest zapewnienie wsparcia kierownictwa dla procesu przeglądu, jednak nie oznacza to, że powinno ono uczestniczyć w przeglądach jako przeglądający.
b) Odpowiedź poprawna. Aby zapewnić pomyślny przebieg przeglądów, ważne jest podzielenie produktu pracy na części, które są na tyle małe, że można je przejrzeć w rozsądnym czasie, aby przeglądający nie tracili koncentracji podczas indywidualnych przeglądów lub spotkań przeglądowych.
c) Odpowiedź niepoprawna. Aby zapewnić pomyślny przebieg przeglądów, ważne jest jasne zdefiniowanie celów i mierzalnych kryteriów wyjścia, bez oceny uczestników.
d) Odpowiedź niepoprawna. Aby zapewnić pomyślny przebieg przeglądów, należy podzielić przegląd na mniejsze części, aby przeglądający nie tracili koncentracji podczas indywidualnych przeglądów lub spotkań przeglądowych. Nie należy więc planować przeglądu jednego dokumentu podczas jednego przeglądu, jeśli jest on np. bardzo duży.

---

# metadata
lo: FL-4.1.1
k-level: K2
points: 1
correct: c

## question
Jaka jest **główna** różnica między czarnoskrzynkowymi technikami testowania a technikami testowania opartymi na doświadczeniu?

## answers
a) Przedmiot testów.
b) Poziom testów, na którym stosowana jest dana technika.
c) Podstawa testów.
d) Cykl wytwarzania oprogramowania, w którym można zastosować daną technikę.

## justification
a) Odpowiedź niepoprawna. W większości przypadków zarówno czarnoskrzynkowe techniki testowania, jak i techniki testowania oparte na doświadczeniu mogą być stosowane do tych samych przedmiotów testów.
b) Odpowiedź niepoprawna. Zarówno czarnoskrzynkowe techniki testowania, jak i techniki testowania oparte na doświadczeniu mogą być stosowane na wszystkich poziomach testów.
c) Odpowiedź poprawna. Czarnoskrzynkowe techniki testowania (znane również technikami opartymi na specyfikacji) opierają się na analizie określonego zachowania przedmiotu testów bez odniesienia do jego wewnętrznej struktury. Podstawą testu jest więc zazwyczaj specyfikacja. Techniki testowania oparte na doświadczeniu skutecznie wykorzystują wiedzę i doświadczenie testerów do projektowania i implementacji przypadków testowych. Oznacza to, że tester podczas projektowania testów może w ogóle nie korzystać ze specyfikacji.
d) Odpowiedź niepoprawna. Techniki testowania oparte na doświadczeniu mogą wykrywać defekty, które mogą zostać pominięte przy użyciu czarnoskrzynkowych i białoskrzynkowych technik testowania. Dlatego techniki testowania oparte na doświadczeniu stanowią uzupełnienie technik czarno- i białoskrzynkowych, a zarówno techniki czarnoskrzynkowe, jak i techniki testowania oparte na doświadczeniu mogą być stosowane we wszystkich cyklach życia oprogramowania.

---

# metadata
lo: FL-4.2.1
k-level: K3
points: 1
correct: a

## question
Testujesz walidator, który akceptuje prawidłowe kody PIN i odrzuca nieprawidłowe. Kod PIN to sekwencja cyfr. Kod PIN jest prawidłowy, jeśli składa się z czterech cyfr, z których co najmniej dwie są różne. Zidentyfikowano następujące poprawne klasy równoważności KR1-KR6:

Zmienna: prawidłowość kodu PIN

- KR1: „kod PIN prawidłowy” (zawierająca prawidłowe kody PIN)
- KR2: „kod PIN nieprawidłowy” (zawierająca nieprawidłowe kody PIN)

Zmienna: długość kodu PIN

- KR3: „długość poprawna” (zawierająca kody PIN o długości 4)
- KR4: „długość niepoprawna” (zawierająca kody PIN o długości innej niż 4)

Zmienna: liczba różnych cyfr w kodzie PIN

- KR5: „liczba różnych cyfr poprawna” (zawierająca kody PIN mające co najmniej dwie różne cyfry)
- KR6: „liczba różnych cyfr niepoprawna” (zawierająca kody PIN, w których wszystkie cyfry są identyczne)

Który z poniższych zestawów wejściowych danych testowych osiąga pełne pokrycie klas równoważności dla tego scenariusza?

## answers
a) 1111, 1234, 12345.
b) 123, 1111, 12345.
c) 11, 1111, 11111.
d) 1111, 1234, 1112.

## justification
Istnieje sześć klas równoważności KR1--KR6 w trzech zidentyfikowanych dziedzinach, które muszą być pokryte przypadkami testowymi.
a) Odpowiedź poprawna. 1111 pokrywa KR2, KR3 i KR6. 1234 dodatkowo pokrywa KR1 i KR5. 12345 dodatkowo pokrywa KR4. Wszystkie klasy równoważności są pokryte.
b) Odpowiedź niepoprawna. Żaden przypadek testowy nie pokrywa KR1.
c) Odpowiedź niepoprawna. Żaden przypadek testowy nie pokrywa klas KR1 i KR5.
d) Odpowiedź niepoprawna. Żaden przypadek testowy nie pokrywa KR4.

---

# metadata
lo: FL-4.2.2
k-level: K3
points: 1
correct: d

## question
Programista został poproszony o zaimplementowanie następującej reguły biznesowej:

> WEJŚCIE: X (liczba całkowita)
>
> JEŚLI (X ≤ 100 LUB X ≥ 200) TO napisz „wartość niepoprawna”
>
> W PRZECIWNYM RAZIE napisz „wartość poprawna”

Projektujesz przypadki testowe przy użyciu dwupunktowej analizy wartości brzegowych.
Który z poniższych zestawów danych wejściowych testowych zapewni **największe** pokrycie?

## answers
a) 100, 150, 200, 201.
b) 99, 100, 200, 201.
c) 98, 99, 100, 101.
d) 101, 150, 199, 200.

## justification
Klasy równoważności to: {..., 99, 100}, {101, 102, ..., 198, 199}, {200, 201, ...}.
W tym podziale dziedziny istnieją 4 wartości brzegowe klas równoważności: 100, 101, 199 i 200. W dwupunktowej analizie wartości brzegowych dla każdej wartości brzegowej istnieją dwa elementy pokrycia: ta wartość brzegowa oraz jej najbliższy sąsiad należący do sąsiedniej klasy równoważności. Ponieważ najbliżsi sąsiedzi są również wartościami brzegowymi sąsiednich klas równoważności, istnieją tylko cztery elementy pokrycia będące czterema wyżej wymienionymi wartościami brzegowymi.
Zatem:
a) Odpowiedź niepoprawna. Tylko 100 i 200 są prawidłowymi elementami pokrycia dla dwupunktowej analizy wartości brzegowych, więc osiągamy 50% pokrycia.
b) Odpowiedź niepoprawna. Tylko 100 i 200 są prawidłowymi elementami pokrycia dla dwupunktowej analizy wartości brzegowych, więc osiągamy 50% pokrycia.
c) Odpowiedź niepoprawna. Tylko 100 i 101 są prawidłowymi elementami pokrycia dla dwupunktowej analizy wartości brzegowych, więc osiągamy 50% pokrycia.
d) Odpowiedź poprawna. 101, 199 i 200 są poprawnymi elementami pokrycia dla dwupunktowej analizy wartości brzegowych, więc osiągamy 75% pokrycia.

---

# metadata
lo: FL-4.2.3
k-level: K3
points: 1
correct: d

## question
Pracujesz nad projektem systemu do analizy wyników egzaminów na prawo jazdy. Poproszono Cię o zaprojektowanie przypadków testowych w oparciu o poniższą tablicę decyzyjną.

| | **Reguła 1** | **Reguła 2** | **Reguła 3** |
| :--- | :---: | :---: | :---: |
| W1: Pierwsza próba zdania egzaminu? | -- | -- | NIE |
| W2: Egzamin teoretyczny zdany? | TAK | NIE | -- |
| W3: Egzamin praktyczny zdany? | TAK | -- | NIE |
| Wydanie prawa jazdy | X | | |
| Żądanie dodatkowych lekcji jazdy | | | X |
| Żądanie ponownego przystąpienia do egzaminu | | X | |

Jakie dane testowe pokażą, że w tablicy decyzyjnej występują **sprzeczne** reguły?

## answers
a) W1 = TAK, W2 = TAK, W3 = NIE.
b) W1 = TAK, W2 = NIE, W3 = TAK.
c) W1 = TAK, W2 = TAK, W3 = TAK oraz W1 = NIE, W2 = TAK, W3 = TAK.
d) W1 = NIE, W2 = NIE, W3 = NIE.

## justification
a) Odpowiedź niepoprawna. Kombinacja (TAK, TAK, NIE) nie pasuje do żadnej reguły. Jest to przykład pominięcia, a nie sprzeczności.
b) Odpowiedź niepoprawna. Kombinacja (TAK, NIE, TAK) pasuje tylko do jednej kolumny, „Reguła 2”, więc nie ma sprzeczności.
c) Odpowiedź niepoprawna. Zarówno kombinacja (TAK, TAK, TAK), jak i (NIE, TAK, TAK) pasują tylko do jednej kolumny, „Reguła 1”, więc nie ma sprzeczności.
d) Odpowiedź poprawna. Kombinacja (NIE, NIE, NIE) pasuje zarówno do kolumny „Reguła 2”, jak i „Reguła 3”, ale akcje dla tych kolumn są różne, więc pokazuje to sprzeczność między tymi dwoma regułami.

---

# metadata
lo: FL-4.2.4
k-level: K3
points: 1
correct: a

## question
Projektujesz przypadki testowe na podstawie poniższego diagramu stanów.

Przejścia:

- START --Room request--> REQUESTING
- REQUESTING --Not available--> WAITING LIST
- REQUESTING --Available--> CONFIRMED
- WAITING LIST --Available--> CONFIRMED
- WAITING LIST --Cancel--> END
- CONFIRMED --Pay--> END

Jaka jest **minimalna** liczba przypadków testowych wymagana do osiągnięcia 100% pokrycia przejść poprawnych?

## answers
a) 3.
b) 2.
c) 5.
d) 6.

## justification
Trzy przejścia etykietowane zdarzeniami „Available” oraz „Cancel” nie mogą pojawić się w tym samym przypadku testowym, co oznacza, że wymagane są co najmniej trzy przypadki testowe, z których każdy pokrywa jedno z tych trzech przejść. Pozostałe przejścia można pokryć rzeczywiście w ramach tych trzech przypadków testowych:

- TC1: Room request, Available, Pay,
- TC2: Room request, Not available, Available, Pay,
- TC3: Room request, Not available, Cancel.

A zatem:
a) Odpowiedź poprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.3.2
k-level: K2
points: 1
correct: c

## question
Chcesz zastosować testowanie gałęzi do kodu przedstawionego na poniższym wykresie przepływu sterowania.

Wykres przepływu sterowania składa się z siedmiu węzłów. Oznaczając punkt wejścia jako węzeł 1, a punkt wyjścia jako węzeł 7, wykres zawiera następujące krawędzie: 1->2, 2->3, 3->2, 2->4, 4->5, 4->6, 5->7, 6->7 (łącznie 8 krawędzi; węzły 3 i 2 tworzą pętlę powrotną).

Ile **elementów** **pokrycia** musisz przetestować?

## answers
a) 2.
b) 4.
c) 8.
d) 7.

## justification
W testowaniu gałęzi elementami pokrycia są gałęzie reprezentowane przez krawędzie w grafie przepływu sterowania. Graf przepływu sterowania zawiera 8 krawędzi.
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.3.3
k-level: K2
points: 1
correct: a

## question
W jaki sposób testowanie białoskrzynkowe może być przydatne we wspieraniu testowania czarnoskrzynkowego?

## answers
a) Miary pokrycia białoskrzynkowego mogą pomóc testerom w ocenie czarnoskrzynkowych testów pod kątem pokrycia kodu osiągniętego przez te testy czarnoskrzynkowe.
b) Analiza pokrycia białoskrzynkowego może pomóc testerom w identyfikacji nieosiągalnych fragmentów kodu źródłowego.
c) Testowanie gałęzi jest silniejsze niż czarnoskrzynkowe techniki testowania, więc osiągnięcie pełnego pokrycia gałęzi gwarantuje osiągnięcie pełnego pokrycia dowolnej techniki czarnoskrzynkowej.
d) Białoskrzynkowe techniki testowania mogą zapewnić elementy pokrycia dla czarnoskrzynkowych technik testowania.

## justification
a) Odpowiedź poprawna. Przeprowadzanie wyłącznie testów czarnoskrzynkowych nie zapewnia pomiaru rzeczywistego pokrycia kodu. Pomiar pokrycia białoskrzynkowego zapewnia obiektywny pomiar pokrycia i dostarcza informacji niezbędnych do wygenerowania dodatkowych testów w celu zwiększenia tego pokrycia, a tym samym zwiększenia zaufania do kodu.
b) Odpowiedź niepoprawna. To stwierdzenie jest poprawne, ale nie ma nic wspólnego z testowaniem czarnoskrzynkowym.
c) Odpowiedź niepoprawna. Ogólnie rzecz biorąc, nie ma relacji subsumpcji między technikami czarno- i białoskrzynkowymi.
d) Odpowiedź niepoprawna. Techniki białoskrzynkowe są wykorzystywane do projektowania testów w oparciu o sam przedmiot testów, natomiast techniki czarnoskrzynkowe są wykorzystywane do projektowania testów w oparciu o specyfikację. Dlatego też nie ma związku między elementami pokrycia wynikającymi z tych dwóch typów technik.

---

# metadata
lo: FL-4.4.1
k-level: K2
points: 1
correct: b

## question
Rozważ poniższą listę:

- Poprawne dane wejściowe nie są akceptowane.
- Niepoprawne dane wejściowe są akceptowane.
- Niepoprawny format danych wyjściowych.
- Wystąpienie dzielenia przez zero.

Jaka technika testowania jest **najprawdopodobniej** stosowana przez testera, który korzysta z tej listy podczas przeprowadzania testów?

## answers
a) Testowanie eksploracyjne.
b) Atak usterek.
c) Testowanie oparte na liście kontrolnej.
d) Analiza wartości brzegowych.

## justification
a) Odpowiedź niepoprawna. Testowanie eksploracyjne wykorzystuje karty opisu testu, a nie listę możliwych defektów/awarii. Chociaż testowanie eksploracyjne może obejmować wykorzystanie innych technik testowania, w tym przypadku atak usterek jest najbardziej prawdopodobną opcją.
b) Odpowiedź poprawna. Jest to lista możliwych awarii. Ataki usterek są metodycznym podejściem do zgadywania błędów i wymagają od testera stworzenia lub uzyskania listy możliwych błędów, defektów i awarii oraz zaprojektowania testów, które zidentyfikują defekty związane z błędami, ujawnią defekty lub spowodują awarie.
c) Odpowiedź niepoprawna. Tester korzysta z listy kontrolnej w celu wsparcia testowania. Zarówno zgadywanie błędów, jak i testowanie oparte na liście kontrolnej wykorzystują takie listy, jednak lista ta zawiera możliwe awarie, a nie warunki testowe, dlatego *najbardziej prawdopodobną* techniką testowania jest atak usterek, który koncentruje się na błędach, defektach i awariach.
d) Odpowiedź niepoprawna. Analiza wartości brzegowych opiera się na wartościach brzegowych klas równoważności. Powyższa lista nie wspomina o klasach równoważności ani ich brzegach.

---

# metadata
lo: FL-4.4.3
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń **najlepiej** opisuje, w jaki sposób testowanie oparte na liście kontrolnej może skutkować zwiększeniem pokrycia?

## answers
a) Elementy listy kontrolnej mogą być zdefiniowane na wystarczająco niskim poziomie szczegółowości, dzięki czemu tester może wdrożyć i wykonać szczegółowe przypadki testowe w oparciu o te elementy.
b) Listy kontrolne mogą być zautomatyzowane, więc za każdym razem, gdy automatyczne wykonanie testu obejmuje elementy listy kontrolnej, skutkuje to dodatkowym pokryciem.
c) Każdy element listy kontrolnej powinien być testowany oddzielnie i niezależnie, dzięki czemu elementy obejmują różne obszary oprogramowania.
d) Dwóch testerów projektujących i wykonujących testy w oparciu o te same elementy listy kontrolnej wysokiego poziomu zazwyczaj przeprowadza te testy w nieco inny sposób.

## justification
a) Odpowiedź niepoprawna. Chociaż prawdą jest, że tester może zaimplementować i wykonać szczegółowe przypadki testowe w oparciu o listę kontrolną, nie wyjaśnia to, w jaki sposób miałoby to skutkować zwiększeniem pokrycia.
b) Odpowiedź niepoprawna. Elementy listy kontrolnej nie powinny być automatyzowane. Ale nawet jeśli są, automatyczne skrypty testowe zawsze wykonują testy w ten sam sposób, co zazwyczaj nie skutkuje zwiększeniem pokrycia.
c) Odpowiedź niepoprawna. Prawdą jest, że każdy element listy kontrolnej powinien być testowany oddzielnie i niezależnie. Ma to jednak wpływ na kolejność wykonywania testów, a nie na osiągnięte pokrycie, więc nie skutkuje zwiększeniem pokrycia.
d) Odpowiedź poprawna. Jeśli listy kontrolne są wysokiego poziomu, prawdopodobnie wystąpi pewna zmienność w rzeczywistym testowaniu, co może skutkować większym pokryciem, ale mniejszą powtarzalnością. Jeśli dwóch testerów postępuje zgodnie z listą kontrolną zawierającą pozycje wysokiego poziomu, każdy z nich może używać innych danych testowych, kroków testowych itp. W ten sposób każdy tester prawdopodobnie pokryje niektóre obszary nieobjęte przez drugiego testera, co spowoduje zwiększenie pokrycia.

---

# metadata
lo: FL-4.5.2
k-level: K2
points: 1
correct: b

## question
Która z poniższych opcji stanowi **najlepszy** przykład kryterium akceptacji zorientowanego na scenariusze?

## answers
a) Aplikacja musi umożliwiać użytkownikom usunięcie swojego konta i wszystkich powiązanych danych na żądanie.
b) Kiedy klient dodaje produkt do koszyka i przechodzi do kasy, powinien zostać poproszony o zalogowanie się lub utworzenie konta, jeśli jeszcze tego nie zrobił.
c) JEŻELI (contain(product(23).Name, cart.products())) TO ZWRÓĆ Fałsz.
d) Witryna internetowa musi być zgodna z normą ICT Accessibility 508 i zapewniać dostępność wszystkich treści dla użytkowników niepełnosprawnych.

## justification
a) Odpowiedź niepoprawna. To kryterium akceptacji opisuje zasady lub przepisy, których system musi przestrzegać (w tym przypadku prawo do bycia zapomnianym). Jest to przykład kryterium akceptacji zapisanego w formacie zorientowanym na reguły.
b) Odpowiedź poprawna. To kryterium akceptacji opisuje przykładowy scenariusz, który musi być możliwy do zrealizowania przez system. Jest to przykład kryterium akceptacji zapisanego w formacie zorientowanym na scenariusze.
c) Odpowiedź niepoprawna. To zdanie wygląda bardziej jak linia kodu, która implementuje regułę biznesową. Kryteria akceptacji powinny być opracowywane we współpracy z przedstawicielami jednostek biznesowych, a zatem powinny być napisane językiem, który rozumieją. To zdanie najprawdopodobniej będzie niezrozumiałe dla tych interesariuszy.
d) Odpowiedź niepoprawna. To kryterium akceptacji opisuje, jakich zasad lub przepisów musi przestrzegać system i w jaki sposób zapewniona zostanie zgodność. Dlatego jest to przykład kryterium akceptacji zapisanego w formacie zorientowanym na reguły, a nie na scenariusze.

---

# metadata
lo: FL-4.5.3
k-level: K3
points: 1
correct: d

## question
Stosujesz wytwarzanie oparte na testach akceptacyjnych i projektujesz przypadki testowe w oparciu o następującą historyjkę użytkownika.

*Jako użytkownik zwykły lub specjalny chcę mieć możliwość korzystania z mojej elektronicznej karty dostępu aby uzyskać dostęp do określonych pięter.*

Kryteria akceptacji:

- KA1: Użytkownicy zwykli mają dostęp do pięter od 1 do 3.
- KA2: Piętro 4 jest dostępne tylko dla użytkowników specjalnych.
- KA3: Użytkownicy specjalni mają wszystkie uprawnienia dostępu użytkowników zwykłych.

Który przypadek testowy **najlepiej** przetestuje KA3?

## answers
a) Sprawdź, czy użytkownik zwykły ma dostęp do pięter 1 i 3.
b) Sprawdź, czy użytkownik zwykły nie ma dostępu do piętra 4.
c) Sprawdź, czy użytkownik specjalny ma dostęp do piętra 5.
d) Sprawdź, czy użytkownik specjalny ma dostęp do pięter 1, 2 i 3.

## justification
a) Odpowiedź niepoprawna. Chcemy sprawdzić, czy użytkownicy specjalni mają uprawnienia użytkowników zwykłych, więc musimy przetestować uprawnienia dostępu dla użytkownika specjalnego, a nie dla użytkownika zwykłego.
b) Odpowiedź niepoprawna. Chcemy sprawdzić, czy użytkownicy specjalni mają uprawnienia użytkowników zwykłych, więc musimy przetestować uprawnienia dostępu dla użytkownika specjalnego, a nie dla użytkownika zwykłego.
c) Odpowiedź niepoprawna. W kryteriach akceptacji nie ma opisu piętra 5. Przypadki testowe nie powinny wykraczać poza zakres historyjki użytkownika. Ale nawet jeśli chcielibyśmy przeprowadzić testy negatywne, ten test nie jest bezpośrednio związany z KA3.
d) Odpowiedź poprawna. W ten sposób możemy sprawdzić, czy użytkownik specjalny ma dostęp do pięter, które są dostępne dla użytkownika zwykłego.

---

# metadata
lo: FL-5.1.1
k-level: K2
points: 1
correct: a

## question
Które z poniższych **nie** jest celem planu testów?

## answers
a) Zdefiniowanie danych testowych i oczekiwanych wyników dla testów modułowych i testów integracji modułów.
b) Zdefiniowanie jako kryterium wyjścia testowania modułowego osiągnięcie 100% pokrycia instrukcji i 100% pokrycia gałęzi.
c) Opisanie, jakie pola powinien zawierać raport z postępów testów i jaka powinna być forma tego raportu.
d) Wyjaśnienie, dlaczego testy integracyjne systemów zostaną wyłączone z testowania, mimo że strategia testowa wymaga tego poziomu testów.

## justification
a) Odpowiedź poprawna. Plan testów może zawierać *wymagania* dotyczące danych testowych (jako część podejścia do testów), ale nie może zawierać szczegółowych danych testowych dla przypadków testowych. Dane testowe są częścią przypadków testowych, a nie planu testów. Ponadto zazwyczaj nie jest możliwe zdefiniowanie takich danych podczas tworzenia planu testów, ponieważ nie wiadomo dokładnie, jak będą wyglądały moduły.
b) Odpowiedź niepoprawna. Jednym z celów planu testów jest zapewnienie, że przeprowadzone czynności testowe spełnią ustalone kryteria, poprzez uwzględnienie kryteriów wejścia i wyjścia. Kryteria pokrycia kodu są przykładem takich kryteriów dla poziomu testowania modułowego.
c) Odpowiedź niepoprawna. Szablony dokumentacji są typową częścią planu testów. Pomaga to ułatwić komunikację między interesariuszami poprzez zdefiniowanie standardowego sposobu komunikacji lub raportowania.
d) Odpowiedź niepoprawna. Jednym z celów planu testów jest wykazanie, że testy będą zgodne z istniejącą polityką testów i strategią testów, lub wyjaśnienie, dlaczego testy będą od nich odbiegać. Jest to przykład wyjaśnienia odchylenia w odniesieniu do poziomów testów, które będą (lub nie będą) przestrzegane.

---

# metadata
lo: FL-5.1.4
k-level: K3
points: 1
correct: c

## question
Na początku każdej iteracji zespół szacuje nakład pracy (w osobodniach), którą będzie musiał wykonać podczas iteracji. Niech $E(n)$ będzie szacowanym nakładem pracy dla iteracji *n*, a $A(n)$ rzeczywistym nakładem pracy wykonanym w iteracji *n*.
Od trzeciej iteracji zespół stosuje następujący model szacowania oparty na ekstrapolacji:

$E(n) = \dfrac{3 \cdot A(n-1) + A(n-2)}{4}$.

Wykres przedstawia szacowaną i rzeczywistą ilość pracy dla pierwszych czterech iteracji.

| **Iteracja** | **Szacowany** | **Rzeczywisty** |
| :--- | :---: | :---: |
| Iteracja nr 1 | 8 | 7 |
| Iteracja nr 2 | 7 | 12 |
| Iteracja nr 3 | 11 | 8 |
| Iteracja nr 4 | 9 | 6 |

Jaki jest szacowany nakład pracy dla iteracji nr 5?

## answers
a) 10,5 osobodni.
b) 8,25 osobodni.
c) 6,5 osobodni.
d) 9,4 osobodni.

## justification
Z wykresu wynika, że: $A(4) = 6$ i $A(3) = 8$ (dwa ostatnie szare pola).
Podstawiając do wzoru otrzymujemy:
$E(5) = \dfrac{3 \cdot A(4) + A(3)}{4} = \dfrac{3 \cdot 6 + 8}{4} = \dfrac{26}{4} = 6,5$ osobodni.
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.1.5
k-level: K3
points: 1
correct: a

## question
Przygotowujesz harmonogram wykonania siedmiu przypadków testowych TC 1 do TC 7. Poniższa tabela przedstawia priorytety tych przypadków testowych (1 = najwyższy priorytet, 3 = najniższy priorytet) oraz zależności między przypadkami testowymi. Na przykład zależność TC 4 -> TC 5 oznacza, że TC 5 może zostać wykonany dopiero wtedy, gdy wcześniej został wykonany TC 4.

| **Przypadek testowy** | **Priorytet** | **Zależy od** |
| :--- | :---: | :--- |
| TC 1 | 2 | brak |
| TC 2 | 3 | TC 1 |
| TC 3 | 2 | brak |
| TC 4 | 2 | brak |
| TC 5 | 1 | TC 2, TC 4 |
| TC 6 | 3 | TC 5 |
| TC 7 | 1 | TC 4 |

Który przypadek testowy powinien zostać wykonany jako **szósty**?

## answers
a) TC 3.
b) TC 5.
c) TC 6.
d) TC 2.

## justification
Chcemy wykonać przypadki testowe zgodnie z ich priorytetami, ale musimy również wziąć pod uwagę zależności.
Jeśli weźmiemy pod uwagę tylko priorytety, najpierw należy wykonać TC 5 i TC 7 (najwyższy priorytet), następnie TC 1, TC 3 i TC 4, a na końcu TC 2 i TC 6 (najniższy priorytet). Jednak, aby uruchomić TC 7, musimy najpierw uruchomić TC 4. Z kolei, aby uruchomić TC 5, musimy uruchomić TC 4 i TC 2, ale TC 2 jest blokowane przez TC 1, które powinno zostać uruchomione przed TC 2.
Aby więc jak najwcześniej uruchomić przypadki testowe o priorytecie 1, pierwsze pięć przypadków testowych powinno wyglądać następująco: TC 4 -- TC 7 -- TC 1 -- TC 2 -- TC 5. Następnie musimy uruchomić TC 3, ponieważ ma on wyższy priorytet niż TC 6. Pełny harmonogram będzie więc wyglądał następująco: TC 4 -- TC 7 -- TC 1 -- TC 2 -- TC 5 -- TC 3 -- TC 6. Dlatego szóstym przypadkiem testowym będzie TC 3.
A zatem:
a) Odpowiedź poprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.1.6
k-level: K1
points: 1
correct: b

## question
Co pokazuje model piramidy testów?

## answers
a) To, że testy mogą mieć różne priorytety.
b) To, że testy mogą mieć różną szczegółowość.
c) To, że testy mogą wymagać różnych kryteriów pokrycia.
d) To, że testy mogą być zależne od innych testów.

## justification
a) Odpowiedź niepoprawna. Model piramidy testów nie dostarcza informacji o priorytetach testów.
b) Odpowiedź poprawna. Model piramidy testów pokazuje, że różne testy mają różne poziomy szczegółowości.
c) Odpowiedź niepoprawna. Model piramidy testów jest niezależny od kryteriów pokrycia.
d) Odpowiedź niepoprawna. Model piramidy testów nie pokazuje żadnych relacji między różnymi testami.

---

# metadata
lo: FL-5.1.7
k-level: K2
points: 1
correct: d

## question
Jaki jest związek między kwadrantami testowymi, poziomami testów i typami testów?

## answers
a) Kwadranty testowe reprezentują określone kombinacje poziomów testów i typów testów, definiując ich umiejscowienie w cyklu wytwarzania oprogramowania.
b) Kwadranty testowe opisują stopień szczegółowości poszczególnych typów testów wykonywanych na każdym poziomie testów.
c) Kwadranty testowe przypisują typy testów, które można wykonać, do poziomów testów.
d) Kwadranty testowe grupują poziomy testów i typy testów według kilku kryteriów, takich jak ukierunkowanie na konkretnych interesariuszy.

## justification
a) Odpowiedź niepoprawna. Kwadranty testowe grupują poziomy testów i typy testów według kilku kryteriów. Nie reprezentują one żadnych kombinacji poziomów testów i typów testów i nie są powiązane z żadnym etapem cyklu życia oprogramowania. Zarówno poziomy testów, jak i typy testów są traktowane oddzielnie w modelu kwadrantów testowych.
b) Odpowiedź niepoprawna. Kwadranty testowe grupują poziomy testów i typy testów według kilku kryteriów. Nie opisują one stopnia szczegółowości poszczególnych typów testów wykonywanych na każdym poziomie testów. Taki model, odnoszący się do poziomów testów, nazywany jest piramidą testów.
c) Odpowiedź niepoprawna. Stwierdzenie jest błędne, ponieważ ogólnie rzecz biorąc, każdy typ testu może być wykonywany na każdym poziomie testów.
d) Odpowiedź poprawna. Kwadranty testowe grupują poziomy testów, typy testów, czynności testowe, techniki testowania i produkty pracy w zwinnym wytwarzaniu oprogramowania. W tym modelu testy mogą być ukierunkowane na biznes lub technologię. Testy mogą wspierać zespół (tj. kierować rozwojem) lub krytykować produkt (tj. mierzyć jego zachowanie w stosunku do oczekiwań). Połączenie tych dwóch punktów widzenia określa cztery kwadranty.

---

# metadata
lo: FL-5.2.3
k-level: K2
points: 1
correct: c

## question
Która z poniższych opcji stanowi przykład tego, jak analiza ryzyka produktowego może wpływać na dokładność i zakres testowania?

## answers
a) Ciągłe monitorowanie ryzyka pozwala szybko zidentyfikować pojawiające się ryzyko.
b) Identyfikacja ryzyka pozwala wdrożyć działania łagodzące i zmniejszyć poziom ryzyka.
c) Oceniony poziom ryzyka pomaga ustalić stopień rygorystyczności testów.
d) Analiza ryzyka pozwala określić elementy testowe, które należy objąć testowaniem.

## justification
a) Odpowiedź niepoprawna. Monitorowanie ryzyka jest częścią kontroli ryzyka, a nie analizy ryzyka.
b) Odpowiedź niepoprawna. Sama identyfikacja ryzyka nie pozwala nam wdrożyć działań łagodzących ryzyko. Działania te są wdrażane podczas fazy kontroli ryzyka.
c) Odpowiedź poprawna. Jest to przykład wpływu analizy ryzyka na dokładność i zakres testowania.
d) Odpowiedź niepoprawna. Elementy pokrycia są określane przy użyciu technik testowania, a nie poprzez analizę ryzyka.

---

# metadata
lo: FL-5.3.2
k-level: K2
points: 1
correct: b

## question
Która z poniższych czynności w procesie testowym w **największym** stopniu wykorzystuje raporty o postępie testów?

## answers
a) Projektowanie testów.
b) Ukończenie testów.
c) Analiza testów.
d) Planowanie testów.

## justification
a) Odpowiedź niepoprawna. Raporty o postępie testów są najczęściej wykorzystywane podczas monitorowania testów i nadzoru nad testami oraz po ich ukończeniu, a nie podczas projektowania testów.
b) Odpowiedź poprawna. Sumaryczny raport z testów jest przygotowywany po ukończeniu testów, gdy projekt, poziom testów lub typ testów został ukończony i, w idealnym przypadku, spełnione zostały kryteria wyjścia. Raport ten wykorzystuje informacje zawarte w raportach o postępie testów oraz inne dane.
c) Odpowiedź niepoprawna. Raporty o postępie testów są najczęściej wykorzystywane podczas monitorowania testów i nadzoru nad testami oraz ukończenia testów, a nie podczas analizy testów.
d) Odpowiedź niepoprawna. Raporty o postępie testów są najczęściej wykorzystywane podczas monitorowania testów i nadzoru nad testami oraz ukończenia testów, a nie podczas planowania testów.

---

# metadata
lo: FL-5.4.1
k-level: K2
points: 1
correct: d

## question
Które z poniższych **nie** jest przykładem tego, jak zarządzanie konfiguracją wspiera testowanie?

## answers
a) Wszystkie zatwierdzenia zmian (ang. *commit*) w repozytorium są jednoznacznie identyfikowane i podlegają kontroli wersji.
b) Wszystkie zmiany w elementach środowiska testowego są śledzone i zapisywane.
c) Wszystkie specyfikacje wymagań są jednoznacznie przywołane w planach testów.
d) Wszystkie zidentyfikowane defekty mają przypisany status.

## justification
a) Odpowiedź niepoprawna. Gdy użytkownik zgłasza awarię oprogramowania, dzięki unikalnej identyfikacji zatwierdzeń zmian (ang. *commit*) możliwe jest ponowne odtworzenie plików z wersji oprogramowania używanej przez użytkownika (a także odpowiednich wersji skryptów testowych), a tym samym odtworzenie awarii i szybsze zlokalizowanie defektu.
b) Odpowiedź niepoprawna. Jeśli zmiana w środowisku testowym powoduje nieoczekiwane problemy podczas testowania, zarządzanie konfiguracją pozwala testerom przywrócić poprzednią wersję środowiska. Dzięki temu testy mogą być kontynuowane bez wpływu zmiany na nie.
c) Odpowiedź niepoprawna. Zarządzanie konfiguracją zapewnia, że wszystkie zidentyfikowane dokumenty (np. specyfikacje wymagań) i elementy oprogramowania są jednoznacznie przywołane w dokumentacji testowej (np. w planach testów).
d) Odpowiedź poprawna. Zapewnia to proces zarządzania defektami, a nie proces zarządzania konfiguracją.

---

# metadata
lo: FL-5.5.1
k-level: K3
points: 1
correct: b

## question
Rozważ poniższy raport o defekcie dla internetowej aplikacji zakupowej.

> Aplikacja: WebShop v0.99
>
> Usterka: Przycisk logowania nie działa
>
> Kroki umożliwiające odtworzenie awarii:
>
> 1. Uruchom stronę internetową
> 2. Kliknij przycisk logowania
>
> Oczekiwany wynik: użytkownik powinien zostać przekierowany do strony logowania.
>
> Rzeczywisty wynik: przycisk logowania nie reaguje po kliknięciu.
>
> Krytyczność: Wysoka
>
> Priorytet: Pilny

Jaka jest **najważniejsza** informacja, której brakuje w tym raporcie o defekcie?

## answers
a) Imię i nazwisko testera oraz data raportu.
b) Elementy środowiska testowego i numery ich wersji.
c) Identyfikacja przedmiotu testów.
d) Wpływ defektu na interesariuszy.

## justification
a) Odpowiedź niepoprawna. Jest to ważne, ale nie tak ważne jak elementy środowiska testowego.
b) Odpowiedź poprawna. Brakuje jednak ważnej informacji, jaką jest identyfikacja przeglądarki i urządzenia użytego do testowania. Informacje o przeglądarce i urządzeniu są ważne, ponieważ taka usterka może być specyficzna dla danej przeglądarki lub urządzenia. Na przykład przycisk logowania może działać poprawnie w jednej przeglądarce (lub jednej wersji konkretnej przeglądarki), ale nie w innej. Dlatego informacje o przeglądarce i urządzeniu mogą pomóc programistom w odtworzeniu problemu i szybszym znalezieniu jego przyczyny.
c) Odpowiedź niepoprawna. Przedmiot testów jest zidentyfikowany (WebShop v0.99).
d) Odpowiedź niepoprawna. Uwzględniono wpływ -- jest to krytyczność (wysoka).

---

# metadata
lo: FL-6.1.1
k-level: K2
points: 1
correct: d

## question
Które z poniższych narzędzi pomagają w organizacji przypadków testowych, wykrytych defektów i zarządzaniu konfiguracją?

## answers
a) Narzędzia do wykonywania testów i obliczania pokrycia.
b) Narzędzia do projektowania i implementacji testów.
c) Narzędzia do zarządzania defektami.
d) Narzędzia do zarządzania testami.

## justification
a) Odpowiedź niepoprawna. Narzędzia do wykonywania testów i pomiaru pokrycia ułatwiają automatyczne wykonywanie przypadków testowych oraz pomiar pokrycia osiągniętego poprzez uruchomienie tych przypadków testowych. Jednak narzędzia te nie pomagają w organizacji defektów i zarządzaniu konfiguracją.
b) Odpowiedź niepoprawna. Narzędzia do projektowania i implementacji testów ułatwiają generowanie przypadków testowych, danych testowych i procedur testowych, ale nie pomagają w organizacji defektów i zarządzaniu konfiguracją.
c) Odpowiedź niepoprawna. Narzędzia do zarządzania defektami służą do zarządzania defektami, ale nie są narzędziami testowymi i nie są używane do organizowania przypadków testowych ani zarządzania konfiguracją.
d) Odpowiedź poprawna. Narzędzia do zarządzania testami zwiększają wydajność procesu testowego, ułatwiając zarządzanie cyklem życia oprogramowania, wymaganiami, testami, defektami i konfiguracją.

---

# metadata
lo: FL-6.2.1
k-level: K1
points: 1
correct: d

## question
Które z poniższych jest **największą** zaletą automatyzacji testów?

## answers
a) Możliwość generowania przypadków testowych bez dostępu do podstawy testów.
b) Osiągnięcie większego pokrycia dzięki bardziej obiektywnej ocenie.
c) Wydłużenie czasu wykonywania testów dzięki większej mocy obliczeniowej.
d) Zapobieganie błędom ludzkim dzięki większej spójności i powtarzalności.

## justification
a) Odpowiedź niepoprawna. „Możliwość generowania przypadków testowych bez dostępu do podstawy testów” nie jest zaletą automatyzacji testów (jest to niemożliwe). Generowanie przypadków testowych przez testerów lub narzędzia wymaga dostępu do podstawy testów.
b) Odpowiedź niepoprawna. „Osiągnięcie większego pokrycia dzięki bardziej obiektywnej ocenie” nie jest bezpośrednią korzyścią wynikającą z automatyzacji testów. Automatyzacja testów zapewni bardziej obiektywną ocenę pokrycia, jednak ta obiektywna ocena nie zwiększy pokrycia. Tylko wykorzystanie wyników pokrycia do napisania dalszych przypadków testowych może potencjalnie zwiększyć pokrycie.
c) Odpowiedź niepoprawna. „Wydłużenie czasu wykonywania testów dzięki większej mocy obliczeniowej” jest stwierdzeniem sprzecznym, ponieważ większa moc obliczeniowa zazwyczaj skraca czas wykonywania, a wydłużenie czasu wykonywania nie jest korzyścią, ponieważ testowanie trwałoby dłużej.
d) Odpowiedź poprawna. „Zapobieganie błędom ludzkim dzięki większej spójności i powtarzalności” jest korzyścią wynikającą z automatyzacji testów, ponieważ automatyzacja testów nie jest narażona na błędy ludzkie. Oznacza to na przykład, że testy są konsekwentnie opracowywane na podstawie wymagań, dane testowe są tworzone w sposób systematyczny, a testy są wykonywane przez narzędzie w tej samej kolejności, w ten sam sposób i z tą samą częstotliwością.
