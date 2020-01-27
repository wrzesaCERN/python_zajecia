import pygame

"""
board_lines to funkcja, która rysuje te niebieskie linie na planszy (raz to sa linie raz prostokąty)
"""


def board_lines(gamedisplay):
    # left side
    blue_color = (0, 0, 255)

    gamedisplay.fill((0, 0, 0))  # black background
    pygame.draw.rect(gamedisplay, (0, 255, 255), [30, 20, 741, 590], 1)  # board rectangle

    pygame.draw.rect(gamedisplay, blue_color, [80, 70, 100, 40], 3)
    pygame.draw.rect(gamedisplay, blue_color, [80, 160, 100, 10], 3)
    pygame.draw.rect(gamedisplay, blue_color, [230, 70, 100, 39], 3)

    pygame.draw.line(gamedisplay, blue_color, (180, 280), (180, 220), 3)
    pygame.draw.line(gamedisplay, blue_color, (30, 280), (180, 280), 3)
    pygame.draw.line(gamedisplay, blue_color, (30, 220), (180, 220), 3)

    pygame.draw.line(gamedisplay, blue_color, (30, 330), (180, 330), 3)

    pygame.draw.line(gamedisplay, blue_color, (180, 330), (180, 380), 3)
    pygame.draw.line(gamedisplay, blue_color, (30, 380), (180, 380), 3)

    pygame.draw.line(gamedisplay, blue_color, (80, 430), (180, 430), 3)
    pygame.draw.line(gamedisplay, blue_color, (80, 440), (140, 440), 3)
    pygame.draw.line(gamedisplay, blue_color, (80, 430), (80, 440), 3)
    pygame.draw.line(gamedisplay, blue_color, (180, 430), (180, 500), 3)
    pygame.draw.line(gamedisplay, blue_color, (140, 500), (180, 500), 3)
    pygame.draw.line(gamedisplay, blue_color, (140, 440), (140, 500), 3)

    pygame.draw.line(gamedisplay, blue_color, (90, 490), (90, 500), 3)
    pygame.draw.line(gamedisplay, blue_color, (30, 490), (90, 490), 3)
    pygame.draw.line(gamedisplay, blue_color, (30, 500), (90, 500), 3)

    pygame.draw.line(gamedisplay, blue_color, (80, 550), (80, 560), 3)
    pygame.draw.line(gamedisplay, blue_color, (80, 550), (230, 550), 3)
    pygame.draw.line(gamedisplay, blue_color, (80, 560), (240, 560), 3)
    pygame.draw.line(gamedisplay, blue_color, (230, 490), (230, 550), 3)
    pygame.draw.line(gamedisplay, blue_color, (230, 490), (240, 490), 3)
    pygame.draw.line(gamedisplay, blue_color, (240, 490), (240, 560), 3)

    pygame.draw.line(gamedisplay, blue_color, (230, 160), (230, 290), 3)
    pygame.draw.line(gamedisplay, blue_color, (230, 290), (240, 290), 3)
    pygame.draw.line(gamedisplay, blue_color, (230, 160), (240, 160), 3)
    pygame.draw.line(gamedisplay, blue_color, (240, 220), (330, 220), 3)
    pygame.draw.line(gamedisplay, blue_color, (240, 230), (330, 230), 3)
    pygame.draw.line(gamedisplay, blue_color, (240, 230), (240, 290), 3)
    pygame.draw.line(gamedisplay, blue_color, (240, 160), (240, 220), 3)
    pygame.draw.line(gamedisplay, blue_color, (330, 220), (330, 230), 3)

    pygame.draw.rect(gamedisplay, blue_color, [230, 340, 10, 40], 3)

    pygame.draw.rect(gamedisplay, blue_color, [230, 430, 100, 10], 3)

    pygame.draw.rect(gamedisplay, blue_color, [290, 490, 40, 70], 3)


    # center
    pygame.draw.rect(gamedisplay, blue_color, [380, 21, 40, 89], 3)
    pygame.draw.line(gamedisplay, blue_color, (290, 160), (510, 160), 3)
    pygame.draw.line(gamedisplay, blue_color, (290, 160), (290, 170), 3)
    pygame.draw.line(gamedisplay, blue_color, (290, 170), (380, 170), 3)
    pygame.draw.line(gamedisplay, blue_color, (380, 170), (380, 230), 3)
    pygame.draw.line(gamedisplay, blue_color, (380, 230), (420, 230), 3)
    pygame.draw.line(gamedisplay, blue_color, (420, 170), (420, 230), 3)
    pygame.draw.line(gamedisplay, blue_color, (510, 160), (510, 170), 3)
    pygame.draw.line(gamedisplay, blue_color, (420, 170), (510, 170), 3)

    pygame.draw.line(gamedisplay, blue_color, (290, 340), (510, 340), 3)
    pygame.draw.line(gamedisplay, blue_color, (290, 380), (380, 380), 3)
    pygame.draw.line(gamedisplay, blue_color, (420, 380), (510, 380), 3)
    pygame.draw.line(gamedisplay, blue_color, (290, 340), (290, 380), 3)
    pygame.draw.line(gamedisplay, blue_color, (510, 340), (510, 380), 3)
    pygame.draw.line(gamedisplay, blue_color, (380, 440), (420, 440), 3)
    pygame.draw.line(gamedisplay, blue_color, (380, 380), (380, 440), 3)
    pygame.draw.line(gamedisplay, blue_color, (420, 380), (420, 440), 3)

    pygame.draw.line(gamedisplay, blue_color, (380, 490), (380, 609), 3)
    pygame.draw.line(gamedisplay, blue_color, (420, 490), (420, 609), 3)
    pygame.draw.line(gamedisplay, blue_color, (380, 490), (420, 490), 3)

    pygame.draw.rect(gamedisplay, blue_color, [290, 280, 220, 10], 3)

    # right side
    pygame.draw.rect(gamedisplay, blue_color, [620, 70, 100, 40], 3)
    pygame.draw.rect(gamedisplay, blue_color, [620, 160, 100, 10], 3)
    pygame.draw.rect(gamedisplay, blue_color, [470, 70, 100, 39], 3)

    pygame.draw.line(gamedisplay, blue_color, (620, 280), (620, 220), 3)
    pygame.draw.line(gamedisplay, blue_color, (620, 280), (770, 280), 3)

    pygame.draw.line(gamedisplay, blue_color, (620, 330), (770, 330), 3)
    pygame.draw.line(gamedisplay, blue_color, (620, 220), (770, 220), 3)

    pygame.draw.line(gamedisplay, blue_color, (620, 330), (620, 380), 3)
    pygame.draw.line(gamedisplay, blue_color, (620, 380), (770, 380), 3)

    pygame.draw.line(gamedisplay, blue_color, (720, 430), (620, 430), 3)
    pygame.draw.line(gamedisplay, blue_color, (720, 440), (660, 440), 3)
    pygame.draw.line(gamedisplay, blue_color, (720, 430), (720, 440), 3)
    pygame.draw.line(gamedisplay, blue_color, (620, 430), (620, 500), 3)
    pygame.draw.line(gamedisplay, blue_color, (660, 500), (620, 500), 3)
    pygame.draw.line(gamedisplay, blue_color, (660, 440), (660, 500), 3)

    pygame.draw.line(gamedisplay, blue_color, (710, 490), (710, 500), 3)
    pygame.draw.line(gamedisplay, blue_color, (710, 490), (770, 490), 3)
    pygame.draw.line(gamedisplay, blue_color, (710, 500), (770, 500), 3)

    pygame.draw.line(gamedisplay, blue_color, (720, 550), (720, 560), 3)
    pygame.draw.line(gamedisplay, blue_color, (720, 550), (570, 550), 3)
    pygame.draw.line(gamedisplay, blue_color, (720, 560), (560, 560), 3)
    pygame.draw.line(gamedisplay, blue_color, (570, 490), (570, 550), 3)
    pygame.draw.line(gamedisplay, blue_color, (570, 490), (560, 490), 3)
    pygame.draw.line(gamedisplay, blue_color, (560, 490), (560, 560), 3)

    pygame.draw.line(gamedisplay, blue_color, (570, 160), (570, 290), 3)
    pygame.draw.line(gamedisplay, blue_color, (570, 290), (560, 290), 3)
    pygame.draw.line(gamedisplay, blue_color, (570, 160), (560, 160), 3)
    pygame.draw.line(gamedisplay, blue_color, (560, 220), (470, 220), 3)
    pygame.draw.line(gamedisplay, blue_color, (560, 230), (470, 230), 3)
    pygame.draw.line(gamedisplay, blue_color, (560, 230), (560, 290), 3)
    pygame.draw.line(gamedisplay, blue_color, (560, 160), (560, 220), 3)
    pygame.draw.line(gamedisplay, blue_color, (470, 220), (470, 230), 3)

    pygame.draw.rect(gamedisplay, blue_color, [560, 340, 10, 40], 3)

    pygame.draw.rect(gamedisplay, blue_color, [470, 430, 100, 10], 3)

    pygame.draw.rect(gamedisplay, blue_color, [470, 490, 40, 70], 3)


