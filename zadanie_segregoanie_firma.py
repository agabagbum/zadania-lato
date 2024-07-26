n = int(input())
m = int(input())

umowy = []


for _ in range(n):
    first_name, last_name, umowy_num = input().split()
    umowy_num = int(umowy_num)
    umowy.append((first_name, last_name, umowy_num))

for _ in range(m):
    last_name_to_find = input().strip()
    found = False
    for first_name, last_name, contract_num in umowy:
        if last_name == last_name_to_find:
            print(umowy_num)
            found = True
            break
    if not found:
        print(-1)

