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
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False
    
    def check_winner(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        if self._check_five_in_a_row(row, col, direction):
                            return self.board[row][col]
        return None
    
    def _check_five_in_a_row(self, row, col, direction):
        dx, dy = direction
        count = 0
        symbol = self.board[row][col]
        while 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == symbol:
            count += 1
            row += dx
            col += dy
        return count == 5