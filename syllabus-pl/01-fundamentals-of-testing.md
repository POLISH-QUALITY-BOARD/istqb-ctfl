# 1. Podstawy testowania – 180 minut {#fundamentals-of-testing}

## Słowa kluczowe

analiza testów, awaria, cel testów, dane testowe, debugowanie, defekt, implementacja testów, jakość, monitorowanie testów, nadzór nad testami, planowanie testów, podstawa testów, podstawowa przyczyna, pokrycie, pomyłka, procedura testowa, proces testowy, projektowanie testów, przedmiot testów, przypadek testowy, śledzenie powiązań, testalia, testowanie, ukończenie testów, walidacja, warunek testowy, weryfikacja, wykonywanie testów, wynik testu, zapewnienie jakości

## Cele nauczania dla rozdziału 1: {.learning-objectives}

1.1 Co to jest testowanie?
FL-1.1.1 (K1) Wskazać typowe cele testów.
FL-1.1.2 (K2) Odróżniać testowanie od debugowania.
1.2 Dlaczego testowanie jest niezbędne?
FL-1.2.1 (K2) Podać przykłady wskazujące, dlaczego testowanie jest niezbędne.
FL-1.2.2 (K1) Pamiętać, jaka jest relacja między testowaniem a zapewnieniem jakości.
FL-1.2.3 (K2) Odróżniać podstawową przyczynę, pomyłkę, defekt i awarię.
1.3 Zasady testowania
FL-1.3.1 (K2) Objaśnić siedem zasad testowania.
1.4 Czynności testowe, testalia i role związane z testami
FL-1.4.1 (K2) Wyjaśnić poszczególne czynności testowe i powiązane z nimi zadania.
FL-1.4.2 (K2) Wyjaśnić wpływ kontekstu na proces testowy.
FL-1.4.3 (K2) Rozróżniać testalia wspomagające czynności testowe.
FL-1.4.4 (K2) Wyjaśnić korzyści wynikające ze śledzenia powiązań.
FL-1.4.5 (K2) Porównać poszczególne role występujące w testowaniu.
1.5 Niezbędne umiejętności i dobre praktyki w dziedzinie testowania
FL-1.5.1 (K2) Podać przykłady ogólnych umiejętności wymaganych w testowaniu.
FL-1.5.2 (K1) Pamiętać, jakie są zalety podejścia „cały zespół”.
FL-1.5.3 (K2) Odróżniać korzyści i wady niezależności testowania.

## 1.1. Co to jest testowanie?

Systemy oprogramowania są integralną częścią naszego codziennego życia. Większość ludzi miała do czynienia z oprogramowaniem, które nie działało zgodnie z oczekiwaniami. Nieprawidłowo działające oprogramowanie może prowadzić do wielu problemów, w tym utraty pieniędzy, czasu lub reputacji firmy, a w skrajnych przypadkach nawet utraty zdrowia lub życia. Testowanie oprogramowania pozwala ocenić jego jakość i pomaga zmniejszyć ryzyko awarii podczas użytkowania.

Testowanie oprogramowania to zestaw czynności mających na celu wykrycie defektów i ocenę jakości produktów pracy. Produkty pracy poddawane takim testom nazywane są przedmiotem testów. Powszechnym błędnym przekonaniem na temat testowania jest to, że polega ono wyłącznie na wykonywaniu testów (tj. uruchamianiu oprogramowania i sprawdzaniu wyników testów). Jednak testowanie oprogramowania obejmuje również inne czynności i musi być dostosowane do cyklu życia oprogramowania (patrz rozdział 2).

Kolejnym powszechnym błędnym przekonaniem dotyczącym testowania jest to, że skupia się ono wyłącznie na weryfikacji przedmiotu testów. Testowanie obejmuje weryfikację, tj. sprawdzenie, czy system spełnia określone wymagania, a także walidację, tj. sprawdzanie, czy system spełnia potrzeby użytkowników i innych interesariuszy w swoim środowisku operacyjnym.

Testowanie może być dynamiczne lub statyczne. Testowanie dynamiczne wiąże się
z uruchamianiem oprogramowania, natomiast testowanie statyczne nie. Testowanie statyczne obejmuje przeglądy (patrz rozdział 3) i analizę statyczną. Testowanie dynamiczne wykorzystuje różne techniki testowania i podejścia do testów w celu wyprowadzania przypadków testowych (patrz rozdział 4).

