# metadata
lo: FL-1.1.1
k-level: K1
points: 1
correct: d

## question
Które z poniższych jest typowym celem testu?

## answers
a) Wykrywanie i usuwanie defektów w przedmiocie testów.  
b) Utrzymanie skutecznej komunikacji z programistami.  
c) Walidacja, czy spełnione zostały wymagania prawne.  
d) Budowanie zaufania do jakości przedmiotu testów.

## justification
a) Odpowiedź niepoprawna. Wykrywanie i usuwanie defektów w przedmiocie testów nie jest typowym celem testów, ponieważ -- chociaż identyfikacja defektów jest celem testów -- usuwanie defektów nie jest czynnością testową.  
b) Odpowiedź niepoprawna. Utrzymywanie skutecznej komunikacji z programistami nie jest typowym celem testów, ponieważ -- chociaż jest to przydatne w osiąganiu innych celów testów, takich jak dostarczanie interesariuszom informacji umożliwiających im podejmowanie świadomych decyzji -- nie jest to główny powód przeprowadzania testów.  
c) Odpowiedź niepoprawna. Walidacja zgodności z wymaganiami prawnymi nie jest typowym celem testów, ponieważ walidacja polega na sprawdzeniu, czy system spełnia potrzeby użytkowników i innych interesariuszy w swoim środowisku operacyjnym. Sprawdzanie zgodności z wymaganiami prawnymi jest formą weryfikacji, a nie walidacji.  
d) Odpowiedź poprawna. Budowanie zaufania do jakości przedmiotu testów osiąga się poprzez wykonywanie testów, które zakończyły się zaliczeniem.

---

# metadata
lo: FL-1.2.3
k-level: K2
points: 1
correct: c

## question
Zmęczony projektant dokumentuje projekt interfejsu użytkownika, który nie jest odpowiednio dostosowany do potrzeb użytkowników niepełnosprawnych. Programista implementuje go zgodnie z projektem, ale ponieważ pracuje pod ogromną presją czasu, nie uwzględnia w kodzie obsługi wyjątku dotyczącego obliczania premii. Podczas korzystania z systemu niektórzy użytkownicy niepełnosprawni zgłaszają reklamacje dotyczące interfejsu, a firma zostaje następnie ukarana grzywną przez odpowiedni organ regulacyjny. Nikt nie zauważa, że obliczenia premii są czasami niepoprawne.
Które z poniższych stwierdzeń jest poprawne?

## answers
a) Błędne obliczenie premii jest defektem, który pojawia się sporadycznie.
b) Grzywna nałożona za nieuwzględnienie potrzeb niepełnosprawnych użytkowników jest awarią.
c) Programista pracujący pod ogromną presją czasu jest podstawową przyczyną.
d) Projekt interfejsu użytkownika zawiera błąd projektanta.

## justification
a) Odpowiedź niepoprawna. Błędne obliczenie premii jest awarią systemu, a nie defektem.
b) Odpowiedź niepoprawna. Brak zapewnienia odpowiedniego wsparcia dla użytkowników niepełnosprawnych jest awarią, która ostatecznie skutkuje nałożeniem grzywny, ale sama grzywna nie jest awarią.
c) Odpowiedź poprawna. Błąd popełnił programista, a przyczyną tego błędu jest praca pod ogromną presją czasu, która jest podstawową przyczyną późniejszego defektu.
d) Odpowiedź niepoprawna. Niewłaściwa konstrukcja interfejsu użytkownika, który nie jest odpowiednio dostosowany do potrzeb użytkowników niepełnosprawnych, jest defektem architektury spowodowanym błędem architekta. Zatem konstrukcja interfejsu użytkownika zawiera defekt, a nie błąd (projektanta).

---

# metadata
lo: FL-1.3.1
k-level: K2
points: 1
correct: a

## question
Warunki testowe są wykorzystywane przez testerów do generowania przypadków testowych i wykonywania testów. Mimo że warunki testowe pozostają niezmienne, przypadki testowe są za każdym razem różne. Która z poniższych zasad testowania dotyczy zróżnicowania przypadków testowych?

## answers
a) Testy się zużywają.
b) Przekonanie o braku defektów jest błędem.
c) Wczesne testowanie oszczędza czas i pieniądze.
d) Defekty mogą się kumulować.

## justification
a) Odpowiedź poprawna. Zasada „testy ulegają zużyciu" dotyczy przekonania, że powtarzanie identycznych testów na niezmienionym kodzie prawdopodobnie nie pozwoli wykryć nowych defektów, dlatego niezbędna może być modyfikacja testów. Dzięki wykorzystaniu warunków testowych do generowania nowych testów za każdym razem, testy nie będą identyczne, a ryzyko ich zużycia zostanie zmniejszone.
b) Odpowiedź niepoprawna. Zasada „przekonanie o braku defektów jest błędem" dotyczy zapewnienia, że potrzeby użytkowników są zaspokajane, nawet jeśli przeprowadzono wiele testów i nie znaleziono żadnych defektów (tj. konieczna jest również walidacja).
c) Odpowiedź niepoprawna. Zasada „wczesne testowanie oszczędza czas i pieniądze" dotyczy wczesnego usuwania defektów, aby zapobiec pojawieniu się kolejnych defektów w pochodnych produktach pracy, zmniejszając w ten sposób koszty i prawdopodobieństwo awarii.
d) Odpowiedź niepoprawna. Zasada „defekty mogą się kumulować" dotyczy rozkładu defektów w systemie, który zazwyczaj jest zgodny z rozkładem Pareto.

---

# metadata
lo: FL-1.4.1
k-level: K2
points: 1
correct: b

## question
Rozważ zadania testowe (1--4) oraz czynności testowe (A--D):
1. Wyprowadź przypadki testowe na podstawie warunków testowych.
2. Zidentyfikuj testalia wielokrotnego użytku.
3. Zorganizuj przypadki testowe w procedury testowe.
4. Oceń podstawę testów i przedmiot testów.

A. Analiza testów.
B. Projektowanie testów.
C. Implementacja testów.
D. Ukończenie testów.

Która z poniższych opcji **najlepiej** dopasowuje zadania do czynności?

## answers
a) 1B, 2A, 3D, 4C.
b) 1B, 2D, 3C, 4A.
c) 1C, 2A, 3B, 4D.
d) 1C, 2D, 3A, 4B.

## justification
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna. Poprawne dopasowanie to: 1B, 2D, 3C, 4A.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-1.4.3
k-level: K2
points: 1
correct: a

## question
Rozważ następujące testalia:
i. Sumaryczny raport z testów.
ii. Dane w bazie danych używane jako dane wejściowe i oczekiwane wyniki.
iii. Lista elementów potrzebnych do zbudowania środowiska testowego.
iv. Udokumentowane sekwencje przypadków testowych w kolejności wykonania.
v. Przypadki testowe.

Które z nich **najlepiej** ukazują testalia powstałe jako wynik fazy implementacji testów?

## answers
a) ii, iv.
b) iii, v.
c) i, ii, v.
d) i, iii, iv.

## justification
a) Odpowiedź poprawna. Pozycje ii oraz iv na liście są wynikiem implementacji testów.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-1.4.5
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń **najlepiej** opisuje zadanie wykonywane przez osobę pełniącą funkcję kierownika testów?

## answers
a) Ocena podstawy testów i przedmiotu testów.
b) Określenie wymagań dotyczących środowiska testowego.
c) Ocena testowalności przedmiotu testów.
d) Sporządzenie raportu z ukończenia testów.

## justification
a) Odpowiedź niepoprawna. Osoba pełniąca rolę związaną z testowaniem odpowiada przede wszystkim za techniczne i inżynieryjne aspekty testowania, takie jak analiza testów, projektowanie testów, implementacja testów i wykonywanie testów. Ocena podstawy testów pod kątem defektów i przedmiotu testów pod kątem testowalności to zadania wykonywane w ramach analizy testów, więc prawdopodobnie są to zadania wykonywane przez osobę pełniącą rolę związaną z testowaniem.
b) Odpowiedź niepoprawna. Osoba pełniąca rolę związaną z testowaniem odpowiada przede wszystkim za techniczne i inżynieryjne aspekty testowania, takie jak analiza testów, projektowanie testów, implementacja testów i wykonywanie testów. Definiowanie wymagań środowiska testowego jest zadaniem wykonywanym w ramach projektowania testów, więc prawdopodobnie jest to zadanie wykonywane przez osobę pełniącą rolę związaną z testowaniem.
c) Odpowiedź niepoprawna. Osoba pełniąca rolę związaną z testowaniem jest przede wszystkim odpowiedzialna za techniczne i inżynieryjne aspekty testowania, takie jak analiza testów, projektowanie testów, implementacja testów i wykonywanie testów. Ocena testowalności przedmiotu testów jest zadaniem wykonywanym w ramach analizy testów, więc prawdopodobnie jest to zadanie wykonywane przez osobę pełniącą rolę związaną z testowaniem.
d) Odpowiedź poprawna. Rola związana z zarządzaniem testami obejmuje przede wszystkim czynności związane z planowaniem testów, monitorowaniem testów i nadzorem nad testami oraz ukończeniem testów. Dlatego też tworzenie sumarycznego raportu z testów, który jest głównym wynikiem działania związanego z ukończeniem testów, jest prawdopodobnie zadaniem wykonywanym przez rolę związaną z zarządzaniem testami.

