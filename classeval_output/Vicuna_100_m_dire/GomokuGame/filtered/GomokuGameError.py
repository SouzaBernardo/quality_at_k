class GomokuGame: 
    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        It initializes the board with empty spaces and sets the current player symble as 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'





    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self._check_five_in_a_row(row, col, 'horizontal'):
                    return 'O'
                elif self._check_five_in_a_row(row, col, 'vertical'):
                    return 'O'
                elif self._check_five_in_a_row(row, col, 'diagonal'):
                    return 'O'
            if self._check_five_in_a_row(row, col, 'horizontal') and self._check_five_in_a_row(row, col, 'vertical'):
                return 'X'
            elif self._check_five_in_a_row(row, col, 'vertical') and self._check_five_in_a_row(row, col, 'diagonal'):
                return 'X'
            elif self._check_five_in_a_row(row, col, 'diagonal') and self._check_five_in_a_row(row, col, 'horizontal'):
                return 'X'
        return None

    def _check_five_in_a_row(self, row, col, direction):
        count = 0
        for r in range(row, row + direction[0] + 1):
            for c in range(col, col + direction[1] + 1):
                if self.board[r][c] == self.current_player:
                    count += 1
        if count == 5:
            return True
        return False