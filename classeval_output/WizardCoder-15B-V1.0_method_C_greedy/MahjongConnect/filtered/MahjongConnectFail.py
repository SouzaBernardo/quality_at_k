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
        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = []
            for j in range(self.BOARD_SIZE[1]):
                row.append(self.ICONS[0])
            board.append(row)
        for i in range(self.BOARD_SIZE[0]):
            for j in range(self.BOARD_SIZE[1]):
                if board[i][j] == self.ICONS[0]:
                    board[i][j] = random.choice(self.ICONS[1:])
        return board

    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False,representing whether the move of two icons is valid
        """
        # check if positions are within the game board range
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1]) or \
                not (0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False
        # check if the two positions are not the same
        if pos1 == pos2:
            return False
        # check if the two positions have the same icon
        if self.board[pos1[0]][pos1[1]]!= self.board[pos2[0]][pos2[1]]:
            return False
        # check if there is a valid path between the two positions
        if not self.has_path(pos1, pos2):
            return False
        return True

    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False,representing whether there is a path between two icons
        """
        # get the x and y coordinates of the icons
        x1, y1 = pos1
        x2, y2 = pos2
        # check if the icons are in the same row or column
        if x1 == x2 or y1 == y2:
            # if they are in the same row or column, check if they are adjacent
            if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
                return True
        # check if the icons are in the same diagonal
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
            # if they are in the same diagonal, check if they are adjacent
            if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
                return True
        # if none of the above conditions are met, there is no path between the icons
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
        if not self.has_path(pos1, pos2):
            return
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 == x2:
            # remove icons on the same row
            for i in range(min(y1, y2), max(y1, y2) + 1):
                self.board[x1][i] =''
        elif y1 == y2:
            # remove icons on the same column
            for i in range(min(x1, x2), max(x1, x2) + 1):
                self.board[i][y1] =''
        else:
            # remove icons on the diagonal
            if x1 < x2:
                x_range = range(x1, x2 + 1)
            else:
                x_range = range(x2, x1 + 1)
            if y1 < y2:
                y_range = range(y1, y2 + 1)
            else:
                y_range = range(y2, y1 + 1)
            for i, j in zip(x_range, y_range):
                self.board[i][j] =''

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False,representing whether the game is over
        """
        for row in self.board:
            for icon in row:
                if icon!='':
                    return False
        return True