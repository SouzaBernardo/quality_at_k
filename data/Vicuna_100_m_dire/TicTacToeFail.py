class TicTacToe: 
    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symble player, default is 'X'.
        """
        self.board = [[' ' for _ in range(N)] for _ in range(3)]
        self.current_player = 'X'



    def make_move(self, row, col):
        if (row < 0 or row >= 3) or (col < 0 or col >= 3):
            return False
        self.board[row][col] = self.current_player
        self.current_player = 'O'
        return True

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions.
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """
        rows = [0, 1, 2]
        cols = [0, 1, 2]
        rows_cols = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for row in rows:
            for col in cols:
                if self.board[row][col] == 'X':
                    return 'X'
        for row in rows:
            for col in cols:
                if self.board[row][col] == 'O':
                    return 'O'
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
    
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        True
        """
        for row in self.board:
            if not row:
                return True
        return False