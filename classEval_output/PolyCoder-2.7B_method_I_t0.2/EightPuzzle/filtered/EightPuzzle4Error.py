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
                if j == 3:
                    return i, j
                i += 1
        return -1, -1



    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        i, j = 0, 0
        while i < len(state):
            if state[i] == 0:
                j += 1
                if j == 3:
                    return state
                i += 1
                if i == len(state):
                    return state
                if direction == 'up':
                    i += 1
                    if i == len(state):
                        return state
                    if direction == 'down':
                        i += 1
                        if i == len(state):
                            return state
                        if direction == 'left':
                            i += 1
                            if i == len(state):
                                return state
                            if direction == 'right':
                                i += 1
                                if i == len(state):
                                    return state
                                if direction == 'down':
                                    i += 1
                                    if i == len(state):
                                        return state
                                    if direction == 'left':
                                        i += 1
                                        if i == len(state):
                                            return state
                                        if direction == 'right':
                                            i += 1
                                            if i == len(state):
                                                return state