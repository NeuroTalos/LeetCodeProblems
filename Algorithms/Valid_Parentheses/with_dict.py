def solution(s: str) -> bool:
    stack = []
    
    # Словарь для соответствия открывающих и закрывающих скобок
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Проходим по каждому символу строки
    for char in s:
        # Если это закрывающая скобка
        if char in matching_bracket:
            # Пытаемся извлечь из стека последнюю открывающую скобку
            top_element = stack.pop() if stack else None
            
            # Проверяем, совпадает ли она с соответствующей парой
            if top_element != matching_bracket[char]:
                return False
        else:
            # Если это открывающая скобка, добавляем её в стек
            stack.append(char)
    
    # Если стек пуст, значит все скобки были правильно закрыты
    return not stack
                    

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