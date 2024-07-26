def maksymalne_zadowlenie(N, aktywnosci):
    dp = [[0] * 3 for _ in range(N + 1)]
    
    dp[1][0] = aktywnosci[0][0]
    dp[1][1] = aktywnosci[0][1]
    dp[1][2] = aktywnosci[0][2]
    
    for i in range(2, N + 1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + aktywnosci[i-1][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + aktywnosci[i-1][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + aktywnosci[i-1][2]
    
    return max(dp[N][0], dp[N][1], dp[N][2])

if __name__ == "__main__":
    N = int(input())
    
    aktywnosci = []
    for _ in range(N):  
        a, b, c = map(int, input().split())
        aktywnosci.append([a, b, c])
    
    result = maksymalne_zadowlenie(N, aktywnosci)
    print(result)
