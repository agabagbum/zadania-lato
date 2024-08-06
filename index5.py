def optimal_game_result(N, a):
    dp = [[0] * N for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = a[i]
    
    for length in range(2, N + 1):  
        for l in range(N - length + 1):
            r = l + length - 1
            dp[l][r] = max(a[l] - dp[l+1][r], a[r] - dp[l][r-1])
    
    return dp[0][N-1]

N = int(input())
a = list(map(int, input().split()))

print(optimal_game_result(N, a)) 