Testowanie nie jest wyłącznie działaniem technicznym. Wymaga ono również odpowiedniego planowania, zarządzania, szacowania, monitorowania i nadzoru (patrz rozdział 5). Testerzy korzystają z narzędzi (patrz rozdział 6), ale należy pamiętać, że testowanie jest działaniem intelektualnym, wymagającym od testerów specjalistycznej wiedzy, umiejętności analitycznych oraz krytycznego i systemowego myślenia (Myers 2011, Roman 2018).

Więcej informacji na temat koncepcji testowania oprogramowania zawiera norma
ISO/IEC/IEEE 29119-1.

### 1.1.1. Cele testów {#test-objectives}

Typowe cele testów to:

* ocena produktów pracy, takich jak wymagania, historyjki użytkowników, projekty i kod,
* wywoływanie awarii i wykrywanie defektów,
* zapewnienie wymaganego pokrycia przedmiotu testów,
* zmniejszenie poziomu ryzyka związanego z nieodpowiednią jakością oprogramowania,
* weryfikacja, czy wyspecyfikowane wymagania zostały spełnione,
* dostarczanie informacji interesariuszom, aby umożliwić im podejmowanie świadomych decyzji,
* budowanie zaufania do jakości przedmiotu testów,
* sprawdzenie, czy przedmiot testów jest kompletny i działa zgodnie z oczekiwaniami
interesariuszy.

Cele testów mogą się różnić w zależności od kontekstu, który obejmuje testowany produkt, poziom testów, ryzyka, stosowany cykl wytwarzania oprogramowania (SDLC) oraz czynniki związane z kontekstem biznesowym, np. struktura korporacyjna, kwestie konkurencyjności lub czas wprowadzenia produktu na rynek.

### 1.1.2. Testowanie a debugowanie

Testowanie i debugowanie to odrębne czynności. Testowanie może wywołać awarie
spowodowane defektami w oprogramowaniu (testowanie dynamiczne) lub bezpośrednio wykryć defekty przedmiotu testów (testowanie statyczne).

Gdy testowanie dynamiczne (patrz rozdział 4) powoduje awarię, debugowanie polega na znalezieniu przyczyn tej awarii (defektów), analizie tych przyczyn i ich wyeliminowaniu. Typowy proces debugowania w tym przypadku obejmuje:

* odtworzenie awarii,
* diagnozę (znalezienie defektu),
* naprawę (usunięcie defektu).

Wykonywane następnie testy potwierdzające sprawdzają, czy poprawki rozwiązały problem. Najlepiej, aby testy potwierdzające były przeprowadzane przez tę samą osobę, która wykonywała wcześniejsze testy. Można również przeprowadzić testy regresji, aby sprawdzić, czy poprawki nie powodują awarii w innych częściach przedmiotu testów (więcej informacji na temat testowania potwierdzającego i testowania regresji znajduje się w sekcji 2.2.3).

Gdy testy statyczne wykryją defekt, debugowanie polega na jego usunięciu. Nie ma potrzeby odtwarzania ani diagnozowania, ponieważ testy statyczne wykrywają defekty bezpośrednio i nie mogą powodować awarii (patrz rozdział 3).

## 1.2. Dlaczego testowanie jest niezbędne?

Testowanie jako forma kontroli jakości pomaga w osiągnięciu uzgodnionych celów testów w ramach ustalonego zakresu, czasu, jakości i ograniczeń budżetowych. Wkład testowania w sukces przedsięwzięcia nie powinien ograniczać się do działań zespołu testowego. Każdy interesariusz może wykorzystać swoje umiejętności testowania, aby zwiększyć szanse na sukces projektu. Testowanie modułów, systemów i powiązanych produktów pracy (np. dokumentacji) pomaga w identyfikacji defektów w oprogramowaniu.

### 1.2.1. Znaczenie testowania dla powodzenia projektu

Testowanie stanowi opłacalny sposób wykrywania defektów. Defekty te można następnie usunąć (poprzez debugowanie – czynność niezwiązaną z testowaniem), więc testowanie pośrednio przyczynia się do poprawy jakości przedmiotów testów.

Testowanie stanowi środek bezpośredniej oceny jakości przedmiotu testów na różnych etapach cyklu życia oprogramowania. Środki te są wykorzystywane w ramach szerszej działalności związanej z zarządzaniem projektami, przyczyniając się do podejmowania decyzji o przejściu do kolejnego etapu cyklu wytwarzania oprogramowania, takiego jak decyzja o wydaniu.

