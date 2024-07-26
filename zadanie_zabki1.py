def minimalny_koszt_skokow(N, h):
    dp = [0] * N
    
    dp[0] = 0
    
    if N > 1:
        dp[1] = abs(h[1] - h[0])
    
    for i in range(2, N):
        koszt_skoku_na_i_1 = dp[i-1] + abs(h[i] - h[i-1])
        koszt_skoku_na_i_2 = dp[i-2] + abs(h[i] - h[i-2])
        dp[i] = min(koszt_skoku_na_i_1, koszt_skoku_na_i_2)
    
    return dp[N-1]

N = int(input("Podaj liczbę kamieni (N): "))
h = list(map(int, input("Podaj wysokości kamieni oddzielone spacjami: ").split()))

if len(h) != N:
    print("Liczba podanych wysokości nie zgadza się z liczbą kamieni (N).")
else:
    wynik = minimalny_koszt_skokow(N, h)
    print("Minimalny koszt skoków: ", wynik)
