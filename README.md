## **Tic Tac Toe 4x4 – Gra z AI**

---

### **Cel i zakres projektu**

Celem projektu było stworzenie gry Tic Tac Toe na planszy 4x4, w której gracze **przegrywają**, jeśli ułożą cztery znaki X w jednej linii. Projekt łączy w sobie logikę gry, sztuczną inteligencję wykorzystującą algorytm minimax z przycinaniem alfa-beta, oraz graficzny interfejs użytkownika w bibliotece `tkinter`.

Zakres projektu obejmuje:

* stworzenie logiki gry zgodnej z zasadami przegrywania przy ułożeniu czterech znaków,
* opracowanie algorytmu AI przewidującego możliwe scenariusze rozgrywki,
* zaprojektowanie interfejsu graficznego umożliwiającego grę człowieka z komputerem,
* optymalizację działania poprzez cache’owanie wyników i heurystyki.

---

### **Opis gry**

**Mechanika działania gry:**

* Plansza ma wymiary 4x4.
* Gracze (gracz i AI) wykonują ruchy naprzemiennie.
* Każdy ruch polega na postawieniu symbolu **X** w wybranym polu.
* Gra kończy się **przegraną gracza**, który jako pierwszy postawi **czwarty symbol w jednej kolumnie, wierszu lub na przekątnej**.

**Zasady:**

* Gra toczy się do momentu, aż jeden z graczy ułoży linię czterech X – wtedy przegrywa.
* Jeżeli wszystkie pola zostaną zapełnione bez ułożenia takiej linii, gra kończy się remisem.
* Gra ma charakter strategiczny – gracz musi nie tylko unikać przegranej, ale też tak planować ruchy, by zmusić przeciwnika do błędu.

---

### **Zastosowane rozwiązania**

**Algorytm:**

* Rdzeniem sztucznej inteligencji jest algorytm **Minimax z przycinaniem alfa-beta**, który przeszukuje wszystkie możliwe stany gry w poszukiwaniu najkorzystniejszego posunięcia.
* Przeszukiwanie jest zoptymalizowane przez eliminowanie ruchów prowadzących do przegranej (`is_losing_move`).

**Heurystyki:**

* Ignorowane są ruchy, które natychmiast kończą grę przegraną.
* Zastosowano **mechanizm pamięci podręcznej** (`self.cache`), dzięki czemu te same konfiguracje planszy nie są analizowane wielokrotnie.
* W przypadku wielu bezpiecznych ruchów, AI wybiera ten, który potencjalnie daje największą kontrolę nad planszą.

**Ocena ruchów:**

* Wynikiem algorytmu `minimax` są wartości:

  * `1` – ruch bezpieczny, korzystny,
  * `0` – neutralny, nie wpływający na przegraną ani wygraną,
  * `-1` – ruch ryzykowny, potencjalnie prowadzący do porażki.
* AI zawsze stara się unikać ruchów o wyniku `-1`.

---

### **Wnioski**

**Spostrzeżenia:**

* Nietypowa logika gry (gdzie celem jest unikanie czterech w linii) wymusza zmianę klasycznego podejścia do strategii AI.
* Dzięki wykorzystaniu przycinania alfa-beta i pamięci podręcznej, AI działa sprawnie nawet w późniejszych fazach gry.

---
