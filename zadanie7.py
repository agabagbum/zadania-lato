def backpack_greedy(weight, values, total_weight):

    data = []
    for i in range(len(weight)):
        data.append({
            "v": values[i],
            "w": weight[i],
            "cost": float(values[i])/float(weight[i])
        })
    data = sorted(data, key=lambda x: x['cost'], reverse=True)
    print(f'DEBUG: {data}')
    remain = total_weight
    result = 0 
    result_list = []
    i = 0 

    while i < len(data):
        if (data[i]['w'] <= remain):
            remain -= data[i]['w']
            remain += data[i]['v']
            result_list.append(data[i])
            print(f"DEBUG: adding {data[i]} - total value = {result} remain space = {remain}")
        i += 1
    
    return  result, result_list
    