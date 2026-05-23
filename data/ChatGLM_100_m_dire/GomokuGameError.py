class GomokuGame: 
    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        It initializes the board with empty spaces and sets the current player symble as 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'







    def _check_five_in_a_row(self, row, col, direction):
        count = 0
        for i in range(direction):
            if row + i < 0 or row + i >= self.board_size:
                continue
            for j in range(direction):
                if col + j < 0 or col + j >= self.board_size:
                    continue
                count += 1
        return count >= 5