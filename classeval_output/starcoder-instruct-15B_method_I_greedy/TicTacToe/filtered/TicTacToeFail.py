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
        if self.board[row][col]!='':
            return False
    
        self.board[row][col] = self.current_player
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        return True

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]!='':
                return self.board[i][0]
    
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]!='':
                return self.board[0][i]
    
        if self.board[0][0] == self.board[1][1] == self.board[2][2]!='':
            return self.board[0][0]
    
        if self.board[0][2] == self.board[1][1] == self.board[2][0]!='':
            return self.board[0][2]
    
        return None

    def is_board_full(self):
        for row in self.board:
            for col in row:
                if col =='':
                    return False
        return True