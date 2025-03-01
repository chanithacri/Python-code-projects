def available_moves_board(self, board):
    """Return a list of indices for all empty cells in the board."""
    return [i for i, cell in enumerate(board) if cell == ""]

def is_winner_board(self, board, mark):
    """Check if the given mark ('X' or 'O') has won on the provided board."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == mark for i in condition):
            return True
    return False

def minimax(self, board, is_maximizing):
    """
    The minimax function for Tic-Tac-Toe.
    
    Parameters:
      board (list): A list representing the board state (with "" for empty cells).
      is_maximizing (bool): True if the current move is for the computer (maximizing),
                            False if for the human (minimizing).
    
    Returns:
      A tuple (best_move, score) where best_move is the index of the best move and
      score is the evaluation of that move.
    """
    # Terminal conditions
    if self.is_winner_board(board, "O"):
        return None, 1   # Computer wins
    if self.is_winner_board(board, "X"):
        return None, -1  # Human wins
    if not any(cell == "" for cell in board):
        return None, 0   # Draw

    if is_maximizing:
        best_score = -float("inf")
        best_move = None
        for move in self.available_moves_board(board):
            board[move] = "O"  # Try the computer's move.
            _, score = self.minimax(board, False)
            board[move] = ""   # Undo the move.
            if score > best_score:
                best_score = score
                best_move = move
        return best_move, best_score
    else:
        best_score = float("inf")
        best_move = None
        for move in self.available_moves_board(board):
            board[move] = "X"  # Try the human's move.
            _, score = self.minimax(board, True)
            board[move] = ""   # Undo the move.
            if score < best_score:
                best_score = score
                best_move = move
        return best_move, best_score