"""
W ogólności chodzenie po danym fragmencie planszy jest determinowane polami true/false. 
Cała plansza jest podzieona na niewidzialną siatkę, a szerokość ścieżki do chodzenia to pięć klatek. 
Taka ścieżka zawiera klatki ustawione na wartość "true". Pozostałe elementy są false. Duszek/gracz może skęcić np. 
w prawo tylko wtedy gdy po swojej prawej ma 5 pól "true". 

Domyśnie siatka ruchów jest "true" - cała plansza jest true. Fnkcja board_move wyłącza ściany, prostokąty obiekty i inne
elementy, które nie należą do ścieżek z ruchu. Ustawia je na "false".
"""


def board_move(board_to_move):
    for i in range(7, 17):
        for j in range(6, 10):
            board_to_move[j][i] = False

    for i in range(7, 17):
        for j in range(15, 16):
            board_to_move[j][i] = False

    for i in range(2, 17):
        for j in range(21, 27):
            board_to_move[j][i] = False

    for i in range(2, 17):
        for j in range(32, 37):
            board_to_move[j][i] = False

    for i in range(7, 17):
        for j in range(42, 43):
            board_to_move[j][i] = False

    for i in range(13, 17):
        for j in range(43, 49):
            board_to_move[j][i] = False

    for i in range(22, 23):
        for j in range(49, 54):
            board_to_move[j][i] = False

    for i in range(22, 23):
        for j in range(48, 55):
            board_to_move[j][i] = False

    for i in range(28, 50):
        for j in range(27, 28):
            board_to_move[j][i] = False

    for i in range(22, 23):
        for j in range(33, 37):
            board_to_move[j][i] = False

    for i in range(55, 56):
        for j in range(33, 37):
            board_to_move[j][i] = False

    for i in range(61, 76):
        for j in range(32, 37):
            board_to_move[j][i] = False

    for i in range(61, 71):
        for j in range(42, 43):
            board_to_move[j][i] = False

    for i in range(28, 50):
        for j in range(33, 37):
            board_to_move[j][i] = False

    for i in range(37, 41):
        for j in range(37, 43):
            board_to_move[j][i] = False

    for i in range(22, 32):
        for j in range(42, 43):
            board_to_move[j][i] = False

    for i in range(46, 56):
        for j in range(42, 43):
            board_to_move[j][i] = False

    for i in range(61, 65):
        for j in range(43, 49):
            board_to_move[j][i] = False

    for i in range(70, 76):
        for j in range(48, 49):
            board_to_move[j][i] = False

    for i in range(22, 32):
        for j in range(6, 10):
            board_to_move[j][i] = False

    for i in range(46, 56):
        for j in range(6, 10):
            board_to_move[j][i] = False

    for i in range(37, 41):
        for j in range(1, 10):
            board_to_move[j][i] = False

    for i in range(61, 71):
        for j in range(6, 10):
            board_to_move[j][i] = False

    for i in range(61, 76):
        for j in range(21, 27):
            board_to_move[j][i] = False

    for i in range(22, 23):
        for j in range(15, 28):
            board_to_move[j][i] = False

    for i in range(23, 32):
        for j in range(21, 22):
            board_to_move[j][i] = False

    for i in range(28, 50):
        for j in range(15, 16):
            board_to_move[j][i] = False

    for i in range(37, 41):
        for j in range(16, 22):
            board_to_move[j][i] = False

    for i in range(55, 56):
        for j in range(15, 28):
            board_to_move[j][i] = False

    for i in range(46, 54):
        for j in range(21, 22):
            board_to_move[j][i] = False

    for i in range(61, 71):
        for j in range(15, 16):
            board_to_move[j][i] = False

    for i in range(37, 41):
        for j in range(48, 60):
            board_to_move[j][i] = False

    for i in range(28, 32):
        for j in range(48, 55):
            board_to_move[j][i] = False

    for i in range(46, 50):
        for j in range(48, 55):
            board_to_move[j][i] = False

    for i in range(55, 56):
        for j in range(48, 55):
            board_to_move[j][i] = False

    for i in range(56, 71):
        for j in range(54, 55):
            board_to_move[j][i] = False

    for i in range(7, 22):
        for j in range(54, 55):
            board_to_move[j][i] = False

    for i in range(2, 8):
        for j in range(48, 49):
            board_to_move[j][i] = False

    for i in range(2, 77):
        board_to_move[0][i] = False

    for i in range(2, 77):
        board_to_move[60][i] = False

    for i in range(1, 60):
        board_to_move[i][1] = False

    for i in range(1, 60):
        board_to_move[i][76] = False


