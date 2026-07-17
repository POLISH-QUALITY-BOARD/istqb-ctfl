# metadata
lo: FL-1.1.1
k-level: K1
points: 1
correct: c

## question
Które z poniższych stwierdzeń opisuje poprawny cel testów?

## answers
a) Dowieść, że w testowanym systemie nie ma żadnych nieusuniętych defektów.  
b) Dowieść, że po wdrożeniu systemu do produkcji nie wystąpią żadne awarie.  
c) Zmniejszyć poziom ryzyka przedmiotu testów i zbudować zaufanie do poziomu jakości.  
d) Zweryfikować, że nie ma nieprzetestowanych kombinacji danych wejściowych.  

## justification
a) Odpowiedź niepoprawna. Nie można udowodnić, że w testowanym systemie nie ma już żadnych defektów (patrz zasada testowania nr 1).  
b) Odpowiedź niepoprawna. Patrz zasada testowania nr 7.  
c) Odpowiedź poprawna. Testowanie pozwala wykryć defekty i awarie, co zmniejsza poziom ryzyka, a jednocześnie zwiększa zaufanie do poziomu jakości przedmiotu testów.  
d) Odpowiedź niepoprawna. Niemożliwe jest przetestowanie wszystkich kombinacji danych wejściowych (patrz zasada testowania nr 2).  

---

# metadata
lo: FL-1.2.1
k-level: K2
points: 1
correct: a

## question
Która z poniższych opcji przedstawia przykład czynności testowych, które przyczyniają się do sukcesu projektu?

## answers
a) Zaangażowanie testerów w różne czynności w ramach cyklu życia oprogramowania pomoże wykryć defekty w produktach pracy.
b) Testerzy starają się nie przeszkadzać programistom podczas pisania kodu, aby programiści mogli pisać lepszy kod.
c) Testerzy współpracujący z użytkownikami końcowymi pomagają poprawić jakość raportów o defektach podczas integracji modułów i testowania systemowego.
d) Certyfikowani testerzy zaprojektują znacznie lepsze przypadki testowe niż testerzy niecertyfikowani.

## justification
a) Odpowiedź poprawna. Ważne jest, aby testerzy byli zaangażowani od samego początku cyklu wytwarzania oprogramowania. Zwiększy to zrozumienie decyzji projektowych i pozwoli na wczesne wykrycie defektów.
b) Odpowiedź niepoprawna. Zarówno programiści, jak i testerzy będą lepiej rozumieli swoje produkty pracy oraz sposób testowania kodu.
c) Odpowiedź niepoprawna. Użytkownicy końcowi nie pomogą testerom w poprawie jakości raportów o defektach; ponadto użytkownicy zazwyczaj nie uczestniczą w testowaniu niskopoziomowym, takim jak testowanie integracyjne.
d) Odpowiedź niepoprawna. Posiadanie certyfikatu nie oznacza automatycznie, że tester będzie lepszy w projektowaniu testów.

---

# metadata
lo: FL-1.3.1
k-level: K2
points: 1
correct: a

## question
Przydzielono Cię jako testera do zespołu tworzącego iteracyjnie nowy system. Zauważasz, że przez kilka iteracji nie wprowadzono żadnych zmian w istniejących przypadkach testowych regresji i nie zidentyfikowano żadnych nowych defektów regresji. Twój kierownik jest zadowolony, ale ty nie. Która zasada testowania uzasadnia twoje sceptyczne podejście?

## answers
a) Testy ulegają zużyciu.
b) Przekonanie o braku defektów jest błędem.
c) Defekty mogą się kumulować.
d) Testowanie gruntowne jest niemożliwe.

## justification
a) Odpowiedź poprawna. Zasada ta oznacza, że jeśli te same testy są powtarzane wielokrotnie, w końcu nie wykrywają one już żadnych nowych defektów. Prawdopodobnie dlatego wszystkie testy zostały zaliczone również w tej wersji.
b) Odpowiedź niepoprawna. Zasada ta odnosi się do błędnego przekonania, że samo wykrycie i usunięcie dużej liczby defektów zapewni sukces systemu.
c) Odpowiedź niepoprawna. Zasada ta mówi, że niewielka liczba modułów zawiera zazwyczaj większość defektów.
d) Odpowiedź niepoprawna. Zasada ta mówi, że testowanie wszystkich kombinacji danych wejściowych i warunków wstępnych jest niewykonalne.

---

# metadata
lo: FL-1.4.1
k-level: K2
points: 1
correct: b

## question
Pracujesz w zespole, który opracowuje aplikację mobilną do zamawiania posiłków. W obecnej iteracji zespół zdecydował się wdrożyć funkcję płatności.
Które z poniższych działań stanowi część **analizy** testów?

## answers
a) Oszacowanie, że testowanie integracji z usługą płatniczą zajmie 8 osobodni.
b) Podjęcie decyzji, że zespół powinien przetestować, czy możliwe jest prawidłowe dzielenie płatności między wielu użytkowników.
c) Wykorzystanie analizy wartości brzegowych w celu uzyskania danych testowych dla przypadków testowych, które sprawdzają prawidłowość przetwarzania płatności dla minimalnej dopuszczalnej kwoty do zapłaty.
d) Analiza rozbieżności między rzeczywistym wynikiem a oczekiwanym wynikiem po wykonaniu przypadku testowego sprawdzającego proces płatności kartą kredytową i zgłoszenie usterki.

## justification
a) Odpowiedź niepoprawna. Oszacowanie nakładu pracy związanego z testowaniem jest częścią planowania testów.
b) Odpowiedź poprawna. Jest to przykład definiowania warunków testowych, które są częścią analizy testów.
c) Odpowiedź niepoprawna. Wykorzystanie technik testowania do uzyskania elementów pokrycia jest częścią projektowania testów.
d) Odpowiedź niepoprawna. Zgłaszanie defektów wykrytych podczas testów dynamicznych jest częścią wykonywania testów.

---

# metadata
lo: FL-1.4.2
k-level: K2
points: 1
correct: b

## question
Które z poniższych czynników mają **istotny** wpływ na podejście do testowania?

i. Model cyklu wytwarzania oprogramowania
ii. Liczba defektów wykrytych w poprzednich projektach
iii. Zidentyfikowane ryzyka produktowe
iv. Nowe wymogi regulacyjne wymuszające formalne testowanie białoskrzynkowe
v. Konfiguracja środowiska testowego

## answers
a) i, ii mają znaczący wpływ; iii, iv, v nie mają znaczącego wpływu.
b) i, iii, iv mają znaczący wpływ; ii, v nie mają znaczącego wpływu.
c) ii, iv, v mają znaczący wpływ; i, iii nie mają znaczącego wpływu.
d) iii, v mają znaczący wpływ; i, ii, iv nie mają znaczącego wpływu.

## justification
Szczegółowe uzasadnienie:
i. Prawda. Cykl wytwarzania oprogramowania ma wpływ na podejście do testów.
ii. Nieprawda. Liczba defektów wykrytych w poprzednich projektach może mieć pewien wpływ, ale nie jest on tak znaczący jak i, iii, iv.
iii. Prawda. Zidentyfikowane ryzyka produktowe są jednym z najważniejszych czynników wpływających na podejście do testów.
iv. Prawda. Wymogi regulacyjne są ważnym czynnikiem wpływającym na podejście do testów.
v. Nieprawda. Środowisko testowe nie ma znaczącego wpływu na podejście do testów.

Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-1.4.5
k-level: K2
points: 1
correct: a, e

## question
Które **dwa** z poniższych zadań wchodzą **głównie** w zakres obowiązków roli testera?

## answers
a) Konfigurowanie środowisk testowych.
b) Utrzymanie backlogu produktu.
c) Projektowanie rozwiązań dla nowych wymagań.
d) Tworzenie planu testów.
e) Analiza podstawy testów.

## justification
a) Odpowiedź poprawna. Jest to wykonywane przez testerów.
b) Odpowiedź niepoprawna. Backlog produktu jest tworzony i utrzymywany przez właściciela produktu.
c) Odpowiedź niepoprawna. Jest to wykonywane przez zespół programistów.
d) Odpowiedź niepoprawna. Jest to zadanie kierownicze.
e) Odpowiedź poprawna. Jest to wykonywane przez testerów, ponieważ jest to zadanie techniczne wykonywane w ramach analizy testów.

---

# metadata
lo: FL-1.5.1
k-level: K2
points: 1
correct: b

## question
Które z poniższych umiejętności (i--v) są **najistotniejsze** dla testera?

i. Posiadanie wiedzy dziedzinowej
ii. Tworzenie wizji produktu
iii. Umiejętność pracy w zespole
iv. Planowanie i organizowanie pracy zespołu
v. Krytyczne myślenie

## answers
a) ii, iv są istotne.
b) i, iii, v są istotne.
c) i, ii, v są istotne.
d) iii, iv są istotne.

## justification
Szczegółowe uzasadnienie:
i. Prawda. Posiadanie wiedzy dziedzinowej jest ważną umiejętnością testera.
ii. Nieprawda. Jest to zadanie analityka biznesowego we współpracy z przedstawicielem jednostki biznesowej.
iii. Prawda. Umiejętność pracy w zespole jest ważną umiejętnością testera.
iv. Nieprawda. Planowanie i organizowanie pracy zespołu jest zadaniem kierownika testów lub, głównie w przypadku zwinnego wytwarzania oprogramowania, całego zespołu, a nie tylko testera.
v. Prawda. Krytyczne myślenie jest jedną z najważniejszych umiejętności testerów.

Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-1.5.2
k-level: K1
points: 1
correct: d

## question
W jaki sposób podejście „cały zespół" przejawia się w interakcjach między testerami a przedstawicielami jednostek biznesowych?

## answers
a) Przedstawiciele jednostek biznesowych decydują o podejściu do automatyzacji testów.
b) Testerzy pomagają przedstawicielom jednostek biznesowych w definiowaniu strategii testów.
c) Przedstawiciele jednostek biznesowych nie są częścią podejścia „cały zespół".
d) Testerzy pomagają przedstawicielom jednostek biznesowych w tworzeniu testów akceptacyjnych.

## justification
a) Odpowiedź niepoprawna. Podejście do automatyzacji testów jest definiowane przez testerów przy pomocy programistów i przedstawicieli jednostek biznesowych.
b) Odpowiedź niepoprawna. Strategia testów jest ustalana we współpracy z programistami.
c) Odpowiedź niepoprawna. Testerzy, programiści i przedstawiciele jednostek biznesowych są częścią podejścia „cały zespół".
d) Odpowiedź poprawna. Testerzy będą ściśle współpracować z przedstawicielami jednostek biznesowych, aby zapewnić osiągnięcie pożądanych poziomów jakości. Obejmuje to wspieranie ich i współpracę z nimi w celu pomocy w tworzeniu odpowiednich testów akceptacyjnych.

---

# metadata
lo: FL-2.1.2
k-level: K1
points: 1
correct: d

## question
Rozważ następującą zasadę: „każdej czynności w ramach cyklu wytwarzania oprogramowania odpowiada odpowiednia czynność testowa". W jakich modelach zasada ta ma zastosowanie?

## answers
a) Tylko w modelach sekwencyjnych.
b) Tylko w modelach iteracyjnych.
c) Tylko w modelach iteracyjnych i przyrostowych.
d) W modelach sekwencyjnych, iteracyjnych i przyrostowych.

## justification
a) Odpowiedź niepoprawna. 
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna. Zasada ta obowiązuje dla wszystkich modeli cyklu wytwarzania oprogramowania.

---

# metadata
lo: FL-2.1.3
k-level: K1
points: 1
correct: c

## question
Które z poniższych stwierdzeń **najlepiej** opisuje wytwarzanie sterowane testami akceptacyjnymi (ATDD)?