---

# metadata
lo: FL-1.5.2
k-level: K1
points: 1
correct: a

## question
Która z poniższych opcji stanowi zaletę podejścia „cały zespół”?

## answers
a) Lepsza komunikacja między członkami zespołu.
b) Zmniejszona indywidualna odpowiedzialność za jakość.
c) Szybsze dostarczanie produktów końcowych użytkownikom końcowym.
d) Ograniczona współpraca z zewnętrznymi użytkownikami biznesowymi.

## justification
a) Odpowiedź poprawna. Podejście „cały zespół” sprzyja intensywnej komunikacji i współpracy między członkami zespołu.
b) Odpowiedź niepoprawna. Chociaż podejście „cały zespół” priorytetowo traktuje zbiorową odpowiedzialność za jakość, każdy członek zespołu jest nadal w równym stopniu odpowiedzialny za jakość.
c) Odpowiedź niepoprawna. Podejście „cały zespół” dotyczy sposobu współpracy zespołu w celu uzyskania produktów o wyższej jakości, ale niekoniecznie skutkuje szybszym wdrożeniem dla użytkowników końcowych.
d) Odpowiedź niepoprawna. Stosując podejście „cały zespół”, testerzy współpracują z przedstawicielami jednostek biznesowych w celu stworzenia testów akceptacyjnych. Nie ma żadnych przesłanek sugerujących, że podejście to ograniczy współpracę z zewnętrznymi użytkownikami biznesowymi.

---

# metadata
lo: FL-1.5.3
k-level: K2
points: 1
correct: b

## question
Biorąc pod uwagę następujące wady i zalety niezależności testowania:

i. Testerzy pracują w innym miejscu niż programiści.
ii. Testerzy kwestionują założenia programistów podczas pisania kodu.
iii. Między testerami a programistami powstała konfrontacyjna atmosfera.
iv. Programiści są przekonani, że to testerzy ponoszą główną odpowiedzialność za jakość.
v. Testerzy mają inne uprzedzenia poznawcze niż programiści.

Które z poniższych są **największymi** **korzyściami** z niezależności testowania?

## answers
a) i, iv.
b) ii, v.
c) i, iii, iv.
d) ii, iii, v.

## justification
Biorąc pod uwagę wszystkie wymienione zalety i wady niezależności testowania:
i. Idealnie byłoby, gdyby testerzy i programiści ściśle ze sobą współpracowali, a izolacja nie sprzyja takiej współpracy. Jest to zatem wada.
ii. Testerzy i programiści mają różne doświadczenia, punkty widzenia i potencjalne uprzedzenia poznawcze, co pozwala testerom efektywnie kwestionować założenia poczynione przez interesariuszy podczas specyfikacji i implementacji systemu. Jest to zatem zaleta.
iii. Główną wadą niezależności testowania jest to, że testerzy mogą zostać odizolowani od zespołu programistów, co prowadzi do problemów z komunikacją, braku współpracy i potencjalnie antagonistycznych relacji, w których testerzy są obwiniani za opóźnienia i bycie wąskim gardłem w procesie wydawania nowych wersji. Jest to zatem wada.
iv. Jedną z wad niezależności testowania jest to, że testerzy mogą zostać odizolowani od zespołu programistów, co prowadzi do tego, że programiści czują się mniej odpowiedzialni za jakość. Jest to zatem wada.
v. Główną zaletą niezależności testowania jest to, że testerzy są bardziej skłonni do identyfikowania różnych rodzajów awarii i defektów w porównaniu z programistami, ze względu na swoje zróżnicowane doświadczenie, techniczny punkt widzenia i potencjalne uprzedzenia, w tym uprzedzenia poznawcze.

Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna. Pozycje na liście wskazujące zalety to ii oraz v.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-2.1.2
k-level: K1
points: 1
correct: a

## question
Która z poniższych opcji stanowi dobrą praktykę testowania, która ma zastosowanie we wszystkich modelach cyklu wytwarzania oprogramowania?

## answers
a) Każdy poziom testów ma określone i odrębne cele testów.
b) Implementacja i wykonanie testów dla danego poziomu testów powinno rozpocząć się w odpowiadającej mu fazie wytwórczej.
c) Testerzy powinni rozpocząć projektowanie testów, gdy tylko dostępne będą wstępne projekty odpowiednich produktów pracy.
d) Każda czynność testowania dynamicznego ma odpowiadającą jej czynność testowania statycznego.

## justification
a) Odpowiedź poprawna. Każdy poziom testów ma określone i odrębne cele testów, ponieważ na każdym poziomie testów sprawdzany jest inny przedmiot testów (np. pojedynczy moduł, kompletny system), a nakładające się cele testów prowadziłyby do niepotrzebnego powielania.
b) Odpowiedź niepoprawna. Analiza i projektowanie testów dla danego poziomu testów powinny rozpocząć się podczas odpowiedniej fazy wytwórczej, aby ułatwić wczesne testowanie (np. analiza i projektowanie testów akceptacyjnych powinny rozpocząć się podczas analizy wymagań). Implementacja testów rozpocznie się zazwyczaj później, a wykonywanie testów rozpocznie się podczas danego poziomu testów.
c) Odpowiedź niepoprawna. Projektowanie testów dla danego poziomu testów powinno rozpocząć się podczas odpowiedniej fazy wytwórczej, aby ułatwić wczesne testowanie, jednak projekt testów (np. generowanie przypadków testowych) musi opierać się na uzgodnionej podstawie testów, a nie na wstępnej wersji projektu, w przeciwnym razie znaczny wysiłek związany z testowaniem może zostać zmarnowany na tworzenie przypadków testowych dla projektu, który później ulegnie zmianie.
d) Odpowiedź niepoprawna. Kontrola jakości dotyczy wszystkich czynności związanych z wytwarzaniem, co oznacza, że każda czynność związana z wytwarzaniem oprogramowania ma odpowiadającą jej czynność testową. Jednak ta sama symetria nie ma zastosowania do testowania dynamicznego i statycznego. Istnieją pewne czynności związane z testowaniem statycznym (np. analiza statyczna), dla których nie ma oczywistego odpowiednika w postaci czynności związanej z testowaniem dynamicznym.

---

# metadata
lo: FL-2.1.3
k-level: K1
points: 1
correct: a

## question
Która z poniższych opcji jest przykładem podejścia „najpierw test”?

## answers
a) Wytwarzanie sterowane zachowaniem.
b) Wytwarzanie sterowane poziomami testów.
c) Wytwarzanie sterowane funkcjami.
d) Wytwarzanie sterowane wydajnością.

## justification
a) Odpowiedź poprawna. Wytwarzanie sterowane zachowaniem (BDD) jest dobrze znanym przykładem podejścia „najpierw test”.
b) Odpowiedź niepoprawna. Wytwarzanie sterowane poziomami testów nie jest poprawnym przykładem podejścia „najpierw test”.
c) Odpowiedź niepoprawna. Wytwarzanie sterowane funkcjami (FDD) nie jest poprawnym przykładem podejścia „najpierw test”.
d) Odpowiedź niepoprawna. Wytwarzanie sterowane wydajnością nie jest poprawnym przykładem podejścia „najpierw test”.

---

# metadata
lo: FL-2.1.4
k-level: K2
points: 1
correct: d

## question
Która z poniższych opcji jest **największym** wyzwaniem napotykanym podczas wdrażania DevOps?

## answers
a) Upewnienie się, że niefunkcjonalne charakterystyki jakościowe nie zostaną pominięte w testach.
b) Zarządzanie stale zmieniającymi się środowiskami testowymi.
c) Potrzeba zatrudnienia większej liczby testerów manualnych z odpowiednim doświadczeniem.
d) Skonfigurowanie automatyzacji testów jako części potoku dostarczania oprogramowania.

## justification
a) Odpowiedź niepoprawna. DevOps generalnie zwiększa widoczność niefunkcjonalnych charakterystyk jakościowych, takich jak wydajność i niezawodność.
b) Odpowiedź niepoprawna. Zautomatyzowane procesy, takie jak ciągła integracja/ciągłe dostarczanie (CI/CD), stosowane w DevOps, ułatwiają tworzenie stabilnych środowisk testowych.
c) Odpowiedź niepoprawna. Zautomatyzowane procesy, takie jak CI/CD stosowane w DevOps, zazwyczaj zmniejszają potrzebę testowania manualnego.
d) Odpowiedź poprawna. Wdrożenie DevOps może wiązać się z kilkoma ryzykami i wyzwaniami, w tym koniecznością zdefiniowania i skonfigurowania potoku dostarczania, wprowadzenia i utrzymania narzędzi CI/CD oraz ustanowienia i utrzymania automatyzacji testów.

---

# metadata
lo: FL-2.1.6
k-level: K2
points: 1
correct: b

## question
Które z poniższych stwierdzeń **najlepiej** opisuje retrospektywy?

## answers
a) Retrospektywy pozwalają członkom zespołu zidentyfikować innych członków zespołu, którzy nie w pełni przyczynili się do osiągnięcia jakości wymaganej w ramach podejścia „cały zespół”.
b) Retrospektywy dają testerom możliwość zidentyfikowania czynności, które zakończyły się sukcesem, tak aby można je było zachować podczas wprowadzania potencjalnych udoskonaleń w przyszłości.
c) Retrospektywy to miejsce, w którym członkowie zwinnego zespołu mogą wyrażać swoje obawy dotyczące zarządzania i klientów w środowisku wolnym od obwiniania.
d) Retrospektywy stanowią dla członków zwinnego zespołu forum, na którym mogą skupić się na omówieniu planu i decyzji technicznych dotyczących kolejnej iteracji.

