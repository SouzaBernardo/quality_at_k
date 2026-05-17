class PushBoxGame: 
    def __init__(self, map):
        """
        Initialize the push box game with the map and various attributes.
        :param map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element, including the following:
            - '#' represents a wall that neither the player nor the box can pass through;
            - 'O' represents the initial position of the player;
            - 'G' represents the target position;
            - 'X' represents the initial position of the box.
        >>> map = ["#####", "#O  #", "# X #", "#  G#", "#####"]   
        >>> game = PushBoxGame(map)                
        """
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False
        self.init_game()


    def init_game(self):
        """
        Initialize the game by setting the positions of the player, targets, and boxes based on the map.
        """
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'O':
                    self.player_row, self.player_col = i, j
                elif self.map[i][j] == 'G':
                    self.targets.append((i, j))
                    self.target_count += 1
                elif self.map[i][j] == 'X':
                    self.boxes.append((i, j))
    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        """
        for box in self.boxes:
            if box not in self.targets:
                self.is_game_over = False
                return self.is_game_over
        self.is_game_over = True
        return self.is_game_over
    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

        :return: True if the game is won, False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
        dx, dy = 0, 0
        if direction == 'w':
            dx, dy = -1, 0
        elif direction == 's':
            dx, dy = 1, 0
        elif direction == 'a':
            dx, dy = 0, -1
        elif direction == 'd':
            dx, dy = 0, 1

        next_row, next_col = self.player_row + dx, self.player_col + dy
        next_cell = self.map[next_row][next_col]

        if next_cell == '#':
            return False

        if (next_row, next_col) in self.boxes:
            next_box_row, next_box_col = next_row + dx, next_col + dy
            next_box_cell = self.map[next_box_row][next_box_col]

            if next_box_cell == '#' or (next_box_row, next_box_col) in self.boxes:
                return False

            self.boxes.remove((next_row, next_col))
            self.boxes.append((next_box_row, next_box_col))

        self.player_row, self.player_col = next_row, next_col

        return self.check_win()