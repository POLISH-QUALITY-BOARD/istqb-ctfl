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

# metadata
lo: FL-1.4.4
k-level: K2
points: 1
correct: b

## question
Które z poniższych stwierdzeń jest **poprawnym** przykładem zalety śledzenia powiązań?

## answers
a) Śledzenie zaliczonych przypadków testowych do łagodzonych ryzyk stanowi metodę określenia poziomu ryzyka rezydualnego (resztkowego).
b) Śledzenie wyników testów do wymagań użytkowników umożliwia pomiar postępów projektu w odniesieniu do celów biznesowych.
c) Śledzenie niezaliczonych przypadków testowych do testerów będących ich autorami pozwala określić poziom umiejętności testerów.
d) Śledzenie zdefiniowanych warunków testowych do zidentyfikowanych ryzyk pozwala określić, które ryzyka warto przetestować.

## justification
a) Odpowiedź niepoprawna. Śledzenie powiązań pomiędzy łagodzonymi ryzykami a zaliczonymi przypadkami testowymi dostarcza niewiele informacji, ponieważ aby ryzyko zostało złagodzone (poprzez testowanie), musiałyby istnieć odpowiadające mu zaliczone przypadki testowe. Aby więc móc ocenić ryzyko resztkowe, konieczne jest śledzenie powiązań między *wszystkimi* ryzykami a wynikami testów, tak, aby ryzyka, które nie mają odpowiadających im zaliczonych testów, mogły zostać zidentyfikowane jako ryzyko resztkowe.
b) Odpowiedź poprawna. Śledzenie powiązań między wymaganiami użytkownika a wynikami testów wskazuje, które wymagania użytkownika zostały przetestowane, a tym samym zapewnia środek pomiaru postępu projektu (w kontekście testowania) w odniesieniu do celów biznesowych.
c) Odpowiedź niepoprawna. Nie jest jasne, czy niezaliczone przypadki testowe dostarczają więcej informacji na temat umiejętności testera niż zaliczone przypadki testowe. Częściowo zależy to od celu testu (np. budowanie zaufania lub powodowanie awarii). Ponadto takie mierzenie testerów na podstawie wyników przypadków testowych może przynosić efekty odwrotne do zamierzonych, ponieważ może spowodować, że testerzy będą optymalizować swoje testy w oparciu o tę metrykę, a nie o cel testu.
d) Odpowiedź niepoprawna. Śledzenie powiązań między zidentyfikowanymi ryzykami a zidentyfikowanymi warunkami testowymi stanowi środek umożliwiający określenie, które dalsze warunki testowe należy zidentyfikować. Określenie, które ryzyka warto testować, stanowi część zarządzania ryzykiem, a w szczególności dotyczy łagodzenia ryzyka.

---

# metadata
lo: FL-1.5.1
k-level: K2
points: 1
correct: b

## question
Które z poniższych jest **najlepszym** przykładem wykorzystania przez testera ogólnych umiejętności podczas testowania?

## answers
a) Głęboka wiedza testera na temat różnych gier komputerowych sprawiła, że dobrze porozumiewał się z jednym z programistów, który również interesował się grami.
b) Tester był byłym pilotem i lepiej rozumiał kryteria akceptacji systemu sterowania helikopterem.
c) Tester pracował wcześniej jako programista i wykorzystał swoje umiejętności w tej dziedzinie, aby lepiej komunikować się z analitykami biznesowymi.
d) Tester bardzo uważał, aby nie popełnić błędów podczas metodycznego generowania przypadków testowych przed rozpoczęciem sesji testów eksploracyjnych.

## justification
a) Odpowiedź niepoprawna. Silne umiejętności komunikacyjne, aktywne słuchanie i umiejętność pracy w zespole umożliwiają testerowi skuteczną interakcję ze wszystkimi interesariuszami, jednak dogłębna znajomość różnych gier komputerowych, która pozwoliła testerowi dobrze porozumieć się z jednym z programistów, nie jest przykładem umiejętności ogólnej przydatnej dla testerów.
b) Odpowiedź poprawna. Wiedza dziedzinowa, którą można wykorzystać do zrozumienia i komunikowania się z użytkownikami końcowymi i przedstawicielami jednostek biznesowych, jest jedną z ważnych, ogólnych umiejętności wymaganych od testerów. Tester z doświadczeniem jako pilot byłby w stanie lepiej ocenić kryteria akceptacji systemu sterowania helikopterem.
c) Odpowiedź niepoprawna. Chociaż umiejętność programowania można uznać za wiedzę techniczną, która może zwiększyć wydajność podczas korzystania z niektórych narzędzi testowych, jest mało prawdopodobne, aby umiejętności te poprawiły komunikację z analitykami biznesowymi.
d) Odpowiedź niepoprawna. Chociaż dokładność, dbałość o szczegóły, ciekawość i metodyczne podejście do identyfikowania trudnych do wykrycia defektów są przydatnymi umiejętnościami ogólnymi dla testerów, wątpliwe jest, aby generowali oni przypadki testowe przed rozpoczęciem testów eksploracyjnych. Wynika to z faktu, że jedną z głównych zasad testów eksploracyjnych jest generowanie przypadków testowych podczas testowania, a nie ich wcześniejsze definiowanie w skryptach.

---

# metadata
lo: FL-1.5.2
k-level: K1
points: 1
correct: d

## question
Które z poniższych stwierdzeń jest zaletą podejścia „cały zespół”?

## answers
a) Pozwala członkom zespołu pełnić dowolną rolę w dowolnym momencie.
b) Wymaga tylko jednego zespołu do wsparcia całego projektu rozwojowego.
c) Włącza przedstawicieli jednostek biznesowych do tego samego zespołu, co programistów.
d) Generuje w zespole synergię, która przynosi korzyści całemu projektowi.

## justification
a) Odpowiedź niepoprawna. Podejście „cały zespół” pozwala każdemu członkowi zespołu posiadającemu wymagane umiejętności i wiedzę podjąć się wykonania dowolnego zadania, jednak nie oznacza to, że członkowie zespołu mogą w dowolnym momencie podjąć się dowolnej roli. Zazwyczaj podejmują się oni tylko tych ról, w których są kompetentni, i nie ma sugestii, że każdy członek zespołu może pełnić każdą rolę.
b) Odpowiedź niepoprawna. Podejście „cały zespół” odnosi się do sposobu pracy pojedynczego zespołu (zazwyczaj w zwinnym wytwarzaniu oprogramowania); nie obejmuje ono sposobu pracy wielu zespołów nad większymi projektami i nie sugeruje, że do realizacji całego projektu potrzebny jest tylko jeden „cały” zespół.
c) Odpowiedź niepoprawna. Podejście „cały zespół” nie zakłada, że każdy członek zespołu będzie zaangażowany w każdą ważną decyzję. Na przykład nie ma potrzeby, aby przedstawiciel jednostki biznesowej (tj. właściciel produktu) był zaangażowany w każdą decyzję techniczną, która nie ma wpływu na wyniki biznesowe, a wdrożenie takiego podejścia niepotrzebnie spowolniłoby postępy zespołu.
d) Odpowiedź poprawna. Wykorzystując w najbardziej efektywny sposób różnorodne umiejętności każdego członka zespołu, podejście „cały zespół” sprzyja doskonałej dynamice zespołu, promuje solidną komunikację i współpracę oraz generuje synergię, która przynosi korzyści całemu projektowi.

---

# metadata
lo: FL-2.1.1
k-level: K2
points: 1
correct: b

## question
Które z poniższych stwierdzeń dotyczących cyklu wytwarzania oprogramowania jest **poprawne**?

## answers
a) W przypadku stosowania zwinnego wytwarzania oprogramowania automatyzacja testów systemowych zastępuje konieczność przeprowadzania testów regresji.
b) W przypadku stosowania sekwencyjnego modelu wytwarzania oprogramowania testowanie dynamiczne jest zazwyczaj ograniczone do późniejszych etapów cyklu wytwarzania.
c) W przypadku stosowania iteracyjnego modelu wytwarzania oprogramowania testowanie modułowe jest zazwyczaj wykonywane manualnie przez programistów.
d) W przypadku stosowania przyrostowego modelu wytwarzania oprogramowania testowanie statyczne jest przeprowadzane we wczesnych przyrostach, a dynamiczne w późniejszych.

