class TicTacToe: 
    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symble player, default is 'X'.
        """
        self.board = [[' ' for _ in range(N)] for _ in range(3)]
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
        board = self.board
        board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return board


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
        winning_rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        winning_cols = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        winning_diags = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 4, 8], [2, 4, 6]]
        for winning_row in winning_rows:
            for winning_col in winning_cols:
                for winning_diag in winning_diags:
                    winner = ttt.board[winning_row[0]][winning_col[0]] == ttt.board[winning_row[1]][winning_col[1]] == ttt.board[winning_row[2]][winning_col[2]]
                    if winner:
                        return ttt.board[winning_row[0]][winning_col[0]] == ttt.board[winning_row[1]][winning_col[1]] == ttt.board[winning_row[2]][winning_col[2]]
        return None


    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        full = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != ' ':
                    full = False
                    break
        return full