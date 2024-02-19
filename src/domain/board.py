import numpy as np
import pygame


SQUARESIZE = 100
COLUMN_COUNT=7
ROW_COUNT=6
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = ROW_COUNT * SQUARESIZE
SIZE=(WIDTH, HEIGHT)
RADIUS=int(SQUARESIZE / 2 - 5)
TWO_INDEX=2
ONE_INDEX=1
SCREEN=pygame.display.set_mode(SIZE)

def board():
    board=np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def draw_board(board):
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(SCREEN, BLUE, (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(SCREEN, BLACK, (int(col * SQUARESIZE + SQUARESIZE / TWO_INDEX), int(row * SQUARESIZE + SQUARESIZE / TWO_INDEX)), RADIUS)

    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col]==ONE_INDEX:
                pygame.draw.circle(SCREEN, RED,
                                   (int(col * SQUARESIZE + SQUARESIZE / TWO_INDEX), HEIGHT - int(row * SQUARESIZE + SQUARESIZE / TWO_INDEX)),
                                   RADIUS)
            elif board[row][col]==TWO_INDEX:
                pygame.draw.circle(SCREEN, YELLOW,
                                   (int(col * SQUARESIZE + SQUARESIZE / TWO_INDEX), HEIGHT - int(row * SQUARESIZE + SQUARESIZE / TWO_INDEX)),
                                   RADIUS)
            pygame.display.update()





