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
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player (if the current player is 'X', then it becomes 'O' and vice versa).
        :param row: int, the row index of this move
        :param col: int, the column index
        return: True if the move is valid, or False otherwise.
        """
        if not (0 <= row < self.board_size and 0 <= col < self.board_size):
            return False
        if self.board[row][col]!='':
            return False
        self.board[row][col] = self.current_player
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        return True

    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        """
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] =='':
                    continue
                if self._check_five_in_a_row(row, col, (0, 1)):
                    return self.board[row][col]
                if self._check_five_in_a_row(row, col, (1, 0)):
                    return self.board[row][col]
                if self._check_five_in_a_row(row, col, (1, 1)):
                    return self.board[row][col]
                if self._check_five_in_a_row(row, col, (1, -1)):
                    return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        if not (0 <= row < self.board_size and 0 <= col < self.board_size):
            return False
        if direction[0] not in [-1, 1] or direction[1] not in [-1, 1]:
            return False
        count = 1
        for i in range(1, 6):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            if not (0 <= new_row < self.board_size and 0 <= new_col < self.board_size):
                break
            if self.board[new_row][new_col]!= self.board[row][col]:
                count = 1
            else:
                count += 1
                if count == 5:
                    return True
        return False