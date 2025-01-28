def solution(nums: list[int], val: int) -> int:
    nums = [i for i in nums if i != val]

    print(f"Array without val: {nums}")

    return len(nums)


# Case 1
print("k =", solution([3,2,2,3], 3))

# Case 2
print("k =", solution([0,1,2,2,3,0,4,2], 2))