"""
Funkcja board_dots przypisuje niektórym miejscom na planszy wartość "true".  W miejscu siatki któremu zostało przypisana
wartość "true" zostanie aktywowana żóta kropeczka. Funkcja ta rysuje te kropki.
"""


def board_dots(gamedisplay, board_yellow_dots, yellow_dot):
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

    for i in range(10):
        board_yellow_dots[26][27+i*3] = True

    for i in range(12):
        board_yellow_dots[32][24 + i * 3] = True

    board_yellow_dots[47][39] = True
    board_yellow_dots[47][42] = True

    for i in range(0, 80):
        for j in range(0, 61):
            if board_yellow_dots[j][i]:
                yellow_dot(gamedisplay, i * 10 - 5, j * 10 - 5)


"""
Funkcja board_magic ustawia na aktywne i rysuje te duże kropki na rogach. Są to kropki "magiczne" - po zjedzeniu takiej
 kropki duszki od nas uciekają i są niebieskie i możemy je zjeść ...
"""


def board_magic(gamedisplay, board_magic_dots, super_yellow_dot):
    board_magic_dots[5][6] = True
    board_magic_dots[5][75] = True
    board_magic_dots[59][6] = True
    board_magic_dots[59][75] = True
    for i in range(0, 80):
        for j in range(0, 61):
            if board_magic_dots[j][i]:
                super_yellow_dot(gamedisplay, i*10-5, j*10-5)
