def find_longest_interesting_substring(s):
    def is_interesting(sub):
        lowers = set()
        uppers = set()
        for char in sub:
            if char.islower():
                lowers.add(char)
            if char.isupper():
                uppers.add(char)
        for char in lowers:
            if char.upper() not in uppers:
                return False
        for char in uppers:
            if char.lower() not in lowers:
                return False
        return True

    def longest_interesting_substring(s, start, end):
        if start > end:
            return ""
        
        lowers = set()
        uppers = set()
        for i in range(start, end + 1):
            if s[i].islower():
                lowers.add(s[i])
            if s[i].isupper():
                uppers.add(s[i])
        
        for i in range(start, end + 1):
            if (s[i].islower() and s[i].upper() not in uppers) or (s[i].isupper() and s[i].lower() not in lowers):
                left_substring = longest_interesting_substring(s, start, i - 1)
                right_substring = longest_interesting_substring(s, i + 1, end)
                if len(left_substring) > len(right_substring):
                    return left_substring
                elif len(right_substring) > len(left_substring):
                    return right_substring
                else:
                    return right_substring if start + len(right_substring) > start + len(left_substring) else left_substring

        return s[start:end + 1]

    result = longest_interesting_substring(s, 0, len(s) - 1)
    return result

if __name__ == "__main__":
    import sys
    input_string = sys.stdin.read().strip()
    result = find_longest_interesting_substring(input_string)
    print(result)
 