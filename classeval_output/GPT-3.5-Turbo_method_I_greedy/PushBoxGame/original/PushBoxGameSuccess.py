
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
        """
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'O':
                    self.player_row = row
                    self.player_col = col
                elif self.map[row][col] == 'G':
                    self.targets.append((row, col))
                    self.target_count += 1
                elif self.map[row][col] == 'X':
                    self.boxes.append((row, col))
    

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        """
        placed_boxes = 0
        for box in self.boxes:
            if box in self.targets:
                placed_boxes += 1
        self.is_game_over = placed_boxes == self.target_count
        return self.is_game_over
    

    def move(self, direction):
        # Determine the new position of the player based on the specified direction
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
    
        # Check if the new position is a valid move
        if self.map[new_row][new_col] != '#':
            # Check if there is a box adjacent to the player in the specified direction
            if (new_row, new_col) in self.boxes:
                # Determine the new position of the box based on the direction
                if direction == 'w':
                    new_box_row = new_row - 1
                    new_box_col = new_col
                elif direction == 's':
                    new_box_row = new_row + 1
                    new_box_col = new_col
                elif direction == 'a':
                    new_box_row = new_row
                    new_box_col = new_col - 1
                elif direction == 'd':
                    new_box_row = new_row
                    new_box_col = new_col + 1
    
                # Check if the new position is a valid move for the box
                if self.map[new_box_row][new_box_col] != '#' and (new_box_row, new_box_col) not in self.boxes:
                    # Update the positions of the player and the box
                    self.player_row = new_row
                    self.player_col = new_col
                    self.boxes.remove((new_row, new_col))
                    self.boxes.append((new_box_row, new_box_col))
            else:
                # Update the position of the player
                self.player_row = new_row
                self.player_col = new_col
    
        # Check if the game is won
        return self.check_win()
    