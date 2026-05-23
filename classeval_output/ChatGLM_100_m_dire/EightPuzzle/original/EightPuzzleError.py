
class EightPuzzle: 
    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        :param initial_state: a 3*3 size list of Integer, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]





    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        if direction == 'left':
            self.find_blank(state)
        elif direction == 'right':
            self.find_blank(state)
        elif direction == 'up':
            self.find_blank(state)
        elif direction == 'down':
            self.find_blank(state)
        else:
            raise ValueError("Invalid direction")
        new_state = state[0] + 1, state[1] + 1, state[2]
        self.goal_state = self.goal_state[0] + 1, self.goal_state[1] + 1, self.goal_state[2]
        return new_state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        moves = []
        for i in range(3):
            if state[i] == 0:
                moves.append('up')
            elif state[i] == 1:
                moves.append('down')
            elif state[i] == 2:
                moves.append('left')
            elif state[i] == 3:
                moves.append('right')
        return moves

    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal state.
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
        open_list.append(self.initial_state)
        while open_list:
            state = open_list.pop()
            direction = self.find_blank(state)
            if direction:
                path.append(direction)
            else:
                for i in range(len(self.goal_state)):
                    if self.move(state, direction):
                        open_list.append(state)
                        break
                path.append(self.goal_state[i])
        return path