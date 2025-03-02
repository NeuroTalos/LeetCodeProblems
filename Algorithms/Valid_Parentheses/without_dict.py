def solution(s: str) -> bool:
    opens = '({['
    closes = ')}]'

    stek = []
    for symbol in s:
        if symbol in opens:
            stek.append(symbol)
        
        if symbol in closes:
            if len(stek) == 0:
                return False
            else:
                k = stek.pop()
                if (k == opens[0] and symbol == closes[0] or
                    k == opens[1] and symbol == closes[1] or
                    k == opens[2] and symbol == closes[2]):
                    continue
                else:
                    return False
    
    if len(stek) != 0:
        return False
    else:
        return True
                    

# Case 1
print("Case 1 result:")
print(solution("()"))

# Case 2
print("Case 2 result:")
print(solution("()[]{}"))

# Case 3
print("Case 3 result:")
print(solution("(]"))

# Case 4
print("Case 4 result:")
print(solution("([])"))