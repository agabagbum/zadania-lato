numbers = []


for i in range(5):
    number = int(input("podaj liczbę: "))
    numbers.append(number)

print(f"najwieksza liczba {max(numbers)}")
print(f"najmniejsza liczba {min(numbers)}")