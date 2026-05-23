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
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
        return None, None

    def move(self, state, direction):
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
            new_state[1][0] = new_state[1][0] - 1
            new_state[1][1] = new_state[1][1] - 1
            new_state[1][2] = new_state[1][2] - 1
        return new_state

    def get_possible_moves(self, state):
        moves = []
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    direction = 'anywhere'
                    if i > 0 and state[i-1][j] > state[i][j]:
                        direction = 'down'
                    elif i < 2 and state[i+1][j] > state[i][j]:
                        direction = 'up'
                    elif j > 0 and state[i][j-1] > state[i][j]:
                        direction = 'left'
                    elif j < 2 and state[i][j+1] > state[i][j]:
                        direction = 'right'
                    if direction == 'anywhere':
                        direction = random.choice(['up', 'down', 'left', 'right'])
                    moves.append(direction)
        return moves

    def solve(self):
        open_list = [self.initial_state]
        while open_list:
            state = open_list[-1]
            direction = self.get_possible_moves(state)[0]
            open_list.append(state + direction)
    
            for move in self.get_possible_moves(state + direction):
                open_list.append(move)
    
        if self.initial_state == self.goal_state:
            return []
    
        path = []
        for state in open_list:
            if state == self.goal_state:
                path.append(state)
                break
            path.append(state)
    
        return path