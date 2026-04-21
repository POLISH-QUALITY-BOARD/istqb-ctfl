# 3. Testowanie statyczne – 80 minut

## Słowa kluczowe

analiza statyczna, anomalia, inspekcja, przegląd, przegląd formalny, przegląd nieformalny, przegląd techniczny, przejrzenie, testowanie dynamiczne, testowanie statyczne

## Cele nauczania dla rozdziału 3

3.1 Podstawy testowania statycznego
    FL-3.1.1 (K1) Rozpoznawać typy produktów pracy, które mogą być badane za pomocą testowania statycznego.
    FL-3.1.2 (K2) Wyjaśnić korzyści wynikające z testowania statycznego.
    FL-3.1.3 (K2) Porównać i zestawiać ze sobą testowanie statyczne i testowanie dynamiczne.
3.2 Informacje zwrotne i proces przeglądu
    FL-3.2.1 (K1) Pamiętać korzyści wynikające z wczesnego i częstego otrzymywania informacji zwrotnych od interesariuszy.
    FL-3.2.2 (K2) Podsumować czynności wykonywane w ramach procesu przeglądu.
    FL-3.2.3 (K1) Pamiętać, jakie obowiązki są przypisane do najważniejszych ról w trakcie wykonywania przeglądów.
    FL-3.2.4 (K2) Porównać i zestawiać ze sobą różne typy przeglądów.
    FL-3.2.5 (K1) Pamiętać, jakie czynniki decydują o powodzeniu przeglądu.

## 3.1. Podstawy testowania statycznego

W przeciwieństwie do testowania dynamicznego, w testowaniu statycznym nie uruchamia się testowanego oprogramowania. Kod, specyfikacja, projekt architektury lub inne produkty pracy są oceniane poprzez badanie manualne (przeglądy) lub przy pomocy narzędzia (analiza statyczna). Cele testowania statycznego obejmują poprawę jakości, wykrywanie defektów oraz ocenę takich charakterystyk jak czytelność, kompletność, poprawność, testowalność i spójność. Testowanie statyczne można stosować zarówno do weryfikacji, jak i walidacji. 

Testerzy, przedstawiciele jednostek biznesowych (właściciel produktu, analityk biznesowy itp.) i programiści współpracują podczas sesji mapowania przykładów (ang. example mapping), wspólnego pisania historyjek użytkownika i sesji doskonalenia backlogu (ang. backlog refinement sessions), aby zapewnić, że historyjki użytkownika i powiązane z nimi produkty pracy spełniają określone kryteria, np. definicję gotowości (ang. Definition of Ready, DoR, patrz sekcja 5.1.3).

Techniki przeglądu mogą być stosowane w celu zapewnienia, że historyjki użytkownika są kompletne i zrozumiałe oraz zawierają testowalne kryteria akceptacji. Zadając właściwe pytania, testerzy badają, kwestionują i doskonalą proponowane historyjki użytkownika.

Analiza statyczna pozwala zidentyfikować problemy przed testowaniem dynamicznym, często wymagając mniejszego wysiłku, ponieważ nie są potrzebne żadne przypadki testowe i zazwyczaj wykorzystuje się narzędzia (patrz rozdział 6). Analiza statyczna stanowi często część procesu ciągłej integracji (patrz sekcja 2.1.4). 

Chociaż jest ona w dużej mierze wykorzystywana do wykrywania konkretnych defektów w kodzie, służy również do oceny łatwości pielęgnacji i poziomu zabezpieczeń. Inne przykłady narzędzi do analizy statycznej to narzędzia do sprawdzania pisowni i do oceny czytelności tekstu.

### 3.1.1. Produkty pracy badane metodą testowania statycznego

Za pomocą testowania statycznego można zbadać prawie każdy produkt pracy. Przykłady obejmują dokumenty specyfikacji wymagań, kod źródłowy, plany testów, przypadki testowe,
elementy backlogu produktu, karty opisu testów, dokumentację projektu, umowy i modele. Każdy produkt pracy, który można przeczytać i zrozumieć, może być przedmiotem przeglądu.
Jednak w przypadku analizy statycznej produkty pracy muszą mieć strukturę, względem której można je sprawdzić (np. modele, kod lub tekst o formalnej składni). Produkty pracy, które nie nadają się do testowania statycznego, to między innymi te, które są trudne do interpretacji przez ludzi i nie powinny być analizowane za pomocą narzędzi (np. kod wykonywalny lub kod innych firm, którego nie można badać z powodów prawnych).

### 3.1.2. Korzyści wynikające z testowania statycznego

