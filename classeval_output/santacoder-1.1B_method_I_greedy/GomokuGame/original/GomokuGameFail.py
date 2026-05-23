
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
        if self.board[row][col]!='':
            return False
        self.board[row][col] = self.current_player
        self.current_player = self.current_player == 'X' and 'O' or 'X'
        return True



    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
       ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """
        for row in range(self.board_size):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
                return self.current_player
            if self.board[0][row] == self.board[1][row] == self.board[2][row] == self.current_player:
                return self.current_player
        for col in range(self.board_size):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
                return self.current_player
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
                return self.current_player
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return self.current_player
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return self.current_player
        return None




    def _check_five_in_a_row(self, row, col, direction):
        """
        checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction (horizontal, vertical, diagonal).
        Counts the number of consecutive symbols in that direction starting from the given cell,
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy). Row and col will plus several dx and dy repectively.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
       ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame._check_five_in_a_row(5, 1, (0, 1))
        True
        >>> gomokuGame._check_five_in_a_row(5, 1, (1, 1))
        False
        """
        count = 0
        for i in range(self.board_size):
            if self.board[row+i][col+i] == self.current_player:
                count += 1
            if count == 5:
                return True
        return False



