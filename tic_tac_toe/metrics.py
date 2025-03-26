import random
from game import TicTacToeGame
from players import DefaultOpponent, AIPlayer, AlphaBetaAIPlayer

def simulate_game(player1, player2):
    """Simulate a single game until completion and return the winner and number of moves."""
    game = TicTacToeGame(player1, player2)
    moves = 0
    while not game.game_over:
        game.auto_move()
        moves += 1
    return game.winner, moves

def simulate_batch(opponent_class, n):
    """
    Simulate n games between DefaultOpponent and the given AI opponent.
    Randomizes the order so that each has a 50% chance to start.
    Returns a dictionary of metrics.
    """
    metrics = {
        'default_wins': 0,
        'ai_wins': 0,
        'draws': 0,
        'total_moves': 0,
        'games': n,
    }

    for _ in range(n):
        if random.random() < 0.5:
            # DefaultOpponent starts: assign 'X' to default
            default_player = DefaultOpponent('X')
            ai_player = opponent_class('O')
            game_players = (default_player, ai_player)
            default_marker = 'X'
        else:
            # AI starts: assign 'X' to the AI, so DefaultOpponent is second with 'O'
            default_player = DefaultOpponent('O')
            ai_player = opponent_class('X')
            game_players = (ai_player, default_player)
            default_marker = 'O'

        game = TicTacToeGame(*game_players)
        moves = 0
        while not game.game_over:
            game.auto_move()
            moves += 1
        metrics['total_moves'] += moves

        winner = game.winner
        if winner is None:
            metrics['draws'] += 1
        elif winner == default_marker:
            metrics['default_wins'] += 1
        else:
            metrics['ai_wins'] += 1

    metrics['avg_moves'] = metrics['total_moves'] / n if n > 0 else 0
    return metrics

def main():
    # Number of games to simulate per matchup.
    n = 10

    # Simulation: DefaultOpponent vs AIPlayer (Minimax)
    print("Simulating DefaultOpponent vs AIPlayer (Minimax)...")
    results_minimax = simulate_batch(AIPlayer, n)
    print("Results (Minimax):")
    print("  DefaultOpponent wins: {}".format(results_minimax['default_wins']))
    print("  AIPlayer wins:         {}".format(results_minimax['ai_wins']))
    print("  Draws:                 {}".format(results_minimax['draws']))
    print("  Average moves per game: {:.2f}".format(results_minimax['avg_moves']))
    print()

    # Simulation: DefaultOpponent vs AlphaBetaAIPlayer (Alpha-Beta Pruning)
    print("Simulating DefaultOpponent vs AlphaBetaAIPlayer (Alpha-Beta Pruning)...")
    results_alphabeta = simulate_batch(AlphaBetaAIPlayer, n)
    print("Results (Alpha-Beta Pruning):")
    print("  DefaultOpponent wins: {}".format(results_alphabeta['default_wins']))
    print("  AlphaBetaAIPlayer wins: {}".format(results_alphabeta['ai_wins']))
    print("  Draws:                 {}".format(results_alphabeta['draws']))
    print("  Average moves per game: {:.2f}".format(results_alphabeta['avg_moves']))

if __name__ == '__main__':
    main()