Testowanie zapewnia użytkownikom pośrednią reprezentację w projekcie wytwórczym. Testerzy dbają o to, aby rozumiane przez nich potrzeby użytkowników były brane pod uwagę w całym cyklu wytwarzania. Alternatywą jest zaangażowanie reprezentatywnej grupy użytkowników w projekt wytwórczy, co zazwyczaj nie jest możliwe ze względu na wysokie koszty i brak odpowiednich użytkowników.

Testowanie może być również wymagane w celu spełnienia wymogów umów, przepisów prawa
lub zapewnienia zgodności z normami regulacyjnymi.

### 1.2.2. Testowanie a zapewnienie jakości (QA)

Chociaż terminy „testowanie” i „zapewnienie jakości” (QA – ang. quality assurance) są często używane zamiennie, to jednak testowanie i QA nie są tym samym.

Testowanie jest podejściem korygującym i zorientowanym na produkt, koncentrującym się na działaniach wspierających osiągnięcie odpowiedniego poziomu jakości. Testowanie jest główną formą kontroli jakości. Inne formy tej kontroli obejmują metody formalne (weryfikacja modelu czy formalne dowodzenie poprawności), symulację i prototypowanie. 

QA jest podejściem prewencyjnym i zorientowanym na procesy, koncentrującym się na ich wdrażaniu i doskonaleniu. Opiera się na założeniu, że prawidłowe stosowanie dobrego procesu pozwoli uzyskać dobry produkt. QA ma zastosowanie zarówno do procesów wytwarzania, jak i testowania, a odpowiedzialność za nie spoczywa na wszystkich uczestnikach projektu.

Wyniki testów są wykorzystywane zarówno przez QA, jak i przez testowanie. W testowaniu służą one do usuwania defektów, natomiast w QA dostarczają informacji zwrotnych na temat skuteczności procesów wytwarzania i testowania.

### 1.2.3. Pomyłki, defekty, awarie i podstawowe przyczyny

Ludzie popełniają błędy, które powodują defekty (usterki, bugi), a te z kolei mogą prowadzić do awarii. Powody popełniania błędów przez człowieka to np. presja czasu, złożoność produktów pracy, procesów, infrastruktury lub interakcji, zmęczenie lub brak odpowiedniego przeszkolenia.

Defekty można znaleźć w dokumentacji (np. w specyfikacja wymagań lub skrypcie testowym), w kodzie źródłowym lub w pomocniczym produkcie pracy (np. plik kompilacji). Niewykrycie defektów w produktach pracy wytworzonych we wcześniejszych etapach cyklu wytwarzania oprogramowania często prowadzi do wadliwych produktów pracy w późniejszych etapach tego cyklu. Wykonanie kodu zawierającego defekt może spowodować, że system nie wykona tego, co powinien, lub wykona coś, czego nie powinien, powodując awarię. Niektóre defekty zawsze powodują awarię po wykonaniu, podczas gdy inne powodują awarię tylko w określonych okolicznościach, a niektóre mogą nigdy nie powodować awarii.

Awarie mogą być spowodowane nie tylko błędami i defektami, ale też warunkami
środowiskowymi, na przykład, gdy promieniowanie lub działanie pola elektromagnetycznego powoduje nieprawidłowe działanie oprogramowania wbudowanego (ang. firmware).

Podstawowa przyczyna to podstawowy, źródłowy powód wystąpienia problemu (np. sytuacja prowadząca do pomyłki). Podstawowe przyczyny są identyfikowane w toku tzw. analizy przyczyny podstawowej (ang. root cause analysis), przeprowadzanej zwykle po wystąpieniu awarii lub wykryciu defektu. Uważa się, że wyeliminowanie podstawowej przyczyny (ang. root cause) może zapobiec lub zmniejszyć częstotliwość dalszych podobnych awarii lub defektów.

## 1.3. Zasady testowania

Na przestrzeni lat zaproponowano szereg zasad testowania, które stanowią ogólne wytyczne mające zastosowanie do wszystkich testów. Niniejszy sylabus opisuje siedem takich zasad.

