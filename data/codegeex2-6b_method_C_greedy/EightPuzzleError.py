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


    def move(self, state, direction):


    def get_possible_moves(self, state):
        

        moves = []
        blank_tile = self.find_blank(state)
        if blank_tile[0] != 0:
            moves.append('up')
        if blank_tile[0] != 2:
            moves.append('down')
        if blank_tile[1] != 0:
            moves.append('left')
        if blank_tile[1] != 2:
            moves.append('right')
        return moves


    def solve(self):