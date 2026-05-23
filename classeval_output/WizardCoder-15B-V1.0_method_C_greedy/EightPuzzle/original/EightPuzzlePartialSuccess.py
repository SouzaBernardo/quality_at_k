
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
        blank_row, blank_col = self.find_blank(state)
        if direction == 'up':
            new_row, new_col = blank_row - 1, blank_col
        elif direction == 'down':
            new_row, new_col = blank_row + 1, blank_col
        elif direction == 'left':
            new_row, new_col = blank_row, blank_col - 1
        elif direction == 'right':
            new_row, new_col = blank_row, blank_col + 1
        else:
            raise ValueError("Invalid direction")
        if new_row < 0 or new_row > 2 or new_col < 0 or new_col > 2:
            raise ValueError("Invalid move")
        new_state = state.copy()
        new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
        return new_state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        blank_row, blank_col = self.find_blank(state)
        moves = []
        if blank_row > 0:
            moves.append('up')
        if blank_row < 2:
            moves.append('down')
        if blank_col > 0:
            moves.append('left')
        if blank_col < 2:
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
        """
        open_list = [self.initial_state]
        closed_list = []
        path = []
        while open_list:
            current_state = open_list.pop(0)
            if current_state == self.goal_state:
                return path
            closed_list.append(current_state)
            possible_moves = self.get_possible_moves(current_state)
            for move in possible_moves:
                new_state = self.move(current_state, move)
                if new_state not in closed_list and new_state not in open_list:
                    open_list.append(new_state)
                    path.append(move)
        return None