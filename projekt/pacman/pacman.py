import pygame
import board
import time
import copy
import random

s_width = 800
s_height = 800
play_width = 700
play_height =700
block_size = 10
player_pos_x = 43
player_pos_y = 45
dots_eaten = 1
dots_eaten_max=196
los = [2,1,0,3]
can_I_go_forward = [True,True,True,True]
can_I_change = [False,False,False,False]

ghost_pos_x = [19,19,19,19]
ghost_pos_y = [17,29,17,17]

pacmany = ["pacman_open_circle_left.png","pacman_open_circle_right.png","pacman_open_circle_up.png","pacman_open_circle_down.png"]
ghosts_colors = ["ghost_red.png","ghost_green.png","ghost_blue.png","ghost_pink.png"]
ghost_color_frozen = [(0,0,255),(255,255,255)]
#niebieski, biały

gameDisplay =pygame.display.set_mode((800,700))
pygame.display.set_caption('P A C M A N')

blue_color = (0,0,225)
gameExit = False




gameDisplay.fill((0,0,0))
pygame.draw.rect(gameDisplay,(0,255,255),[30,20,741,590],1) #board rectangle

board.board_lines(gameDisplay, blue_color)

    #oddzielenie londu od wody
y_size = 66#61
x_size = 85#80

board_to_move = [[True] * x_size for i in range(y_size)]

board.board_move(board_to_move, x_size, y_size)

board_yellow_dots = [[False] * x_size for i in range(y_size)]
dots_counts = [[False] * x_size for i in range(y_size)]


def yellow_dot(pos_x,pos_y):
    pygame.draw.circle(gameDisplay,(255,255,160),(pos_x,pos_y),6)

board.board_dots(board_yellow_dots)
dots_counts = copy.deepcopy(board_yellow_dots)
for i in range(0,80):
    for j in range(0,61):
        if board_yellow_dots[j][i] == True:
            yellow_dot(i*10-5, j*10-5)

pacman_circle = pygame.image.load("pacman_circle.png")
pacman_circle = pygame.transform.scale(pacman_circle,(39,39))

pacman_bg = pygame.image.load("pacman_bg.png")
pacman_bg = pygame.transform.scale(pacman_bg,(38,36))

pacman_open_circle = []
pacman_open_circle_2 = []
ghosts = []

for i in range(4):
    pacman_open_circle.append(pygame.image.load(pacmany[i]))
    pacman_open_circle_2.append(pygame.transform.scale(pacman_open_circle[i], (36, 36)))
    ghosts.append(pygame.transform.scale(pygame.image.load(ghosts_colors[i]), (36, 36)))

