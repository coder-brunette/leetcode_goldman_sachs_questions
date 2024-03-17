# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. 
# The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

# A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction,
# then one cell in an orthogonal direction. Each time the knight is to move, it chooses one of eight possible moves 
# uniformly at random (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly k moves or has moved off the chessboard.

# Return the probability that the knight remains on the board after it has stopped moving.

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1), (1, -2), (-2, 1)] 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp_prev = [[0 for _ in range(n)] for _ in range(n)]
        dp_prev[row][column] = 1

        for step in range(k):
            for r in range(n):
                for c in range(n):
                    dp[r][c] = 0
                    for dr, dc in moves:
                        prev_r, prev_c = r - dr, c - dc
                        if 0 <= prev_r < n and 0 <= prev_c < n:
                            dp[r][c] += dp_prev[prev_r][prev_c] / 8.0
            dp, dp_prev = dp_prev, dp 

        total_probability = sum(sum(dp_prev[r][c] for c in range(n)) for r in range(n))
        return total_probability