import random
import game_functions

"""
Funcka "check_the_board" używa "check_function_x" i "check_function_y" z game_functions i ustawia tablice: can_the_ghost_go_forward i 
can_the_ghost_change_direction zgodnie z możliwościami, które mogły zaistnieć podcas ruchu
"""


def check_the_board(ii, board_to_move, ghost_pos_x, ghost_pos_y, ghost_direction, ghost_dulr, can_the_ghost_go_forward,can_the_ghost_change_direction):
    if game_functions.check_function_x(board_to_move, ghost_pos_y[ii], ghost_pos_x[ii], True):
        ghost_dulr[ii][0] = True
        if ghost_direction[ii] == 0:
            can_the_ghost_go_forward[ii] = True
        if ghost_direction[ii] != 1:
            can_the_ghost_change_direction[ii] = True

    if game_functions.check_function_x(board_to_move, ghost_pos_y[ii], ghost_pos_x[ii], False):
        ghost_dulr[ii][1] = True
        if ghost_direction[ii] == 1:
            can_the_ghost_go_forward[ii] = True
        if ghost_direction[ii] != 0:
            can_the_ghost_change_direction[ii] = True

    if game_functions.check_function_y(board_to_move, ghost_pos_y[ii], ghost_pos_x[ii], True):
        ghost_dulr[ii][2] = True
        if ghost_direction[ii] == 2:
            can_the_ghost_go_forward[ii] = True
        if ghost_direction[ii] != 3:
            can_the_ghost_change_direction[ii] = True

    if game_functions.check_function_y(board_to_move, ghost_pos_y[ii], ghost_pos_x[ii], False):
        ghost_dulr[ii][3] = True
        if ghost_direction[ii] == 3:
            can_the_ghost_go_forward[ii] = True
        if ghost_direction[ii] != 2:
            can_the_ghost_change_direction[ii] = True


"""
Funkcja "atraction_repulsion" w zależności czy mamy przyciąganie czy odpychanie ustawia nam kierunek ruchu ducha. 
Jeśli mamy np. przyciąganie , czyli duchy chcą zabić pacmana  to gdy duch będzie miał pacmana po swojej prawej stronie
 to jest o wiele większe prawdopodobieństwo, że wybierze kierunek w prawo niż w lewo.  Odpychanie działa na odwrotnej 
 zasadzie.
"""


def atraction_repulsion(ghost_pos_x, ghost_pos_y, player_pos_x, player_pos_y, rand_tmp, move_ghost_tab):
    rand = 0
    if player_pos_x > ghost_pos_x and player_pos_y > ghost_pos_y:
        if rand_tmp < 35:
            rand = move_ghost_tab[0]
        elif (rand_tmp < 70) and (rand_tmp >= 35):
            rand = move_ghost_tab[1]
        elif (rand_tmp < 82) and (rand_tmp >= 70):
            rand = move_ghost_tab[2]
        else:
            rand = move_ghost_tab[3]
    elif player_pos_x > ghost_pos_x and player_pos_y < ghost_pos_y:
        if rand_tmp < 35:
            rand = move_ghost_tab[0]
        elif (rand_tmp < 70) and (rand_tmp >= 35):
            rand = move_ghost_tab[3]
        elif (rand_tmp < 82) and (rand_tmp >= 70):
            rand = move_ghost_tab[2]
        else:
            rand = move_ghost_tab[1]
    elif player_pos_x < ghost_pos_x and player_pos_y > ghost_pos_y:
        if rand_tmp < 35:
            rand = move_ghost_tab[2]
        elif (rand_tmp < 70) and (rand_tmp >= 35):
            rand = move_ghost_tab[1]
        elif (rand_tmp < 82) and (rand_tmp >= 70):
            rand = move_ghost_tab[0]
        else:
            rand = move_ghost_tab[3]
    else:
        if rand_tmp < 35:
            rand = move_ghost_tab[2]
        elif (rand_tmp < 70) and (rand_tmp >= 35):
            rand = move_ghost_tab[3]
        elif (rand_tmp < 82) and (rand_tmp >= 70):
            rand = move_ghost_tab[0]
        else:
            rand = move_ghost_tab[1]

    return rand


"""
Funcja "move_forward" wykonuje sie do tąd, aż obrany zostanie kolejny ruch dla danego ducha. Losowanie kierunku funckją 
"atraction_repulsion" to jedno a akceptacja tego kierunku to drugie. Dlaczego? ponieważ jak nam wylosuje kierunk w prawo 
a po prawej będzie np przeszkoda to musi zrobić to jeszcze raz. Do skutku. 

funkcja jest istotna z puktu widzenia napotykania ścian lub przeszkód 
"""