## answers
a) W ATDD kryteria akceptacji są zazwyczaj tworzone w formacie „mając/kiedy/wtedy".
b) W ATDD przypadki testowe są zorientowane na kod i tworzone głównie podczas testowania modułowego.
c) W ATDD testy są tworzone w oparciu o kryteria akceptacji, aby kierować rozwojem powiązanego oprogramowania.
d) W ATDD testy opierają się na pożądanym zachowaniu oprogramowania, co ułatwia ich zrozumienie członkom zespołu.

## justification
a) Odpowiedź niepoprawna. Jest to częściej stosowane w wytwarzaniu sterowanym zachowaniem (BDD).
b) Odpowiedź niepoprawna. Jest to opis wytwarzania sterowanego testami (TDD).
c) Odpowiedź poprawna. W wytwarzaniu sterowanym testami akceptacyjnymi (ATDD) testy są tworzone na podstawie kryteriów akceptacji w ramach procesu projektowania.
d) Odpowiedź niepoprawna. Jest to używane w BDD.

---

# metadata
lo: FL-2.1.5
k-level: K2
points: 1
correct: d

## question
Które z poniższych **nie** jest przykładem podejścia „przesunięcie w lewo"?

## answers
a) Przeglądanie wymagań użytkowników przed ich formalną akceptacją przez interesariuszy.
b) Napisanie testu modułowego przed napisaniem odpowiadającego mu fragmentu kodu.
c) Wykonanie testu wydajności modułu podczas testowania modułowego.
d) Napisanie skryptu testowego przed skonfigurowaniem procesu zarządzania konfiguracją.

## justification
a) Odpowiedź niepoprawna. Wczesne przeglądy są przykładem podejścia „przesunięcie w lewo".
b) Odpowiedź niepoprawna. TDD jest przykładem podejścia „przesunięcie w lewo".
c) Odpowiedź niepoprawna. Wczesne testowanie niefunkcjonalne jest przykładem podejścia „przesunięcie w lewo".
d) Odpowiedź poprawna. Skrypty testowe powinny podlegać zarządzaniu konfiguracją, więc nie ma sensu tworzyć skryptów testowych przed ustanowieniem tego procesu.

---

# metadata
lo: FL-2.1.6
k-level: K2
points: 1
correct: c

## question
Który z poniższych argumentów można wykorzystać, aby przekonać swojego przełożonego do organizowania retrospektyw na koniec każdego cyklu wydania oprogramowania?

## answers
a) Retrospektywy są obecnie bardzo popularne i klienci doceniliby, gdybyśmy włączyli je do naszych procesów.
b) Organizowanie retrospektyw pozwoli organizacji zaoszczędzić pieniądze, ponieważ bez nich przedstawiciele użytkowników końcowych nie przekazują natychmiastowych opinii na temat produktu.
c) Słabe punkty procesu zidentyfikowane podczas retrospektywy mogą zostać przeanalizowane i posłużyć jako lista zadań do wykonania w ramach programu ciągłego doskonalenia procesów w organizacji.
d) Retrospektywy obejmują pięć wartości, w tym odwagę i szacunek, które są kluczowe dla utrzymania ciągłego doskonalenia w organizacji.

## justification
a) Odpowiedź niepoprawna. Retrospektywy są bardziej przydatne do identyfikowania możliwości doskonalenia procesu i mają niewielkie znaczenie dla klientów.
b) Odpowiedź niepoprawna. Retrospektywy nie mają na celu zbierania opinii na temat produktu, ale na temat procesu. Ponadto retrospektywy są działaniem wewnętrznym zespołu i nie powinny obejmować przedstawicieli użytkowników końcowych.
c) Odpowiedź poprawna. Regularnie przeprowadzane retrospektyw, gdy podejmowane są odpowiednie działania następcze, ma kluczowe znaczenie dla ciągłego doskonalenia projektowania i testowania.
d) Odpowiedź niepoprawna. Odwaga i szacunek to wartości *eXtreme Programming* i nie są one ściśle związane z retrospektywami.

---

# metadata
lo: FL-2.2.1
k-level: K2
points: 1
correct: a

## question
Dopasuj rodzaje awarii (1--4) do poszczególnych poziomów testów (A--D).

1. Awarie w działaniu systemu polegające na odbieganiu od potrzeb biznesowych użytkownika
2. Awarie w komunikacji między modułami
3. Awarie logiki w kodzie
4. Awarie wynikające z nieprawidłowej implementacji reguł biznesowych

A. Testowanie modułowe
B. Testowanie integracji modułów
C. Testowanie systemowe
D. Testowanie akceptacyjne

## answers
a) 1D, 2B, 3A, 4C.
b) 1D, 2B, 3C, 4A.
c) 1B, 2A, 3D, 4C.
d) 1C, 2B, 3A, 4D.

## justification
Szczegółowe uzasadnienie:
- Podstawą testów akceptacyjnych są potrzeby biznesowe użytkownika (1D).
- Komunikacja między modułami jest testowana podczas testów integracji modułów (2B).
- Awarie w logice można wykryć podczas testowania modułów (3A).
- Zasady biznesowe stanowią podstawę testów systemu (4C).

Zatem:
a) Odpowiedź poprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-2.2.3
k-level: K2
points: 1
correct: b

## question
Testujesz historyjkę użytkownika z trzema kryteriami akceptacji: AC1, AC2 i AC3. AC1 jest objęte przypadkiem testowym TC1, AC2 przypadkiem TC2, a AC3 przypadkiem TC3. Historia wykonania testów obejmowała trzy serie testów na trzech kolejnych wersjach oprogramowania, jak pokazano poniżej:

|         | **Wykonanie 1** | **Wykonanie 2** | **Wykonanie 3** |
| :--- | :---: | :---: | :---: |
| **TC1** | (1) Niezaliczony | (4) Zaliczony    | (7) Zaliczony   |
| **TC2** | (2) Zaliczony    | (5) Niezaliczony | (8) Zaliczony   |
| **TC3** | (3) Niezaliczony | (6) Niezaliczony | (9) Zaliczony   |

Testy są powtarzane po otrzymaniu informacji, że wszystkie usterki wykryte podczas testów zostały usunięte i dostępna jest nowa wersja oprogramowania.
Które z powyższych testów są wykonywane jako testy regresji?

## answers
a) Tylko 4, 7, 8, 9.
b) Tylko 5, 7.
c) Tylko 4, 6, 8, 9.
d) Tylko 5, 6.

## justification
Szczegółowe uzasadnienie:
Ponieważ TC1 i TC3 były niezaliczone w wykonaniu 1 (tj. test (1) i test (3)), test (4) i test (6) są testami potwierdzającymi.
Ponieważ TC2 i TC3 były niezaliczone w wykonaniu 2 (tj. testy (5) i (6)), test (8) i test (9) są również testami potwierdzającymi. TC2 był zaliczony w wykonaniu 1 (tj. test (2)), więc test (5) jest testem regresji. TC1 był zaliczony w wykonaniu 2 (tj. test (4)), więc test (7) jest również testem regresji.

Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-3.1.2
k-level: K2
points: 1
correct: a

## question
Które z poniższych **nie** jest zaletą testowania statycznego?

## answers
a) Tańsze zarządzanie defektami dzięki łatwości wykrywania defektów na późniejszych etapach cyklu wytwarzania oprogramowania.
b) Usuwanie defektów wykrytych podczas testowania statycznego jest zazwyczaj znacznie tańsze niż usuwanie defektów wykrytych podczas testowania dynamicznego.
c) Wykrywanie defektów w kodzie źródłowym, które mogłyby pozostać niewykryte przy przeprowadzaniu wyłącznie testowania dynamicznego.
d) Wykrywanie luk i niespójności w wymaganiach.

## justification
a) Odpowiedź poprawna. Zarządzanie defektami nie jest tańsze. Wykrywanie i naprawianie defektów na późniejszych etapach cyklu życia oprogramowania jest bardziej kosztowne.
b) Odpowiedź niepoprawna. Jest to zaleta testowania statycznego.
c) Odpowiedź niepoprawna. Jest to zaleta testowania statycznego.
d) Odpowiedź niepoprawna. Jest to zaleta testowania statycznego.

---

# metadata
lo: FL-3.2.1
k-level: K1
points: 1
correct: d

## question
Która z poniższych opcji jest zaletą wczesnego i częstego przekazywania informacji zwrotnych?

## answers
a) Poprawia proces testowania w przyszłych projektach.
b) Zmusza klientów do ustalenia priorytetów swoich wymagań w oparciu o uzgodnione ryzyka.
c) Dostarcza metodę pomiaru jakości zmian.
d) Pomaga uniknąć nieporozumień dotyczących wymagań.

## justification
a) Odpowiedź niepoprawna. Informacje zwrotne mogą usprawnić proces testowania, ale jeśli celem jest wyłącznie doskonalenie przyszłych projektów, informacje zwrotne nie muszą być przekazywane wcześnie ani często.
b) Odpowiedź niepoprawna. Informacje zwrotne nie są wykorzystywane do priorytetyzacji wymagań.
c) Odpowiedź niepoprawna. Nie ma jednej, zalecanej metody pomiaru jakości zmian. Nie jest to również jedna z korzyści wynikających z wczesnej informacji zwrotnej, o których mowa w sekcji 3.2.1 sylabusa.
d) Odpowiedź poprawna. Wczesne i częste informacje zwrotne mogą zapobiegać nieporozumieniom dotyczącym wymagań.

---

# metadata
lo: FL-3.2.4
k-level: K2
points: 1
correct: b

## question
Przeglądy stosowane w Twojej organizacji mają następujące cechy:
- Istnieje rola protokolanta
- Głównym celem jest ocena jakości
- Spotkanie przeglądowe jest prowadzone przez autora produktu pracy
- Każdy uczestnik przygotowuje się indywidualnie przed spotkaniem przeglądowym
- Sporządzany jest raport z przeglądu

Który z poniższych typów przeglądu jest **najprawdopodobniej** stosowany w organizacji?

## answers
a) Przegląd nieformalny.
b) Przejrzenie.
c) Przegląd techniczny.
d) Inspekcja.

## justification
Szczegółowe uzasadnienie:
Rola protokolanta sugeruje istnienie spotkania przeglądowego, co eliminuje przegląd nieformalny. Spotkanie prowadzone jest przez autora, co sugeruje przejrzenie i eliminuje przegląd techniczny (który jest prowadzony przez moderatora). Ocena jakości jako główny cel przeglądu sugeruje przede wszystkim, że mamy do czynienia z przejrzeniem, choć może to również być przegląd techniczny lub inspekcja. Indywidualne przygotowanie i raport mogą występować w przypadku przejrzenia. Podane cechy wskazują więc na przejrzenie.

Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-3.2.5
k-level: K1
points: 1
correct: d

## question
Które z poniższych stwierdzeń **nie** jest czynnikiem przyczyniającym się do pomyślnego przeprowadzenia przeglądu?

## answers
a) Poświęcenie przez uczestników odpowiedniej ilości czasu na przegląd.
b) Podzielenie dużych produktów pracy na mniejsze, aby zmniejszyć intensywność wysiłku.
c) Unikanie zachowań, które mogą wskazywać na znudzenie, irytację lub wrogość wobec innych uczestników.
d) Uznanie, docenienie i potraktowanie w sposób obiektywny wykrytych awarii.

## justification
a) Odpowiedź niepoprawna. Odpowiednia ilość czasu dla poszczególnych osób jest czynnikiem sukcesu.
b) Odpowiedź niepoprawna. Podział produktów pracy na małe, odpowiednie części jest czynnikiem sukcesu.
c) Odpowiedź niepoprawna. Unikanie zachowań, które mogą wskazywać na nudę, irytację itp., jest czynnikiem sukcesu.
d) Odpowiedź poprawna. Podczas przeglądów można znaleźć defekty, a nie awarie.

---

# metadata
lo: FL-4.1.1
k-level: K2
points: 1
correct: c

## question
Które z poniższych jest cechą charakterystyczną technik testowania opartych na doświadczeniu?

