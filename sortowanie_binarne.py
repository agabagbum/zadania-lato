def serch_history(value, list):

    start = 0 
    end = len(list) - 1
    found = False 
    while start <= end and not found:
        print(f'{start} - {end}')
        midline = (start + end) // 2 
        if list[midline] == value:
            found = True
        else: 
            if value < list[midline]:
                end = midline - 1 
            else:
                start = midline + 1 
    if found:
        return midline
    else:
        return None