def move_forward(can_the_ghost_go_forward, ghost_direction, ghost_dulr, atraction, player_pos_x, player_pos_y, ghost_pos_x, ghost_pos_y):
    if not can_the_ghost_go_forward:
        changed = False
        rand = 0
        while not changed:
            rand_tmp = random.randint(0, 100)
            if atraction:
                rand = atraction_repulsion(ghost_pos_x, ghost_pos_y, player_pos_x, player_pos_y, rand_tmp, (2, 0, 3, 1))
            else:
                rand = atraction_repulsion(ghost_pos_x, ghost_pos_y, player_pos_x, player_pos_y, rand_tmp, (3, 1, 2, 0))

            # jeśli może się ruszyć w danym kierunku i jeśli wylosowano ten kierunek następuje wstępna akceptacja tego kierunku
            if ghost_dulr[0] and rand == 0:
                ghost_direction = 0
                changed = True

            if ghost_dulr[1] and rand == 1:
                ghost_direction = 1
                changed = True

            if ghost_dulr[2] and rand == 2:
                ghost_direction = 2
                changed = True

            if ghost_dulr[3] and rand == 3:
                ghost_direction = 3
                changed = True

    else:
        return ghost_direction


"""
change_direction obsługuje zmianę kierunku nie tylko przy zeknięciu ze ścianą lub przeszkodą a napotknaiu jakiejś drogi 
"bocznej" - odbiegającej od jej pierwotnego kierunku. Jak move_forward wykonuje się do momentu ustalenia kierunku.
"""


def change_direction(can_the_ghost_change_direction, ghost_direction, ghost_dulr, atraction, player_pos_x, player_pos_y, ghost_pos_x, ghost_pos_y):
    if can_the_ghost_change_direction:
        changed = False
        while not changed:
            rand_tmp = random.randint(0, 100)
            if atraction:
                rand = atraction_repulsion(ghost_pos_x, ghost_pos_y, player_pos_x, player_pos_y, rand_tmp, (2, 0, 3, 1))
            else:
                rand = atraction_repulsion(ghost_pos_x, ghost_pos_y, player_pos_x, player_pos_y, rand_tmp, (3, 1, 2, 0))

            tmp = ghost_direction

            # jeśli może się ruszyć w danym kierunku i jeśli wylosowano ten kierunek następuje wstępna akceptacja tego kierunku
            if ghost_dulr[0] and rand == 0:
                ghost_direction = 0
            if ghost_dulr[1] and rand == 1:
                ghost_direction = 1
            if ghost_dulr[2] and rand == 2:
                ghost_direction = 2
            if ghost_dulr[3] and rand == 3:
                ghost_direction = 3

            # drugi etap akceptacji. nowy kierunek nie może być odbiciem (to strasznie dziwnie wyglądało np
            # gdy idąc po prostej lini do góry chciałoby się cofać i trochę do góry i trochę cofać etc )
            if ghost_direction == 0 and tmp != 1:
                changed = True
                return ghost_direction

            elif ghost_direction == 1 and tmp != 0:
                changed = True
                return ghost_direction

            elif ghost_direction == 2 and tmp != 3:
                changed = True
                return ghost_direction

            elif ghost_direction == 3 and tmp != 2:
                changed = True
                return ghost_direction
    else:
        return ghost_direction


"""
"dispaly_subfun" to funkcja pomocnicza, kótra rysuje duszka przesuniętego o "1" w kierunku zależnym od zadanej opcji.
wywoływana jest w dispay_ghosts, która już zna ostateczny kierunek ruchu ducha
"""


def dispaly_subfun(gameDisplay, pacman_bg, ghost_pos_x, ghost_pos_y, ii, blue_ghosts, ghosts_b, ghosts, option):
    gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))

    if option == 0:
        ghost_pos_y[ii] += 1
    elif option == 1:
        ghost_pos_y[ii] -= 1
    elif option == 2:
        ghost_pos_x[ii] += 1
    else:
        ghost_pos_x[ii] -= 1

    if blue_ghosts:
        gameDisplay.blit(ghosts_b[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
    else:
        gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))


def dispay_ghosts(ii, ghost_direction, ghost_dulr, ghost_pos_x, ghost_pos_y, pacman_bg, gameDisplay, ghosts_b, ghosts, blue_ghosts):
    if ghost_direction[ii] == 0 and ghost_dulr[ii][0]:
        dispaly_subfun(gameDisplay, pacman_bg, ghost_pos_x, ghost_pos_y, ii, blue_ghosts, ghosts_b, ghosts, 0)

    elif ghost_direction[ii] == 1 and ghost_dulr[ii][1]:
        dispaly_subfun(gameDisplay, pacman_bg, ghost_pos_x, ghost_pos_y, ii, blue_ghosts, ghosts_b, ghosts, 1)

    elif ghost_direction[ii] == 2 and ghost_dulr[ii][2]:
        dispaly_subfun(gameDisplay, pacman_bg, ghost_pos_x, ghost_pos_y, ii, blue_ghosts, ghosts_b, ghosts, 2)

    elif ghost_direction[ii] == 3 and ghost_dulr[ii][3]:
        dispaly_subfun(gameDisplay, pacman_bg, ghost_pos_x, ghost_pos_y, ii, blue_ghosts, ghosts_b, ghosts, 3)
