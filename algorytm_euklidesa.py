def NWD(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
a = int(input('podaj liczbe a:'))
b = int(input('podaj liczbe b:'))

print("NWD wynosi =", NWD(a, b))
