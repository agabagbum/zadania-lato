l = []
n = int(input('podaj ilosc liczb'))
for i in range(n):
    l.append(int(input('podaj liczbe ')))
print(l)
min  = l[0]
for i in l:
    if i < min:
        min = i 
print('minimalna wartosc wynosi' , min)
mac = l[0]
for i in l:
    if i > max:
        max = i
print('maksymalna wartosc to', max)