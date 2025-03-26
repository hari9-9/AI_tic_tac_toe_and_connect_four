from board import TicTacToeBoard
from players import HumanPlayer, AIPlayer, DefaultOpponent

class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = TicTacToeBoard()
        self.players = [player1, player2]
        self.current_player_index = 0
        self.game_over = False
        self.winner = None

    def reset_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.game_over = False
        self.winner = None

    def get_current_player(self):
        return self.players[self.current_player_index]

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play_turn(self, row, col):
        # This method is intended for human moves.
        if self.game_over:
            return
        
        current_player = self.get_current_player()
        if self.board.make_move(current_player.marker, row, col):
            winner = self.board.check_win()
            if winner:
                self.game_over = True
                self.winner = winner
            elif self.board.check_draw():
                self.game_over = True
                self.winner = None
            else:
                self.switch_player()
        # If the move was invalid, do nothing.

    def auto_move(self):
        # For non-human players (AI or default opponent).
        if self.game_over:
            return
        current_player = self.get_current_player()
        move = current_player.get_move(self.board)
        if move:
            row, col = move
            self.board.make_move(current_player.marker, row, col)
            winner = self.board.check_win()
            if winner:
                self.game_over = True
                self.winner = winner
            elif self.board.check_draw():
                self.game_over = True
                self.winner = None
            else:
                self.switch_player()
