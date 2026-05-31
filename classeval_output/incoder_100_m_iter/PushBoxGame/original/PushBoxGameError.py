
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
        
        
    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
        
        for x, y in self.boxes:
            if self.map[y][x] == 'G':
                self.is_game_over = True
                break
        
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
        
        if direction == 'w':
            self.player_row -= 1
        elif direction == 's':
            self.player_row += 1
        elif direction == 'a':
            self.player_col -= 1
        elif direction == 'd':
            self.player_col += 1
        else:
            return False
        
        self.player_col = self.player_col % len(self.map)
        self.player_row = self.player_row % len(self.map[0])
        
        self.boxes = [(x, y) for x, y in self.boxes if self.map[y][x] == 'X']
        self.targets = [(x, y) for x, y in self.targets if self.map[y][x] == 'G']
        
        self.is_game_over = len(self.boxes) == 0 and len(self.targets) == 0
        
        return self.is_game_over