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
        self.player_col = self.get_player_col()
        self.player_row = self.get_player_row()
        self.boxes = self.get_boxes()
        self.targets = self.get_targets()
        self.is_game_over = self.check_game_over()


    def check_win(self):
        boxes_on_target = 0
        for target in self.targets:
            if self.map[target[2]][target[3]] == '#':
                continue
            if self.map[target[2]][target[3]] == self.map[self.player_col][self.player_row]:
                boxes_on_target += 1
        return boxes_on_target == len(self.targets)

    def move(self, direction):
        if direction == 'w':
            if self.player_col < len(self.map) - 1:
                self.player_col += 1
                self.check_win()
        elif direction == 's':
            if self.player_col > 0:
                self.player_col -= 1
                self.check_win()
        elif direction == 'a':
            if self.player_row < len(self.map[0]) - 1:
                self.player_row += 1
                self.check_win()
        elif direction == 'd':
            if self.player_row > 0:
                self.player_row -= 1
                self.check_win()
        else:
            self.is_game_over = True
            self.check_win()