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
                    minesweeper_map.append([i, j, 0])
                    minesweeper_map.append([i, j, 1])
                    minesweeper_map.append([i, j, 2])
                    minesweeper_map.append([i, j, 3])
                    minesweeper_map.append([i, j, 4])
                    minesweeper_map.append([i, j, 5])
                    minesweeper_map.append([i, j, 6])
                    minesweeper_map.append([i, j, 7])
                    minesweeper_map.append([i, j, 8])
                    minesweeper_map.append([i, j, 9])
                    minesweeper_map.append([i, j, 10])
                    minesweeper_map.append([i, j, 11])
                    minesweeper_map.append([i, j, 12])
                    minesweeper_map.append([i, j, 13])
                    minesweeper_map.append([i, j, 14])
                    minesweeper_map.append([i, j, 15])
                    minesweeper_map.append([i, j, 16])
                    minesweeper_map.append([i, j, 17])
                    minesweeper_map.append([i, j, 18])
                    minesweeper_map.append([i, j, 19])
                    minesweeper_map.append([i, j, 20])
                    minesweeper_map.append([i, j, 21])
                    minesweeper_map.append([i, j, 22])
                    minesweeper_map.append([i, j, 23])
                    minesweeper_map.append([i, j, 24])
                    minesweeper_map.append([i, j, 25])
                    minesweeper_map.append([i, j, 26])
                    minesweeper_map.append([i, j, 27])
                    minesweeper_map.append([i, j, 28])
                    minesweeper_map.append([i, j, 29])
                    minesweeper_map.append([i, j, 30])
                    minesweeper_map.append([i, j, 31])
                    minesweeper_map.append([i, j, 32])
                    minesweeper_map.append([i, j, 33])
                    minesweeper_map.append([i, j, 34])
                    minesweeper_map.append([i, j, 35])
                    minesweeper_map.append([i, j, 36])
                    minesweeper_map.append([i, j, 37])
                    minesweeper_map.append([i, j, 38])
                    minesweeper_map.append([i, j, 39])
                    minesweeper_map.append([i, j, 40])
                    minesweeper_map.append([