from game import TicTacToeGame
from players import AIPlayer, DefaultOpponent, AlphaBetaAIPlayer
from gui import TicTacToeGUI

def play_game(game_instance, algorithm_desc):
    gui = TicTacToeGUI(game_instance, algorithm_desc)
    gui.start()

def main():
    # First game: non-alpha-beta version (Minimax)
    game1 = TicTacToeGame(AIPlayer('X'), DefaultOpponent('O'))
    play_game(game1, "Minimax")
    
    # After closing the first window, prompt to start the next game.
    input("Press Enter to play with Alpha-Beta Pruning...")
    game2 = TicTacToeGame(AlphaBetaAIPlayer('X'), DefaultOpponent('O'))
    play_game(game2, "Alpha-Beta Pruning")

if __name__ == '__main__':
    main()
