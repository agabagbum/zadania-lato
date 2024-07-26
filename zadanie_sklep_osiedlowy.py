def dane():
    n = int(input('podaj liczbe prduktów: ').strip())
    produkty = []
    for _ in range(n):
        linia = input().strip().split()
        nazwa = linia[0]
        kod = int(linia[1])
        produkty.append((nazwa, kod))
    tryb_sortowania = int(input().strip())
    return produkty, tryb_sortowania
def sortowanie (produkty, tryb_sortowania):
    for i in range(1, len(produkty)):
        klucz = produkty[i]
        j = i - 1
        if tryb_sortowania == 0:
            while j >= 0 and (produkty[j][0] > klucz[0] or 
                              (produkty[j][0] == klucz[0] and produkty[j][1] > klucz[1])):
                produkty[j + 1] = produkty[j]
                j -= 1
        else:  
            while j >= 0 and (produkty[j][1] < klucz[1] or 
                              (produkty[j][1] == klucz[1] and produkty[j][0] > klucz[0])):
                produkty[j + 1] = produkty[j]
                j -= 1
        produkty[j + 1] = klucz

def main(): 

    produkty, tryb_sortowania = dane()
    sortowanie(produkty, tryb_sortowania)
    for nazwa, kod in produkty:
        print(nazwa, kod)

if __name__ == "__main__":
    main()
