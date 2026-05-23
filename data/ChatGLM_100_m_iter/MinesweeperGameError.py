import random
class MinesweeperGame:  
    """
    This is a class that implements mine sweeping games including minesweeping and winning judgment.
    """

    def __init__(self, n, k) -> None:
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        :param n: The size of the board, int.
        :param k: The number of mines, int.
        """
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0



    def generate_mine_sweeper_map(self):
        """
        Generates a minesweeper map with the given size of the board and the number of mines,
        the given parameter n is the size of the board, the size of the board is n*n,
        the parameter k is the number of mines,'X' represents the mine,other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        """
        # Generate the mine map
        mine_map = [[random.choice(['X', 'O']) for i in range(n)] for j in range(n)]
        # Add the player's position
        player_map = [[self.player_map[i][j] for i in range(n)] for j in range(n)]
        # Add the score
        score_map = [[self.score for i in range(n)] for j in range(n)]
        # Add the mines
        mines_map = [['X' for i in range(n)] for j in range(n)]
        # Join the mine map and player map
        mines_map = [[mine_map[i][j] for i in range(n)] for j in range(n)]
        player_map = [[player_map[i][j] for i in range(n)] for j in range(n)]
        # Join the score map and mine map
        score_map = [[score_map[i][j] for i in range(n)] for j in range(n)]
        # Return the minesweeper map
        return mine_map, player_map, score_map

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        # Generate the mine map
        mine_map = [[random.choice(['X', 'O']) for i in range(n)] for j in range(n)]
        # Add the player's position
        player_map = [[self.player_map[i][j] for i in range(n)] for j in range(n)]
        # Add the score
        score_map = [[self.score for i in range(n)] for j in range(n)]
        # Add the mines
        mines_map = [['X' for i in range(n)] for j in range(n)]
        # Join the mine map and player map
        mines_map = [[mine_map[i][j] for i in range(n)] for j in range(n)]
        player_map = [[player_map[i][j] for i in range(n)] for j in range(n)]
        # Join the score map and mine map
        score_map = [[score_map[i][j] for i in range(n)] for j in range(n)]
        # Return the player map
        return mine_map, player_map, score_map

    def check_won(self):

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise, if the game still continues, return the player map, list.
        """
        # Check if the player has won the game
        if self.check_won():
            # If the player has won, return the player map, list
            return self.player_map, self.score_map
        # If the game is still ongoing, return the mine map, list
        else:
            # Generate the mine map
            mine_map = [[random.choice(['X', 'O']) for i in range(n)] for j in range(n)]
            # Add the player's position
            player_map = [[self.player_map[i][j] for i in range(n)] for j in range(n)]
            # Add the score
            score_map = [[self.score for i in range(n)] for j in range(n)]
            # Add the mines
            mines_map = [['X' for i in range(n)] for j in range(n)]
            # Join the mine map and player map
            mines_map = [[mine_map[i][j] for i in range(n)] for j in range(n)]
            player_map = [[player_map[i][j] for i in range(n)] for j in range(n)]
            # Join the score map and mine map
            score_map = [[score_map[i][j] for i in range(n)] for j in range(n)]
            # Return the player map
            return mine_map, player_map, score_map