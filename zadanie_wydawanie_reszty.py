def wydaj(n):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    i = 0 
    while n  > 0:
        if n >= nominaly[i]:
            print(n//nominaly[i],'x',nominaly[i],sep='', end=' ')
            n %= nominaly[i] 
        i += 1 


wydaj(int(input("podaj ile potrzeba wydać: ")))
