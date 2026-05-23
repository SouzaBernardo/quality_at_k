class EightPuzzle:  
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile, making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        :param initial_state: a 3*3 size list of Integer, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]



    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        i, j = self.find_blank(state)
        if direction == 'up':
            if i > 0:
                new_state = state.copy()
                new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
                return new_state
        elif direction == 'down':
            if i < 2:
                new_state = state.copy()
                new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
                return new_state
        elif direction == 'left':
            if j > 0:
                new_state = state.copy()
                new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
                return new_state
        elif direction == 'right':
            if j < 2:
                new_state = state.copy()
                new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
                return new_state
        return state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        i, j = self.find_blank(state)
        moves = []
        if i > 0:
            if state[i-1][j]!= 0:
                moves.append('up')
        if i < 2:
            if state[i+1][j]!= 0:
                moves.append('down')
        if j > 0:
            if state[i][j-1]!= 0:
                moves.append('left')
        if j < 2:
            if state[i][j+1]!= 0:
                moves.append('right')
        return moves