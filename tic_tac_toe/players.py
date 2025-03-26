from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, marker):
        self.marker = marker
    
    @abstractmethod
    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, marker):
        super().__init__(marker)
    
    def get_move(self, board):
        # Human moves will be provided via GUI button clicks.
        return None

class AIPlayer(Player):
    def __init__(self, marker):
        super().__init__(marker)
        # Assume opponent's marker is the opposite.
        self.opponent_marker = 'O' if marker == 'X' else 'X'
        self.algorithm = "Minimax"

    def get_move(self, board):
        best_score = -float('inf')
        best_move = None
        for move in board.available_moves():
            row, col = move
            board.board[row][col] = self.marker
            score = self.minimax(board, False)
            board.board[row][col] = ''
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, board, is_maximizing):
        winner = board.check_win()
        if winner == self.marker:
            return 1
        elif winner == self.opponent_marker:
            return -1
        elif board.check_draw():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for move in board.available_moves():
                row, col = move
                board.board[row][col] = self.marker
                score = self.minimax(board, False)
                board.board[row][col] = ''
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for move in board.available_moves():
                row, col = move
                board.board[row][col] = self.opponent_marker
                score = self.minimax(board, True)
                board.board[row][col] = ''
                best_score = min(best_score, score)
            return best_score

class DefaultOpponent(Player):
    def __init__(self, marker):
        super().__init__(marker)

    def get_move(self, board):
        # 1. Check for a winning move.
        for move in board.available_moves():
            row, col = move
            board.board[row][col] = self.marker
            if board.check_win() == self.marker:
                board.board[row][col] = ''
                return move
            board.board[row][col] = ''
        
        # 2. Check for a blocking move.
        opponent_marker = 'O' if self.marker == 'X' else 'X'
        for move in board.available_moves():
            row, col = move
            board.board[row][col] = opponent_marker
            if board.check_win() == opponent_marker:
                board.board[row][col] = ''
                return move
            board.board[row][col] = ''
        
        # 3. Otherwise, choose a random move.
        return random.choice(board.available_moves())

class AlphaBetaAIPlayer(Player):
    def __init__(self, marker):
        super().__init__(marker)
        self.opponent_marker = 'O' if marker == 'X' else 'X'
        self.algorithm = "Alpha-Beta Pruning"

    def get_move(self, board):
        best_score = -float('inf')
        best_move = None
        alpha = -float('inf')
        beta = float('inf')
        for move in board.available_moves():
            row, col = move
            board.board[row][col] = self.marker
            score = self.minimax_ab(board, False, alpha, beta)
            board.board[row][col] = ''
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
        return best_move

    def minimax_ab(self, board, is_maximizing, alpha, beta):
        winner = board.check_win()
        if winner == self.marker:
            return 1
        elif winner == self.opponent_marker:
            return -1
        elif board.check_draw():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for move in board.available_moves():
                row, col = move
                board.board[row][col] = self.marker
                score = self.minimax_ab(board, False, alpha, beta)
                board.board[row][col] = ''
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in board.available_moves():
                row, col = move
                board.board[row][col] = self.opponent_marker
                score = self.minimax_ab(board, True, alpha, beta)
                board.board[row][col] = ''
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
