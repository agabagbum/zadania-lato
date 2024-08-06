def probability_more_heads_than_tails(N, probabilities):
    dp = [[0.0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1.0 

    for i in range(1, N + 1):
        p = probabilities[i-1]
        for j in range(i + 1):
            if j > 0:
                dp[i][j] = dp[i-1][j-1] * p
            dp[i][j] += dp[i-1][j] * (1 - p)

    result = 0.0
    for j in range((N // 2) + 1, N + 1):
        result += dp[N][j]

    return result

N = 3
probabilities = [0.30, 0.60, 0.80]

print(probability_more_heads_than_tails(N, probabilities))
