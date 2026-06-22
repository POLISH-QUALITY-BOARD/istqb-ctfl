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
