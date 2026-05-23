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





    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        player_map = [['-' for j in range(self.n)] for i in range(self.n)]
        return player_map

    def check_won(self, player_map):
        """
        Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
        :return: True if the player has won the game, False otherwise.
        """
        num_mines = 0
        for i in range(self.n):
            for j in range(self.n):
                if player_map[i][j] == 'X':
                    num_mines += 1
        if num_mines == self.k:
            return True
        else:
            return False

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        """
        if self.player_map[x][y]!= '-':
            return self.player_map
        if self.minesweeper_map[x][y] == 'X':
            for i in range(self.n):
                for j in range(self.n):
                    if self.minesweeper_map[i][j] == 'X':
                        self.player_map[i][j] = 'X'
            return True
        self.player_map[x][y] = self.minesweeper_map[x][y]
        if self.check_won(self.player_map):
            return True
        return self.player_map