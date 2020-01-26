import game_functions

"""
player_avaliability_to_move sprawdza, w których kierunkach można się ruszyć 
"""


def player_avaliability_to_move(board_to_move, player_pos_x, player_pos_y):
    d_u_l_r = [False, False, False, False]
    if game_functions.check_function_x(board_to_move, player_pos_y, player_pos_x, True):
        d_u_l_r[0] = True
    if game_functions.check_function_x(board_to_move, player_pos_y, player_pos_x, False):
        d_u_l_r[1] = True
    if game_functions.check_function_y(board_to_move, player_pos_y, player_pos_x, False):
        d_u_l_r[2] = True
    if game_functions.check_function_y(board_to_move, player_pos_y, player_pos_x, True):
        d_u_l_r[3] = True

    return d_u_l_r

"""
move_just_move sprawdza, przesuwa pacmana i rysuje w nowym miejscu. + zwraca jego nowe pozycje 
"""

def move_just_move(gameDisplay, pacman_bg, player_pos_x, player_pos_y, pacman_directions, option):
    gameDisplay.blit(pacman_bg, (player_pos_x * 10 - 3, player_pos_y * 10 - 3))
    if option == 0:
        player_pos_y += 1
    elif option == 1:
        player_pos_y -= 1
    elif option == 2:
        player_pos_x += 1
    else:
        player_pos_x -= 1

    gameDisplay.blit(pacman_directions, (player_pos_x * 10 - 3, player_pos_y * 10 - 3))
    return player_pos_x, player_pos_y


"""
move_score sprawdzenie czy przesunięcie nie generuje zjedzenia jakiejśc aktywnje kropki.jeśli natrafi na aktywna kropkę to zwiekszamy
pulę zdobytych punktów i zamieniamy ją na false tak by już jej nie zjadac drugi raz 
tu tez jest obsługa dźwieku jedzenia kropek
"""


def move_score(board_yellow_dots, player_pos_x, player_pos_y, add_x, add_y, eating_Sound, eat_Sound, score, option):

    if board_yellow_dots[player_pos_y + add_y][player_pos_x + add_x]:
        board_yellow_dots[player_pos_y + add_y][player_pos_x + add_x] = False
        score += 1
        if not eating_Sound.get_busy():
            eating_Sound.play(eat_Sound)

    if option == 0:
        if board_yellow_dots[player_pos_y + add_y + 3][player_pos_x + add_x]:
            board_yellow_dots[player_pos_y + add_y + 3][player_pos_x + add_x] = False
            score += 1
            if not eating_Sound.get_busy():
                eating_Sound.play(eat_Sound)
    elif option == 1:
        if board_yellow_dots[player_pos_y + add_y + 3][player_pos_x + add_x]:
            board_yellow_dots[player_pos_y + add_y + 3][player_pos_x + add_x] = False
            score += 1
            if not eating_Sound.get_busy():
                eating_Sound.play(eat_Sound)
    elif option == 2:
        if board_yellow_dots[player_pos_y + add_y + 2][player_pos_x + add_x+3]:
            board_yellow_dots[player_pos_y + add_y + 2][player_pos_x + add_x+3] = False
            score += 1
            if not eating_Sound.get_busy():
                eating_Sound.play(eat_Sound)

    return score


"""
move_magic_dot obsługa zjadania magicznych kropek. Oczywiście tu też je "gasimy" ustawiając na false a także włączamy możliwośc zabijania 
duchów która z koleii uruchamia ich oepychanie etc..
"""


def move_magic_dot(board_magic_dots, player_pos_x, player_pos_y, add_x, add_y, option):
    power_to_kill = False
    if board_magic_dots[player_pos_y + add_y][player_pos_x + add_x]:
        board_magic_dots[player_pos_y + add_y][player_pos_x + add_x] = False
        power_to_kill = True
    if option == 0:
        if board_magic_dots[player_pos_y + add_y + 3][player_pos_x + add_x]:
            board_magic_dots[player_pos_y + add_y + 3][player_pos_x + add_x] = False
            power_to_kill = True
    elif option == 2:
        if board_magic_dots[player_pos_y + add_y + 2][player_pos_x + add_x + 3]:
            board_magic_dots[player_pos_y + add_y + 2][player_pos_x + add_x + 3] = False
            power_to_kill = True

    return power_to_kill
