# 4. Analiza i projektowanie testów (390 min)

## Słowa kluczowe

analiza wartości brzegowych, białoskrzynkowa technika testowania, czarnoskrzynkowa technika testowania, element pokrycia, kryteria akceptacji, podejście do testowania oparte na współpracy, podział na klasy równoważności, pokrycie, pokrycie gałęzi, pokrycie instrukcji kodu, technika testowania oparta na doświadczeniu, technika testowania, testowanie eksploracyjne, testowanie przejść pomiędzy stanami, testowanie w oparciu o tablicę decyzyjną, testowanie w oparciu o listę kontrolną, wytwarzanie sterowane testami akceptacyjnymi, zgadywanie błędów

## Cele nauczania dla rozdziału 4

4.1 Ogólna charakterystyka technik testowania
    FL-4.1.1 (K2) Rozróżniać czarnoskrzynkowe techniki testowania, białoskrzynkowe techniki testowania oraz techniki testowania oparte na doświadczeniu.
4.2 Czarnoskrzynkowe techniki testowania
    FL-4.2.1 (K3) Zastosować technikę podziału na klasy równoważności, aby zaprojektować przypadki testowe.
    FL-4.2.2 (K3) Zastosować technikę analizy wartości brzegowych, aby zaprojektować przypadki testowe.
    FL-4.2.3 (K3) Zastosować technikę testowania w oparciu o tablicę decyzyjną, aby zaprojektować przypadki testowe.
    FL-4.2.4 (K3) Zastosować technikę testowania przejść pomiędzy stanami, aby zaprojektować przypadki testowe.
4.3 Białoskrzynkowe techniki testowania
    FL-4.3.1 (K2) Wyjaśnić technikę testowania instrukcji.
    FL-4.3.2 (K2) Wyjaśnić technikę testowania gałęzi.
    FL-4.3.3 (K2) Wyjaśnić korzyści wynikające z testowania białoskrzynkowego.
4.4 Techniki testowania oparte na doświadczeniu
    FL-4.4.1 (K2) Wyjaśnić technikę zgadywania błędów.
    FL-4.4.2 (K2) Wyjaśnić technikę testowania eksploracyjnego.
    FL-4.4.3 (K2) Wyjaśnić technikę testowania w oparciu o listę kontrolną.
4.5 Podejścia do testowania oparte na współpracy
    FL-4.5.1 (K2) Wyjaśnić, w jaki sposób należy pisać historyjki użytkownika we współpracy z programistami i przedstawicielami jednostek biznesowych.
    FL-4.5.2 (K2) Klasyfikować różne sposoby pisania kryteriów akceptacji.
    FL-4.5.3 (K3) Zastosować metodę wytwarzania sterowanego testami akceptacyjnymi (ATDD), aby zaprojektować przypadki testowe.

## 4.1. Ogólna charakterystyka technik testowania

Techniki testowania wspierają testera w analizie testów (co testować) i projektowaniu testów (jak testować). Pomagają w opracowaniu stosunkowo niewielkiego, ale wystarczającego zestawu przypadków testowych w sposób systematyczny. Pomagają również testerowi w definiowaniu warunków testowych, identyfikowaniu elementów pokrycia i identyfikowaniu danych testowych podczas analizy i projektowania testów. Więcej informacji na temat technik testowania można znaleźć w normie ISO/IEC/IEEE 29119-4 oraz w publikacjach (Beizer 1990, Craig 2002, Copeland 2004, Koomen 2006, Jorgensen 2014, Ammann 2016, Forgács 2019).

W niniejszym sylabusie techniki testowania są klasyfikowane jako czarnoskrzynkowe, białoskrzynkowe oraz oparte na doświadczeniu.

**Czarnoskrzynkowe techniki testowania** (zwane również technikami opartymi na specyfikacji) opierają się na analizie zachowania przedmiotu testów bez odniesienia do jego wewnętrznej
struktury. Dlatego też przypadki testowe są niezależne od sposobu implementacji oprogramowania. W konsekwencji, jeśli implementacja ulegnie zmianie, ale wymagane zachowanie pozostanie takie samo, przypadki testowe nadal będą aktualne.

**Białoskrzynkowe techniki testowania** (zwane również technikami opartymi na strukturze) opierają się na analizie wewnętrznej struktury i przetwarzania przedmiotu testów. Ponieważ
przypadki testowe są zależne od sposobu zaprojektowania oprogramowania, można je tworzyć dopiero po zaprojektowaniu lub implementacji przedmiotu testów.

