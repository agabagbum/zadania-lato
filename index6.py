def is_dosc_ciekawy(s):
    lower = set()
    upper = set()
    
    for char in s:
        if char.islower():
            lower.add(char)
        if char.isupper():
            upper.add(char)
    
    for char in lower:
        if char.upper() not in upper:
            return False
    for char in upper:
        if char.lower() not in lower:
            return False
            
    return True

def find_longest_dosc_ciekawy(s, start, end):
    if start >= end:
        return "" 
       
       
    
    for i in range(start, end):
        char = s[i]
        if (char.islower() and char.upper() not in s[start:end]) or (char.isupper() and char.lower() not in s[start:end]):
            left = find_longest_dosc_ciekawy(s, start, i)
            right = find_longest_dosc_ciekawy(s, i + 1, end)
            
            if len(left) > len(right):
                return left
            elif len(right) > len(left):
                return right
            else:
                return right if s.rfind(right) > s.rfind(left) else left
    
    return s[start:end]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().strip()
    
    result = find_longest_dosc_ciekawy(input, 0, len(input))
    print(result)
