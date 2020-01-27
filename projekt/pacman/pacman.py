import pygame
import time

import board
import ghosts_functions
import game_functions
import player_functions

"""
Ustawienie kilku podstawowych parametrów wejściowych, takich jak wielkość planszy, liczba kropek do zjedzenia (score_max), 
 opóźnienie z jakim wychodzą duchy na początku ghost_delay, początowa pozycja gracza player_pos_x/y etc....
"""

Y_SIZE = 66
X_SIZE = 85

lives = 3
score = 1
score_max = 227
player_pos_x = 43
player_pos_y = 45

atraction = True # jest to zmienna, która decyduje o tym czy duchy są "przyciągane" do gracza czy "odpychane" od niego
ghost_direction = [4, 4, 3, 3] # 1 - down, 2 - up, 3 - left, 4 - right, początkowe kierunki kiedy duchy wychodzą z jam
GHOST_DIRECTION_START = [4, 4, 3, 3]  # te tablice z "start" są przydatne gdy tracimy życie i duchy zaczynają od nowa

ghost_delay = [0, 11, 2, 16] #początkow opóźnienie aby np nie pojawiały się na raz
ghost_pos_x = [5, 5, 69, 69]
ghost_pos_y = [29, 29, 29, 29]
GHOST_POS_X_START = [5, 5, 69, 69]
GHOST_POS_Y_START = [29, 29, 29, 29]

can_the_ghost_go_forward = [True, True, True, True] # true dany duch może poruszać sie w tym samym kierunku, false -  przeszkodę/ściane
can_the_ghost_change_direction = [False, False, False, False] # dany duch ma mozliwość zmiany kierunku (nie tylko gdy spotka np. ścianę)

"""
inicjalizacja i stworzenie pacmanowej planszy
"""
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
gameDisplay = pygame.display.set_mode((800, 700))
pygame.display.set_caption('P A C M A N')

board_to_move = [[True] * X_SIZE for i in range(Y_SIZE)]
board_yellow_dots = [[False] * X_SIZE for i in range(Y_SIZE)]
board_magic_dots = [[False] * X_SIZE for i in range(Y_SIZE)]

board.board_lines(gameDisplay)
board.board_move(board_to_move)
board.board_dots(gameDisplay, board_yellow_dots, game_functions.yellow_dot)
board.board_magic(gameDisplay, board_magic_dots, game_functions.super_yellow_dot)

"""
umieszczenie pacmana i inicjacja duchów
"""
pacman = ["images/pacman_open_circle_left.png", "images/pacman_open_circle_right.png", "images/pacman_open_circle_up.png", "images/pacman_open_circle_down.png"]
ghosts_colors = ["images/ghost_red.png", "images/ghost_green.png", "images/ghost_blue.png", "images/ghost_pink.png"]
ghosts_colors_b = ["images/ghost_red_b.png", "images/ghost_green_b.png", "images/ghost_blue_b.png", "images/ghost_pink_b.png"] #wersje niebieskie po zjedzeniu magicznej kropki

pacman_circle = pygame.image.load("images/pacman_circle.png")
pacman_circle = pygame.transform.scale(pacman_circle, (39, 39))

pacman_bg = pygame.image.load("images/pacman_bg.png")
pacman_bg = pygame.transform.scale(pacman_bg, (38, 36))

pacman_directions = []
ghosts = []
ghosts_b = []

for i in range(4):
    pacman_directions.append(pygame.transform.scale(pygame.image.load(pacman[i]), (36, 36)))
    ghosts.append(pygame.transform.scale(pygame.image.load(ghosts_colors[i]), (36, 36)))
    ghosts_b.append(pygame.transform.scale(pygame.image.load(ghosts_colors_b[i]), (36, 36)))

gameDisplay.blit(pacman_directions[0], (player_pos_x*10-3, player_pos_y*10-3))


"""
muzyka poczatkowa, jedzenie kropek i zabranie życia
"""
pygame.mixer.set_num_channels(4)
pygame.mixer.music.load('music/pacman_beginning.wav')
pygame.mixer.music.play()
eating_Sound = pygame.mixer.Channel(2)
eat_Sound = pygame.mixer.Sound('music/pacman_chomp.wav')
eat_Sound.set_volume(0.5)
lives_decrease_Sound = pygame.mixer.Channel(3)
lives_Sound = pygame.mixer.Sound('music/pacman_death.wav')
lives_Sound.set_volume(0.5)

font = pygame.font.SysFont("comicsansms", 36)