**Techniki testowania oparte na doświadczeniu** wykorzystują wiedzę i doświadczenie testerów do projektowania i implementacji testów. Skuteczność tych technik zależy w dużej mierze
od umiejętności testera. Techniki te pozwalają wykrywać defekty, które mogły zostać pominięte przy użyciu czarnoskrzynkowych i białoskrzynkowych technik testowania. Dlatego też techniki testowania oparte na doświadczeniu stanowią uzupełnienie powyższych technik.

## 4.2. Czarnoskrzynkowe techniki testowania

W poniższych sekcjach omówiono cztery powszechnie stosowane techniki czarnoskrzynkowe:

* podział na klasy równoważności,
* analiza wartości brzegowych,
* testowanie w oparciu o tablicę decyzyjną,
* testowanie przejść pomiędzy stanami.

### 4.2.1. Podział na klasy równoważności

Technika podziału na klasy równoważności dzieli dane na zbiory zwane klasami równoważności w oparciu o założenie, że wszystkie elementy danej klasy równoważności są przetwarzane w ten sam sposób przez przedmiot testów. Teoria stojąca za tą techniką zakłada więc, że jeśli przypadek testowy, który testuje jedną wartość z klasy równoważności, wykryje defekt, to defekt ten powinien zostać wykryty również przez przypadki testowe, które testują dowolną inną wartość z tej samej klasy równoważności. W związku z tym wystarczy jeden test dla każdej klasy równoważności.

Klasy równoważności można zidentyfikować dla każdego elementu danych związanego z przedmiotem testów, w tym danych wejściowych, wyjściowych, elementów konfiguracji,
wartości wewnętrznych, wartości związanych z czasem i parametrów interfejsu. Klasy równoważności mogą być ciągłe lub dyskretne, uporządkowane lub nieuporządkowane,
skończone lub nieskończone. Klasy równoważności muszą być rozłączne (nie mogą się nakładać) i niepuste.

W przypadku prostych przedmiotów testów podział na klasy równoważności zazwyczaj nie nastręcza trudności, ale w praktyce zrozumienie, w jaki sposób przedmiot testów będzie traktował różne wartości, jest często skomplikowane. Dlatego przy dokonywaniu podziału na klasy równoważności należy zachować ostrożność.

Klasa równoważności zawierająca wartości poprawne nazywana jest poprawną klasą równoważności, a ta zawierająca wartości niepoprawne – niepoprawną klasą równoważności.
Definicje wartości poprawnych i niepoprawnych mogą się różnić w zależności od zespołów i organizacji. Na przykład wartości poprawne mogą być interpretowane jako te, które powinny być przetwarzane przez przedmiot testów, lub jako te, dla których specyfikacja definiuje sposób ich przetwarzania. Wartości niepoprawne mogą być interpretowane jako te, które powinny być ignorowane lub odrzucane przez przedmiot testów, lub jako te, dla których specyfikacja nie definiuje przetwarzania przez przedmiot testów.

W technice podziału na klasy równoważności elementami pokrycia są klasy równoważności. Aby osiągnąć 100% pokrycia przy użyciu tej techniki, przypadki testowe muszą sprawdzić wszystkie zidentyfikowane klasy równoważności (w tym niepoprawne), pokrywając każdą z nich co najmniej raz. Pokrycie mierzy się jako liczbę klas równoważności sprawdzonych przez co najmniej jeden przypadek testowy, podzieloną przez całkowitą liczbę zidentyfikowanych klas równoważności, a uzyskaną wartość wyraża się w procentach.

Często element testowy zawiera wiele grup klas równoważności (np. elementy testowe z więcej niż jednym parametrem wejściowym), co oznacza, że przypadek testowy pokrywa jednocześnie
klasy równoważności pochodzące z różnych grup klas równoważności. Najprostszym kryterium pokrycia w takim przypadku jest pokrycie „każdy wybór” (ang. each choice) (Ammann 2016). Pokrycie to wymaga, aby przypadki testowe sprawdzały każdą klasę równoważności z każdej grupy klas przynajmniej raz. Pokrycie „każdy wybór” nie bierze pod uwagę kombinacji klas równoważności.

### 4.2.2. Analiza wartości brzegowych

Analiza wartości brzegowych to technika testowania oparta na sprawdzaniu wartości leżących na brzegach klas równoważności. Dlatego może być stosowana tylko w przypadku klas
uporządkowanych. Wartościami brzegowymi klasy równoważności są jej minimalna i maksymalna wartość. W przypadku tej techniki, jeśli dwa elementy należą do tej samej klasy
równoważności, wszystkie elementy pomiędzy nimi również muszą należeć do tej klasy.

Analiza wartości brzegowych koncentruje się na wartościach brzegowych, ponieważ programiści często popełniają błędy (tzw. „błędy o jeden”) powodujące defekty związane z tymi właśnie wartościami. Typowe defekty wykrywane przez analizę wartości brzegowych znajdują się zatem w miejscach, gdzie zaimplementowane granice klas równoważności są umieszczone w pozycjach powyżej lub poniżej zamierzonych pozycji lub są całkowicie pominięte.