## justification
a) Odpowiedź niepoprawna. Korzyści płynące z retrospektyw obejmują budowanie więzi w zespole i uczenie się poprzez dzielenie się problemami oraz lepszą współpracę między programistami i testerami poprzez przeglądanie i doskonalenie praktyk. Wskazywanie osób, które zdaniem członka zespołu nie przyczyniły się w pełni do osiągnięcia jakości wymaganej przez podejście „cały zespół”, nie przyczyni się do budowania więzi w zespole i współpracy.
b) Odpowiedź poprawna. Podczas retrospektywy grupa omawia, które aspekty projektu zakończyły się sukcesem i powinny zostać zachowane, które obszary można udoskonalić, oraz sposoby, w jakie można to zrobić.
c) Odpowiedź niepoprawna. Korzyści płynące z retrospektyw opierają się na zwiększonej skuteczności i wydajności dzięki udoskonalaniu procesów; nie są one okazją do wyładowania emocji i krytykowania kierownictwa i klientów. Ponadto wyniki są zazwyczaj zapisywane w sumarycznym raporcie z testów, więc wszystko, co zostało powiedziane podczas spotkania, może zostać przeczytane przez innych interesariuszy.
d) Odpowiedź niepoprawna. Retrospektywy to spotkania, które zazwyczaj odbywają się pod koniec iteracji, podczas których członkowie zespołu skupiają się na omówieniu kwestii związanych z jakością, które pojawiły się w bieżącej iteracji. Nie służą one do tworzenia planów ani podejmowania decyzji technicznych dotyczących następnej iteracji; odbywa się to podczas planowania iteracji na początku następnej iteracji.

---

# metadata
lo: FL-2.2.2
k-level: K2
points: 1
correct: a

## question
Który z poniższych testów z **największym** prawdopodobieństwem zostanie wykonany w ramach testów funkcjonalnych?

## answers
a) Sprawdzenie, czy funkcja sortowania umieszcza elementy listy lub tablicy w porządku rosnącym.
b) Sprawdzenie, czy funkcja sortowania kończy działanie w ciągu sekundy od rozpoczęcia.
c) Sprawdzenie, jak łatwo można zmienić funkcję sortowania z rosnącego na malejące.
d) Sprawdzenie, czy funkcja sortowania nadal działa poprawnie po przeniesieniu z architektury 32-bitowej do 64-bitowej.

## justification
a) Odpowiedź poprawna. Sprawdzenie, czy funkcja sortowania umieszcza elementy listy lub tablicy w porządku rosnącym, stanowi ocenę poprawności funkcjonalnej funkcji sortowania, co jest częścią testowania funkcjonalnego.
b) Odpowiedź niepoprawna. Ocena, czy funkcja sortowania spełnia wymagania niefunkcjonalne dotyczące zakończenia działania w ciągu jednej sekundy, stanowi część testowania wydajności, które jest częścią testowania niefunkcjonalnego.
c) Odpowiedź niepoprawna. Ocena łatwości modyfikacji funkcji sortowania z porządkowania rosnącego na porządkowanie malejące stanowi testowanie jej modyfikowalności, co jest formą testowania niefunkcjonalnej utrzymywalności, będącą częścią testowania niefunkcjonalnego.
d) Odpowiedź niepoprawna. Ocena, czy funkcja sortowania nadal działa poprawnie po przeniesieniu z architektury 32-bitowej do 64-bitowej, stanowi testowanie jej adaptowalności, czyli formę testowania przenaszalności, która jest częścią testowania niefunkcjonalnego.

---

# metadata
lo: FL-2.3.1
k-level: K2
points: 1
correct: b

## question
Która z poniższych opcji jest **najbardziej** prawdopodobnym wyzwalaczem testowania pielęgnacyjnego systemu wymiany walut?

## answers
a) Programiści zgłosili, że zmiana systemu wymiany walut jest trudna, a testerzy postanowili sprawdzić, czy to prawda.
b) Opcja zwrotu kosztów w systemie wymiany walut została usunięta, ponieważ nie zawsze zwracała klientom prawidłową kwotę.
c) Zespół zwinny rozpoczął opracowywanie historyjki użytkownika, która dodaje nową funkcję lojalnościową dla klientów do systemu wymiany walut.
d) Opcja obsługi języków w systemie wymiany walut została wykorzystana do umożliwienia transakcji walutowych zarówno w języku angielskim, jak i lokalnym.

## justification
a) Odpowiedź niepoprawna. Zakładając, że testerzy mogliby sprawdzić łatwość zmiany systemu wymiany walut, odbywałoby się to poprzez testowanie utrzymywalności, a nie testowanie pielęgnacyjne, więc nie jest to czynnik wyzwalający testowanie pielęgnacyjne.
b) Odpowiedź poprawna. Modyfikacja systemu (np. poprawka lub ulepszenie) jest przykładem czynnika wyzwalającego testowanie pielęgnacyjne. Usunięcie opcji zwrotu kosztów z systemu wymiany walut było poprawką, która doprowadziłaby do testowania pielęgnacyjnego.
c) Odpowiedź niepoprawna. Jeśli zespół zwinny rozpoczął opracowywanie historyjki użytkownika, która dodaje nową funkcję lojalnościową dla klientów systemu wymiany walut, powoduje to przetestowanie nowej funkcji, a następnie przeprowadzenie testów regresji. W tej sytuacji nie są wymagane testy pielęgnacyjne.
d) Odpowiedź niepoprawna. Rekonfiguracja systemu wymiany walut w celu obsługi transakcji walutowych zarówno w języku lokalnym, jak i angielskim, nie jest modyfikacją systemu, zmianą środowiska operacyjnego ani wycofaniem systemu, które są trzema czynnikami wyzwalającymi testy pielęgnacyjne.

---

# metadata
lo: FL-3.1.1
k-level: K1
points: 1
correct: c

## question
Który z poniższych produktów pracy **nie** **może** być zbadany za pomocą testowania statycznego?

## answers
a) Umowa z klientem.
b) Plan testów.
c) Zaszyfrowany kod.
d) Karta opisu testów.

## justification
a) Odpowiedź niepoprawna. Większość produktów pracy można zbadać za pomocą pewnej formy testowania statycznego, a umowa musi być zrozumiała dla ludzi, a zatem może być poddana przeglądowi, co jest formą testowania statycznego.
b) Odpowiedź niepoprawna. Większość produktów pracy można zbadać za pomocą pewnej formy testowania statycznego, a plan testów musi być zrozumiały dla ludzi, a zatem może być poddany przeglądowi, co stanowi formę testowania statycznego.
c) Odpowiedź poprawna. Większość produktów pracy można zbadać za pomocą pewnej formy testowania statycznego; nie jest to jednak odpowiednie w przypadku produktów pracy, które są zbyt złożone, aby mogły być interpretowane przez ludzi, i nie powinny być analizowane za pomocą narzędzi, a zaszyfrowany kod jest zbyt złożony dla ludzi i jeśli jest prawidłowo zaszyfrowany, nie będzie można go analizować za pomocą większości narzędzi.
d) Odpowiedź niepoprawna. Większość produktów pracy można zbadać za pomocą pewnej formy testowania statycznego, a karta opisu testu musi być zrozumiała dla ludzi, aby można ją było poddać przeglądowi, co stanowi formę testowania statycznego.

---

# metadata
lo: FL-3.1.2
k-level: K2
points: 1
correct: c

## question
Które z poniższych stwierdzeń dotyczących wartości testowania statycznego jest **poprawne**?

## answers
a) Rodzaje defektów wykryte podczas testowania statycznego różnią się od rodzajów defektów, które można wykryć podczas testowania dynamicznego.
b) Testowanie dynamiczne może wykryć rodzaje defektów wykrywalne podczas testowania statycznego oraz dodatkowo jeszcze inne rodzaje defektów.
c) Testowanie dynamiczne może wykryć niektóre defekty wykrywalne podczas testowania statycznego, ale nie wszystkie.
d) Testowanie statyczne może wykryć rodzaje defektów wykrywalne podczas testowania dynamicznego oraz dodatkowo jeszcze inne rodzaje defektów.

## justification
Niektóre typy defektów, które można wykryć wyłącznie za pomocą testowania statycznego, to niedostępny kod, błędnie użyte wzorce projektowe oraz defekty w produktach pracy, które nie są wykonywalne. Niektóre typy defektów, które można wykryć zarówno za pomocą testowania statycznego, jak i dynamicznego, to defekty programistyczne, które mogą zostać zauważone przez przeglądającego podczas przeglądu kodu i które powodują zauważalne awarie podczas testowania dynamicznego. Niektóre rodzaje defektów można wykryć wyłącznie za pomocą testowania dynamicznego, np. problemy z wydajnością lub pamięcią, które można zaobserwować wyłącznie podczas wykonywania kodu lub systemu. Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-3.2.2
k-level: K2
points: 1
correct: b

## question
Rozważ poniższe opisy czynności związanych z przeglądami:

