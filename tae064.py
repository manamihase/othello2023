class taeAI(OthelloAI):
    def __init__(self, depth=7):
        self.face = '⛄'
        self.name = 'テヒョン'
        self.depth = depth

    def move(self, board: np.array, piece: int) -> tuple[int, int]:
        _, best_move = self.negamax(board, piece, self.depth, -float('inf'), float('inf'))
        if best_move not in [(0, 1), (1, 0), (1, 1), (0, 6), (1, 6), (1, 7), (7, 1), (6, 0), (6, 1), (7, 6), (6, 6), (6, 7)]:
            return best_move
        return best_move

    def negamax(self, board, piece, depth, alpha, beta):
        if depth == 0 or not get_valid_moves(board, piece):
            return self.evaluate(board, piece), None

        max_eval = -float('inf')
        best_move = None

        for move in get_valid_moves(board, piece):
            new_board = board.copy()
            new_board[move] = piece
            flipped_stones = flip_stones(new_board, *move, piece)
            for r, c in flipped_stones:
                new_board[r, c] = piece

            eval_, _ = self.negamax(new_board, -piece, depth - 1, -beta, -alpha)
            eval_ = -eval_

            if eval_ > max_eval:
                max_eval = eval_
                best_move = move

            alpha = max(alpha, eval_)
            if alpha >= beta:
                break

        return max_eval, best_move

    def evaluate(self, board, piece):
        # Implement your board evaluation function
        # This is a placeholder; you should replace it with your evaluation logic
        return count_board(board, piece) - count_board(board, -piece)
