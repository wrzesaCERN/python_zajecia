import pytest

from game_functions import (
check_function_x,
check_function_y,
)

from ghosts_functions import (
check_the_board,
move_forward,
change_direction,
)

from player_functions import (
move_magic_dot,
)


"""
game_functions 
  check_function_x i check_function_y sprawdzają czy po danej stronie mają 5 pół true. jeśli tak zwracają true.
"""

board_to_move = [[False] * 85 for i in range(66)] #sytuacja gdy nie ma żadego pola true
board_to_move_left = [[False] * 85 for i in range(66)] #sytuacja gdy po lewej stronie pacmana jest 5 pól true
board_to_move_left[31][65] = True
board_to_move_left[30][65] = True
board_to_move_left[29][65] = True
board_to_move_left[28][65] = True
board_to_move_left[27][65] = True
board_to_move_down = [[False] * 85 for i in range(66)] #sytuacja gdy od dołu pacmana jest 5 pól true
board_to_move_down[32][66] = True
board_to_move_down[32][67] = True
board_to_move_down[32][68] = True
board_to_move_down[32][69] = True
board_to_move_down[32][70] = True
board_to_move_no_left = [[False] * 85 for i in range(66)] #sytuacja gdy po lewej stronie pacmana  brakuje 2 pól do 5
board_to_move_no_left[31][65] = True
board_to_move_no_left[30][65] = True
board_to_move_no_left[29][65] = True
board_to_move_no_left[28][65] = False
board_to_move_no_left[27][65] = False

#sprawdzenie ruchu do dołu (pierwsze true (false to góra)), potem do dołu ale na drugiej planszy i potem do góry też na tej drugiej
test_tab_game_functions_x = [
    (board_to_move, 29, 68, True, False),
    (board_to_move_down, 29, 68, True, True),
    (board_to_move_down, 29, 68, False, False),

]
@pytest.mark.parametrize("board_to_move, ghost_pos_y, ghost_pos_x, down , expected", test_tab_game_functions_x)
def test_check_function_x(board_to_move, ghost_pos_y, ghost_pos_x, down , expected):
    assert check_function_x(board_to_move, ghost_pos_y, ghost_pos_x, down) == expected

#sprawdzenie ruchu w lewo , potem w lewo na planszy gdzie to lewo faktycznie jest dostępne, a potem tam gdzie nie jest dostępne
test_tab_game_functions_y = [
    (board_to_move, 29, 68, False, False),
    (board_to_move_left, 29, 68, False, True),
    (board_to_move_no_left, 29, 68, False, False),

]
@pytest.mark.parametrize("board_to_move, ghost_pos_y, ghost_pos_x, right , expected", test_tab_game_functions_y)
def test_check_function_y(board_to_move, ghost_pos_y, ghost_pos_x, right , expected):
    assert check_function_y(board_to_move, ghost_pos_y, ghost_pos_x, right) == expected


"""
ghosts_funtions
  "check_function_x" i "check_function_x" (powyżej) używane są w "check_the_board" (poniżej), która ma zmieniać duszkowe tablice
   odpowiedzialne za ich przyzwolenie do kontynuacji ruchu w danym kierunku, do zmiany kierunku czy przymusu tej zmiany
"""

ghost_pos_x = [5, 5, 68, 69]
ghost_pos_y = [29, 29, 29, 29]
ghost_direction = [4, 4, 3, 3]
ghost_dulr = [[False, False, False, False], [False, False, False, False], [False, False, False, False],
              [False, False, False, False]]
can_the_ghost_go_forward = [False, False, False, False]
can_the_ghost_change_direction = [False, False, False, False]
ii = 0
ii2 = 2

test_tab_check_the_board = [
    (0, board_to_move, ghost_pos_x, ghost_pos_y, ghost_direction, ghost_dulr, can_the_ghost_go_forward,
                              can_the_ghost_change_direction, False, False, [False, False, False, False]),
    (2, board_to_move_left, ghost_pos_x, ghost_pos_y, ghost_direction, ghost_dulr, can_the_ghost_go_forward,
                              can_the_ghost_change_direction, True, True, [False, False, False, True]),
]

@pytest.mark.parametrize("ii, board_to_move, ghost_pos_x, ghost_pos_y, ghost_direction, ghost_dulr, "
                         "can_the_ghost_go_forward,can_the_ghost_change_direction ,newforward, newchange, directions",
                         test_tab_check_the_board)
