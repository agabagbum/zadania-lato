def expected_operations(N, a):
    dp = [[[0.0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]

    for x1 in range(N + 1):
        for x2 in range(N + 1):
            for x3 in range(N + 1):
                if x1 == 0 and x2 == 0 and x3 == 0:
                    continue
                total_dishes = x1 + x2 + x3
                dp[x1][x2][x3] = N / total_dishes
                if x1 > 0:
                    dp[x1][x2][x3] += (x1 / total_dishes) * dp[x1-1][x2][x3]
                if x2 > 0:
                    dp[x1][x2][x3] += (x2 / total_dishes) * dp[x1+1][x2-1][x3]
                if x3 > 0:
                    dp[x1][x2][x3] += (x3 / total_dishes) * dp[x1][x2+1][x3-1]

    x1 = a.count(1)
    x2 = a.count(2)
    x3 = a.count(3)

    return dp[x1][x2][x3]

N = 3
a = [1, 2, 3]
print(expected_operations(N, a)) 