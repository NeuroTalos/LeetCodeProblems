def solution(nums: list[int], target: int) -> list[int]:
    nums_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in nums_dict:
            return [nums_dict[complement], i]
        
        nums_dict[num] = i
        
                
# Case 1
print("Case 1 result:")
print(solution([2, 7, 11 ,15], 9))

# Case 2
print("Case 2 result:")
print(solution([3, 2, 4], 6))

# Case 3
print("Case 3 result:")
print(solution([3, 3], 6))