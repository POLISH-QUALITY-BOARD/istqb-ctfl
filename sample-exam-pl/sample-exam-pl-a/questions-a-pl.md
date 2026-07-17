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
| **TC1** | 91 | bardzo dobry |
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

