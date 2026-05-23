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
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
            return True
        else:
            return False
    

    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # horizontal, vertical, diagonal (top-left to bottom-right), diagonal (top-right to bottom-left)
    
        for row in range(self.board_size):
            for col in range(self.board_size):
                symbol = self.board[row][col]
                if symbol != ' ':
                    for direction in directions:
                        dx, dy = direction
                        consecutive_count = 1
    
                        # Check for consecutive symbols in the current direction
                        for i in range(1, 5):
                            new_row = row + dx * i
                            new_col = col + dy * i
    
                            # Check if the new position is within the board boundaries
                            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                                if self.board[new_row][new_col] == symbol:
                                    consecutive_count += 1
                                else:
                                    break
                            else:
                                break
    
                        # If there are five consecutive symbols, return the symbol of the winning player
                        if consecutive_count == 5:
                            return symbol
    
        # If no winning player is found, return None
        return None
    

    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction (horizontal, vertical, diagonal).
        Counts the number of consecutive symbols in that direction starting from the given cell.
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy). Row and col will plus several dx and dy respectively.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        """
        dx, dy = direction
        symbol = self.board[row][col]
        consecutive_count = 1
    
        # Check for consecutive symbols in the given direction
        for i in range(1, 5):
            new_row = row + dx * i
            new_col = col + dy * i
    
            # Check if the new position is within the board boundaries
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                if self.board[new_row][new_col] == symbol:
                    consecutive_count += 1
                else:
                    break
            else:
                break
    
        # If there are five consecutive symbols, return True
        if consecutive_count == 5:
            return True
    
        return False