class TicTacToeBoard:
    def __init__(self):
        self.reset_board()
    
    def reset_board(self):
        # Initialize a 3x3 board with empty strings
        self.board = [['' for _ in range(3)] for _ in range(3)]
    
    def make_move(self, player, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
    
    def is_valid_move(self, row, col):
        return self.board[row][col] == ''
    
    def available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    moves.append((i, j))
        return moves
    
    def check_win(self):
        # Check rows for a win
        for row in self.board:
            if row[0] != '' and row[0] == row[1] == row[2]:
                return row[0]
        
        # Check columns for a win
        for col in range(3):
            if self.board[0][col] != '' and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]
        
        # Check diagonals for a win
        if self.board[0][0] != '' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != '' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        
        return None
    
    def check_draw(self):
        # If there's no winner and no available moves, it's a draw
        return self.check_win() is None and not self.available_moves()
    
    def __str__(self):
        # Represent the board as a string for debugging
        rows = []
        for row in self.board:
            rows.append(" | ".join([cell if cell else " " for cell in row]))
        return "\n-----\n".join(rows)