Niniejszy sylabus omawia dwie wersje analizy wartości brzegowych: dwupunktową i trójpunktową. Różnią się one pod względem elementów pokrycia przypadających na każdą
ze zidentyfikowanych wartości brzegowych, które należy wykonać, aby osiągnąć 100% pokrycia.

W dwupunktowej analizie wartości brzegowych (Craig 2002, Myers 2011) dla każdej wartości brzegowej istnieją dwa elementy pokrycia: ta wartość brzegowa oraz jej najbliższy sąsiad należący do sąsiedniej klasy równoważności. Aby osiągnąć 100% pokrycia za pomocą tego wariantu techniki, przypadki testowe muszą sprawdzać wszystkie elementy pokrycia, tj. wszystkie zidentyfikowane wartości brzegowe wszystkich klas równoważności. Pokrycie mierzy się jako liczbę sprawdzonych wartości brzegowych podzieloną przez całkowitą liczbę zidentyfikowanych wartości brzegowych i wyraża się je w procentach.

W trójpunktowej analizie wartości brzegowych (Koomen 2006, O’Regan 2019) dla każdej wartości brzegowej istnieją trzy elementy pokrycia: ta wartość brzegowa oraz jej obie sąsiednie wartości. Dlatego w tym wariancie techniki niektóre elementy pokrycia mogą nie być wartościami brzegowymi. Aby osiągnąć 100% pokrycia za pomocą tego wariantu techniki, przypadki testowe muszą sprawdzać wszystkie elementy pokrycia, tj. wszystkie zidentyfikowane wartości brzegowe i ich sąsiednie wartości. Pokrycie mierzy się jako liczbę sprawdzonych wartości brzegowych i ich sąsiednich wartości podzieloną przez całkowitą liczbę zidentyfikowanych wartości brzegowych i ich sąsiednich wartości i wyraża się je w procentach.

Wariant trójpunktowy jest bardziej rygorystyczny niż dwupunktowy, ponieważ może wykryć defekty pominięte przez wariant dwupunktowy. Na przykład, jeśli decyzja „if (x ≤ 10) …” zostanie nieprawidłowo zaimplementowana jako „if (x = 10) …”, dane testowe pochodzące z wariantu dwupunktowego (x = 10, x = 11) nie wykryją tego defektu. Jednak wartość x = 9, wymagana przez wariant trójpunktowy, prawdopodobnie ją wykryje.

### 4.2.3. Testowanie w oparciu o tablicę decyzyjną

Tablice decyzyjne służą do testowania implementacji wymagań opisujących, w jaki sposób różne kombinacje warunków prowadzą do różnych wyników. Tablice decyzyjne są skutecznym
sposobem modelowania złożonej logiki, takiej jak reguły biznesowe. Podczas tworzenia tablic decyzyjnych definiuje się warunki i wynikające z nich akcje systemu.
Warunki i akcje tworzą wiersze tablicy. Każda kolumna odpowiada regule decyzyjnej, która definiuje unikalną kombinację warunków wraz z powiązanymi akcjami. W ograniczonych
tablicach decyzyjnych wszystkie wartości warunków i akcji (z wyjątkiem nieistotnych lub niemożliwych do spełnienia; patrz poniżej) są przedstawiane jako wartości logiczne (prawda lub fałsz). W uogólnionych tablicach decyzyjnych niektóre lub wszystkie warunki i akcje przyjmują wiele wartości (np. zakresy liczb, klasy równoważności, wartości dyskretne).

Notacja dla warunków jest następująca:

* „P” (prawda) oznacza, że warunek jest spełniony.
* „F” (fałsz) oznacza, że warunek nie jest spełniony. 
* Symbol „–” oznacza, że wartość warunku nie ma znaczenia dla wyniku akcji, 
* a „N/A” („nie dotyczy”) oznacza, że warunek nie występuje dla danej reguły. 

W przypadku akcji „X” oznacza, że akcja powinna zostać wykonana, a puste pole oznacza, że akcja nie powinna zostać wykonana. 

Można również stosować inne notacje.

Pełna tablica decyzyjna ma tyle kolumn, ile jest niezbędne do pokrycia każdej kombinacji warunków. Tablicę można uprościć, usuwając kolumny zawierające niemożliwe do spełnienia
kombinacje warunków. Można ją również zminimalizować, łącząc kolumny, w których niektóre warunki nie mają wpływu na wynik, w jedną kolumnę. Algorytmy minimalizacji tablicy decyzyjnej wykraczają poza zakres niniejszego sylabusa.

