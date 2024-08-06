MOD = 10**9 + 7

def count_paths(H, W, grid):
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[1][1] = 1
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i-1][j-1] == '.':
                if i > 1:
                    dp[i][j] += dp[i-1][j]
                if j > 1:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    
    return dp[H][W]


H = 3
W = 3
grid = [
    ['.', '.', '.'],
    ['.', '#', '.'],
    ['.', '.', '.']
]

print(count_paths(H, W, grid))
