
def knightProbability(n: int, k: int, row: int, column: int) -> float:
    moves = [(2,1),(1,2),(-2,1),(1,-2),(2,-1),(-1,2),(-2,-1),(-1,-2)]
    memo = {}

    def dfs(r,c,m):
        # If the knight is off the board, probability is 0
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0
        # If no more moves are left, probability is 1
        if m == 0:
            return 1
        # Check if result is already in the memo, return probability
        if (r,c,m) in memo:
            return memo[(r,c,m)]
        # Explore all the moves
        # Intialize probability
        probab = 0
        for dr, dc in moves:
            probab += dfs(dr+r, dc+c, m-1) / 8
        # Add this probability to memo
        memo[(r,c,m)] = probab
        return probab
    return dfs(row,column,k)

print(knightProbability(n = 3, k = 2, row = 0, column = 0))