W testowaniu tablicy decyzyjnej elementami pokrycia są jej kolumny zawierające możliwe do spełnienia kombinacje warunków. Aby osiągnąć 100% pokrycia przy użyciu tej techniki,
przypadki testowe muszą sprawdzać wszystkie te kolumny. Pokrycie mierzy się jako liczbę sprawdzonych kolumn podzieloną przez całkowitą liczbę kolumn i wyraża się je w procentach.
Zaletą testowania w oparciu o tablicę decyzyjną jest to, że zapewnia ono systematyczne podejście do zidentyfikowania wszystkich kombinacji warunków, które w innym przypadku mogłyby zostać przeoczone. Pomaga również znaleźć luki lub sprzeczności w wymaganiach. Jeśli istnieje wiele warunków, sprawdzenie wszystkich reguł decyzyjnych może być czasochłonne, ponieważ liczba reguł rośnie wykładniczo wraz z liczbą warunków. W takim przypadku, aby zmniejszyć liczbę reguł, które należy sprawdzić, można zminimalizować tablicę decyzyjną lub zastosować podejście oparte na ryzyku.

### 4.2.4. Testowanie przejść pomiędzy stanami

Diagram stanów umożliwia modelowanie zachowania systemu poprzez zobrazowanie jego możliwych stanów i poprawnych przejść między nimi. Przejście jest inicjowane przez zdarzenie,
które może być dodatkowo kwalifikowane przez warunek dozoru. Przyjmuje się, że przejścia są natychmiastowe i mogą niekiedy powodować wykonanie przez oprogramowanie określonej akcji. Typowa notacja stosowana do oznaczania przejść ma postać „zdarzenie [warunek dozoru] / akcja”, przy czym warunki dozoru i akcje można pominąć, jeśli nie istnieją lub są nieistotne z punktu widzenia testera.

Tablica stanów jest modelem równoważnym diagramowi stanów. Jej wiersze odpowiadają stanom, a kolumny – zdarzeniom (wraz z ewentualnymi warunkami dozoru). Wpisy w tablicy
stanów odpowiadają przejściom i zawierają stan docelowy, a także akcje, jeśli zostały zdefiniowane. W przeciwieństwie do diagramu stanów, tablica stanów wyraźnie pokazuje
przejścia niepoprawne, reprezentowane jako puste komórki w tablicy.

Przypadek testowy oparty na diagramie stanów lub tablicy stanów to sekwencja zdarzeń, która skutkuje sekwencją zmian stanów (i wykonaniem akcji, jeśli są zdefiniowane). Jeden przypadek testowy może pokrywać wiele przejść pomiędzy stanami.

Istnieje wiele kryteriów pokrycia dla testowania przejść pomiędzy stanami. Niniejszy sylabus omawia trzy z nich.

W **pokryciu wszystkich stanów** elementami pokrycia są stany. Aby osiągnąć 100% tego pokrycia, przypadki testowe muszą osiągnąć każdy stan co najmniej raz. Pokrycie mierzy się jako liczbę osiągniętych stanów podzieloną przez całkowitą liczbę stanów i wyraża się je w procentach.

W **pokryciu przejść poprawnych** (zwanym również pokryciem 0-przełączeń) elementami pokrycia są pojedyncze poprawne przejścia. Aby osiągnąć 100% tego pokrycia, przypadki testowe
muszą wykonać każde poprawne przejście co najmniej raz. Pokrycie mierzy się jako liczbę wykonanych poprawnych przejść podzieloną przez całkowitą liczbę poprawnych przejść i wyraża
się je w procentach.

W **pokryciu wszystkich przejść** elementami pokrycia są wszystkie przejścia pokazane w tablicy stanów. Aby osiągnąć 100% tego pokrycia, przypadki testowe muszą wykonać każde poprawne przejście co najmniej raz i podjąć próbę wykonania każdego niepoprawnego przejścia. Przetestowanie tylko jednego niepoprawnego przejścia w jednym przypadku testowym pomaga
uniknąć maskowania defektów, tj. sytuacji, w której jeden defekt uniemożliwia wykrycie innego. Pokrycie mierzy się jako iloraz liczby poprawnych i niepoprawnych przejść, które zostały wykonane lub w przypadku których podjęto próbę wykonania za pomocą przypadków testowych przez łączną liczbę poprawnych i niepoprawnych przejść i wyraża się je w procentach.

