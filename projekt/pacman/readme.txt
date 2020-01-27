Gra P A C M A N


Aby gra działała musi być zainstalowany "pygame". Do testów potrzebny jest "pytest".
Wersje, przy których został wykonany projekt podane są w requirements.txt
Aby je zainstalować wystarczy "pip install -r requirements.txt"

Aby uruchomić wystarczy "python3.6 pacman.py"


OPIS GRY:

Jesli ktoś nigdy nie grał (w co szczerze wątpie) to w PACMANie chodzi o to, że poruszamy się żółtą kulką, która zjada inne mniejsze kuleczki (również żółte) i naszym zadaniem jest zjedzenie wszystkich kulek. Oczywiście samo to czyniło by tę grę nudną, więc po planszy poruszają sie również duszki, które mogą nas zabić. Jeśli jednak zjemy magiczną (dużą) kulkę to my możemy zabić duszka a one będą się nas bały i będa uciekały.  



MODUŁY:
______________________________________________________________________________________________________
board.py 

    zawiera wszelkie elementy związane z wyglądem planszy: linie, ustawienie pól ruchu, ustawienie zwykłych żółtych kropek, ustaiwanie magicznych kropek.
    Moduł ten ma DUŻO monotonnych ustawień, jednakże plansza została od podstaw zrobiona przeze mnie. Stworzenie wyglądu planszy i przypisanie pewnych cech do niektórych miejsc na planszy wiąże się (BARDZO) żmudnym ustawianiem lini etc. 

______________________________________________________________________________________________________
ghosts_functions.py 

   zawiera wszystkie funkcje używane do obsługi duchów jak np. sposób wybierania kierunku ich ruchu czy ich rysowanie

______________________________________________________________________________________________________
player_functions.py 

   zawiera wszystkie funcje związane z obslugą pacmana/gracza - podobnie jak ghosts_functions do duszków.

______________________________________________________________________________________________________
game_functions.py 

   zawiera wszystkie pomocnicze funckcje np. do rysowania, do obsługi dialogu z graczem, do odświerzania plnaszy etc.

______________________________________________________________________________________________________
pacman.py 

   jest to GŁÓWNY MODUŁ i jego ODPALAMY
   W tym module łączą się wszystkie moduły w jedność (ale to ładnie napisałam :) ).


TESTY:

Testy zostały przeprowadzone tylko do funkcji, które nie są z logicznego punktu widzenia banalne (jak np. rysowanie kropek, czy wygląd planszy, wygląd dialogu, przesuniecie obiektu o x pól w którąś ze stron). 