"""
gra rusza. Jej super :D
"""
gameExit = False
while not gameExit:

    #wyjście x-em
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    freeze = True
    if freeze:
        """
        co każdą iterację kropki malowane są od nowa. dlaczego?
        ponieważ duszki to  obrazek, który malowany jest w każdej iteracji na nowej pozycji zgodnej z ich przemieszczeniem.
        Stary duszek na poprzedniej pozycji zsotaje. Dlatego po każdym ruchu duszka malowany jest za nim czarny kwadracik 
        zmazujący jakby starego dzuszka. Prowadzi to jednak do zamazywaniu obrazu kropek i przez duszki. Dlatego poza tym
        co każdą iterację malowane są od nowa kropki. Duszki nie mogą zmienić przypisanych do kropek wartości true.
        Dopiero pacman zamienia kropeczkom, które zjadł wartość true na flase. W kolejnych iteracjach malowane są tylko 
        kropki które mają true.
        """
        for i in range(0, 80):
            for j in range(0, 61):
                if board_yellow_dots[j][i]:
                    game_functions.yellow_dot(gameDisplay, i * 10 - 5, j * 10 - 5)
                if board_magic_dots[j][i]:
                    game_functions.super_yellow_dot(gameDisplay, i * 10 - 5, j * 10 - 5)

        # tablica d_u_l_r mówi nam w którym kierunku moze sie poruszać gracz w danej iteracji
        d_u_l_r = [False, False, False, False]

        # tablice ruchów duchów [duch1, duch 2, duch 3, duch 4]
        ghost_dulr = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]

        #jeśli jest odpychanie to to odpychanie trwa tylko przez 200 iteracji czyli jakieś 20 sekund
        if not atraction:
            counter += 1
            if counter == 200:
                atraction = True
                counter = 0

        """
        Ruchy duszków. 
        
        Najpierw dla każdego jest sprawdzana tablica, w kótrym kierunku moga się poruszyć 
        czy nie napotkali jakichś przeszkód, ścian czy też może mają możliwość zmiany kierunku "check_the_board".
        Potem wybierany jest inny kierunek. "move_forward" i "change_direction" definiuja kierunek ruchu 
        
        Duchy pojawiają sie tylko wtedy gdy ich zmienna związana z opóźnieniem zostaje zredukowana o "0"
        """
        for ii in range(4):
            ghosts_functions.check_the_board(ii, board_to_move, ghost_pos_x, ghost_pos_y, ghost_direction,
                                             ghost_dulr, can_the_ghost_go_forward,
                                             can_the_ghost_change_direction)

            ghost_direction[ii] = ghosts_functions.move_forward(can_the_ghost_go_forward[ii], ghost_direction[ii],
                                                                ghost_dulr[ii], atraction, player_pos_x, player_pos_y,
                                                                ghost_pos_x[ii], ghost_pos_y[ii])

            ghost_direction[ii] = ghosts_functions.change_direction(can_the_ghost_change_direction[ii],
                                                                    ghost_direction[ii], ghost_dulr[ii], atraction, player_pos_x,
                                                                    player_pos_y, ghost_pos_x[ii], ghost_pos_y[ii])

            if ghost_delay[ii] == 0:
                ghosts_functions.dispay_ghosts(ii, ghost_direction, ghost_dulr, ghost_pos_x,
                                               ghost_pos_y, pacman_bg, gameDisplay, ghosts_b, ghosts, not atraction)
            if ghost_delay[ii] > 0:
                ghost_delay[ii] -= 1


        """
        Ruch gracza 
        
        Sprawdzamy, w których kierunkach gracz może się ruszać. Jeśli kierunke wybrany przez gracza na klawiaturze 
        jest dostepny to się tam przemieszczamy. Przy okazji zjadamy kropk i wyłączamy ich widoczność (true-false). 
        Sprawdzamy też czy zjedliśmy magiczną kropkę i jesli tak ustawiamy mozliwoś zabijania duchów oraz ich uciekanie 
        """

        d_u_l_r = player_functions.player_avaliability_to_move(board_to_move, player_pos_x, player_pos_y)

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_DOWN) and d_u_l_r[0]:

                player_pos_x, player_pos_y = player_functions.move_just_move(gameDisplay, pacman_bg, player_pos_x, player_pos_y, pacman_directions[3], 0)
                score = player_functions.move_score(board_yellow_dots, player_pos_x, player_pos_y, 2, 0, eating_Sound, eat_Sound, score, 0)
                power_to_kill = player_functions.move_magic_dot(board_magic_dots, player_pos_x, player_pos_y, 2, 0, 0)

                if power_to_kill:
                    atraction = False
                    counter = 0

            elif (event.key == pygame.K_UP) and d_u_l_r[1]:

                player_pos_x, player_pos_y = player_functions.move_just_move(gameDisplay, pacman_bg, player_pos_x, player_pos_y, pacman_directions[2], 1)
                score = player_functions.move_score(board_yellow_dots, player_pos_x, player_pos_y, 2, 1, eating_Sound, eat_Sound, score, 1)
                power_to_kill = player_functions.move_magic_dot(board_magic_dots, player_pos_x, player_pos_y, 2, 1, 1)

                if power_to_kill:
                    atraction = False
                    counter = 0

            elif (event.key == pygame.K_RIGHT) and d_u_l_r[3]:

                player_pos_x, player_pos_y = player_functions.move_just_move(gameDisplay, pacman_bg, player_pos_x, player_pos_y, pacman_directions[1], 2)
                score = player_functions.move_score(board_yellow_dots, player_pos_x, player_pos_y, 3, 2, eating_Sound, eat_Sound, score, 2)
                power_to_kill = player_functions.move_magic_dot(board_magic_dots, player_pos_x, player_pos_y, 3, 2, 2)

                if power_to_kill:
                    atraction = False
                    counter = 0

            elif (event.key == pygame.K_LEFT) and d_u_l_r[2]:

                player_pos_x, player_pos_y = player_functions.move_just_move(gameDisplay, pacman_bg, player_pos_x, player_pos_y, pacman_directions[0], 3)
                score = player_functions.move_score(board_yellow_dots, player_pos_x, player_pos_y, 1, 2, eating_Sound, eat_Sound, score, 3)
                power_to_kill = player_functions.move_magic_dot(board_magic_dots, player_pos_x, player_pos_y, 1, 2, 3)

                if power_to_kill:
                    atraction = False
                    counter = 0

        # obsługa naszej wygranej
        if score == score_max:
            game_functions.retry(gameDisplay, True, board_yellow_dots, game_functions.yellow_dot, board_magic_dots, game_functions.super_yellow_dot)

            lives = 3
            score = 1
            atraction = True
            player_pos_x = 43
            player_pos_y = 45
            ghost_pos_x = [5, 5, 69, 69]
            ghost_pos_y = [29, 29, 29, 29]
            ghost_direction = [4, 4, 3, 3]  # 1 - down, 2 - up, 3 - left, 4 - right
            ghost_delay = [0, 11, 2, 16]
            game_functions.onceagain(gameDisplay, board_yellow_dots, board_magic_dots, pacman_directions,
                      player_pos_x, player_pos_y)
            time.sleep(2)

        #sytuacja gdy duch i gracz są zdecydowanie za blisko
        for ii in range(4):
            if abs(player_pos_x - ghost_pos_x[ii]) < 3 and abs(player_pos_y - ghost_pos_y[ii]) < 3:

                # obsługa utraty życia
                if atraction:
                    if not lives_decrease_Sound.get_busy():
                        lives_decrease_Sound.play(lives_Sound)

                    # nie tylko utrata zycia a też śmierć :/
                    if lives == 1:
                        game_functions.retry(gameDisplay, False, board_yellow_dots, game_functions.yellow_dot, board_magic_dots,
                                            game_functions.super_yellow_dot)
                        lives = 4
                        score = 0

                    atraction = True
                    counter = 0
                    lives -= 1

                    player_pos_x = 43
                    player_pos_y = 45
                    ghost_pos_x = [5, 5, 69, 69]
                    ghost_pos_y = [29, 29, 29, 29]
                    ghost_direction = [4, 4, 3, 3]  # 1 - down, 2 - up, 3 - left, 4 - right
                    ghost_delay = [0, 11, 2, 16]

                    # jeśli nadal żyjemy po utacie życia cofa duchy i pacmana do ustawień pierwotnych (położenia, opóźnienia)
                    game_functions.still_alive(gameDisplay, board_yellow_dots, game_functions.yellow_dot, board_magic_dots,
                                game_functions.super_yellow_dot, pacman_directions, player_pos_x, player_pos_y)

                    time.sleep(2)

                #obsługa sytucji zjedzenia ducha. pojedyńczy duch gdy się pojawi ponownie to w swoim poczatkowym położeniu etc.
                else:
                    ghost_pos_x[ii] = GHOST_POS_X_START[ii]
                    ghost_pos_y[ii] = GHOST_POS_Y_START[ii]
                    ghost_delay[ii] = 200
                    ghost_direction[ii] = GHOST_DIRECTION_START[ii]

        # wyświetlanie aktualnych informacji na dole ekranu
        pygame.draw.rect(gameDisplay, (0, 0, 0), [30, 620, 700, 40])
        text = font.render(f'Lives: {lives}/3                                           Scores: {score}/{score_max}',
                           True, (255, 255, 0))
        gameDisplay.blit(text, (100, 630))
        pygame.display.update()
        time.sleep(0.1)


