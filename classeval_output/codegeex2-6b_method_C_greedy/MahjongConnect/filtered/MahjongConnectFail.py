import random
class MahjongConnect: 
    def __init__(self, BOARD_SIZE, ICONS):
        """
        initialize the board size and the icon list, create the game board
        :param BOARD_SIZE: list of two integer numbers, representing the number of rows and columns of the game board
        :param ICONS: list of string, representing the icons
        >>>mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.BOARD_SIZE = [4, 4]
        mc.ICONS = ['a', 'b', 'c']
        mc.board = mc.create_board()
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()



    def create_board(self):
        
        board = []
        for i in range(self.BOARD_SIZE[0]):
            board.append([])
            for j in range(self.BOARD_SIZE[1]):
                board[i].append(self.ICONS[random.randint(0, len(self.ICONS) - 1)])
        return board


    def is_valid_move(self, pos1, pos2):
        
        if pos1[0] < 0 or pos1[0] >= self.BOARD_SIZE[0] or pos1[1] < 0 or pos1[1] >= self.BOARD_SIZE[1]:
            return False
        if pos2[0] < 0 or pos2[0] >= self.BOARD_SIZE[0] or pos2[1] < 0 or pos2[1] >= self.BOARD_SIZE[1]:
            return False
        if pos1 == pos2:
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        if self.has_path(pos1, pos2):
            return True
        else:
            return False


    def has_path(self, pos1, pos2):


    def remove_icons(self, pos1, pos2):


    def is_game_over(self):