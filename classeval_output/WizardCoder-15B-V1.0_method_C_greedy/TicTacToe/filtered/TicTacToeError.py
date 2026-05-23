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
        """
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
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        # check rows
        for row in self.board:
            if self._is_winning_row(row):
                return self.current_player
        # check columns
        for col in range(len(self.board[0])):
            if self._is_winning_col(col):
                return self.current_player
        # check diagonals
        if self._is_winning_diagonal():
            return self.current_player
        if self._is_winning_diagonal(True):
            return self.current_player
        # check if board is full
        if not any(''in row for row in self.board):
            return 'Tie'
        # no winner yet
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        for row in self.board:
            for elem in row:
                if elem =='':
                    return False
        return True