1. Wykryte anomalie są rozpatrywane i podejmowane są decyzje dotyczące ich statusu, odpowiedzialności oraz wszelkich dalszych niezbędnych działań.
2. Defekty są rejestrowane, a wszelkie niezbędne aktualizacje są wprowadzane przed akceptacją produktu pracy.
3. Przeglądający stosują techniki pozwalające na sformułowanie sugestii i pytań dotyczących produktu pracy oraz wykrycie anomalii.
4. W celu zapewnienia ukierunkowanego i efektywnego przeglądu definiowany jest cel przeglądu i jego harmonogram.
5. Uczestnicy otrzymują dostęp do elementu poddawanego przeglądowi.

Która z poniższych sekwencji działań jest **poprawna** w ramach procesu przeglądu?

## answers
a) 4 -- 3 -- 5 -- 2 -- 1.
b) 4 -- 5 -- 3 -- 1 -- 2.
c) 5 -- 4 -- 1 -- 3 -- 2.
d) 5 -- 4 -- 3 -- 2 -- 1.

## justification
Poniżej przedstawiono pięć opisów i odpowiadające im czynności w ramach procesu przeglądu:
1. Opisuje część czynności „przekazanie informacji i analiza”.
2. Opisuje część czynności „usunięcie defektów i raportowanie”.
3. Opisuje część czynności „przegląd indywidualny”.
4. Opisuje część czynności „planowanie”.
5. Opisuje część czynności „rozpoczęcie przeglądu”.

Ogólny proces przeglądu wg normy ISO/IEC 20246, który został opisany w sylabusie, obejmuje następujące czynności w następującej kolejności:

- Planowanie (4).
- Rozpoczęcie przeglądu (5).
- Przegląd indywidualny (3).
- Przekazanie informacji i analiza (1).
- Usunięcie defektów i raportowanie (2).

W związku z tym:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna. Prawidłowa kolejność czynności to: 4 -- 5 -- 3 -- 1 -- 2.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-3.2.3
k-level: K1
points: 1
correct: b

## question
Która rola w przeglądzie jest odpowiedzialna za zapewnienie sprawnego przebiegu spotkań przeglądowych i umożliwienie wszystkim uczestnikom swobodnego wyrażania opinii?

## answers
a) Kierownik.
b) Moderator.
c) Przewodniczący.
d) Lider przeglądu.

## justification
a) Odpowiedź niepoprawna. Kierownik jest odpowiedzialny za podjęcie decyzji, co należy poddać przeglądowi, oraz za przydzielenie zasobów, takich jak personel i czas, na przeprowadzenie przeglądu.
b) Odpowiedź poprawna. Moderator (lub facylitator) jest odpowiedzialny za zapewnienie skutecznego przebiegu spotkań przeglądowych, w tym zarządzanie czasem, mediację podczas dyskusji i tworzenie bezpiecznego środowiska, w którym każdy może swobodnie wyrażać swoje opinie.
c) Odpowiedź niepoprawna. Przewodniczący nie jest rolą w przeglądach.
d) Odpowiedź niepoprawna. Lider przeglądu jest odpowiedzialny za nadzorowanie procesu przeglądu, np. wybór członków zespołu przeglądowego, planowanie spotkań przeglądowych i zapewnienie pomyślnego zakończenia przeglądu.

---

# metadata
lo: FL-4.1.1
k-level: K2
points: 1
correct: b

## question
Przeprowadzasz testy systemowe aplikacji internetowej do handlu elektronicznego. Otrzymujesz następujące wymaganie: *REQ 05-017. Jeśli łączny koszt zakupów przekroczy 100 $, klient otrzymuje 5% zniżki na kolejne zakupy. W przeciwnym razie klient nie otrzymuje zniżki.*
Które techniki testowania będą **najbardziej** pomocne w projektowaniu przypadków testowych w oparciu o to wymaganie?

## answers
a) Białoskrzynkowe techniki testowania.
b) Czarnoskrzynkowe techniki testowania.
c) Techniki testowania oparte na doświadczeniu.
d) Techniki testowania oparte na ryzyku.

## justification
a) Odpowiedź niepoprawna. Dokument nie odnosi się do wewnętrznej struktury przedmiotu testów, ale określa jego pożądane zachowanie. Dlatego białoskrzynkowe techniki testowania nie będą pomocne w projektowaniu przypadków testowych.
b) Odpowiedź poprawna. Dokument jest wymaganiem, które określa pożądane zachowanie przedmiotu testów. Dlatego najbardziej odpowiednimi technikami testowania w tym przypadku są czarnoskrzynkowe techniki testowania (np. analiza wartości brzegowych lub testowanie w oparciu o tablicę decyzyjną).
c) Odpowiedź niepoprawna. Chociaż techniki testowania oparte na doświadczeniu mogą być wykorzystane do projektowania przypadków testowych w oparciu o ten dokument, bardziej odpowiednie będą czarnoskrzynkowe techniki testowania. Dokument opisuje precyzyjną regułę biznesową, a sformułowania typu „jeśli... przekroczy 100 $” sugerują istnienie ważnych wartości brzegowych klas równoważności, które powinny być testowane przy użyciu czarnoskrzynkowych technik testowania, takich jak analiza wartości brzegowych.
d) Odpowiedź niepoprawna. Techniki testowania oparte na ryzyku nie są uznanym typem technik testowania.

---

# metadata
lo: FL-4.2.1
k-level: K3
points: 1
correct: b, e

## question
System sprzedaży biletów do kina oblicza rodzaj zniżki na podstawie roku urodzenia klienta (RU) i bieżącego roku (BR) w następujący sposób. Niech D = BR -- RU.

- Jeśli D < 0, wyświetl komunikat „rok urodzenia nie może być większy niż bieżący”.
- Jeśli 0 ≤ D < 18, zastosuj zniżkę studencką.
- Jeśli 18 ≤ D < 65, nie stosuj zniżki.
- Jeśli D ≥ 65, zastosuj zniżkę dla emerytów.

Twój zestaw testowy zawiera już dwa przypadki testowe:

- RU = 1990, BR = 2020, oczekiwany wynik: brak zniżki
- RU = 2030, BR = 2029, oczekiwany wynik: wyświetlenie komunikatu o błędzie

Które **dwa** z poniższych zestawów danych testowych należy dodać do już istniejących, aby uzyskać pełne pokrycie klas równoważności dla dziedziny wyjściowej (rodzaj zniżki)?

## answers
a) RU = 2001, BR = 2065.
b) RU = 1900, BR = 1965.
c) RU = 1965, BR = 1900.
d) RU = 2011, BR = 2029.
e) RU = 2000, BR = 2000.

## justification
Istniejące dwa przypadki testowe pokrywają dwie klasy równoważności: „nie stosuj zniżki” (D = 2020 -- 1990 = 30) oraz „wyświetl komunikat 'rok urodzenia nie może być większy niż bieżący'” (D = 2029 -- 2030 = -1).
Istnieją więc dwie klasy równoważności, które nie zostały jeszcze pokryte, odpowiadające „zniżce studenckiej” (gdy 0 ≤ D < 18) i „zniżce dla emerytów” (gdy D ≥ 65). Zatem:
a) Odpowiedź niepoprawna. BR -- RU = 64, więc te dane wejściowe pokrywają już pokrytą klasę równoważności „nie stosuj zniżki”.
b) Odpowiedź poprawna. BR -- RU = 65, więc te dane wejściowe pokrywają klasę równoważności, która nie została jeszcze pokryta („zniżka dla emerytów”).
c) Odpowiedź niepoprawna. BR -- RU = -65, więc te dane wejściowe pokrywają już uwzględnioną klasę równoważności dotyczącą komunikatu o błędzie.
d) Odpowiedź niepoprawna. BR -- RU = 18, więc te dane wejściowe pokrywają już uwzględnioną klasę równoważności „nie stosuj zniżki”.
e) Odpowiedź poprawna. BR -- RU = 0, więc te dane wejściowe pokrywają klasę równoważności, która nie została jeszcze uwzględniona („zniżka studencka”).

---

# metadata
lo: FL-4.2.2
k-level: K3
points: 1
correct: c

## question
Testujesz system kontroli temperatury w chłodni ogrodniczej. System otrzymuje temperaturę (w pełnych stopniach Celsjusza) jako dane wejściowe. Jeśli temperatura wynosi od 0 do 2 stopni włącznie, system wyświetla komunikat „temperatura OK”. W przypadku niższych temperatur system wyświetla komunikat „temperatura zbyt niska”, a w przypadku wyższych temperatur wyświetla komunikat „temperatura zbyt wysoka”.
Korzystając z analizy wartości brzegowych w wersji dwupunktowej, który z poniższych zestawów danych wejściowych zapewnia **najwyższy** poziom pokrycia wartości brzegowych?

## answers
a) -1, 3.
b) 0, 2.
c) -1, 0, 2, 3.
d) -2, 0, 2, 4.

