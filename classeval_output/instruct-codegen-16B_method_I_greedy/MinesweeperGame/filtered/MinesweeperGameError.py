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
        Generates a minesweeper map with the given size of the board and the number of mines,the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'X' represents the mine,other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        """
        minesweeper_map = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.k):
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            minesweeper_map[x][y] = 'X'
        for i in range(self.n):
            for j in range(self.n):
                if minesweeper_map[i][j]!= 'X':
                    minesweeper_map[i][j] = self.get_num_mines_around(i, j, minesweeper_map)
        return minesweeper_map



    def get_num_mines_around(self, x, y, minesweeper_map):
        """
        Gets the number of mines around the given position.
        :param x: The x-coordinate of the position, int.
        :param y: The y-coordinate of the position, int.
        :param minesweeper_map: The minesweeper map, list.
        :return: The number of mines around the position, int.
        """
        num_mines = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.n and 0 <= y + j < self.n and minesweeper_map[x + i][y + j] == 'X':
                    num_mines += 1
        return num_mines

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        player_map = [['-' for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] == 'X':
                    player_map[i][j] = 'X'
        return player_map

    def check_won(self,map):
        """
        Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
        :return: True if the player has won the game, False otherwise.
        """
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] == 'X':
                    return True
        return False