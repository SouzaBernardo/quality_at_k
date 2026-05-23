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
        """
        self.board = [[None for _ in range(self.BOARD_SIZE[1])] for _ in range(self.BOARD_SIZE[0])]
        for i in range(self.BOARD_SIZE[0]):
            for j in range(self.BOARD_SIZE[1]):
                self.board[i][j] = random.choice(self.ICONS)
        return self.board



    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False,representing whether there is a path between two icons
        """
        # create a visited array
        visited = [[False for _ in range(self.BOARD_SIZE[1])] for _ in range(self.BOARD_SIZE[0])]
        # create a queue for BFS
        queue = []
        # mark the starting point as visited
        visited[pos1[0]][pos1[1]] = True
        queue.append([pos1, 0])
        while len(queue) > 0:
            # get the first element in the queue
            node = queue.pop(0)
            # get the current node's position
            pos = node[0]
            # get the node's distance
            dist = node[1]
            # check if we reached the end of the path
            if pos == pos2:
                return True
            # explore all neighbors
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # calculate the new position
                    new_pos = (pos[0] + i, pos[1] + j)
                    # check if the new position is within the board
                    if 0 <= new_pos[0] < self.BOARD_SIZE[0] and 0 <= new_pos[1] < self.BOARD_SIZE[1]:
                        # check if the new position is not visited
                        if not visited[new_pos[0]][new_pos[1]]:
                            # mark the new position as visited
                            visited[new_pos[0]][new_pos[1]] = True
                            # add the new position to the queue
                            queue.append([new_pos, dist + 1])
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
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 == x2 and y1 == y2:
            self.board[x1][y1] =''
            self.board[x2][y2] =''
        else:
            self.board[x1][y1] =''
            self.board[x2][y2] =''
            if x1 > x2:
                for i in range(x1 - x2 - 1):
                    self.board[x1 - i - 1][y1] = self.board[x1 - i - 2][y1]
                self.board[x1 - x2][y1] =''
            elif x2 > x1:
                for i in range(x2 - x1 - 1):
                    self.board[x2 - i - 1][y2] = self.board[x2 - i - 2][y2]
                self.board[x2 - x1][y2] =''
            if y1 > y2:
                for i in range(y1 - y2 - 1):
                    self.board[x1][y1 - i - 1] = self.board[x1][y1 - i - 2]
                self.board[x1][y1 - y2] =''
            elif y2 > y1:
                for i in range(y2 - y1 - 1):
                    self.board[x2][y2 - i - 1] = self.board[x2][y2 - i - 2]
                self.board[x2][y2 - y1] =''

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False,representing whether the game is over
        """
        for row in range(self.BOARD_SIZE[0]):
            for col in range(self.BOARD_SIZE[1]):
                if self.board[row][col]!='':
                    return False
        return True