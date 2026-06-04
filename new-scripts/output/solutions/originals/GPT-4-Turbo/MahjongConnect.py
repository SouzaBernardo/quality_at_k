```python
import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = []
            for j in range(self.BOARD_SIZE[1]):
                row.append(random.choice(self.ICONS))
            board.append(row)
        return board

    def is_valid_move(self, pos1, pos2):
        if pos1 == pos2:
            return False
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1]):
            return False
        if not (0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        # This is a placeholder. The actual implementation depends on the rules of the game.
        return True

    def remove_icons(self, pos1, pos2):
        if self.is_valid_move(pos1, pos2):
            self.board[pos1[0]][pos1[1]] = ' '
            self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True
```