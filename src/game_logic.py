# game_logic.py

import numpy as np
from config import ROW, COL

class Connect4Game:
    def __init__(self):
        self.board = np.zeros((ROW, COL), dtype=int)

    def reset(self):
        self.board = np.zeros((ROW, COL), dtype=int)

    def is_valid(self, col):
        return self.board[ROW - 1][col] == 0

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def get_next_row(self, col):
        for r in range(ROW):
            if self.board[r][col] == 0:
                return r

    def check_win(self, piece):
        # 横向
        for c in range(COL - 3):
            for r in range(ROW):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return True

        # 纵向
        for c in range(COL):
            for r in range(ROW - 3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return True

        # 正斜线
        for c in range(COL - 3):
            for r in range(ROW - 3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return True

        # 反斜线
        for c in range(COL - 3):
            for r in range(3, ROW):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return True

        return False