## justification
a) Odpowiedź niepoprawna. W zwinnym wytwarzaniu oprogramowania wyniki są generowane w każdej iteracji, a częste dostarczanie przyrostów wymaga szeroko zakrojonych testów regresji. Chociaż niektóre (lub wszystkie) z tych testów regresji mogą być zautomatyzowane, testy regresji (zautomatyzowane lub nie) nie mogą być zastąpione automatyzacją testów systemowych.
b) Odpowiedź poprawna. Jeśli stosowany jest sekwencyjny model wytwarzania, to na wczesnym etapie cyklu wytwarzania oprogramowania nie ma kodu dostępnego do wykonania, więc w tym czasie przeprowadza się testy statyczne (np. przeglądy). W późniejszych etapach, gdy kod jest dostępny do wykonania, możliwe jest przeprowadzenie testowania dynamicznego. Należy jednak pamiętać, że przygotowania do testów dynamicznych często mają miejsce na wczesnym etapie cyklu wytwarzania oprogramowania.
c) Odpowiedź niepoprawna. Jeśli stosowany jest iteracyjny model wytwarzania, taki jak zwinne wytwarzanie oprogramowania, testy modułowe mogą być wykorzystywane do testów regresji dla każdej iteracji. W takim przypadku istnieje silny argument za automatyzacją tych testów, które będą musiały być wykonywane często, i jest mało prawdopodobne, aby istniał poważny argument za manualnym wykonywaniem tych testów przez programistów.
d) Odpowiedź niepoprawna. W większości przyrostowych modeli wytwarzania wyniki są tworzone w każdym przyroście, co wymaga zarówno testów statycznych, jak i dynamicznych na wszystkich poziomach testów dla każdego dostarczonego przyrostu.

---

# metadata
lo: FL-2.1.2
k-level: K1
points: 1
correct: b

## question
Które z poniższych jest dobrą praktyką testowania, która ma zastosowanie we wszystkich cyklach wytwarzania oprogramowania?

## answers
a) Testerzy powinni przeglądać produkty pracy jako część kolejnej fazy wytwórczej.
b) Testerzy powinni przeglądać produkty pracy, gdy tylko dostępne są ich wersje robocze.
c) Testerzy powinni przeglądać produkty pracy przed rozpoczęciem analizy i projektowania testów.
d) Testerzy powinni dokonywać przeglądu produktów pracy natychmiast po ich opublikowaniu.

## justification
a) Odpowiedź niepoprawna. Testerzy powinni sprawdzać produkty pracy, gdy tylko dostępne są ich wersje robocze, aby umożliwić wczesne testowanie w ramach podejścia „przesunięcie w lewo”. Jeśli czekaliby do następnej fazy wytwarzania, mogłoby to spowodować rozpoczęcie niepotrzebnych prac rozwojowych (i testowych) nad niesprawdzonymi, wadliwymi produktami pracy.
b) Odpowiedź poprawna. Testerzy powinni przeglądać produkty pracy, gdy tylko dostępne są ich wersje robocze, aby umożliwić wczesne testowanie w ramach podejścia „przesunięcie w lewo”.
c) Odpowiedź niepoprawna. Testerzy zazwyczaj sprawdzają produkty pracy, które stanowią podstawę testów, w ramach analizy testów, a nie przed analizą testów i projektowaniem testów.
d) Odpowiedź niepoprawna. Testerzy powinni sprawdzać produkty pracy, gdy tylko dostępne są ich wersje robocze, aby umożliwić wczesne testowanie w ramach podejścia „przesunięcie w lewo”. Czekanie do momentu ich opublikowania oznacza, że defekty, które mogłyby zostać wykryte podczas sprawdzania przez testerów, znajdą się w opublikowanym dokumencie.

---

# metadata
lo: FL-2.1.3
k-level: K1
points: 1
correct: a

## question
Które z poniższych jest przykładem podejścia „najpierw test”?

## answers
a) Wytwarzanie sterowane testami.
b) Wytwarzanie sterowane pokryciem.
c) Wytwarzanie sterowane jakością.
d) Wytwarzanie sterowane funkcjami.

## justification
a) Odpowiedź poprawna. Wytwarzanie sterowane testami (TDD) jest dobrze znanym przykładem podejścia „najpierw test”.
b) Odpowiedź niepoprawna. Wytwarzanie sterowane pokryciem nie jest poprawnym przykładem podejścia „najpierw test”.
c) Odpowiedź niepoprawna. Wytwarzanie sterowane jakością nie jest poprawnym przykładem podejścia „najpierw test”.
d) Odpowiedź niepoprawna. Wytwarzanie sterowane funkcjami (FDD) nie jest przykładem podejścia „najpierw test”, ale jest metodologią zwinnego programowania oprogramowania opartą na dostarczaniu funkcji (w przeciwieństwie do historyjek użytkownika np. w Scrum).

---

# metadata
lo: FL-2.1.4
k-level: K2
points: 1
correct: b

## question
Które z poniższych stwierdzeń dotyczących DevOps jest **poprawne**?

## answers
a) Aby przyspieszyć wydawanie nowych wersji, stosuje się ciągłą integrację, która zachęca programistów do szybkiego przesyłania kodu bez konieczności przeprowadzania testów modułowych.
b) Aby móc częściej aktualizować i wydawać systemy, konieczne jest przeprowadzenie wielu automatycznych testów regresji w celu zmniejszenia ryzyka regresji.
c) Aby traktować programistów i pracowników działu operacyjnego na równi, testerzy poświęcają więcej uwagi testowaniu wdrożeń dokonywanych przez dział operacyjny, stosując podejście „*shift-right*”.
d) Aby zwiększyć synergię między testerami, programistami i działem operacyjnym, testowanie musi stać się w pełni zautomatyzowane, bez testów manualnych.

## justification
a) Odpowiedź niepoprawna. DevOps usprawnia testowanie na kilka sposobów, np. poprzez zapewnienie szybkiej informacji zwrotnej na temat jakości kodu, zautomatyzowane testy regresji, które minimalizują ryzyko regresji, oraz promowanie podejścia „przesunięcie w lewo” poprzez dostarczanie wysokiej jakości kodu i testów modułowych. Jest to w dużej mierze zapewnione poprzez mechanizm ciągłej integracji, w ramach którego programiści dostarczają testy modułowe wraz z nowym kodem, które muszą zostać zaliczone, aby kod został dopuszczony do kompilacji. Dlatego programiści muszą przeprowadzić testy modułowe.
b) Odpowiedź poprawna. DevOps usprawnia testowanie na kilka sposobów, np. poprzez zapewnienie szybkiej informacji zwrotnej na temat jakości kodu, zautomatyzowane testy regresji, które minimalizują ryzyko regresji, oraz promowanie podejścia „przesunięcie w lewo” poprzez przesyłanie wysokiej jakości kodu i testy modułowe.
c) Odpowiedź niepoprawna. DevOps usprawnia testowanie na kilka sposobów, np. poprzez zapewnienie szybkiej informacji zwrotnej na temat jakości kodu, zautomatyzowane testy regresji, które minimalizują ryzyko regresji, oraz promowanie podejścia „przesunięcie w lewo” poprzez dostarczanie wysokiej jakości kodu i testy modułowe. Testerzy nie próbują traktować programistów i operatorów na równi, poświęcając więcej czasu na testowanie wersji, chociaż podejście „*shift-right*” do testowania (testowanie w środowisku produkcyjnym) może być z powodzeniem stosowane.
d) Odpowiedź niepoprawna. Zautomatyzowane procesy, takie jak ciągła integracja/ciągłe dostarczanie (CI/CD) w DevOps, ułatwiają stabilne środowiska testowe i zmniejszają potrzebę testowania manualnego, jednak istnieje ryzyko przeoczenia znaczenia testowania manualnego, zwłaszcza z perspektywy użytkownika.

---

# metadata
lo: FL-2.2.1
k-level: K2
points: 1
correct: a

## question
Które z poniższych działań będzie **najprawdopodobniej** wykonane w ramach testowania systemowego?

## answers
a) Testowanie zabezpieczeń systemu zarządzania kredytami przez niezależny zespół testowy.
b) Testowanie interfejsu systemu wymiany walut z zewnętrznym systemem bankowym.
c) Testowanie beta systemu zdalnego nauczania przeprowadzane przez twórców oprogramowania edukacyjnego.
d) Testowanie interakcji między interfejsem użytkownika a bazą danych systemu zarządzania zasobami ludzkimi.

## justification
a) Odpowiedź poprawna. Testowanie systemowe bada zachowanie i możliwości całego systemu i obejmuje testowanie niefunkcjonalne charakterystyk jakościowych, w tym testowanie zabezpieczeń. Ten rodzaj testowania jest często wykonywany przez niezależny zespół testowy w oparciu o specyfikację systemu.
b) Odpowiedź niepoprawna. Testowanie integracyjne systemów bada interfejsy z innymi systemami i usługami zewnętrznymi.
c) Odpowiedź niepoprawna. Testowanie beta to rodzaj testowania akceptacyjnego przeprowadzanego w zewnętrznej lokalizacji przez osoby spoza organizacji zajmującej się wytwarzaniem.
d) Odpowiedź niepoprawna. Testowanie integracyjne modułów obejmuje testowanie interfejsów i interakcji między modułami systemu, takimi jak interfejs użytkownika i baza danych.

---

# metadata
lo: FL-2.2.3
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń jest **prawdziwe**?

