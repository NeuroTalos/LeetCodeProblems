def solution(nums: list[int]) -> int:
    i = 0 
    length = len(nums)

    while i < length:
        value_count = nums.count(nums[i])

        if value_count > 2:
            for c in range(value_count - 2):
                nums.remove(nums[i])

            i = i-1
            length = len(nums)

        i += 1
        
    
    print(nums)
    
    return len(nums)


print(solution([1,1,1,2,2,3]))

print(solution([0,0,1,1,1,1,2,3,3]))

print(solution([1,1,1,1,1,1,1,1,1,1,1]))
