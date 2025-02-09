def solution(nums: list[int]) -> int:
    nums = sorted(list(set(nums)))

    print(nums)
    
    return len(nums)


# Case 1
print("Case 1 result:")
print(f"k = {solution([1,1,2])}")

# Case 2
print("Case 2 result:")
print(f"k = {solution([0,0,1,1,1,2,2,3,3,4])}")

# Case 3
print("Case 3 result:")
print(f"k = {solution([1,1,1,1])}")