## answers
a) W miarę postępu projektu liczba testów regresji wzrasta, natomiast liczba testów potwierdzających maleje.
b) Testy regresji są tworzone i uruchamiane, gdy przedmiot testów jest naprawiany, natomiast testy potwierdzające są uruchamiane za każdym razem, gdy przedmiot testów jest ulepszany.
c) Testy regresji mają na celu sprawdzenie, czy środowisko operacyjne pozostaje niezmienione, natomiast testy potwierdzające mają na celu sprawdzenie zmian w przedmiocie testów.
d) Testy regresji dotyczą niekorzystnych skutków w niezmienionym kodzie, natomiast testy potwierdzające dotyczą testowania zmienionego kodu.

## justification
a) Odpowiedź niepoprawna. Liczba testów regresji rośnie wraz z postępem projektu, ponieważ nowe testy regresji są zazwyczaj wymagane w miarę wprowadzania zmian w systemie. Podobnie liczba testów potwierdzających również zazwyczaj rośnie wraz z postępem projektu, ponieważ nowe testy potwierdzające są potrzebne dla każdej poprawki wprowadzonej w systemie.
b) Odpowiedź niepoprawna. Jest odwrotnie. Testy potwierdzające są tworzone i uruchamiane po naprawieniu przedmiotu testów, a testy regresji są (w idealnym przypadku) uruchamiane za każdym razem, gdy przedmiot testów jest ulepszany (zmieniany).
c) Odpowiedź niepoprawna. Testy potwierdzające sprawdzają, czy defekt został skutecznie usunięty, a zatem dotyczą testowania zmian w przedmiocie testów. Testy regresji zapewniają natomiast, że zmiany (w tym zmiany w środowisku operacyjnym) nie mają negatywnego wpływu na niezmienione oprogramowanie, a zatem nie sprawdzają, czy środowisko operacyjne pozostało niezmienione.
d) Odpowiedź poprawna. Testy regresji zapewniają, że zmiany nie mają negatywnego wpływu na niezmienione oprogramowanie. Testy potwierdzające sprawdzają, czy defekt został usunięty, a więc dotyczą zmienionego kodu.

---

# metadata
lo: FL-3.1.3
k-level: K2
points: 1
correct: b

## question
Które z poniższych jest przykładem defektu, który można wykryć za pomocą testów statycznych, ale **nie** za pomocą testów dynamicznych?

## answers
a) Brak użyteczności zapewnianej przez interfejs użytkownika.
b) Kod, do którego nie prowadzi żadna ścieżka.
c) Słabe czasy odpowiedzi według większości użytkowników.
d) Wymagane funkcje, które nie zostały zaimplementowane w kodzie.

## justification
a) Odpowiedź niepoprawna. Brak użyteczności interfejsu użytkownika można wykryć poprzez przegląd przy użyciu odpowiedniej listy kontrolnej, ale brak użyteczności można również zidentyfikować, prosząc kilku typowych użytkowników o dynamiczne przetestowanie interfejsu użytkownika i przekazanie opinii na temat jego użyteczności.
b) Odpowiedź poprawna. Przegląd kodu pozwala wykryć kod, do którego nie można dotrzeć żadną ścieżką, jednak testy dynamiczne mogą sprawdzić tylko kod, do którego można dotrzeć, i nie pozwalają stwierdzić, że kod jest niedostępny bez uruchomienia wszystkich możliwych kombinacji danych wejściowych i stanów wejściowych, co jest niepraktyczne (a w większości przypadków -- niemożliwe) w przypadku rzeczywistego kodu.
c) Odpowiedź niepoprawna. Słabe czasy odpowiedzi dla większości użytkowników są trudne do określenia bez wykonania kodu (tj. poprzez testowanie statyczne), więc w tej sytuacji testy dynamiczne mogą wykryć defekt, ale testy statyczne prawdopodobnie jego nie wykryją.
d) Odpowiedź niepoprawna. Przegląd kodu przez osobę znającą wymagane funkcje mógłby wykryć, że wymagane funkcje nie zostały zaimplementowane w kodzie, a testy dynamiczne mogłyby również posłużyć do ustalenia, że te wymagane funkcje nie zostały zaimplementowane.

---

# metadata
lo: FL-3.2.1
k-level: K1
points: 1
correct: c

## question
Która z poniższych opcji jest zaletą wczesnych i częstych informacji zwrotnych od interesariuszy?

## answers
a) Dzięki nim menedżerowie wiedzą, którzy programiści są mniej produktywni.
b) Pozwalają kierownikom projektów ustalać priorytety w kontaktach z interesariuszami.
c) Ułatwiają wczesną komunikację potencjalnych problemów związanych z jakością.
d) Użytkownicy końcowi lepiej rozumieją, dlaczego dostawa produktu jest opóźniona.

## justification
a) Odpowiedź niepoprawna. Informacje zwrotne pochodzą od interesariuszy (np. przedstawicieli jednostek biznesowych i użytkowników końcowych), a nie od programistów, więc nie są one w stanie dostarczyć menedżerom informacji o tym, którzy programiści są bardziej lub mniej produktywni.
b) Odpowiedź niepoprawna. Wczesna i częsta informacja zwrotna od interesariuszy nie jest wykorzystywana przez kierowników projektów do ustalania priorytetów w kontaktach z różnymi interesariuszami.
c) Odpowiedź poprawna. Uzyskiwanie wczesnej i częstej informacji zwrotnej od interesariuszy może być bardzo korzystne, ponieważ ułatwia wczesną komunikację potencjalnych problemów związanych z jakością, może zapobiegać nieporozumieniom dotyczącym wymagań i zapewnia, że wszelkie zmiany w wymaganiach interesariuszy są zrozumiałe i wdrażane szybciej.
d) Odpowiedź niepoprawna. Wczesne i częste informacje zwrotne mogą zapobiec opracowaniu produktu, który nie spełnia potrzeb interesariuszy, a skutkuje kosztownymi przeróbkami i niedotrzymaniem terminów, więc idealnie byłoby, gdyby nie było żadnych opóźnień. Ponadto informacje zwrotne pochodzą od interesariuszy (a nie są do nich kierowane), w tym od użytkowników końcowych, więc użytkownicy końcowi przekazujący informacje zwrotne nie pomogą w zrozumieniu użytkowników końcowych.

---

# metadata
lo: FL-3.2.2
k-level: K2
points: 1
correct: d

## question
Rozważ poniższe opisy zadań (1--4) oraz czynności związane z przeglądami (A--D).

1. Wybrano charakterystyki jakościowe, które mają być oceniane, oraz kryteria zakończenia.
2. Wszyscy mają dostęp do produktu pracy.
3. W produkcie pracy zidentyfikowano anomalie.
4. Omówiono anomalie.

A. Przegląd indywidualny.
B. Rozpoczęcie przeglądu.
C. Planowanie.
D. Przekazanie informacji i analiza.

Które z poniższych najlepiej łączy opisy zadań z czynnościami?

## answers
a) 1B, 2C, 3D, 4A.
b) 1B, 2D, 3C, 4A.
c) 1C, 2A, 3B, 4D.
d) 1C, 2B, 3A, 4D.

## justification
Rozważając każdy z wymienionych opisów zadań:
1. Wybrano charakterystyki jakościowe, które mają być oceniane, oraz kryteria wyjścia -- (Planowanie (C): określenie zakresu przeglądu, celu, produktu pracy, który ma być poddany przeglądowi, charakterystyk jakościowych, które mają być oceniane, obszarów zainteresowania, kryteriów wyjścia, informacji pomocniczych, takich jak normy, nakład pracy i ramy czasowe).
2. Wszyscy mają dostęp do produktu pracy -- (Rozpoczęcie przeglądu (B): zapewnienie wszystkim uczestnikom dostępu do produktu pracy i niezbędnych zasobów oraz wyjaśnienie ich ról i obowiązków).
3. W produkcie pracy zidentyfikowano anomalie -- (Indywidualny przegląd (A): ocena jakości produktu pracy, identyfikacja i rejestrowanie anomalii, zaleceń i pytań przy użyciu technik przeglądu, takich jak przegląd oparty na liście kontrolnej i przegląd oparty na scenariuszach).
4. Analiza i omówienie anomalii -- (Komunikacja i analiza (D): analiza i omówienie każdej anomalii, określenie jej statusu, odpowiedzialności i wymaganych działań oraz podjęcie decyzji dotyczących przeglądu, zazwyczaj podczas spotkania przeglądowego. Może to obejmować określenie potrzeby przeprowadzenia przeglądu uzupełniającego).

Zatem prawidłowe dopasowanie to: 1C, 2B, 3A, 4D, a więc:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-3.2.3
k-level: K1
points: 1
correct: c

## question
Rozważ role w przeglądach (1--4) oraz obowiązki ich dotyczące (A--D).

1. Protokolant.
2. Lider przeglądu.
3. Moderator.
4. Kierownik.

A. Zapewnia skuteczne prowadzenie spotkań przeglądowych i stworzenie bezpiecznego środowiska przeglądu.
B. Rejestruje informacje dotyczące przeglądu, takie jak podjęte decyzje i nowe anomalie wykryte podczas spotkania przeglądowego.
C. Podejmuje decyzje dotyczące zakresu przeglądu i zapewnia zasoby, takie jak personel i czas na przeprowadzenie przeglądu.
D. Ponosi ogólną odpowiedzialność za przegląd, np. za organizowanie terminu i miejsca jego przeprowadzenia.

