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
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return i, j
    

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        # Find the blank block
        blank_row, blank_col = self.find_blank(state)
    
        # Make the board move in the given direction
        new_state = [row[:] for row in state]  # Create a copy of the state
    
        if direction == 'up':
            new_state[blank_row][blank_col], new_state[blank_row - 1][blank_col] = new_state[blank_row - 1][blank_col], new_state[blank_row][blank_col]
        elif direction == 'down':
            new_state[blank_row][blank_col], new_state[blank_row + 1][blank_col] = new_state[blank_row + 1][blank_col], new_state[blank_row][blank_col]
        elif direction == 'left':
            new_state[blank_row][blank_col], new_state[blank_row][blank_col - 1] = new_state[blank_row][blank_col - 1], new_state[blank_row][blank_col]
        elif direction == 'right':
            new_state[blank_row][blank_col], new_state[blank_row][blank_col + 1] = new_state[blank_row][blank_col + 1], new_state[blank_row][blank_col]
    
        return new_state
    

    def get_possible_moves(self, state):
        moves = []
        blank_row, blank_col = self.find_blank(state)
    
        # Check if moving up is possible
        if blank_row > 0:
            moves.append('up')
    
        # Check if moving down is possible
        if blank_row < 2:
            moves.append('down')
    
        # Check if moving left is possible
        if blank_col > 0:
            moves.append('left')
    
        # Check if moving right is possible
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
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['right']
        """
        open_list = [self.initial_state]  # Initialize the open list with the initial state
        visited = set()  # Keep track of visited states to avoid loops
    
        while open_list:
            current_state = open_list.pop(0)  # Get the first state from the open list
            visited.add(tuple(map(tuple, current_state)))  # Add the current state to the visited set
    
            if current_state == self.goal_state:  # Check if the current state is the goal state
                # Construct the path from the initial state to the goal state
                path = []
                while current_state != self.initial_state:
                    previous_state, move_direction = current_state[1]
                    path.append(move_direction)
                    current_state = previous_state
                path.reverse()
                return path
    
            possible_moves = self.get_possible_moves(current_state)  # Get possible moves from the current state
    
            for move_direction, new_state in possible_moves:
                if tuple(map(tuple, new_state)) not in visited:  # Check if the new state has not been visited
                    open_list.append(new_state)  # Add the new state to the open list
    
        return []  # Return an empty path if no solution is found