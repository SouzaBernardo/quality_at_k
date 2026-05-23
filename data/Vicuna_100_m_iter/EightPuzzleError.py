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
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
        return None, None

    def move(state, direction):
        new_state = state.copy()
        if direction == 'up':
            new_state[0][0] = new_state[0][0] + 1
            new_state[0][1] = new_state[0][1] + 1
            new_state[0][2] = new_state[0][2] + 1
        elif direction == 'down':
            new_state[0][0] = new_state[0][0] - 1
            new_state[0][1] = new_state[0][1] - 1
            new_state[0][2] = new_state[0][2] - 1
        elif direction == 'left':
            new_state[1][0] = new_state[1][0] + 1
            new_state[1][1] = new_state[1][1] + 1
            new_state[1][2] = new_state[1][2] + 1
        elif direction == 'right':
            new_state[2][0] = new_state[2][0] + 1
            new_state[2][1] = new_state[2][1] + 1
            new_state[2][2] = new_state[2][2] + 1
        return new_state

    def get_possible_moves(self, state):
        moves = []
        for direction in ['up', 'down', 'left', 'right']:
            new_state = self.move(state, direction)
            if new_state != state:
                moves.append(direction)
        return moves

    def solve(self):
        open_list = [self.initial_state]
        path = []
        while open_list:
            state = open_list[-1]
            open_list.pop()
            goal_state = self.goal_state
            if state == goal_state:
                path.append(state.copy())
                break
            for direction in self.get_possible_moves(state):
                new_state = self.move(state, direction)
                if new_state != state:
                    open_list.append(new_state)
        return path