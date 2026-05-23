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
            self.player_row -= 1
        elif direction =='s':
            self.player_row += 1
        elif direction == 'a':
            self.player_col -= 1
        elif direction == 'd':
            self.player_col += 1
        if self.player_row < 0 or self.player_row >= len(self.map) or self.player_col < 0 or self.player_col >= len(self.map[0]):
            self.is_game_over = True
        else:
            if self.map[self.player_row][self.player_col] == 'X':
                self.is_game_over = True
            elif self.map[self.player_row][self.player_col] == 'G':
                self.target_count += 1
                self.targets.append((self.player_row, self.player_col))
                self.boxes.append((self.player_row, self.player_col))
                self.map[self.player_row][self.player_col] = 'O'
                self.player_row, self.player_col = self.get_next_position()
            else:
                self.is_game_over = True

    def get_next_position(self):
        """
        Get the next position of the player based on the current position of the player and the map.
        :return: tuple, the next position of the player.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        >>> game.get_next_position()
        (2, 2)
        >>> game.get_next_position()
        (1, 1)
        >>> game.get_next_position()
        (0, 0)
        """
        if self.player_row == len(self.map) - 1:
            self.player_row = 0
        elif self.player_col == len(self.map[0]) - 1:
            self.player_col = 0
        else:
            self.player_row += 1
            self.player_col += 1
        return self.player_row, self.player_col

    def print_map(self):
        """
        Print the map of the game.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        """
        for row in self.map:
            print(row)


if __name__ == '__main__':
    map = ["#####", "#O  #", "# X #", "#  G#", "#####"]
    game = PushBoxGame(map)
    game.print_map()
    game.move('d')
    game.print_map()
    game.move('s')
    game.print_map()
    game.move('a')
    game.print_map()
    game.move('s')
    game.print_map()
    game.move('d')
    game.print_map()
    game.check_win()
    game.print_map()