## justification
Istnieją trzy klasy równoważności: {..., -2, -1}, {0, 1, 2}, {3, 4, ...}. W przypadku dwupunktowej analizy wartości brzegowych wszystkie wartości brzegowe dla wszystkich klas równoważności muszą być pokryte. Wartości brzegowe to -1 (dla klasy równoważności „temperatura zbyt niska”), 0 i 2 (dla klasy równoważności „temperatura OK”) i 3 (dla klasy równoważności „temperatura zbyt wysoka”).
Zatem:
a) Odpowiedź niepoprawna. Ten zestaw danych wejściowych osiągnie 50% pokrycia.
b) Odpowiedź niepoprawna. Ten zestaw danych wejściowych osiągnie 50% pokrycia.
c) Odpowiedź poprawna. Ten zestaw danych wejściowych pokrywa wszystkie wartości brzegowe wszystkich klas równoważności, więc osiągnie 100% pokrycia.
d) Odpowiedź niepoprawna. Ten zestaw danych wejściowych osiągnie 50% pokrycia; wartości -2 i 4 nie są elementami pokrycia.

---

# metadata
lo: FL-4.2.3
k-level: K3
points: 1
correct: a

## question
Projektujesz przypadki testowe na podstawie poniższej tablicy decyzyjnej.

| | **R1** | **R2** | **R3** | **R4** | **R5** | **R6** | **R7** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| C1: Wiek | 0--18 | 19--65 | 19--65 | >65 | 0--18 | 19--65 | >65 |
| C2: Doświadczenie | -- | 0--4 | >4 | -- | -- | -- | -- |
| C3: Zarejestrowany? | NIE | NIE | NIE | NIE | TAK | TAK | TAK |
| Kategoria | A | A | B | B | B | D | C |

Do tej pory udało ci się zaprojektować następujące przypadki testowe:

- TC1: 19-letni, niezarejestrowany mężczyzna bez doświadczenia; oczekiwany wynik: A
- TC2: 65-letnia, niezarejestrowana kobieta z 5-letnim doświadczeniem; oczekiwany wynik: B
- TC3: 66-letni, zarejestrowany mężczyzna bez doświadczenia; oczekiwany wynik: C
- TC4: 65-letnia, zarejestrowana kobieta z 4-letnim doświadczeniem; oczekiwany wynik: D

Który z poniższych przypadków testowych, dodany do istniejącego zestawu przypadków testowych, zwiększy pokrycie tablicy decyzyjnej?

## answers
a) 66-letni, niezarejestrowany mężczyzna bez doświadczenia; oczekiwany wynik: B.
b) 55-letnia, niezarejestrowana kobieta z 2-letnim doświadczeniem; oczekiwany wynik: A.
c) 19-letnia, zarejestrowana kobieta z 5-letnim doświadczeniem; oczekiwany wynik: D.
d) Żadne dodatkowe przypadki testowe nie mogą zwiększyć już osiągniętego pokrycia tablicy decyzyjnej.

## justification
Przypadki testowe TC1, TC2, TC3 i TC4 pokrywają odpowiednio reguły R2, R3, R7 i R6 w tablicy decyzyjnej. Zatem:
a) Odpowiedź poprawna. Warunki „66 lat”, „niezarejestrowany” i „brak doświadczenia” odpowiadają regule R4, która nie jest pokryta istniejącymi przypadkami testowymi, więc po dodaniu tego przypadku testowego pokrycie tablicy decyzyjnej wzrośnie.
b) Odpowiedź niepoprawna. Warunki „55 lat”, „niezarejestrowany” i „2 lata doświadczenia” odpowiadają regule R2, która jest już pokryta przypadkiem testowym TC1. Dodanie tego przypadku testowego nie zwiększy więc pokrycia.
c) Odpowiedź niepoprawna. Warunki „19 lat”, „zarejestrowany” i „5 lat doświadczenia” odpowiadają regule R6, która jest już pokryta przypadkiem testowym TC4. Dodanie tego przypadku testowego nie zwiększy więc pokrycia.
d) Odpowiedź niepoprawna. Istniejące przypadki testowe pokrywają tylko 4 z 7 kolumn tablicy decyzyjnej. Pokrycie można zwiększyć przez dodanie przypadków testowych pokrywających kolumny, które nie zostały jeszcze uwzględnione, czyli R1, R4 i R5.

---

# metadata
lo: FL-4.2.4
k-level: K3
points: 1
correct: b

## question
Stosujesz testowanie przejść pomiędzy stanami systemu rezerwacji pokoi hotelowych, modelowanego przez poniższą tablicę stanów, zawierającą 4 stany i 5 różnych zdarzeń:

| **Stan** | **Dostępny** | **Niedostępny** | **Zmień pokój** | **Anuluj** | **Zapłać** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| S1: Żądanie | S2 | S3 | | | |
| S2: Potwierdzanie | | | S1 | S4 | S4 |
| S3: Oczekujący | S2 | | | S4 | |
| S4: Koniec | | | | | |

Zakładając, że wszystkie przypadki testowe rozpoczynają się w stanie „Żądanie”, który z poniższych przypadków testowych, przedstawionych jako sekwencja zdarzeń, osiąga **najwyższy** poziom pokrycia przejść poprawnych?

## answers
a) Niedostępny, Dostępny, Zmień pokój, Niedostępny, Anuluj.
b) Dostępny, Zmień pokój, Niedostępny, Dostępny, Zapłać.
c) Dostępny, Zmień pokój, Dostępny, Zmień pokój, Niedostępny.
d) Niedostępny, Anuluj, Zmień pokój, Dostępny, Zapłać.

## justification
a) Odpowiedź niepoprawna. Ta sekwencja pięciu zdarzeń pokrywa 4 różne przejścia poprawne (oba zdarzenia „Niedostępny” odpowiadają temu samemu przejściu między S1 a S3). Ten przypadek testowy pokrywa więc 4 z 7 przejść poprawnych.
b) Odpowiedź poprawna. Ta sekwencja pięciu zdarzeń obejmuje 5 różnych przejść poprawnych (pierwsze zdarzenie „Dostępny” odpowiada przejściu między S1 a S2, a drugie zdarzenie „Dostępny” odpowiada przejściu między S3 a S2, więc pokryte są dwa różne przejścia). Ten przypadek testowy pokrywa 5 z 7 przejść poprawnych i osiąga najwyższy poziom pokrycia przejść poprawnych spośród wszystkich opcji.
c) Odpowiedź niepoprawna. Ta sekwencja pięciu zdarzeń obejmuje 3 różne przejścia poprawne (oba zdarzenia „Dostępny” odpowiadają temu samemu przejściu z S1 do S2; oba zdarzenia „Zmień pokój” odpowiadają temu samemu przejściu z S2 do S1). Ten przypadek testowy pokrywa więc 3 z 7 przejść poprawnych.
d) Odpowiedź niepoprawna. Ta sekwencja pięciu zdarzeń nie stanowi wykonalnego przypadku testowego, ponieważ po zdarzeniu „Anuluj” system kończy swoje działanie i nie można wykonać żadnych dalszych przejść poprawnych.

---

# metadata
lo: FL-4.3.1
k-level: K2
points: 1
correct: c

## question
Twój zestaw testowy Z dla programu P osiąga 100% pokrycia instrukcji. Zestaw składa się z trzech przypadków testowych, z których każdy osiąga 50% pokrycia instrukcji.
Które z poniższych stwierdzeń jest **poprawne**?

## answers
a) Wykonanie Z spowoduje wszystkie możliwe awarie w P.
b) Z osiąga 100% pokrycia gałęzi dla P.
c) Każda instrukcja wykonywalna w P zawierająca defekt została uruchomiona co najmniej raz podczas wykonywania Z.
d) Po usunięciu jednego przypadku testowego z zestawu Z pozostałe dwa przypadki testowe nadal będą osiągać 100% pokrycia instrukcji.

## justification
a) Odpowiedź niepoprawna. Instrukcja z defektem po wykonaniu nie musi powodować awarii. Na przykład linia x := y / z spowoduje awarię *tylko* wtedy, gdy z jest równe 0.
b) Odpowiedź niepoprawna. 100% pokrycia instrukcji nie gwarantuje 100% pokrycia gałęzi. Na przykład przypadek testowy z wejściem x = 0 dla kodu

```
1. IF (x == 0) THEN
2.   A;
3. ENDIF
```

osiąga 100% pokrycia instrukcji, ale nie pokrywa gałęzi 1 -> 3.
c) Odpowiedź poprawna. 100% pokrycia instrukcji oznacza, że każda instrukcja wykonywalna została wykonana co najmniej raz.
d) Odpowiedź niepoprawna. Usunięty przypadek testowy może zapewnić pokrycie niektórych instrukcji, które nie są pokryte przez żaden z pozostałych dwóch przypadków testowych, w którym to przypadku pozostałe dwa przypadki testowe razem nie osiągną 100% pokrycia instrukcji.

---

# metadata
lo: FL-4.3.3
k-level: K2
points: 1
correct: a

## question
Dlaczego testowanie białoskrzynkowe ułatwia wykrywanie defektów, nawet jeśli specyfikacja oprogramowania jest niejasna, nieaktualna lub niekompletna?

## answers
a) W testowaniu białoskrzynkowym przypadki testowe są projektowane w oparciu o strukturę przedmiotu testów, a nie specyfikację.
b) W przypadku każdej białoskrzynkowej techniki testowania pokrycie można dobrze zdefiniować i łatwo zmierzyć.
c) Białoskrzynkowe techniki testowania są bardzo dobrze zaprojektowane, aby wykrywać pominięcia w wymaganiach.
d) Białoskrzynkowe techniki testowania mogą być stosowane zarówno w testowaniu statycznym, jak i dynamicznym.

