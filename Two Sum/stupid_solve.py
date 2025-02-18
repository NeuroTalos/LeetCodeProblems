def solution(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
                

# Case 1
print("Case 1 result:")
print(solution([2, 7, 11 ,15], 9))

# Case 2
print("Case 2 result:")
print(solution([3, 2, 4], 6))

# Case 3
print("Case 3 result:")
print(solution([3, 3], 6))