import pygame
import board
import time
import funtions

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

blue_color = (0, 0, 225)
y_size = 66#61
x_size = 85#80

# settings at the beginning
score_max = 227
ghost_delay = [0, 11, 2, 16] # delay at the beginning, when ghosts appear on the board


score = 1
player_pos_x = 43
player_pos_y = 45
ghost_direction = [4, 4, 3, 3] # 1 - down, 2 - up, 3 - left, 4 - right
lives = 3

can_the_ghost_go_forward = [True, True, True, True] # If true the ghost can go one step forward, in the same direction. If "false" it means a wall or an obstacle
can_the_ghost_change_direction = [False, False, False, False] # It gives a possibility to change the ghost's direction - not only when hit the wall or obstacles
board_to_move = [[True] * x_size for i in range(y_size)]
board_yellow_dots = [[False] * x_size for i in range(y_size)]

ghost_pos_x = [5, 5, 69, 69]
ghost_pos_y = [29, 29, 29, 29]

pacman = ["pacman_open_circle_left.png", "pacman_open_circle_right.png", "pacman_open_circle_up.png", "pacman_open_circle_down.png"]
ghosts_colors = ["ghost_red.png", "ghost_green.png", "ghost_blue.png", "ghost_pink.png"]
ghost_color_frozen = "ghost_red.png" #musze zrobić nieieskiego ducha

gameDisplay = pygame.display.set_mode((800, 700))
pygame.display.set_caption('P A C M A N')
gameDisplay.fill((0, 0, 0)) # black background
pygame.draw.rect(gameDisplay, (0, 255, 255), [30, 20, 741, 590], 1) # board rectangle
board.board_lines(gameDisplay, blue_color) # A function that draw obstacles on the board

# An array of the board. Every position is labeled as by the true or false value. we can move only if we have 5 true one by one in x and y
board.board_move(board_to_move)

# A board of yellow dots
def yellow_dot(pos_x,pos_y):
    pygame.draw.circle(gameDisplay,(255,255,160),(pos_x,pos_y),6)

board.board_dots(board_yellow_dots)

for i in range(0,80):
    for j in range(0,61):
        if board_yellow_dots[j][i] == True:
            yellow_dot(i*10-5, j*10-5)

#drawing pacman an ghosts
pacman_circle = pygame.image.load("pacman_circle.png")
pacman_circle = pygame.transform.scale(pacman_circle, (39, 39))

pacman_bg = pygame.image.load("pacman_bg.png")
pacman_bg = pygame.transform.scale(pacman_bg, (38, 36))

pacman_directions = []
ghosts = []

for i in range(4):
    pacman_directions.append(pygame.transform.scale(pygame.image.load(pacman[i]), (36, 36)))
    ghosts.append(pygame.transform.scale(pygame.image.load(ghosts_colors[i]), (36, 36)))

gameDisplay.blit(pacman_directions[0], (player_pos_x*10-3, player_pos_y*10-3))

#music
pygame.mixer.set_num_channels(4)
pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play()
eating_Sound = pygame.mixer.Channel(2)
eat_Sound = pygame.mixer.Sound('pacman_chomp.wav')
eat_Sound.set_volume(0.5)
lives_decrease_Sound = pygame.mixer.Channel(3)
lives_Sound = pygame.mixer.Sound('pacman_death.wav')
lives_Sound.set_volume(0.5)