**1. Testowanie ujawnia defekty, ale nie może dowieść ich braku.** Testowanie może wykazać istnienie defektów w przedmiocie testów, ale nie może udowodnić, że jest on od nich wolny (Buxton 1970). Testowanie zmniejsza prawdopodobieństwo, że defekty pozostaną niewykryte w przedmiocie testów, ale niewykrycie żadnych defektów nie jest dowodem poprawności przedmiotu testów.

**2. Testowanie gruntowne jest niemożliwe.** Testowanie wszystkiego jest niewykonalne,
z wyjątkiem trywialnych przypadków (Manna 1978). Zamiast przeprowadzać wyczerpujące testy, należy skupić się na technikach testowania (patrz rozdział 4), priorytetyzacji przypadków testowych (patrz sekcja 5.1.5) i testowaniu opartym na ryzyku (patrz podrozdział 5.2).

**3. Wczesne testowanie oszczędza czas i pieniądze.** Defekty usunięte na wczesnym etapie procesu nie spowodują kolejnych defektów w pochodnych produktach pracy. Koszt jakości zmniejszy się, ponieważ w późniejszym etapie cyklu wytwarzania oprogramowania wystąpi mniej awarii (Boehm 1981). Aby wcześnie wykryć defekty, należy jak najwcześniej rozpocząć zarówno testowanie statyczne (patrz rozdział 3), jak i testowanie dynamiczne (patrz rozdział 4).

**4. Defekty mogą się kumulować.** Niewielka liczba modułów systemu zawiera zazwyczaj
większość wykrytych defektów lub jest odpowiedzialna za większość awarii operacyjnych (Enders 1975). Zjawisko to ilustruje zasadę Pareto. Przewidywane skupiska defektów oraz rzeczywiste skupiska defektów zaobserwowane podczas testowania lub eksploatacji stanowią ważny wkład w testowanie oparte na ryzyku (patrz podrozdział 5.2).

**5. Testy ulegają zużyciu.** Jeśli te same testy są powtarzane wiele razy, stają się coraz mniej skuteczne w wykrywaniu nowych defektów (Beizer 1990). Aby przezwyciężyć ten efekt, może być konieczna modyfikacja istniejących testów i danych testowych oraz napisanie nowych testów. Jednak w niektórych przypadkach powtarzanie tych samych testów może być korzystne, np. w automatycznych testach regresji (patrz sekcja 2.2.3).

**6. Testowanie zależy od kontekstu.** Nie ma jednego uniwersalnego podejścia do testowania. Testowanie przebiega inaczej w różnych kontekstach (Kaner 2011).

**7. Przekonanie o braku defektów jest błędem.** Błędem jest oczekiwanie, że sama weryfikacja zapewni sukces systemu. Dokładne przetestowanie wszystkich wyspecyfikowanych wymagań i usunięcie wszystkich znalezionych defektów może nadal skutkować powstaniem systemu, który nie spełnia potrzeb i oczekiwań użytkowników, nie pomaga w osiągnięciu celów biznesowych klienta i jest gorszy od innych konkurencyjnych systemów. Oprócz weryfikacji należy zatem również przeprowadzać walidację (Boehm 1981).

## 1.4. Czynności testowe, testalia i role związane z testami

Testowanie zależy od kontekstu, ale istnieją typowe grupy czynności testowych, których pominięcie zmniejsza szanse osiągnięcia celów testów. Te grupy czynności testowych tworzą proces testowy. Dobór procesu testowego do danej sytuacji zależy od wielu czynników. To, jakie czynności testowe są uwzględnione w tym procesie testowym, w jaki sposób są one wdrażane i kiedy mają miejsce, jest zazwyczaj ustalane w ramach planowania testów z uwzględnieniem kontekstu (patrz podrozdział 5.1). Poniżej opisano ogólne aspekty tego procesu testowego w odniesieniu do czynności i zadań testowych, wpływu kontekstu, testaliów, śledzenia powiązań między podstawą testów a testaliami oraz ról występujących w testowaniu.
Więcej informacji na temat procesów testowych zawiera norma ISO/IEC/IEEE 29119-2.

### 1.4.1. Czynności i zadania testowe {#test-activities-and-tasks}

W procesie testowym wyróżnia się główne grupy czynności opisane poniżej. Chociaż wiele z tych czynności może sprawiać wrażenie logicznie uszeregowanych, często są one realizowane metodą iteracyjną lub równolegle. Ponadto zwykle wymagają one dostosowania do potrzeb konkretnego systemu i projektu.