## justification
a) Odpowiedź poprawna. Podstawową zaletą wszystkich białoskrzynkowych technik testowania jest to, że podczas testowania brana jest pod uwagę cała implementacja oprogramowania, co ułatwia wykrywanie defektów nawet wtedy, gdy specyfikacja oprogramowania jest niejasna, nieaktualna lub niekompletna. Oznacza to, że testowanie białoskrzynkowe pozwala wykryć defekty, takie jak dodatkowa funkcja dodana do kodu (przypadkowo lub celowo), która nie powinna się tam znajdować, a której testowanie czarnoskrzynkowe nie jest w stanie wykryć.
b) Odpowiedź niepoprawna. Fakt, że pokrycie można precyzyjnie zdefiniować, nie jest właściwym powodem. Osiągnięty poziom pokrycia miałby znacznie większy wpływ niż sama możliwość pomiaru pokrycia.
c) Odpowiedź niepoprawna. Jeśli oprogramowanie nie spełnia jednego lub więcej wymagań, testowanie białoskrzynkowe prawdopodobnie nie wykryje wynikających z tego defektów pominięcia.
d) Odpowiedź niepoprawna. Chociaż jest to prawda, nie jest to właściwa odpowiedź, ponieważ nie ma związku między możliwością wykorzystania technik białoskrzynkowych zarówno w testowaniu statycznym, jak i dynamicznym, a twierdzeniem, że testowanie białoskrzynkowe ułatwia wykrywanie defektów przy problematycznych specyfikacjach.

---

# metadata
lo: FL-4.4.1
k-level: K2
points: 1
correct: c

## question
Które z poniższych **nie** **jest** przewidziane przez testera podczas stosowania zgadywania błędów?

## answers
a) Programista źle zrozumiał wzór na obliczanie odsetek zawarty w historyjce użytkownika.
b) Programista napisał w kodzie źródłowym „FA = A*(1+IR^N)” zamiast „FA = A*(1+IR)^N”.
c) Programista opuścił szkolenie dotyczące nowych przepisów dotyczących procentu składanego.
d) Dokładność odsetek obliczonych przez system nie jest wystarczająca.

## justification
Zgadywanie błędów polega na przewidywaniu błędów, defektów i awarii w oparciu o wiedzę testera. Zatem:
a) Odpowiedź niepoprawna. Jest to przykład przewidywania błędu programisty.
b) Odpowiedź niepoprawna. Jest to przykład przewidywania defektu.
c) Odpowiedź poprawna. Jest to przykład potencjalnej podstawowej przyczyny defektu, która nie jest ani błędem, ani defektem, ani awarią i jest trudna do przewidzenia przez testera.
d) Odpowiedź niepoprawna. Jest to przykład przewidywania awarii, być może w oparciu o doświadczenia z testowania poprzednich systemów w tej dziedzinie biznesowej.

---

# metadata
lo: FL-4.4.2
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń dotyczących testowania eksploracyjnego jest **prawdziwe**?

## answers
a) Przypadki testowe są projektowane przed rozpoczęciem sesji testów eksploracyjnych.
b) Tester może wykonywać testy, ale nie może ich projektować.
c) Wyniki testów eksploracyjnych są dobrym wskaźnikiem liczby pozostałych defektów.
d) Podczas testowania eksploracyjnego tester może stosować techniki czarnoskrzynkowe.

## justification
a) Odpowiedź niepoprawna. W testowaniu eksploracyjnym przypadki testowe są zazwyczaj tworzone „dynamicznie” podczas sesji testowania eksploracyjnego, równolegle z analizą testów, implementacją testów i wykonywaniem testów.
b) Odpowiedź niepoprawna. W testowaniu eksploracyjnym testy są jednocześnie projektowane, wykonywane i oceniane, podczas gdy tester poznaje przedmiot testów.
c) Odpowiedź niepoprawna. Wyniki testowania eksploracyjnego w dużym stopniu zależą od doświadczenia testera, więc nawet jeśli wyniki testowania eksploracyjnego mogą służyć jako wskaźnik ryzyka i być wykorzystywane do oceny, czy będzie mniej lub więcej defektów w porównaniu z poprzednią sesją testowania eksploracyjnego, nie są one dobrym przykładem wiarygodnych modeli przewidywania defektów, które mogą przewidzieć liczbę pozostałych defektów.
d) Odpowiedź poprawna. Podczas testowania eksploracyjnego testerzy mogą stosować dowolne techniki, które uznają za przydatne.

---

# metadata
lo: FL-4.5.1
k-level: K2
points: 1
correct: d

## question
Która z praktyk wspólnego pisania historyjek użytkownika pozwala zespołowi osiągnąć wspólne zrozumienie tego, co należy dostarczyć?

## answers
a) Poker planistyczny, dzięki czemu zespół może osiągnąć konsensus co do nakładu pracy niezbędnego do implementacji historyjki użytkownika.
b) Przeglądy, dzięki którym zespół może wykryć niespójności i sprzeczności w historyjce użytkownika.
c) Planowanie iteracji, aby historyjki użytkownika o najwyższej wartości biznesowej dla klienta mogły zostać potraktowane priorytetowo podczas implementacji.
d) Rozmowa, dzięki której członkowie zespołu mogą zrozumieć, w jaki sposób oprogramowanie będzie wykorzystywane.

## justification
a) Odpowiedź niepoprawna. Poker planistyczny pozwala oszacować nakład pracy dla już napisanej historyjki użytkownika. Nie pomaga on w zrozumieniu, co powinno zostać dostarczone.
b) Odpowiedź niepoprawna. Przeglądy nie są praktyką wspólnego pisania historyjek użytkownika.
c) Odpowiedź niepoprawna. Planowanie iteracji jest praktyką związaną z projektem, służącą do planowania pracy, a nie do zrozumienia, co należy dostarczyć.
d) Odpowiedź poprawna. Rozmowa (ang. *conversation*) wyjaśnia, w jaki sposób oprogramowanie będzie wykorzystywane, i często pozwala zespołowi zdefiniować sensowne kryteria akceptacji, uzyskując w ten sposób wspólną wizję tego, co powinno zostać dostarczone.

---

# metadata
lo: FL-4.5.3
k-level: K3
points: 1
correct: a

## question
Zaczynasz projektować przypadki testowe dla poniższej historyjki użytkownika.

*Jako klient chcę mieć możliwość filtrowania wyników wyszukiwania według przedziału cenowego, aby łatwiej znaleźć produkty mieszczące się w moim budżecie.*

Kryteria akceptacji:

1. Filtr powinien działać we wszystkich wersjach aplikacji od wersji 3.0 w górę.
2. Filtr powinien umożliwiać ustawienie przedziału cenowego z ceną minimalną i maksymalną.
3. Wyniki wyszukiwania powinny być aktualizowane dynamicznie w miarę dostosowywania przez klienta filtra zakresu cenowego.

We wszystkich przypadkach testowych warunek wstępny jest następujący: dostępne są tylko dwa produkty, produkt A i produkt B. Produkt A kosztuje 100 $, a produkt B kosztuje 110 $.
Który z poniższych przykładów jest **najlepszym** przykładem przypadku testowego dla tej historyjki użytkownika?

## answers
a) Wejdź na stronę internetową i ustaw filtr, aby wyświetlać ceny od 90 do 100 $. Oczekiwany wynik: wyniki pokazują tylko produkt A. Ustaw maksymalną cenę na 110 $. Oczekiwany wynik: wyniki obejmują teraz zarówno produkt A, jak i B.
b) Wejdź na stronę internetową. Oczekiwany wynik: domyślne ceny min i max wynoszą odpowiednio 100 $ i 110 $. Dodaj produkt C do magazynu, z ceną 120 $. Odśwież stronę internetową klienta. Oczekiwany wynik: domyślna cena maksymalna zmienia się na 120 $.
c) Wejdź na stronę internetową i ustaw filtr, aby wyświetlać ceny od 90 do 115 $. Oczekiwany wynik: wyniki pokazują zarówno produkt A, jak i B. Zmień walutę z $ na EUR. Oczekiwany wynik: zakres filtra zmienia się poprawnie na wartości w EUR, zgodnie z aktualnym kursem wymiany.
d) Wejdź na stronę za pomocą trzech różnych przeglądarek: Edge, Chrome i Opera. W każdej przeglądarce ustaw filtr między 90 a 110 $. Oczekiwany wynik: wyniki obejmują zarówno produkt A, jak i B, a układ wyników jest taki sam we wszystkich przeglądarkach.

## justification
a) Odpowiedź poprawna. Ten przypadek testowy jest powiązany z kryteriami akceptacji 2 i 3, ponieważ sprawdzamy, czy możemy ustawić zakres cen (kryterium akceptacji 2) i czy wyniki aktualizują się dynamicznie po dostosowaniu filtra zakresu cen (kryterium akceptacji 3).
b) Odpowiedź niepoprawna. Ten przypadek testowy nie jest powiązany z żadnym z kryteriów akceptacji. Sprawdza on, czy filtr dynamicznie ustawia domyślny minimalny i maksymalny zakres cenowy, a nie to, czy klient może to zrobić.
c) Odpowiedź niepoprawna. Ten przypadek testowy nie jest powiązany z żadnym z kryteriów akceptacji. Sprawdza on funkcję wymiany walut, która nie jest omawiana w tej historyjce użytkownika.
d) Odpowiedź niepoprawna. Ten przypadek testowy nie jest powiązany z żadnym z kryteriów akceptacji. Sprawdza on kompatybilność aplikacji z różnymi przeglądarkami, co nie jest omawiane w tej historyjce użytkownika.

