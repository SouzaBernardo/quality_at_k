import random

class MahjongConnect:
    """
     MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, BOARD_SIZE, ICONS):
        """
        Initialize the board size and the icon list, create the game board
        :param BOARD_SIZE: list of two integer numbers, representing the number of rows and columns of the game board
        :param ICONS: list of string, representing the icons
        >>>mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>>mc.BOARD_SIZE = [4, 4]
        >>>mc.ICONS = ['a', 'b', 'c']
        >>>mc.board = mc.create_board()
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        >>>mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>>mc.create_board()
        >>>mc.board = [['a', 'b', 'c', 'a'],