## answers
a) Przypadki testowe są tworzone na podstawie szczegółowych informacji projektowych.
b) Elementy testowane w sekcji kodu interfejsu są wykorzystywane do pomiaru pokrycia.
c) Techniki testowania w dużym stopniu opierają się na wiedzy testera na temat oprogramowania i dziedziny biznesowej.
d) Przypadki testowe służą do identyfikacji odchyleń od wymagań.

## justification
a) Odpowiedź niepoprawna. Jest to typowa cecha białoskrzynkowych technik testowania. Warunki testowe, przypadki testowe i dane testowe pochodzą z podstawy testów, która może obejmować kod, architekture oprogramowania, szczegółowy projekt lub inne źródła informacji dotyczące wewnętrznej struktury oprogramowania.
b) Odpowiedź niepoprawna. Jest to typowa cecha białoskrzynkowych technik testowania. Pokrycie mierzy się na podstawie elementów przetestowanych w ramach wybranej struktury oraz techniki testowania zastosowanej do podstawy testów.
c) Odpowiedź poprawna. Jest to powszechna cecha technik testowania opartych na doświadczeniu. Wiedza i doświadczenie obejmują oczekiwane wykorzystanie oprogramowania, jego środowisko, prawdopodobne defekty oraz rozkład tych defektów, które są wykorzystywane do definiowania testów.
d) Odpowiedź niepoprawna. Jest to typowa cecha czarnoskrzynkowych technik testowania. Przypadki testowe mogą być wykorzystywane do wykrywania luk w wymaganiach i ich implementacji, a także odchyleń od wymagań.

---

# metadata
lo: FL-4.2.1
k-level: K3
points: 1
correct: b

## question
Testujesz uproszczony formularz wyszukiwania mieszkań, który ma tylko dwa kryteria wyszukiwania:
- piętro (z trzema możliwymi opcjami: parter; pierwsze piętro; drugie lub wyższe piętro)
- rodzaj ogródka (trzy możliwe opcje: bez ogródka; mały ogródek; duży ogródek).

Każde mieszkanie na parterze może mieć ogródek. Mieszkania na wyższych piętrach nie mają ogródka. Formularz posiada wbudowany mechanizm walidacji, który nie pozwala na użycie kryteriów wyszukiwania naruszających tę zasadę. Każdy test ma dwie wartości wejściowe: piętro i rodzaj ogródka. Chcesz zastosować podział na klasy równoważności z pokryciem „każdy wybór", aby uwzględnić w testach każde piętro i każdy rodzaj ogródka.
Jaka jest **minimalna** liczba przypadków testowych, aby osiągnąć 100% pokrycia „każdy wybór"?

## answers
a) 3.
b) 4.
c) 5.
d) 6.

## justification
Szczegółowe uzasadnienie:
Wymagana technika to podział na klasy równoważności w wersji „każdy wybór", co oznacza, że każda klasa równoważności z każdej dziedziny musi być pokryta przynajmniej raz w jakimś przypadku testowym. „Mały ogródek" i „duży ogródek" mogą występować tylko z „parterem", więc potrzebujemy dwóch przypadków testowych z „parterem", które pokryją te dwie klasy równoważności „typ ogródka". Potrzebujemy jeszcze dwóch przypadków testowych, aby pokryć pozostałe dwie klasy równoważności dla „piętra". Pozostała klasa równoważności „rodzaju ogródka" „bez ogrodu" jest objęta tymi testami.

Potrzebujemy więc łącznie czterech przypadków testowych:
- TC1 (parter, mały ogródek)
- TC2 (parter, duży ogródek)
- TC3 (pierwsze piętro, brak ogródka)
- TC4 (drugie lub wyższe piętro, brak ogródka)

A zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.2.2
k-level: K3
points: 1
correct: a

## question
Testujesz system, który oblicza końcową ocenę z kursu dla danego studenta.
Ocena końcowa jest przyznawana na podstawie wyniku końcowego, zgodnie z następującymi zasadami:
- 0--50 punktów: niedostateczny
- 51--60 punktów: dostateczny
- 61--70 punktów: zadowalający
- 71--80 punktów: dobry
- 81--90 punktów: bardzo dobry
- 91--100 punktów: celujący

Przygotowałeś następujący zestaw przypadków testowych:

|         | **Wynik końcowy** | **Ocena końcowa** |
| :--- | :---: | :---: |
| **TC1** | 91 | celujący |
| **TC2** | 50 | niedostateczny |
| **TC3** | 81 | bardzo dobry |
| **TC4** | 60 | dostateczny |
| **TC5** | 70 | zadowalający |
| **TC6** | 80 | dobry |

Jakie pokrycie wartości brzegowych w wersji dwupunktowej dla wartości wyniku końcowego osiąga ten zbiór sześciu przypadków testowych?

## answers
a) 50%.
b) 60%.
c) 33,3%.
d) 100%.

## justification
Szczegółowe uzasadnienie:
Istnieje 12 wartości brzegowych dla końcowego wyniku: 0, 50, 51, 60, 61, 70, 71, 80, 81, 90, 91 i 100. Przypadki testowe obejmują sześć z nich (TC1 -- 91, TC2 -- 50, TC3 -- 81, TC4 -- 60, TC5 -- 70 i TC6 -- 80 - uwaga: w kluczu wymieniono błędnie TC7 -- 51, jednak łączna liczba pokrytych to 6). W związku z tym przypadki testowe obejmują 6/12 = 50%. Zatem:

a) Odpowiedź poprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.2.3
k-level: K3
points: 1
correct: d

## question
Wypożyczalnia rowerów właśnie wprowadziła nowy system zarządzania relacjami z klientami i poprosiła Cię, jako jednego z najbardziej lojalnych członków, o przetestowanie go. Wdrożone funkcje są następujące:
- Każdy może wypożyczyć rower, ale członkowie otrzymują 20% zniżki.
- W przypadku przekroczenia terminu zwrotu zniżka przestaje obowiązywać.
- Po 15 wypożyczeniach członkowie otrzymują prezent: koszulkę z nadrukiem.

Tablica decyzyjna opisująca wdrożone funkcje wygląda następująco:

| **Warunki** | **R1** | **R2** | **R3** | **R4** | **R5** | **R6** | **R7** | **R8** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Bycie członkiem | TAK | TAK | TAK | TAK | NIE | NIE | NIE | NIE |
| Przekroczono termin zwrotu | TAK | NIE | TAK | NIE | TAK | NIE | NIE | TAK |
| 15-te wypożyczenie | NIE | NIE | TAK | TAK | NIE | NIE | TAK | TAK |
| **Akcje** | | | | | | | | |
| Przyznanie 20% zniżki | | X | | X | | | | |
| Prezent -- koszulka z nadrukiem | | | X | X | | | | X |

Opierając się **wyłącznie** na opisie funkcji systemu zarządzania relacjami z klientami, która reguła opisuje sytuację niemożliwą?

## answers
a) R4.
b) R2.
c) R6.
d) R8.

## justification
a) Odpowiedź niepoprawna. Członek, który nie przekroczył terminu, może otrzymać zniżkę i koszulkę z nadrukiem w prezencie po 15 wypożyczeniach roweru.
b) Odpowiedź niepoprawna. Członek, który nie przekroczył terminu, może otrzymać zniżkę, ale nie otrzyma koszulki z nadrukiem, dopóki nie wypożyczy roweru 15 razy.
c) Odpowiedź niepoprawna. Osoby niebędące członkami nie mogą uzyskać zniżki, nawet jeśli nie przekroczyły jeszcze terminu.
d) Odpowiedź poprawna. Osoby niebędące członkami, które również przekroczyły termin, nie otrzymują zniżki, a tylko członkowie mogą otrzymać koszulkę z nadrukiem w prezencie. Dlatego akcja jest niepoprawna.

---

# metadata
lo: FL-4.2.4
k-level: K3
points: 1
correct: d

## question
Testujesz system modelowany przez diagram stanów. System rozpoczyna pracę w stanie INIT, a kończy ją w stanie OFF. Z podanych przejść: INIT -> run -> error -> done -> OFF oraz INIT -> test -> done -> OFF oraz run <-> pause.
Jaka jest **minimalna** liczba przypadków testowych wymagana do uzyskania prawidłowego pokrycia przejść poprawnych?

## answers
a) 4.
b) 2.
c) 7.
d) 3.

## justification
Szczegółowe uzasadnienie:
Przejścia „test" i „error" nie mogą wystąpić w jednym przypadku testowym, a oba mogą być kontynuowane jedynie przejściem „done" do stanu OFF. Oba przejścia „done" również nie mogą wystąpić w jednym przypadku testowym. Oznacza to, że potrzebujemy co najmniej trzech przypadków testowych, aby osiągnąć pokrycie przejść poprawnych, na przykład:
TC1: test, done
TC2: run, error, done
TC3: run, pause, resume, pause, done

A zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-4.3.1
k-level: K2
points: 1
correct: a

## question
Twój zestaw testowy osiągnął 100% pokrycia instrukcji.
Jakie są tego konsekwencje?

## answers
a) Każda instrukcja w kodzie zawierająca defekt została wykonana co najmniej raz.
b) Każdy zestaw testowy zawierający więcej przypadków testowych niż Twój zestaw testowy również osiągnie 100% pokrycia instrukcji.
c) Każda ścieżka w kodzie została wykonana co najmniej raz.
d) Każda kombinacja wartości wejściowych została przetestowana co najmniej raz.

## justification
a) Odpowiedź poprawna. Ponieważ osiągnięto 100% pokrycia instrukcji, każda instrukcja, w tym każda zawierająca defekt, musiała zostać wykonana co najmniej raz.
b) Odpowiedź niepoprawna. Pokrycie zależy od tego, co jest testowane, a nie od liczby przypadków testowych. Na przykład dla kodu „if (x==0) y=1" jeden przypadek testowy (x=0) osiąga 100% pokrycia instrukcji, ale dwa przypadki testowe (x=1) i (x=2) razem osiągają tylko 50% pokrycia instrukcji.
c) Odpowiedź niepoprawna. Jeśli w kodzie występuje pętla, może istnieć nieskończona liczba możliwych ścieżek, więc nie jest możliwe wykonanie wszystkich możliwych ścieżek w kodzie.
d) Odpowiedź niepoprawna. Testowanie gruntowne nie jest możliwe (patrz sekcja o zasadach testowania w sylabusie). Na przykład dla kodu „input x; print x" każdy pojedynczy test z dowolnym wejściem x osiąga 100% pokrycia instrukcji, ale pokrywa tylko jedną wartość wejściową.

---

# metadata
lo: FL-4.3.3
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń **nie** jest prawdziwe w przypadku testowania białoskrzynkowego?

## answers
a) Podczas testowania białoskrzynkowego brana jest pod uwagę cała implementacja oprogramowania.
b) Metryki pokrycia białoskrzynkowego mogą pomóc w identyfikacji dodatkowych testów w celu zwiększenia pokrycia kodu.
c) Techniki testowania białoskrzynkowego mogą być stosowane w testowaniu statycznym.
d) Testowanie białoskrzynkowe może pomóc w identyfikacji luk w implementacji wymagań.

## justification
a) Odpowiedź niepoprawna. Podstawową zaletą białoskrzynkowych technik testowania jest to, że podczas testowania brana jest pod uwagę cała implementacja oprogramowania.
b) Odpowiedź niepoprawna. Miary pokrycia białoskrzynkowego zapewniają obiektywną miarę pokrycia i dostarczają informacji niezbędnych do generowania dodatkowych testów w celu zwiększenia tego pokrycia.
c) Odpowiedź niepoprawna. Białoskrzynkowe techniki testowania mogą być wykorzystywane do przeprowadzania przeglądów (testów statycznych).
d) Odpowiedź poprawna. Jest to słaba strona białoskrzynkowych technik testowania. Nie są one w stanie zidentyfikować brakującej implementacji, ponieważ opierają się wyłącznie na strukturze przedmiotu testów, a nie na specyfikacji wymagań.

