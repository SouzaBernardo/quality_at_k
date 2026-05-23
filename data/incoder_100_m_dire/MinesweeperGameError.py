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
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_mine_sweeper_map()
        [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

        """
        map = []
        for i in range(0, self.n):
            map.append([])
            for j in range(0, self.n):
                map[i].append(0)
        return map


    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_playerMap()
        [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

        """
        player_map = []
        for i in range(self.n):
            player_map.append(['-' for j in range(self.n)])
        return player_map


    def check_won(self):
        """
        Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
        :return: True if the player has won the game, False otherwise.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False

        """
        count = 0
        for row in self.player_map:
            for cell in row:
                if cell == '-':
                    count += 1
        if count == self.k:
            return True
        else:
            return False


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
        player_map = self.player_map
        player_map[x][y] = 'X'
        player_map[x][y+1] = 'X'
        player_map[x][y+2] = 'X'
        player_map[x+1][y] = 'X'
        player_map[x+1][y+1] = 'X'
        player_map[x+1][y+2] = 'X'
        player_map[x+2][y] = 'X'
        player_map[x+2][y+1] = 'X'
        player_map[x+2][y+2] = 'X'
        player_map[x][y] = '-'
        player_map[x][y+1] = '-'
        player_map[x][y+2] = '-'
        player_map[x+1][y] = '-'
        player_map[x+1][y+1] = '-'
        player_map[x+1][y+2] = '-'
        player_map[x+2][y] = '-'
        player_map[x+2][y+1] = '-'
        player_map[x+2][y+2] = '-'
        player_map[x][y] = '-'
        player_map[x][y+1] = '-'
        player_map[x][y+2] = '-'
        player_map[x+1][y] = '-'
        player_map[x+1][y+1] = '-'
        player_map[x+1][y+2] = '-'
        player_map[x+2][y] = '-'
        player_map[x+2][y+1] = '-'
        player_map[x+2][y+2] = '-'
        return player_map