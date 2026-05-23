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
        Generates a minesweeper map with the given size of the board and the number of mines,
        the given parameter n is the size of the board, the size of the board is n*n,
        the parameter k is the number of mines,'X' represents the mine,other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        """
        # Generate the mine map
        mine_map = [[random.choice(['X', 'O']) for i in range(n)] for j in range(n)]
        # Add the number of mines around the position
        mine_map[0][0] = 1
        for i in range(1, n):
            for j in range(i):
                mine_map[i][j] = min(min(mine_map[i-1][j], mine_map[i][j-1], mine_map[i-1][j-1]), mine_map[i-1][j+1], mine_map[i][j+1])
        # Return the mine map
        return mine_map

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        # Generate a random number of mines for each player
        mines = random.randint(1, self.k)
        
        # Create a list to store the player's positions
        player_map = [['-' for i in range(n)] for j in range(n)]
        
        # Loop through each player and add their position to the player map
        for i in range(n):
            for j in range(n):
                if i == j:
                    player_map[i][j] = '-'
                else:
                    player_map[i][j] = random.choice(['-', 'M'])
        
        return player_map

    def check_won(self):
        """
        Checks whether the player has won the game.
        :return: True if the player has won the game, False otherwise.
        """
        if len(self.player_map) == 0:
            return True
        for i in range(self.n):
            for j in range(self.n):
                if self.player_map[i][j] == 'X':
                    self.score += 1
                    return True
        return False


    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise, if the game still continues, return the player map, list.
        
        Example:
            >>> minesweeper_game = MinesweeperGame(3, 1)
            >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
            >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            >>> minesweeper_game.sweep(1, 1)
            [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]
        """
        if x < 0 or x >= self.n or y < 0 or y >= self.k:
            return False
        if self.check_won():
            return True
        self.player_map[y][x] = 'X'
        return False