Testowanie statyczne pozwala wykryć defekty na najwcześniejszych etapach cyklu wytwarzania oprogramowania, spełniając zasadę wczesnego testowania (patrz podrozdział 1.3). Pozwala ono również identyfikować defekty, których nie można wykryć za pomocą testowania dynamicznego (np. martwy kod, błędnie zastosowane wzorce projektowe, defekty w niewykonywalnych
produktach pracy). 

Testowanie statyczne umożliwia ocenę jakości produktów pracy i budowanie zaufania do nich. Dzięki weryfikacji udokumentowanych wymagań interesariusze mogą również upewnić się, że wymagania te opisują ich rzeczywiste potrzeby. Ponieważ testowanie statyczne można przeprowadzać na wczesnym etapie cyklu wytwarzania oprogramowania, zaangażowani w ten proces interesariusze mogą wypracować wspólny punkt widzenia. Inną ważną korzyścią jest usprawnienie wymiany informacji pomiędzy interesariuszami. Z tego powodu zaleca się, aby w proces testowania statycznego zaangażowane było możliwie szerokie ich grono.

Mimo że wdrożenie przeglądów może być kosztowne, całkowite koszty projektu są zazwyczaj znacznie niższe niż w przypadku braku przeglądów, ponieważ trzeba poświęcić mniej czasu i wysiłku na usuwanie defektów w późniejszych fazach projektu.

Analiza statyczna pozwala wykrywać niektóre defekty w kodzie skuteczniej niż testowanie dynamiczne, co zazwyczaj skutkuje mniejszą liczbą tego rodzaju defektów i mniejszym ogólnym wysiłkiem związanym z wytwarzaniem oprogramowania.

### 3.1.3. Różnice między testowaniem statycznym a dynamicznym

Testowanie statyczne i testowanie dynamiczne wzajemnie się uzupełniają. Mają podobne cele, takie jak wykrywanie defektów w produktach pracy (patrz sekcja 1.1.1), ale różnią się pod
pewnymi względami opisanymi poniżej:

* Zarówno testowanie statyczne, jak i testowanie dynamiczne (z analizą awarii), prowadzi do wykrycia defektów, jednak istnieją pewne rodzaje defektów wykrywalne tylko za pomocą testowania statycznego lub tylko za pomocą testowania dynamicznego.
* Testowanie statyczne wykrywa defekty bezpośrednio, natomiast testowanie dynamiczne powoduje występowanie awarii, których późniejsza analiza pozwala identyfikować związane z nimi defekty.
* Testowanie statyczne może łatwiej wykrywać defekty znajdujące się na ścieżkach kodu, rzadko wykonywanych lub trudnych do osiągnięcia w testowaniu dynamicznym.
* Testowanie statyczne można stosować do niewykonywalnych produktów pracy, natomiast testowanie dynamiczne – tylko do wykonywalnych produktów pracy.
* Testowanie statyczne może być stosowane do pomiaru charakterystyk jakościowych niezależnych od wykonywania kodu (np. utrzymywalność), natomiast testowanie
dynamiczne może być stosowane do pomiaru charakterystyk jakościowych, które są zależne od wykonywania kodu (np. wydajność).

Typowe defekty, które można wykryć łatwiej lub taniej za pomocą testowania statycznego, obejmują:

* defekty w wymaganiach (np. niespójności, niejasności, sprzeczności, pominięcia, niedokładności, powtórzenia),
* defekty w projekcie (np. nieefektywne struktury baz danych, słaba modularyzacja),
* niektóre typy defektów w kodzie (np. zmienne o nieokreślonych wartościach, zmienne niezadeklarowane, nieosiągalny lub zduplikowany kod, nadmierna złożoność kodu),
* odstępstwa od norm (np. brak zgodności z konwencjami nazewnictwa w standardach kodowania),
* nieprawidłowe specyfikacje interfejsów (np. zła liczba, typ lub kolejność parametrów),
* określone rodzaje luk w zabezpieczeniach (np. przepełnienie bufora),
* braki lub nieścisłości w pokryciu podstawy testów (np. brakujące testy dla kryterium akceptacji).

## 3.2. Informacje zwrotne i proces przeglądu

### 3.2.1. Korzyści wynikające z wczesnego i częstego otrzymywania informacji zwrotnych od interesariuszy

Wczesne i częste informacje zwrotne pozwalają na wczesne zgłaszanie potencjalnych problemów związanych z jakością. Jeśli zaangażowanie interesariuszy w cyklu wytwarzania oprogramowania jest niewielkie, opracowywany produkt może nie spełniać pierwotnej lub aktualnej wizji interesariuszy. Niezrealizowanie oczekiwań interesariuszy może skutkować kosztownymi przeróbkami, niedotrzymaniem terminów, wzajemnym obwinianiem się, a nawet całkowitym
niepowodzeniem projektu.

