def minimalny_koszt_skokow(N, K, h):
    dp = [float('inf')] * N
    dp[0] = 0 

    for i in range(1, N):
        for j in range(1, K+1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

    return dp[N-1]

N = int(input("Podaj liczbę kamieni (N): "))
K = int(input("Podaj maksymalny dystans skoku (K): "))
h = list(map(int, input("Podaj wysokości kamieni oddzielone spacjami: ").split()))
if len(h) != N:
    print("Liczba podanych wysokości nie zgadza się z liczbą kamieni (N).")
else:   
    wynik = minimalny_koszt_skokow(N, K, h)
    print("Minimalny koszt skoków: ", wynik)