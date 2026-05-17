
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
                for k in range(3):
                    if state[i][j][k] == 1:
                        new_state[i][j][k] = direction
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
            moves.append('down')
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
        while len(open_list) < 3:
            current_state = self.initial_state
            while current_state!= self.goal_state[0]:
                current_state = self.get_possible_moves(current_state)
                if current_state == self.goal_state[0]:
                    open_list.append(current_state)
                    self.move(current_state, self.goal_state[1])
                    self.move(current_state, self.goal_state[2])
                    self.move(current_state, self.goal_state[3])
                    self.move(current_state, self.goal_state[4])
                    self.move(current_state, self.goal_state[5])
                    self.move(current_state, self.goal_state[6])
                    self.move(current_state, self.goal_state[7])
                    self.move(current_state, self.goal_state[8])
                    self.move(current_state, self.goal_state[9])
                    self.move(current_state, self.goal_state[10])
                    self.move(current_state, self.goal_state[11])
                    self.move(current_state, self.goal_state[12])
                    self.move(current_state, self.goal_state[13])
                    self.move(current_state, self.goal_state[14])
                    self.move(current_state, self.goal_state[15])
                    self.move(current_state, self.goal_state[16])
                    self.move(current_state, self.goal_state[17])
                    self.move(current_state, self.goal_state[18])
                    self.move(current_state, self.goal_state[19])
                    self.move(current_state, self.goal_state[20])
                    self.move(current_state, self.goal_state[21])
                    self.move(current_state, self.goal_state[22])
                    self.move(current_state, self.goal_state[23])
                    self.move(current_state, self.goal_state[24])
                    self.move(current_state, self.goal_state[25])
                    self.move(current_state, self.goal_state[26])
                    self.move(current_state, self.goal_state[27])
                    self.move(current_state, self.goal_state[28])
                    self.move(current_state, self.goal_state[29])
                    self.move(current_state, self.goal_state[30])
                    self.move(current_state, self.goal_state[31])
                    self.move(current_state, self.goal_state[32])
                    self.move(current_state, self.goal_state[33])
                    self.move(current_state, self.goal_state[34])
                    self.move(current_state, self.goal_state[35])
                    self.move(current_state, self.goal_state[36])