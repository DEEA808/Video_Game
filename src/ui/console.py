import sys

import numpy as np
import pygame
import math
import random

from src.domain.board import board, draw_board
SQUARESIZE = 100
FIRST_PLAYER=1
SECOND_PLAYER=2
ROW_COUNT=6
ZERO_VALUE=0
FIRST_TURN=0
SECOND_TURN=1
class UI:
    def __init__(self,game_service):
        self.__game_service=game_service

    def check_column_ui(self,column):
        #column=int(input('column:'))
        try:
            if column < ZERO_VALUE:
                raise ValueError('This column doesnt exits')
            good=self.__game_service.check_column(column)
            if good==True:
                return column
        except ValueError:
            print('This column doesnt exits')

    pygame.init()
    def start_game(self):
        turn=FIRST_TURN
        game_over=False
        b = self.__game_service.get_board()
        draw_board(b)
        while not game_over:
            # b =self.__game_service.get_board()
            # draw_board(b)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                     if turn==FIRST_TURN:
                         posx=event.pos[ZERO_VALUE]
                         column=int(math.floor(posx / SQUARESIZE))
                         #column=self.check_column_ui()
                         row=self.__game_service.find_good_row(column)
                         self.__game_service.draw_circle(row,column,FIRST_PLAYER)
                         if self.__game_service.winning(FIRST_PLAYER)==True:
                             print('Player 1 wins')
                             game_over=True
                         print(b)
                         draw_board(b)
                         turn += 1
                         turn = turn % 2

                if turn == SECOND_TURN and game_over==False:
                          pygame.time.wait(1000)
                          #posx = event.pos[0]
                          #column = int(math.floor(posx / squaresize))
                          column = random.randint(ZERO_VALUE,ROW_COUNT)
                          col= self.check_column_ui(column)
                          row = self.__game_service.find_good_row(col)
                          self.__game_service.draw_circle(row, col, SECOND_PLAYER)
                          if self.__game_service.winning(SECOND_PLAYER) == True:
                                print('Player 2 wins')
                                game_over = True
                          print(b)
                          draw_board(b)
                          turn += 1
                          turn = turn % 2