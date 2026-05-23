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
        if row < 0 or row >= self.board_size:
            return False
        if col < 0 or col >= self.board_size:
            return False
        
        if self.board[row][col] =='':
            self.current_player = None
            return True
        
        self.board[row][col] = self.current_player
        self.current_player = other_player
        
        return True

    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        """
        if not self.board:
            return None
        
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] =='':
                    continue
                
                if row < 0 or row >= self.board_size:
                    return None
                if col < 0 or col >= self.board_size:
                    return None
                
                if self.board[row][col] == self.current_player:
                    if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] == self.board[row][col + 4] =='':
                        return 'X'
                    elif self.board[row][col] == self.board[row][col - 1] == self.board[row][col - 2] == self.board[row][col - 3] == self.board[row][col - 4] =='':
                        return 'O'
                    else:
                        return None
        
        return None

    def _check_five_in_a_row(self, row, col, direction):
        count = 0
        for i in range(direction):
            if row + i < 0 or row + i >= self.board_size:
                return False
            if col + i < 0 or col + i >= self.board_size:
                return False
            if self.board[row + i][col + i] == self.current_player:
                if count == 5:
                    return True
                count += 1
        return False