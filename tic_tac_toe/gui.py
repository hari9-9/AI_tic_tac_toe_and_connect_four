import tkinter as tk
from tkinter import messagebox
from game import TicTacToeGame
from players import HumanPlayer

class TicTacToeGUI:
    def __init__(self, game, algorithm_desc=None):
        self.game = game
        self.algorithm_desc = algorithm_desc
        self.window = tk.Tk()
        title = "Tic Tac Toe"
        if algorithm_desc:
            title += " - " + algorithm_desc
        self.window.title(title)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.status_label = None
        self.create_widgets()
        self.window.after(500, self.auto_turn)  # Start automatic turns if needed

    def create_widgets(self):
        # Status label at row 0.
        self.status_label = tk.Label(self.window, text="Player {}'s turn".format(self.game.get_current_player().marker))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Algorithm description label at row 1.
        if self.algorithm_desc:
            algo_label = tk.Label(self.window, text="Current AI Algorithm: " + self.algorithm_desc)
        else:
            algo_label = tk.Label(self.window, text="Current AI Algorithm: N/A")
        algo_label.grid(row=1, column=0, columnspan=3, pady=5)
        
        # Mapping label at row 2.
        p1 = self.game.players[0]
        p2 = self.game.players[1]
        p1_type = "AI" if p1.__class__.__name__ in ["AIPlayer", "AlphaBetaAIPlayer"] else "Default Opponent" if p1.__class__.__name__ == "DefaultOpponent" else "Human"
        p2_type = "AI" if p2.__class__.__name__ in ["AIPlayer", "AlphaBetaAIPlayer"] else "Default Opponent" if p2.__class__.__name__ == "DefaultOpponent" else "Human"
        mapping_text = "X: {} | O: {}".format(p1_type, p2_type)
        mapping_label = tk.Label(self.window, text=mapping_text)
        mapping_label.grid(row=2, column=0, columnspan=3, pady=5)
        
        # Board grid starting at row 3.
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i+3, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        # Reset button at row 6.
        reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
        reset_button.grid(row=6, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        current_player = self.game.get_current_player()
        if not isinstance(current_player, HumanPlayer):
            return
        if self.game.board.is_valid_move(row, col):
            self.game.play_turn(row, col)
            self.update_board()
            self.update_status()
        else:
            messagebox.showwarning("Invalid Move", "That cell is already occupied!")
    
    def auto_turn(self):
        if self.game.game_over:
            self.update_status()
            return
        current_player = self.game.get_current_player()
        if not isinstance(current_player, HumanPlayer):
            self.game.auto_move()
            self.update_board()
            self.update_status()
        if not self.game.game_over:
            self.window.after(500, self.auto_turn)

    def update_board(self):
        for i in range(3):
            for j in range(3):
                marker = self.game.board.board[i][j]
                self.buttons[i][j]['text'] = marker if marker else " "

    def update_status(self):
        if self.game.game_over:
            if self.game.winner:
                status_text = "Player {} wins!".format(self.game.winner)
            else:
                status_text = "It's a draw!"
        else:
            status_text = "Player {}'s turn".format(self.game.get_current_player().marker)
        self.status_label.config(text=status_text)

    def reset_game(self):
        self.game.reset_game()
        self.update_board()
        self.update_status()
        self.window.after(500, self.auto_turn)

    def start(self):
        self.window.mainloop()
