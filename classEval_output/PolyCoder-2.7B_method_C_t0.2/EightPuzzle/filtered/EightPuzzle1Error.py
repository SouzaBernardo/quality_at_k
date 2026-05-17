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
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
        pass


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
        for i in range(3):
            for j in range(3):
                if direction == 'up':
                    new_state[i][j] = state[i][j]
                elif direction == 'down':
                    new_state[i][j] = state[i][j]
                elif direction == 'left':
                    new_state[i][j] = state[i][j]
                elif direction == 'right':
                    new_state[i][j] = state[i][j]
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
        for i in range(4):
            moves.append(self.move(state, direction=i))
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
        while len(open_list) > 0:
            current_state = self.initial_state
            current_state.append(self.goal_state[0])
            self.initial_state = current_state
            self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
            self.find_blank(current_state)
            self.move(current_state, 0)
            self.get_possible_moves(current_state)
            self.move(current_state, 1)
            self.get_possible_moves(current_state)
            self.move(current_state, 2)
            self.get_possible_moves(current_state)
            self.move(current_state, 3)
            self.get_possible_moves(current_state)
            self.move(current_state, 4)
            self.get_possible_moves(current_state)
            self.move(current_state, 5)
            self.get_possible_moves(current_state)
            self.move(current_state, 6)
            self.get_possible_moves(current_state)
            self.move(current_state, 7)
            self.get_possible_moves(current_state)
            self.move(current_state, 8)
            self.get_possible_moves(current_state)
            self.move(current_state, 9)
            self.get_possible_moves(current_state)
            self.move(current_state, 10)
            self.get_possible_moves(current_state)
            self.move(current_state, 11)
            self.get_possible_moves(current_state)
            self.move(current_state, 12)
            self.get_possible_moves(current_state)
            self.move(current_state, 13)
            self.get_possible_moves(current_state)
            self.move(current_state, 14)
            self.get_possible_moves(current_state)
            self.move(current_state, 15)
            self.get_possible_moves(current_state)
            self.move(current_state, 16)
            self.get_possible_moves(current_state)
            self.move(current_state, 17)
            self.get_possible_moves(current_state)
            self.move(current_state, 18)
            self.get_possible_moves(current_state)
            self.move(current_state, 19)
            self.get_possible_moves(current_state)
            self.move(current_state, 20)
            self.get_possible_moves(current_state)
            self.move(current_state, 21)
            self.get_possible_moves(current_state)
            self.move(current_state, 22)
            self.get_possible_moves(current_state)
            self.move(current_state, 23)
            self.get_possible_moves(current_state)
            self.move(current_state, 24)
            self.get_possible_moves(current_state)
            self.move(current_state, 25)
            self.get_possible_moves(current_state)
            self.move(current_state, 26)
            self.get_possible_moves(current_state)
            self.move(current_state, 27)
            self.get_possible_moves(current_state)
            self.move(current_state