Która z poniższych opcji najlepiej łączy role z odpowiadającymi im obowiązkami?

## answers
a) 1A, 2B, 3D, 4C.
b) 1A, 2C, 3B, 4D.
c) 1B, 2D, 3A, 4C.
d) 1B, 2D, 3C, 4A.

## justification
Rozważając każdy z wymienionych opisów ról:
1. Protokolant -- odpowiedzialny za zbieranie opinii przeglądających i dokumentowanie informacji dotyczących przeglądu, takich jak podjęte decyzje i wszelkie nowe anomalie zidentyfikowane podczas spotkania przeglądowego. (Rejestruje informacje dotyczące przeglądu, takie jak decyzje i nowe anomalie wykryte podczas spotkania przeglądowego -- B).
2. Lider przeglądu -- odpowiedzialny za nadzorowanie procesu przeglądu, np. wybór członków zespołu przeglądowego, planowanie spotkań przeglądowych i zapewnienie pomyślnego zakończenia przeglądu. (Liderzy przeglądu ponoszą ogólną odpowiedzialność za przegląd, np. za organizację terminu i miejsca przeglądu -- D).
3. Moderator (facylitator) -- odpowiedzialny za zapewnienie skutecznego przebiegu spotkań przeglądowych, w tym zarządzanie czasem, moderowanie dyskusji i tworzenie bezpiecznego środowiska, w którym każdy może swobodnie wyrażać swoje opinie. (Zapewnia skuteczny przebieg spotkań przeglądowych i stworzenie bezpiecznego środowiska przeglądu -- A).
4. Kierownik -- odpowiedzialny za podejmowanie decyzji dotyczących tego, co należy poddać przeglądowi oraz przydzielanie zasobów, takich jak personel i czas, na potrzeby przeglądu. (Podejmuje decyzje dotyczące tego, co należy poddać przeglądowi, oraz zapewnia zasoby, takie jak personel i czas, na potrzeby przeglądu -- C).

Prawidłowe dopasowanie to: 1B, 2D, 3A, 4C, zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.1.1
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń **najlepiej** opisuje różnicę między testowaniem w oparciu o tablicę decyzyjną a testowaniem gałęzi?

## answers
a) W testowaniu w oparciu o tablicę decyzyjną przypadki testowe są wyprowadzane z instrukcji decyzyjnych w kodzie. W testowaniu gałęzi przypadki testowe są wyprowadzane na podstawie wiedzy o przepływie sterowania przedmiotu testów.
b) W testowaniu w oparciu o tablicę decyzyjną przypadki testowe są wyprowadzane ze specyfikacji opisującej logikę biznesową. W testowaniu gałęzi przypadki testowe opierają się na przewidywaniu potencjalnych defektów w kodzie źródłowym.
c) W testowaniu w oparciu o tablicę decyzyjną przypadki testowe są wyprowadzane na podstawie wiedzy na temat przepływu sterowania w przedmiocie testów. W testowaniu gałęzi przypadki testowe są wyprowadzane ze specyfikacji opisującej logikę biznesową.
d) W testowaniu w oparciu o tablicę decyzyjną przypadki testowe są niezależne od sposobu implementacji oprogramowania. W testowaniu gałęzi przypadki testowe można tworzyć dopiero po zaprojektowaniu lub zaimplementowaniu kodu.

## justification
a) Odpowiedź niepoprawna. Testowanie w oparciu o tablicę decyzyjną jest czarnoskrzynkową, a nie białoskrzynkową techniką testowania -- przypadki testowe nie są oparte na decyzjach zawartych w kodzie źródłowym. W testowaniu gałęzi przypadki testowe są wyprowadzane na podstawie wiedzy o przepływie sterowania przedmiotu testów.
b) Odpowiedź niepoprawna. Przewidywanie potencjalnych defektów jest stosowane w zgadywaniu błędów (technika testowania oparta na doświadczeniu), a nie w testowaniu gałęzi (białoskrzynkowa technika testowania). W testowaniu w oparciu o tablicę decyzyjną przypadki testowe są wyprowadzane ze specyfikacji opisującej logikę biznesową.
c) Odpowiedź niepoprawna. Jeśli przypadek testowy opiera się na wiedzy o przepływie sterowania w przedmiocie testów, mamy do czynienia z białoskrzynkową techniką testowania. Testowanie w oparciu o tablicę decyzyjną opiera się zazwyczaj na analizie logiki biznesowej, więc jest to czarnoskrzynkowa technika testowania. W testowaniu gałęzi przypadki testowe nie są wyprowadzane ze specyfikacji -- to sprawiłoby, że byłaby to czarnoskrzynkowa technika testowania. Testowanie gałęzi jest białoskrzynkową techniką testowania, w której przypadki testowe są wyprowadzane na podstawie struktury kodu źródłowego.
d) Odpowiedź poprawna. Testowanie w oparciu o tablicę decyzyjną jest czarnoskrzynkową techniką testowania, więc opiera się na analizie określonego zachowania przedmiotu testów bez odniesienia do jego wewnętrznej struktury. W związku z tym przypadki testowe są niezależne od sposobu implementacji oprogramowania. Testowanie gałęzi jest białoskrzynkową techniką testowania, więc przypadki testowe opierają się na analizie wewnętrznej struktury i przetwarzania przedmiotu testów. Ponieważ przypadki testowe są zależne od sposobu zaprojektowania i zakodowania oprogramowania, można je utworzyć dopiero po zaprojektowaniu lub implementacji przedmiotu testów.

---

# metadata
lo: FL-4.2.1
k-level: K3
points: 1
correct: a

## question
Klienci sieci myjni samochodowych TestWash posiadają karty z zapisem liczby dotychczas zakupionych myć. Wartość początkowa wynosi 0. Po wjeździe do myjni system zwiększa liczbę na karcie o jeden. Wartość ta reprezentuje liczbę bieżących myć. Na podstawie tej liczby system decyduje, do jakiej zniżki klient jest uprawniony.
Za każde dziesiąte mycie system przyznaje 10% zniżki, a za każde dwudzieste mycie przyznaje dodatkowe 40% zniżki (tj. łącznie 50% zniżki).
Który z poniższych zestawów danych wejściowych (rozumianych jako liczby bieżącego mycia) osiąga najwyższe pokrycie w podziale na klasy równoważności?

## answers
a) 19, 20, 30.
b) 11, 12, 20.
c) 1, 10, 50.
d) 10, 29, 30, 31.

## justification
a) Odpowiedź poprawna. 19 pokrywa klasę równoważności „bez rabatu”, 20 pokrywa klasę równoważności „50% rabatu”, a 30 pokrywa klasę równoważności „10% rabatu”. Te trzy wartości pokrywają więc wszystkie trzy klasy równoważności.
b) Odpowiedź niepoprawna. 11 i 12 pokrywają klasę równoważności „bez rabatu”, a 20 pokrywa klasę równoważności „50% rabatu”, więc pokrywają one dwie z trzech klas równoważności.
c) Odpowiedź niepoprawna. 1 pokrywa klasę równoważności „bez rabatu”, a 10 i 50 pokrywają klasę równoważności „10% rabatu”. Klasa równoważności „50% rabatu” nie jest pokryta, więc łącznie dane testowe pokrywają dwie z trzech klas równoważności.
d) Odpowiedź niepoprawna. 29 i 31 pokrywają klasę równoważności „bez rabatu”, natomiast 10 i 30 pokrywają klasę równoważności „10% rabatu”. Klasa równoważności „50% rabatu” nie jest pokryta, więc łącznie pokryte są dwie z trzech klas równoważności.

---

# metadata
lo: FL-4.2.2
k-level: K3
points: 1
correct: d

## question
Testujesz formularz, który weryfikuje poprawność długości hasła podanego jako dane wejściowe. Formularz akceptuje hasło o prawidłowej długości i odrzuca hasło, które jest zbyt krótkie lub zbyt długie. Długość hasła jest prawidłowa, jeśli zawiera od 6 do 12 znaków włącznie. W przeciwnym razie jest ono uznawane za nieprawidłowe. Początkowo formularz jest pusty (długość hasła = 0).
Stosujesz analizę wartości brzegowych do zmiennej „długość hasła”. Twój zestaw przypadków testowych osiąga 100% pokrycia wartości brzegowych w wersji dwupunktowej. Zespół zdecydował, że ze względu na wysokie ryzyko związane z tym modułem należy dodać przypadki testowe, aby zapewnić 100% pokrycia wartości brzegowych w wersji **trójpunktowej**.
Jakie **dodatkowe** długości hasła należy przetestować, aby osiągnąć to pokrycie?

## answers
a) 4, 5, 13, 14.
b) 7, 11.
c) 1, 5, 13.
d) 1, 4, 7, 11, 14.

## justification
Dziedzina „długość hasła” ma trzy klasy równoważności:

