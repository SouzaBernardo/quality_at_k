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
                    return i, j
    

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        # Find the blank position
        blank_i, blank_j = self.find_blank(state)
    
        # Create a copy of the state
        new_state = [row[:] for row in state]
    
        # Move the blank block based on the given direction
        if direction == 'up':
            new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], new_state[blank_i][blank_j]
        elif direction == 'down':
            new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], new_state[blank_i][blank_j]
        elif direction == 'left':
            new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], new_state[blank_i][blank_j]
        elif direction == 'right':
            new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], new_state[blank_i][blank_j]
    
        return new_state
    

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        moves = []
        blank_i, blank_j = self.find_blank(state)
    
        # Check if moving up is possible
        if blank_i > 0:
            moves.append('up')
    
        # Check if moving down is possible
        if blank_i < 2:
            moves.append('down')
    
        # Check if moving left is possible
        if blank_j > 0:
            moves.append('left')
    
        # Check if moving right is possible
        if blank_j < 2:
            moves.append('right')
    
        return moves
    

    def solve(self):
        # Initialize the open list as a queue and append the initial state
        open_list = [self.initial_state]
        
        # Initialize a dictionary to keep track of visited states
        visited = {tuple(map(tuple, self.initial_state)): None}
        
        # Initialize a dictionary to store the path from the initial state to each state
        path = {tuple(map(tuple, self.initial_state)): []}
        
        # Perform BFS until the open list is empty or the goal state is reached
        while open_list:
            # Get the current state from the front of the open list
            current_state = open_list.pop(0)
            
            # Check if the current state is the goal state
            if current_state == self.goal_state:
                return path[tuple(map(tuple, current_state))]
            
            # Get all possible moves from the current state
            possible_moves = self.get_possible_moves(current_state)
            
            # Generate new states by making each possible move
            for move in possible_moves:
                new_state = self.move(current_state, move)
                
                # Check if the new state has been visited
                if tuple(map(tuple, new_state)) not in visited:
                    # Add the new state to the open list, visited dictionary, and path dictionary
                    open_list.append(new_state)
                    visited[tuple(map(tuple, new_state))] = current_state
                    path[tuple(map(tuple, new_state))] = path[tuple(map(tuple, current_state))] + [move]
        
        # If the open list is empty and the goal state is not reached, return None
        return None