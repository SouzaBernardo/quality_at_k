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
        
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):
                if col == "O":
                    self.player_row = row_index
                    self.player_col = col_index
                elif col == "G":
                    self.targets.append((row_index, col_index))
                    self.target_count += 1
                elif col == "X":
                    self.boxes.append((row_index, col_index))


    def check_win(self):


    def move(self, direction):