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
        # Initialize the map with 0s
        map = [[0 for _ in range(self.n)] for _ in range(self.n)]
    
        # Randomly place the mines
        mines = random.sample(range(self.n * self.n), self.k)
        for mine in mines:
            x, y = divmod(mine, self.n)
            map[x][y] = 'X'
    
            # Update the numbers around the mine
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.n and 0 <= ny < self.n and map[nx][ny] != 'X'):
                        map[nx][ny] += 1
    
        return map
    
    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]
    def check_won(self, map):
        for row in map:
            for cell in row:
                if cell == '-':
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
            return False
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            if self.check_won(self.player_map):
                return True
            else:
                return self.player_map
