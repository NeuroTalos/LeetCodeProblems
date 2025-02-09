def solution(nums):
    max_jump = 0 
    n = len(nums)
    
    for i in range(n):
        if i > max_jump:
            return False
        
        max_jump = max(max_jump, i + nums[i])
        
        if max_jump >= n - 1:
            return True
    
    return False


# Case 1
print("Case 1 result:")
print(solution([2,3,1,1,4]))

# Case 2
print("Case 2 result:")
print(solution([3,2,1,0,4]))

# Case 3
print("Case 3 result:")
print(solution([0]))