**Planowanie testów** polega na zdefiniowaniu celów testów, a następnie wybraniu podejścia, które najlepiej pozwoli osiągnąć te cele w ramach ograniczeń narzuconych przez ogólny kontekst. Planowanie testów zostało szczegółowo omówione w podrozdziale 5.1.

**Monitorowanie testów i nadzór nad testami.** Monitorowanie testów obejmuje ciągłą kontrolę wszystkich czynności testowych oraz porównanie rzeczywistych postępów z planem. Nadzór nad testami obejmuje podejmowanie działań niezbędnych do osiągnięcia celów testów. Monitorowanie testów i nadzór nad testami zostały szczegółowo omówione w podrozdziale 5.3.

**Analiza testów** obejmuje analizę podstawy testów w celu zidentyfikowania cech, które można przetestować oraz zdefiniowanie i spriorytetyzowanie powiązanych z nimi warunków testowych, biorąc pod uwagę istniejące ryzyka (patrz podrozdział 5.2). Analizuje się również podstawę testów i przedmiot testów w celu oceny ich testowalności oraz zidentyfikowania ewentualnych defektów. Analiza testów jest często wspierana przez zastosowanie technik testowania (patrz rozdział 4).
Analiza testów odpowiada na pytanie: „co testować?” w kategoriach mierzalnych kryteriów pokrycia.

**Projektowanie testów** przekształca warunki testowe w przypadki testowe i inne testalia (np. karty opisu testów). Czynność ta często wiąże się z identyfikacją elementów pokrycia, które służą jako wskazówki do określenia danych wejściowych dla przypadków testowych. Do wsparcia tej czynności można wykorzystać techniki testowania (patrz rozdział 4). Projektowanie testów
obejmuje również określenie wymagań dotyczących danych testowych, zaprojektowanie
środowiska testowego oraz identyfikację niezbędnej infrastruktury i narzędzi. Projektowanie testów odpowiada na pytanie: „jak testować?”.

**Implementacja testów** obejmuje tworzenie lub pozyskiwanie testaliów niezbędnych
do wykonania testów (np. danych testowych), organizację przypadków testowych w procedury testowe i zestawy testowe, tworzenie manualnych i automatycznych skryptów testowych. Procedury testowe są szeregowane według priorytetów i układane w harmonogramie wykonywania testów w celu zapewnienia efektywnego wykonywania testów (patrz sekcja 5.1.5). Środowisko testowe jest budowane i weryfikowane pod kątem prawidłowej konfiguracji.

**Wykonywanie testów** obejmuje przeprowadzenie testów zgodnie z harmonogramem wykonania testów (czyli wykonywanie przebiegów testów). Wykonywanie testów może być manualne lub automatyczne i może przybierać różne formy, np. testowania ciągłego lub sesji testowania w parach. Rzeczywiste wyniki testów są porównywane z wynikami oczekiwanymi. Wyniki testów są rejestrowane. Anomalie są analizowane w celu zidentyfikowania ich prawdopodobnych przyczyn. Analiza ta pozwala zgłaszać anomalie na podstawie zaobserwowanych awarii (patrz podrozdział 5.5).

**Ukończenie testów** następuje zazwyczaj w momencie osiągnięcia kamieni milowych projektu (np. wydanie, koniec iteracji, ukończenie testów danego poziomu). W przypadku nierozwiązanych defektów tworzone są żądania zmian lub pozycje w backlogu produktu. Wszelkie testalia, które mogą być przydatne w przyszłości, są identyfikowane i archiwizowane lub przekazywane odpowiednim zespołom. Środowisko testowe jest zamykane w uzgodnionym stanie. Czynności testowe są analizowane w celu sformułowania wniosków i zidentyfikowania udoskonaleń dla przyszłych iteracji, wydań lub projektów (patrz sekcja 2.1.6). Sumaryczny raport z testów jest
tworzony i przekazywany interesariuszom.

### 1.4.2. Proces testowy w kontekście

Testowanie nie jest przeprowadzane w izolacji. Czynności testowe są integralną częścią procesów wytwarzania oprogramowania realizowanych w ramach organizacji. Testowanie jest również finansowane przez interesariuszy, a jego ostatecznym celem jest pomoc w zaspokojeniu ich potrzeb biznesowych. Dlatego sposób przeprowadzania testów będzie zależał od wielu czynników kontekstowych, w tym:

* interesariuszy (ich potrzeb, oczekiwań, wymagań, chęci współpracy itp.),
* członków zespołu (ich umiejętności, wiedzy, poziomu doświadczenia, dostępności, potrzeb szkoleniowych itp.),
* dziedziny biznesowej (krytyczność przedmiotu testów, zidentyfikowane ryzyka, potrzeby rynku, szczegółowe regulacje prawne itp.),
* czynników technicznych (rodzaj oprogramowania, architektura produktu, zastosowana technologia itp.),
* ograniczeń projektu (zakres, czas, budżet, zasoby itp.),
* czynników organizacyjnych (struktura organizacyjna, istniejące polityki, stosowane praktyki itp.),
* cyklu życia oprogramowania (praktyki inżynieryjne, metody rozwoju itp.),
* narzędzi (dostępność, użyteczność, zgodność itp.).

Czynniki te będą miały wpływ na wiele kwestii związanych z testowaniem, w tym na strategię testów, stosowane techniki testowania, stopień automatyzacji testów, wymagany poziom pokrycia, poziom szczegółowości dokumentacji testowej, raportowanie testów itp.

### 1.4.3. Testalia

Testalia powstają jako produkty pracy czynności testowych opisanych w sekcji 1.4.1. Istnieją znaczne różnice w sposobie, w jaki różne organizacje tworzą, nazywają, organizują i zarządzają swoimi testaliami. Właściwe zarządzanie konfiguracją (patrz podrozdział 5.4) zapewnia spójność i integralność testaliów. Poniższa lista zawiera wybrane przykłady testaliów (produktów pracy).

* **Produkty pracy związane z planowaniem** testów obejmują: plan testów, harmonogram testów, rejestr ryzyk, kryteria wejścia i kryteria wyjścia (patrz podrozdział 5.1). Rejestr ryzyk to lista ryzyk wraz z prawdopodobieństwem, wpływem i sposobem łagodzenia tych ryzyk (patrz podrozdział 5.2). Harmonogram testów, rejestr ryzyk, kryteria wejścia i kryteria wyjścia często są częścią planu testów.
* **Produkty pracy związane z monitorowaniem testów i nadzorem nad testami**
obejmują: raporty o postępie testów (patrz sekcja 5.3.2), dokumentację dyrektyw nadzoru (patrz podrozdział 5.3) oraz informacje o ryzykach (patrz podrozdział 5.2).
* **Produkty pracy związane z analizą testów** obejmują spriorytetyzowane warunki testowe (np. kryteria akceptacji, patrz sekcja 4.5.2) oraz raporty o defektach w podstawie testów (jeśli nie zostały one natychmiast usunięte).
* **Produkty pracy związane z projektowaniem testów** obejmują spriorytetyzowane przypadki testowe, karty opisu testów, elementy pokrycia, wymagania dotyczące danych testowych oraz wymagania dotyczące środowiska testowego.
* **Produkty pracy związane z implementacją testów** obejmują procedury testowe, manualne i zautomatyzowane skrypty testowe, zestawy testowe, dane testowe, harmonogram wykonywania testów oraz elementy środowiska testowego. Przykłady elementów środowiska testowego obejmują zaślepki, sterowniki, symulatory i wirtualizację usług.
* **Produkty pracy związane z wykonywaniem testów** obejmują dzienniki testów i raporty o defektach (patrz podrozdział 5.5).
* **Produkty pracy związane z ukończeniem testów** obejmują sumaryczny raport z testów (patrz sekcja 5.3.2), listę działań mających na celu doskonalenie kolejnych projektów lub iteracji, udokumentowane wnioski oraz żądania zmian (np. jako elementy backlogu produktu).

### 1.4.4. Śledzenie powiązań między podstawą testów a testaliami

Wdrożenie skutecznego monitorowania testów i nadzoru nad testami wymaga ustanowienia i utrzymywania przez cały czas trwania projektu testowego mechanizmu śledzenia powiązań pomiędzy elementami podstawy testów a testaliami (np. warunkami testowymi, ryzykami, przypadkami testowymi), wynikami testów i defektami. Dokładne śledzenie powiązań wspiera ocenę pokrycia, dlatego bardzo przydatne jest zdefiniowanie mierzalnych kryteriów pokrycia w podstawie testów. Kryteria pokrycia mogą funkcjonować jako kluczowe wskaźniki wydajności (ang. key performance indicators – KPI), które pokazują, w jakim stopniu osiągnięto cele testów (patrz sekcja 1.1.1). Na przykład:

