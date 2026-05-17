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
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
        i, j = 0, 0
        while i < len(state):
            if state[i] == 0:
                j += 1
            i += 1
        return i, j



    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        new_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        i, j = 0, 0
        while i < len(state):
            if state[i] == 0:
                j += 1
            i += 1
            if direction == 'up':
                if j == 0:
                    new_state[i][0] = 1
                elif j == 1:
                    new_state[i][1] = 1
                elif j == 2:
                    new_state[i][2] = 1
            elif direction == 'down':
                if j == 0:
                    new_state[i][0] = 0
                elif j == 1:
                    new_state[i][1] = 0
                elif j == 2:
                    new_state[i][2] = 0
            elif direction == 'left':
                if j == 0:
                    new_state[i][0] = 0
                elif j == 1:
                    new_state[i][1] = 0
                elif j == 2:
                    new_state[i][2] = 0
            elif direction == 'right':
                if j == 0:
                    new_state[i][0] = 0
                elif j == 1:
                    new_state[i][1] = 0
                elif j == 2:
                    new_state[i][2] = 0
            else:
                raise ValueError('direction must be one of [up, down, left, right]')
            i += 1
        return new_state




    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
        """
        moves = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        i, j = 0, 0
        while i < len(state):
            if state[i] == 0:
                j += 1
            i += 1
            if state[i] == 0:
                moves[i][0] = 1
            elif state[i] == 1:
                moves[i][1] = 1
            elif state[i] == 2: