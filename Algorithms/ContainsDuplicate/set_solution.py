def solution(nums: list[int]) -> bool:
    set_nums = set(nums)

    if len(set_nums) != len(nums):
        return True
    else:
        return False


print("Case 1 result:")
print(solution([1,2,3,1]))

print("Case 2 result:")
print(solution([1,2,3,4]))

print("Case 3 result:")
print(solution([1,1,1,3,3,4,3,2,4,2]))