* Śledzenie powiązań między przypadkami testowymi a wymaganiami pozwala zweryfikować, czy wymagania zostały pokryte przypadkami testowymi.
* Śledzenie powiązań między wynikami testów a ryzykami umożliwia ocenę poziomu ryzyka rezydualnego (resztkowego) w przedmiocie testów.

Oprócz oceny pokrycia, śledzenie powiązań umożliwia określenie wpływu zmian, ułatwia audyty i pomaga spełnić kryteria zarządzania IT. Śledzenie powiązań ułatwia rozumienie raportów o postępie testów i sumarycznych raportów z testów dzięki uwzględnieniu statusu elementów podstawy testów. To z kolei pomaga w przekazywaniu interesariuszom informacji na temat technicznych aspektów testowania w zrozumiały sposób. Śledzenie powiązań dostarcza ponadto informacji potrzebnych do oceny jakości produktu, wydajności procesów i postępów w realizacji projektu w odniesieniu do celów biznesowych.

### 1.4.5. Role w procesie testowania

W niniejszym sylabusie omówiono dwie główne role w testowaniu: rolę związaną z zarządzaniem testami i rolę związaną z testowaniem. Czynności i zadania przypisane do tych dwóch ról zależą od takich czynników jak: kontekst projektu i produktu, umiejętności osób pełniących te role oraz specyfika organizacji.

**Rola związana z zarządzaniem testami** obejmuje ogólną odpowiedzialność za proces testowy, zespół testowy i kierowanie czynnościami testowymi. Rola ta koncentruje się głównie na działaniach związanych z planowaniem testów, monitorowaniem testów, nadzorem nad testami i ukończeniem testów. Sposób wykonywania tej roli różni się w zależności od kontekstu. Na przykład w ramach zwinnego wytwarzania oprogramowania niektóre zadania związane z zarządzaniem testami mogą być wykonywane przez zespół zwinny. Zadania obejmujące wiele zespołów lub całą organizację mogą być wykonywane przez kierowników testów spoza zespołu tworzącego oprogramowania.

**Rola związana z testowaniem** obejmuje ogólną odpowiedzialność za inżynieryjny (techniczny) aspekt testowania. Rola ta koncentruje się głównie na działaniach związanych z analizą testów, projektowaniem testów, implementacją testów i wykonywaniem testów.

Różne osoby mogą pełnić powyższe role w różnym czasie. Na przykład rolę związaną
z zarządzaniem testami może pełnić kierownik zespołu, kierownik ds. testów, kierownik ds. rozwoju itp. Możliwe jest również, aby jedna osoba pełniła jednocześnie obie role.

## 1.5. Niezbędne umiejętności i dobre praktyki w dziedzinie testowania

Umiejętność to zdolność do prawidłowego wykonywania czegoś, wynikająca z wiedzy, praktyki i predyspozycji danej osoby. Dobrzy testerzy powinni posiadać pewne podstawowe umiejętności, aby dobrze wykonywać swoją pracę. Powinni być skutecznymi graczami zespołowymi i powinni być w stanie wykonywać testy na różnych poziomach niezależności.

### 1.5.1. Ogólne umiejętności wymagane w związku z testowaniem

Poniższe umiejętności, choć ogólne, są szczególnie istotne dla testerów:

* wiedza w zakresie testowania (zwiększa skuteczność testowania, np. poprzez stosowanie technik testowania),
* staranność, ostrożność, ciekawość, dbałość o szczegóły, metodyczność (ułatwia identyfikację defektów, zwłaszcza tych trudnych do wykrycia),
* umiejętności komunikacyjne, aktywne słuchanie, umiejętność pracy w zespole (pozwala na skuteczną interakcję ze wszystkimi interesariuszami, efektywne przekazywanie informacji, bycie zrozumiałym oraz sprawne zgłaszanie i omawianie defektów),
* myślenie analityczne, myślenie krytyczne, kreatywność (zwiększa skuteczność testowania),
* wiedza techniczna (zwiększa wydajność testowania, np. poprzez stosowanie odpowiednich narzędzi testowych),
* wiedza dziedzinowa (pozwala zrozumieć użytkowników oraz przedstawicieli jednostek biznesowych i efektywnie komunikować się z nimi).

