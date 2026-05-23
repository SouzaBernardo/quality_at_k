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
        minesweeper_map = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append(0)
            minesweeper_map.append(row)
        for i in range(self.k):
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            while minesweeper_map[x][y] == 'X':
                x = random.randint(0, self.n - 1)
                y = random.randint(0, self.n - 1)
            minesweeper_map[x][y] = 'X'
            for i in range(max(0, x - 1), min(self.n, x + 2)):
                for j in range(max(0, y - 1), min(self.n, y + 2)):
                    if i!= x or j!= y:
                        minesweeper_map[i][j] += 1
        return minesweeper_map

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        player_map = [['-' for i in range(self.n)] for j in range(self.n)]
        return player_map

    def check_won(self, player_map):
        """
        Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
        :return: True if the player has won the game, False otherwise.
        """
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] == 'X' and player_map[i][j]!= 'X':
                    return False
        return True

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return False
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            if self.minesweeper_map[x][y] == 0:
                for i in range(max(0, x-1), min(self.n, x+2)):
                    for j in range(max(0, y-1), min(self.n, y+2)):
                        if self.player_map[i][j] == '-':
                            self.sweep(i, j)
            return self.check_won(self.player_map)