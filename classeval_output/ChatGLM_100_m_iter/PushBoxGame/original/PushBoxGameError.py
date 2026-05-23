
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
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False
        self.game_over = False
        for i in range(len(self.map)):
            row = self.map[i]
            col = self.map[i]
            if self.is_game_over:
                self.is_game_over = False
                break
            if row == "#" and col == "O":
                self.player_row = i
                self.player_col = i
            elif row == "#" and col == "X":
                self.player_row = i
                self.player_col = j
            elif row == "#" and col == "G":
                self.targets.append((i, j))
                self.boxes.append((i, j))
                self.target_count += 1
                self.is_game_over = True
            else:
                if row == col:
                    self.game_over = True
                    break
        if self.is_game_over:
            self.game_over = False

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
        if len(self.targets) == len(self.boxes):
            self.is_game_over = True
        for i in range(len(self.targets)):
            for j in range(len(self.boxes)):
                if self.targets[i][j]!= self.boxes[i][j]:
                    self.is_game_over = False
                    break
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w','s', 'a', or 'd' representing up, down, left, or right respectively.

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
        if direction == 'w' or direction =='s' or direction == 'a' or direction == 'd':
            self.player_row = int(direction)
            self.player_col = int(direction)
        else:
            if self.player_row == 0 and self.player_col == 0:
                self.player_row = 1
                self.player_col = 1
            elif self.player_row == 0 and self.player_col == 1:
                self.player_row = 2
                self.player_col = 1
            elif self.player_row == 1 and self.player_col == 0:
                self.player_row = 3
                self.player_col = 0
            elif self.player_row == 1 and self.player_col == 1:
                self.player_row = 4
                self.player_col = 0
            else:
                if self.player_row == 0 and self.player_col == 1:
                    self.player_col = 2
                    self.player_row = 3
                elif self.player_row == 0 and self.player_col == 2:
                    self.player_col = 4
                    self.player_row = 3
                elif self.player_row == 1 and self.player_col == 0:
                    self.player_col = 5
                    self.player_row = 2
                elif self.player_row == 1 and self.player_col == 2:
                    self.player_col = 6
                    self.player_row = 2
                else:
                    if self.player_row == 0 and self.player_col == 2:
                        self.player_col = 4
                        self.player_row = 3
                    elif self.player_row == 0 and self.player_col == 3:
                        self.player_col = 5
                        self.player_row = 1
                    elif self.player_row == 1 and self.player_col == 0:
                        self.player_col = 6
                        self.player_row = 1
                    elif self.player_row == 1 and self.player_col == 1:
                        self.player_col = 7
                        self.player_row = 0
                    else:
                        if self.player_row == 0 and self.player_col == 3:
                            self.player_col = 6
                            self.player_row = 2
                        elif self.player_row == 0 and self.player_col == 4:
                            self.player_col = 7
                            self.player_row = 2
                        elif self.player_row == 1 and self.player_col == 0:
                            self.player_col = 8
                            self.player_row