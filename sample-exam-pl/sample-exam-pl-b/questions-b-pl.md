# metadata
lo: FL-1.2.1
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń jest przykładem tego, dlaczego testowanie jest konieczne?

## answers
a) Testowanie dynamiczne zwiększa jakość, wywołując awarie przedmiotów testów w sposób, który nigdy nie byłby możliwy do osiągnięcia przez użytkowników.  
b) Testowanie statyczne jest wykorzystywane przez programistów do identyfikowania defektów w kodzie wcześniej niż jest to możliwe do osiągnięcia w przypadku testowania dynamicznego.  
c) Analiza statyczna dostarcza klientom dowodów, że elementy systemu, które nie generują żadnych wyników, nadają się do wydania.  
d) Przeglądy zwiększają jakość specyfikacji wymagań i prowadzą do zmniejszenia liczby zmian wymaganych w pochodnych produktach pracy.

## justification
a) Odpowiedź niepoprawna. Można użyć testowania dynamicznego tak, żeby przedmiot testów uległ awarii w sposób, który nigdy nie byłby możliwy do osiągnięcia dla użytkowników, na przykład przez wstrzyknięcie usterki. Ale jeśli awaria nigdy nie może się zdarzyć u rzeczywistych użytkowników, to jej wykrycie nie jest zbyt przydatne, bo testy mają na celu poprawę produktu pracy dla użytkowników. Poświęcanie czasu na testowanie awarii, które nie mogą wystąpić u rzeczywistych użytkowników, nie jest efektywnym wykorzystaniem czasu testera.  
b) Odpowiedź niepoprawna. Testowanie statyczne w formie analizy statycznej jest wykorzystywane przez programistów do identyfikacji defektów w kodzie wcześniej niż można to osiągnąć za pomocą testowania dynamicznego. Należy jednak pamiętać, że testowanie statyczne (i analiza statyczna) służy do wykrywania defektów, a nie awarii, które są wykrywane za pomocą testowania dynamicznego. Dlatego też użycie terminu „awarie" sprawia, że jest to nieprawidłowa odpowiedź.  
c) Odpowiedź niepoprawna. Analiza statyczna bezpośrednio wykrywa defekty w kodzie i zazwyczaj jest to informacja dla programisty, a nie dla klienta.  
d) Odpowiedź poprawna. Przeglądy są formą testowania statycznego, które można stosować od samego początku cyklu wytwarzania oprogramowania i służą do wykrywania defektów, które można usunąć, zanim kolejne czynności związane z rozwojem oprogramowania spowodują stratę czasu poprzez implementację wadliwych wymagań. Jeśli defekty nie zostaną wykryte i usunięte na wczesnym etapie, to gdy zostaną wykryte w pochodnych produktach pracy, takich jak projekt i kod, wymagania będą musiały zostać zmienione.

---

# metadata
lo: FL-1.2.2
k-level: K2
points: 1
correct: b

## question
Które z poniższych stwierdzeń dotyczących zapewnienia jakości (QA) i/lub kontroli jakości (QC) jest poprawne?

## answers
a) QA jest przeprowadzane w ramach testowania.
b) Testowanie jest przeprowadzane w ramach QC.
c) Testowanie jest innym terminem określającym QC.
d) Testowanie jest przeprowadzane w ramach QA.

## justification
a) Odpowiedź niepoprawna. Zapewnienie jakości koncentruje się na doskonaleniu i wdrażaniu procesów, stosując podejście zapobiegawcze w celu uniknięcia błędów i defektów, podczas gdy testowanie jest formułą kontroli jakości stosowaną do wykrywania defektów.
b) Odpowiedź poprawna. Kontrola jakości ma na celu osiągnięcie odpowiedniego poziomu jakości poprzez skupienie się na identyfikacji i usuwaniu defektów w produkcie. Testowanie jest istotną częścią kontroli jakości i pomaga wykrywać te defekty.
c) Odpowiedź niepoprawna. Chociaż testowanie stanowi istotną część kontroli jakości i pomaga wykrywać defekty, pojęcia te nie są tożsame. Istnieją inne techniki (niezwiązane z testowaniem) stosowane w kontroli jakości. Obejmują one formalne metody, takie jak weryfikacja modelowa, dowodzenie poprawności, a także symulacje i prototypowanie.
d) Odpowiedź niepoprawna. Zapewnienie jakości koncentruje się na doskonaleniu i wdrażaniu procesów, stosując podejście zapobiegawcze w celu uniknięcia błędów i defektów, podczas gdy testowanie jest formułą kontroli jakości stosowaną do wykrywania defektów.

---

# metadata
lo: FL-1.3.1
k-level: K2
points: 1
correct: d

## question
Jedna z zasad testowania mówi, że testowanie gruntowne jest niemożliwe.
Które z poniższych jest przykładem zastosowania tej zasady w praktyce?

## answers
a) Tworzenie przypadków testowych obejmujących wszystkie możliwe wyniki.
b) Dokumentowanie wszystkich możliwych wariantów danych wejściowych do testów i ustalanie ich priorytetów w oparciu o ich znaczenie.
c) Rozpoczęcie testowania jak najwcześniej, od przeglądów i innych statycznych metod testowania.
d) Wykorzystanie podziału na klasy równoważności i analizy wartości brzegowych do generowania przypadków testowych.

