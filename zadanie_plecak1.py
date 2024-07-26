print("aby program zadziałał musisz najpierw podać ile rzeczy musimy sprawdzic i wage plecaka potem podaj wage plecaka a potem wartosc")
def plecak(N, W, rzeczy):
    dp = [0] * (W + 1 )
    for weight, value in rzeczy:
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[W]

N, W = map(int, input("podaj wartosci do policzenia: ").split())
rzeczy = [tuple(map(int, input().split())) for _ in range(N)]

result = plecak(N, W, rzeczy)
print(result) 