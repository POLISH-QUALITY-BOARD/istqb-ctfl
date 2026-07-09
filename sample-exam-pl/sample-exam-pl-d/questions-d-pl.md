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
v. Przypapki testowe.

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
