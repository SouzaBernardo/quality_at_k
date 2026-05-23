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
        
        minesweeper_map = []
        for i in range(self.n):
            minesweeper_map.append([])
            for j in range(self.n):
                minesweeper_map[i].append(0)
        for i in range(self.k):
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            while minesweeper_map[x][y] == 'X':
                x = random.randint(0, self.n - 1)
                y = random.randint(0, self.n - 1)
            minesweeper_map[x][y] = 'X'
        return minesweeper_map


    def generate_playerMap(self):
        
        player_map = []
        for i in range(self.n):
            player_map.append([])
            for j in range(self.n):
                player_map[i].append('-')
        return player_map


    def check_won(self,map):


    def sweep(self, x, y):