---

# metadata
lo: FL-4.4.1
k-level: K2
points: 1
correct: a

## question
Które z poniższych stwierdzeń **najlepiej** opisuje koncepcję zgadywania błędów?

## answers
a) Zgadywanie błędów polega na wykorzystaniu wiedzy i doświadczenia dotyczącego defektów wykrytych w przeszłości oraz typowych błędów popełnianych przez programistów.
b) Zgadywanie błędów polega na wykorzystaniu osobistych doświadczeń związanych z programowaniem oraz błędów popełnionych jako programista.
c) Zgadywanie błędów wymaga wyobrażenia sobie, że jesteśmy użytkownikiem przedmiotu testów i zgadujemy błędy, które moglibyśmy popełnić podczas interakcji z nim.
d) Zgadywanie błędów wymaga szybkiego powielenia zadania programistycznego w celu zidentyfikowania rodzajów błędów, które może popełnić programista.

## justification
a) Odpowiedź poprawna. Podstawową koncepcją zgadywania błędów jest to, że tester, opierając się na wcześniejszych doświadczeniach (a czasem na listach kontrolnych), próbuje odgadnąć, jakie błędy mogły zostać popełnione przez programistę i jakie defekty mogą występować w przedmiocie testów.
b) Odpowiedź niepoprawna. Chociaż tester, który wcześniej był programistą, może wykorzystać swoje doświadczenie podczas zgadywania błędów, to jednak ta technika testowania nie opiera się na wcześniejszego doświadczenia w programowaniu.
c) Odpowiedź niepoprawna. Zgadywanie błędów nie jest techniką ograniczoną do testowania użyteczności i odgadywania, w jaki sposób użytkownicy mogą nieprawidłowo korzystać z przedmiotu testów.
d) Odpowiedź niepoprawna. Powielanie zadania programistycznego to nie zgadywanie błędów. Ponadto, ma ono kilka wad, które sprawiają, że jest ono niepraktyczne, np. konieczność posiadania przez testera umiejętności równoważnych umiejętnościom programisty oraz czas potrzebny do wykonania zadania programistycznego. To nie jest zgadywanie błędów.

---

# metadata
lo: FL-4.4.2
k-level: K2
points: 1
correct: c

## question
W ramach realizowanego projektu nastąpiło opóźnienie w wydaniu zupełnie nowej aplikacji, a testy rozpoczęły się z opóźnieniem. Dysponujesz jednak bardzo szczegółową wiedzą dziedzinową i dobrymi umiejętnościami analitycznymi. Pełna lista wymagań nie została jeszcze udostępniona zespołowi, ale kierownictwo prosi o przedstawienie niektórych wyników testów.
Która technika testowania najlepiej pasuje w tej sytuacji?

## answers
a) Testowanie oparte na liście kontrolnej.
b) Zgadywanie błędów.
c) Testowanie eksploracyjne.
d) Testowanie gałęzi.

## justification
a) Odpowiedź niepoprawna. Jest to nowy produkt. Prawdopodobnie nie masz jeszcze listy kontrolnej, a warunki testowe mogą być nieznane z powodu brakujących wymagań.
b) Odpowiedź niepoprawna. Jest to nowy produkt. Prawdopodobnie nie masz wystarczających informacji, aby poprawnie zgadywać błędy.
c) Odpowiedź poprawna. Testowanie eksploracyjne jest najbardziej przydatne, gdy specyfikacja jest szczątkowa lub jej brak, bądź gdy termin wykonania testów jest pilny.
d) Odpowiedź niepoprawna. Testowanie gałęzi jest czasochłonne, a kierownictwo prosi o wyniki testów już teraz. Ponadto testowanie gałęzi nie wymaga wiedzy dziedzinowej.

---

# metadata
lo: FL-4.5.2
k-level: K2
points: 1
correct: b

## question
Które z poniższych stwierdzeń **NAJLEPIEJ** opisuje sposób dokumentowania kryteriów akceptacji?

## answers
a) Przeprowadzanie retrospektyw w celu określenia rzeczywistych potrzeb interesariuszy w odniesieniu do danej historyjki użytkownika.
b) Użycie formatu „mając/kiedy/wtedy” do opisania przykładowego warunku testowego związanego z daną historyjką użytkownika.
c) Wykorzystanie komunikacji werbalnej w celu zmniejszenia ryzyka niezrozumienia kryteriów akceptacji przez inne osoby.
d) Dokumentowanie ryzyk związanych z daną historyjką użytkownika w planie testów w celu ułatwienia testowania danej historyjki użytkownika w oparciu o ryzyko.

## justification
a) Odpowiedź niepoprawna. Retrospektywy służą do rejestrowania wniosków i doskonalenia procesu rozwoju i testowania, a nie do dokumentowania kryteriów akceptacji.
b) Odpowiedź poprawna. To standardowy sposób dokumentowania kryteriów akceptacji.
c) Odpowiedź niepoprawna. Komunikacja werbalna nie pozwala na fizyczne udokumentowanie kryteriów akceptacji jako części historyjki użytkownika (aspekt „karty” w modelu 3C).
d) Odpowiedź niepoprawna. Kryteria akceptacji odnoszą się do historyjki użytkownika, a nie do planu testów. Ponadto kryteria akceptacji to warunki, które muszą zostać spełnione, aby uznać historyjkę użytkownika za zakończoną. Ryzyka nie stanowią takich warunków.

---

# metadata
lo: FL-4.5.3
k-level: K3
points: 1
correct: a

## question
Rozważ następującą historyjkę użytkownika:

*JAKO redaktor*
*CHCĘ przejrzeć treść przed jej opublikowaniem,*
*ABY upewnić się, że gramatyka jest poprawna.*

oraz kryteria akceptacji:

- Użytkownik może zalogować się do systemu zarządzania treścią z rolą „redaktor”
- Redaktor może przeglądać istniejące strony z treściami
- Redaktor może edytować zawartość strony
- Redaktor może dodawać komentarze w postaci znaczników
- Redaktor może zapisywać zmiany
- Redaktor może ponownie przypisać artykuł do roli „właściciel treści”, aby wprowadzać aktualizacje

Które z poniższych jest **najlepszym** przykładem testu ATDD dla tej historyjki użytkownika?

## answers
a) Sprawdź, czy redaktor może zapisać dokument po edycji zawartości strony.
b) Sprawdź, czy właściciel treści może się zalogować i wprowadzać aktualizacje treści.
c) Sprawdź, czy redaktor może zaplanować publikację edytowanej treści.
d) Sprawdź, czy redaktor może przypisać artykuł do innego redaktora w celu aktualizacji.

## justification
a) Odpowiedź poprawna. Test ten obejmuje dwa kryteria akceptacji: jedno dotyczące edycji dokumentu, a drugie dotyczące zapisywania zmian.
b) Odpowiedź niepoprawna. Kryteria akceptacji dotyczą działań redaktora, a nie właściciela treści.
c) Odpowiedź niepoprawna. Planowanie publikacji redagowanej treści może być przydatną funkcją, ale nie jest objęte kryteriami akceptacji.
d) Odpowiedź niepoprawna. Kryteria akceptacji dotyczą przeniesienia odpowiedzialności z redaktora na właściciela treści, a nie na innego redaktora.

---

# metadata
lo: FL-5.1.2
k-level: K1
points: 1
correct: c

## question
W jaki sposób testerzy wspierają planowanie iteracji i wydania?

## answers
a) Określając priorytet historyjek użytkownika, które mają zostać opracowane przez zespół wytwórczy.
b) Koncentrując się wyłącznie na aspektach funkcjonalnych testowanego systemu.
c) Uczestnicząc w szczegółowej identyfikacji i ocenie ryzyka związanego z historyjkami użytkownika.
d) Gwarantując wydanie wysokiej jakości oprogramowania poprzez wczesne projektowanie testów podczas planowania wydania.

## justification
a) Odpowiedź niepoprawna. Priorytety dla historyjek użytkownika są ustalane przez przedstawiciela jednostki biznesowej wraz z zespołem wytwórczym.
b) Odpowiedź niepoprawna. Testerzy koncentrują się zarówno na funkcjonalnych, jak i niefunkcjonalnych aspektach testowanego systemu.
c) Odpowiedź poprawna. Zgodnie z sylabusem jest to jeden ze sposobów, w jaki testerzy zwiększają wartość planowania iteracji i wydania.
d) Odpowiedź niepoprawna. Wczesne projektowanie testów nie jest częścią planowania wydania. Wczesne projektowanie testów nie gwarantuje automatycznie wydania wysokiej jakości oprogramowania.

---

# metadata
lo: FL-5.1.3
k-level: K2
points: 1
correct: c, e

## question
Które **dwie** z poniższych opcji są kryteriami wyjścia z fazy testowania systemowego?

## answers
a) Gotowość środowiska testowego.
b) Możliwość zalogowania się do przedmiotu testów przez testera.
c) Osiągnięcie szacowanej gęstości defektów.
d) Wymagania są przetłumaczone na format „mając/kiedy/wtedy”.
e) Testy regresji są zautomatyzowane.

## justification
a) Odpowiedź niepoprawna. Gotowość środowiska testowego jest kryterium dostępności zasobów, dlatego należy do kryteriów wejścia.
b) Odpowiedź niepoprawna. Jest to kryterium dostępności zasobów, dlatego należy do kryteriów wejścia.
c) Odpowiedź poprawna. Szacowana gęstość defektów jest miarą staranności, dlatego należy do kryteriów wyjścia.
d) Odpowiedź niepoprawna. Wymagania przetłumaczone na określony format dają wymagania możliwe do przetestowania, dlatego należą do kryteriów wejścia.
e) Odpowiedź poprawna. Automatyzacja testów regresji jest kryterium ukończenia, dlatego należy do kryteriów wyjścia.

---

# metadata
lo: FL-5.1.4
k-level: K3
points: 1
correct: d

## question
Twój zespół stosuje technikę szacowania trójpunktowego, aby oszacować wysiłek testowy związany z testowaniem nowej funkcji wysokiego ryzyka. Dokonano następujących szacunków:

- Najbardziej optymistyczne oszacowanie: 2 osobogodziny
- Najbardziej prawdopodobne oszacowanie: 11 osobogodzin
- Najbardziej pesymistyczne oszacowanie: 14 osobogodzin

Ile ostatecznie wynosi szacowany wysiłek testowy?

## answers
a) 9 osobogodzin.
b) 14 osobogodzin.
c) 11 osobogodzin.
d) 10 osobogodzin.

## justification
W technice szacowania trójpunktowego: $E = (opt + 4 \cdot npr + pes)/6$, gdzie *opt*, *npr* i *pes* to odpowiednio szacowanie optymistyczne, najbardziej prawdopodobne i pesymistyczne.
Podstawiając do wzoru otrzymujemy: $E = (2 + 4 \cdot 11 + 14)/6 = 10$.
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-5.1.5
k-level: K3
points: 1
correct: a

## question
Testujesz aplikację mobilną, która pozwala użytkownikom znaleźć pobliską restaurację na podstawie rodzaju potraw, które użytkownicy chcą zjeść. Rozważ poniższą listę przypadków testowych, priorytetów (1 = wysoki priorytet, 2 = średni priorytet, 3 = niski priorytet) i zależności.

| **Numer przypadku testowego** | **Warunek testowy objęty testem** | **Priorytet** | **Zależność logiczna** |
| :--- | :--- | :---: | :---: |
| TC 001 | Wybierz rodzaj żywności | 3 | brak |
| TC 002 | Wybierz restaurację | 2 | TC 001 |
| TC 003 | Uzyskaj wskazówki dojazdu | 1 | TC 002 |
| TC 004 | Zadzwoń do restauracji | 2 | TC 002 |
| TC 005 | Zarezerwuj stolik | 3 | TC 002 |

Który z poniższych przypadków testowych powinien zostać wykonany jako **trzeci** w kolejności?

