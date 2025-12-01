# players.py

class HumanPlayer:
    def __init__(self, piece):
        self.piece = piece  # 1=红, 2=黄

    def get_move(self, event, game):
        """ 人类玩家逻辑由 UI 在 connect4.py 内处理 """
        pass


class AIPlayer:
    def __init__(self, piece):
        self.piece = piece

    def get_move(self, board):
        """
        暂时写一个最简单的 AI：
        找到第一个能落子的位置。
        后续可以扩展 Minimax / Monte Carlo / RL 都可以。
        """
        import random
        valid_cols = [c for c in range(board.shape[1]) if board[-1][c] == 0]
        return random.choice(valid_cols)


