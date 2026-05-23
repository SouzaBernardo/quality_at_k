Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class TicTacToe in the following code.
class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symble player, default is 'X'.
        """
        self.board = [[''for _ in range(N)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
       ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """

### Response:class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symble player, default is 'X'.
        """
        self.board = [[''for _ in range(N)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return False
        if self.board[row][col]!='':
            return False
        self.board[row][col] = self.current_player
        if self.check_winner():
            return True
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return False

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
       ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """
        for direction in [self.check_rows, self.check_columns, self.check_diagonals]:
            winner = direction()
            if winner:
                return winner
        return None

    def check_rows(self):
        """
        Check if there is a winner in rows
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner in rows
        """
        for row in self.board:
            if 'X' in row and 'O' in row:
                return None
        for row in self.board:
            if row.count('X') == len(row):
                return 'X'
            if row.count('O') == len(row):
                return 'O'
        return None

    def check_columns(self):
        """
        Check if there is a winner in columns
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner in columns
        """
        for col in range(len(self.board[0])):
            if 'X' in [self.board[row][col] for row in range(len(self.board))]:
                if 'O' in [self.board[row][col] for row in range(len(self.board))]:
                    return None
        for col in range(len(self.board[0])):
            if self.board[0][col] == 'X' and self.board[1][col] == 'X' and self.board[2][col] == 'X':
                return 'X'
            if self.board[0][col] == 'O' and self.board[1][col] == 'O' and self.board[2][col] == 'O':
                return 'O'
        return None

    def check_diagonals(self):
        """
        Check if there is a winner in diagonals
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner in diagonals
        """
        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            return 'X'
        if self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            return 'O'
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        for row in self.board:
            if'' in row:
                return False
        return True

# Test the class
ttt = TicTacToe()
print(ttt.is_board_full())