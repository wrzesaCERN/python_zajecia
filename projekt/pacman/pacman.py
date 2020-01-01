import pygame
#import random

s_width = 800
s_height = 800
play_width = 700
play_height =700
block_size = 10

ghost_color_alive = [(0,255,0),(255,0,0),(0,255,255), (255,255,0),(255,165,0),(128,0,128)]
#zielony,czerwony,jasnyniebieski,żółty,pomarańczowy,fioletowy
ghost_color_frozen = [(0,0,255),(255,255,255)]
#niebieski, biały

gameDisplay =pygame.display.set_mode((800,700))
pygame.display.set_caption('P A C M A N')

blue_color = (0,0,225)
gameExit = False

def yellow_dot(pos_x,pos_y):
    pygame.draw.circle(gameDisplay,(255,255,0),(pos_x,pos_y),6)

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay,(0,255,255),[30,20,741,590],1) #board rectangle

    #left
    pygame.draw.rect(gameDisplay,blue_color,[80,70,100,40],3)
    pygame.draw.rect(gameDisplay,blue_color,[80,160,100,10],3)
    pygame.draw.rect(gameDisplay,blue_color,[230,70,100,39],3)

    pygame.draw.line(gameDisplay, blue_color, (180, 280), (180, 220), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 280), (180, 280), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 220), (180, 220), 3)

    pygame.draw.line(gameDisplay, blue_color, (30, 330), (180, 330), 3)

    pygame.draw.line(gameDisplay, blue_color, (180, 330), (180, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 380), (180, 380), 3)

    pygame.draw.line(gameDisplay, blue_color, (80, 430), (180, 430), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 440), (140, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 430), (80, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (180, 430), (180, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (140, 500), (180, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (140, 440), (140, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (90, 490), (90, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 490), (90, 490), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 500), (90, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (80, 550), (80, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 550), (230, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 560), (240, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 490), (230, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 490), (240, 490), 3)
    pygame.draw.line(gameDisplay, blue_color, (240, 490), (240, 560), 3)

    pygame.draw.line(gameDisplay, blue_color, (230, 160), (230, 290), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 290), (240, 290), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 160), (240, 160), 3)
    pygame.draw.line(gameDisplay, blue_color, (240, 220), (330, 220), 3)
    pygame.draw.line(gameDisplay, blue_color, (240, 230), (330, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (240, 230), (240, 290), 3)
    pygame.draw.line(gameDisplay, blue_color, (240, 160), (240, 220), 3)
    pygame.draw.line(gameDisplay, blue_color, (330, 220), (330, 230), 3)

    pygame.draw.rect(gameDisplay,blue_color,[230,340,10,40],3)

    pygame.draw.rect(gameDisplay,blue_color,[230,430,100,10],3)

    pygame.draw.rect(gameDisplay,blue_color,[290,490,40,70],3)


    #center
    pygame.draw.rect(gameDisplay,blue_color,[380,21,40,89],3)
    pygame.draw.line(gameDisplay, blue_color, (290, 160), (510, 160), 3)
    pygame.draw.line(gameDisplay, blue_color, (290, 160), (290, 170), 3)
    pygame.draw.line(gameDisplay, blue_color, (290, 170), (380, 170), 3)
    pygame.draw.line(gameDisplay, blue_color, (380, 170), (380, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (380, 230), (420, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (420, 170), (420, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (510, 160), (510, 170), 3)
    pygame.draw.line(gameDisplay, blue_color, (420, 170), (510, 170), 3)

    pygame.draw.line(gameDisplay, blue_color, (290, 340), (510, 340), 3)
    pygame.draw.line(gameDisplay, blue_color, (290, 380), (380, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (420, 380), (510, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (290, 340), (290, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (510, 340), (510, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (380, 440), (420, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (380, 380), (380, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (420, 380), (420, 440), 3)

    pygame.draw.line(gameDisplay, blue_color, (380, 490), (380, 609), 3)
    pygame.draw.line(gameDisplay, blue_color, (420, 490), (420, 609), 3)
    pygame.draw.line(gameDisplay, blue_color, (380, 490), (420, 490), 3)

    pygame.draw.rect(gameDisplay,blue_color,[290,280,220,10],3)

    #right
    pygame.draw.rect(gameDisplay,blue_color,[620,70,100,40],3)
    pygame.draw.rect(gameDisplay,blue_color,[620,160,100,10],3)
    pygame.draw.rect(gameDisplay,blue_color,[470,70,100,39],3)

    pygame.draw.line(gameDisplay, blue_color, (620, 280), (620, 220), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 280), (770, 280), 3)

    pygame.draw.line(gameDisplay, blue_color, (620, 330), (770, 330), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 220), (770, 220), 3)

    pygame.draw.line(gameDisplay, blue_color, (620, 330), (620, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 380), (770, 380), 3)

    pygame.draw.line(gameDisplay, blue_color, (720, 430), (620, 430), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 440), (660, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 430), (720, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 430), (620, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (660, 500), (620, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (660, 440), (660, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (710, 490), (710, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (710, 490), (770, 490), 3)
    pygame.draw.line(gameDisplay, blue_color, (710, 500), (770, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (720, 550), (720, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 550), (570, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 560), (560, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 490), (570, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 490), (560, 490), 3)
    pygame.draw.line(gameDisplay, blue_color, (560, 490), (560, 560), 3)

    pygame.draw.line(gameDisplay, blue_color, (570, 160), (570, 290), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 290), (560, 290), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 160), (560, 160), 3)
    pygame.draw.line(gameDisplay, blue_color, (560, 220), (470, 220), 3)
    pygame.draw.line(gameDisplay, blue_color, (560, 230), (470, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (560, 230), (560, 290), 3)
    pygame.draw.line(gameDisplay, blue_color, (560, 160), (560, 220), 3)
    pygame.draw.line(gameDisplay, blue_color, (470, 220), (470, 230), 3)

    pygame.draw.rect(gameDisplay,blue_color,[560,340,10,40],3)

    pygame.draw.rect(gameDisplay,blue_color,[470,430,100,10],3)

    pygame.draw.rect(gameDisplay,blue_color,[470,490,40,70],3)




    #oddzielenie londu od wody
    y_size = 61
    x_size = 80

    board_to_move = [[True] * x_size for i in range(y_size)]

    for i in range(8,18):
        for j in range(7,11):
            board_to_move[j][i] = False

    for i in range(8,18):
        for j in range(16,17):
            board_to_move[j][i] = False

    for i in range(3,18):
        for j in range(22,28):
            board_to_move[j][i] = False

    for i in range(3,18):
        for j in range(33,38):
            board_to_move[j][i] = False

    for i in range(8,18):
        for j in range(43,44):
            board_to_move[j][i] = False

    for i in range(14,18):
        for j in range(44,50):
            board_to_move[j][i] = False

    for i in range(23,24):
        for j in range(50,55):
            board_to_move[j][i] = False

    for i in range(5,25):
        for j in range(49,56):
            board_to_move[j][i] = False

    for i in range(29,51):
        for j in range(28,29):
            board_to_move[j][i] = False

    for i in range(23,24):
        for j in range(34,38):
            board_to_move[j][i] = False

    for i in range(56,57):
        for j in range(34,38):
            board_to_move[j][i] = False

    for i in range(62,77):
        for j in range(32,38):
            board_to_move[j][i] = False

    for i in range(62,72):
        for j in range(43,44):
            board_to_move[j][i] = False

    for i in range(29,51):
        for j in range(34,38):
            board_to_move[j][i] = False

    for i in range(38,42):
        for j in range(38,44):
            board_to_move[j][i] = False

    for i in range(23,33):
        for j in range(43,44):
            board_to_move[j][i] = False

    for i in range(47,57):
        for j in range(43,44):
            board_to_move[j][i] = False

    for i in range(62,66):
        for j in range(44,50):
            board_to_move[j][i] = False

    for i in range(71,77):
        for j in range(49,50):
            board_to_move[j][i] = False

    for i in range(23,34):
        for j in range(7,11):
            board_to_move[j][i] = False

    for i in range(46,57):
        for j in range(7,11):
            board_to_move[j][i] = False

    for i in range(38,42):
        for j in range(2,11):
            board_to_move[j][i] = False

    for i in range(62,72):
        for j in range(7,11):
            board_to_move[j][i] = False

    for i in range(62,77):
        for j in range(23,28):
            board_to_move[j][i] = False

    for i in range(23,24):
        for j in range(16,29):
            board_to_move[j][i] = False

    for i in range(24,33):
        for j in range(22,23):
            board_to_move[j][i] = False

    for i in range(29,51):
        for j in range(16,17):
            board_to_move[j][i] = False

    for i in range(38,42):
        for j in range(17,23):
            board_to_move[j][i] = False

    for i in range(56,57):
        for j in range(16,29):
            board_to_move[j][i] = False

    for i in range(47,55):
        for j in range(22,23):
            board_to_move[j][i] = False

    for i in range(62,72):
        for j in range(16,17):
            board_to_move[j][i] = False

    for i in range(38,42):
        for j in range(49,61):
            board_to_move[j][i] = False

    for i in range(29,33):
        for j in range(49,56):
            board_to_move[j][i] = False

    for i in range(45,49):
        for j in range(49,56):
            board_to_move[j][i] = False

    for i in range(56,57):
        for j in range(49,56):
            board_to_move[j][i] = False

    for i in range(57,72):
        for j in range(55,56):
            board_to_move[j][i] = False



    board_yellow_dots = [[False] * x_size for i in range(y_size)]
    #left up
    for i in range(11):
        board_yellow_dots[5][6+i*3] = True

    for i in range(5):
        board_yellow_dots[8+i*3][6] = True

    for i in range(16):
        board_yellow_dots[8+3*i][21] = True

    for i in range(4):
        board_yellow_dots[20][9+i*3] = True

    board_yellow_dots[8][36] = True
    board_yellow_dots[11][36] = True

    for i in range(11):
        board_yellow_dots[14][6+i*3] = True

    board_yellow_dots[17][27] = True
    board_yellow_dots[20][27] = True

    board_yellow_dots[20][30] = True
    board_yellow_dots[20][33] = True
    board_yellow_dots[20][36] = True

    board_yellow_dots[23][36] = True

    for i in range(5):
        board_yellow_dots[53][6+i*3] = True

    for i in range(10):
        board_yellow_dots[41][6+i*3] = True

    board_yellow_dots[44][6] = True
    board_yellow_dots[47][6] = True
    board_yellow_dots[47][9] = True
    board_yellow_dots[47][12] = True
    board_yellow_dots[50][12] = True

    board_yellow_dots[56][6] = True

    for i in range(6):
        board_yellow_dots[56-i*3][36] = True

    for i in range(11):
        board_yellow_dots[59][6+i*3] = True

    for i in range(4):
        board_yellow_dots[47][24 + i * 3] = True

    for i in range(4):
        board_yellow_dots[47+i*3][27] = True

#right up
    for i in range(11):
        board_yellow_dots[5][45+i*3] = True

    board_yellow_dots[8][45] = True
    board_yellow_dots[11][45] = True
    for i in range(16):
        board_yellow_dots[8+i*3][60] = True

    for i in range(5):
        board_yellow_dots[8+i*3][75] = True

    for i in range(4):
        board_yellow_dots[20][63+i*3] = True

    for i in range(11):
        board_yellow_dots[14][45+i*3] = True

    board_yellow_dots[14][39] = True
    board_yellow_dots[14][42] = True

    board_yellow_dots[17][54] = True
    board_yellow_dots[20][54] = True

    board_yellow_dots[20][45] = True
    board_yellow_dots[20][48] = True
    board_yellow_dots[20][51] = True

    board_yellow_dots[23][45] = True

    for i in range(6):
        board_yellow_dots[56-i*3][45] = True

    for i in range(11):
        board_yellow_dots[59][45+i*3] = True

    for i in range(11):
        board_yellow_dots[41][45+i*3] = True

    for i in range(5):
        board_yellow_dots[47][45 + i * 3] = True

    for i in range(6):
        board_yellow_dots[53][60+i*3] = True

    board_yellow_dots[50][69] = True
    board_yellow_dots[47][69] = True
    board_yellow_dots[47][72] = True
    board_yellow_dots[47][75] = True
    board_yellow_dots[44][75] = True
    board_yellow_dots[56][75] = True
    board_yellow_dots[56][54] = True
    board_yellow_dots[53][54] = True
    board_yellow_dots[50][54] = True


    board_yellow_dots[29][27] = True
    board_yellow_dots[35][27] = True
    board_yellow_dots[38][27] = True

    board_yellow_dots[29][54] = True
    board_yellow_dots[35][54] = True
    board_yellow_dots[38][54] = True

#center
    for i in range(10):
        board_yellow_dots[26][27+i*3] = True
    for i in range(12):
        board_yellow_dots[32][24 + i * 3] = True

    board_yellow_dots[47][39] = True
    board_yellow_dots[47][42] = True


    for i in range(0,80):
        for j in range(0,61):
            if board_yellow_dots[j][i] == True:
                yellow_dot(i*10-5, j*10-5)

    # display
    pygame.display.update()



