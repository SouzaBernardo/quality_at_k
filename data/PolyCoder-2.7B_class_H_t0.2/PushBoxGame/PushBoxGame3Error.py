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
            self.is_game_over = True
            return False
        elif direction == 'd':
            self.is_game_over = False
            return False
        else:
            return False

    def print_map(self):
        """
        Print the map to the screen.
        :return:
        """
        print(self.map)

    def print_player_row(self, row):
        """
        Print the player's row to the screen.
        :param row: int, the row of the player's box.
        :return:
        """
        print(str(row))

    def print_player_col(self, col):
        """
        Print the player's column to the screen.
        :param col: int, the column of the player's box.
        :return:
        """
        print(str(col))

    def print_boxes(self, boxes):
        """
        Print the boxes to the screen.
        :param boxes: list[tuple], the boxes to print.
        :return:
        """
        for box in boxes:
            print(str(box))

    def print_target_count(self, target_count):
        """
        Print the target count to the screen.
        :param target_count: int, the target count of the player.
        :return:
        """
        print(str(target_count))

    def print_player_count(self, player_count):
        """
        Print the player count to the screen.
        :param player_count: int, the player count of the player.
        :return:
        """
        print(str(player_count))

    def print_player_name(self, player_name):
        """
        Print the player's name to the screen.
        :param player_name: str, the player's name.