def test_check_the_board(ii, board_to_move, ghost_pos_x, ghost_pos_y, ghost_direction, ghost_dulr, can_the_ghost_go_forward,
                         can_the_ghost_change_direction ,newforward, newchange, directions):
     check_the_board(ii, board_to_move, ghost_pos_x, ghost_pos_y, ghost_direction, ghost_dulr, can_the_ghost_go_forward,
                     can_the_ghost_change_direction);
     assert (can_the_ghost_go_forward[ii], can_the_ghost_change_direction[ii], ghost_dulr[ii]) == (newforward, newchange, directions)


"""
W tym tescie chodzi o sprawdzenie obsługi zdarzenia odbicia od ściany etc. Musimy wymusić zmianę kierunku ducha.
Więc nowy kierunek  zwracany przez "move_forward" nie może być taki jak stary.
Kierunki to liczby od 1 do 4.
"""

test_tab2 = [
    (False, 4, [True, True, True, True], True, 31, 65, ghost_pos_x[0], ghost_pos_y[0], 4),
    (False, 1, [True, True, True, True], True, 31, 65, ghost_pos_x[0], ghost_pos_y[0], 1),

]
@pytest.mark.parametrize("can_the_ghost_go_forward, ghost_direction, ghost_dulr, atraction, player_pos_x, player_pos_y,"
                         " ghost_pos_x, ghost_pos_y ,notexpected", test_tab2)
def test_move_forward(can_the_ghost_go_forward, ghost_direction, ghost_dulr, atraction, player_pos_x, player_pos_y,
                      ghost_pos_x, ghost_pos_y, notexpected):
    assert move_forward(can_the_ghost_go_forward, ghost_direction, ghost_dulr, atraction, player_pos_x, player_pos_y,
                        ghost_pos_x, ghost_pos_y) != notexpected


"""
Test analogiczny jak wyżej tylko odnosi sie do zmiany kierunku nieniewymuszonego przeszkodą. Aby uniknąć sytuacji w której
duszek przemieszczając sie w niezmąconej szparami ścieżce nadle sie cofał zmiana kierunku funkcją "change_direction "
 nie może przeciwna do naszego obecnego
"""


test_tab2 = [
    (False, 4, [True, True, True, True], True, 31, 65, ghost_pos_x[0], ghost_pos_y[0], 3),
    (False, 1, [True, True, True, True], True, 31, 65, ghost_pos_x[0], ghost_pos_y[0], 2),
]

@pytest.mark.parametrize(
    "can_the_ghost_go_forward, ghost_direction, ghost_dulr, atraction, player_pos_x, player_pos_y, ghost_pos_x, ghost_pos_y ,notexpected",
    test_tab2)
def test_change_direction(can_the_ghost_go_forward, ghost_direction, ghost_dulr, atraction, player_pos_x, player_pos_y,
                      ghost_pos_x, ghost_pos_y, notexpected):
    assert change_direction(can_the_ghost_go_forward, ghost_direction, ghost_dulr, atraction, player_pos_x,
                            player_pos_y, ghost_pos_x, ghost_pos_y) != notexpected


"""
player_functions
   "move_magic_dot" ma zwracać możliwość zabijania (true) gdy zje odpowiednią kropkę 
"""
board_magic_dots = [[False] * 85 for i in range(66)]
board_magic_dots[5][6] = True
board_magic_dots[5][75] = True
board_magic_dots[59][6] = True
board_magic_dots[59][75] = True

test_tab_move_magic_dot = [
    (board_magic_dots, 29, 28, 2, 1, 1, False),
    (board_magic_dots, 4, 58, 2, 1, 1, True),
    (board_magic_dots, 4, 58, 2, 1, 1, False),#sprawdzenie czy poprzednie wywołanie wyłączyło (zjadać można tylko raz zjeść daną kropkę)
]

@pytest.mark.parametrize(
    "board_magic_dots, player_pos_x, player_pos_y, add_x, add_y, option, expected", test_tab_move_magic_dot)
def test_move_magic_dot(board_magic_dots, player_pos_x, player_pos_y, add_x, add_y, option, expected):
    assert move_magic_dot(board_magic_dots, player_pos_x, player_pos_y, add_x, add_y, option) == expected