font = pygame.font.SysFont("comicsansms", 36)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    for i in range(0, 80):
        for j in range(0, 61):
            if board_yellow_dots[j][i]:
                yellow_dot(i * 10 - 5, j * 10 - 5)

    d = False
    u = False
    l = False
    r = False

    ghost_d = [False, False, False, False]
    ghost_u = [False, False, False, False]
    ghost_l = [False, False, False, False]
    ghost_r = [False, False, False, False]

    funtions.ghosts_move(ghost_delay, ghost_direction, board_to_move, ghost_pos_x, ghost_pos_y, ghost_d, ghost_u, ghost_l, ghost_r, can_the_ghost_go_forward, can_the_ghost_change_direction, gameDisplay, pacman_bg, ghosts)

    #funtions.player_move(board_to_move, player_pos_x, player_pos_y, gameDisplay, pacman_bg, pacman_directions, board_yellow_dots, score, eating_Sound, eat_Sound, event)
    if board_to_move[player_pos_y+3][player_pos_x+2] and board_to_move[player_pos_y+3][player_pos_x-2]:
        d = True
    if board_to_move[player_pos_y-3][player_pos_x+2] and board_to_move[player_pos_y-3][player_pos_x-2]:
        u = True
    if board_to_move[player_pos_y+2][player_pos_x-3] and board_to_move[player_pos_y-2][player_pos_x-3]:
        l = True
    if board_to_move[player_pos_y+2][player_pos_x+3] and board_to_move[player_pos_y-2][player_pos_x+3]:
        r = True

    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_DOWN) and d:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_y += 1
            gameDisplay.blit(pacman_directions[3], (player_pos_x*10-3, player_pos_y*10-3))
            if board_yellow_dots[player_pos_y][player_pos_x+2]:
                board_yellow_dots[player_pos_y][player_pos_x+2] = False
                score += 1
                if not eating_Sound.get_busy():
                    eating_Sound.play(eat_Sound)
            if board_yellow_dots[player_pos_y+3][player_pos_x+2]:
                board_yellow_dots[player_pos_y+3][player_pos_x+2] = False
                score += 1
                if not eating_Sound.get_busy():
                    eating_Sound.play(eat_Sound)
        elif (event.key == pygame.K_UP) and u:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_y -= 1
            gameDisplay.blit(pacman_directions[2], (player_pos_x*10-3, player_pos_y*10-3))
            if board_yellow_dots[player_pos_y-2][player_pos_x+2]:
                board_yellow_dots[player_pos_y-2][player_pos_x+2] = False
                score += 1
                if not eating_Sound.get_busy():
                    eating_Sound.play(eat_Sound)
            if board_yellow_dots[player_pos_y+1][player_pos_x+2]:
                board_yellow_dots[player_pos_y+1][player_pos_x+2] = False
                score += 1
                if not eating_Sound.get_busy():
                    eating_Sound.play(eat_Sound)
        elif (event.key == pygame.K_RIGHT) and r:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_x += 1
            gameDisplay.blit(pacman_directions[1], (player_pos_x*10-3, player_pos_y*10-3))
            if board_yellow_dots[player_pos_y+2][player_pos_x+3]:
                board_yellow_dots[player_pos_y+2][player_pos_x+3] = False
                score += 1
                if not eating_Sound.get_busy():
                    eating_Sound.play(eat_Sound)
            if board_yellow_dots[player_pos_y + 2][player_pos_x]:
                board_yellow_dots[player_pos_y + 2][player_pos_x] = False
                score += 1
                if not eating_Sound.get_busy():
                    eating_Sound.play(eat_Sound)
        elif (event.key == pygame.K_LEFT) and l:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_x -= 1
            gameDisplay.blit(pacman_directions[0], (player_pos_x*10-3, player_pos_y*10-3))
            if board_yellow_dots[player_pos_y+2][player_pos_x+1]:
                board_yellow_dots[player_pos_y+2][player_pos_x+1] = False
                score += 1
                if not eating_Sound.get_busy():
                    eating_Sound.play(eat_Sound)
        print(score)

    for ii in range(4):
        if abs(player_pos_x - ghost_pos_x[ii]) < 3 and abs(player_pos_y - ghost_pos_y[ii]) < 3:
            if not lives_decrease_Sound.get_busy():
                lives_decrease_Sound.play(lives_Sound)

                gameDisplay.fill((0, 0, 0))  # black background
                pygame.draw.rect(gameDisplay, (0, 255, 255), [30, 20, 741, 590], 1)  # board rectangle
                board.board_lines(gameDisplay, blue_color)  # A function that draw obstacles on the board

                for i in range(0, 80):
                    for j in range(0, 61):
                        if board_yellow_dots[j][i]:
                            yellow_dot(i * 10 - 5, j * 10 - 5)

                player_pos_x = 43
                player_pos_y = 45
                ghost_pos_x = [5, 5, 69, 69]
                ghost_pos_y = [29, 29, 29, 29]
                ghost_delay = [0, 11, 2, 16]

                gameDisplay.blit(pacman_directions[0], (player_pos_x * 10 - 3, player_pos_y * 10 - 3))

                lives -=1
                time.sleep(2)

    pygame.draw.rect(gameDisplay, (0,0,0), [30, 620, 700, 40])
    text = font.render(f'Lives: {lives}/3                                           Scores: {score}/{score_max}', True, (255, 255, 0))
    gameDisplay.blit(text, (100, 630))
    pygame.display.update()
    time.sleep(0.1)