## answers
a) TC 003.
b) TC 005.
c) TC 002.
d) TC 001.

## justification
Test TC 001 musi być wykonany jako pierwszy, a następnie TC 002, aby spełnić zależności. Następnie TC 003, aby spełnić priorytet, a następnie TC 004, po którym następuje TC 005.
Zatem:
a) Odpowiedź poprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.1.7
k-level: K2
points: 1
correct: a

## question
Rozważ następujące kategorie testów (1--4) i kwadranty testowe (A--D).

1. Testowanie użyteczności
2. Testowanie modułowe
3. Testowanie funkcjonalne
4. Testowanie niezawodności

A. Kwadrant Q1: zorientowany na technologię, wspierający zespół programistów
B. Kwadrant Q2: zorientowany na biznes, wspierający zespół programistów
C. Kwadrant Q3: zorientowany na biznes, krytykujący produkt
D. Kwadrant Q4: zorientowany na technologię, krytykujący produkt

W jaki sposób poniższe kategorie testów odnoszą się do kwadrantów testowych?

## answers
a) 1C, 2A, 3B, 4D.
b) 1D, 2A, 3C, 4B.
c) 1C, 2B, 3D, 4A.
d) 1D, 2B, 3C, 4A.

## justification
Uwzględniając, iż:

- testy użyteczności są w Q3 (1 -- C),
- testy modułów są w Q1 (2 -- A),
- testy funkcjonalne są w Q2 (3 -- B),
- testy niezawodności są w Q4 (4 -- D),

mamy:
a) Odpowiedź poprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.2.4
k-level: K2
points: 1
correct: c

## question
Podczas analizy ryzyka zidentyfikowano i oceniono następujące ryzyko:

- Ryzyko: czas reakcji jest zbyt długi, aby wygenerować raport
- Prawdopodobieństwo wystąpienia ryzyka: średnie
- Wpływ ryzyka: wysoki
- Reakcja na ryzyko:
    - Niezależny zespół testowy przeprowadza testy wydajności podczas testowania systemowego
    - Wybrana grupa użytkowników końcowych przeprowadza testy akceptacyjne alfa i beta przed wydaniem produktu

Jakie działania należy podjąć w odpowiedzi na to przeanalizowane ryzyko?

## answers
a) Akceptacja ryzyka.
b) Plan awaryjny.
c) Łagodzenie ryzyka.
d) Przeniesienie ryzyka.

## justification
a) Odpowiedź niepoprawna. Nie akceptujemy ryzyka; proponujemy konkretne działania.
b) Odpowiedź niepoprawna. Nie zaproponowano żadnych planów awaryjnych.
c) Odpowiedź poprawna. Proponowane działania dotyczą testowania, które jest formą łagodzenia ryzyka.
d) Odpowiedź niepoprawna. Ryzyko nie jest przenoszone, ale łagodzone.

---

# metadata
lo: FL-5.3.3
k-level: K2
points: 1
correct: d

## question
Który produkt pracy może zostać wykorzystany przez zespół zwinny w celu pokazania ilości pracy, jaka została wykonana oraz całkowitej ilości pracy pozostałej do wykonania w danej iteracji?

## answers
a) Kryteria akceptacji.
b) Raport o defekcie.
c) Sumaryczny raport z testów.
d) Wykres spalania.

## justification
a) Odpowiedź niepoprawna. Kryteria akceptacji to warunki stosowane do podjęcia decyzji, czy historyjka użytkownika jest gotowa. Nie mogą one pokazywać postępu prac.
b) Odpowiedź niepoprawna. Raporty o defektach informują o defektach. Nie pokazują one postępu prac.
c) Odpowiedź niepoprawna. Sumaryczny raport z testów można utworzyć po zakończeniu iteracji, więc nie pokazuje on postępu w sposób ciągły w ramach iteracji.
d) Odpowiedź poprawna. Wykresy spalania są graficznym przedstawieniem pozostałej pracy w stosunku do pozostałego czasu. Są one aktualizowane codziennie, więc mogą w sposób ciągły pokazywać postęp prac.

---

# metadata
lo: FL-5.4.1
k-level: K2
points: 1
correct: c

## question
Musisz zaktualizować jeden ze skryptów testów automatycznych, aby był zgodny z nowym wymaganiem. Który proces wskazuje, że tworzysz nową wersję skryptu testowego w repozytorium testów?

## answers
a) Zarządzanie śledzeniem powiązań.
b) Testowanie pielęgnacyjne.
c) Zarządzanie konfiguracją.
d) Inżynieria wymagań.

## justification
a) Odpowiedź niepoprawna. Śledzenie powiązań to związek między dwoma lub więcej produktami pracy, a nie między różnymi wersjami tego samego produktu pracy.
b) Odpowiedź niepoprawna. Testowanie pielęgnacyjne dotyczy testowania zmian; nie jest ściśle związane z wersjonowaniem skryptów testowych i zarządzaniem konfiguracją.
c) Odpowiedź poprawna. Aby wesprzeć testowanie, zarządzanie konfiguracją może obejmować kontrolę wersji wszystkich elementów testowych.
d) Odpowiedź niepoprawna. Inżynieria wymagań polega na pozyskiwaniu, dokumentowaniu i zarządzaniu wymaganiami; nie jest ściśle związana z wersjonowaniem skryptów testowych i zarządzaniem konfiguracją.

---

# metadata
lo: FL-5.5.1
k-level: K3
points: 1
correct: c

## question
Programiści przekazali Ci następujący raport o defekcie stwierdzający, że anomalia opisana w niniejszym raporcie nie jest powtarzalna.

> *Aplikacja zawiesza się*
>
> *3.05.2022 -- Jan Kowalski -- Odrzucone*
>
> *Aplikacja zawiesza się po wpisaniu „Test input: \$ä” w polu Nazwa na ekranie tworzenia nowego użytkownika. Próbowałem się wylogować, zalogować na konto test_admin01, ale problem się powtórzył. Próbowałem z innymi kontami testowymi administratora, ale problem się powtórzył. Nie pojawił się żaden komunikat o błędzie; log (patrz załącznik) zawiera powiadomienie o błędzie krytycznym. Zgodnie z przypadkiem testowym TC-1305 aplikacja powinna zaakceptować podane dane i utworzyć użytkownika. Proszę o pilne usunięcie tego defektu, ponieważ funkcja ta jest powiązana z REQ-0012, które jest krytycznym nowym wymaganiem biznesowym.*

Jakich krytycznych informacji, które byłyby przydatne dla programistów, **brakuje** w tym raporcie?

## answers
a) Oczekiwany wynik i rzeczywisty wynik.
b) Odniesienia i status defektu.
c) Środowisko testowe i element testowy.
d) Priorytet i krytyczność (ang. *severity*).

## justification
a) Odpowiedź niepoprawna. Oczekiwanym rezultatem jest „aplikacja powinna zaakceptować podane dane wejściowe i utworzyć użytkownika”. Rzeczywisty rezultat to „Aplikacja zawiesza się po wpisaniu 'Test input. \$ä'”.
b) Odpowiedź niepoprawna. Istnieje odniesienie do przypadku testowego TC--1305 i powiązanego wymagania REQ-0012, a także status, który stwierdza, że defekt został wcześniej odrzucony. Ponadto status nie byłby zbyt pomocny dla programistów.
c) Odpowiedź poprawna. Nie wiemy, w jakim środowisku testowym wykryto anomalię, nie wiemy również, która aplikacja (i jej wersja) jest nią dotknięta.
d) Odpowiedź niepoprawna. Raport o defekcie stwierdza, że anomalia jest pilna, że jest to problem globalny (tj. dotyczy wielu, jeśli nie wszystkich, kont administratorów testów) i że ma ona duży wpływ na interesariuszy biznesowych.

---

# metadata
lo: FL-6.1.1
k-level: K2
points: 1
correct: c

## question
Które czynności testowe wspiera narzędzie do przygotowywania danych?

## answers
a) Monitorowanie testów i nadzór nad testami.
b) Analiza testów.
c) Projektowanie testów i implementacja testów.
d) Ukończenie testów.

## justification
a) Odpowiedź niepoprawna. Monitorowanie testów obejmuje bieżącą kontrolę wszystkich czynności i porównanie rzeczywistych postępów z planem testów. Nadzór nad testami obejmuje podejmowanie czynności niezbędnych do osiągnięcia celów testów określonych w planie testów. Podczas tych czynności nie przygotowuje się żadnych danych testowych.
b) Odpowiedź niepoprawna. Analiza testów obejmuje analizę podstawy testów w celu zidentyfikowania warunków testowych i ustalenia ich priorytetów. Podczas tej czynności nie przygotowuje się danych testowych.
c) Odpowiedź poprawna. Projektowanie i implementacja testów może obejmować identyfikację, tworzenie lub pozyskiwanie testaliów (np. danych testowych) niezbędnych do wykonania testów.
d) Odpowiedź niepoprawna. Czynności związane z ukończeniem testów mają miejsce w kluczowych momentach projektu (np. wydanie, koniec iteracji, ukończenie testów danego poziomu), więc jest już za późno na przygotowanie danych testowych.

---

# metadata
lo: FL-6.2.1
k-level: K1
points: 1
correct: b

## question
Które z poniższych stwierdzeń prawidłowo identyfikuje potencjalne ryzyko związane z automatyzacją testów?

## answers
a) Automatyzacja może spowodować nieznane regresje w produkcji.
b) Wysiłek niezbędny do utrzymania testaliów może nie być odpowiednio oszacowany.
c) Narzędzia testowe i związane z nimi testalia mogą nie być wystarczająco niezawodne.
d) Automatyzacja może skrócić czas przeznaczony na testowanie manualne.

## justification
a) Odpowiedź niepoprawna. Automatyzacja testów nie powoduje pojawienia się nieznanych regresji w środowisku produkcyjnym.
b) Odpowiedź poprawna. Niewłaściwe szacowanie wysiłku na utrzymanie testaliów stanowi ryzyko.
c) Odpowiedź niepoprawna. Narzędzia testowe należy dobierać tak, aby można było polegać na nich i na ich testaliach.
d) Odpowiedź niepoprawna. Głównym celem automatyzacji testów jest ograniczenie testów manualnych. Jest to więc korzyść, a nie ryzyko.

---

# metadata
lo: FL-1.1.2
k-level: K2
points: 1
correct: a
additional: true

## question
Poproszono Cię o przeanalizowanie i usunięcie przyczyn awarii w nowym systemie, który ma zostać uruchomiony.
Jakie czynności wykonujesz?

## answers
a) Debugowanie.
b) Testowanie oprogramowania.
c) Pozyskiwanie wymagań.
d) Zarządzanie defektami.

## justification
a) Odpowiedź poprawna. Debugowanie to proces wyszukiwania, analizowania i usuwania przyczyn awarii modułu lub systemu.
b) Odpowiedź niepoprawna. Testowanie to proces związany z planowaniem, przygotowaniem i oceną modułu lub systemu oraz powiązanych produktów pracy w celu ustalenia, czy spełniają one określone wymagania, wykazania, że są one odpowiednie do zamierzonego celu, oraz wykrycia defektów. Nie ma to związku z usuwaniem przyczyn awarii.
c) Odpowiedź niepoprawna. Pozyskiwanie wymagań to proces gromadzenia, rejestrowania i dokumentowania wymagań z dostępnych źródeł. Nie ma to związku z usuwaniem przyczyn awarii.
d) Odpowiedź niepoprawna. Zarządzanie defektami to proces rozpoznawania, rejestrowania, klasyfikowania, badania, rozwiązywania i usuwania defektów. Nie ma to związku z usuwaniem przyczyn awarii.

---

# metadata
lo: FL-1.2.2
k-level: K1
points: 1
correct: d
additional: true

## question
W wielu organizacjach zajmujących się oprogramowaniem dział testowania nazywa się działem zapewnienia jakości (QA). Czy to zdanie jest poprawne, czy nie i dlaczego?

