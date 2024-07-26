def czyPalindrom(zdanie):
    zdanie = zdanie.lower().replace(" ", "")
    n = len(zdanie)
    for i in range(n//2):
        if zdanie[i] != zdanie[n-1-i]:
            return False
    return True
print('sprawdzenie czy zdanie jest palindromem')
zdanie = input('podaj zdanie:')
print("podane zdanie" + ("jest" if(czyPalindrom(zdanie)) else "nie jest ") + "palindromemlima")