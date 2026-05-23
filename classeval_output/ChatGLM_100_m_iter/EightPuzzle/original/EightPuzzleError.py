
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
        # Check if the state is the goal state
        if state == self.goal_state:
            return (self.goal_state[0][0], self.goal_state[0][1])
        
        # Check if the state is a valid state
        for row in range(3):
            for col in range(3):
                if state[row][col]!= 0:
                    continue
                if state[row][col] == 1:
                    return (row, col)
                elif state[row][col] == 4:
                    return (row, col)
                elif state[row][col] == 7:
                    return (row, col)
        
        # Check if the state is an invalid state
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    continue
                if state[row][col] < 0 or state[row][col] > 12:
                    continue
                if state[row][col]!= 4:
                    continue
                if state[row][col] == 7:
                    continue
                return (row, col)
        
        # If none of the above conditions are met, the blank position is unknown
        return (0, 0)

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        # Check if the state is the goal state
        if state == self.goal_state:
            return [[self.goal_state[0][0], self.goal_state[0][1]],
                   [[self.goal_state[1][0], self.goal_state[1][1]],
                   [[self.goal_state[2][0], self.goal_state[2][1]],
                   [[self.goal_state[3][0], self.goal_state[3][1]]],
                   [0, 0, 0]]
        
        # Check if the state is a valid state
        for row in range(3):
            for col in range(3):
                if state[row][col]!= 0:
                    continue
                if state[row][col] == 1:
                    return [[row, col], [0, 0, 0]],
                   [[row, col], [0, 0, 0]],
                   [[row, col], [0, 0, 0]]]
        
        # Check if the state is an invalid state
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    continue
                if state[row][col] < 0 or state[row][col] > 12:
                    continue
                if state[row][col]!= 4:
                    continue
                if state[row][col] == 7:
                    continue
                return [[row, col], [0, 0, 0]],
                   [[row, col], [0, 0, 0]],
                   [[row, col], [0, 0, 0]]]
        
        # If none of the above conditions are met, the blank block is unknown
        return [[0, 0, 0], [0, 0, 0]]



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
        path = []
        open_list = self.open_list
        while open_list:
            state = open_list.pop()
            direction = 'up' if state[0] == 1 else 'down' if state[0] == 4 else 'left' if state[0] == 7 else 'right'
            path.append((state[0], state[1]))
            for row in range(3):
                for col in range(3):
                    if state[row][col]!= 0:
                        state = self.move(state, direction)
            open_list = self.open_list
        return path