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
        Generates a minesweeper map with the given size of the board and the number of mines.
        'X' represents the mine, and other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        """
        minesweeper_map = [['0' for _ in range(self.n)] for _ in range(self.n)]
        mine_positions = random.sample(range(self.n * self.n), self.k)
        
        for position in mine_positions:
            row = position // self.n
            col = position % self.n
            minesweeper_map[row][col] = 'X'
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    new_row = row + i
                    new_col = col + j
                    if 0 <= new_row < self.n and 0 <= new_col < self.n and minesweeper_map[new_row][new_col] != 'X':
                        minesweeper_map[new_row][new_col] = str(int(minesweeper_map[new_row][new_col]) + 1)
        
        return minesweeper_map
    

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board.
        '-' represents the unknown position.
        :return: The player map, list.
        """
        player_map = [['-' for _ in range(self.n)] for _ in range(self.n)]
        return player_map
    

    def check_won(self, map):
        """
        Checks whether the player has won the game. If there are only mines in the player map, return True. Otherwise, return False.
        :param map: The player map, list.
        :return: True if the player has won the game, False otherwise.
        """
        for row in map:
            for cell in row:
                if cell != 'X':
                    return False
        return True
    

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise. If the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return False
    
        self.player_map[x][y] = self.minesweeper_map[x][y]
    
        if self.check_won(self.player_map):
            return True
    
        return self.player_map
    