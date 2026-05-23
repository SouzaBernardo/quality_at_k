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
        # Initialize the map with zeros
        mine_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        # Randomly place the mines
        mines = random.sample(range(self.n * self.n), self.k)
        for mine in mines:
            row, col = divmod(mine, self.n)
            mine_map[row][col] = 'X'
            
            # Update the numbers around the mine
            for i in range(max(0, row - 1), min(self.n, row + 2)):
                for j in range(max(0, col - 1), min(self.n, col + 2)):
                    if mine_map[i][j] != 'X':
                        mine_map[i][j] += 1
                        
        return mine_map
    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        player_map = [['-' for _ in range(self.n)] for _ in range(self.n)]
        return player_map
    def check_won(self, map):
        for i in range(self.n):
            for j in range(self.n):
                # If there is a position in the player map that is not a mine in the minesweeper map and is still unknown in the player map, return False
                if self.minesweeper_map[i][j] != 'X' and map[i][j] == '-':
                    return False
        return True
    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.sweep(1, 1)
        [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]

        """
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return False, self.player_map
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            if self.check_won(self.player_map):
                return True, self.player_map
            else:
                return False, self.player_map