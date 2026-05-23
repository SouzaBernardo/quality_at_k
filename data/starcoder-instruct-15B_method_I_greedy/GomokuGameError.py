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
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
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
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
       ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """

    def _check_five_in_a_row(self, row, col, direction):
        count = 1
        dx, dy = direction
        while row + dx < self.board_size and col + dy < self.board_size and self.board[row + dx][col + dy] == self.current_player:
            count += 1
            row += dx
            col += dy
        return count == 5