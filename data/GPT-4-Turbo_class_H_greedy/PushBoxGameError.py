def init_game(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'O':
                    self.player_row, self.player_col = i, j
                elif self.map[i][j] == 'G':
                    self.targets.append((i, j))
                    self.target_count += 1
                elif self.map[i][j] == 'X':
                    self.boxes.append((i, j))

    def check_win(self):
        for box in self.boxes:
            if box not in self.targets:
                return False
        self.is_game_over = True
        return True

    def move(self, direction):
        dx, dy = 0, 0
        if direction == 'w':
            dx, dy = -1, 0
        elif direction == 's':
            dx, dy = 1, 0
        elif direction == 'a':
            dx, dy = 0, -1
        elif direction == 'd':
            dx, dy = 0, 1

        next_row, next_col = self.player_row + dx, self.player_col + dy
        if self.map[next_row][next_col] == '#':
            return False

        if (next_row, next_col) in self.boxes:
            next_box_row, next_box_col = next_row + dx, next_col + dy
            if self.map[next_box_row][next_box_col] == '#' or (next_box_row, next_box_col) in self.boxes:
                return False
            self.boxes.remove((next_row, next_col))
            self.boxes.append((next_box_row, next_box_col))

        self.player_row, self.player_col = next_row, next_col
        return self.check_win()