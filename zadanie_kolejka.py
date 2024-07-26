p, d = map(int, input().split())

students = []

for _ in range(d):
    n = int(input())
    
    for _ in range(n):
        x, s = input().split()
        x = int(x)
        s = float(s)
        students.append((s, x))
    
    students.sort()
    
    accepted = []
    for _ in range(p):
        if students:
            accepted.append(students.pop(0)[1])
    
    print(" ".join(map(str, accepted)))