Pokrycie wszystkich stanów jest słabsze niż pokrycie przejść poprawnych, ponieważ zazwyczaj można je osiągnąć bez wykonywania wszystkich przejść. Pokrycie przejść poprawnych jest
najczęściej stosowanym kryterium pokrycia. Osiągnięcie pełnego pokrycia przejść poprawnych gwarantuje pełne pokrycie wszystkich stanów. Osiągnięcie pełnego pokrycia wszystkich przejść gwarantuje zarówno pełne pokrycie wszystkich stanów, jak i pełne pokrycie przejść poprawnych i powinno być minimalnym wymaganiem dla oprogramowania krytycznego ze względów bezpieczeństwa.

## 4.3. Białoskrzynkowe techniki testowania

Ze względu na ich popularność i prostotę, w tym podrozdziale skupiono się na dwóch technikach testowania białoskrzynkowego związanych z kodem:

* testowanie instrukcji,
* testowanie gałęzi.

Istnieją bardziej rygorystyczne techniki testowania białoskrzynkowego, które są stosowane w przypadku systemów krytycznych ze względów bezpieczeństwa, w systemach kluczowych dla
działalności przedsiębiorstwa oraz w środowiskach wymagających wysokiego poziomu integralności w celu uzyskania pełniejszego pokrycia kodu. Istnieją również techniki testowania
białoskrzynkowego stosowane na wyższych poziomach testów (np. testowanie API) lub wykorzystujące pokrycie niezwiązane z kodem (np. pokrycie neuronów w testowaniu sieci neuronowych). Techniki te nie są omawiane w niniejszym sylabusie.

### 4.3.1. Testowanie instrukcji i pokrycie instrukcji kodu

W testowaniu instrukcji elementami pokrycia są instrukcje wykonywalne. Celem tej techniki jest zaprojektowanie przypadków testowych, które sprawdzają instrukcje w kodzie aż do osiągnięcia akceptowalnego poziomu pokrycia. Pokrycie mierzy się jako liczbę instrukcji sprawdzonych przez przypadki testowe podzieloną przez łączną liczbę instrukcji wykonywalnych w kodzie i wyraża się je w procentach.

Osiągnięcie 100% pokrycia instrukcji gwarantuje, że każda instrukcja wykonywalna została sprawdzona co najmniej raz. W szczególności oznacza to, że każda instrukcja zawierająca defekt zostanie wykonana, co może spowodować awarię wskazującą na obecność defektu. Jednak sprawdzenie instrukcji za pomocą przypadku testowego nie zawsze wywoła awarię, na przykład może nie wykryć defektów zależnych od danych (np. dzielenie przez zero, które kończy się niepowodzeniem tylko wtedy, gdy mianownik jest zerem). Ponadto uzyskanie 100% pokrycia instrukcji nie gwarantuje, że cała logika decyzyjna została przetestowana, ponieważ testy mogą nie sprawdzić wszystkich gałęzi w kodzie (patrz sekcja 4.3.2).

### 4.3.2. Testowanie gałęzi i pokrycie gałęzi

Gałąź to przepływ sterowania między dwoma wierzchołkami w grafie przepływu sterowania, modelującym możliwe sekwencje wykonywania instrukcji kodu w przedmiocie testów1. Każdy
przepływ sterowania może być bezwarunkowy (kod liniowy) lub warunkowy (tj. wynik decyzji). 

W testowaniu gałęzi elementami pokrycia są gałęzie, a celem jest zaprojektowanie przypadków testowych sprawdzających gałęzie w kodzie do momentu osiągnięcia akceptowalnego poziomu pokrycia. Pokrycie mierzy się jako liczbę gałęzi sprawdzonych przez przypadki testowe podzieloną przez całkowitą liczbę gałęzi w kodzie i wyraża się je w procentach.

Uzyskanie 100% pokrycia gałęzi oznacza, że każda gałąź w kodzie, zarówno bezwarunkowa jak i warunkowa, została sprawdzona przez przypadki testowe. Gałęzie warunkowe zazwyczaj
odpowiadają wynikowi („prawda” lub „fałsz”) decyzji if-then, wynikowi z instrukcji switch-case lub wynikowi decyzji o wyjściu lub kontynuowaniu pętli. Jednak sprawdzenie gałęzi za pomocą przypadku testowego nie zawsze wykryje defekt (np. może nie wykryć defektów, których wystąpienie wymaga wykonania określonej ścieżki w kodzie).

Pokrycie gałęzi subsumuje pokrycie instrukcji. Oznacza to, że każdy zbiór przypadków testowych osiągający 100% pokrycia gałęzi osiąga również 100% pokrycia instrukcji (ale nie odwrotnie).

### 4.3.3. Korzyści wynikające z testowania białoskrzynkowego

