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

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """


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

        if direction == 'w':
            self.is_game_over = True
            return True
        elif direction =='s':
            self.is_game_over = False
            return True
        elif direction == 'a':
            self.is_game_over = False
            return True
        elif direction == 'd':
            self.is_game_over = True
            return True
        else:
            return False

    def print_map(self):
        """
        Print the map of the game.
        :return:
        """
        print(self.map)

    def get_player_row(self):
        """
        Get the row of the player.
        :return: int, the row of the player.
        """
        return self.player_row

    def get_player_col(self):
        """
        Get the column of the player.
        :return: int, the column of the player.
        """
        return self.player_col

    def get_boxes(self):
        """
        Get the boxes of the game.
        :return: list[tuple], the boxes of the game.
        """
        return self.boxes

    def get_target_count(self):
        """
        Get the number of targets of the game.
        :return: int, the number of targets of the game.
        """
        return self.target_count

    def get_player_row_and_col(self):
        """
        Get the row and column of the player.
        :return: (int, int), the row and column of the player.
        """
        return self.player_row, self.player_col

    def get_player_row_and_col_and_direction(self):
        """
        Get the row and column of the player.
        :return: (int, int, str), the row and column of the player.
        """
        return self.player_row, self.player_col, self.direction

    def get_player_row_and_col_and_direction_and_direction(self):
        """
        Get the row and column of the player.