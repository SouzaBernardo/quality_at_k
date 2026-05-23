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
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return (i, j)

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        i, j = self.find_blank(state)
        if direction == 'up':
            new_i = i - 1
            new_j = j
            while new_i >= 0:
                if state[new_i][new_j]!= 0:
                    new_i -= 1
                else:
                    break
            if new_i < 0:
                return None
            else:
                temp = state[i][j]
                state[i][j] = state[new_i][new_j]
                state[new_i][new_j] = temp
                return state
        elif direction == 'down':
            new_i = i + 1
            new_j = j
            while new_i < 3:
                if state[new_i][new_j]!= 0:
                    new_i += 1
                else:
                    break
            if new_i == 3:
                return None
            else:
                temp = state[i][j]
                state[i][j] = state[new_i][new_j]
                state[new_i][new_j] = temp
                return state
        elif direction == 'left':
            new_i = i
            new_j = j - 1
            while new_j >= 0:
                if state[new_i][new_j]!= 0:
                    new_j -= 1
                else:
                    break
            if new_j < 0:
                return None
            else:
                temp = state[i][j]
                state[i][j] = state[new_i][new_j]
                state[new_i][new_j] = temp
                return state
        elif direction == 'right':
            new_i = i
            new_j = j + 1
            while new_j < 3:
                if state[new_i][new_j]!= 0:
                    new_j += 1
                else:
                    break
            if new_j == 3:
                return None
            else:
                temp = state[i][j]
                state[i][j] = state[new_i][new_j]
                state[new_i][new_j] = temp
                return state
        else:
            return None

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        moves = []
        i, j = self.find_blank(state)
        if i-1 >= 0:
            moves.append('up')
        if i+1 < 3:
            moves.append('down')
        if j-1 >= 0:
            moves.append('left')
        if j+1 < 3:
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
        path = []
        open_list = [self.initial_state]
        while open_list:
            state = open_list.pop(0)
            if state == self.goal_state:
                path.append(state)
                break
            else:
                moves = self.get_possible_moves(state)
                for move in moves:
                    new_state = self.move(state, move)
                    if new_state and new_state not in open_list and new_state not in path:
                        open_list.append(new_state)
        return path