Podstawową zaletą wszystkich białoskrzynkowych technik testowania jest to, że podczas testowania brana jest pod uwagę cała implementacja oprogramowania, co ułatwia wykrywanie
defektów nawet wtedy, gdy specyfikacja oprogramowania jest niejasna, nieaktualna lub niekompletna. Wadą z kolei jest to, że jeśli oprogramowanie nie implementuje jakiegoś
wymagania, testowanie białoskrzynkowe może nie wykryć tego pominięcia (Watson 1996).

Techniki białoskrzynkowe mogą być stosowane w testowaniu statycznym (np. podczas próbnych przebiegów kodu, ang. dry runs). Nadają się również do przeglądów kodu, który nie jest jeszcze gotowy do uruchomienia (Hetzel 1988), pseudokodu oraz innych mechanizmów logicznych, które można modelować za pomocą diagramów przepływu (np. takich jak diagram aktywności).

Wykonanie jedynie testowania czarnoskrzynkowego nie pozwala zmierzyć rzeczywistego pokrycia kodu. Miary pokrycia stosowane w technikach białoskrzynkowych zapewniają obiektywny pomiar pokrycia oraz informacje niezbędne do wygenerowania dodatkowych testów w celu zwiększenia tego pokrycia, a tym samym zwiększenia zaufania do kodu.

## 4.4. Techniki testowania oparte na doświadczeniu

Powszechnie stosowane techniki testowania oparte na doświadczeniu omówione w poniższych sekcjach to:

* zgadywanie błędów (ang. error guessing),
* testowanie eksploracyjne,
* testowanie oparte na liście kontrolnej.

Zazwyczaj przyjmuje się, że wierzchołek w grafie przepływu sterowania reprezentuje nie pojedynczą instrukcję wykonywalną, lecz tzw. blok podstawowy kodu (czyli liniową sekwencję instrukcji, które zawsze muszą być wykonane albo w całości albo w ogóle) [przyp. tłum.].

### 4.4.1. Zgadywanie błędów

Zgadywanie błędów to technika testowania stosowana w celu przewidzenia wystąpienia błędów, defektów i awarii w oparciu o wiedzę testera, dotyczącą w szczególności:

* sposobu działania aplikacji w przeszłości,
* typów błędów popełnianych przez programistów i wynikających z nich typów defektów,
* rodzajów awarii, które wystąpiły w innych, podobnych aplikacjach.

Błędy, defekty i awarie mogą być związane z: danymi wejściowymi (np. brak akceptacji poprawnych danych wejściowych, błędne lub brakujące parametry), danymi wyjściowymi
(np. nieprawidłowy format lub wynik), logiką (np. brakujące przypadki, nieprawidłowy operator), obliczeniami (np. nieprawidłowy operand, błędne obliczenie), interfejsami (np. niezgodność parametrów, niekompatybilny typ) lub danymi (np. błędna inicjalizacja, niewłaściwy typ).

Atak usterek (ang. fault attack) to metodyczne podejście do zgadywania błędów. Wymaga on od testera stworzenia lub uzyskania listy możliwych błędów, defektów i awarii oraz
zaprojektowania testów, które zidentyfikują defekty związane z błędami, ujawnią defekty lub spowodują awarie z listy. Listy te można tworzyć w oparciu o doświadczenie, dane dotyczące defektów i awarii lub powszechną wiedzę na temat przyczyn awarii oprogramowania (np. taksonomie defektów).

Więcej informacji na temat zgadywania błędów i ataku usterek można znaleźć w (Whittaker 2002, Whittaker 2003, Andrews 2006).

### 4.4.2. Testowanie eksploracyjne

W testowaniu eksploracyjnym testy są jednocześnie projektowane, wykonywane i oceniane, podczas gdy tester poznaje przedmiot testów. Testowanie to służy do uzyskania większej wiedzy
na temat przedmiotu testów, głębszego zbadania go za pomocą ukierunkowanych testów oraz stworzenia testów dla obszarów, które nie zostały jeszcze przetestowane.

Testowanie eksploracyjne może być wykonywane jako tzw. testowanie w sesjach, w celu ustrukturyzowania całego procesu testowania. W podejściu tym testowanie eksploracyjne jest
wykonywane w określonym przedziale czasowym. Tester prowadzi testy korzystając z karty opisu testu (ang. test charter) zawierającej cele testów. Po zakończeniu sesji testowej zazwyczaj odbywa się spotkanie podsumowujące, które obejmuje dyskusję między testerem a interesariuszami zainteresowanymi wynikami sesji testowej. W tym podejściu cele testów mogą
być traktowane jako warunki testowe wysokiego poziomu. Elementy pokrycia są identyfikowane i sprawdzane podczas sesji testowej. Tester może korzystać z arkuszy sesji testowej, aby
dokumentować wykonane czynności i dokonane odkrycia.

