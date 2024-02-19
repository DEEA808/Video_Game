FREE_SPACE=0
GOOD_ROW=5
ROW_COUNT=6
GOOD_COLUMNS=4
COLUMN_COUNT=7
GOOD_ROWS=3
class GameService:
    def __init__(self,board):
        self.__board=board


    def get_board(self):
        return self.__board

    def check_column(self,column):
        if self.__board[GOOD_ROW][column] == FREE_SPACE:
            return True
        return False


    def find_good_row(self,column):
        for row in range(ROW_COUNT):
            if self.__board[row][column]==FREE_SPACE:
                return row

    def draw_circle(self,row,column,player):
        self.__board[row][column]=player
        print(self.__board[row][column])


    def winning(self,player):
        #Horizontal
        for column in range(GOOD_COLUMNS):
            for row in range(ROW_COUNT):
                if self.__board[row][column]==player and self.__board[row][column+1]==player and self.__board[row][column+2]==player and self.__board[row][column+3]==player:
                    return True

        #Vertical
        for column in range(COLUMN_COUNT):
            for row in range(GOOD_ROWS):
                if self.__board[row][column]==player and self.__board[row+1][column]==player and self.__board[row+2][column]==player and self.__board[row+3][column]==player:
                    return True

        #diagonal1
        for column in range(GOOD_COLUMNS):
            for row in range(GOOD_ROWS):
                if self.__board[row][column]==player and self.__board[row+1][column+1]==player and self.__board[row+2][column+2]==player and self.__board[row+3][column+3]==player:
                    return True

        #diagonal2
        for column in range(GOOD_COLUMNS):
            for row in range(GOOD_ROWS,ROW_COUNT):
                if self.__board[row][column]==player and self.__board[row-1][column+1]==player and self.__board[row-2][column+2]==player and self.__board[row-3][column+3]==player:
                    return True