gameDisplay.blit(pacman_open_circle_2[0], (player_pos_x*10-3, player_pos_y*10-3))


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True



    d = False
    u = False
    l = False
    r = False

    ghost_d = [False, False, False, False]
    ghost_u = [False, False, False, False]
    ghost_l = [False, False, False, False]
    ghost_r = [False, False, False, False]

    for ii in range(2,4):

        if los[ii] == 0:
            if board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] + 2] and board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] - 2]:
                if board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] + 1] and board_to_move[ghost_pos_y[ii] + 3][
                    ghost_pos_x[ii]] and board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] - 1]:
                    ghost_d[ii] = True
                    can_I_go_forward[ii] = True

        if los[ii] == 1:
            if board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] + 2] and board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] - 2]:
                if board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] + 1] and board_to_move[ghost_pos_y[ii] - 3][
                    ghost_pos_x[ii]] and board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] - 1]:
                    ghost_u[ii] = True
                    can_I_go_forward[ii] = True

        if los[ii] == 2:
            if board_to_move[ghost_pos_y[ii] + 2][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii] - 2][ghost_pos_x[ii] + 3]:
                if board_to_move[ghost_pos_y[ii] + 1][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii]][
                    ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii] - 1][ghost_pos_x[ii] + 3]:
                    ghost_r[ii] = True
                    can_I_go_forward[ii] = True

        if los[ii] == 3:
            if board_to_move[ghost_pos_y[ii] + 2][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii] - 2][ghost_pos_x[ii] - 3]:
                if board_to_move[ghost_pos_y[ii] + 1][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii]][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii] - 1][ghost_pos_x[ii] - 3]:
                    ghost_l[ii] = True
                    can_I_go_forward[ii] = True



        if board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] + 2] and board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] - 2]:
            if board_to_move[ghost_pos_y[ii]+3][ghost_pos_x[ii] + 1] and board_to_move[ghost_pos_y[ii]+3][ghost_pos_x[ii]] and board_to_move[ghost_pos_y[ii]+3][ghost_pos_x[ii] - 1]:
                ghost_d[ii] = True
                if los[ii] != 1:
                    can_I_change[ii]=True


        if board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] + 2] and board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] - 2]:
            if board_to_move[ghost_pos_y[ii]-3][ghost_pos_x[ii] + 1] and board_to_move[ghost_pos_y[ii]-3][ghost_pos_x[ii]] and board_to_move[ghost_pos_y[ii]-3][ghost_pos_x[ii] - 1]:
                ghost_u[ii] = True
                if los[ii] != 0:
                    can_I_change[ii]=True


        if board_to_move[ghost_pos_y[ii] + 2][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii] - 2][ghost_pos_x[ii] + 3]:
            if board_to_move[ghost_pos_y[ii]+1][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii]][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii]-1][ghost_pos_x[ii] + 3]:
                ghost_r[ii] = True
                if los[ii] != 3:
                    can_I_change[ii]=True


        if board_to_move[ghost_pos_y[ii] + 2][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii] - 2][ghost_pos_x[ii] - 3]:
            if board_to_move[ghost_pos_y[ii]+1][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii]][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii]-1][ghost_pos_x[ii] - 3]:
                ghost_l[ii] = True
                if los[ii] != 2:
                    can_I_change[ii] = True




        if (can_I_go_forward[ii] == False):

            notok = False

            while notok== False:
                rand = random.randint(0, 4)
                tmp = los[ii]

                if ghost_d[ii] and rand == 0:
                   los[ii] = 0
                if ghost_u[ii] and rand == 1:
                   los[ii] = 1
                if ghost_r[ii] and rand == 2:
                   los[ii] = 2
                if ghost_l[ii] and rand == 3:
                   los[ii] = 3

                if (can_I_go_forward[ii] == False):
                    if (los[ii] != tmp):
                        notok = True

        elif can_I_change[ii]:
            notok = False

            while notok== False:
                rand = random.randint(0, 4)
                tmp = los[ii]

                if ghost_d[ii] and rand == 0:
                   los[ii] = 0
                if ghost_u[ii] and rand == 1:
                   los[ii] = 1
                if ghost_r[ii] and rand == 2:
                   los[ii] = 2
                if ghost_l[ii] and rand == 3:
                   los[ii] = 3

                if (los[ii] == 0 and tmp != 1):
                   notok = True
                elif (los[ii] == 1 and tmp != 0):
                   notok = True
                elif (los[ii] == 2 and tmp != 3):
                   notok = True
                elif (los[ii] == 3 and tmp != 2):
                   notok = True

        if (los[ii]==0):
            if ghost_d[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_y[ii] = ghost_pos_y[ii] + 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                if board_yellow_dots[ghost_pos_y[ii]-1][ghost_pos_x[ii]+2]:
                    yellow_dot((ghost_pos_x[ii]+2) * 10 - 5, (ghost_pos_y[ii]-1) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]+2][ghost_pos_x[ii]+5]:
                    yellow_dot((ghost_pos_x[ii]+5) * 10 - 5, (ghost_pos_y[ii]+2) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]+2][ghost_pos_x[ii]-1]:
                    yellow_dot((ghost_pos_x[ii]-1) * 10 - 5, (ghost_pos_y[ii]+2) * 10 - 5)
        elif (los[ii] == 1):
            if ghost_u[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_y[ii] = ghost_pos_y[ii] - 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                if board_yellow_dots[ghost_pos_y[ii]+5][ghost_pos_x[ii]+2]:
                    yellow_dot((ghost_pos_x[ii]+2) * 10 - 5, (ghost_pos_y[ii]+5) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]+2][ghost_pos_x[ii]+5]:
                    yellow_dot((ghost_pos_x[ii]+5) * 10 - 5, (ghost_pos_y[ii]+2) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]+2][ghost_pos_x[ii]-1]:
                    yellow_dot((ghost_pos_x[ii]-1) * 10 - 5, (ghost_pos_y[ii]+2) * 10 - 5)
        elif (los[ii] == 2):
            if ghost_r[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_x[ii] = ghost_pos_x[ii] + 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                if board_yellow_dots[ghost_pos_y[ii]+2][ghost_pos_x[ii]-1]:
                    yellow_dot((ghost_pos_x[ii]-1) * 10 - 5, (ghost_pos_y[ii]+2) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]+5][ghost_pos_x[ii]+2]:
                    yellow_dot((ghost_pos_x[ii]+2) * 10 - 5, (ghost_pos_y[ii]+5) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]-1][ghost_pos_x[ii]+2]:
                    yellow_dot((ghost_pos_x[ii]+2) * 10 - 5, (ghost_pos_y[ii]-1) * 10 - 5)

        elif (los[ii] == 3 ):
            if ghost_l[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_x[ii] = ghost_pos_x[ii] - 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                if board_yellow_dots[ghost_pos_y[ii]+2][ghost_pos_x[ii]+5]:
                    yellow_dot((ghost_pos_x[ii]+5) * 10 - 5, (ghost_pos_y[ii]+2) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]+5][ghost_pos_x[ii]+2]:
                    yellow_dot((ghost_pos_x[ii]+2) * 10 - 5, (ghost_pos_y[ii]+5) * 10 - 5)
                if board_yellow_dots[ghost_pos_y[ii]-1][ghost_pos_x[ii]+2]:
                    yellow_dot((ghost_pos_x[ii]+2) * 10 - 5, (ghost_pos_y[ii]-1) * 10 - 5)


    #gameDisplay.blit(pacman_circle,(185,200))
    if (board_to_move[player_pos_y+3][player_pos_x+2] == True) and (board_to_move[player_pos_y+3][player_pos_x-2] == True):
        d= True
    if (board_to_move[player_pos_y-3][player_pos_x+2] == True) and (board_to_move[player_pos_y-3][player_pos_x-2] == True):
        u= True
    if (board_to_move[player_pos_y+2][player_pos_x-3] == True) and (board_to_move[player_pos_y-2][player_pos_x-3] == True):
        l= True
    if (board_to_move[player_pos_y+2][player_pos_x+3] == True) and (board_to_move[player_pos_y-2][player_pos_x+3] == True):
        r= True

    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_DOWN) and d:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_y=player_pos_y+1
            gameDisplay.blit(pacman_open_circle_2[3], (player_pos_x*10-3, player_pos_y*10-3))
            if dots_counts[player_pos_y][player_pos_x+2] == True:
                dots_counts[player_pos_y][player_pos_x+2] = False
                board_yellow_dots[player_pos_y][player_pos_x+2] = False
                dots_eaten += 1
        elif (event.key == pygame.K_UP) and u:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_y=player_pos_y-1
            gameDisplay.blit(pacman_open_circle_2[2], (player_pos_x*10-3, player_pos_y*10-3))
            if dots_counts[player_pos_y-2][player_pos_x+2] == True:
                dots_counts[player_pos_y-2][player_pos_x+2] = False
                board_yellow_dots[player_pos_y-2][player_pos_x+2] = False

                dots_eaten += 1
        elif (event.key == pygame.K_RIGHT) and r:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_x = player_pos_x + 1
            gameDisplay.blit(pacman_open_circle_2[1], (player_pos_x*10-3, player_pos_y*10-3))
            if dots_counts[player_pos_y+2][player_pos_x] == True:
                dots_counts[player_pos_y+2][player_pos_x] = False
                board_yellow_dots[player_pos_y+2][player_pos_x] = False

                dots_eaten += 1
        elif (event.key == pygame.K_LEFT) and l:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_x = player_pos_x - 1
            gameDisplay.blit(pacman_open_circle_2[0], (player_pos_x*10-3, player_pos_y*10-3))
            if dots_counts[player_pos_y+2][player_pos_x-2] == True:
                dots_counts[player_pos_y+2][player_pos_x-2] = False
                board_yellow_dots[player_pos_y+2][player_pos_x-2] = False

                dots_eaten += 1

        print(dots_eaten)
    # display
    pygame.display.update()
    time.sleep(0.1)



