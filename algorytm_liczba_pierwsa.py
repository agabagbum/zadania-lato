def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <=1:
        return False
    
    pierwsza = int(n**0.5) + 1
    for dzielnik in range(3, pierwsza, 2):
        if n % dzielnik == 0:
            return False 
    return True
print(czy_pierwsza(int(input('podaj liczbe: '))))