- długość hasła: zbyt krótkie {0, 1, ..., 4, 5},
- długość hasła: poprawne {6, 7, ..., 11, 12},
- długość hasła: zbyt długie {13, 14, ...}.

Aby uzyskać pełne pokrycie dla trójpunktowej analizy wartości brzegowych, należy przetestować wszystkie brzegi oraz wszystkich ich sąsiadów, czyli wartości: 0, 1, 4, 5, 6, 7, 11, 12, 13, 14.
Ponieważ testy osiągają już pełne pokrycie wartości brzegowych w wersji dwupunktowej, oznacza to, że przetestowaliśmy już wartości: 0, 5, 6, 12 i 13.
Zatem dodatkowe wartości, które należy pokryć, aby zapewnić pełne pokrycie w wersji trójpunktowej to różnica pomiędzy tymi dwoma zbiorami, czyli 1, 4, 7, 11, 14.
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź poprawna.

---

# metadata
lo: FL-4.2.3
k-level: K3
points: 1
correct: b

## question
Poniższa tablica decyzyjna zawiera zasady określania ryzyka miażdżycy.

| **Warunki** | **Reguła 1** | **Reguła 2** | **Reguła 3** | **Reguła 4** | **Reguła 5** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Cholesterol (mg/dl) | ≤ 124 | ≤ 124 | 125 -- 200 | 125 -- 200 | ≥ 201 |
| Ciśnienie krwi (mm Hg) | ≤ 140 | > 140 | ≤ 140 | > 140 | -- |
| **Akcje** | | | | | |
| Poziom ryzyka | bardzo niski | niski | średni | wysoki | bardzo wysoki |

Posiadasz już przypadki testowe z następującymi danymi wejściowymi:

- TC1: Cholesterol = 125 mg/dl, Ciśnienie krwi = 141 mm Hg
- TC2: Cholesterol = 200 mg/dl, Ciśnienie krwi = 201 mm Hg
- TC3: Cholesterol = 124 mg/dl, Ciśnienie krwi = 201 mm Hg
- TC4: Cholesterol = 109 mg/dl, Ciśnienie krwi = 200 mm Hg
- TC5: Cholesterol = 201 mg/dl, Ciśnienie krwi = 140 mm Hg

Jakie pokrycie tablicy decyzyjnej osiąga ten zestaw przypadków testowych?

## answers
a) 40%.
b) 60%.
c) 80%.
d) 100%.

## justification
Tablica decyzyjna ma pięć kolumn. Każdy przypadek testowy pokrywa jedną z nich.
TC1 i TC2 pokrywają regułę 4.
TC3 i TC4 pokrywają regułę 2.
TC5 pokrywa regułę 5.
Zatem te pięć przypadków testowych pokrywa trzy z pięciu kolumn, osiągając pokrycie (3/5)*100% = 60%.
W związku z tym:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.2.4
k-level: K3
points: 1
correct: c

## question
System pamięci może przechowywać do trzech elementów i jest modelowany za pomocą poniższego diagramu stanów. Zmienna N reprezentuje liczbę aktualnie przechowywanych elementów. System rozpoczyna pracę w stanie START.

Przejścia:

- START --Add [N := 1]--> NOT FULL
- NOT FULL --Add [N < 2] / N := N + 1--> NOT FULL (przejście do samego siebie)
- NOT FULL --Add [N = 2] / N := N + 1--> FULL
- FULL --Remove / N := N - 1--> NOT FULL
- NOT FULL --Remove [N > 0] / N := N - 1--> NOT FULL (przejście do samego siebie)

Który z poniższych przypadków testowych, przedstawionych jako sekwencje zdarzeń, osiąga najwyższy poziom pokrycia przejść poprawnych?

## answers
a) Add, Remove, Add, Add, Add.
b) Add, Add, Add, Add, Remove, Remove.
c) Add, Add, Add, Remove, Remove.
d) Add, Add, Add, Remove, Add.

## justification
Istnieje pięć poprawnych przejść: START->NOT FULL (Add), NOT FULL->NOT FULL (Add, N < 2), NOT FULL->FULL (Add, N = 2), FULL->NOT FULL (Remove) oraz NOT FULL->NOT FULL (Remove, N > 0).
Test a) Add, Remove, Add, Add, Add pokrywa: START->NOT FULL, NOT FULL->NOT FULL (Remove), NOT FULL->NOT FULL (Add), NOT FULL->FULL, czyli 4 z 5 poprawnych przejść (80% pokrycia).
Test b) Add, Add, Add, Add, Remove, Remove jest niewykonalny, ponieważ po pierwszych trzech akcjach Add system znajduje się w stanie FULL i nie ma żadnego poprawnego przejścia z FULL wywołanego zdarzeniem Add. Po pierwszych trzech przejściach osiągnięto jedynie 60% pokrycia przejść poprawnych.
Test c) Add, Add, Add, Remove, Remove pokrywa: START->NOT FULL, NOT FULL->NOT FULL (Add), NOT FULL->FULL, FULL->NOT FULL, NOT FULL->NOT FULL (Remove), czyli 5 z 5 przejść poprawnych (100% pokrycia).
Test d) Add, Add, Add, Remove, Add pokrywa: START->NOT FULL, NOT FULL->NOT FULL (Add), NOT FULL->FULL, FULL->NOT FULL, NOT FULL->FULL (przejście już policzone), czyli 4 z 5 poprawnych przejść (80% pokrycia).
Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-4.3.1
k-level: K2
points: 1
correct: b

## question
Wykonujesz dwa przypadki testowe, T1 i T2, na tym samym kodzie. Test T1 osiągnął 40% pokrycia instrukcji, a test T2 osiągnął 65% pokrycia instrukcji.
Które z poniższych stwierdzeń musi być prawdziwe?

## answers
a) Zestaw testowy składający się z testów T1 i T2 osiąga 105% pokrycia instrukcji.
b) Co najmniej jedna instrukcja musiała zostać wykonana zarówno przez T1, jak i T2.
c) Co najmniej 5% instrukcji w testowanym kodzie jest niewykonalnych.
d) Zestaw testowy składający się z testów T1 i T2 osiąga pełne pokrycie gałęzi.

## justification
a) Odpowiedź niepoprawna. Pokrycie jest zawsze definiowane jako procent pokrytych elementów. Dlatego nie może przekraczać 100%.
b) Odpowiedź poprawna. Gdyby instrukcje wykonane przez T1 i T2 były rozłączne, pokrycie zestawu testowego {T1, T2} wynosiłoby 105%, co jest niemożliwe (patrz odpowiedź a). Dlatego co najmniej 5% instrukcji wykonywalnych musiało zostać wykonanych zarówno przez T1, jak i T2.
c) Odpowiedź niepoprawna. Pokrycie instrukcji nie mówi nam nic o liczbie instrukcji niewykonywalnych w kodzie.
d) Odpowiedź niepoprawna. Nawet jeśli zestaw testowy osiąga pełne pokrycie instrukcji, nie oznacza to osiągnięcia pełnego pokrycia gałęzi.

---

# metadata
lo: FL-4.3.2
k-level: K2
points: 1
correct: c

## question
Metryka pokrycia gałęzi zdefiniowana jest jako PG = (X / Y) * 100%.
Co oznaczają X i Y w tym wzorze?

## answers
a) X = liczba wyników decyzji wykonanych przez przypadki testowe, Y = całkowita liczba możliwych wyników decyzji w kodzie.
b) X = liczba gałęzi warunkowych wykonanych przez przypadki testowe, Y = całkowita liczba gałęzi w kodzie.
c) X = liczba gałęzi wykonanych przez przypadki testowe, Y = całkowita liczba gałęzi w kodzie.
d) X = liczba gałęzi warunkowych wykonanych przez przypadki testowe, Y = całkowita liczba możliwych wyników decyzji w kodzie.

## justification
Testowanie gałęzi to białoskrzynkowa technika testowania, w której elementami pokrycia są gałęzie. Gałąź to przeniesienie sterowania między dwoma wierzchołkami w grafie przepływu sterowania, który pokazuje możliwe sekwencje wykonywania fragmentów kodu źródłowego w przedmiocie testów. Każde przeniesienie sterowania może być bezwarunkowe (tj. kod liniowy) lub warunkowe (tj. wynik decyzji). Pokrycie mierzy się jako liczbę gałęzi wykonanych przez przypadki testowe podzieloną przez całkowitą liczbę gałęzi i wyraża się w procentach.
Zatem:
a) Odpowiedź niepoprawna. Wynik decyzji jest gałęzią warunkową. W przypadku testowania gałęzi X liczy nie tylko gałęzie warunkowe, ale także bezwarunkowe.
b) Odpowiedź niepoprawna. Pokrycie gałęzi uwzględnia nie tylko gałęzie warunkowe, ale także bezwarunkowe.
c) Odpowiedź poprawna. Pokrycie gałęzi mierzy się jako liczbę gałęzi wykonanych przez przypadki testowe podzieloną przez całkowitą liczbę gałęzi i wyraża się w procentach.
d) Odpowiedź niepoprawna. Zarówno X, jak i Y uwzględniają tylko gałęzie warunkowe i nie uwzględniają gałęzi bezwarunkowych.