---

# metadata
lo: FL-5.1.3
k-level: K2
points: 1
correct: b, d

## question
Które **dwa** z poniższych stwierdzeń **najlepiej** definiują kryteria **wyjścia** w projekcie testowym?

## answers
a) Budżet został zatwierdzony.
b) Wyczerpanie budżetu.
c) Podstawa testów jest dostępna.
d) Przypadki testowe osiągnęły co najmniej 80% pokrycia instrukcji.
e) Wszyscy analitycy testów posiadają certyfikat ISTQB® na poziomie podstawowym.

## justification
a) Odpowiedź niepoprawna. Zatwierdzenie budżetu jest przykładem kryterium wejścia. Nie miałoby sensu zatwierdzanie budżetu na działanie, które zostało już zrealizowane.
b) Odpowiedź poprawna. Wyczerpanie budżetu można uznać za ważne kryterium wyjścia.
c) Odpowiedź niepoprawna. Dostępność zasobów jest przykładem kryterium wejścia do testowania.
d) Odpowiedź poprawna. Pokrycie jest miarą dokładności, więc jest to typowe kryterium wyjścia.
e) Odpowiedź niepoprawna. Jest to przykład kryterium wejścia, sprawdzanego przed rozpoczęciem projektu.

---

# metadata
lo: FL-5.1.4
k-level: K3
points: 1
correct: a

## question
Zespół chce oszacować czas potrzebny jednemu testerowi na wykonanie czterech przypadków testowych dla modułu oprogramowania. Zespół zebrał następujące miary dotyczące nakładu pracy potrzebnego do wykonania jednego przypadku testowego:

- Optymistyczny scenariusz: 1 godzina.
- Pesymistyczny scenariusz: 8 godzin.
- Najbardziej prawdopodobny scenariusz: 3 godziny.

Biorąc pod uwagę, że stosowana jest technika szacowania trójpunktowego, jaka jest ostateczna szacowana liczba godzin potrzebnych do wykonania wszystkich czterech przypadków testowych?

## answers
a) 14 godzin.
b) 3,5 godziny.
c) 16 godzin.
d) 12 godzin.

## justification
Stosując technikę szacowania trójpunktowego, ostateczną wartość szacunkową (E) oblicza się jako $E = (a + 4 \cdot m + b) / 6$, gdzie *a* jest oszacowaniem optymistycznym, *m* jest najbardziej prawdopodobnym, a *b* pesymistycznym.
Zatem:
a) Odpowiedź poprawna. W tym przypadku oszacowanie wykonania pojedynczego przypadku testowego wynosi: $E = (1h + 4 \cdot 3h + 8h) / 6 = 3,5$ godziny. Zatem całkowity czas potrzebny testerowi do wykonania 4 przypadków testowych wynosi 3,5h * 4 = 14 godzin.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.1.5
k-level: K3
points: 1
correct: b

## question
Przygotowujesz harmonogram wykonania siedmiu przypadków testowych TC 1 do TC 7. Tablica przedstawia macierz śledzenia przypadków testowych do wymagań (Req1 -- Req7). „X” oznacza, że dany przypadek testowy pokrywa odpowiednie wymaganie.

| | **Req1** | **Req2** | **Req3** | **Req4** | **Req5** | **Req6** | **Req7** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| TC1 | X | | X | X | | | X |
| TC2 | | X | | | | | |
| TC3 | | | | | X | X | |
| TC4 | | X | | | | | |

Chcesz nadać priorytety przypadkom testowym stosując technikę dodatkowego pokrycia. Wszystkie cztery przypadki testowe muszą zostać wykonane.
Który przypadek testowy należy wykonać jako **ostatni**?

## answers
a) TC1.
b) TC2.
c) TC3.
d) TC4.

## justification
TC1 osiąga najwyższe pokrycie (4/7, pokrywając Req1, Req3, Req4 i Req7), więc powinien być wykonany jako pierwszy. Req2, Req5 i Req6 nadal nie są pokryte. Kolejnym przypadkiem testowym, który osiągnie najwyższe dodatkowe pokrycie pozostałych wymagań jest więc TC3, pokrywający 2 z tych 3 wymagań (Req5 i Req6). Zatem TC3 powinien zostać wykonany jako drugi. Teraz jedynym wymaganiem, które nadal nie zostało pokryte, jest Req2, które jest pokryte przez TC4. Dlatego TC4 powinien zostać wykonany jako trzeci przypadek testowy. Ostatnim wykonanym przypadkiem testowym będzie więc TC2.
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.1.7
k-level: K2
points: 1
correct: c

## question
W jaki sposób kwadranty testowe mogą być pomocne w testowaniu?

## answers
a) Pomagają w planowaniu testów poprzez podział procesu testowania na cztery etapy, odpowiadające czterem podstawowym poziomom testów: modułowemu, integracyjnemu, systemowemu i akceptacyjnemu.
b) Pomagają w ocenie wysokopoziomowego pokrycia (np. pokrycia wymagań) w oparciu o niskopoziomowe pokrycie (np. pokrycie kodu).
c) Pomagają one osobom nieposiadającym wiedzy technicznej zrozumieć różne typy testów oraz fakt, że niektóre typy testów są bardziej odpowiednie dla niektórych poziomów testów niż inne.
d) Pomagają zespołom zwinnym w opracowaniu strategii komunikacyjnej opartej na klasyfikacji osób według czterech podstawowych typów psychologicznych oraz na modelowaniu relacji między nimi.

## justification
a) Odpowiedź niepoprawna. Kwadranty testowe nie mają nic wspólnego z opisywaniem relacji między poziomami testów.
b) Odpowiedź niepoprawna. Kwadranty testowe nie mogą pomóc w ocenie żadnego rodzaju pokrycia.
c) Odpowiedź poprawna. Kwadranty testowe pozwalają menedżerom i innym interesariuszom zrozumieć relacje między typami testów, czynnościami, które wspierają (wsparcie zespołu lub krytyka produktu) oraz punktem widzenia, na którym się koncentrują (biznesowym lub technologicznym).
d) Odpowiedź niepoprawna. Kwadranty testowe nie są modelem psychologicznym.

---

# metadata
lo: FL-5.2.1
k-level: K1
points: 1
correct: b

## question
Dla danego ryzyka poziom ryzyka wynosi 1000 $, a prawdopodobieństwo wystąpienia ryzyka szacuje się na 50%.
Jaki jest wpływ tego ryzyka?

## answers
a) 500 $.
b) 2000 $.
c) 50 000 $.
d) 200 $.

## justification
Ocena ryzyka może opierać się na podejściu ilościowym lub jakościowym albo na połączeniu obu tych podejść. W podejściu ilościowym poziom ryzyka oblicza się jako iloczyn prawdopodobieństwa wystąpienia ryzyka i wpływu ryzyka. Zatem poziom ryzyka = prawdopodobieństwo wystąpienia ryzyka x wpływ ryzyka. Wówczas wpływ ryzyka = poziom ryzyka / prawdopodobieństwo wystąpienia ryzyka.
W naszym przypadku wpływ ryzyka = 1000 $ / 50% = 1000 $ / 0,5 = 2000 $.
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.2.2
k-level: K2
points: 1
correct: b, e

## question
Które **dwa** z poniższych ryzyk są ryzykami produktowymi?

## answers
a) Rozszerzenie zakresu projektu.
b) Architektura niskiej jakości.
c) Cięcia kosztów.
d) Słabe wsparcie narzędziowe.
e) Zbyt długi czas reakcji systemu.

## justification
a) Odpowiedź niepoprawna. Rozszerzenie zakresu projektu jest przykładem ryzyka projektowego związanego z kwestiami technicznymi.
b) Odpowiedź poprawna. Niskiej jakości architektura jest przykładem ryzyka produktowego, ponieważ odnosi się do cechy produktu.
c) Odpowiedź niepoprawna. Cięcia kosztów są przykładem ryzyka projektowego związanego z kwestiami organizacyjnymi.
d) Odpowiedź niepoprawna. Słabe wsparcie narzędziowe jest przykładem ryzyka projektowego związanego z kwestiami technicznymi.
e) Odpowiedź poprawna. Zbyt długi czas reakcji jest przykładem ryzyka produktowego, ponieważ odnosi się do charakterystyki produktu.

---

# metadata
lo: FL-5.3.2
k-level: K2
points: 1
correct: c

## question
Które z poniższych **nie** jest prawidłowym celem raportu z testów?

## answers
a) Śledzenie postępów testów i identyfikowanie obszarów wymagających dalszej uwagi.
b) Dostarczanie informacji na temat przeprowadzonych testów, ich wyników oraz wszelkich wykrytych problemów lub defektów.
c) Dostarczanie informacji o każdym defekcie, takich jak kroki niezbędne do jego odtworzenia.
d) Dostarczanie informacji na temat testów planowanych na następny okres.

