class PushBoxGame:  
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

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
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.targets
        [(3, 3)]
        >>> game.boxes
        [(2, 2)]
        >>> game.player_row
        1
        >>> game.player_col
        1
        """
        map_size = len(self.map)
        self.player_row = int(map_size / 2)
        self.player_col = int(map_size / 2)
        self.targets = []
        self.boxes = []
        self.target_count = 0
        for y in range(0, self.player_row):
            for x in range(0, self.player_col):
                if self.map[y][x] == '#':
                    self.boxes.append((x, y))
                elif self.map[y][x] == 'O':
                    self.player_row, self.player_col = y, x
                    self.targets.append((x, y))
                elif self.map[y][x] == 'G':
                    self.target_count += 1
                    self.targets.append((x, y))
                elif self.map[y][x] == 'X':
                    self.boxes.append((x, y))
        self.target_count = len(self.targets)
        self.is_game_over = self.target_count == 0

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
        win = True
        for box in self.boxes:
            win = win and (self.targets[box[0]][box[1]] == self.targets[box[0]][box[1] + 1] or self.targets[box[0]][box[1]] == self.targets[box[0]][box[1] - 1])
        self.is_game_over = win
        return win

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
        moved = False
        if direction == 'w':
            if self.player_row > 0:
                self.player_row -= 1
                moved = True
        elif direction == 's':
            if self.player_row < self.player_col - 1:
                self.player_row += 1
                moved = True
        elif direction == 'a':
            if self.player_col > 0:
                self.player_col -= 1
                moved = True
        elif direction == 'd':
            if self.player_col < self.player_row - 1:
                self.player_col += 1
                moved = True
        return moved

    def print_map(self):
        """
        Print the map of the push box game.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        """
        for y in range(0, self.player_row):
            for x in range(0, self.player_col):
                print(self.map[y][x], end=' ')
            print('')
        print('')