Testowanie eksploracyjne jest przydatne, gdy specyfikacje są niepełne lub nieodpowiednie lub gdy testowanie podlega znacznej presji czasowej. Testowanie eksploracyjne jest również
przydatne jako uzupełnienie innych, bardziej formalnych technik testowania. Testowanie eksploracyjne będzie bardziej skuteczne, jeśli tester ma doświadczenie, posiada wiedzę
dziedzinową i wysoki poziom niezbędnych umiejętności, takich jak umiejętności analityczne, ciekawość i kreatywność (patrz sekcja 1.5.1).

Testowanie eksploracyjne może obejmować wykorzystanie innych technik testowania (np. podział na klasy równoważności). Więcej informacji na temat testowania eksploracyjnego można znaleźć w (Kaner 1999, Whittaker 2009, Hendrickson 2013).

### 4.4.3. Testowanie w oparciu o listę kontrolną

W testowaniu w oparciu o listę kontrolną tester projektuje, implementuje i wykonuje testy w celu pokrycia warunków testowych z listy kontrolnej. Listy kontrolne mogą być tworzone w oparciu o doświadczenie, znajomość oczekiwań użytkownika lub wiedzę na temat przyczyn i objawów awarii oprogramowania. Listy kontrolne nie powinny zawierać elementów, które można sprawdzić automatycznie, elementów lepiej nadających się jako kryteria wejścia bądź kryteria wyjścia lub elementów, które są sformułowane w zbyt ogólny sposób (Brykczynski 1999).

Elementy listy kontrolnej są często sformułowane w formie pytań. Każdy element powinien być możliwy do sprawdzenia oddzielnie i bezpośrednio. Elementy mogą odnosić się do wymagań,
właściwości interfejsu graficznego, charakterystyk jakościowych lub innych form warunków testowych. Listy kontrolne mogą być tworzone w celu wsparcia różnych typów testów, w tym
testów funkcjonalnych i niefunkcjonalnych (np. 10 heurystyk użyteczności (Nielsen 1994)).

Niektóre elementy listy kontrolnej mogą z czasem stopniowo tracić na skuteczności, ponieważ programiści nauczą się unikać popełniania tych samych błędów. Konieczne może być również
dodanie nowych elementów, aby odzwierciedlić nowo wykryte defekty o wysokim stopniu krytyczności. Dlatego listy kontrolne powinny być regularnie aktualizowane na podstawie analizy
defektów. Należy jednak uważać, aby lista kontrolna nie stała się zbyt obszerna (Gawande 2009).

W przypadku braku szczegółowych przypadków testowych testowanie w oparciu o listy kontrolne zapewnia niezbędne wytyczne i pewien stopień spójności testowania. Jeśli listy kontrolne są wysokopoziomowe, prawdopodobne jest wystąpienie pewnej zmienności w rzeczywistym testowaniu, co może skutkować większym pokryciem, ale mniejszą powtarzalnością testów.

## 4.5. Podejścia do testowania oparte na współpracy

Każda z technik opisanych w podrozdziałach 4.2, 4.3 i 4.4 ma określony cel związany z wykrywaniem defektów. Podejścia do testowania oparte na współpracy koncentrują się również
na unikaniu defektów poprzez zapewnienie współpracy i wymianę informacji.

### 4.5.1. Wspólne pisanie historyjek użytkownika

Historyjka użytkownika (ang. user story) reprezentuje cechę systemu cenną dla użytkownika lub nabywcy. Historyjki użytkowników mają trzy kluczowe aspekty (Jeffries 2000), tzw. „3C”:
* **karta** (ang. card) – nośnik opisujący historyjkę użytkownika (np. karta katalogowa, wpis w kartotece elektronicznej),
* **rozmowa** (ang. conversation) – wyjaśnia, w jaki sposób oprogramowanie będzie używane (może być udokumentowana lub ustna),
* **potwierdzenie** (ang. confirmation) – czyli kryteria akceptacji (patrz sekcja 4.5.2).

Najpopularniejszym formatem historyjki użytkownika jest „Jako [rola], chcę [cel do osiągnięcia], aby móc [wynikająca z tego wartość biznesowa dla roli]”, po czym następują kryteria akceptacji.

Wspólne tworzenie historyjki użytkownika może wykorzystywać techniki takie jak burza mózgów i tworzenie map myśli. Współpraca pozwala zespołowi uzyskać wspólną wizję tego, co powinno zostać dostarczone, biorąc pod uwagę trzy perspektywy: biznesową, programistyczną i testową.

Dobre historyjki użytkownika powinny być niezależne, negocjowalne, wartościowe, możliwe do oszacowania, niewielkie i możliwe do przetestowania (ang. Independent, Negotiable,
Valuable, Estimable, Small, Testable – INVEST). Jeśli interesariusz nie wie, jak przetestować historyjkę użytkownika, może to oznaczać, że nie jest ona wystarczająco jasna, nie odzwierciedla czegoś wartościowego dla interesariusza lub że interesariusz po prostu potrzebuje pomocy w testowaniu (Wake 2003).

