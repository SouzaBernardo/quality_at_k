
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
        
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False


    def check_winner(self):
        
        for row in self.board:
            if all(mark == row[0] for mark in row):
                return row[0]
        for col in range(3):
            if all(self.board[row][col] == self.board[0][col] for row in range(3)):
                return self.board[0][col]
        if all(self.board[i][i] == self.board[0][0] for i in range(3)):
            return self.board[0][0]
        if all(self.board[i][2 - i] == self.board[0][0] for i in range(3)):
            return self.board[0][0]
        return 'T'


    def is_board_full(self):
        
        return all(mark != ' ' for row in self.board for mark in row)


    def check_winner(self):
        

        for row in self.board:
            if all(mark == row[0] for mark in row):
                return row[0]
        for col in range(3):
            if all(self.board[row][col] == self.board[0][col] for row in range(3)):
                return self.board[0][col]
        if all(self.board[i][i] == self.board[0][0] for i in range(3)):
            return self.board[0][0]
        if all(self.board[i][2 - i] == self.board[0][0] for i in range(3)):
            return self.board[0][0]
        return 'T'


    def is_board_full(self):
