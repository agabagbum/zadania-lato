def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Przenieś dysk 1 z {source} do {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Przenieś dysk {n} z {source} do {target}")
    hanoi(n - 1, auxiliary, target, source)

n = int(input("podaj liczbe krążków: "))
hanoi(n, '1', '3', '2')
