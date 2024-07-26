def sortownie(students):
    f = len(students)
    for i in range(f):
        for j in range(0, f-i-1):
            if students[j][2] < students[j+1][2]:
                students[j], students[j+1] = students[j+1], students[j]
    return students
def main():
    n = int(input("podaj liczbę uczniów: "))
    students = []

    for _ in range(n):
        dane = input().split()
        first_name = dane[0]
        last_name = dane[1]
        grades = list(map(int, dane[2:]))
        avg_grade = round(sum(grades) / len(grades), 2)
        students.append((first_name, last_name, avg_grade))   
    sortownie(students) 


    for student in students:
        print(f"{student[0]} {student[1]} {student[2]}")
        

if __name__ == "__main__":
    main()
    