Testerzy są często posłańcami złych wieści. Obwinianie osoby przynoszącej złe wiadomości jest powszechną cechą ludzką. Dlatego umiejętności komunikacyjne są tak ważne dla testerów. Przekazywanie wyników testów może być postrzegane jako krytyka produktu i jego autora. Efekt potwierdzenia (ang. confirmation bias) może utrudniać akceptację informacji, które są sprzeczne z aktualnymi przekonaniami. Niektórzy mogą postrzegać testowanie jako działanie destrukcyjne, mimo że w znacznym stopniu przyczynia się ono do sukcesu projektu i jakości produktu. Aby uniknąć powyższych problemów, informacje o defektach i awariach powinny być przekazywane w konstruktywny sposób.

### 1.5.2. Podejście „cały zespół” {#whole-team-approach}

Jedną z ważnych umiejętności testera jest zdolność do efektywnej pracy w zespole i pozytywnego przyczyniania się do realizacji celów zespołu. Na tej umiejętności opiera się podejście „cały zespół” (ang. whole-team approach) – praktyka wywodząca się z programowania ekstremalnego (patrz podrozdział 2.1).

W podejściu „cały zespół” każdy członek zespołu posiadający niezbędną wiedzę i umiejętności może wykonywać dowolne zadanie, a odpowiedzialność za jakość spoczywa w równym stopniu na wszystkich. Członkowie zespołu dzielą tę samą przestrzeń roboczą (fizyczną lub wirtualną), ponieważ wspólna lokalizacja ułatwia komunikację i interakcję. Podejście „cały zespół” poprawia dynamikę zespołu, usprawnia komunikację i współpracę w zespole oraz tworzy synergię, umożliwiając wykorzystanie różnych zestawów umiejętności w zespole z korzyścią dla projektu.

Testerzy ściśle współpracują z innymi członkami zespołu, aby zapewnić osiągnięcie wymaganego poziomu jakości. Obejmuje to również współpracę z przedstawicielami biznesowymi w celu tworzenia testów akceptacyjnych oraz współpracę z programistami w celu uzgodnienia strategii testów i podjęcia decyzji dotyczących automatyzacji testów. Testerzy mogą w ten sposób przekazywać wiedzę na temat testowania innym członkom zespołu i wpływać na proces wytwarzania produktu.

W pewnych przypadkach podejście „cały zespół” nie jest odpowiednie. Na przykład w ramach wytwarzania systemów krytycznych ze względów bezpieczeństwa, może być wymagany wysoki poziom niezależności testów.

### 1.5.3. Niezależność testowania

Pewien stopień niezależności sprawia, że tester jest bardziej skuteczny w wykrywaniu defektów ze względu na różnice między błędami poznawczymi (ang. cognitive bias) autora i testera (por. Salman 1995). Niezależność nie zastępuje jednak znajomości produktu, np. programiści mogą skutecznie wykrywać wiele defektów we własnym kodzie.

Produkty pracy mogą być testowane przez ich autora (brak niezależności), przez
współpracowników autora z tego samego zespołu (pewna niezależność), przez testerów spoza zespołu autora, ale z tej samej organizacji (wysoka niezależność) lub przez testerów spoza organizacji (bardzo wysoka niezależność). W przypadku większości projektów zazwyczaj najlepiej jest przeprowadzać testy z wykorzystaniem wielu poziomów niezależności (np. programiści przeprowadzają testowanie modułowe i testowanie integracji modułów, zespół testowy – testowanie systemowe i testowanie integracji systemów, a przedstawiciele biznesowi – testowanie akceptacyjne).

Główną zaletą niezależności testowania jest to, że niezależni testerzy mogą dostrzegać inne rodzaje awarii i defektów niż programiści ze względu na swoje odmienne doświadczenie, perspektywę techniczną i błędy poznawcze. Ponadto niezależny tester może weryfikować, kwestionować lub obalać założenia poczynione przez interesariuszy podczas specyfikacji i implementowania systemu.

Niezależność testowania ma również pewne wady. Niezależni testerzy mogą być odizolowani od zespołu programistów, co może prowadzić do braku współpracy, problemów z komunikacją lub nawet konfliktów z zespołem programistów. Programiści mogą utracić poczucie odpowiedzialności za jakość. Niezależni testerzy mogą być postrzegani jako wąskie gardło lub być obwiniani za opóźnienia w wydaniu produktu.