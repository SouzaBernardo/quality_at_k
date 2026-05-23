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
        self.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]

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
                print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False,representing whether the move of two icons is valid
        """
        # Check if the two positions are within the game board range
        if pos1 < 0 or pos1 >= self.board.shape[0] or pos2 < 0 or pos2 >= self.board.shape[1]:
            return False
        # Check if the two positions are not the same
        if self.board[pos1][pos2]!= 'a':
            return False
        # Check if the two positions have the same icon
        if self.board[pos1][pos2] == self.board[pos2][pos1]:
            return False
        # Check if there is a valid path between the two positions
        path = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if pos1 == i and pos2 == j:
                    path.append(self.board[i][j])
                elif pos1 == i and pos2 == j + 1:
                    path.append(self.board[i][j + 1])
                elif pos1 == i and pos2 == j + 2:
                    path.append(self.board[i][j + 2])
                else:
                    break
        # If there is no valid path, return False
        if len(path) == 0:
            return False
        return True

    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False,representing whether there is a path between two icons
        """
        # Check if there is a valid path between the two positions
        path = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if pos1 == i and pos2 == j:
                    path.append(self.board[i][j])
                elif pos1 == i and pos2 == j + 1:
                    path.append(self.board[i][j + 1])
                elif pos1 == i and pos2 == j + 2:
                    path.append(self.board[i][j + 2])
                else:
                    break
        # If there is no valid path, return False
        if len(path) == 0:
            return False
        # Get the icon at the current position
        icon = self.board[pos1][pos2]
        # Get the icon at the next position
        icon_next = self.board[pos1 + 1][pos2]
        # Check if the icon at the current position is the same as the icon at the next position
        if icon == icon_next:
            return True
        # If there is no next icon, return False
        return False

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        """
        # Check if the two positions are within the game board range
        if pos1 < 0 or pos1 >= self.board.shape[0] or pos2 < 0 or pos2 >= self.board.shape[1]:
            return None
        # Check if the two positions have the same icon
        if self.board[pos1][pos2] == self.board[pos2][pos1]:
            return None
        # Get the icon at the current position
        icon = self.board[pos1][pos2]
        # Get the icon at the next position
        icon_next = self.board[pos1 + 1][pos2]
        # Check if the icon at the current position is the same as the icon at the next position
        if icon == icon_next:
            return None
        # If there is no next icon, return the removed icons
        return [self.board[pos1][pos2], self.board[pos1 + 1][pos2]]

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False,representing whether the game is over
        """
        # Check if the game is over
        if len(self.board) == 0:
            return True
        # Remove the last two icons on the game board
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i][j] =='' and self.board[i][j + 1] =='':
                    self.board.remove_icons((i, j))