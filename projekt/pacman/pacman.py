import pygame
import board
import time
#import random

s_width = 800
s_height = 800
play_width = 700
play_height =700
block_size = 10
player_pos_x = 19
player_pos_y = 20
ghost_color_alive = [(0,255,0),(255,0,0),(0,255,255), (255,255,0),(255,165,0),(128,0,128)]
pacmany = ["pacman_open_circle_left.png","pacman_open_circle_right.png","pacman_open_circle_up.png","pacman_open_circle_down.png"]
#zielony,czerwony,jasnyniebieski,żółty,pomarańczowy,fioletowy
ghost_color_frozen = [(0,0,255),(255,255,255)]
#niebieski, biały

gameDisplay =pygame.display.set_mode((800,700))
pygame.display.set_caption('P A C M A N')

blue_color = (0,0,225)
gameExit = False

def yellow_dot(pos_x,pos_y):
    pygame.draw.circle(gameDisplay,(255,255,160),(pos_x,pos_y),6)


gameDisplay.fill((0,0,0))
pygame.draw.rect(gameDisplay,(0,255,255),[30,20,741,590],1) #board rectangle

board.board_lines(gameDisplay, blue_color)

    #oddzielenie londu od wody
y_size = 61
x_size = 80

board_to_move = [[True] * x_size for i in range(y_size)]

board.board_move(board_to_move, x_size, y_size)

board_yellow_dots = [[False] * x_size for i in range(y_size)]

board.board_dots(board_yellow_dots)

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

for i in range(4):
    pacman_open_circle.append(pygame.image.load(pacmany[i]))
    pacman_open_circle_2.append(pygame.transform.scale(pacman_open_circle[i], (36, 36)))

gameDisplay.blit(pacman_open_circle_2[3], (player_pos_x*10-3, player_pos_y*10-3))


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True



    d = False
    u = False
    l = False
    r = False
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
        elif (event.key == pygame.K_UP) and u:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_y=player_pos_y-1
            gameDisplay.blit(pacman_open_circle_2[2], (player_pos_x*10-3, player_pos_y*10-3))
        elif (event.key == pygame.K_RIGHT) and r:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_x = player_pos_x + 1
            gameDisplay.blit(pacman_open_circle_2[1], (player_pos_x*10-3, player_pos_y*10-3))
        elif (event.key == pygame.K_LEFT) and l:
            gameDisplay.blit(pacman_bg, (player_pos_x*10-3, player_pos_y*10-3))
            player_pos_x = player_pos_x - 1
            gameDisplay.blit(pacman_open_circle_2[0], (player_pos_x*10-3, player_pos_y*10-3))
    # display
    pygame.display.update()
    time.sleep(0.1)