## justification
a) Odpowiedź niepoprawna. Zasada ta stanowi, że nie jest możliwe przetestowanie wszystkiego, z wyjątkiem przypadków trywialnych. Przetestowanie wszystkiego wymagałoby przetestowania wszystkich możliwych wariantów danych wejściowych we wszystkich możliwych okolicznościach, co jest generalnie niewykonalne, ponieważ istnieje praktycznie nieskończona liczba możliwości. Testowanie wszystkich możliwych oczekiwanych wyników nie rozwiąże tego problemu, ponieważ związek między danymi wejściowymi a oczekiwanymi wynikami może być różny dla każdego przedmiotu testów.
b) Odpowiedź niepoprawna. Zasada ta mówi, że nie jest możliwe przetestowanie wszystkich możliwych wariantów danych wejściowych we wszystkich możliwych okolicznościach. Wynika to z faktu, że w przypadku systemów nietrywialnych liczba ta jest praktycznie nieskończona. Dlatego w praktyce dokumentowanie wszystkich możliwych wariantów danych wejściowych jest niepraktyczne, a wręcz niewykonalne, ponieważ wymagałoby to nieskończenie dużo czasu.
c) Odpowiedź niepoprawna. Rozpoczęcie testowania jak najwcześniej począwszy od przeglądów, aż po inne statyczne metody testowania, nie rozwiąże problemu zbyt dużej liczby możliwych przypadków testowych. Zasada „wczesne testowanie oszczędza czas i pieniądze" dotyczy wczesnego usuwania defektów, aby zapobiec pojawieniu się kolejnych defektów w pochodnych produktach pracy, zmniejszając w ten sposób koszty i prawdopodobieństwo awarii.
d) Odpowiedź poprawna. Wykorzystanie podziału na klasy równoważności i analizy wartości brzegowych do generowania przypadków testowych jest jednym ze sposobów realizacji tej zasady, ponieważ techniki te zapewniają systematyczny sposób uzyskania skończonego podzbioru wszystkich możliwych przypadków testowych.

---

# metadata
lo: FL-1.4.1
k-level: K2
points: 1
correct: a

## question
Która czynność testowa obejmuje pracę z wymaganiami dotyczącymi danych testowych, warunkami testowymi, wymaganiami dotyczącymi środowiska testowego i przypadkami testowymi?

## answers
a) Projektowanie testów.
b) Wykonywanie testów.
c) Analiza testów.
d) Implementacja testów.

## justification
a) Odpowiedź poprawna. Projektowanie testów obejmuje wykorzystanie warunków testowych do tworzenia przypadków testowych i innych niezbędnych testaliów, takich jak wymagania dotyczące danych testowych i karty opisu testu do testów eksploracyjnych. Określane są również wymagania dotyczące środowiska testowego, w tym niezbędna infrastruktura i narzędzia.
b) Odpowiedź niepoprawna. Wykonywanie testów obejmuje wykonanie przypadków testowych (w ramach procedur testowych), jednak nie obejmuje bezpośrednio innych testaliów wymienionych w pytaniu, takich jak wymagania dotyczące danych testowych, wymagania dotyczące środowiska testowego i warunki testowe.
c) Odpowiedź niepoprawna. Analiza testów służy do identyfikacji funkcji, które wymagają przetestowania. W wyniku analizy podstawy testów definiuje się warunki testowe, które są następnie uszeregowane według priorytetów wraz powiązanymi ryzykami. Chociaż czynność ta obejmuje pracę z warunkami testowymi, nie obejmuje innych testaliów wymienionych w pytaniu.
d) Odpowiedź niepoprawna. Implementacja testów obejmuje generowanie procedur testowych, takich jak manualne i automatyczne skrypty testowe, które są tworzone na podstawie przypadków testowych i mogą być łączone w zestawy testowe. Chociaż działanie to obejmuje pracę z przypadkami testowymi i może wykorzystywać wymagania dotyczące danych testowych i środowiska testowego, nie obejmuje ono warunków testowych.

---

# metadata
lo: FL-1.4.2
k-level: K2
points: 1
correct: c

## question
Który z poniższych czynników ma największy wpływ na sposób przeprowadzania testów dla danego przedmiotu testów?

## answers
a) Przeciętny poziom doświadczenia zespołu marketingowego organizacji.
b) Świadomość użytkowników, że nowy system jest tworzony z myślą o nich.
c) Liczba lat doświadczenia członków zespołu testowego.
d) Struktura organizacji użytkowników końcowych komercyjnej aplikacji do strumieniowego przesyłania muzyki.

## justification
a) Odpowiedź niepoprawna. Zespół marketingowy organizacji prawdopodobnie nie przeprowadza wielu testów, więc średni poziom doświadczenia jego członków prawdopodobnie nie ma wpływu na sposób przeprowadzania testów.
b) Odpowiedź niepoprawna. Poziom wiedzy użytkowników, dla których tworzony jest nowy system, prawdopodobnie nie będzie miał wpływu na sposób przeprowadzania testów.
c) Odpowiedź poprawna. Liczba lat doświadczenia członków zespołu testowego ds. testowania wydajności pomoże określić umiejętności i wiedzę (np. na temat różnych narzędzi i rodzajów defektów), które członkowie zespołu będą stosować podczas testowania.
d) Odpowiedź niepoprawna. Struktura organizacji użytkownika końcowego może mieć niewielki wpływ na sposób przeprowadzania testów.

---
