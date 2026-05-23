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
        if self.board[row][col] =='':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
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
        # check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current_player:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current_player:
                return self.board[0][i]
        # check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current_player:
                return self.board[0][i]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current_player:
                return self.board[0][i]
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return self.board[0][2]
        return None


    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        for row in self.board:
            if row.count(' ')!= 3:
                return False
        return True