import random

class MinesweeperGame:
    def __init__(self, n, k) -> None:
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0

    def generate_mine_sweeper_map(self):
        map = [['0' for _ in range(self.n)] for _ in range(self.n)]
        mines = random.sample(range(self.n*self.n), self.k)
        for mine in mines:
            x, y = divmod(mine, self.n)
            map[x][y] = 'X'
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.n and 0 <= ny < self.n and map[nx][ny] != 'X'):
                        map[nx][ny] = str(int(map[nx][ny]) + 1)
        return map

    def generate_playerMap(self):
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self,map):
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x, y):
        if self.minesweeper_map[x][y] == 'X':
            return False
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            if self.check_won(self.player_map):
                return True
            else:
                return self.player_map