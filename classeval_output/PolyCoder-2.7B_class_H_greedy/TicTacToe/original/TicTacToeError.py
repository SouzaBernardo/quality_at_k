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

    def is_board_empty(self):
        """
        Check if the game board is empty.
        :return: bool, indicating whether the game board is empty or not
        >>> ttt.is_board_empty()
        True
        """

    def is_board_full_and_empty(self):
        """
        Check if the game board is completely filled and empty.
        :return: bool, indicating whether the game board is full and empty or not
        >>> ttt.is_board_full_and_empty()
        True
        """

    def is_board_full_and_empty_and_winner(self):
        """
        Check if the game board is completely filled and empty and the winner is 'X'.
        :return: bool, indicating whether the game board is full and empty and the winner is 'X' or not
        >>> ttt.is_board_full_and_empty_and_winner()
        True
        """

    def is_board_empty_and_winner(self):
        """
        Check if the game board is empty and the winner is 'O'.
        :return: bool, indicating whether the game board is empty and the winner is 'O' or not
        >>> ttt.is_board_empty_and_winner()
        True
        """

    def is_board_full_and_winner(self):
        """
        Check if the game board is completely filled and the winner is 'O'.
        :return: bool, indicating whether the game board is full and the winner is 'O' or not
        >>> ttt.is_board_full_and_winner()
        True
        """

    def is_board_empty_and_winner(self):
        """
        Check if the game board is empty and the winner is 'X'.
        :return: bool, indicating whether the game board is empty and the winner is 'X' or not
        >>> ttt.is_board_empty_and_winner()
        True
        """

    def is_board_full_and_winner_and_empty(self):
        """
        Check if the game board is completely filled and the winner is 'O' and the empty is 'X'.
        :return: bool, indicating whether the game board is full and the winner is 'O' and the empty is 'X' or not
        >>> ttt.is_board_full_and_winner_and_empty()
        True
        """

    def is_board_empty_and_winner_and_empty(self):
        """
        Check if the game board is empty and the winner is 'O' and the empty is 'X'.
        :return: bool, indicating whether the game board is empty and the winner is 'O' and the empty is 'X' or not
        >>> ttt.is_board_empty_and_winner_and_empty()
        True
        """

    def is_board_full_and_winner_and_empty(self):
        """
        Check if the game board is completely filled and the winner is 'O' and the empty is 'X'.
        :return: bool, indicating whether the game board is full and the winner is 'O' and the empty is 'X' or not
        >>> ttt.is_board_full_and_winner_and_empty()
        True
        """

    def is_board_empty_and_winner_and_empty(self):
        """
        Check if the game board is empty and the winner is 'X' and the empty is 'O'.
        :return: bool, indicating whether the game board is empty and the winner is 'X' and the empty is 'O' or not
        >>> ttt.is_board_empty_and_winner_and_empty()
        True
        """

    def is_board_full_and_winner_and_empty(self):
        """
        Check if the game board is completely filled and the winner is 'O' and the empty is 'X'.
        :return: bool, indicating whether the game board is full and the winner is 'O' and the empty is 'X' or not
        >>> ttt.is_board_full