---

# metadata
lo: FL-4.4.2
k-level: K2
points: 1
correct: a, e

## question
Które **dwa** z poniższych stwierdzeń stanowią **najlepsze** uzasadnienie dla stosowania testowania eksploracyjnego?

## answers
a) Testerom nie przydzielono wystarczającej ilości czasu na projektowanie i wykonywanie testów.
b) Strategia testów wymaga od testerów stosowania formalnych technik testowania czarnoskrzynkowego.
c) Specyfikacja jest napisana w formalnym języku, który może być przetwarzany przez narzędzie.
d) Testerzy są członkami zespołu zwinnego i mają dobre umiejętności programistyczne.
e) Testerzy mają doświadczenie w danej dziedzinie biznesowej i posiadają dobre umiejętności analityczne.

## justification
Testowanie eksploracyjne jest przydatne, gdy specyfikacje są niepełne lub nie istnieją lub gdy istnieje znaczna presja czasowa na przeprowadzenie testów. Testowanie eksploracyjne jest również przydatne jako uzupełnienie innych, bardziej formalnych technik testowania. Testowanie eksploracyjne będzie bardziej skuteczne, jeśli tester jest doświadczony, posiada wiedzę dziedzinową i wysoki poziom niezbędnych umiejętności, takich jak zdolności analityczne, ciekawość i kreatywność.
Zatem:
a) Odpowiedź poprawna. Testowanie eksploracyjne jest przydatne, gdy specyfikacje są niepełne lub nieistniejące lub gdy istnieje znaczna presja czasowa na testowanie.
b) Odpowiedź niepoprawna. Testowanie eksploracyjne nie jest czarnoskrzynkową techniką testowania.
c) Odpowiedź niepoprawna. Testowanie eksploracyjne jest przydatne, gdy jakość specyfikacji jest niska.
d) Odpowiedź niepoprawna. Umiejętności programowania nie mają zasadniczo nic wspólnego z testowaniem eksploracyjnym.
e) Odpowiedź poprawna. Testowanie eksploracyjne będzie bardziej skuteczne, jeśli tester ma doświadczenie, posiada wiedzę dziedzinową i wysoki poziom niezbędnych umiejętności, takich jak zdolności analityczne, ciekawość i kreatywność.

---

# metadata
lo: FL-4.4.3
k-level: K2
points: 1
correct: d

## question
Które z poniższych stwierdzeń **najlepiej** pasuje jako element listy kontrolnej używanej w testowaniu opartym na liście kontrolnej?

## answers
a) „Programista popełnił błąd podczas implementacji kodu”.
b) „Osiągnięte pokrycie instrukcji przekracza 85%”.
c) „Program działa poprawnie pod względem wymagań funkcjonalnych i niefunkcjonalnych”.
d) „Komunikaty o błędach są napisane w języku zrozumiałym dla użytkownika”.

## justification
a) Odpowiedź niepoprawna. Listy kontrolne powinny zawierać warunki testowe, które należy zweryfikować. Jest to przykład błędu, a nie warunku testowego; nawet jeśli tester był w stanie wywnioskować pewne potencjalne warunki testowe na podstawie przykładów błędów, opis tego błędu jest zbyt ogólny.
b) Odpowiedź niepoprawna. Listy kontrolne nie powinny zawierać pozycji, które lepiej nadają się jako kryteria wyjścia. Jest to przykład kryterium wyjścia.
c) Odpowiedź niepoprawna. Listy kontrolne nie powinny zawierać pozycji, które są zbyt ogólne. Jest to bardzo ogólna pozycja, która praktycznie opisuje cel testu.
d) Odpowiedź poprawna. Jest to przykład warunku testowego, który może zostać sprawdzony przez człowieka.

---

# metadata
lo: FL-4.5.2
k-level: K2
points: 1
correct: b

## question
Rozważ poniższe kryterium akceptacji dla historyjki użytkownika napisanej z perspektywy właściciela sklepu internetowego.

*Zakładając, że użytkownik jest zalogowany i znajduje się na stronie głównej,*
*Kiedy użytkownik kliknie przycisk „Dodaj produkt”,*
*Wtedy powinien pojawić się formularz „Utwórz produkt” oraz użytkownik powinien móc wprowadzić nazwę i cenę nowego produktu.*

W jakim formacie napisano to kryterium akceptacji?

## answers
a) W formacie zorientowanym na reguły.
b) W formacie zorientowanym na scenariusze.
c) W formacie zorientowanym na produkt.
d) W formacie zorientowanym na proces.

## justification
a) Odpowiedź niepoprawna. Format zorientowany na reguły obejmuje formaty takie jak listy kontrolne z punktami lub tabele mapowań wejścia-wyjścia, wyraźnie pokazujące reguły, których należy przestrzegać. Format „Given/When/Then” jest formatem zorientowanym na scenariusze, ponieważ opisuje scenariusz, który ma zostać zweryfikowany.
b) Odpowiedź poprawna. Jest to format „Given/When/Then”, który jest zorientowany na scenariusze.
c) Odpowiedź niepoprawna. Nie ma formatu kryteriów akceptacji „zorientowanego na produkt”.
d) Odpowiedź niepoprawna. Nie ma formatu kryteriów akceptacji „zorientowanego na proces”.

---

# metadata
lo: FL-4.5.3
k-level: K3
points: 1
correct: d

## question
Twój zespół analizuje poniższą historyjkę użytkownika w celu zdefiniowania kryteriów akceptacji.

*Jako zarejestrowany klient chcę mieć możliwość przeglądania moich poprzednich zamówień na stronie internetowej firmy, aby móc śledzić moje zakupy.*

Który z poniższych przypadków testowych **nie** jest wyprowadzony z tej historyjki użytkownika?

## answers
a) Dane wejściowe: klient loguje się na swoje konto na stronie internetowej i klika przycisk „zobacz historię zamówień”. Oczekiwany wynik: system wyświetla listę wszystkich poprzednich zamówień klienta, w tym datę, numer zamówienia i całkowity koszt.
b) Dane wejściowe: klient klika zamówienie z listy zamówień. Oczekiwany wynik: system wyświetla poszczególne zakupione produkty wraz z ich cenami i ilościami.
c) Dane wejściowe: klient klika przycisk „Sortuj rosnąco” na ekranie historii zamówień. Oczekiwany rezultat: system wyświetla historię zamówień posortowaną według numeru zamówienia w porządku rosnącym.
d) Dane wejściowe: niezarejestrowany klient rejestruje się jako nowy klient, podając prawidłowy adres e-mail, który nie istnieje jeszcze w bazie danych klientów. Oczekiwany rezultat: system akceptuje rejestrację i tworzy konto.

## justification
a) Odpowiedź niepoprawna. Przypadek testowy dotyczy przeglądania poprzednich zamówień w historii zamówień.
b) Odpowiedź niepoprawna. Przypadek testowy dotyczy przeglądania poprzednich zamówień w historii zamówień.
c) Odpowiedź niepoprawna. Przypadek testowy dotyczy przeglądania poprzednich zamówień w historii zamówień.
d) Odpowiedź poprawna. Przypadek testowy dotyczy procesu rejestracji, który nie jest omawiany w historyjce użytkownika. Historyjka użytkownika dotyczy przeglądania poprzednich zamówień.

---

# metadata
lo: FL-5.1.4
k-level: K2
points: 1
correct: a

## question
Twój zespół stosuje proces wykorzystujący potok dostarczania DevOps. Pierwsze trzy etapy tego procesu to:

1. Opracowanie kodu.
2. Przesłanie kodu do systemu kontroli wersji i scalenie go z gałęzią „testową”.
3. Przeprowadzenie testów modułowych dla przesłanego kodu.

Które z poniższych jest **najlepszym** kryterium wejścia do kroku (2) tego procesu?

## answers
a) Analiza statyczna nie zwraca żadnych ostrzeżeń o wysokim stopniu krytyczności dla przesłanego kodu.
b) System kontroli wersji nie zgłasza żadnych konfliktów podczas scalania kodu z gałęzią „testową”.
c) Testy modułowe są skompilowane i gotowe do wykonania.
d) Pokrycie instrukcji przesłanego kodu wynosi co najmniej 80%.

## justification
a) Odpowiedź poprawna. Jest to coś, co można (i należy) sprawdzić *przed* przesłaniem kodu do systemu kontroli wersji.
b) Odpowiedź niepoprawna. Jest to coś, co można sprawdzić *po* wykonaniu kroku (2), ponieważ zgłoszenie konfliktu scalania można wykonać po przesłaniu i scaleniu kodu.
c) Odpowiedź niepoprawna. Lepiej pasuje jako kryterium wejścia do kroku (3).
d) Odpowiedź niepoprawna. Lepiej pasuje jako kryterium wyjścia do kroku (3).

---

# metadata
lo: FL-5.1.4
k-level: K3
points: 1
correct: b

