def solution(nums: list[int]) -> int:
    majority_element = None

    uniqie_values = set(nums)

    for value in uniqie_values:
        if nums.count(value) > len(nums)/2:
            majority_element = value
            break

    return majority_element


# Case 1
print("Case 1 result:")
print(solution([3,2,3]))

# Case 2
print("Case 2 result:")
print(solution([2,2,1,1,1,2,2]))

# Case 3
print("Case 3 result:")
print(solution([1,2,2,2,1,1,3,3,1,2,2,3,3,3,3,3,3,3,3,3,3,1,1,2,3]))