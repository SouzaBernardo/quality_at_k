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
        valid_move = False
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            valid_move = False
        else:
            valid_move = True
            if row + col == self.board_size:
                valid_move = False
            if row + col == 0:
                valid_move = False
            if row + col == self.board_size - 1:
                valid_move = False
            if col + row == self.board_size:
                valid_move = False
            if col + row == 0:
                valid_move = False
            if col + row == self.board_size - 1:
                valid_move = False
            if valid_move:
                self.board[row][col] = self.current_player
                if self.current_player == 'X':
                    self.current_player = 'O'
                else:
                    self.current_player = 'X'

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
        winner = None
        for direction in [(0,1), (0,-1), (1,0), (1,-1), (1,1), (-1,1), (-1,-1)]:
            if self._check_five_in_a_row(self.board[row][col], col, direction):
                winner = self.board[row][col]
        return winner

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
        for dx in direction:
            for dy in direction:
                if dx == 0 and dy == 0:
                    continue
                if row + dx >= 0 and row + dx < self.board_size and col + dy >= 0 and col + dy < self.board_size:
                    if self.board[row + dx][col + dy] == self.board[row][col]:
                        count += 1
        return count == 5