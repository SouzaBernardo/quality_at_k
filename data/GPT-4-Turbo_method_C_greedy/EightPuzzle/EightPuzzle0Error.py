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
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return i, j
        return None
    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        # Find the blank block
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    blank = (i, j)
    
        # Make a copy of the current state
        new_state = [row[:] for row in state]
    
        # Move the blank block in the given direction
        if direction == 'up':
            if blank[0] != 0:
                new_state[blank[0]][blank[1]], new_state[blank[0] - 1][blank[1]] = new_state[blank[0] - 1][blank[1]], new_state[blank[0]][blank[1]]
        elif direction == 'down':
            if blank[0] != 2:
                new_state[blank[0]][blank[1]], new_state[blank[0] + 1][blank[1]] = new_state[blank[0] + 1][blank[1]], new_state[blank[0]][blank[1]]
        elif direction == 'left':
            if blank[1] != 0:
                new_state[blank[0]][blank[1]], new_state[blank[0]][blank[1] - 1] = new_state[blank[0]][blank[1] - 1], new_state[blank[0]][blank[1]]
        elif direction == 'right':
            if blank[1] != 2:
                new_state[blank[0]][blank[1]], new_state[blank[0]][blank[1] + 1] = new_state[blank[0]][blank[1] + 1], new_state[blank[0]][blank[1]]
    
        return new_state
    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        moves = []
        blank_position = self.find_blank(state)
    
        # Check if blank can move up
        if blank_position[0] > 0:
            moves.append('up')
    
        # Check if blank can move down
        if blank_position[0] < 2:
            moves.append('down')
    
        # Check if blank can move left
        if blank_position[1] > 0:
            moves.append('left')
    
        # Check if blank can move right
        if blank_position[1] < 2:
            moves.append('right')
    
        return moves
    def solve(self):
        open_list = [self.initial_state]
        path = []
        while open_list:
            current_state = open_list.pop(0)
            if current_state == self.goal_state:
                return path
            possible_moves = self.get_possible_moves(current_state)
            for move in possible_moves:
                new_state = self.move(current_state, move)
                open_list.append(new_state)
                path.append(move)
        return path