Częste informacje zwrotne od interesariuszy we wszystkich fazach cyklu wytwarzania oprogramowania mogą zapobiec nieporozumieniom dotyczącym wymagań i zapewnić, że zmiany w wymaganiach zostaną zrozumiane i wdrożone wcześniej. Pomaga to zespołowi wytwórczemu lepiej zrozumieć, co tworzy. Pozwala mu także skupić się na tych funkcjach, które zapewniają największą wartość dla interesariuszy i mają najbardziej pozytywny wpływ na zidentyfikowane ryzyka.

### 3.2.2. Czynności wykonywane w procesie przeglądu

Norma ISO/IEC 20246 definiuje ogólny proces przeglądu, który zapewnia ustrukturyzowane, ale elastyczne ramy, na podstawie których można dostosować konkretny proces przeglądu do danej sytuacji. Jeśli wymagany przegląd ma bardziej formalny charakter, konieczne będzie wykonanie większej liczby zadań opisanych poniżej dla różnych działań.

Wiele produktów pracy ma zbyt duży rozmiar, aby można je było objąć jednym przeglądem. Z tego powodu proces przeglądu może być przeprowadzany wielokrotnie, aby przeanalizować całość produktu pracy.

W procesie przeglądu można wyróżnić następujące czynności:

* **Planowanie**. Podczas fazy planowania należy określić zakres przeglądu, który obejmuje cel, produkt pracy podlegający przeglądowi, charakterystyki jakościowe podlegające
ocenie, obszary, na których należy się skupić, kryteria wyjścia, informacje pomocnicze (np. wykorzystywane normy), wysiłek oraz ramy czasowe przeglądu.
* **Rozpoczęcie przeglądu** polega na upewnieniu się, że wszystkie zaangażowane osoby i niezbędne elementy są gotowe do rozpoczęcia przeglądu. Obejmuje to sprawdzenie, czy
każdy uczestnik ma dostęp do przeglądanego produktu pracy, rozumie swoją rolę i obowiązki oraz otrzymał wszystkie informacje niezbędne do przeprowadzenia przeglądu.
* **Przegląd indywidualny**. Każdy przeglądający dokonuje indywidualnego przeglądu w celu oceny jakości przeglądanego produktu pracy oraz zidentyfikowania anomalii, zaleceń
i pytań, stosując jedną lub więcej technik przeglądu (np. przegląd oparty na liście kontrolnej, przegląd oparty na scenariuszach). Norma ISO/IEC 20246 zawiera bardziej szczegółowe informacje na temat różnych technik przeglądu. Przeglądający rejestrują wszystkie zidentyfikowane przez siebie anomalie, zalecenia i pytania.
* **Przekazanie informacji i analiza**. Ponieważ zidentyfikowane podczas przeglądu anomalie niekoniecznie muszą być defektami, wszystkie anomalie należy przeanalizować i omówić, określić ich status, wskazać wymagane działania względem anomalii oraz wyznaczyć osobę za to odpowiedzialną. Zazwyczaj czynności te odbywają się podczas spotkania przeglądowego, podczas którego uczestnicy decydują również o poziomie jakości przeglądanego produktu pracy oraz dalszych wymaganych działaniach. W szczególności działania te mogą obejmować przeprowadzenie kolejnego przeglądu.
* **Usunięcie defektów i raportowanie**. Dla każdego zidentyfikowanego defektu należy sporządzić raport o defekcie, aby umożliwić podjęcie działań naprawczych. Po osiągnięciu kryteriów wyjścia produkt pracy można uznać za zaakceptowany. Wyniki przeglądu są raportowane.

### 3.2.3. Role i obowiązki w przeglądach

W przeglądach biorą udział różni interesariusze, którzy mogą pełnić różne role. Główne role i związane z nimi obowiązki są następujące:

* **Kierownik** – decyduje, co ma zostać poddane przeglądowi, i zapewnia zasoby takie jak personel i czas przeznaczony na przegląd.
* **Autor** – tworzy oraz usuwa defekty z produktu pracy poddawanego przeglądowi.
* **Moderator** (zwany również facylitatorem) – zapewnia skuteczne prowadzenie spotkań przeglądowych, w tym mediację, zarządzanie czasem i bezpieczne środowisko, w którym każdy może swobodnie zabierać głos.
* **Protokolant** (zwany również rejestrującym) – dokumentuje uwagi przeglądających i rejestruje informacje dotyczące przeglądu, takie jak decyzje i nowe nieprawidłowości wykryte podczas spotkania przeglądowego.
* **Przeglądający** – przeprowadza przegląd. Może to być osoba pracująca nad projektem, ekspert merytoryczny lub dowolny inny interesariusz.
* **Lider przeglądu** – ponosi ogólną odpowiedzialność za przegląd, np. decyduje, kto będzie w nim uczestniczył, oraz organizuje miejsce przeglądu i wyznacza jego termin.