### 4.5.2. Kryteria akceptacji

Kryteria akceptacji dla historyjki użytkownika to warunki, które muszą zostać spełnione, aby została ona zaakceptowana przez interesariuszy. Z tej perspektywy kryteria akceptacji można postrzegać jako warunki testowe, które powinny być sprawdzane podczas testów. Kryteria akceptacji są zazwyczaj wynikiem rozmowy (patrz sekcja 4.5.1).

Kryteria akceptacji służą do:

* określenia zakresu historyjki użytkownika,
* osiągnięcia konsensusu wśród interesariuszy,
* opisania zarówno pozytywnych, jak i negatywnych scenariuszy,
* stworzenia podstawy do testowania akceptacyjnego historyjek użytkownika (patrz sekcja 4.5.3),
* umożliwienia dokładnego planowania i szacowania.

Istnieje wiele sposobów zapisywania kryteriów akceptacji dla historyjki użytkownika. Dwa najpopularniejsze formaty to:

* zorientowany na scenariusze (np. format Given/When/Then stosowany w wytwarzaniu sterowanym zachowaniem, patrz sekcja 2.1.3),
* zorientowany na reguły (np. lista kontrolna w punktach lub tabelaryczna forma mapowania danych wejściowych i wyjściowych).

Większość kryteriów akceptacji można udokumentować w jednym z tych dwóch formatów. Zespół może też użyć innego formatu, o ile kryteria akceptacji są dobrze zdefiniowane i jednoznaczne.

### 4.5.3. Wytwarzanie sterowane testami akceptacyjnymi (ATDD)

Wytwarzanie sterowane testami akceptacyjnymi to podejście typu „najpierw test” (patrz sekcja2.1.3), zgodnie z którym przypadki testowe są tworzone przed zaimplementowaniem
historyjki użytkownika. Przypadki testowe są tworzone przez członków zespołu reprezentujących różne perspektywy, np. klientów, programistów i testerów (Adzic 2009). Przypadki testowe mogą być następnie wykonywane manualnie lub automatycznie.

Pierwszym krokiem jest warsztat specyfikacji, podczas którego członkowie zespołu analizują, omawiają i opisują historyjkę użytkownika oraz jej kryteria akceptacji (jeśli nie zostały jeszcze zdefiniowane). W trakcie tego procesu uzupełnia się braki, wyjaśnia się niejasności i usuwa defekty wykryte w historyjce użytkownika. Drugi krok to stworzenie przypadków testowych. Może to zrobić cały zespół lub indywidualnie tester. Przypadki testowe tworzy się w oparciu o kryteria
akceptacji i można je traktować jako przykłady działania oprogramowania. Pomaga to zespołowi w prawidłowej implementacji historyjki użytkownika.

Ponieważ przykłady i testy są tym samym, terminy te są często używane zamiennie. Podczas projektowania testów można stosować techniki testowania opisane w sekcjach 4.2, 4.3 i 4.4.

Zazwyczaj najpierw wykonuje się pozytywne przypadki testowe, czyli takie, które potwierdzają prawidłowe działanie (bez popełniania błędów i występowania wyjątków) i obejmują sekwencję czynności, w której wszystko przebiega zgodnie z oczekiwaniami. Po zakończeniu wykonywania pozytywnych przypadków testowych zespół powinien przeprowadzić testy negatywne. Na koniec zespół powinien uwzględnić niefunkcjonalne charakterystyki jakościowe (np. wydajność, użyteczność). Przypadki testowe powinny być wyrażone w sposób zrozumiały dla interesariuszy. Zazwyczaj zawierają one zdania w języku naturalnym, obejmujące niezbędne warunki wstępne (jeśli występują), dane wejściowe i warunki wyjściowe.

Przypadki testowe muszą obejmować wszystkie charakterystyki historyjki użytkownika i nie powinny wykraczać poza jej zakres. Natomiast kryteria akceptacji mogą szczegółowo opisywać
niektóre kwestie opisane w historyjce użytkownika. Ponadto żadne dwa przypadki testowe nie powinny opisywać tej samej charakterystyki historyjki użytkownika.

Jeśli przypadki testowe zostaną zapisane w formacie obsługiwanym przez strukturę do testów automatycznych, programiści mogą zautomatyzować ich wykonywanie pisząc kod pomocniczy
podczas implementacji funkcjonalności opisanej w historyjce użytkownika. Testy akceptacyjne stają się wówczas wykonywalnymi wymaganiami.