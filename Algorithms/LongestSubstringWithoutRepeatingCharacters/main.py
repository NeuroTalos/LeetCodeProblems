def solution(s: str) -> int:
    max_length = 0
    pass_symbols = {}
    start = 0 

    for i in range(len(s)):
        if s[i] in pass_symbols and pass_symbols[s[i]] >= start:
            start = pass_symbols[s[i]] + 1
        
        pass_symbols[s[i]] = i
        
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Case 1
print("Case 1 result:")
print(solution("abcabcbb"))

# Case 2
print("Case 2 result:")
print(solution("bbbbb"))

# Case 3
print("Case 3 result:")
print(solution("pwwkew"))