Norma ISO/IEC 20246 opisuje również inne, bardziej szczegółowe role.

### 3.2.4. Typy przeglądów

Istnieje wiele typów przeglądów, od nieformalnych po formalne. Wymagany poziom sformalizowania zależy od takich czynników jak stosowany cykl wytwarzania oprogramowania,
dojrzałość procesu wytwórczego, krytyczność i złożoność przeglądanego produktu pracy, wymogi prawne lub regulacyjne oraz potrzeba prowadzenia ścieżki audytu. Ten sam produkt pracy może być poddawany różnym typom przeglądów, np. najpierw nieformalnym, a później bardziej sformalizowanym.

Wybór odpowiedniego typu przeglądu ma kluczowe znaczenie dla osiągnięcia wymaganych celów przeglądu (patrz sekcja 3.2.5). Wybór ten opiera się nie tylko na celach, ale także na takich czynnikach jak potrzeby projektu, dostępne zasoby, rodzaj produktu pracy, zidentyfikowane ryzyka, dziedzina biznesowa oraz kultura organizacyjna firmy.

Niniejszy sylabus omawia następujące cztery typy przeglądów:

* **Przegląd nieformalny** (ang. informal review). Nie przebiega według określonego procesu i nie wymaga formalnego dokumentowania wyników. Jego głównym celem jest wykrywanie anomalii.
* **Przejrzenie** (ang. walkthrough). Jest prowadzone przez autora. Może służyć wielu celom takim jak ocena jakości i budowanie zaufania do produktu pracy, edukowanie
przeglądających, osiągnięcie konsensusu, generowanie nowych pomysłów, motywowanie autorów do rozwoju i stworzenie im warunków do tego oraz wykrywanie anomalii. Przed rozpoczęciem przejrzenia przeglądający mogą przeprowadzić przegląd indywidualny, ale nie jest to konieczne.
* **Przegląd techniczny** (ang. technical review). Prowadzony przez moderatora i wykonywany przez przeglądających, którzy dysponują odpowiednimi kwalifikacjami
technicznymi. Celem przeglądu technicznego jest osiągnięcie konsensusu i podjęcie decyzji dotyczących problemu technicznego, ale także wykrywanie anomalii, ocena jakości i budowanie zaufania do produktu pracy, generowanie nowych pomysłów oraz motywowanie autorów do rozwoju i stworzenie im warunków do tego.
* **Inspekcja** (ang. inspection). Najbardziej formalny rodzaj przeglądu, przebiega zgodnie z pełnym procesem opisanym w sekcji 3.2.2. Głównym celem jest wykrycie jak
największej liczby anomalii. Inne cele to ocena jakości, budowanie zaufania do produktu pracy oraz motywowanie autorów do rozwoju i stworzenie im warunków do tego. Podczas inspekcji zbiera się metryki wykorzystywane później do doskonalenia cyklu wytwarzania oprogramowania, w tym samego procesu inspekcji. W ramach inspekcji autor nie może pełnić roli lidera przeglądu ani protokolanta.

### 3.2.5. Czynniki sukcesu związane z przeglądami

Czynniki decydujące o sukcesie przeglądów to między innymi:

* określenie jasnych celów i mierzalnych kryteriów wyjścia (ocena uczestników nigdy nie powinna być celem przeglądu),
* wybór odpowiedniego typu przeglądu, aby umożliwić osiągnięcie założonych celów i dostosować przegląd do rodzaju produktu pracy, uczestników przeglądu, potrzeb projektu i kontekstu,
* przeprowadzanie przeglądów dla małych partii materiału, aby przeglądający nie tracili koncentracji podczas przeglądu indywidualnego lub spotkania przeglądowego (jeśli się odbywa),
* przekazywanie interesariuszom i autorom informacji zwrotnych z przeglądów, aby mogli doskonalić produkt i usprawniać swoje działania (patrz sekcja 3.2.1),
* zapewnienie uczestnikom odpowiedniego czasu na przygotowanie się do przeglądu,
* wsparcie kierownictwa dla procesu przeglądu,
* włączenie przeglądów w kulturę organizacyjną w celu promowania poszerzania wiedzy i doskonalenia procesów,
* zapewnienie odpowiednich szkoleń wszystkim uczestnikom, aby wiedzieli, jak wypełniać swoje role,
* sprawne przeprowadzanie spotkań.
