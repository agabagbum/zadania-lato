def wartosc(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_chars = set1.intersection(set2)
    return 
def find_longest_substring(s1, s2):
    filtered_s1 = ''.join([ch for ch in s1 if ch in s2])
    
    max_substring = ""
    current_substring = ""
    
    for ch in filtered_s1:
        if ch in s2:
            current_substring += ch
        else:
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            current_substring = ""
    
    if len(current_substring) > len(max_substring):
        max_substring = current_substring
     
    return max_substring

if __name__ == "__main__":
    input_lines = []
    while True:
        try:
            line = input().strip()
            if line:
                input_lines.append(line)
            if len(input_lines) == 2:
                break
        except EOFError:
            break
    
    if len(input_lines) != 2:
        print("Invalid input format. Expected exactly two lines.")
    else:
        s1 = input_lines[0]
        s2 = input_lines[1]
    
        longest_substring = find_longest_substring(s1, s2)
    
        print(longest_substring) 
    
