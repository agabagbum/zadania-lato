def backpack_greedy(weight, values, total_weight):
    data = []

    for i in range(len(weight)):
        data.append({
            "v": values[i],
            "w": weight[i],
            "cost": float(values[i]) / float(weight[i])
        })

    data = sorted(data, key=lambda x: x['cost'], reverse=True)
    print(f'{data}')

    remain = total_weight
    result = 0 
    result_list = []
    i = 0 

    while i < len(data):
        if data[i]['w'] <= remain:
            remain -= data[i]['w']
            result += data[i]['v']
            result_list.append(data[i])
            print(f"adding {data[i]} - total value = {result} remain space = {remain}")
        i += 1

    return result, result_list

if __name__ == "__main__":
    weight = list(map(int, input("Podaj wagi przedmiotów oddzielone spacjami: ").split()))
    values = list(map(int, input("Podaj wartości przedmiotów oddzielone spacjami: ").split()))
    total_weight = int(input("Podaj całkowitą wagę plecaka: "))

    result, result_list = backpack_greedy(weight, values, total_weight)
    print(f"Całkowita wartość przedmiotów w plecaku: {result}")
    print("Przedmioty w plecaku:")
    for item in result_list:
        print(item)
