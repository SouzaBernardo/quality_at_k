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
        blank_position = [i for i, x in enumerate(state) if x == 0]
        if len(blank_position) == 1:
            return blank_position[0]
        else:
            raise Exception("The blank position has more than one element")

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        blank_position = self.find_blank(state)
        if direction == 'up':
            new_state = state[0:blank_position[0]] + state[blank_position[0] + 1:blank_position[0] + 2] + state[blank_position[0] + 2:blank_position[0] + 3] + \
                        state[blank_position[0] + 3:blank_position[0] + 4] + state[blank_position[0] + 4:blank_position[0] + 5]
        elif direction == 'down':
            new_state = state[0:blank_position[0]] + state[blank_position[0] + 1:blank_position[0] + 2] + state[blank_position[0] + 2:blank_position[0] + 3] + \
                        state[blank_position[0] + 3:blank_position[0] + 4] + state[blank_position[0] + 4:blank_position[0] + 5]
        elif direction == 'left':
            new_state = state[0:blank_position[0]] + state[blank_position[0] + 1:blank_position[0] + 2] + state[blank_position[0] + 2:blank_position[0] + 3] + \
                        state[blank_position[0] + 3:blank_position[0] + 4] + state[blank_position[0] + 4:blank_position[0] + 5]
        elif direction == 'right':
            new_state = state[0:blank_position[0]] + state[blank_position[0] + 1:blank_position[0] + 2] + state[blank_position[0] + 2:blank_position[0] + 3] + \
                        state[blank_position[0] + 3:blank_position[0] + 4] + state[blank_position[0] + 4:blank_position[0] + 5]
        return new_state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
        """
        moves = []
        blank_position = self.find_blank(state)
        if state[blank_position[0]][blank_position[1]] == 1:
            moves.append('up')
        if state[blank_position[0]][blank_position[1]] == 2:
            moves.append('down')
        if state[blank_position[0]][blank_position[1]] == 3:
            moves.append('left')
        if state[blank_position[0]][blank_position[1]] == 4:
            moves.append('right')
        return moves

    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
        Traversal the possible_moves list and invoke move method to get several new states.Then append them.
        redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['right']
        """
        open_list = []
        open_list.append(self.initial_state)
        path = []
        while len(open_list) > 0:
            state = open_list.pop(0)
            moves = self.get_possible_moves(state)
            for move in moves:
                new_state = self.move(state, move)
                if new_state != self.goal_state:
                    open_list.append(new_state)
                    path.append(move)
        return path