## answers
a) Jest poprawne. Testowanie i QA oznaczają dokładnie to samo.
b) Jest poprawne. Nazwy te mogą być używane zamiennie, ponieważ zarówno testowanie, jak i QA, koncentrują się na tych samych kwestiach związanych z jakością.
c) Nie jest poprawne. Testowanie to coś więcej; testowanie obejmuje wszystkie czynności związane z jakością. QA koncentruje się na procesach związanych z jakością.
d) Nie jest poprawne. QA koncentruje się na procesach związanych z jakością, a testowanie na kontroli modułu lub systemu pod kątem występowania w nim defektów.

## justification
Uwzględniając, że testowanie i zapewnienie jakości to nie to samo, należy pamiętać, że testowanie to proces obejmujący wszystkie czynności w ramach cyklu wytwarzania oprogramowania -- zarówno statyczne, jak i dynamiczne -- związane z planowaniem, przygotowaniem i oceną modułu lub systemu oraz powiązanych produktów pracy w celu ustalenia, czy spełniają one określone wymagania oraz wykazania, że są one odpowiednie do zamierzonego celu, a także wykrycia defektów. Zapewnienie jakości natomiast koncentruje się na ustanawianiu, wprowadzaniu, monitorowaniu, ulepszaniu i przestrzeganiu procesów związanych z jakością.
Zapewnienie jakości natomiast koncentruje się na ustanawianiu, wprowadzaniu, monitorowaniu, ulepszaniu i przestrzeganiu procesów związanych z jakością. W związku z powyższym:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-1.2.3
k-level: K2
points: 1
correct: d
additional: true

## question
Dzwoniący telefon na sąsiednim stanowisku pracy rozprasza programistę, powodując, że nieprawidłowo programuje on logikę sprawdzającą górną wartość brzegową zmiennej wejściowej. Później, podczas testowania systemu, tester zauważa, że pole wejściowe akceptuje nieprawidłowe wartości wejściowe.
Czym w tym scenariuszu jest nieprawidłowo zakodowana górna wartość brzegowa?

## answers
a) Podstawową przyczyną.
b) Awarią.
c) Błędem.
d) Defektem.

## justification
a) Odpowiedź niepoprawna. Podstawową przyczyną jest rozproszenie uwagi programisty podczas programowania.
b) Odpowiedź niepoprawna. Akceptowanie nieprawidłowych danych wejściowych jest awarią.
c) Odpowiedź niepoprawna. Błędem jest pomyłka programisty, która spowodowała tę niepoprawną implementację wartości brzegowej.
d) Odpowiedź poprawna. Problemem w kodzie jest defekt.

---

# metadata
lo: FL-1.4.3
k-level: K2
points: 1
correct: d
additional: true

## question
Rozważ następujący produkt pracy związany z testowaniem.

| Karta opisu testu nr 04.018 | Czas trwania sesji: 1 godz. |
| :--- | :--- |
| Przeglądaj: | Strona rejestracji |
| Przy pomocy: | Różnych zestawów nieprawidłowych danych wejściowych |
| Aby odkryć: | Defekty związane z akceptacją rejestracji przy użyciu błędnego wejścia |

W ramach której grupy czynności testowych tworzony jest ten dokument?

## answers
a) Planowanie testów.
b) Monitorowanie testów i nadzór nad testami.
c) Analiza testów.
d) Projektowanie testów.

## justification
Rozważanymi testaliami jest karta opisu testów, która jest wynikiem projektowania testów, zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-1.4.4
k-level: K2
points: 1
correct: c
additional: true

## question
Które z poniższych **najlepiej** pokazuje, jak śledzenie powiązań wspiera testowanie?

## answers
a) Przeprowadzenie analizy wpływu zmiany dostarczy informacji o ukończeniu testów.
b) Analizowanie śledzenia wyników testów do przypadków testowych dostarczy informacji na temat szacowanego poziomu ryzyka rezydualnego (resztkowego).
c) Przeprowadzenie analizy wpływu zmiany pomoże w wyborze odpowiednich przypadków testowych do testów regresji.
d) Analizowanie śledzenia przypadków testowych i przedmiotów testów do podstawy testów pomoże w wyborze danych testowych w celu osiągnięcia zakładanego pokrycia przedmiotu testów.

## justification
a) Odpowiedź niepoprawna. Przeprowadzenie analizy wpływu nie dostarczy informacji o kompletności testów. Analiza wpływu zmian pomoże w wyborze odpowiednich przypadków testowych do wykonania.
b) Odpowiedź niepoprawna. Śledzenie powiązań nie dostarcza informacji o szacowanym poziomie ryzyka rezydualnego (resztkowego), jeśli przypadki testowe nie są powiązane z ryzykami.
c) Odpowiedź poprawna. Przeprowadzenie analizy wpływu zmian pomaga w wyborze przypadków testowych do testów regresji.
d) Odpowiedź niepoprawna. Analiza śledzenia powiązań między podstawą testów, przedmiotami testów i przypadkami testowymi nie pomaga w wyborze danych testowych w celu osiągnięcia zakładanego pokrycia przedmiotu testów. Wybór danych testowych jest bardziej związany z analizą i implementacją testów, a nie śledzeniem powiązań.

---

# metadata
lo: FL-1.5.3
k-level: K2
points: 1
correct: d
additional: true

## question
Które z poniższych stwierdzeń **najlepiej** opisuje korzyść wynikającą z niezależności testowania?

## answers
a) Wykorzystanie niezależnego zespołu testowego pozwala kierownictwu projektu przypisać odpowiedzialność za jakość końcowego produktu temu zespołowi.
b) Jeśli można sobie pozwolić na zespół testowy spoza organizacji, zespół ten nie będzie tak łatwo podatny na wpływy kierownictwa projektu związane z dostarczeniem produktu i koniecznością dotrzymania ścisłych terminów dostawy.
c) Niezależny zespół testowy może pracować oddzielnie od programistów, nie musi reagować na zmiany wymagań projektowych i może ograniczyć komunikację z programistami do zgłaszania defektów przez system zarządzania defektami.
d) Gdy specyfikacje zawierają niejasności i niespójności, przyjmuje się założenia dotyczące ich interpretacji, a niezależny tester może być przydatny w kwestionowaniu tych założeń i interpretacji dokonanych przez programistę.

## justification
a) Odpowiedź niepoprawna. Jakość powinna być obowiązkiem wszystkich osób pracujących nad projektem, a nie wyłącznie zespołu testowego.
b) Odpowiedź niepoprawna. Po pierwsze, nie jest to korzystne, jeśli zewnętrzny zespół testowy nie dotrzymuje terminów dostaw, a po drugie, nie ma powodu, aby sądzić, że zewnętrzne zespoły testowe będą uważały, że nie muszą dotrzymywać ścisłych terminów dostaw.
c) Odpowiedź niepoprawna. Całkowita izolacja zespołu testowego jest złą praktyką -- oczekuje się, że zewnętrzny zespół testowy będzie zwracał uwagę na zmieniające się wymagania projektu i dobrze komunikował się z programistami.
d) Odpowiedź poprawna. Specyfikacje nigdy nie są idealne, co oznacza, że programista będzie musiał przyjąć pewne założenia. Niezależny tester jest przydatny, ponieważ może kwestionować i weryfikować założenia oraz wynikające z nich interpretacje programisty.

---

# metadata
lo: FL-2.1.1
k-level: K2
points: 1
correct: b, c
additional: true

## question
Pracujesz jako tester w zespole, który stosuje model V.
Które **dwie** z poniższych czynności **można** wykonać w początkowych fazach cyklu wytwarzania oprogramowania?

## answers
a) Dynamiczne wykonywanie testów.
b) Testowanie statyczne.
c) Planowanie testów.
d) Wykonywanie testów akceptacyjnych.
e) Testowanie pielęgnacyjne.

## justification
a) Odpowiedź niepoprawna. Kod wykonywalny jest zazwyczaj tworzony w późniejszych fazach, więc dynamiczne testy nie mogą być przeprowadzane na wczesnym etapie wytwarzania oprogramowania.
b) Odpowiedź poprawna. W sekwencyjnych modelach wytwarzania oprogramowania testerzy uczestniczą w początkowych fazach w przeglądach wymagań, co jest formą testowania statycznego.
c) Odpowiedź poprawna. Planowanie testów można przeprowadzić na wczesnym etapie cyklu wytwarzania oprogramowania, przed rozpoczęciem projektu testowego wraz z analizą testów i projektowaniem testów.
d) Odpowiedź niepoprawna. Testy akceptacyjne można przeprowadzić, gdy produkt jest już gotowy do działania. W modelach sekwencyjnych gotowy produkt jest zazwyczaj dostarczany w późniejszej fazie cyklu wytwarzania.
e) Odpowiedź niepoprawna. Testy pielęgnacyjne przeprowadza się, gdy produkt działa i jest wdrożony, co nie ma miejsca we wczesnych fazach cyklu wytwarzania.

---

# metadata
lo: FL-2.1.4
k-level: K2
points: 1
correct: c
additional: true

## question
Które z poniższych są zaletami podejścia DevOps?

i. Szybsze wydawanie produktów i skrócenie czasu wprowadzenia ich na rynek
ii. Zwiększenie potrzeby powtarzalnych testów manualnych
iii. Stała dostępność wykonywalnego oprogramowania
iv. Zmniejszenie liczby testów regresji związanych z refaktoryzacją kodu
v. Konfiguracja środowiska automatyzacji testów jest niedroga, ponieważ wszystko jest zautomatyzowane

## answers
a) i, ii, iv to zalety.
b) iii, v to zalety.
c) i, iii to zalety.
d) ii, iv, v to zalety.

## justification
Biorąc pod uwagę:
i. Prawda. Szybsze wydawanie produktu i skrócenie czasu wprowadzenia go na rynek to zalety DevOps.
ii. Fałsz. Zazwyczaj dzięki automatyzacji testów testy manualne wymagają mniejszego nakładu pracy.
iii. Prawda. Stała dostępność wykonywalnego oprogramowania jest zaletą.
iv. Fałsz. Potrzeba więcej testów regresji.
v. Fałsz. Nie wszystko jest zautomatyzowane, a skonfigurowanie struktury automatyzacji testów jest kosztowne.

mamy:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-2.2.2
k-level: K2
points: 1
correct: b
additional: true

## question
Pracujesz jako tester przy projekcie aplikacji mobilnej do zamawiania jedzenia dla jednego z Twoich klientów. Klient przesłał Ci listę wymagań. Jedno z nich, o wysokim priorytecie, brzmi: *„Zamówienie musi być przetworzone w mniej niż 10 sekund w 95% przypadków”*. Stworzyłeś/-łaś zestaw przypadków testowych, w których złożono kilka losowych zamówień, zmierzono czas przetwarzania i sprawdzono wyniki testów pod kątem wymagań.
Jaki rodzaj testu przeprowadziłeś/-łaś?

## answers
a) Funkcjonalny, ponieważ przypadki testowe obejmują wymagania biznesowe użytkownika dla systemu.
b) Niefunkcjonalny, ponieważ przypadki testowe mierzą wydajność systemu.
c) Funkcjonalny, ponieważ przypadki testowe współdziałają z interfejsem użytkownika.
d) Białoskrzynkowy, ponieważ należy znać wewnętrzną strukturę programu, aby zmierzyć czas przetwarzania zamówienia.

