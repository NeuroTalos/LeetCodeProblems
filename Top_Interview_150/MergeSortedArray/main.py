def solution(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1 += nums2
    
    nums1 = sorted([i for i in nums1 if i != 0])
    
    print(nums1)


# Case 1
print('Case 1 result:')
solution(nums1=[1,2,3,0,0,0], nums2=[2,5,6], m=3, n=3)

# Case 2
print('Case 2 result:')
solution(nums1=[1], nums2=[], m=1, n=0)

# Case 3
print('Case 3 result:')
solution(nums1=[0], nums2=[1], m=1, n=1)