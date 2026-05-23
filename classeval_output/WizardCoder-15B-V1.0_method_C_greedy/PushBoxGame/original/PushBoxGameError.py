
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
        self.player_row = self.map.index('O')
        self.player_col = self.map[self.player_row].index('O')
        self.targets = []
        self.boxes = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'G':
                    self.targets.append((row, col))
                elif self.map[row][col] == 'X':
                    self.boxes.append((row, col))
        self.target_count = len(self.targets)
        self.is_game_over = False
    

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        """
        for box in self.boxes:
            if box not in self.targets:
                return False
        self.is_game_over = True
        return True

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w','s', 'a', or 'd' representing up, down, left, or right respectively.
        :return: True if the game is won, False otherwise.
        """
        if direction == 'w':
            if self.player_row > 0 and self.map[self.player_row-1][self.player_col]!= '#':
                self.player_row -= 1
        elif direction =='s':
            if self.player_row < len(self.map)-1 and self.map[self.player_row+1][self.player_col]!= '#':
                self.player_row += 1
        elif direction == 'a':
            if self.player_col > 0 and self.map[self.player_row][self.player_col-1]!= '#':
                self.player_col -= 1
        elif direction == 'd':
            if self.player_col < len(self.map[0])-1 and self.map[self.player_row][self.player_col+1]!= '#':
                self.player_col += 1
        # Check if the player has reached a target
        for target in self.targets:
            if target[0] == self.player_row and target[1] == self.player_col:
                self.target_count += 1
                self.targets.remove(target)
                if self.target_count == len(self.boxes):
                    self.is_game_over = True
                    return True
        # Check if the player has reached a box
        for box in self.boxes:
            if box[0] == self.player_row and box[1] == self.player_col:
                self.boxes.remove(box)
                self.boxes.append((self.player_row, self.player_col))
        return False