import random
import pygame

#function called when a ghost meet the pacman
def beginning_positions(player_pos_x,player_pos_y, ghost_pos_x,ghost_pos_y):
    player_pos_x = 43
    player_pos_y = 45
    ghost_pos_x = [5, 5, 69, 69]
    ghost_pos_y = [29, 29, 29, 29]

def ghosts_move(ghost_delay, ghost_direction, board_to_move, ghost_pos_x, ghost_pos_y, ghost_d, ghost_u, ghost_l, ghost_r, can_the_ghost_go_forward, can_the_ghost_change_direction, gameDisplay, pacman_bg, ghosts):
    for ii in range(4):
        if ghost_delay[ii] == 0:
            if board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] + 2] and board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] - 2] and board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] + 1] and board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii]] and board_to_move[ghost_pos_y[ii] + 3][ghost_pos_x[ii] - 1]:
                    ghost_d[ii] = True
                    if ghost_direction[ii] == 0:
                        can_the_ghost_go_forward[ii] = True
                    if ghost_direction[ii] != 1:
                        can_the_ghost_change_direction[ii] = True

            if board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] + 2] and board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] - 2] and board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] + 1] and board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii]] and board_to_move[ghost_pos_y[ii] - 3][ghost_pos_x[ii] - 1]:
                    ghost_u[ii] = True
                    if ghost_direction[ii] == 1:
                        can_the_ghost_go_forward[ii] = True
                    if ghost_direction[ii] != 0:
                        can_the_ghost_change_direction[ii] = True

            if board_to_move[ghost_pos_y[ii] + 2][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii] - 2][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii] + 1][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii]][ghost_pos_x[ii] + 3] and board_to_move[ghost_pos_y[ii] - 1][ghost_pos_x[ii] + 3]:
                    ghost_r[ii] = True
                    if ghost_direction[ii] == 2:
                        can_the_ghost_go_forward[ii] = True
                    if ghost_direction[ii] != 3:
                        can_the_ghost_change_direction[ii] = True

            if board_to_move[ghost_pos_y[ii] + 2][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii] - 2][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii] + 1][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii]][ghost_pos_x[ii] - 3] and board_to_move[ghost_pos_y[ii] - 1][ghost_pos_x[ii] - 3]:
                    ghost_l[ii] = True
                    if ghost_direction[ii] == 3:
                        can_the_ghost_go_forward[ii] = True
                    if ghost_direction[ii] != 2:
                        can_the_ghost_change_direction[ii] = True

            move_forward(can_the_ghost_go_forward, ghost_direction, ghost_d, ghost_u, ghost_l, ghost_r, ii)

            change_direction(can_the_ghost_change_direction, ghost_direction, ghost_d, ghost_u, ghost_l, ghost_r, ii)

            if ghost_direction[ii] == 0 and ghost_d[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_y[ii] = ghost_pos_y[ii] + 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))

            elif ghost_direction[ii] == 1 and ghost_u[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_y[ii] = ghost_pos_y[ii] - 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))

            elif ghost_direction[ii] == 2 and ghost_r[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_x[ii] = ghost_pos_x[ii] + 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))

            elif ghost_direction[ii] == 3 and ghost_l[ii]:
                gameDisplay.blit(pacman_bg, (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))
                ghost_pos_x[ii] = ghost_pos_x[ii] - 1
                gameDisplay.blit(ghosts[ii], (ghost_pos_x[ii] * 10 - 3, ghost_pos_y[ii] * 10 - 3))

        else:
            ghost_delay[ii] -= 1

def move_forward(can_the_ghost_go_forward, ghost_direction, ghost_d, ghost_u, ghost_l, ghost_r, ii):
    if not can_the_ghost_go_forward[ii]:
        changed = False

        while not changed:
            rand = random.randint(0, 4)
            tmp = ghost_direction[ii]

            if ghost_d[ii] and rand == 0:
                ghost_direction[ii] = 0
            if ghost_u[ii] and rand == 1:
                ghost_direction[ii] = 1
            if ghost_r[ii] and rand == 2:
                ghost_direction[ii] = 2
            if ghost_l[ii] and rand == 3:
                ghost_direction[ii] = 3

            if can_the_ghost_go_forward[ii] == False and ghost_direction[ii] != tmp:
                changed = True

def change_direction(can_the_ghost_change_direction, ghost_direction, ghost_d, ghost_u, ghost_l, ghost_r, ii):
    if can_the_ghost_change_direction[ii]:
        changed = False

        while not changed:
            rand = random.randint(0, 4)
            tmp = ghost_direction[ii]

            if ghost_d[ii] and rand == 0:
                ghost_direction[ii] = 0
            if ghost_u[ii] and rand == 1:
                ghost_direction[ii] = 1
            if ghost_r[ii] and rand == 2:
                ghost_direction[ii] = 2
            if ghost_l[ii] and rand == 3:
                ghost_direction[ii] = 3

            if ghost_direction[ii] == 0 and tmp != 1:
                changed = True
            elif ghost_direction[ii] == 1 and tmp != 0:
                changed = True
            elif ghost_direction[ii] == 2 and tmp != 3:
                changed = True
            elif ghost_direction[ii] == 3 and tmp != 2:
                changed = True

def player_move(board_to_move, player_pos_x, player_pos_y, gameDisplay, pacman_bg, pacman_directions, board_yellow_dots, score, eating_Sound, eat_Sound, event):
    pass
    # copy paste
