
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
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell == 'O':
                    self.player_row, self.player_col = i, j
                elif cell == 'G':
                    self.targets.append((i, j))
                    self.target_count += 1
                elif cell == 'X':
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
        """
        if direction == 'w':
            new_row = self.player_row - 1
            new_col = self.player_col
        elif direction == 's':
            new_row = self.player_row + 1
            new_col = self.player_col
        elif direction == 'a':
            new_row = self.player_row
            new_col = self.player_col - 1
        elif direction == 'd':
            new_row = self.player_row
            new_col = self.player_col + 1
        else:
            return False
    
        if self.map[new_row][new_col] == '#':
            return False
    
        if (new_row, new_col) in self.boxes:
            if direction == 'w':
                box_new_row = new_row - 1
                box_new_col = new_col
            elif direction == 's':
                box_new_row = new_row + 1
                box_new_col = new_col
            elif direction == 'a':
                box_new_row = new_row
                box_new_col = new_col - 1
            elif direction == 'd':
                box_new_row = new_row
                box_new_col = new_col + 1
    
            if self.map[box_new_row][box_new_col] == '#' or (box_new_row, box_new_col) in self.boxes:
                return False
    
            self.boxes.remove((new_row, new_col))
            self.boxes.append((box_new_row, box_new_col))
    
        self.player_row = new_row
        self.player_col = new_col
    
        if set(self.boxes) == set(self.targets):
            self.is_game_over = True
            return True
    
        return False
