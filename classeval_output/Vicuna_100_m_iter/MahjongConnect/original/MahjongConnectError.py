import random
class MahjongConnect:  
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

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
        """
        board = [[random.choice(self.ICONS) for _ in range(self.BOARD_SIZE[0])] for _ in range(self.BOARD_SIZE[1])]
        return board

    def print_board(self):
        """
        print the game board
        :return: None
        """
        for row in self.board:
            print("".join(row))

    def is_valid_move(pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether the move of two icons is valid
        """
        if pos1[0] < 0 or pos1[0] >= self.BOARD_SIZE[0] or pos1[1] < 0 or pos1[1] >= self.BOARD_SIZE[1] or pos2[0] == pos2[1] or pos2[0] == pos2[1]:
            return False
        if pos1[0] == pos2[0] and pos1[1] == pos2[1]:
            return False
        if pos1[0] != pos2[0] and pos2[0] != pos1[0] and pos1[1] == pos2[1]:
            return False
        if self.is_valid_path(pos1, pos2):
            return True
        return False

    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether there is a path between two icons
        """
        if self.is_valid_move(pos1, pos2):
            for i in range(self.BOARD_SIZE[1]):
                for j in range(self.BOARD_SIZE[0]):
                    if self.board[i][j] == pos1[0] and self.board[i][j] == pos2[0]:
                        if self.is_valid_move((i, j), (i, j)) and self.is_valid_move((i, j), (i, j+1)) and self.is_valid_move((i, j), (i+1, j)) and self.is_valid_move((i, j), (i+1, j+1)):
                            return True
        return False

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.remove_icons((0, 0), (1, 0))
        mc.board = [[' ', 'b', 'c', 'a'],
                    [' ', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
        if not self.is_valid_move(pos1, pos2):
            return
        self.board = [self.board[i:i+2] for i in range(0, self.BOARD_SIZE[0], 2)]
        for i in range(0, self.BOARD_SIZE[1]):
            for j in range(0, self.BOARD_SIZE[0]):
                if self.board[i][j] == pos1[0] and self.board[i][j] == pos2[0]:
                    self.board[i][j] = ' '

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        >>> mc = MahjongConnect([4, 4] ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True