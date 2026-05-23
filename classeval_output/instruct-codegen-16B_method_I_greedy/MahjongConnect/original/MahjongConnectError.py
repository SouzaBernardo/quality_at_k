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
        # mark the starting node as visited
        visited[pos1[0]][pos1[1]] = True
        queue.append([pos1, 0])
        while len(queue) > 0:
            # get the first element in the queue
            node, distance = queue.pop(0)
            # if the node is the target node
            if node == pos2:
                return True
            # explore all neighbours
            for neighbour in self.get_neighbours(node):
                # if the neighbour is not visited
                if not visited[neighbour[0]][neighbour[1]]:
                    # mark the neighbour as visited
                    visited[neighbour[0]][neighbour[1]] = True
                    # add the neighbour to the queue
                    queue.append([neighbour, distance + 1])
        return False
        def get_neighbours(self, node):
        """
        get all neighbours of a given node
        :param node: position tuple(x, y)
        :return: list of neighbour position tuples
        """
        neighbours = []
        # check for neighbours in the four directions
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = node[0] + dx
            y = node[1] + dy
            # if the neighbour is within the board
            if 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]:
                neighbours.append((x, y))
        return neighbours

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        """
        # get the positions of the two icons
        x1, y1 = pos1
        x2, y2 = pos2
        # get the path between the two icons
        path = self.find_path(pos1, pos2)
        # remove the icons from the board
        for x, y in path:
            self.board[x][y] = None
        # remove the empty rows and columns
        self.remove_empty_rows_and_columns()

