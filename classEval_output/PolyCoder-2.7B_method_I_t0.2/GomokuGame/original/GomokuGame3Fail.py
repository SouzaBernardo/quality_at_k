
class GomokuGame:  
    """
    This class is an implementation of a Gomoku game, supporting for making moves, checking for a winner, and checking if there are five consecutive symbols on the game board.
    """

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
        >>> gomokuGame = GomokuGame(10)
        >>> gomokuGame.make_move(5, 5)
        True
        >>> gomokuGame.make_move(5, 5)
        False
        """
        if self.current_player == 'X':
            return False
        if self.current_player == 'O':
            self.current_player = 'X'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'
            self.board[row][col] = 'O'
            self.board[row][col] = 'X'



