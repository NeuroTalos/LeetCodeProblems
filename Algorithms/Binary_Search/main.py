def solution(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2 

        if nums[mid] == target: 
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
    


# Case 1
print("Case 1 result:")
print(solution([-1,0,3,5,9,12], 9))

# Case 2
print("Case 2 result:")
print(solution([-1,0,3,5,9,12], 2))