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
        i, j = 0, 0
        while i < len(state):
            if state[i] == 0:
                j = i
            i += 1
        return j




    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        self.move_forward(state, direction)
        self.move_backward(state, direction)
        return self.get_possible_moves(state)


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
            for j in range(4):
                if state[i][j] == 1:
                    moves.append('up')
                elif state[i][j] == 0:
                    moves.append('down')
                elif state[i][j] == 7:
                    moves.append('left')
                elif state[i][j] == 6:
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
        goal_state = self.goal_state
        while len(open_list)!= 0:
            #print open_list
            #print open_list[0]
            #print open_list[1]
            #print open_list[2]
            #print open_list[3]
            #print open_list[4]
            #print open_list[5]
            #print open_list[6]
            #print open_list[7]
            #print open_list[8]
            #print open_list[9]
            #print open_list[10]
            #print open_list[11]
            #print open_list[12]
            #print open_list[13]
            #print open_list[14]
            #print open_list[15]
            #print open_list[16]
            #print open_list[17]
            #print open_list[18]
            #print open_list[19]
            #print open_list[20]
            #print open_list[21]
            #print open_list[22]
            #print open_list[23]
            #print open_list[24]
            #print open_list[25]
            #print open_list[26]
            #print open_list[27]
            #print open_list[28]
            #print open_list[29]
            #print open_list[30]
            #print open_list[31]
            #print open_list[32]
            #print open_list[33]
            #print open_list[34]
            #print open_list[35]
            #print open_list[36]
            #print open_list[37]
            #print open_list[38]
            #print open_list[39]
            #print open_list[40]
            #print open_list[41]
            #print open_list[42]
            #print open_list[43]
            #print open_list[44]
            #print open_list[45]
            #print open_list[46]
            #print open_list[47]
            #print open_list[48]
            #print open_list[49]
            #print open_list[50]
            #print open_list[51]
            #print open_list[52]
            #print open_list[53]
            #print open_list[54]
            #print open_list[55]
            #print open_list[56]
            #print open_list[57]
            #print open_list[58]
            #print open_list[59]
            #print open_list[60]
            #print open_list[61]
            #print open_list[62]
            #print open_list[63]
            #print open_list[64]
            #print open_list[65]
            #print open_list[66]
            #print open_list[67]
            #print open_list[68]
            #print open_list[69]