## justification
a) Odpowiedź niepoprawna. Fakt, że wymagania dotyczące wydajności systemu pochodzą bezpośrednio od klienta i że wydajność jest ważna z punktu widzenia biznesowego (tj. ma wysoki priorytet) nie sprawia, że testy te są funkcjonalne, ponieważ nie sprawdzają one tego, „co” robi system, ale „jak” (tj. jak szybko przetwarzane są zamówienia).
b) Odpowiedź poprawna. Jest to przykład testowania wydajności, czyli rodzaj testowania niefunkcjonalnego.
c) Odpowiedź niepoprawna. Na podstawie scenariusza nie wiemy, czy interakcja z interfejsem użytkownika jest częścią warunków testowych. Ale nawet gdybyśmy to wiedzieli, głównym celem testów jest sprawdzenie wydajności, a nie użyteczności.
d) Odpowiedź niepoprawna. Nie musimy znać wewnętrznej struktury kodu, aby przeprowadzić testy wydajności. Testy wydajności można przeprowadzić bez wiedzy na temat tej struktury.

---

# metadata
lo: FL-2.3.1
k-level: K2
points: 1
correct: a
additional: true

## question
Strategia testów Twojej organizacji sugeruje, że po wycofaniu systemu należy przetestować migrację danych. W ramach jakiego rodzaju testów najprawdopodobniej zostanie przeprowadzona ta weryfikacja?

## answers
a) W ramach testów pielęgnacyjnych.
b) W ramach testów regresji.
c) W ramach testów niezawodności.
d) W ramach testów integracji.

## justification
a) Odpowiedź poprawna. Wycofanie systemu z eksploatacji może wymagać przetestowania migracji danych, co jest formą testowania pielęgnacyjnego.
b) Odpowiedź niepoprawna. Testy regresji sprawdzają, czy poprawka nie wpłynęła przypadkowo negatywnie na działanie innych części kodu, ale tu mowa jest o migracji danych do nowego systemu.
c) Odpowiedź niepoprawna. Testowanie niezawodności koncentruje się na dojrzałości systemu i odporności na awarie, a nie na migracji danych.
d) Odpowiedź niepoprawna. Testy integracyjne koncentrują się na interakcjach między modułami i/lub systemami, a nie na migracji danych. Nie jest to również typ testu, ale poziom testu.

---

# metadata
lo: FL-3.1.1
k-level: K1
points: 1
correct: c
additional: true

## question
Rozważ poniższą listę produktów pracy powstałych w ramach cyklu życia oprogramowania.

i. Wymagania biznesowe
ii. Harmonogram
iii. Budżet testów
iv. Kod wykonywalny strony trzeciej
v. Historyjki użytkownika i kryteria ich akceptacji

Które z nich można poddać przeglądowi?

## answers
a) Tylko i oraz iv.
b) Tylko i, ii, iii, iv.
c) Tylko i, ii, iii, v.
d) Tylko iii, iv, v.

## justification
Tylko kod wykonywalny strony trzeciej nie może być poddany przeglądowi.
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-3.1.3
k-level: K2
points: 1
correct: d
additional: true

## question
Które z poniższych stwierdzeń (i--v) są prawdziwe w odniesieniu do testów statycznych?

i. Nieprawidłowe zachowania zewnętrzne są łatwiejsze do zidentyfikowania dzięki tym testom
ii. Dzięki tym testom łatwiej wykryć rozbieżności w stosunku do norm kodowania
iii. Wykrywają awarie spowodowane defektami podczas działania oprogramowania.
iv. Celem testów jest jak najwcześniejsze wykrycie defektów.
v. Brak pokrycia krytycznych wymagań bezpieczeństwa jest łatwiejszy do znalezienia i usunięcia.

## answers
a) i, iv, v.
b) i, iii, iv.
c) ii, iii.
d) ii, iv, v.

## justification
Biorąc pod uwagę, że:
i. Zachowania te są łatwe do wykrycia podczas działania oprogramowania. W związku z tym do ich identyfikacji należy zastosować testowanie dynamiczne.
ii. Jest to przykład odstępstwa od norm, które jest typowym defektem łatwiejszym do wykrycia podczas testowania statycznego.
iii. Jeśli oprogramowanie jest uruchamiane podczas testowania, jest to testowanie dynamiczne.
iv. Jak najwcześniejsze wykrywanie defektów jest celem zarówno testowania statycznego, jak i dynamicznego.
v. Jest to przykład luk w śledzeniu powiązań podstawy testów lub pokryciu, co jest typowym defektem, który łatwiej wykryć za pomocą testowania statycznego.

A zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-3.2.2
k-level: K2
points: 1
correct: b
additional: true

## question
Które z poniższych stwierdzeń dotyczących przeglądów formalnych jest prawdziwe?

## answers
a) Niektóre przeglądy nie wymagają więcej niż jednej roli.
b) Proces przeglądu obejmuje kilka czynności.
c) Dokumentacja przeznaczona do przeglądu nie jest dystrybuowana przed spotkaniem przeglądowym, z wyjątkiem produktów pracy dla określonych typów przeglądów.
d) Defekty wykryte podczas przeglądu nie są zgłaszane, ponieważ nie zostały wykryte podczas testów dynamicznych.

## justification
a) Odpowiedź niepoprawna. We wszystkich rodzajach przeglądów występuje więcej niż jedna rola, nawet w przeglądach nieformalnych.
b) Odpowiedź poprawna. W trakcie formalnego procesu przeglądu odbywa się kilka czynności.
c) Odpowiedź niepoprawna. Dokumentacja przeznaczona do przeglądu powinna zostać rozesłana jak najwcześniej.
d) Odpowiedź niepoprawna. Defekty wykryte podczas przeglądu powinny zostać zgłoszone.

---

# metadata
lo: FL-3.2.3
k-level: K1
points: 1
correct: b
additional: true

## question
Jakie zadanie może podjąć kierownictwo podczas przeglądu formalnego?

## answers
a) Przejęcie ogólnej odpowiedzialności za przegląd.
b) Podejmowanie decyzji dotyczących zakresu przeglądu.
c) Zapewnienie skutecznego przebiegu spotkań przeglądowych i moderowanie ich w razie potrzeby.
d) Rejestrowanie informacji dotyczących przeglądu, takich jak decyzje podjęte w jego trakcie.

## justification
a) Odpowiedź niepoprawna. Jest to zadanie lidera przeglądu.
b) Odpowiedź poprawna. Jest to zadanie kierownictwa w ramach przeglądu formalnego.
c) Odpowiedź niepoprawna. Jest to zadanie moderatora.
d) Odpowiedź niepoprawna. Jest to zadanie protokolanta.

---

# metadata
lo: FL-4.2.2
k-level: K3
points: 1
correct: c
additional: true

## question
System przechowywania wina wykorzystuje urządzenie kontrolne, które mierzy temperaturę T w piwniczce (mierzoną w °C, zaokrągloną do najbliższego stopnia) i alarmuje użytkownika, jeśli odbiega ona od optymalnej wartości 12, zgodnie z następującymi zasadami:

- jeśli T = 12, system wyświetla komunikat „temperatura optymalna”
- jeśli T < 12, system wyświetla komunikat „temperatura jest zbyt niska!”
- jeśli T > 12, system wyświetla komunikat „temperatura jest zbyt wysoka!”

Chcesz użyć trójpunktowej analizy wartości brzegowych w celu zweryfikowania działania urządzenia kontrolnego. Dane wejściowe to temperatura w °C podana przez urządzenie.
Jaki jest **minimalny** zestaw danych wejściowych, który zapewnia 100% pożądanego pokrycia?

## answers
a) 11, 12, 13.
b) 10, 12, 14.
c) 10, 11, 12, 13, 14.
d) 10, 11, 13, 14.

## justification
Istnieją trzy klasy równoważności: {..., 10, 11}, {12} oraz {13, 14, ...}. Wartości brzegowe tych klas to 11, 12 i 13. W analizie wartości brzegowych w wersji trójpunktowej dla każdego brzegu należy przetestować brzeg oraz obu jego sąsiadów, więc:

- dla brzegu 11 należy przetestować wartości 10, 11, 12,
- dla brzegu 12 należy przetestować wartości 11, 12, 13,
- dla brzegu 13 należy przetestować wartości 12, 13, 14.

Łącznie należy przetestować wartości 10, 11, 12, 13 i 14, zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.3.2
k-level: K2
points: 1
correct: d
additional: true

## question
Które z poniższych stwierdzeń dotyczących testowania gałęzi jest prawdziwe?

## answers
a) Jeśli program zawiera tylko gałęzie bezwarunkowe, to można osiągnąć 100% pokrycia gałęzi bez wykonywania żadnych przypadków testowych.
b) Jeśli przypadki testowe sprawdzają wszystkie gałęzie bezwarunkowe w kodzie, osiąga się 100% pokrycia gałęzi.
c) Jeśli osiągnięto 100% pokrycia instrukcji, to osiągnięto również 100% pokrycia gałęzi.
d) Jeśli osiągnięto 100% pokrycia gałęzi, to wymuszono wszystkie wyniki decyzji w każdym wyrażeniu decyzyjnym w kodzie.

## justification
a) Odpowiedź niepoprawna. W tym przypadku nadal potrzebny jest jeden przypadek testowy, ponieważ istnieje co najmniej jedna (bezwarunkowa) gałąź, która musi zostać pokryta.
b) Odpowiedź niepoprawna. Pokrycie tylko gałęzi bezwarunkowych nie oznacza pokrycia wszystkich gałęzi warunkowych.
c) Odpowiedź niepoprawna. 100% pokrycia gałęzi oznacza 100% pokrycia instrukcji, a nie odwrotnie. Na przykład w przypadku decyzji IF bez ELSE wystarczy jeden test, aby osiągnąć 100% pokrycia instrukcji, ale osiąga się tylko 50% pokrycia gałęzi.
d) Odpowiedź poprawna. Każdy wynik decyzji odpowiada gałęzi warunkowej, więc 100% pokrycia gałęzi oznacza 100% pokrycia wyników decyzji.

---

# metadata
lo: FL-4.4.3
k-level: K2
points: 1
correct: c
additional: true

## question
Testujesz aplikację mobilną, która umożliwia klientom dostęp do ich kont bankowych i zarządzanie nimi. Uruchamiasz zestaw testów, który obejmuje ocenę każdego ekranu i każdego pola na każdym ekranie w oparciu o zestaw najlepszych praktyk dotyczących interfejsu użytkownika zaczerpnięty z popularnej książki na ten temat, maksymalizujących użyteczność takich aplikacji.
Która z poniższych opcji **najlepiej** opisuje technikę testowania, którą stosujesz?

## answers
a) Testowanie czarnoskrzynkowe.
b) Testowanie eksploracyjne.
c) Testowanie oparte na liście kontrolnej.
d) Zgadywanie błędów.

## justification
a) Odpowiedź niepoprawna. Książka zawiera ogólne wytyczne i nie jest formalnym dokumentem zawierającym wymagania, specyfikacją ani zbiorem przypadków użycia, historyjek użytkownika czy procesów biznesowych.
b) Odpowiedź niepoprawna. Chociaż listę praktyk można traktować jako zestaw kart opisu testu, bardziej przypomina ona listę warunków testowych, które należy sprawdzić.
c) Odpowiedź poprawna. Lista najlepszych praktyk dotyczących interfejsu użytkownika jest listą warunków testowych, które należy systematycznie sprawdzać.
d) Odpowiedź niepoprawna. Testy nie koncentrują się na potencjalnych awariach, ale raczej na wiedzy o tym, co jest ważne dla użytkownika pod względem użyteczności.

---

# metadata
lo: FL-4.5.1
k-level: K2
points: 1
correct: b
additional: true

## question
Które z poniższych stwierdzeń najlepiej opisuje podejście do pisania historyjek użytkownika oparte na współpracy?

## answers
a) Historyjki użytkownika są tworzone przez testerów i programistów, a następnie akceptowane przez przedstawicieli jednostek biznesowych.
b) Historyjki użytkownika są tworzone wspólnie przez przedstawicieli jednostek biznesowych, programistów i testerów.
c) Historyjki użytkownika są tworzone przez przedstawicieli jednostek biznesowych i weryfikowane przez programistów i testerów.
d) Historyjki użytkownika są tworzone w taki sposób, aby były niezależne, negocjowalne, wartościowe, możliwe do oszacowania, niewielkie i możliwe do przetestowania.

