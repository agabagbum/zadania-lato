def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    length_of_lcs = L[m][n]

    index = length_of_lcs
    lcs_seq = [""] * (index)

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_seq[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_seq)
X = "zxcvbnm"
Y = "mbhfrcd"
print("Najdłuższy wspólny podciąg to:", lcs(X, Y))

       
