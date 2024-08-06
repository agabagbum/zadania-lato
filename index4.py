def determine_winner(N, K, A):
    dp = [False] * (K + 1)

    dp[0] = False  


    for k in range(1, K + 1):
        for a in A:
            if k >= a and not dp[k - a]:
                dp[k] = True
                break

 
    return "First" if dp[K] else "Second"

N = int(input())
K = int(input())
A = list(map(int, input().split()))
print(determine_winner(N, K, A))        
