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





    def check_winner(self):
        winner = None
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ' ':
                    if self.board[i][j-1] == self.current_player:
                        winner = self.current_player
                    elif self.board[i][j-1] == ' ':
                        for k in range(8):
                            if self.board[i+k][j] == ' ':
                                if self.board[i+k][j-1] == self.current_player:
                                    winner = self.current_player
                                    break
        return winner

    def _check_five_in_a_row(self, row, col, direction):
        count = 0
        for i in range(row, row+direction[0]+1):
            for j in range(col, col+direction[1]+1):
                if self.board[i][j] == self.current_player:
                    count += 1
        if count == 5:
            return True
        return False