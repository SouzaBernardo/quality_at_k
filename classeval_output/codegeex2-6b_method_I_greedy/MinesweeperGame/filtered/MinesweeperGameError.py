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
        
        minesweeper_map = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.k):
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            while minesweeper_map[x][y] == 'X':
                x = random.randint(0, self.n - 1)
                y = random.randint(0, self.n - 1)
            minesweeper_map[x][y] = 'X'
        return minesweeper_map

    def generate_playerMap(self):
        
        player_map = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] == 'X':
                    player_map[i][j] = 'X'
                else:
                    player_map[i][j] = self.minesweeper_map[i][j]
        return player_map

    def get_minesweeper_map(self):
        
        return self.minesweeper_map

    def get_player_map(self):
        
        return self.player_map

    def get_score(self):
        
        return self.score

    def set_score(self, score):
        
        self.score = score

    def get_n(self):
        
        return self.n

    def get_k(self):
        
        return self.k

    def get_mine_count(self, x, y):
        
        return self.minesweeper_map[x][y]

    def get_mine_count_around(self, x, y):
        
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if 0 <= i < self.n and 0 <= j < self.n:
                    if self.minesweeper_map[i][j] == 'X':
                        count += 1
        return count

    def is_mine(self, x, y):
        
        return self.minesweeper_map[x][y] == 'X'

    def is_valid_position(self, x, y):


    def generate_playerMap(self):
        
        player_map = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] == 'X':
                    player_map[i][j] = 'X'
                else:
                    player_map[i][j] = self.minesweeper_map[i][j]
        return player_map

    def get_player_map(self):


    def check_won(self,map):
        
        for i in range(self.n):
            for j in range(self.n):
                if self.player_map[i][j] == 'X':
                    continue
                if self.player_map[i][j] == 0:
                    return False
        return True

    def get_score(self):
        
        return self.score

    def set_score(self, score):
        
        self.score = score

    def get_n(self):
        
        return self.n

    def get_k(self):
        
        return self.k

    def get_mine_count(self, x, y):


    def sweep(self, x, y):
        
        if self.is_valid_position(x, y):
            if self.is_mine(x, y):
                self.score -= 1
                return self.player_map
            else:
                self.score += self.get_mine_count_around(x, y)
                self.player_map[x][y] = self.get_mine_count_around(x, y)
                if self.check_won(self.player_map):
                    return self.player_map
                else:
                    return self.player_map
        else:
            return self.player_map