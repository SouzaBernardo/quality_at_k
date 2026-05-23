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
        
        for row in self.map:
            for col in row:
                if col == '#':
                    self.boxes.append((row, col))
                elif col == 'O':
                    self.player_row, self.player_col = row, col
                elif col == 'G':
                    self.targets.append((row, col))
                elif col == 'X':
                    self.target_count += 1
        
        self.player_col += self.target_count
        self.player_row += self.target_count
        
        self.player_col = self.player_col % len(self.map)
        self.player_row = self.player_row % len(self.map[0])
        
        self.boxes = [(x, y) for x, y in self.boxes if self.map[y][x] == 'X']
        self.targets = [(x, y) for x, y in self.targets if self.map[y][x] == 'G']
        
        self.is_game_over = len(self.boxes) == 0 and len(self.targets) == 0