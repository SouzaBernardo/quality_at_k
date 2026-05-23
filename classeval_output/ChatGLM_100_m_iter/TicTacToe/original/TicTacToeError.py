
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







    def is_board_full(self):
        for row in range(self.board[0][0], self.board[0][1], 3):
            for col in range(self.board[0][2], self.board[0][3], 3):
                if self.board[row][col] =='':
                    return False
        return True