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

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay,(0,255,255),[30,20,741,590],1) #board rectangle

    #left
    pygame.draw.rect(gameDisplay,blue_color,[80,70,100,40],3)
    pygame.draw.rect(gameDisplay,blue_color,[80,160,100,20],3)
    pygame.draw.rect(gameDisplay,blue_color,[230,70,110,39],3)

    pygame.draw.line(gameDisplay, blue_color, (180, 280), (180, 225), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 280), (180, 280), 3)

    pygame.draw.line(gameDisplay, blue_color, (30, 330), (180, 330), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 225), (180, 225), 3)

    pygame.draw.line(gameDisplay, blue_color, (180, 330), (180, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 380), (180, 380), 3)

    pygame.draw.line(gameDisplay, blue_color, (80, 430), (180, 430), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 440), (130, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 430), (80, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (180, 430), (180, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (130, 500), (180, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (130, 440), (130, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (80, 490), (80, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 490), (80, 490), 3)
    pygame.draw.line(gameDisplay, blue_color, (30, 500), (80, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (80, 550), (80, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 550), (230, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (80, 560), (250, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 500), (230, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 500), (250, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (250, 500), (250, 560), 3)

    pygame.draw.line(gameDisplay, blue_color, (230, 160), (230, 280), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 280), (250, 280), 3)
    pygame.draw.line(gameDisplay, blue_color, (230, 160), (250, 160), 3)
    pygame.draw.line(gameDisplay, blue_color, (250, 230), (340, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (250, 250), (340, 250), 3)
    pygame.draw.line(gameDisplay, blue_color, (250, 250), (250, 280), 3)
    pygame.draw.line(gameDisplay, blue_color, (250, 160), (250, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (340, 230), (340, 250), 3)

    pygame.draw.rect(gameDisplay,blue_color,[230,330,20,50],3)

    pygame.draw.rect(gameDisplay,blue_color,[230,430,110,20],3)

    pygame.draw.rect(gameDisplay,blue_color,[300,500,40,60],3)


    #center
    pygame.draw.rect(gameDisplay,blue_color,[390,21,20,89],3)
    pygame.draw.line(gameDisplay, blue_color, (300, 160), (500, 160), 3)
    pygame.draw.line(gameDisplay, blue_color, (300, 160), (300, 180), 3)
    pygame.draw.line(gameDisplay, blue_color, (300, 180), (390, 180), 3)
    pygame.draw.line(gameDisplay, blue_color, (390, 180), (390, 250), 3)
    pygame.draw.line(gameDisplay, blue_color, (390, 250), (410, 250), 3)
    pygame.draw.line(gameDisplay, blue_color, (410, 180), (410, 250), 3)
    pygame.draw.line(gameDisplay, blue_color, (500, 160), (500, 180), 3)
    pygame.draw.line(gameDisplay, blue_color, (410, 180), (500, 180), 3)

    pygame.draw.line(gameDisplay, blue_color, (300, 360), (500, 360), 3)
    pygame.draw.line(gameDisplay, blue_color, (300, 380), (390, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (410, 380), (500, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (300, 360), (300, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (500, 360), (500, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (390, 450), (410, 450), 3)
    pygame.draw.line(gameDisplay, blue_color, (390, 380), (390, 450), 3)
    pygame.draw.line(gameDisplay, blue_color, (410, 380), (410, 450), 3)

    pygame.draw.line(gameDisplay, blue_color, (390, 500), (390, 609), 3)
    pygame.draw.line(gameDisplay, blue_color, (410, 500), (410, 609), 3)
    pygame.draw.line(gameDisplay, blue_color, (390, 500), (410, 500), 3)

    pygame.draw.rect(gameDisplay,blue_color,[300,300,200,10],3)

    #right
    pygame.draw.rect(gameDisplay,blue_color,[620,70,100,40],3)
    pygame.draw.rect(gameDisplay,blue_color,[620,160,100,20],3)
    pygame.draw.rect(gameDisplay,blue_color,[460,70,110,39],3)

    pygame.draw.line(gameDisplay, blue_color, (620, 280), (620, 225), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 280), (770, 280), 3)

    pygame.draw.line(gameDisplay, blue_color, (620, 330), (770, 330), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 225), (770, 225), 3)

    pygame.draw.line(gameDisplay, blue_color, (620, 330), (620, 380), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 380), (770, 380), 3)

    pygame.draw.line(gameDisplay, blue_color, (720, 430), (620, 430), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 440), (670, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 430), (720, 440), 3)
    pygame.draw.line(gameDisplay, blue_color, (620, 430), (620, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (670, 500), (620, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (670, 440), (670, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (720, 490), (720, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 490), (770, 490), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 500), (770, 500), 3)

    pygame.draw.line(gameDisplay, blue_color, (720, 550), (720, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 550), (570, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (720, 560), (550, 560), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 500), (570, 550), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 500), (550, 500), 3)
    pygame.draw.line(gameDisplay, blue_color, (550, 500), (550, 560), 3)

    pygame.draw.line(gameDisplay, blue_color, (570, 160), (570, 280), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 280), (550, 280), 3)
    pygame.draw.line(gameDisplay, blue_color, (570, 160), (550, 160), 3)
    pygame.draw.line(gameDisplay, blue_color, (550, 230), (460, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (550, 250), (460, 250), 3)
    pygame.draw.line(gameDisplay, blue_color, (550, 250), (550, 280), 3)
    pygame.draw.line(gameDisplay, blue_color, (550, 160), (550, 230), 3)
    pygame.draw.line(gameDisplay, blue_color, (460, 230), (460, 250), 3)

    pygame.draw.rect(gameDisplay,blue_color,[550,330,20,50],3)

    pygame.draw.rect(gameDisplay,blue_color,[460,430,110,20],3)

    pygame.draw.rect(gameDisplay,blue_color,[460,500,40,60],3)

    #display
    pygame.display.update()

