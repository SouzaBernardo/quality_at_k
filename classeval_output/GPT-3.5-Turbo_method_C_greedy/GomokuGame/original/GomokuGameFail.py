
class GomokuGame: 
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
    
        if self.board[row][col] != ' ':
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
        """
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # horizontal, vertical, diagonal (top-left to bottom-right), diagonal (top-right to bottom-left)
    
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    for direction in directions:
                        winner = self._check_five_in_a_row(row, col, direction)
                        if winner:
                            return winner
    
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
        player = self.board[row][col]
        count = 1
        dx, dy = direction
    
        # Check in the positive direction
        x, y = row + dx, col + dy
        while x < self.board_size and y < self.board_size and self.board[x][y] == player:
            count += 1
            x += dx
            y += dy
    
        # Check in the negative direction
        x, y = row - dx, col - dy
        while x >= 0 and y >= 0 and self.board[x][y] == player:
            count += 1
            x -= dx
            y -= dy
    
        return count >= 5