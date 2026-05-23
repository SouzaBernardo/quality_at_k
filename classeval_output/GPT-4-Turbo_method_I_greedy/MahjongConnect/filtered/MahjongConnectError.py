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
        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = []
            for j in range(self.BOARD_SIZE[1]):
                row.append(random.choice(self.ICONS))
            board.append(row)
        return board
    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        """
        # Check if positions are within the game board range
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1] and 0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False
    
        # Check if the two positions are not the same
        if pos1 == pos2:
            return False
    
        # Check if the two positions have the same icon
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
    
        # Check if there is a valid path between the two positions
        # This is a placeholder, you need to implement the path finding algorithm
        if not self.find_path(pos1, pos2):
            return False
    
        return True
    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        """
        # Initialize the queue for BFS with the start position
        queue = [pos1]
        # Initialize the set for visited positions
        visited = set()
    
        # BFS
        while queue:
            # Get the current position
            current_pos = queue.pop(0)
            # Mark the current position as visited
            visited.add(current_pos)
    
            # If the current position is the end position, return True
            if current_pos == pos2:
                return True
    
            # Get the neighbors of the current position
            neighbors = [(current_pos[0] - 1, current_pos[1]), (current_pos[0] + 1, current_pos[1]), (current_pos[0], current_pos[1] - 1), (current_pos[0], current_pos[1] + 1)]
    
            # For each neighbor
            for neighbor in neighbors:
                # If the neighbor is within the game board range and has not been visited
                if 0 <= neighbor[0] < self.BOARD_SIZE[0] and 0 <= neighbor[1] < self.BOARD_SIZE[1] and neighbor not in visited:
                    # If the neighbor is the end position or the icon at the neighbor position is the same as the icon at the start position
                    if neighbor == pos2 or self.board[neighbor[0]][neighbor[1]] == self.board[pos1[0]][pos1[1]]:
                        # Add the neighbor to the queue
                        queue.append(neighbor)
    
        # If there is no path, return False
        return False
    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        """
        # Check if the move is valid
        if self.is_valid_move(pos1, pos2):
            # Remove the icons at the given positions
            self.board[pos1[0]][pos1[1]] = ' '
            self.board[pos2[0]][pos2[1]] = ' '
    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        """
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True