## question
Chcesz oszacować wysiłek (wyrażony w pieniądzu) związany z testowaniem nowego projektu, korzystając z szacowania na podstawie proporcji. Obliczasz stosunek wysiłku związanego z testowaniem w stosunku do wysiłku związanego z rozwojem, korzystając z uśrednionego wysiłku związanego z rozwojem oraz z uśrednionego wysiłku związanego z testowaniem, pochodzących z czterech poprzednich projektów podobnych do nowego. Tabela przedstawia te dane historyczne.

| **Projekt** | **Wysiłek związany z rozwojem ($)** | **Wysiłek związany z testowaniem ($)** |
| :--- | :---: | :---: |
| P1 | 800 000 | 40 000 |
| P2 | 1 200 000 | 130 000 |
| P3 | 600 000 | 70 000 |
| P4 | 1 000 000 | 120 000 |

Szacowany koszt opracowania nowego projektu wynosi 800 000 $.
Jaki będzie wynik szacowania wysiłku testowego w ramach tego projektu?

## answers
a) 40 000 $.
b) 80 000 $.
c) 81 250 $.
d) 82 500 $.

## justification
Średni koszt rozwoju wynosi 900 000 $, a średni koszt testowania wynosi 90 000 $ (obliczony na podstawie czterech projektów). Średni stosunek nakładów na testowanie do nakładów na rozwój wynosi więc 1:10 (90 000 $ : 900 000 $), co oznacza, że historycznie średnio nakłady na testowanie stanowią 10% nakładów na rozwój. Jeśli więc koszt rozwoju szacuje się na 800 000 $, szacowany koszt testowania wynosi 10% x 800 000 $ = 0,1 x 800 000 $ = 80 000 $.
A zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.1.5
k-level: K3
points: 1
correct: b

## question
Testujesz aplikację, która umożliwia użytkownikom WYSZUKIWANIE produktów, WYŚWIETLANIE szczegółów produktów, DODAWANIE produktów do koszyka i SKŁADANIE ZAMÓWIEŃ.
Dysponujesz siedmioma poniższymi przypadkami testowymi, które chcesz wykonać. Testy powinny być przeprowadzone w optymalnej kolejności, w oparciu o priorytet testów.

| **Test** | | **Priorytet (1 = najwyższy priorytet)** |
| :--- | :--- | :---: |
| TC1 | WYSZUKAJ produkt A | 4 |
| TC2 | WYSZUKAJ produkt B | 4 |
| TC3 | WYŚWIETL szczegóły produktu A | 3 |
| TC4 | WYŚWIETL szczegóły produktu B | 2 |
| TC5 | DODAJ produkt A do koszyka | 3 |
| TC6 | DODAJ produkt B do koszyka | 1 |
| TC7 | ZŁÓŻ ZAMÓWIENIE | 5 |

Zidentyfikowano następujące zależności logiczne między przypadkami testowymi:

- Funkcja WYSZUKAJ musi zostać przetestowana przed przetestowaniem funkcji WYŚWIETL.
- Funkcja WYŚWIETL musi zostać przetestowana przed funkcją DODAJ.
- Funkcja DODAJ musi zostać przetestowana przed funkcją ZŁÓŻ ZAMÓWIENIE.

Który przypadek testowy powinien zostać wykonany jako **czwarty**?

## answers
a) TC3.
b) TC1.
c) TC7.
d) TC2.

## justification
Zależności logiczne oznaczają, że dla każdego produktu przed uruchomieniem funkcji ZŁÓŻ ZAMÓWIENIE należy uruchomić funkcje WYSZUKAJ -> WYŚWIETL -> DODAJ. Przed uruchomieniem funkcji ZŁÓŻ ZAMÓWIENIE można dodać więcej produktów (korzystając z tej samej sekwencji).
W związku z tym najpierw należy wykonać TC1 lub TC2, w przeciwnym razie nie będzie można kontynuować. Pierwszeństwo należy nadać przypadkom testowym WYŚWIETL i DODAJ produkt B, ponieważ przypadki te (TC6, TC4) mają wyższy priorytet. Tak więc pierwsze 3 testy do wykonania to TC2 -> TC4 -> TC6.
Teraz musimy rozważyć, czy uruchomić TC7, a następnie cały przebieg dla produktu A, czy też najpierw uruchomić przypadki testowe dla produktu A. TC7 ma niższy priorytet niż pozostałe testy, należy go więc przetestować w pierwszej kolejności. W związku z tym cały przebieg powinien wyglądać następująco: TC2 -> TC4 -> TC6 -> TC1 -> TC3 -> TC5 -> TC7. Zatem:
a) Odpowiedź niepoprawna. TC1 musi zostać wykonane przed TC3.
b) Odpowiedź poprawna.
c) Odpowiedź niepoprawna. Jak pokazano powyżej, TC7 jest wykonywany jako ostatni.
d) Odpowiedź niepoprawna. Produkt B musi zostać przetestowany przed produktem A.

---

# metadata
lo: FL-5.1.7
k-level: K2
points: 1
correct: d

## question
Które z poniższych działań, zgodnie z modelem kwadrantów testowych, należy do kwadrantu Q1 („zorientowanie na technologię” i „wsparcie zespołu”)?

## answers
a) Testowanie użyteczności.
b) Testowanie funkcjonalne.
c) Testowanie akceptacyjne użytkownika.
d) Testowanie integracji modułów.

## justification
a) Odpowiedź niepoprawna. Testowanie użyteczności to testowanie ukierunkowane na biznes, które krytykuje produkt, a więc testowanie z kwadrantu Q3.
b) Odpowiedź niepoprawna. Testy funkcjonalne to testy biznesowe z kwadrantu Q2.
c) Odpowiedź niepoprawna. Testy akceptacyjne użytkownika to testy biznesowe, które krytykują produkt (kwadrant Q3).
d) Odpowiedź poprawna. Testowanie integracji modułów to testowanie ukierunkowane na technologię, które wspiera zespół (kwadrant Q1).

---

# metadata
lo: FL-5.1.7
k-level: K2
points: 1
correct: c

## question
Rozważ następujące ryzyka (1--4) oraz czynności łagodzące (A--D).

1. Nieskuteczne wdrożenie pętli powoduje długi czas odpowiedzi systemu.
2. Konsumenci zmieniają swoje preferencje.
3. Zalanie serwerowni.
4. Pacjenci powyżej określonego wieku otrzymują niedokładne raporty.

A. Akceptacja ryzyka.
B. Testowanie wydajności.
C. Wykorzystanie analizy wartości brzegowych jako techniki testowania.
D. Przeniesienie ryzyka.

Która z poniższych opcji **najlepiej** przyporządkowuje ryzyka do czynności łagodzących ryzyko?

## answers
a) 1C, 2D, 3A, 4B.
b) 1B, 2D, 3A, 4C.
c) 1B, 2A, 3D, 4C.
d) 1C, 2A, 3D, 4B.

## justification
Uwzględniając każde z wymienionych ryzyk i sposoby ich łagodzenia:
Długie czasy reakcji systemu (1) można przetestować w testach wydajnościowych (B). Zmiany preferencji konsumentów (2) są zazwyczaj poza naszą kontrolą, więc zazwyczaj akceptujemy to ryzyko (A). Zalanie serwerowni (3) może spowodować znaczne straty, dlatego powinniśmy przenieść ryzyko, np. poprzez wykupienie polisy ubezpieczeniowej (D). Fakt, że pacjenci powyżej określonego wieku otrzymują niedokładne raporty (4) sugeruje potencjalny problem z implementacją dziedziny, który można skutecznie wykryć za pomocą technik testowych, takich jak analiza wartości brzegowych (C). Zatem:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna. Poprawna kombinacja to 1B, 2A, 3D, 4C.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-5.3.1
k-level: K1
points: 1
correct: a

## question
Które z poniższych jest metryką jakości produktu?

## answers
a) Średni czas do awarii.
b) Liczba wykrytych defektów.
c) Pokrycie wymagań.
d) Odsetek wykrytych defektów.

## justification
a) Odpowiedź poprawna. Metryki jakości produktu mierzą charakterystyki jakościowe. Średni czas do awarii mierzy dojrzałość, więc jest to metryka jakości produktu.
b) Odpowiedź niepoprawna. Jest to przykład metryki defektów, a nie jakości produktu.
c) Odpowiedź niepoprawna. Jest to przykład metryki pokrycia, a nie jakości produktu.
d) Odpowiedź niepoprawna. Jest to przykład metryki defektów, a nie jakości produktu.

---

# metadata
lo: FL-5.3.3
k-level: K2
points: 1
correct: a

## question
Jesteś członkiem zespołu testowego z siedzibą w Ameryce Północnej, który opracowuje produkt dla klienta z Europy. Zespół jest zwinny, stosuje podejście DevOps i korzysta z ciągłej integracji/ciągłego dostarczania.
Który z poniższych sposobów przekazywania klientowi informacji o postępach testów jest **najmniej** skuteczny?

## answers
a) Komunikacja bezpośrednia.
b) Tablice wskaźników.
c) E-mail.
d) Wideokonferencje.

