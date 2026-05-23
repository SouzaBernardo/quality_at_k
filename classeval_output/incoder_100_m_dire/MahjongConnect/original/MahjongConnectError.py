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
        for r in range(len(self.BOARD_SIZE)):
            board.append([])
            for c in range(len(self.BOARD_SIZE[r])):
                board[r].append(random.choice(self.ICONS))
        return board


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
        board = self.board
        for r in range(len(self.BOARD_SIZE)):
            for c in range(len(self.BOARD_SIZE[r])):
                print(board[r][c], self.ICONS[c])
            print()


    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        x, y = pos1
        x2, y2 = pos2
        if x < 0 or x >= self.BOARD_SIZE[0] or y < 0 or y >= self.BOARD_SIZE[1]:
            return False
        if x == x2 and y == y2:
            return False
        if self.board[x][y] != self.board[x2][y2]:
            return False
        if self.has_path(pos1, pos2):
            return False
        return True


    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        board = self.board
        board[pos1][pos2] = '#'
        board[pos2][pos1] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos2] = '#'
        board[pos2][pos1] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos2][pos2] = '#'
        board[pos1][pos1] = '#'
        board[pos


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
        board = self.board
        board[pos1][pos2] = ' '
        board[pos2][pos1] = ' '
        self.board = board


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
        """
        count = 0
        for row in self.board:
            for col in row:
                if col == '#':
                    count += 1
        if count == 0:
            return True
        else:
            return False
