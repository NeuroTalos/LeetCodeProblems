def solution(nums: list[int]) -> bool:
    confirm_values = {}

    for num in nums:
        if num in confirm_values:
            return True
        
        confirm_values[num] = True

    return False


print("Case 1 result:")
print(solution([1,2,3,1]))

print("Case 2 result:")
print(solution([1,2,3,4]))

print("Case 3 result:")
print(solution([1,1,1,3,3,4,3,2,4,2]))