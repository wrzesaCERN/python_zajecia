import pygame
import board

"""
Funcje "check_function_x" i "check_function_y" sprawdzają odpowiendio czy po prawej / lewej oraz od góry / dołu mamy 
5 pól ruchu ustawionych na true. Ostatni parametr np down mówi o tym że jeśli jest true to sprawdzamy czy pod nami jest 
 5 pół. Ustawiony na false oznacza, że sprawdzamy kierunek przeciwny czyli up

Te dwie są subfunkcjami używanymi w innych funkcjach spawdzających dostępność planszy 
"""


def check_function_x(board_to_move, ghost_pos_y, ghost_pos_x, down):
    if down:
        add_y = 3
    else:
        add_y = -3

    out = False
    if board_to_move[ghost_pos_y + add_y][ghost_pos_x + 2] and board_to_move[ghost_pos_y + add_y][
        ghost_pos_x - 2] and board_to_move[ghost_pos_y + add_y][ghost_pos_x + 1] and \
            board_to_move[ghost_pos_y + add_y][ghost_pos_x] and board_to_move[ghost_pos_y + add_y][
        ghost_pos_x - 1]:
        out = True
    return out


def check_function_y(board_to_move, ghost_pos_y, ghost_pos_x, right):
    if right:
        add_x = 3
    else:
        add_x = -3

    out = False
    if board_to_move[ghost_pos_y + 2][ghost_pos_x + add_x] and board_to_move[ghost_pos_y + 1][
        ghost_pos_x + add_x] and board_to_move[ghost_pos_y][ghost_pos_x + add_x] and \
            board_to_move[ghost_pos_y - 1][ghost_pos_x + add_x] and board_to_move[ghost_pos_y - 2][
        ghost_pos_x + add_x]:
        out = True
    return out


"""
funkcje odpowiedzialne za rywsanie i wygląd kropek na zadanej pozycji. yellow_dot - zwykłe, super_yellow_dot - magiczne 
"""


def yellow_dot(gameDisplay, pos_x, pos_y):
    pygame.draw.circle(gameDisplay, (255, 255, 160), (pos_x, pos_y), 6)


def super_yellow_dot(gameDisplay, pos_x, pos_y):
    pygame.draw.circle(gameDisplay, (255, 255, 160), (pos_x, pos_y), 9)


""" 
funkcje do dialogu z graczem, wygląd ich itp.
"""


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 0, 0))
    return textSurface, textSurface.get_rect()


def message_display(gameDisplay, tekst, posY, size):
    largeText = pygame.font.SysFont("curier", size)
    TextSurf, TextRect = text_objects(tekst, largeText)
    TextRect.center = (400, posY)
    gameDisplay.blit(TextSurf, TextRect)


"""
dialog z graczem i obsługa tego czy chcem grać dalej czy wyjść z gry
"""


def retry(gameDisplay, win, board_yellow_dots, yellow_dot, board_magic_dots, super_yellow_dot):
    pygame.draw.rect(gameDisplay, (0, 0, 0), [100, 160, 580, 300])
    pygame.draw.rect(gameDisplay, (0, 0, 255), [100, 160, 580, 300], 3)

    if not win:
        message_display(gameDisplay, "GAME OVER", 250, 80)
    else:
        message_display(gameDisplay, "YOU WON !!!", 300, 80)

    valid_answer = False
    while not valid_answer:
        for event in pygame.event.get():
            message_display(gameDisplay, "Retry? y/n", 370, 60)
            pygame.display.update()
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_y):
                valid_answer = True
                board.board_dots(gameDisplay, board_yellow_dots, yellow_dot)
                board.board_magic(gameDisplay, board_magic_dots, super_yellow_dot)

            elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_n):
                quit()

            elif event.type == pygame.QUIT:
                quit()


"""
"still_alive" jest to funkcja wykonywana gdy po utracie zycia nadal mamy koljne. cel ? - dświerzenie planszy
"""


def still_alive(gameDisplay, board_yellow_dots, yellow_dot, board_magic_dots, super_yellow_dot, pacman_directions, player_pos_x, player_pos_y):
    gameDisplay.fill((0, 0, 0))  # black background
    pygame.draw.rect(gameDisplay, (0, 255, 255), [30, 20, 741, 590], 1)  # board rectangle
    board.board_lines(gameDisplay)  # A function that draw obstacles on the board
    for i in range(0, 80):
        for j in range(0, 61):
            if board_yellow_dots[j][i]:
                yellow_dot(gameDisplay, i * 10 - 5, j * 10 - 5)
            if board_magic_dots[j][i]:
                super_yellow_dot(gameDisplay, i * 10 - 5, j * 10 - 5)

    gameDisplay.blit(pacman_directions[0], (player_pos_x * 10 - 3, player_pos_y * 10 - 3))
    pygame.display.update()


"""
funkcja "onceagain" to funkcja wykonywana gdy po wygraniu chcey nadal grać
"""


def onceagain(gameDisplay, board_yellow_dots, board_magic_dots, pacman_directions, player_pos_x, player_pos_y):

    board.board_lines(gameDisplay)
    board.board_dots(gameDisplay, board_yellow_dots, yellow_dot)
    board.board_magic(gameDisplay, board_magic_dots, super_yellow_dot)

    gameDisplay.blit(pacman_directions[0], (player_pos_x * 10 - 3, player_pos_y * 10 - 3))
    pygame.display.update()