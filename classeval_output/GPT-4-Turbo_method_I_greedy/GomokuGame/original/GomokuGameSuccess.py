
class GomokuGame: 
    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        It initializes the board with empty spaces and sets the current player symble as 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'


    def make_move(self, row, col):
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False
        if self.board[row][col] != ' ':
            return False
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True
    def check_winner(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    # check horizontal
                    if col + 4 < self.board_size and all(self.board[row][col+i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col]
                    # check vertical
                    if row + 4 < self.board_size and all(self.board[row+i][col] == self.board[row][col] for i in range(5)):
                        return self.board[row][col]
                    # check diagonal from top left to bottom right
                    if row + 4 < self.board_size and col + 4 < self.board_size and all(self.board[row+i][col+i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col]
                    # check diagonal from bottom left to top right
                    if row - 4 >= 0 and col + 4 < self.board_size and all(self.board[row-i][col+i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col]
        return None
    def _check_five_in_a_row(self, row, col, direction):
        dx, dy = direction
        current_player = self.board[row][col]
        if current_player == ' ':
            return False
        for i in range(5):
            new_row, new_col = row + i * dx, col + i * dy
            if new_row < 0 or new_row >= self.board_size or new_col < 0 or new_col >= self.board_size:
                return False
            if self.board[new_row][new_col] != current_player:
                return False
        return True