## justification
a) Odpowiedź niepoprawna. Proces tworzenia historyjek użytkownika angażuje wszystkich interesariuszy, by wypracować spójną wizję.
b) Odpowiedź poprawna. Proces tworzenia historyjek użytkownika angażuje wszystkich interesariuszy, by wypracować spójną wizję.
c) Odpowiedź niepoprawna. Proces tworzenia historyjek użytkownika angażuje wszystkich interesariuszy, by wypracować spójną wizję.
d) Odpowiedź niepoprawna. Jest to lista właściwości, które powinna posiadać każda historyjka użytkownika, a nie opis podejścia opartego na współpracy.

---

# metadata
lo: FL-5.1.1
k-level: K2
points: 1
correct: d
additional: true

## question
Rozważ następującą część planu testów: „*Testy będą przeprowadzane przy użyciu testowania modułowego i integracji modułów. Przepisy wymagają wykazania, że dla każdego modułu sklasyfikowanego jako krytyczny osiągnięte będzie 100% pokrycia gałęzi.*”
Do której części planu testów należy ta część?

## answers
a) Komunikacja.
b) Rejestr ryzyk.
c) Kontekst testowania.
d) Podejście do testów.

## justification
a) Odpowiedź niepoprawna. Ta część planu zawiera informacje na temat poziomów testów i kryteriów wyjścia, które są częścią podejścia do testów, a nie opisu komunikacji.
b) Odpowiedź niepoprawna. Ta część planu zawiera informacje na temat poziomów testów i kryteriów wyjścia, które są częścią podejścia do testów, a nie rejestru ryzyk.
c) Odpowiedź niepoprawna. Ta część planu zawiera informacje na temat poziomów testów i kryteriów wyjścia, które są częścią podejścia do testów, a nie opisu kontekstu.
d) Odpowiedź poprawna. Ta część planu zawiera informacje na temat poziomów testów i kryteriów wyjścia, które są częścią podejścia do testów.

---

# metadata
lo: FL-5.1.4
k-level: K3
points: 1
correct: b
additional: true

## question
Twój zespół używa pokera planistycznego do oszacowania nakładu pracy związanego z testowaniem nowej wymaganej funkcji. W zespole obowiązuje zasada, że jeśli nie ma czasu na osiągnięcie pełnej zgody, a różnice w wynikach są niewielkie, można zastosować zasady takie jak „zaakceptuj liczbę, która uzyskała najwięcej głosów”.
Po dwóch rundach nie osiągnięto konsensusu, więc rozpoczęto trzecią rundę. Wyniki oszacowania testów można zobaczyć w poniższej tabeli.

Szacunki członków zespołu:

| **Runda** |  |  |  |  |  |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Runda 1 | 21 | 2 | 5 | 34 | 13 | 8 | 2 |
| Runda 2 | 13 | 8 | 8 | 34 | 13 | 8 | 5 |
| Runda 3 | 13 | 8 | 13 | 13 | 13 | 13 | 8 |

Które z poniższych jest **najlepszym** przykładem kolejnego kroku?

## answers
a) Właściciel produktu musi wkroczyć do akcji i podjąć ostateczną decyzję.
b) Akceptacja 13 jako ostatecznego wyniku, ponieważ uzyskała ona najwięcej głosów.
c) Nie są potrzebne żadne dalsze działania, gdyż osiągnięto konsensus.
d) Usunąć nową funkcję z bieżącej wersji, ponieważ nie osiągnięto konsensusu.

## justification
a) Odpowiedź niepoprawna. Powinna to być aktywność zespołowa i nie powinna być podważana przez jednego członka zespołu.
b) Odpowiedź poprawna. Jeśli różnice w wynikach są niewielkie, można zastosować zasady takie jak „zaakceptuj wynik z największą liczbą głosów”.
c) Odpowiedź niepoprawna. Nie ma jeszcze konsensusu, ponieważ niektórzy twierdzą, że 13, a inni, że 8.
d) Odpowiedź niepoprawna. Funkcja nie powinna zostać usunięta tylko dlatego, że zespół nie może dojść do porozumienia w sprawie szacunku wysiłku testowego.

---

# metadata
lo: FL-5.1.6
k-level: K1
points: 1
correct: a
additional: true

## question
Które z poniższych stwierdzeń dotyczących piramidy testów jest **prawdziwe**?

## answers
a) Sugeruje przeprowadzanie większej liczby testów na niższych poziomach testów.
b) Sugeruje, że każdy test niskiego poziomu sprawdza dużą część funkcjonalności.
c) Opisuje rozkład typów testów w całym cyklu wytwarzania oprogramowania.
d) Nie ma wpływu na tworzenie testów automatycznych.

## justification
a) Odpowiedź poprawna. Piramida testów kładzie nacisk na większą liczbę testów na niższych poziomach testów.
b) Odpowiedź niepoprawna. Nie jest prawdą, że test na niższym poziomie testów sprawdza większą część funkcjonalności. Testy na niższych poziomach piramidy testów są bardziej atomowe i zorientowane na konkretną logikę, więc jest odwrotnie.
c) Odpowiedź niepoprawna. Piramida testów pokazuje, jak liczba testów jest rozłożona na poszczególnych poziomach testów.
d) Odpowiedź niepoprawna. Model piramidy testów wspiera zespół w automatyzacji testów.

---

# metadata
lo: FL-5.2.1
k-level: K1
points: 1
correct: c
additional: true

## question
Podczas analizy ryzyka zespół rozważał następujące ryzyko: „*System pozwala na zbyt wysokie rabaty dla klientów*”. Zespół oszacował wpływ ryzyka jako bardzo wysoki.
Co można powiedzieć o prawdopodobieństwie wystąpienia tego ryzyka?

## answers
a) Jest ono również bardzo wysokie; wysoki wpływ ryzyka zawsze oznacza wysokie prawdopodobieństwo wystąpienia ryzyka.
b) Jest bardzo niskie; wysoki wpływ ryzyka zawsze oznacza niskie prawdopodobieństwo wystąpienia ryzyka.
c) Nie można nic powiedzieć o prawdopodobieństwie wystąpienia ryzyka; wpływ ryzyka i prawdopodobieństwo wystąpienia ryzyka są niezależne.
d) Prawdopodobieństwo wystąpienia ryzyka nie jest ważne przy tak wysokim wpływie ryzyka; nie ma potrzeby jego definiowania.

## justification
a) Odpowiedź niepoprawna. Wpływ ryzyka i prawdopodobieństwo wystąpienia ryzyka są od siebie niezależne.
b) Odpowiedź niepoprawna. Wpływ ryzyka i prawdopodobieństwo wystąpienia ryzyka są od siebie niezależne.
c) Odpowiedź poprawna. Wpływ ryzyka i prawdopodobieństwo wystąpienia ryzyka są od siebie niezależne.
d) Odpowiedź niepoprawna. Potrzebujemy obu czynników, aby obliczyć poziom ryzyka.

---

# metadata
lo: FL-5.2.2
k-level: K2
points: 1
correct: a
additional: true

## question
Poniższa lista zawiera ryzyka, które zostały zidentyfikowane dla nowego produktu oprogramowania, który ma zostać opracowany:

i. Kierownictwo przenosi dwóch doświadczonych testerów do innego projektu
ii. System nie spełnia norm bezpieczeństwa
iii. Czas reakcji systemu przekracza wymagania użytkowników
iv. Interesariusze mają niejasne oczekiwania
v. Osoby niepełnosprawne mają problemy podczas korzystania z systemu

Które z nich są ryzykami projektowymi?

## answers
a) i, iv.
b) iv, v.
c) i, iii.
d) ii, v.

## justification
Biorąc pod uwagę, że:
i. Jest to ryzyko projektowe
ii. Jest to ryzyko produktowe
iii. Jest to ryzyko produktowe
iv. Jest to ryzyko projektowe
v. Jest to ryzyko produktowe

mamy:
a) Odpowiedź poprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.2.3
k-level: K2
points: 1
correct: d
additional: true

## question
Które z poniższych stanowi przykład wpływu analizy ryzyka produktowego na dokładność i zakres testowania?

## answers
a) Kierownik testów codziennie monitoruje i raportuje poziom wszystkich znanych ryzyk, aby interesariusze mogli podjąć świadomą decyzję dotyczącą daty wydania.
b) Jednym ze zidentyfikowanych ryzyk był „*Brak wsparcia dla otwartych baz danych*”, więc zespół zdecydował się zintegrować system z otwartą bazą danych.
c) Podczas ilościowej analizy ryzyka zespół oszacował całkowity poziom wszystkich zidentyfikowanych ryzyk i zgłosił go jako całkowite ryzyko rezydualne przed testowaniem.
d) Ocena ryzyka wykazała bardzo wysoki poziom ryzyk związanych z wydajnością, dlatego zdecydowano się przeprowadzić wczesne, szczegółowe testy wydajności.

## justification
a) Odpowiedź niepoprawna. Jest to przykład działania związanego z monitorowaniem ryzyka, a nie z analizą ryzyka.
b) Odpowiedź niepoprawna. Jest to przykład decyzji architektonicznej, niezwiązanej z testowaniem.
c) Odpowiedź niepoprawna. Jest to przykład przeprowadzenia ilościowej analizy ryzyka i nie ma związku z dokładnością ani zakresem testowania.
d) Odpowiedź poprawna. Pokazuje to, jak analiza ryzyka wpływa na dokładność testowania (tj. poziom szczegółowości testów).

---

# metadata
lo: FL-5.3.1
k-level: K1
points: 1
correct: a, d
additional: true

## question
Które **dwie** z poniższych opcji są powszechnie stosowanymi metrykami służącymi do raportowania poziomu jakości przedmiotu testów?

## answers
a) Liczba defektów wykrytych podczas testowania systemu.
b) Całkowity nakład pracy nad projektem testów podzielony przez liczbę zaprojektowanych przypadków testowych.
c) Liczba wykonanych procedur testowych.
d) Liczba wykrytych defektów podzielona przez rozmiar produktu pracy.
e) Czas potrzebny do usunięcia defektu.

## justification
a) Odpowiedź poprawna. Liczba wykrytych defektów jest związana z jakością przedmiotu testów.
b) Odpowiedź niepoprawna. Jest to miara efektywności testowania, a nie jakości przedmiotu testów.
c) Odpowiedź niepoprawna. Liczba wykonanych przypadków testowych nie mówi nam nic o jakości; wyniki testów mogą to zrobić.
d) Odpowiedź poprawna. Gęstość defektów jest związana z jakością przedmiotu testów.
e) Odpowiedź niepoprawna. Czas naprawy jest metryką procesu, a nie jakości produktu.

---

# metadata
lo: FL-5.3.2
k-level: K2
points: 1
correct: b
additional: true

## question
Która z poniższych informacji zawartych w raporcie o postępie testów jest **najmniej** przydatna dla przedstawicieli jednostek biznesowych?

## answers
a) Przeszkody w testowaniu.
b) Osiągnięte pokrycie gałęzi.
c) Postęp testów.
d) Nowe ryzyka w cyklu testowym.

## justification
a) Odpowiedź niepoprawna. Przeszkody w testowaniu mogą mieć charakter ogólny i być związane z działalnością biznesową, dlatego jest to ważna informacja dla interesariuszy biznesowych.
b) Odpowiedź poprawna. Testowanie gałęzi jest techniczną metryką stosowaną przez programistów i technicznych analityków testów. Informacja ta nie jest interesująca dla przedstawicieli jednostek biznesowych.
c) Odpowiedź niepoprawna. Postęp testów jest związany z projektem, więc informacja na jego temat może być przydatna dla przedstawicieli jednostek biznesowych.
d) Odpowiedź niepoprawna. Ryzyka mają wpływ na jakość produktu, więc informacja na ich temat może być przydatna dla przedstawicieli jednostek biznesowych.
