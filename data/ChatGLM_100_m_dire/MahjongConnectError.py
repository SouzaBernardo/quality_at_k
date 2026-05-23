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
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.create_board()
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
        self.board = [[random.choice(['a', 'b', 'c']) for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]

    def print_board(self):
        """
        print the game board
        :return: None
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.print_board()
        a b c a
        a b c a
        a b c a
        a b c a
        """
        for row in self.board:
            for col in row:
                print(f"{row} {col} {self.ICONS[0]} {self.ICons[1]}")



    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False,representing whether there is a path between two icons
        """
        path = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i][j] == pos1 and self.board[i+1][j] == pos2:
                    path.append((i, j))
        return path.count(pos1) > 0 and path.count(pos2) > 0

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        
        removes the connected icons on the game board and returns None
        """
        # Create a new board with the removed icons
        new_board = [[' ', 'b', 'c', 'a']]
        # Remove the icons from the old board
        for i in range(len(self.board)):
            for j in range(i+1, len(self.board)):
                if self.board[i][j] == self.board[j][i]:
                    self.board[i][j] =''
                    self.board[j][i] =''
                    break
        # Return the new board
        return new_board

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False,representing whether the game is over
        """
        if len(self.board) == 0:
            return True
        return False