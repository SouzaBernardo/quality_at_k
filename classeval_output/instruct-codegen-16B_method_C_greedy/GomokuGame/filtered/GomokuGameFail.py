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
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player (if the current player is 'X', then it becomes 'O' and vice versa).
        :param row: int, the row index of this move
        :param col: int, the column index
        return: True if the move is valid, or False otherwise.
        """
        if self.board[row][col] =='':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False

    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        """
        # check horizontally
        for row in range(self.board_size):
            for col in range(self.board_size - 4):
                if self._check_five_in_a_row(row, col, 'horizontal'):
                    return self.board[row][col]
        # check vertically
        for col in range(self.board_size):
            for row in range(self.board_size - 4):
                if self._check_five_in_a_row(row, col,'vertical'):
                    return self.board[row][col]
        # check diagonally
        for row in range(self.board_size - 4):
            for col in range(self.board_size - 4):
                if self._check_five_in_a_row(row, col, 'diagonal'):
                    return self.board[row][col]
        # no winner
        return None

    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction (horizontal, vertical, diagonal).
        Counts the number of consecutive symbols in that direction starting from the given cell,
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy). Row and col will plus several dx and dy repectively.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        """
        count = 1
        while True:
            if direction == (0, 1):
                if col + count >= self.board_size:
                    break
                if self.board[row][col + count] == self.current_player:
                    count += 1
                else:
                    break
            elif direction == (1, 0):
                if row + count >= self.board_size:
                    break
                if self.board[row + count][col] == self.current_player:
                    count += 1
                else:
                    break
            elif direction == (1, 1):
                if row + count >= self.board_size or col + count >= self.board_size:
                    break
                if self.board[row + count][col + count] == self.current_player:
                    count += 1
                else:
                    break
            elif direction == (1, -1):
                if row - count < 0 or col + count >= self.board_size:
                    break
                if self.board[row - count][col + count] == self.current_player:
                    count += 1
                else:
                    break
            elif direction == (-1, 1):
                if row + count >= self.board_size or col - count < 0:
                    break
                if self.board[row + count][col - count] == self.current_player:
                    count += 1
                else:
                    break
            elif direction == (-1, -1):
                if row - count < 0 or col - count < 0:
                    break
                if self.board[row - count][col - count] == self.current_player:
                    count += 1
                else:
                    break
            else:
                break
        if count >= 5:
            return True
        else:
            return False