## justification
a) Odpowiedź poprawna. Klient znajduje się w innej lokalizacji i strefie czasowej, więc komunikacja bezpośrednia może być utrudniona.
b) Odpowiedź niepoprawna. Tablice wskaźników są zazwyczaj dostępne dla każdego użytkownika w dowolnym momencie, więc różnica stref czasowych nie będzie stanowić tak dużej przeszkody w komunikacji, jak komunikacja werbalna, twarzą w twarz.
c) Odpowiedź niepoprawna. Chociaż różnica czasu między Europą a Ameryką wynosi kilka godzin i może to powodować pewne niedogodności, z pewnością nie jest ona tak duża, jak w przypadku komunikacji twarzą w twarz.
d) Odpowiedź niepoprawna. Narzędzia do wideokonferencji są wygodnym środkiem komunikacji. Chociaż komunikacja między Europą a Ameryką w godzinach pracy wymaga zazwyczaj od jednej ze stron połączenia się bardzo wcześnie lub bardzo późno, nie jest to tak uciążliwe jak komunikacja werbalna twarzą w twarz.

---

# metadata
lo: FL-5.4.1
k-level: K2
points: 1
correct: a

## question
Które z poniższych stwierdzeń **najlepiej** opisuje przykład wsparcia testowania przez zarządzanie konfiguracją (ZK)?

## answers
a) Dysponując numerem wersji środowiska, narzędzie ZK może pobrać numery wersji bibliotek, zaślepek i sterowników używanych w tym środowisku.
b) Dysponując zapisem wartości danych wejściowych, narzędzie ZK może wykonać przypadki testowe dla tych konfiguracji i obliczyć pokrycie.
c) Dysponując danymi dotyczącymi daty zakupu licencji oprogramowania, narzędzie ZK automatycznie generuje informacje o zbliżającym się wygaśnięciu licencji produktu.
d) Dysponując numerem wersji przypadku testowego, narzędzie ZK może automatycznie wygenerować dane testowe dla tego przypadku testowego.

## justification
a) Odpowiedź poprawna. W przypadku złożonego elementu konfiguracji (np. środowiska testowego) zarządzanie konfiguracją (ZK) rejestruje elementy, z których ten złożony element się składa, ich relacje i wersje.
b) Odpowiedź niepoprawna. Narzędzia ZK nie wykonują przypadków testowych i nie obliczają pokrycia.
c) Odpowiedź niepoprawna. Narzędzia ZK nie są narzędziami do zarządzania licencjami.
d) Odpowiedź niepoprawna. Narzędzia ZK nie generują danych testowych.

---

# metadata
lo: FL-5.5.1
k-level: K3
points: 1
correct: b

## question
Testujesz funkcję sortowania, która pobiera zestaw liczb jako dane wejściowe i zwraca ten sam zestaw liczb posortowanych w porządku rosnącym. Dziennik wykonania testów wygląda następująco.

> Konfiguracja środowiska: funkcja sortowania (build 2.002.2182)
>
> Zestaw przypadków testowych: TCS-3, liczba przypadków testowych: 5
>
> Identyfikator przebiegu testu: 736
>
> Start 12:43:21.003
>
> 12:43:21.003 Wykonanie TC1. Wejście: 3. Wyjście: 3. Wynik: zaliczony.
>
> 12:43:21.003 Wykonanie TC2. Wejście: 3 11 6 5. Wyjście: 3 5 6 11. Wynik: zaliczony.
>
> 12:43:21.004 Wykonanie TC3. Wejście: 8 7 3 7 1. Wyjście: 1 3 7 8. Wynik: niezaliczony.
>
> 12:43:21.005 Wykonanie TC4. Wejście: -2 -2 -2 -3 -3. Wyjście: -3 -2. Wynik: niezaliczony.
>
> 12:43:21.005 Wykonanie TC5. Wejście: 0 -2 0 3 4 4. Wyjście: -2 0 3 4. Wynik: niezaliczony.
>
> Koniec 12:43:21.005
>
> Całkowity czas cyklu testowego: 0:00:00.002

Które z poniższych stwierdzeń można wykorzystać w raporcie o defekcie, ponieważ **najlepiej** opisuje awarię?

## answers
a) System nie sortuje kilku zestawów liczb. Odniesienie: TC3, TC4, TC5.
b) System wydaje się ignorować duplikaty podczas sortowania. Odniesienie: TC3, TC4, TC5.
c) System nie sortuje liczb ujemnych. Odniesienie: TC4, TC5.
d) TC3, TC4 i TC5 zawierają defekty (duplikaty danych wejściowych) i powinny zostać poprawione.

## justification
a) Odpowiedź niepoprawna. Chociaż zdanie jest prawdziwe, nie ma ono większej wartości dla programisty.
b) Odpowiedź poprawna. Z wyników testów wynika, że system ignoruje duplikaty i sortuje listę bez uwzględniania powtórzeń. Jest to prawdopodobnie przyczyną niepowodzeń w TC3, TC4, TC5. Taka informacja może pomóc programiście w znalezieniu defektu i bardziej efektywnym jego usunięciu.
c) Odpowiedź niepoprawna. System nie zawodzi podczas sortowania liczb ujemnych. Problem polega raczej na ignorowaniu duplikatów.
d) Odpowiedź niepoprawna. Przypadki testowe TC3, TC4 i TC5 są niezaliczone, ale nie wiemy, czy zawierają one jakieś defekty.

---

# metadata
lo: FL-6.1.1
k-level: K2
points: 1
correct: c

## question
Rozważ poniższe opisy (1--4) oraz kategorie narzędzi testowych (A--D).

1. Wspieranie śledzenia przepływu pracy.
2. Ułatwianie komunikacji.
3. Maszyny wirtualne.
4. Wsparcie przeglądów.

A. Narzędzia do testowania statycznego.
B. Narzędzia wspierające skalowalność i standaryzację wdrażania.
C. Narzędzia DevOps.
D. Narzędzia do współpracy.

Która z poniższych opcji najlepiej przyporządkowuje narzędzia do opisów wspieranych przez nie czynności?

## answers
a) 1A, 2B, 3C, 4D.
b) 1B, 2D, 3C, 4A.
c) 1C, 2D, 3B, 4A.
d) 1D, 2C, 3A, 4B.

## justification
Biorąc pod uwagę każdą z wymienionych kategorii narzędzi i ich opisy:
Narzędzia do testowania statycznego (A) wspierają testera w przeprowadzaniu przeglądów i analiz statycznych (4). Narzędzia wspierające skalowalność i standaryzację wdrażania (B) -- to na przykład maszyny wirtualne, narzędzia do konteneryzacji (3). Narzędzia DevOps (C) wspierają potok dostarczania DevOps, śledzenie przepływu pracy, zautomatyzowane procesy kompilacji, ciągłą integrację/ciągłe dostarczanie (CI/CD) (1). Narzędzia do współpracy (D) ułatwiają komunikację (2).
W związku z tym:
a) Odpowiedź niepoprawna.
b) Odpowiedź niepoprawna.
c) Odpowiedź poprawna. Prawidłowe dopasowanie to: 1C, 2D, 3B, 4A.
d) Odpowiedź niepoprawna.

---

# metadata
lo: FL-6.2.1
k-level: K1
points: 1
correct: a

## question
Która z poniższych opcji jest **największą** zaletą automatyzacji testów?

## answers
a) Zapewnienie miar pokrycia, które są zbyt skomplikowane, aby mogły być uzyskane przez ludzi.
b) Podział odpowiedzialności za testowanie z dostawcą narzędzia.
c) Eliminacja potrzeby krytycznego myślenia podczas analizowania wyników testów.
d) Generowanie przypadków testowych na podstawie analizy kodu programu.

## justification
a) Odpowiedź poprawna. Automatyzacja testów może zapewnić miary, które są zbyt skomplikowane, aby mogły być uzyskane przez ludzi, takie jak miary pokrycia testami białoskrzynkowymi dla wszystkich kodów z wyjątkiem tych najbardziej trywialnych.
b) Odpowiedź niepoprawna. Korzystając z narzędzi testowych, odpowiedzialność za testowanie *nie* jest dzielona z dostawcą narzędzia, ponieważ dostawca nie jest zaangażowany w testowanie, a odpowiedzialność spoczywa na testerze. Jedyną możliwą odpowiedzialność, jaką można przypisać dostawcy narzędzia, to sytuacja, w której narzędzie nie działa zgodnie z oczekiwaniami i dostarcza niepoprawne wyniki testów.
c) Odpowiedź niepoprawna. Testerzy nadal muszą stosować krytyczne myślenie podczas analizowania anomalii w wynikach testów, aby określić ich prawdopodobną przyczynę.
d) Odpowiedź niepoprawna. Ani testerzy, ani narzędzia nie mogą generować przypadków testowych wyłącznie na podstawie analizy kodu programu, ponieważ kod jest implementacją i nie dostarcza informacji o oczekiwanych wynikach, które muszą pochodzić z innej części podstawy testów, na przykład ze specyfikacji projektu.
