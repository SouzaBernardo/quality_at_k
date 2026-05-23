import random
class MinesweeperGame: 
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
                    minesweeper_map[i][j] = self.get_num_mines_around(i, j)
        return minesweeper_map


    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        player_map = [['-' for _ in range(self.n)] for _ in range(self.n)]
        mines = random.sample(range(self.n * self.n), self.k)
        for mine in mines:
            row = mine // self.n
            col = mine % self.n
            player_map[row][col] = 'M'
        return player_map

    def check_won(self, map):
        """
        Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
        :return: True if the player has won the game, False otherwise.
        """
        for row in range(self.n):
            for col in range(self.n):
                if map[row][col] == 'X':
                    return True
        return False

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        """
        # check if the position is a mine
        if self.minesweeper_map[x][y] == 'M':
            self.player_map[x][y] = 'M'
            return True
        # check if the position is a number
        elif self.minesweeper_map[x][y] > 0:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            # recursively sweep all adjacent positions
            if x > 0:
                if self.player_map[x-1][y] == '-':
                    self.sweep(x-1, y)
            if x < self.n-1:
                if self.player_map[x+1][y] == '-':
                    self.sweep(x+1, y)
            if y > 0:
                if self.player_map[x][y-1] == '-':
                    self.sweep(x, y-1)
            if y < self.n-1:
                if self.player_map[x][y+1] == '-':
                    self.sweep(x, y+1)
        return False