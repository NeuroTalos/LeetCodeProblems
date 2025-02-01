def solution(nums: list[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
            
    print(nums)


# Case 1
print('Case 1 result:')    
solution([1, 2, 3, 4, 5, 6, 7], 3)

# Case 2
print('Case 2 result:')  
solution([-1,-100,3,99], 2)

# Case 3
print('Case 3 result:')  
solution([1, 2], 3)