## justification
a) Odpowiedź niepoprawna. Śledzenie postępów testów i identyfikowanie obszarów wymagających dalszej uwagi jest przykładem wspierania bieżącego nadzoru nad testami. Jest to jeden z celów raportów z testów.
b) Odpowiedź niepoprawna. Dostarczanie informacji na temat przeprowadzonych testów, ich wyników oraz wszelkich defektów jest przykładem podsumowania czynności testowych przeprowadzonych na danym poziomie testów. Jest to jeden z celów raportów z testów.
c) Odpowiedź poprawna. Dostarczanie informacji o defektach jest celem raportu o defekcie, a nie raportu z testów.
d) Odpowiedź niepoprawna. Dostarczanie informacji na temat testów zaplanowanych na następny okres jest jednym z celów raportów z testów (a dokładniej raportów o postępie testów).

---

# metadata
lo: FL-5.4.1
k-level: K2
points: 1
correct: d

## question
Użytkownik zgłosił awarię oprogramowania. Inżynier z zespołu wsparcia poprosił go o podanie numeru wersji oprogramowania, w którym zaobserwowano awarię. Na podstawie numeru wersji zespół odtworzył wszystkie pliki składające się na daną wersję. Pozwoliło to później programiście przeprowadzić analizę, znaleźć defekt i go usunąć.
Która z poniższych opcji umożliwiła zespołowi wykonanie powyższych czynności?

## answers
a) Zarządzanie ryzykiem.
b) Monitorowanie testów i nadzór nad testami.
c) Podejście „cały zespół”.
d) Zarządzanie konfiguracją.

## justification
a) Odpowiedź niepoprawna. Zarządzanie ryzykiem obejmuje analizę ryzyka i kontrolę ryzyka. Żadna z tych czynności nie wspiera ponownego odtworzenia plików, które tworzyły wydanie, ponieważ czynności te dotyczą ryzyka, a nie elementów konfiguracji.
b) Odpowiedź niepoprawna. Monitorowanie testów dotyczy gromadzenia informacji o testowaniu. Informacje te są wykorzystywane do oceny postępów testów i sprawdzania, czy spełnione są kryteria wyjścia z testów lub wykonane zostały zadania testowe związane z kryteriami wyjścia, takie jak osiągnięcie celów w zakresie pokrycia ryzyk produktowych, pokrycia wymagań lub innych kryteriów akceptacji. Nadzór nad testami wykorzystuje informacje uzyskane podczas monitorowania testów w celu zapewnienia, w formie dyrektyw nadzoru, wskazówek i niezbędnych działań korygujących, aby osiągnąć najbardziej efektywne i wydajne testowanie. Żadna z tych czynności nie dotyczy zarządzania elementami konfiguracji.
c) Odpowiedź niepoprawna. Podejście „cały zespół” opiera się na umiejętnościach testera efektywnej pracy zespołowej i pozytywnego przyczyniania się do osiągnięcia celów zespołu. Koncentruje się więc na kwestiach związanych z zespołem, a nie na elementach konfiguracji.
d) Odpowiedź poprawna. Zarządzanie konfiguracją zapewnia identyfikację, kontrolę i śledzenie produktów pracy. Zarządzanie konfiguracją przechowuje zapis zmienionych elementów konfiguracji po utworzeniu nowej konfiguracji bazowej (ang. *baseline*). Dzięki zarządzaniu konfiguracją możliwy jest powrót do poprzedniej konfiguracji bazowej np. w celu odtworzenia poprzednich wyników testów.

---

# metadata
lo: FL-5.5.1
k-level: K3
points: 1
correct: a

## question
Rozważ poniższy raport o defekcie w systemie wypożyczania książek.

> **Identyfikator usterki**: 001 **Tytuł**: Nie można zwrócić książki
>
> **Krytyczność**: Wysoka **Priorytet**:
>
> **Środowisko**: Windows 10, Google Chrome
>
> **Opis**: Podczas próby zwrotu książki za pomocą funkcji zwrotu książki system nie rejestruje zwrotu, a książka pozostaje wypożyczona użytkownikowi.
>
> **Kroki umożliwiające odtworzenie awarii**:
>
> 1. Zaloguj się do systemu wypożyczania książek jako użytkownik, który wypożyczył książkę.
> 2. Kliknij przycisk „Zwrot książki” dla książki, która została wypożyczona.
> 3. System nie rejestruje zwrotu, a książka pozostaje wypożyczona.
>
> **Oczekiwany wynik**: Książka powinna zostać zwrócona i nie być już wypożyczona użytkownikowi.
>
> **Rzeczywisty wynik**: Książka pozostaje wypożyczona użytkownikowi i nie jest zarejestrowana w systemie jako zwrócona.
>
> **Załączniki**: [pusta lista]

Które z poniższych działań **najprawdopodobniej** pomoże programiście szybko odtworzyć awarię?

## answers
a) Dodanie informacji o tym, których użytkowników i których książek dotyczy problem, do sekcji „Opis”.
b) Wypełnienie brakującej wartości w polu „Priorytet”.
c) Dodanie zrzutów pamięci i migawek bazy danych wykonanych po każdym kroku opisanym w sekcji „Kroki umożliwiające odtworzenie awarii” do sekcji „Załączniki”.
d) Powtórzenie tego samego przypadku testowego dla różnych środowisk i sporządzenie oddzielnych raportów o defekcie dla każdego z nich.

## justification
a) Odpowiedź poprawna. Dodanie tej informacji pozwala programiście na użycie tych samych danych wejściowych, dzięki czemu istnieje większe prawdopodobieństwo, że uda mu się szybko odtworzyć awarię i szybciej zidentyfikować defekt.
b) Odpowiedź niepoprawna. Dodanie wartości „Priorytet” nie pomoże w odtworzeniu samego defektu.
c) Odpowiedź niepoprawna. Chociaż niektóre z tych informacji mogą być wartościowe, dodawanie zrzutów pamięci i migawek bazy danych po każdym kroku będzie zbyt dużym obciążeniem, ponieważ większość tych artefaktów będzie zawierała informacje bezużyteczne dla programisty i sprawi, że raport o defekcie będzie mniej czytelny. Będzie to również wymagało od programisty poświęcenia dużej ilości czasu na analizę tych informacji, co wydłuży proces naprawy.
d) Odpowiedź niepoprawna. Pytanie dotyczyło pomocy programistom w odtworzeniu awarii zaobserwowanej w konkretnej konfiguracji środowiska.

---

# metadata
lo: FL-6.1.1
k-level: K2
points: 1
correct: b

## question
Rozważ następujące kategorie narzędzi testowych:

i. Narzędzia do współpracy.
ii. Narzędzia DevOps.
iii. Narzędzia do zarządzania.
iv. Narzędzia do testowania niefunkcjonalnego.
v. Narzędzia do projektowania i implementacji testów.

Które z tych kategorii narzędzi najprawdopodobniej ułatwią wykonywanie testów?

## answers
a) i, v.
b) ii, iv.
c) i, iii, v.
d) ii, iii, iv.

## justification
i. Narzędzia do komunikacji ułatwiają komunikację, a nie wykonywanie testów.
ii. Narzędzia DevOps wspierają potok dostarczania (ang. *delivery pipeline*), śledzenie przepływu pracy, procesy automatycznego tworzenia wersji oraz praktyki takie jak ciągła integracja/ciągłe dostarczanie, więc wspierają wykonywanie testów, takich jak testowanie modułów dla CI.
iii. Narzędzia do zarządzania zwiększają efektywność procesu zarządzania cyklem życia, wymaganiami, testami, defektami i konfiguracją. Zarządzanie tymi elementami nie wspiera bezpośrednio wykonywania testów.
iv. Narzędzia do testowania niefunkcjonalnego umożliwiają testerowi wykonywanie testów niefunkcjonalnych, które trudno jest wykonać manualnie lub ich manualne wykonanie jest niemożliwe. Testowanie niefunkcjonalne może zawierać w sobie zarówno testowanie statyczne, jak i dynamiczne, włączając w to wykonywanie testów.
v. Narzędzia do projektowania i implementacji testów wspierają projektowanie i implementację, a nie wykonywanie testów.

Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna. Zarówno narzędzia DevOps (ii), jak i narzędzia testowania niefunkcjonalnego (iv) wspierają wykonywanie testów.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-6.2.1
k-level: K1
points: 1
correct: c

## question
Która spośród poniższych opcji jest **największym** ryzykiem związanym z automatyzacją testów?

## answers
a) Wykrywanie dodatkowych defektów o wysokim stopniu krytyczności (ang. *severity*).
b) Zapewnienie miar, które są zbyt skomplikowane, aby ludzie mogli je obliczać.
c) Niezgodność z platformą programistyczną.
d) Znacznie skrócony czas wykonywania testów.

## justification
a) Odpowiedź niepoprawna. Wykrywanie dodatkowych defektów o wysokim stopniu krytyczności byłoby raczej korzyścią wynikającą z automatyzacji testów, a nie ryzykiem.
b) Odpowiedź niepoprawna. Obliczenie miar, które są zbyt skomplikowane, aby człowiek mógł je samodzielnie wyliczyć, jest zazwyczaj uważane za korzyść wynikającą z automatyzacji testów.
c) Odpowiedź poprawna. Jeśli automatyzacja testów jest niezgodna z platformą programistyczną, nie będzie można testów zintegrować i np. automatycznie przekazać danych wejściowych do przedmiotu testów oraz otrzymać wyników testów z przedmiotu testów.
d) Odpowiedź niepoprawna. Znaczne skrócenie czasu wykonywania testów byłoby zazwyczaj uważane za korzyść wynikającą z automatyzacji testów.
