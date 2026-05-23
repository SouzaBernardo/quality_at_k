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
        minesweeper_map = []
        for i in range(self.n):
            for j in range(self.n):
                if i == 0 or j == 0:
                    continue
                if i == 0:
                    minesweeper_map.append([i, j, 0])
                else:
                    minesweeper_map.append([i, j, 1])
        return minesweeper_map


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
            for j in range(self.n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    player_map.append([i, j, 'X'])
                if j == 0:
                    player_map.append([i, j, 'Y'])
                if i == self.n - 1 and j == self.n - 1:
                    player_map.append([i, j, 'Z'])
                if i == self.n - 1:
                    player_map.append([i, j, 'W'])
                if j == self.n - 1:
                    player_map.append([i, j, 'U'])
                if i == 0:
                    player_map.append([i, j, 'E'])
                if j == 0:
                    player_map.append([i, j, 'A'])
                if i == self.n - 1:
                    player_map.append([i, j, 'D'])
                if j == self.n - 1:
                    player_map.append([i, j, 'C'])
                if i == 0:
                    player_map.append([i, j, 'B'])
                if j == 0:
                    player_map.append([i, j, 'F'])
                if i == self.n - 1:
                    player_map.append([i, j, 'G'])
                if j == self.n - 1:
                    player_map.append([i, j, 'H'])
                if i == 0:
                    player_map.append([i, j, 'I'])
                if j == 0:
                    player_map.append([i, j, 'J'])
                if i == self.n - 1:
                    player_map.append([i, j, 'K'])
                if j == self.n - 1:
                    player_map.append([i, j, 'L'])
                if i == 0:
                    player_map.append([i, j, 'M'])
                if j == 0:
                    player_map.append([i, j, 'N'])
                if i == self.n - 1:
                    player_map.append([i, j, 'O'])
                if j == self.n - 1:
                    player_map.append([i, j, 'P'])
                if i == 0:
                    player_map.append([i, j, 'Q'])
                if j == 0:
                    player_map.append([i, j, 'R'])
                if i == self.n - 1:
                    player_map.append([i, j, 'S'])
                if j == self.n - 1:
                    player_map.append([i, j, 'T'])
                if i == 0:
                    player_map.append([i

    def check_won(self,map):
        """
        Checks whether the player has won the game,if there are just mines in the player map,return True,otherwise return False.
        :return: True if the player has won the game, False otherwise.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False

        """
        for i in range(self.k):
            if map[i][0] == 1:
                return True
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
        if self.player_map[x][y] == 'X':
            return False
        else:
            self.player_map[x][y] = 'X'
            self.minesweeper_map[x][y] = 'X'
            return True