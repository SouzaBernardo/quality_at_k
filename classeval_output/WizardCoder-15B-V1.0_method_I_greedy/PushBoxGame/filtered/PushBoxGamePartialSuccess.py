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
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 'O':
                    self.player_row = i
                    self.player_col = j
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
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
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
            if self.map[self.player_row - 1][self.player_col]!= '#':
                self.player_row -= 1
        elif direction =='s':
            if self.map[self.player_row + 1][self.player_col]!= '#':
                self.player_row += 1
        elif direction == 'a':
            if self.map[self.player_row][self.player_col - 1]!= '#':
                self.player_col -= 1
        elif direction == 'd':
            if self.map[self.player_row][self.player_col + 1]!= '#':
                self.player_col += 1
        # Check if the player has reached a target position
        for target in self.targets:
            if self.player_row == target[0] and self.player_col == target[1]:
                # Move the box to the target position
                box_row, box_col = self.boxes[0]
                self.map[box_row][box_col] =''
                self.boxes[0] = target
                self.map[target[0]][target[1]] = 'X'
                break
        # Check if the player has reached a box
        for i in range(len(self.boxes)):
            if self.player_row == self.boxes[i][0] and self.player_col == self.boxes[i][1]:
                # Swap the two boxes
                box1_row, box1_col = self.boxes[i]
                box2_row, box2_col = self.boxes[1 - i]
                self.boxes[i] = (box2_row, box2_col)
                self.boxes[1 - i] = (box1_row, box1_col)
                break
        # Check if the game is won
        if self.check_win():
            return True
        else:
            return False