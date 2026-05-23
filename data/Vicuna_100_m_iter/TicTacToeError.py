class TicTacToe:  
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

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
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'

    def is_board_full(self):
        """
        :return: bool, indicating whether the game board is full or not
        """
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False
        return True