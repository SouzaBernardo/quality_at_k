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
        blank_position = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == blank_position:
                    return i, j
        return None, None


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
        if blank_position is None:
            return state
        if direction == 'up':
            new_state = [[state[x][y-1] for x in range(3)] for y in range(3)]
        elif direction == 'down':
            new_state = [[state[x][y+1] for x in range(3)] for y in range(3)]
        elif direction == 'left':
            new_state = [[state[x-1][y] for x in range(3)] for y in range(3)]
        elif direction == 'right':
            new_state = [[state[x+1][y] for x in range(3)] for y in range(3)]
        else:
            return state
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
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    moves.append('up' if i == 0 else 'down' if j == 0 else 'left' if i == 1 else 'right')
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
        open_list.append([self.initial_state])
        path = []
        while open_list:
            current_state = open_list.pop()
            path.append(self.get_possible_moves(current_state))
            for move in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move)
                if new_state == self.goal_state:
                    return path
                open_list.append(new_state)
        return path