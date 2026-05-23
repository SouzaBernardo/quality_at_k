class EightPuzzle: 
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
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == 0:
                    return (i, j)

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        row, col = self.find_blank(state)
        if direction == 'up':
            new_row = row - 1
            new_state = [[state[row][col] for row in range(3)] for col in range(3)]
            new_state[row][col] = state[new_row][col]
            new_state[new_row][col] = 0
            return new_state
        elif direction == 'down':
            new_row = row + 1
            new_state = [[state[row][col] for row in range(3)] for col in range(3)]
            new_state[row][col] = state[new_row][col]
            new_state[new_row][col] = 0
            return new_state
        elif direction == 'left':
            new_col = col - 1
            new_state = [[state[row][col] for row in range(3)] for col in range(3)]
            new_state[row][col] = state[row][new_col]
            new_state[row][new_col] = 0
            return new_state
        elif direction == 'right':
            new_col = col + 1
            new_state = [[state[row][col] for row in range(3)] for col in range(3)]
            new_state[row][col] = state[row][new_col]
            new_state[row][new_col] = 0
            return new_state
        else:
            raise ValueError('Direction should be one of the four: up, down, left, right')

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        moves = []
        row, col = self.find_blank(state)
        if row > 0:
            moves.append('up')
        if row < 2:
            moves.append('down')
        if col > 0:
            moves.append('left')
        if col < 2:
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
        ['right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', '
        """